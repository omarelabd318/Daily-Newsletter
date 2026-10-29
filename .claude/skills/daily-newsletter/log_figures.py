#!/usr/bin/env python3
"""Record the day's figures in data/markets.json (one entry per edition date).

Usage:
  python3 .claude/skills/daily-newsletter/log_figures.py DATE key=value [key=value ...]

Keys (numbers only; leave out anything not confirmed):
  usd_egp eur_egp sar_egp aed_egp gold21_egp gold_usd brent egx30 sp500 nasdaq btc
  egx.TICKER  for the Egypt Stocks Watch rows, e.g. egx.COMI=120.30
  us.TICKER   for the USA Stocks Watch rows, e.g. us.AAPL=347.10

Running it again for the same DATE updates that entry (keys you pass replace old values; others stay).
It also rewrites data/markets-recent.json, the last 400 days that the site loads.
"""
import datetime
import json
import math
import os
import re
import sys

KEYS = {"usd_egp", "eur_egp", "sar_egp", "aed_egp", "gold21_egp", "gold_usd", "brent",
        "egx30", "sp500", "nasdaq", "btc"}
PATH = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "markets.json")


def write_recent(data, path):
    """The site loads only the last 400 days, kept in data/markets-recent.json beside the full log."""
    cut = (datetime.date.fromisoformat(data["days"][-1]["date"]) - datetime.timedelta(days=400)).isoformat()
    recent = {"note": "The last 400 days of markets.json, for the site. Written by log_figures.py; do not edit.",
              "days": [d for d in data["days"] if d["date"] >= cut]}
    with open(os.path.join(os.path.dirname(path), "markets-recent.json"), "w") as f:
        json.dump(recent, f, separators=(",", ":"))
        f.write("\n")


def main(args):
    if len(args) < 2 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        sys.exit(__doc__)
    try:
        datetime.date.fromisoformat(args[0])
    except ValueError:
        sys.exit(f"Not a real date: {args[0]}")
    date, pairs = args[0], args[1:]
    path = os.path.normpath(PATH)
    data = json.load(open(path)) if os.path.exists(path) else {"days": []}
    entry = next((e for e in data["days"] if e["date"] == date), None)
    if entry is None:
        entry = {"date": date, "egx": {}, "us": {}}
        data["days"].append(entry)
    entry.pop("seed", None)
    for p in pairs:
        k, _, v = p.partition("=")
        try:
            num = float(v.replace(",", ""))
        except ValueError:
            sys.exit(f"Not a number: {p}")
        if not math.isfinite(num):
            sys.exit(f"Not a finite number: {p}")
        m = re.fullmatch(r"(egx|us)\.([A-Z.]{2,6})", k)
        if m:
            entry.setdefault(m.group(1), {})[m.group(2)] = num
        elif k in KEYS:
            entry[k] = num
        else:
            sys.exit(f"Unknown key: {k} (allowed: {', '.join(sorted(KEYS))}, egx.TICKER, us.TICKER)")
    data["days"].sort(key=lambda e: e["date"])
    with open(path, "w") as f:
        json.dump(data, f, indent=1)
        f.write("\n")
    write_recent(data, path)
    print(f"Logged {len(pairs)} figure(s) for {date} in data/markets.json")


if __name__ == "__main__":
    main(sys.argv[1:])
