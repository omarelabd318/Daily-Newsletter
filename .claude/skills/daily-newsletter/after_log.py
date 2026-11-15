#!/usr/bin/env python3
"""Every chore after log_figures.py, in one call: the six steps the skill's "Log the day's figures" lists.

Usage (from the repo root, once log_figures.py has logged DATE):
  python3 .claude/skills/daily-newsletter/after_log.py DATE [MOVER ...] [--facts-all]

Runs, in order, each with a time limit, carrying on past one that fails:
  1. corporate_actions.py --check        bonus shares or splits past their ex-date (the run applies one by hand)
  2. fill_gaps.py DATE 10 --write        figures missing from the last ten entries, filled from dated sources
  3. fetch_intraday.py                   the desk's intraday prices up to the last session
  4. week_snapshot.py DATE               data/weeks/DATE.json, the edition's "Last 7 days" lines
  5. market_facts.py DATE                only its NOTABLE lines (--facts-all for every item)
  6. tables.py DATE [MOVER ...]          Stocks Watch and Currency and Commodities Watch, ready to paste

Output is cut to what needs the run's attention: step 1's finding, step 2's filled values and MANUAL lines, the
last lines of steps 3 and 4, the notable facts and the two tables in full. Ends with a line per step: ok or FAILED.
A failed step can be rerun on its own with the command it prints.
"""
import os
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
NL = ".claude/skills/daily-newsletter"
DESK = ".claude/skills/markets-desk"


def run(cmd, limit):
    try:
        p = subprocess.run([sys.executable] + cmd, cwd=ROOT, capture_output=True, text=True, timeout=limit)
        return p.returncode == 0, (p.stdout + ("\n" + p.stderr if p.returncode else "")).strip()
    except subprocess.TimeoutExpired:
        return False, f"timed out after {limit}s"


def main(a):
    if not a or a[0].startswith("-"):
        print(__doc__)
        sys.exit(2)
    date, movers = a[0], [x for x in a[1:] if not x.startswith("--")]
    facts_all = "--facts-all" in a
    steps = [
        ("bonus shares", [f"{NL}/corporate_actions.py", "--check"], 120,
         lambda out: [l for l in out.splitlines() if "feed failed" not in l][-6:]),
        ("gaps", [f"{NL}/fill_gaps.py", date, "10", "--write"], 240,
         lambda out: [l for l in out.splitlines() if l.strip()][-25:]),
        ("intraday", [f"{DESK}/fetch_intraday.py"], 300, lambda out: out.splitlines()[-3:]),
        ("week snapshot", [f"{NL}/week_snapshot.py", date], 60, lambda out: out.splitlines()[-2:]),
        ("market facts", [f"{NL}/market_facts.py", date], 60,
         lambda out: out.splitlines() if facts_all else ([l for l in out.splitlines() if "NOTABLE" in l] or ["(nothing notable)"])),
        ("tables", [f"{NL}/tables.py", date] + movers, 120, lambda out: out.splitlines()),
    ]
    status = []
    for name, cmd, limit, cut in steps:
        ok, out = run(cmd, limit)
        print(f"\n## {name}{'' if ok else ' — FAILED'}")
        lines = cut(out) if ok else out.splitlines()[-12:]
        print("\n".join(lines) if lines else "(no output)")
        status.append((name, ok, "python3 " + " ".join(cmd)))
    print("\n## Steps")
    for name, ok, cmd in status:
        print(f"{'ok    ' if ok else 'FAILED'} {name}" + ("" if ok else f": rerun with {cmd}"))
    sys.exit(0 if all(ok for _, ok, _ in status) else 1)


if __name__ == "__main__":
    main(sys.argv[1:])
