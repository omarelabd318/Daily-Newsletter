#!/usr/bin/env python3
"""Which desk stocks have new results the desk has not recorded yet, with the figures already read for it.

Usage (from the repo root; run_data.py runs it and puts its output in desk/brief.md):
  python3 .claude/skills/markets-desk/results_due.py [DAYS]

For every desk stock it checks whether results for the latest quarter came out in the last DAYS days (default 10):
- US stocks: the SEC's own list of filings (an earnings release, 8-K item 2.02, or a 10-Q or 10-K), with the
  quarter's revenue, net income and diluted EPS from the SEC's filed figures against a year earlier.
- Egyptian stocks: results headlines in the last DAYS days (Google News, English and Arabic, naming the company),
  with the first three pages read (daily-newsletter/articles.py) and their sentences with figures.
Then, against desk/stocks.json, it lists only the work left: results out but no lastResults written for them, and
for Egyptian stocks lastResults written but set_results.py not run (the P/E still on the old quarter). Stocks
already done are named on one line. The figures are outlets' and the SEC's: take profit attributable to
shareholders from the filing or two outlets that agree before set_results.py, as the skill says.
"""
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "daily-newsletter"))
try:
    import sources
    sources.install()
except Exception:
    pass
import stock_news as sn   # noqa: E402
import articles           # noqa: E402
import run_research       # noqa: E402  (us_filing: the SEC's filings and filed figures)

# a results headline names profit or results, not only sales or a period (contract-sales rankings are not results)
RES = re.compile(r"(results|net profit|profit|earnings|net income|net loss|أرباح|نتائج|خسائر|صافي ربح|القوائم المالية)", re.I)


def quarter_end(d):
    """The last quarter end on or before d minus a week (results never come out the week the quarter ends)."""
    d = d - datetime.timedelta(days=7)
    for m in (12, 9, 6, 3):
        q = datetime.date(d.year, m, 31 if m in (12, 3) else 30)
        if q <= d:
            return q
    return datetime.date(d.year - 1, 12, 31)


def recorded(x, q):
    """lastResults written for quarter q (its date after the quarter end), and the filed figures for q."""
    lr = x.get("lastResults") or {}
    done = bool(lr.get("date")) and lr["date"] > q.isoformat()
    filed = (x.get("filed") or {}).get("period") == q.isoformat()
    return done, filed


def egx_check(t, days):
    """Results headlines naming the company in the last `days` days, newest first, the first three pages read."""
    en, ar = sn.STOCKS[t]
    rows = []
    for qy, arabic in ((en, False), (ar, True)):
        if qy:
            try:
                rows += sn.google(qy, days, arabic)
            except Exception:
                pass
    seen, keep = set(), []
    for r in sorted(rows, key=lambda r: r[0], reverse=True):
        k = re.sub(r"\W+", "", r[2].lower())[:60]
        if k in seen or not RES.search(r[2]) or sn.NOISE.search(r[2]) or not any(m.lower() in r[2].lower() for m in sn.MUST[t]):
            continue
        seen.add(k)
        keep.append(r)
    return keep[:6]


def main(a):
    days = int(a[0]) if a and a[0].isdigit() else 10
    today = datetime.date.today()
    q = quarter_end(today)
    S = json.load(open(os.path.join(ROOT, "desk", "stocks.json")))["stocks"]
    us = [t for t in S if t in run_research.CIK]
    egx = [t for t in S if t in sn.STOCKS and t not in run_research.CIK]
    todo, done, nofile, read = [], [], [], []
    print(f"Results for the quarter to {q}, out in the last {days} days, against desk/stocks.json:\n")
    for t in us:
        wrote, _ = recorded(S[t], q)
        lines = run_research.us_filing(t, today)
        out = not any("no results release" in x for x in lines[:1])
        filed_recent = [x for x in lines if re.search(r"filed (\d{4}-\d{2}-\d{2})", x)
                        and (today - datetime.date.fromisoformat(re.search(r"filed (\d{4}-\d{2}-\d{2})", x).group(1))).days <= days]
        if not out or not filed_recent:
            continue
        (done if wrote else todo).append((t, lines))
    for t in egx:
        wrote, filed = recorded(S[t], q)
        hits = egx_check(t, days)
        if wrote and filed:
            done.append((t, []))
            continue
        if wrote and not filed:
            nofile.append(t)
            continue
        if not hits:
            continue
        pages = articles.read_many([sn.resolve(r[3]) for r in hits[:3]])
        lines = []
        for (w, o, ti, l), pg in zip(hits[:4], pages + [None] * 4):
            lines.append(f"- {w:%a %d %b} | {o} | {ti[:150]}" + (f"\n  {articles.short(pg['url'])}" if pg else ""))
            if pg and not pg["error"]:
                lines.append(f"  > {articles.excerpt(pg['text'], 70, sn.MUST[t])}")
                read.append(pg["url"])
        todo.append((t, lines))
    if todo:
        print("## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py")
        for t, lines in todo:
            print(f"### {t}")
            print("\n".join(x[:700] for x in lines))
        print()
    else:
        print("- No new results waiting: every desk stock that reported in the period is recorded.")
    if nofile:
        print(f"- lastResults written but set_results.py not run, so the P/E is still on the old quarter: {', '.join(nofile)}.")
    if done:
        print(f"- Already recorded: {', '.join(t for t, _ in done)}.")
    if read:
        cairo = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)).date().isoformat()
        articles.log_pages(cairo, "desk", read)


if __name__ == "__main__":
    main(sys.argv[1:])
