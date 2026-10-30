#!/usr/bin/env python3
"""Bonus shares and splits for the Egyptian stocks in the data log.

Usage:
  python3 .claude/skills/daily-newsletter/corporate_actions.py --check
      Lists bonus-share distributions and splits (from Mubasher's corporate-actions feed) whose date falls in
      the last 14 days or the next 30, for every Egyptian stock in the log. For one already past, it also
      estimates the ratio from the exchange's reference price on the ex-date (previous close / opening price).
  python3 .claude/skills/daily-newsletter/corporate_actions.py --apply TICKER EXDATE BONUS
      Scales every logged price of TICKER before EXDATE (the first session without the right) by
      1 / (1 + BONUS), and its volumes by 1 + BONUS, so the history reads as if today's share count had always
      applied. BONUS is free shares per share held: 0.25 for one free share for every four, 1 for a 1-for-1
      split. Run it once per distribution, after confirming the ratio in the company's disclosure.

Mubasher's daily history (used for backfills) already adjusts older distributions, but recent ones only
after a delay, and the daily log records prices as traded: so a distribution must be applied here on its
ex-date or the charts show a drop that never happened to holders.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PATH = os.path.join(ROOT, "data", "markets.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read().decode("utf-8", "replace")


def when(s):
    try:
        return datetime.datetime.strptime(s, "%d %B %Y").date()
    except (TypeError, ValueError):
        return None


def reference_ratio(t, ex):
    """Free shares per share implied by the ex-date's reference price, from Mubasher's daily history."""
    page = get(f"https://english.mubasher.info/markets/EGX/stocks/{t}")
    url = re.search(r'data-url="(https://static[^"]*Historical[^"]*)"', page).group(1)
    rows = {l.split(",")[0][:10]: l.split(",") for l in get(url).splitlines() if l[:4].isdigit()}
    ds = sorted(rows)
    after = [d for d in ds if d >= ex.isoformat()]
    if not after:
        return None
    d1 = after[0]
    d0 = ds[ds.index(d1) - 1]
    prev, opening = float(rows[d0][4]), float(rows[d1][1])
    return d1, prev / opening - 1 if opening else None


def check():
    data = json.load(open(PATH))
    tickers = sorted({t for e in data["days"][-30:] for t in (e.get("egx") or {})})
    today = datetime.date.today()
    found = 0
    for t in tickers:
        try:
            rows = json.loads(get(f"https://english.mubasher.info/api/1/corporate-actions?symbol={t}"))["rows"]
        except Exception as e:
            print(f"{t}: feed failed ({e})")
            continue
        seen = set()
        for r in rows:
            if not r.get("url", "").endswith("/" + t) or not re.search(r"bonus|split", r.get("type", ""), re.I):
                continue
            d = when(r.get("effectiveFrom")) or when(r.get("announcedAt"))
            key = (r.get("type"), r.get("effectiveFrom"), r.get("announcedAt"))
            if not d or key in seen or not (today - datetime.timedelta(days=14) <= d <= today + datetime.timedelta(days=30)):
                continue
            seen.add(key)
            found += 1
            line = f"{t}: {r.get('type')}, announced {r.get('announcedAt')}, effective {r.get('effectiveFrom')}"
            if d <= today:
                try:
                    est = reference_ratio(t, d)
                    if est and est[1] and est[1] > 0.01:
                        line += f"; reference price on {est[0]} implies about {est[1]:.4f} free shares per share"
                except Exception:
                    pass
            print(line)
    if not found:
        print("No bonus shares or splits in the last 14 days or the next 30.")


def apply(t, ex, bonus):
    data = json.load(open(PATH))
    f = 1 / (1 + bonus)
    n = 0
    # an entry holds the close of the session before its date, so entries up to the ex-date are pre-distribution
    for e in data["days"]:
        if e["date"] <= ex and t in (e.get("egx") or {}):
            e["egx"][t] = round(e["egx"][t] * f, 4)
            if t in (e.get("vol") or {}):
                e["vol"][t] = int(round(e["vol"][t] / f))
            n += 1
    data["note"] = data["note"].rstrip() + f" {t}: prices before {ex} scaled by 1/{1 + bonus:g} for a bonus distribution."
    with open(PATH, "w") as fh:
        json.dump(data, fh, indent=1)
        fh.write("\n")
    sys.path.insert(0, os.path.dirname(__file__))
    from log_figures import write_recent
    write_recent(data, PATH)
    print(f"{t}: scaled {n} entries before {ex} by {f:.6f}; run export_xlsx.py next.")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--check"]:
        check()
    elif a[:1] == ["--apply"] and len(a) == 4:
        apply(a[1].upper(), datetime.date.fromisoformat(a[2]).isoformat(), float(a[3]))
    else:
        sys.exit(__doc__)
