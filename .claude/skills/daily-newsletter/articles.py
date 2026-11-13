#!/usr/bin/env python3
"""Read news pages without the run opening them one by one: each page's own text, cut to the lines that matter.

Usage (from the repo root):
  python3 .claude/skills/daily-newsletter/articles.py [--words N] [--full] [--about WORD,WORD] [--log DATE PART] URL [URL ...]

Reads every URL at once (Google News links are resolved to the outlet's own page first) and prints, per page: the
outlet's link, then the opening and every sentence with a figure (or naming one of --about), up to N words (default
120; --full prints up to 700). A page that will not load, or is too short to be the story (a paywall, a cookie wall),
is named so it can be opened by hand. --log records the pages that were read in the day's research log
(research_log.py; PART is newsletter or desk), as read_enterprise.py does.

Use it in place of opening pages one at a time: five URLs in one command are one step of the run, not five.
run_research.py (editions/articles.md) and the desk's stock_news.py use the same reader. The text is the outlet's
own words; check a figure that moves a story against a second outlet, as always.
"""
import concurrent.futures
import html
import os
import re
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
SHORT = 70   # fewer words than this is not the story (a paywall, a consent page, a video page)
_traf = None
_OPENER = urllib.request.build_opener()


def _extractor():
    """trafilatura when it is installed (or can be: one pip install, a few seconds), else a plain paragraph reader."""
    global _traf
    if _traf is None:
        try:
            import trafilatura
            _traf = trafilatura
        except ImportError:
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", "-q", "trafilatura"], capture_output=True, timeout=180)
                import trafilatura
                _traf = trafilatura
            except Exception:
                _traf = False
    return _traf


def _plain(page):
    page = re.sub(r"<(script|style|nav|header|footer|aside|form)[^>]*>.*?</\1>|<!--.*?-->", " ", page, flags=re.S | re.I)
    paras = [html.unescape(re.sub(r"<[^>]+>", "", p)).strip() for p in re.findall(r"<p[^>]*>(.*?)</p>", page, re.S | re.I)]
    return "\n".join(p for p in paras if len(p.split()) >= 8)


def short(url):
    """The link as people read it: Arabic addresses decoded from %D8%A7... (a third the length, the same page)."""
    import urllib.parse
    try:
        return urllib.parse.unquote(url)
    except Exception:
        return url


def resolve(link):
    if "news.google.com" not in link:
        return link
    sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "markets-desk"))
    import stock_news
    return stock_news.resolve(link)


def read(url):
    """{"url", "text", "words", "error"}: the page's article text (the outlet's own words, no menus or ads)."""
    url = resolve(url)
    out = {"url": url, "text": "", "words": 0, "error": None}
    if "news.google.com" in url:
        out["error"] = "Google's link could not be resolved to the outlet's page"
        return out
    try:
        # its own opener, not urlopen: news sites refusing a reader (paywalls) are not data sources failing, so they
        # stay out of sources.py's retries and health report
        r = _OPENER.open(urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en,ar;q=0.8"}), timeout=20)
        raw = r.read(3_000_000)
        h = getattr(r, "headers", None)   # sources.py's saved answers carry a plain dict here
        cs = (h.get_content_charset() if hasattr(h, "get_content_charset") else None) or \
            (re.search(rb'charset=["\']?([\w-]+)', raw[:3000]) or [None, b"utf-8"])[1].decode()
        page = raw.decode(cs, "replace")
    except Exception as e:
        out["error"] = f"did not load ({getattr(e, 'code', None) or type(e).__name__})"
        return out
    t = _extractor()
    text = ""
    if t:
        try:
            text = t.extract(page, include_comments=False, include_tables=True, favor_precision=True) or ""
        except Exception:
            text = ""
    if not text:
        text = _plain(page)
    out["text"], out["words"] = text.strip(), len(text.split())
    if out["words"] < SHORT:
        out["error"] = f"only {out['words']} words came back (a paywall or a page the reader cannot see): open it by hand if it matters"
    return out


def read_many(urls, threads=8):
    with concurrent.futures.ThreadPoolExecutor(threads) as pool:
        return list(pool.map(read, urls))


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?؟؛])\s+|\n+", text) if len(s.strip().split()) >= 4]


def excerpt(text, words=120, about=()):
    """The opening sentence or two, then every sentence with a figure or naming one of `about`, in the page's order,
    up to `words`. Whole sentences only."""
    ss = sentences(text)
    if not ss:
        return ""
    lower = [w.lower() for w in about if w]
    keep, seen, n = [], set(), 0
    for i, s in enumerate(ss):
        hit = i < 2 or re.search(r"\d", s) or any(w in s.lower() for w in lower)
        key = re.sub(r"\W+", "", s)[:80]
        if not hit or key in seen:
            continue
        seen.add(key)
        w = len(s.split())
        if n + w > words and keep:
            break
        keep.append(s if w <= words else " ".join(s.split()[:words]) + " ...")
        n += w
    return " ".join(keep)


def names(text, about):
    """Whether the page names any of `about` at all (a lead whose page never names the company is not about it)."""
    low = text.lower()
    return any(w.lower() in low for w in about if w)


def log_pages(date, part, urls):
    if not urls:
        return
    try:
        subprocess.run([sys.executable, os.path.join(HERE, "research_log.py"), date, part, "page", *urls],
                       cwd=ROOT, capture_output=True, timeout=30)
    except Exception:
        pass


def main(a):
    words, full, about, log, urls = 120, False, (), None, []
    i = 0
    while i < len(a):
        x = a[i]
        if x == "--words":
            words, i = int(a[i + 1]), i + 1
        elif x == "--full":
            full = True
        elif x == "--about":
            about, i = tuple(a[i + 1].split(",")), i + 1
        elif x == "--log":
            log, i = (a[i + 1], a[i + 2]), i + 2
        elif x.startswith("http"):
            urls.append(x)
        i += 1
    if not urls:
        sys.exit(__doc__)
    got = read_many(urls)
    for g in got:
        print(f"## {short(g['url'])}")
        if g["error"]:
            print(f"- {g['error']}\n")
            continue
        body = " ".join(g["text"].split()[:700]) if full else excerpt(g["text"], words, about)
        print(f"({g['words']} words on the page)\n{body}\n")
    if log:
        log_pages(log[0], log[1], [g["url"] for g in got if not g["error"]])


if __name__ == "__main__":
    main(sys.argv[1:])
