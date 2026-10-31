#!/usr/bin/env python3
"""Weekly health check of data/markets.json, run by the Saturday recap.

Usage:
  python3 .claude/skills/daily-newsletter/check_log.py DATE [DAYS]

Looks at the DAYS days up to DATE (default 7) and reports: regular editions with no log entry, logged
entries missing a figure that the day before had, and day-on-day moves over 15% (repeated weekend
values are skipped). Prints "Data log OK" when nothing is found. It only reports; fix real problems with
log_figures.py and mention anything left in the recap's Publishing note.
"""
import datetime
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def flat(entry):
    out = {k: v for k, v in entry.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
    for group in ("egx", "us"):
        out.update({f"{group}.{t}": v for t, v in (entry.get(group) or {}).items()})
    return out


def main(args):
    if not args:
        sys.exit(__doc__)
    end = datetime.date.fromisoformat(args[0])
    start = (end - datetime.timedelta(days=int(args[1]) if len(args) > 1 else 7)).isoformat()
    days = json.load(open(os.path.join(ROOT, "data", "markets.json")))["days"]
    editions = json.load(open(os.path.join(ROOT, "editions", "index.json")))["editions"]
    logged = {d["date"]: d for d in days}
    problems = []

    for e in editions:
        if start < e["date"] <= end.isoformat() and not e.get("id", "").endswith("recap") \
                and e["date"] not in logged:
            problems.append(f"{e['date']}: edition published but no figures logged.")

    prev, last = None, {}
    for d in days:
        if d["date"] > end.isoformat():
            break
        cur = flat(d)
        if d["date"] > start and prev and not d.get("seed"):
            # rates that are only set on some days (auctions, decisions) are not expected every day
            missing = sorted(k for k in set(prev) - set(cur) if not k.startswith(("tbill_", "cbe_", "egx_turnover", "infl_", "reserves_", "egx70", "egx30_vol")))
            if missing:
                problems.append(f"{d['date']}: missing {', '.join(missing)} (logged the day before).")
        for k, v in cur.items():
            if d["date"] > start and k in last and last[k] and v != last[k]:
                move = (v / last[k] - 1) * 100
                if abs(move) > 15:
                    problems.append(f"{d['date']}: {k} moved {move:+.1f}% ({last[k]:,.2f} to {v:,.2f}); check it.")
            last[k] = v
        prev = cur

    print("\n".join(problems) if problems else "Data log OK")


if __name__ == "__main__":
    main(sys.argv[1:])
