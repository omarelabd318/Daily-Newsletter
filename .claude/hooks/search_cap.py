#!/usr/bin/env python3
"""PreToolUse hook: the newsletter's and the desk's hard caps on searches (60 and 35), for the built-in web search.

search.py enforces the cap on its own queries; this blocks WebSearch once the day's research log
(data/research/DATE.json) holds the cap's number of newsletter searches, side sessions included.

Which run a session is: the hook also sees every Bash call, and the first research_log.py or
search.py --log call that names a part (newsletter or desk) and a date ties the session to them
(kept in data/research/.sessions.json, not committed). A session never tied (an interactive session)
is never blocked. An allowed WebSearch is logged at once, under the lock, so side sessions
searching at the same time cannot overshoot the cap; logging the same query afterwards with
research_log.py does not count it twice.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "daily-newsletter"))
TIE = re.compile(r"(?:research_log\.py|--log)\s+(\d{4}-\d{2}-\d{2})\s+(newsletter|desk)\b")
SESSIONS = os.path.join(ROOT, "data", "research", ".sessions.json")


def main():
    try:
        h = json.load(sys.stdin)
    except Exception:
        return 0
    sid, tool, inp = h.get("session_id") or "", h.get("tool_name"), h.get("tool_input") or {}
    try:
        tied = json.load(open(SESSIONS))
    except Exception:
        tied = {}
    if tool == "Bash":
        m = TIE.search(inp.get("command") or "")
        if m and sid and tied.get(sid) != [m.group(1), m.group(2)]:
            tied[sid] = [m.group(1), m.group(2)]
            os.makedirs(os.path.dirname(SESSIONS), exist_ok=True)
            with open(SESSIONS, "w") as f:
                json.dump(dict(list(tied.items())[-50:]), f)
        return 0
    if tool != "WebSearch" or sid not in tied:
        return 0
    date, name = tied[sid]
    import research_log
    if name not in research_log.HARD_CAPS:
        return 0
    query = inp.get("query") or ""
    ok, refused = research_log.reserve(date, name, [query])
    if refused:
        n = len(research_log.part(research_log.load(date), name)["searches"])
        print(research_log.CAP_NOTE.format(n=n, cap=research_log.HARD_CAPS[name], part=name), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
