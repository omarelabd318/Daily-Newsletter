#!/usr/bin/env python3
"""One fetch layer under every desk script: retries, pacing, a shared short memory and a health report.

Every fetch script calls urllib.request.urlopen. `install()` wraps that one function, so none of them needs
rewriting, and each gets:
- retries: a network error, a timeout, HTTP 429 or 5xx is tried again (3 tries, waiting 1.5s then 4s, or the
  server's Retry-After up to 20s). A 4xx other than 429 is the site's answer and is not retried.
- pacing: requests to one host are spaced at least 0.3s apart (PACE has the hosts that need more), so a burst
  from one script does not get the next one refused.
- memory: an identical request made again within 15 minutes, by this script or the next one in the same run, is
  answered from a file in the system temp folder (the desk's scripts ask TradingView's screener for the same
  table several times a morning). Nothing is kept between runs: each script already keeps its last saved
  output when a source fails, which is the right fallback for stale data.
- a health line per host (calls, from memory, retried, failed), appended to a JSON-lines file that run_data.py
  reads into the brief, so a flaky source is reported once instead of being investigated by hand.
run_data.py installs it for every step through _site/sitecustomize.py (DESK_SOURCES=1). To use it alone:
`import sources; sources.install()` before any fetch.
"""
import hashlib
import io
import json
import os
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

TTL, TRIES, WAITS = 900, 3, (1.5, 4.0)
PACE = {"default": 0.3, "api.polygon.io": 13.0, "news.google.com": 0.6}
DIR = os.environ.get("DESK_SOURCES_DIR") or os.path.join(tempfile.gettempdir(), "desk-sources")
HEALTH = os.path.join(DIR, "health.jsonl")
_real, _last = urllib.request.urlopen, {}


class Saved(io.BytesIO):
    """A stored answer that reads like urlopen's: read(), status, headers, geturl(), usable in a with-block."""
    def __init__(self, body, url, status=200):
        super().__init__(body)
        self.status, self.code, self.url, self.headers = status, status, url, {}

    def geturl(self):
        return self.url

    def getcode(self):
        return self.status


def _note(host, kind):
    try:
        with open(HEALTH, "a") as f:
            f.write(json.dumps({"host": host, "kind": kind, "script": os.path.basename(os.environ.get("DESK_STEP", "")), "t": round(time.time())}) + "\n")
    except OSError:
        pass


def fetch(req, data=None, timeout=40, **kw):
    if isinstance(req, str):
        req = urllib.request.Request(req, data=data)
    body = req.data if req.data is not None else data
    url, host = req.full_url, urllib.parse.urlsplit(req.full_url).hostname or ""
    key = hashlib.sha1((req.get_method() + url).encode() + (body or b"")).hexdigest()
    path = os.path.join(DIR, key)
    if os.path.exists(path) and time.time() - os.path.getmtime(path) < TTL:
        _note(host, "memory")
        return Saved(open(path, "rb").read(), url)
    err = None
    for i in range(TRIES):
        gap = PACE.get(host, PACE["default"]) - (time.time() - _last.get(host, 0))
        if gap > 0:
            time.sleep(gap)
        _last[host] = time.time()
        try:
            with _real(req, data=data, timeout=timeout, **kw) as r:
                out = r.read()
            if len(out) < 8_000_000:
                tmp = path + ".part%d" % os.getpid()
                open(tmp, "wb").write(out)
                os.replace(tmp, path)
            _note(host, "ok" if i == 0 else "retried")
            return Saved(out, url, getattr(r, "status", 200))
        except urllib.error.HTTPError as e:
            err = e
            if e.code != 429 and e.code < 500:
                break
            wait = min(20.0, float(e.headers.get("Retry-After") or 0) or WAITS[min(i, len(WAITS) - 1)])
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
            err, wait = e, WAITS[min(i, len(WAITS) - 1)]
        if i < TRIES - 1:
            time.sleep(wait)
    _note(host, "failed")
    raise err


def install():
    os.makedirs(DIR, exist_ok=True)
    if urllib.request.urlopen is not fetch:
        urllib.request.urlopen = fetch


def health(since=0):
    """{host: {"ok", "memory", "retried", "failed"}} from the health file, for calls after `since`."""
    out = {}
    try:
        for line in open(HEALTH):
            x = json.loads(line)
            if x["t"] >= since:
                h = out.setdefault(x["host"], {"ok": 0, "memory": 0, "retried": 0, "failed": 0, "scripts": []})
                h[x["kind"]] += 1
                if x["kind"] == "failed" and x["script"] not in h["scripts"]:
                    h["scripts"].append(x["script"])
    except OSError:
        pass
    return out


if __name__ == "__main__":
    # self-check, against a local server: a 500 then a 200 is retried; a 404 is not; a repeat comes from memory
    import http.server
    import threading
    hits = {"n": 0}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            hits["n"] += 1
            code = 404 if self.path == "/missing" else 500 if self.path == "/flaky" and hits["n"] == 1 else 200
            self.send_response(code)
            self.end_headers()
            self.wfile.write(b"hello" if code == 200 else b"")

        def log_message(self, *a):
            pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    DIR = tempfile.mkdtemp()
    HEALTH = os.path.join(DIR, "health.jsonl")
    WAITS = (0.05, 0.05)
    install()
    base = "http://127.0.0.1:%d" % srv.server_port
    assert urllib.request.urlopen(base + "/flaky", timeout=5).read() == b"hello" and hits["n"] == 2
    assert urllib.request.urlopen(base + "/flaky", timeout=5).read() == b"hello" and hits["n"] == 2      # memory
    try:
        urllib.request.urlopen(base + "/missing", timeout=5)
        raise SystemExit("a 404 should raise")
    except urllib.error.HTTPError as e:
        assert e.code == 404 and hits["n"] == 3                                                          # one try only
    h = health()["127.0.0.1"]
    assert (h["retried"], h["memory"], h["failed"]) == (1, 1, 1), h
    print("sources: retry, memory and failure checks pass")
