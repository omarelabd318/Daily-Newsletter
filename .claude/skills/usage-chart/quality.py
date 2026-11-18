#!/usr/bin/env python3
"""Word counts and a quality check for each day's newsletter (or Saturday recap) and Markets Desk, so a cost cut
can be checked against what the runs published.

usage: quality.py START END [--baseline-end DATE] [--json]

For every day from START to END it reads what the repo holds (editions/, editions/notes/, desk/days/,
data/research/) and measures:

  Newsletter: words (without Sources), stories (bold lead-ins), source links, distinct outlets, the share of the
              side sessions' facts confirmed at a second outlet (editions/notes: Chk lines not "single source"),
              sections missing against the usual set, checker errors.
  Desk:       words published in the day file, calls (stories), views, whether the flows were confirmed, checker
              errors; stocks researched is shown but not scored (it is light on weekends by design).

Each day is compared with a baseline: the median of the same kind of day (weekday edition, Saturday recap,
weekday desk, Saturday desk) over the 7 days up to --baseline-end (default: the day before START). Set
--baseline-end to the last day before a change (e.g. 2026-11-18 for the Nov 19 cost cuts) to compare every later
day with how the runs were before it.

Score (0-100): the average, over the measures above except words, of the day's figure as a share of the
baseline's (capped at 100%), less 10 for each missing section and 5 for each checker error. Words count only
when they fall below 85% of the baseline (the guides are ceilings, so fewer words is not a fault by itself).
  95 and up: holding;  85-95: watch;  below 85: dropped.
"""
import argparse, datetime as dt, glob, json, os, re, statistics, sys
from urllib.parse import urlparse

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DAILY_SECTIONS = ["Today at a Glance", "Quick Hits", "Weather", "Egypt News", "Top World Headlines",
                  "Regional and Gulf", "Markets", "In Other News", "Stocks Watch", "Currency and Commodities Watch",
                  "Economic Calendar", "Worth Knowing", "Sources"]
RECAP_SECTIONS = ["Since Friday", "The Week in Brief", "Egypt This Week", "Region and World", "Markets This Week",
                  "The Week Ahead", "Sources"]
LEADIN = re.compile(r"^(?:[-*]\s+)?\*\*[^*]{3,90}:\*\*")
URL = re.compile(r"\]\((https?://[^)\s]+)")
SCORED = {"news": ["stories", "links", "outlets", "confirmed"], "desk": ["calls", "views", "flows"]}


def p(*a):
    return os.path.join(ROOT, *a)


def load(path):
    try:
        return json.load(open(path))
    except Exception:
        return None


def newsletter(date):
    d = dt.date.fromisoformat(date)
    key = date if os.path.exists(p("editions", f"{date}.md")) else f"{date}-recap"
    path = p("editions", f"{key}.md")
    if not os.path.exists(path):
        return None
    text = open(path).read()
    body = text.split("\n## Sources")[0]
    heads = re.findall(r"^## (.+)$", text, re.M)
    want = RECAP_SECTIONS if key.endswith("recap") else DAILY_SECTIONS
    urls = set(URL.findall(text))
    m = {"kind": "recap" if key.endswith("recap") else "daily",
         "words": len(re.sub(r"[#*|>\-\[\]()]", " ", re.sub(URL, "", body)).split()),
         "stories": sum(1 for ln in body.splitlines() if LEADIN.match(ln.strip())),
         "links": len(urls),
         "outlets": len({urlparse(u).netloc.removeprefix("www.") for u in urls}),
         "missing": [s for s in want if s not in heads]}
    chk = single = opens = 0
    for f in glob.glob(p("editions", "notes", f"{key}-*.md")):
        t = open(f).read()
        for ln in re.findall(r"^\s*-?\s*Chk:.*$", t, re.M):
            chk += 1
            single += bool(re.search(r"single source|same wording", ln, re.I))
        opens += len(re.findall(r"^\s*-?\s*Open:", t, re.M))
    m["confirmed"] = round(1 - single / chk, 3) if chk else None
    m["open_points"] = opens if chk else None
    r = (load(p("data", "research", f"{date}.json")) or {}).get("recap" if key.endswith("recap") else "newsletter") or {}
    chk_run = r.get("check") or {}
    m["errors"] = len(chk_run.get("errors", [])) if chk_run else None
    m["searches"], m["pages"] = len(r.get("searches", [])) or None, len(r.get("pages", [])) or None
    return m


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in ("url", "src", "source", "date", "key", "id", "ticker", "status", "confidence"):
                yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def desk(date):
    day = load(p("desk", "days", f"{date}.json"))
    if not day:
        return None
    eg, gl = day.get("egypt", {}), day.get("global", {})
    words = sum(len(re.sub(r"<[^>]+>", " ", s).split()) for s in strings([eg, gl, day.get("pages", {})])
                if len(s.split()) > 3)
    r = (load(p("data", "research", f"{date}.json")) or {}).get("desk") or {}
    chk_run = r.get("check") or {}
    flows = eg.get("flows") or {}
    return {"kind": "sat" if dt.date.fromisoformat(date).weekday() == 5 else "daily",
            "words": words,
            "calls": len(eg.get("calls", [])) + len(gl.get("calls", [])),
            "views": len(eg.get("views", [])) + len(gl.get("views", [])),
            "stocks": len(r.get("stocks", {})) or None,
            "flows": None if "confirmed" not in flows else (1.0 if flows["confirmed"] else 0.0),
            "missing": [],
            "errors": len(chk_run.get("errors", [])) if chk_run else None,
            "searches": len(r.get("searches", [])) or None, "pages": len(r.get("pages", [])) or None}


def baseline(fn, date, kind, end, n=7):
    rows = []
    d = dt.date.fromisoformat(end)
    for i in range(n * 2):
        k = (d - dt.timedelta(i)).isoformat()
        if k >= date:
            continue
        m = fn(k)
        if m and m["kind"] == kind:
            rows.append(m)
        if len(rows) >= n:
            break
    out = {}
    for f in ("words", "stocks", *SCORED["news"], *SCORED["desk"]):
        v = [r[f] for r in rows if r.get(f) is not None]
        if v:
            out[f] = statistics.median(v)
    return out


def score(m, base, which):
    if not m:
        return None, []
    parts, low = [], []
    for f in SCORED[which] + ["words"]:
        v, b = m.get(f), base.get(f)
        if v is None or not b:
            continue
        # small counts (calls, views) move by one from day to day: one short of the baseline is not a drop
        ratio = 1.0 if f in ("calls", "views") and v >= b - 1 else min(v / b, 1.0)
        if f == "words":
            if ratio >= 0.85:
                continue
        parts.append(ratio)
        if ratio < 0.85:
            low.append(f"{f} {v:g} vs {b:g}")
    if not parts:
        return None, []
    s = 100 * sum(parts) / len(parts) - 10 * len(m["missing"]) - 5 * (m.get("errors") or 0)
    if m["missing"]:
        low.append("missing: " + ", ".join(m["missing"]))
    if m.get("errors"):
        low.append(f"{m['errors']} checker error(s)")
    return round(max(s, 0)), low


def verdict(s):
    return None if s is None else ("holding" if s >= 95 else "watch" if s >= 85 else "dropped")


def run(start, end, baseline_end=None):
    d0, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    out = {}
    for i in range((d1 - d0).days + 1):
        k = (d0 + dt.timedelta(i)).isoformat()
        be = baseline_end or (dt.date.fromisoformat(k) - dt.timedelta(1)).isoformat()
        row = {}
        for which, fn in (("news", newsletter), ("desk", desk)):
            m = fn(k)
            if not m:
                continue
            base = baseline(fn, k, m["kind"], be)
            s, low = score(m, base, which)
            row[which] = {**m, "score": s, "verdict": verdict(s), "low": low, "baseline": base}
        if row:
            out[k] = row
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("start"); ap.add_argument("end")
    ap.add_argument("--baseline-end")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = run(a.start, a.end, a.baseline_end)
    if a.json:
        print(json.dumps(res, indent=1)); return
    for k, row in res.items():
        for which in ("news", "desk"):
            m = row.get(which)
            if not m:
                continue
            name = ("Recap" if m["kind"] == "recap" else "Newsletter") if which == "news" else "Desk"
            facts = (f"{m['stories']} stories, {m['outlets']} outlets, {m['links']} links, "
                     f"confirmed {m['confirmed']:.0%}" if m.get("confirmed") is not None else
                     f"{m['stories']} stories, {m['outlets']} outlets, {m['links']} links") if which == "news" else \
                    f"{m['calls']} calls, {m['views']} views, {m['stocks']} stocks, flows {'n/a' if m['flows'] is None else 'ok' if m['flows'] else 'unconfirmed'}"
            sc = "  -" if m["score"] is None else f"{m['score']:3d} {m['verdict']}"
            print(f"{k} {name:10s} {m['words']:5d} words  {sc:12s} {facts}" + (f"  LOW: {'; '.join(m['low'])}" if m["low"] else ""))


if __name__ == "__main__":
    main()
