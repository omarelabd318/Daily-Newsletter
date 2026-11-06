#!/usr/bin/env python3
"""Save the week of prices behind an edition's "Last 7 days" lines (data/weeks/DATE.json).

Usage (from the repo root, after the day's figures are logged):
  python3 .claude/skills/markets-desk/fetch_intraday.py      # brings desk/intraday.json up to the last session
  python3 .claude/skills/daily-newsletter/week_snapshot.py DATE

Keeps, from desk/intraday.json's "week", the sessions before DATE (the closes the edition shows) for the EGX30, the
Nasdaq Composite, the S&P 500, the Dow and the desk's stocks, one price an hour plus each session's last, so every
edition keeps its own detailed week however the intraday file changes later. About 15 KB a day. The site draws the
Stocks Watch lines from it, and falls back to daily closes for anything it lacks.
"""
import datetime
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SRC = os.path.join(ROOT, "desk", "intraday.json")
OUT = os.path.join(ROOT, "data", "weeks")


def hourly(points):
    """On the hour, plus the session's first and last prices."""
    if not points:
        return []
    keep = [p for i, p in enumerate(points) if i == 0 or i == len(points) - 1 or str(p[0]).endswith(":00")]
    return [[t, round(v, 4)] for t, v in keep]


def main(a):
    if len(a) != 1:
        sys.exit(__doc__)
    date = a[0]
    datetime.date.fromisoformat(date)
    W = (json.load(open(SRC)).get("week") or {})
    out = {"date": date, "note": "Each market's sessions before the edition's date, one price an hour (local exchange time)."}
    for mk in ("egx", "us"):
        sess = [w for w in W.get(mk, []) if w["session"] < date]
        out[mk] = [{"session": w["session"], "series": {k: hourly(v) for k, v in (w.get("series") or {}).items() if len(v) >= 2}} for w in sess[-5:]]
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{date}.json")
    with open(path, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"Saved {path}: " + ", ".join(f"{mk} {len(out[mk])} sessions ({out[mk][0]['session'] if out[mk] else '—'} to {out[mk][-1]['session'] if out[mk] else '—'})"
                                          for mk in ("egx", "us")) + f", {os.path.getsize(path) // 1024} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
