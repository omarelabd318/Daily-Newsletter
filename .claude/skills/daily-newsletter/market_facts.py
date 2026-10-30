#!/usr/bin/env python3
"""Compute context facts for an edition from data/markets.json.

Usage:
  python3 .claude/skills/daily-newsletter/market_facts.py DATE            # readable report
  python3 .claude/skills/daily-newsletter/market_facts.py DATE --ytd      # just the YTD % per item
  python3 .claude/skills/daily-newsletter/market_facts.py DATE --year     # year-in-numbers table

Run it after log_figures.py, so DATE's own figures are included. For every logged item it reports the
latest value, change today, month to date, year to date, the 52-week high and low and how far it is from
them, any run of consecutive up or down days, and "highest/lowest since" when that reaches back at least
three months. Items flagged NOTABLE are worth a line in the edition.
"""
import datetime
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
NAMES = {"usd_egp": "USD/EGP", "eur_egp": "EUR/EGP", "sar_egp": "SAR/EGP", "aed_egp": "AED/EGP",
         "kwd_egp": "KWD/EGP", "qar_egp": "QAR/EGP", "gbp_egp": "GBP/EGP", "dxy": "US dollar index",
         "gold21_egp": "Gold 21K", "gold24_egp": "Gold 24K", "gold18_egp": "Gold 18K",
         "goldpound_egp": "Gold pound", "gold_usd": "Gold ($/oz)",
         "brent": "Brent", "egx30": "EGX30", "sp500": "S&P 500", "nasdaq": "Nasdaq", "dow": "Dow Jones", "btc": "Bitcoin"}


def series(days, upto):
    out = {}
    for d in days:
        if d["date"] > upto:
            break
        for k, v in d.items():
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                out.setdefault(NAMES.get(k, k), []).append((d["date"], float(v)))
        for group in ("egx", "us"):
            for t, v in (d.get(group) or {}).items():
                out.setdefault(t, []).append((d["date"], float(v)))
    return out


def pct(a, b):
    return (a / b - 1) * 100 if b else None


def since(pts, before):
    """Last value on or before the date `before` (a value filed under that edition date)."""
    prior = [v for d, v in pts if d <= before]
    return prior[-1] if prior else None


def facts(name, pts, upto):
    date, last = pts[-1]
    if date != upto:
        return None
    y, m = int(upto[:4]), int(upto[5:7])
    prev = pts[-2][1] if len(pts) > 1 else None
    ytd_base = since(pts, f"{y}-01-01")
    mtd_base = since(pts, f"{y}-{m:02d}-01")
    cut = (datetime.date.fromisoformat(upto) - datetime.timedelta(days=365)).isoformat()
    year = [v for d, v in pts if d >= cut]
    hi, lo = max(year), min(year)
    # consecutive moves in the same direction, ignoring unchanged days
    vals = [v for _, v in pts]
    streak, direction = 0, 0
    for a, b in zip(reversed(vals[:-1]), reversed(vals[1:])):
        step = (b > a) - (b < a)
        if step == 0:
            continue
        if direction == 0:
            direction = step
        if step != direction:
            break
        streak += 1
    # highest / lowest since
    note_since = None
    earlier = pts[:-1]
    higher = [d for d, v in earlier if v >= last]
    lower = [d for d, v in earlier if v <= last]
    for label, hits in (("highest", higher), ("lowest", lower)):
        ref = hits[-1] if hits else (earlier[0][0] if earlier else None)
        if ref and (datetime.date.fromisoformat(upto) - datetime.date.fromisoformat(ref)).days >= 90:
            note_since = (label, ref if hits else None)
    return {
        "name": name, "last": last, "day": pct(last, prev) if prev else None,
        "mtd": pct(last, mtd_base) if mtd_base else None,
        "ytd": pct(last, ytd_base) if ytd_base else None,
        "hi": hi, "lo": lo, "from_hi": pct(last, hi), "from_lo": pct(last, lo),
        "streak": streak * direction, "since": note_since,
    }


def fmt(x):
    return "n/a" if x is None else f"{x:+.1f}%"


def main(args):
    if not args:
        sys.exit(__doc__)
    upto = args[0]
    days = json.load(open(os.path.join(ROOT, "data", "markets.json")))["days"]
    data = series(days, upto)
    rows = [f for f in (facts(n, p, upto) for n, p in data.items() if p) if f]
    if not rows:
        sys.exit(f"No figures logged for {upto}; run log_figures.py first.")
    if "--ytd" in args:
        for f in rows:
            print(f"{f['name']}: {fmt(f['ytd'])}")
        return
    if "--year" in args:
        print("| Item | Start of year | End of year | Change |\n|---|---|---|---|")
        for n, p in data.items():
            base = since(p, f"{upto[:4]}-01-01")
            if base and p[-1][0] == upto:
                print(f"| {n} | {base:,.2f} | {p[-1][1]:,.2f} | {fmt(pct(p[-1][1], base))} |")
        return
    for f in rows:
        notes = []
        if f["from_hi"] is not None and f["from_hi"] > -3:
            notes.append(f"within {abs(f['from_hi']):.1f}% of its 52-week high ({f['hi']:,.2f})")
        if f["from_lo"] is not None and f["from_lo"] < 3:
            notes.append(f"within {f['from_lo']:.1f}% of its 52-week low ({f['lo']:,.2f})")
        if abs(f["streak"]) >= 4:
            notes.append(f"{'up' if f['streak'] > 0 else 'down'} {abs(f['streak'])} sessions in a row")
        if f["since"]:
            label, ref = f["since"]
            notes.append(f"{label} since {ref}" if ref else f"{label} in the whole log")
        flag = "NOTABLE: " + "; ".join(notes) if notes else ""
        print(f"{f['name']}: {f['last']:,.2f} | day {fmt(f['day'])} | MTD {fmt(f['mtd'])} | YTD {fmt(f['ytd'])} | "
              f"52w {f['lo']:,.2f}-{f['hi']:,.2f} ({fmt(f['from_hi'])} from high) {flag}")


if __name__ == "__main__":
    main(sys.argv[1:])
