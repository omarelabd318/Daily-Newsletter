#!/usr/bin/env python3
"""Check and publish in one call: the end of a newsletter, recap or desk run.

Usage (from the repo root):
  python3 .claude/skills/daily-newsletter/publish.py newsletter|recap|desk DATE            checks only
  python3 .claude/skills/daily-newsletter/publish.py newsletter|recap|desk DATE --push     checks, then commits and pushes
  python3 .claude/skills/daily-newsletter/publish.py newsletter|recap|desk DATE --push-if-clean
      checks, and commits and pushes only when nothing is left to fix: no ERROR, no TRIM, and no WARNING other
      than the information-only ones (word counts, links a site refused to check, research and data notes)

Checks: editions/index.json parses and has the entry (newsletter, recap), check_edition.py on the edition (and
check_log.py DATE for the recap), or check_desk.py (desk). The checkers print briefly, as they do on their own.
With --push, and only when no check reports an ERROR: stages the run's files, commits ('Newsletter DATE', 'Weekly
Recap DATE' or 'Desk DATE'), fetches main, rebases onto it, pushes to main (once more after a fresh fetch if main
moved), then pushes the same commit to the session's branch. A rebase conflict is aborted and reported (exit 3)
with the files in conflict: merge them by hand (keep both runs' entries in data files), then run --push again.
Prints one line per step and ends with PUBLISHED <commit> or NOT PUBLISHED and why. Exit 0 only when all went well.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
NL = ".claude/skills/daily-newsletter"
DESK = ".claude/skills/markets-desk"


def run(cmd, show=True, tail=60):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=isinstance(cmd, str))
    out = (r.stdout + r.stderr).strip()
    if show and out:
        lines = out.splitlines()
        print("\n".join(lines[-tail:]) if len(lines) > tail else out)
    return r.returncode, out


def files_for(kind, date):
    if kind == "desk":
        return ["desk/", f"data/research/{date}.json", "data/markets.json", "data/markets-recent.json"]
    f = ["editions/", "data/markets.json", "data/markets-recent.json", f"data/research/{date}.json", "data/topics.json",
         f"data/puzzles/{date}.json", "data/puzzles/index.json", "desk/intraday.json", f"{NL}/pronounce.json"]
    if kind == "newsletter":
        f.append(f"data/weeks/{date}.json")
    return [x for x in f if os.path.exists(os.path.join(ROOT, x))]


# Warnings that need no fix before publishing: they go in the final reply, if anywhere.
INFO_ONLY = re.compile(r"words \(guide|words without Sources|could not be checked|^Research: the scripts read|"
                       r"^Closes not compared|^Listen: |fine if several outlets", re.I)
FOUND = []   # (kind, text) of every ERROR and WARNING the checkers printed


def note(out):
    for line in out.splitlines():
        m = re.match(r"(ERROR|WARNING):\s*(.*)", line.strip())
        if m:
            FOUND.append((m.group(1), m.group(2)))


def to_fix():
    """The findings that block --push-if-clean: errors, a TRIM, and warnings that are not information only."""
    return [f"{k}: {t}" for k, t in FOUND
            if k == "ERROR" or "TRIM" in t or not INFO_ONLY.search(t)]


def checks(kind, date):
    ok = True
    if kind in ("newsletter", "recap"):
        key = f"{date}-recap" if kind == "recap" else date
        try:
            eds = json.load(open(os.path.join(ROOT, "editions", "index.json")))["editions"]
            want = (lambda e: e.get("id") == key) if kind == "recap" else (lambda e: e.get("date") == date and "id" not in e)
            if not any(want(e) for e in eds):
                print(f"ERROR: editions/index.json has no entry for {key}.")
                ok = False
            else:
                print(f"index.json: entry for {key} found.")
        except Exception as e:
            print(f"ERROR: editions/index.json does not parse ({e}).")
            ok = False
        print(f"--- check_edition.py editions/{key}.md")
        code, out = run(["python3", f"{NL}/check_edition.py", f"editions/{key}.md"])
        note(out)
        ok = ok and code == 0
        if kind == "recap":
            print(f"--- check_log.py {date}")
            run(["python3", f"{NL}/check_log.py", date])   # reports; problems go in the final reply, not a block
    else:
        print("--- check_desk.py")
        code, out = run(["python3", f"{DESK}/check_desk.py"])
        note(out)
        ok = code == 0
    return ok


def push(kind, date):
    msg = {"newsletter": f"Newsletter {date}", "recap": f"Weekly Recap {date}", "desk": f"Desk {date}"}[kind]
    run(["git", "add", "--", *files_for(kind, date)], show=False)
    if run(["git", "diff", "--cached", "--quiet"], show=False)[0] != 0:
        code, out = run(["git", "commit", "-q", "-m", msg], show=False)
        if code:
            print(f"NOT PUBLISHED: the commit failed: {out[-400:]}")
            return 1
        print(f"Committed '{msg}'.")
    else:
        print("Nothing new to commit; pushing what is committed.")
    for attempt in (1, 2):
        run(["git", "fetch", "-q", "origin", "main"], show=False)
        code, out = run(["git", "rebase", "--autostash", "origin/main"], show=False)
        if code:
            _, conflicts = run(["git", "diff", "--name-only", "--diff-filter=U"], show=False)
            run(["git", "rebase", "--abort"], show=False)
            print("NOT PUBLISHED: rebase conflict with main in: " + (", ".join(conflicts.split()) or out[-300:])
                  + ". Merge by hand (keep both runs' entries), commit, then run --push again.")
            return 3
        code, out = run(["git", "push", "-q", "origin", "HEAD:main"], show=False)
        if code == 0:
            break
        if attempt == 2:
            print(f"NOT PUBLISHED: push to main failed twice: {out[-400:]}")
            return 1
        time.sleep(5)
    sha = run(["git", "rev-parse", "--short", "HEAD"], show=False)[1]
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], show=False)[1]
    if branch not in ("main", "HEAD"):
        code, out = run(["git", "push", "-q", "-u", "origin", "HEAD"], show=False)
        print(f"Session branch {branch}: " + ("pushed." if code == 0 else f"push failed ({out[-200:]})."))
    print(f"PUBLISHED {sha} to main ('{msg}').")
    return 0


def main(a):
    if len(a) < 2 or a[0] not in ("newsletter", "recap", "desk"):
        sys.exit(__doc__)
    kind, date = a[0], a[1]
    ok = checks(kind, date)
    if "--push-if-clean" in a:
        left = to_fix()
        if left:
            print(f"NOT PUBLISHED: {len(left)} finding(s) to fix first:")
            print("\n".join("  " + x[:160] for x in left))
            sys.exit(1)
        sys.exit(push(kind, date))
    if "--push" not in a:
        print("CHECKS PASS (no errors)." if ok else "CHECKS FAIL: fix the errors above, then run again.")
        sys.exit(0 if ok else 1)
    if not ok:
        print("NOT PUBLISHED: fix the errors above, then run --push again.")
        sys.exit(1)
    sys.exit(push(kind, date))


if __name__ == "__main__":
    main(sys.argv[1:])
