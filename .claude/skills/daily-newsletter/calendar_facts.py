#!/usr/bin/env python3
"""The dated items the Economic Calendar can start from, out of the repo's own data.

Usage:
  python3 .claude/skills/daily-newsletter/calendar_facts.py [DATE] [DAYS]

Lists, for the DAYS after DATE (defaults: today, 14):
  - Egyptian public holidays and EGX closures (data/holidays.json; "expected" until the government confirms them);
  - results dates and dividends for the desk's stocks (desk/calendar.json, from TradingView; results dates are often
    TradingView's estimate, so write "expected" unless a company announcement confirms them);
  - dates the desk confirmed itself (each stock's "next" in desk/stocks.json).
The calendar still needs the day's research for everything else (central bank meetings, data releases, auctions,
fixtures); this only makes sure the dates already known are in it, and right.
"""
import datetime
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def load(rel):
    try:
        return json.load(open(os.path.join(ROOT, rel)))
    except Exception:
        return {}


def main(a):
    start = datetime.date.fromisoformat(a[0]) if a else datetime.date.today()
    end = start + datetime.timedelta(days=int(a[1]) if len(a) > 1 else 14)
    names = {}
    st = (load("desk/stocks.json").get("stocks") or {})
    rows = []
    for h in load("data/holidays.json").get("days", []):
        d = datetime.date.fromisoformat(h["date"])
        if start <= d <= end:
            rows.append((d, f"{h['name']}" + (" (EGX closed)" if h.get("egx_closed") else "") + (f" [{h.get('status')}]" if h.get("status") else "")))
    cal = load("desk/calendar.json")
    for x in cal.get("items", []):
        d = datetime.date.fromisoformat(x["date"])
        if not start <= d <= end:
            continue
        if x["kind"] == "results":
            q = x.get("period")
            rows.append((d, f"{x['t']} results" + (f" for the quarter to {datetime.date.fromisoformat(q):%b %Y}" if q else "") + (f", {x['time']}" if x.get("time") else "")
                         + " [expected, TradingView]"))
        elif x["kind"] == "split":
            rows.append((d, f"{x['t']} stock split, {x['ratio']} [Polygon]"))
        else:
            rows.append((d, f"{x['t']} goes ex-dividend, {'$' if x.get('cur') == '$' else 'EGP '}{x['amount']} a share" + (f", paid {x['pay']}" if x.get("pay") else "")
                         + (f" [declared {x['declared']}, Polygon]" if x.get("declared") else " [TradingView]")))
    for t, e in st.items():
        for n in e.get("next", []) or []:
            if n.get("date"):
                d = datetime.date.fromisoformat(n["date"])
                if start <= d <= end:
                    rows.append((d, f"{t}: {n['event']} [desk, confirmed]"))
    if not rows:
        print(f"Nothing in the repo's data between {start} and {end}.")
    for d, text in sorted(rows):
        print(f"{d:%a %b} {d.day}: {text}")
    print(f"(desk/calendar.json fetched {cal.get('fetched', 'never')})")


if __name__ == "__main__":
    main(sys.argv[1:])
