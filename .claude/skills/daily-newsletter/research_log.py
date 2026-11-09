#!/usr/bin/env python3
"""The day's research log: every search made and page opened, for the newsletter and the desk (data/research/DATE.json).

Usage (from the repo root; PART is newsletter or desk):
  python3 .claude/skills/daily-newsletter/research_log.py DATE PART search "query" ["query" ...]
  python3 .claude/skills/daily-newsletter/research_log.py DATE PART page URL [URL ...]
  python3 .claude/skills/daily-newsletter/research_log.py DATE desk stock TICKER "what was found (or: no news)"
  python3 .claude/skills/daily-newsletter/research_log.py DATE PART close TICKER PRICE "where it was confirmed"
  python3 .claude/skills/daily-newsletter/research_log.py DATE PART summary

Log each search as you make it and each page as you open it (a script that reads a whole edition, such as
read_enterprise.py, counts as the pages it prints). The checkers read the log: check_edition.py for the newsletter,
check_desk.py for the desk, and both runs end their final reply with the summary line this prints. "close" records a
close checked at its source when the checker finds it far from the session's last trade (check_edition.py then
accepts it).
"""
import datetime
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DIR = os.path.join(ROOT, "data", "research")
# what a full day's research looks like; the checkers warn below these and error below half
TARGETS = {"newsletter": {"searches": 25, "pages": 30}, "desk": {"searches": 15, "pages": 15}}


def path(date):
    return os.path.join(DIR, f"{date}.json")


def load(date):
    try:
        return json.load(open(path(date)))
    except Exception:
        return {"date": date}


def part(log, name):
    return log.setdefault(name, {"searches": [], "pages": [], "stocks": {}})


def summary(log, name):
    p = log.get(name) or {}
    s, pg, st = len(p.get("searches", [])), len(set(p.get("pages", []))), len(p.get("stocks", {}))
    return f"Research: {s} searches, {pg} pages opened" + (f", {st} stocks checked" if name == "desk" else "") + "."


def record_check(date, name, errors, warnings, **extra):
    """The checker's last result for the day's newsletter, recap or desk, kept in the log for the site's Runs page
    (/desk/runs/). Only for today's or yesterday's work (Cairo), so checking an old edition leaves its log alone."""
    try:
        cairo = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
        if date < (cairo.date() - datetime.timedelta(days=1)).isoformat():
            return
        log = load(date)
        log.setdefault(name, {"searches": [], "pages": [], "stocks": {}})["check"] = {
            "at": cairo.strftime("%Y-%m-%d %H:%M"), "errors": errors, "warnings": warnings, **extra}
        os.makedirs(DIR, exist_ok=True)
        with open(path(date), "w") as f:
            json.dump(log, f, indent=1, ensure_ascii=False)
            f.write("\n")
    except Exception:
        pass


def main(a):
    if len(a) < 3 or a[1] not in TARGETS:
        sys.exit(__doc__)
    date, name, cmd, rest = a[0], a[1], a[2], a[3:]
    datetime.date.fromisoformat(date)
    log = load(date)
    p = part(log, name)
    if cmd == "search":
        p["searches"] += rest
    elif cmd == "page":
        for u in rest:
            if u not in p["pages"]:
                p["pages"].append(u)
    elif cmd == "stock" and len(rest) >= 1:
        p["stocks"][rest[0].upper()] = " ".join(rest[1:]) or "checked"
    elif cmd == "close" and len(rest) >= 3:
        p.setdefault("closes", {})[rest[0].upper()] = {"price": float(rest[1].replace(",", "")), "source": " ".join(rest[2:])}
    elif cmd != "summary":
        sys.exit(__doc__)
    if cmd != "summary":
        os.makedirs(DIR, exist_ok=True)
        with open(path(date), "w") as f:
            json.dump(log, f, indent=1, ensure_ascii=False)
            f.write("\n")
    print(summary(log, name))


if __name__ == "__main__":
    main(sys.argv[1:])
