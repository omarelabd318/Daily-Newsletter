#!/usr/bin/env python3
"""The week's editions in one short read, for the Weekly Recap's main run.

Usage (from the repo root, DATE is the Saturday):
  python3 .claude/skills/daily-newsletter/week_digest.py DATE
  python3 .claude/skills/daily-newsletter/week_digest.py --edition editions/YYYY-MM-DD.md   (one edition, the same way)

Prints, for each edition from Sunday to Friday (second editions of a day included): its intro line, Today at a
Glance in full, and each story's bold lead-in and first sentence, section by section (no Weather, Quick Hits,
tables or Sources). Then where each running topic moved this week stands now (data/topics.json), and the research
notes the week's side sessions saved (editions/notes/). The recap's side sessions read the editions in full for
their own blocks; the main run works from this digest and opens an edition only for a story it needs in full.
--edition prints one edition's digest: the daily run reads the last edition this way to tell new stories from
continuing ones (about half the words), and greps the edition for a story it needs to check in full.
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SKIP = ("Quick Hits", "Weather", "Stocks Watch", "Currency and Commodities Watch", "Sources")


def first_sentence(t):
    m = re.match(r"(.+?[.!?])(\s|$)", t.strip())
    return m.group(1) if m else t.strip()


def digest(path):
    lines = open(path).read().splitlines()
    out, sec = [], None
    for i, ln in enumerate(lines):
        h2, h3 = re.match(r"^## (.+)", ln), re.match(r"^### (.+)", ln)
        if h2:
            sec = h2.group(1).strip()
            if sec not in SKIP:
                out += ["", ln]
            continue
        if sec in SKIP:
            continue
        if h3:
            out.append(ln)
            continue
        if sec is None:
            if ln.strip():
                out.append(ln)   # the intro line
            continue
        if sec == "Today at a Glance":
            if ln.strip():
                out.append(ln)
            continue
        m = re.match(r"^(?:[-*]\s+|\d+\.\s+)?(\*\*[^*]+\*\*:?)\s*(.*)", ln)
        if m:
            out.append(f"- {m.group(1)} {first_sentence(m.group(2))}")
    return "\n".join(out).strip(), sum(len(l.split()) for l in lines)


def main(a):
    if not a:
        sys.exit(__doc__)
    if a[0] == "--edition" and len(a) > 1:
        text, n = digest(a[1])
        print(f"===== {a[1]} =====\n{text}\n\n({len(text.split())} of {n} words; grep the file for a story in full.)")
        return
    date = a[0][:10]
    sat = datetime.date.fromisoformat(date)
    sun = sat - datetime.timedelta(days=6)
    days = {(sun + datetime.timedelta(days=k)).isoformat() for k in range(6)}
    eds = sorted(f for f in os.listdir(os.path.join(ROOT, "editions"))
                 if re.match(r"\d{4}-\d{2}-\d{2}(-v\d+)?\.md$", f) and f[:10] in days)
    total_in = total_out = 0
    for f in eds:
        text, n = digest(os.path.join(ROOT, "editions", f))
        total_in += n
        total_out += len(text.split())
        print(f"\n===== editions/{f} =====\n{text}")
    try:
        D = json.load(open(os.path.join(ROOT, "data", "topics.json")))
        moved = [t for t in D.get("topics", []) if str(t.get("now_date", ""))[:10] >= sun.isoformat() and t.get("now")]
    except (OSError, ValueError):
        moved = []
    if moved:
        print("\n===== Running topics: where each stands now =====")
        for t in moved:
            print(f"- **{t.get('name', t.get('id'))}** ({t.get('now_date')}): {t['now']}")
    nd = os.path.join(ROOT, "editions", "notes")
    notes = sorted(f for f in os.listdir(nd) if f[:10] in days) if os.path.isdir(nd) else []
    if notes:
        print("\n===== Side-session notes saved this week (checked facts with sources; open one only if needed) =====")
        print("\n".join(f"- editions/notes/{f}" for f in notes))
    print(f"\n({total_out} of {total_in} words of {len(eds)} editions; open an edition for a story in full or its links.)")


if __name__ == "__main__":
    main(sys.argv[1:])
