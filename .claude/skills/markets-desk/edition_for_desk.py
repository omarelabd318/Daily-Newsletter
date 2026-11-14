#!/usr/bin/env python3
"""The parts of today's edition the desk uses, in one read: the desk then carries a third of the edition through the
run, not all of it.

Usage (from the repo root):
  python3 .claude/skills/markets-desk/edition_for_desk.py DATE

Prints, from editions/DATE.md:
- in full: the intro line, Today at a Glance (with What to watch today), both parts of Markets, Stocks Watch,
  Currency and Commodities Watch and the Economic Calendar;
- each story's bold lead-in and first sentence: Egypt News, Regional and Gulf, Top World Headlines, Tech and AI;
- nothing from Quick Hits, Weather, Sports, Health and Science, Entertainment and Culture, Worth Knowing or Sources.
On a Saturday (no DATE.md) it prints the Weekly Recap, editions/DATE-recap.md, in full. Open the edition itself only
for a story you need in full or for its source links.
"""
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
FULL = ("Today at a Glance", "Markets", "Stocks Watch", "Currency and Commodities Watch", "Economic Calendar")
GIST = ("Egypt News", "Regional and Gulf", "Top World Headlines", "Tech and AI")


def first_sentence(t):
    m = re.match(r"(.+?[.!?])(\s|$)", t.strip())
    return m.group(1) if m else t.strip()


def main(a):
    if not a:
        sys.exit(__doc__)
    date = a[0]
    path = os.path.join(ROOT, "editions", f"{date}.md")
    if not os.path.exists(path):
        recap = os.path.join(ROOT, "editions", f"{date}-recap.md")
        if os.path.exists(recap):
            print(open(recap).read())
            return
        sys.exit(f"No edition for {date} yet.")
    lines = open(path).read().splitlines()
    out, mode = [], None
    for i, ln in enumerate(lines):
        h2, h3 = re.match(r"^## (.+)", ln), re.match(r"^### (.+)", ln)
        if h2:
            name = h2.group(1).strip()
            mode = "full" if name in FULL else ("gist" if name in GIST else ("in-other" if name == "In Other News" else None))
            if mode in ("full", "gist"):
                out += ["", ln]
            continue
        if h3 and mode in ("in-other", "gist-sub"):
            mode = "gist-sub" if h3.group(1).strip() in GIST else "in-other"
            if mode == "gist-sub":
                out += ["", ln]
            continue
        if i == 0 or (not out and ln.strip()):
            out.append(ln)   # the intro line
            continue
        if mode == "full":
            out.append(ln)
        elif mode in ("gist", "gist-sub"):
            m = re.match(r"^(?:[-*]\s+)?(\*\*[^*]+\*\*:?)\s*(.*)", ln)
            if m:
                out.append(f"- {m.group(1)} {first_sentence(m.group(2))}")
    text = "\n".join(out).strip()
    print(text)
    print(f"\n({len(text.split())} of {sum(len(l.split()) for l in lines)} words of editions/{date}.md; open it for a story in full or its links.)")


if __name__ == "__main__":
    main(sys.argv[1:])
