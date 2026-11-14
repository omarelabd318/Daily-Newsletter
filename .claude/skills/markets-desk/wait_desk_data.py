#!/usr/bin/env python3
"""Wait for the day's edition and for GitHub Actions' desk data, then pull them: one step of the run, not many.

Usage (from the repo root, at the start of the desk run):
  python3 .claude/skills/markets-desk/wait_desk_data.py DATE [MINUTES]

Checks origin/main every 30 seconds for up to MINUTES (default 9, inside one command's time limit) for:
1. editions/DATE.md or, on a Saturday, editions/DATE-recap.md (the edition whose figures the desk starts from), and
2. desk/run-steps.json dated DATE from GitHub Actions (.github/workflows/desk-data.yml runs run_data.py as soon as
   the edition is pushed, about 10 to 15 minutes, and commits the data files and desk/brief.md).
Then it pulls and prints one line saying which arrived:
- "READY": read desk/brief.md; rerun only the steps it lists as FAILED, with run_data.py NAME (the brief keeps the
  others' output).
- "WAITING": run it again (the skill allows up to 30 minutes in all for the edition, 25 for the data).
- "NO DESK DATA": the edition is in but GitHub Actions has not delivered: run run_data.py yourself, as before.
"""
import datetime
import json
import subprocess
import sys
import time


def sh(*a):
    return subprocess.run(list(a), capture_output=True, text=True)


def state(date):
    sh("git", "fetch", "-q", "origin", "main")
    # the day's edition: DATE.md, or on a Saturday the Weekly Recap, DATE-recap.md
    ed = any(sh("git", "cat-file", "-e", f"origin/main:editions/{date}{x}.md").returncode == 0 for x in ("", "-recap"))
    try:
        S = json.loads(sh("git", "show", "origin/main:desk/run-steps.json").stdout or "{}")
    except ValueError:
        S = {}
    data = S.get("date") == date and any(r.get("where") == "GitHub Actions" for r in S.get("results", []))
    return ed, data, S


def main(a):
    if not a:
        sys.exit(__doc__)
    date = a[0]
    datetime.date.fromisoformat(date)
    minutes = float(a[1]) if len(a) > 1 else 9
    end = time.time() + minutes * 60
    t0 = time.time()
    while True:
        ed, data, S = state(date)
        if (ed and data) or time.time() >= end:
            break
        time.sleep(30)
    if ed or data:
        r = sh("git", "pull", "-q", "--rebase", "--autostash", "origin", "main")
        if r.returncode:
            print("git pull failed: " + r.stderr.strip()[:300])
    waited = round((time.time() - t0) / 60, 1)
    if ed and data:
        bad = [x["name"] for x in S.get("results", []) if not x.get("ok")]
        print(f"READY after {waited} min: the edition and GitHub Actions' desk data are pulled. Read desk/brief.md"
              + (f"; rerun the steps that failed there: run_data.py {' '.join(bad)}" if bad else "; every step ran.") )
    elif ed:
        # the workflow starts when the edition is pushed and takes 10 to 15 minutes
        pushed = sh("git", "log", "-1", "--format=%ct", "origin/main", "--", f"editions/{date}.md", f"editions/{date}-recap.md").stdout.strip()
        age = (time.time() - int(pushed)) / 60 if pushed else 99
        if age < 25:
            print(f"WAITING: the edition is in (pushed {age:.0f} min ago); GitHub Actions' desk data is not yet. Run this again.")
        else:
            print(f"NO DESK DATA: the edition was pushed {age:.0f} min ago and GitHub Actions has not delivered. Run run_data.py yourself.")
    else:
        print(f"WAITING after {waited} min: the edition is not in yet. Run this again (up to 30 minutes in all).")


if __name__ == "__main__":
    main(sys.argv[1:])
