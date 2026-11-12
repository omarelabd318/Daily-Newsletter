#!/usr/bin/env python3
"""The desk read aloud: an 8 to 9 minute summary of the day's desk in the Heart voice, for the Listen button on the
Egypt and US dashboards.

Usage (from the repo root, after the desk is final and checked):
  python3 .claude/skills/markets-desk/desk_audio.py DATE [--script]

It writes the summary from desk/days/DATE.json alone (no writing by the run: the desk's own finding, close, stories
and views, cut to fit), saves it as desk/listen/DATE.md, and records it with the newsletter's make_audio.py as
"desk-DATE" (data/audio/desk-DATE.json; the MP3 goes on the audio branch, which keeps the last seven desks).
--script writes the text only, to read it. Takes about two minutes; if anything fails it says so and the run goes on.
Commit desk/listen/DATE.md and data/audio/.
"""
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
TARGET = (780, 960)    # words: Heart reads about 105 a minute, so 8 to 9 minutes (under 10)


def plain(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(t or ""))).strip()


def sentences(t):
    t = plain(t)
    # a sentence ends at . ! or ? before a space and a capital or a quote, never inside a figure such as 54.31
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", t) if s.strip()]


def first(t, n):
    return " ".join(sentences(t)[:n])


def nosrc(t):
    # sources in brackets are for the page, not the ear: "(Mubasher, Alborsa)" goes
    t = re.sub(r"\s*\((?:company|its own|the company's) (?:release|statement|filing)[^()]*\)", "", t)
    return re.sub(r"\s*\((?:[A-Z][^()]{1,60}?)(?:, [A-Z][^()]{1,40}?)*\)(?=[.,;: ]|$)", "", t)


def close_line(group):
    out = []
    for r in group.get("rows", [])[:5]:
        if r.get("value") is None:
            continue
        ch = r.get("change")
        lab = re.sub(r"\s*\(.*?\)", "", r["label"])
        if ch is None:
            out.append(f"{lab} at {r['value']}")
        else:
            out.append(f"{lab} {'up' if ch > 0 else 'down' if ch < 0 else 'flat'}"
                       + (f" {abs(ch):.2f}% at {r['value']}" if ch else f" at {r['value']}"))
    return ("; ".join(out) + ".") if out else ""


def section(name, X, depth):
    """depth: how much of each story (sentences of its body, of its view, of the stocks note; stories read)."""
    L = [f"## {name}", "", f"**The day:** {nosrc(plain(X.get('finding')))}", ""]
    groups = (X.get("close") or {}).get("groups") or []
    if groups:
        g = groups[0]
        L += [f"**The close:** {close_line(g)}", ""]
    for c in (X.get("calls") or [])[:depth[3]]:
        body = nosrc(first(c.get("body"), depth[0]))
        view = nosrc(first(c.get("view"), depth[1]))
        txt = body + (f" The desk's view: {view}" if view else "")
        L += [f"**{plain(c.get('headline')).rstrip('.')}:** {txt}", ""]
    note = nosrc(first(X.get("stocksNote"), depth[2]))
    if note:
        L += [f"**The stocks:** {note}", ""]
    views = [v for v in (X.get("views") or []) if v.get("call")]
    if views:
        parts = [f"{plain(v['call']).rstrip('.')}: {plain(v.get('status') or 'open')}" for v in views[:4]]
        L += ["**The desk's views:** " + "; ".join(parts) + ".", ""]
    if X.get("next"):
        L += [f"**Coming up:** {plain(X['next'])}", ""]
    return L


def build(date):
    D = json.load(open(os.path.join(ROOT, "desk", "days", date + ".json")))
    d = datetime.date.fromisoformat(date)
    words = lambda L: len(" ".join(L).split())
    # the most of each story that still fits the length: whole sentences only
    # trimmed in this order: the stocks note, the later stories, then the story text; the desk's view on each story
    # it reads stays (it is the desk's own judgement), down to its first sentence
    for depth in ((2, 2, 1, 5), (2, 1, 1, 4), (1, 1, 1, 4), (1, 1, 0, 4), (1, 1, 0, 3), (1, 1, 0, 2), (1, 0, 0, 2)):
        L = [f"*Markets Desk, {d:%A, %B} {d.day}, {d.year}.*", ""]
        L += section("Egypt", D.get("egypt") or {}, depth)
        L += section("United States", D.get("global") or {}, depth)
        if words(L) <= TARGET[1]:
            break
    return "\n".join(L).rstrip() + "\n", words(L)


def main(a):
    args = [x for x in a if not x.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    date = args[0]
    text, n = build(date)
    os.makedirs(os.path.join(ROOT, "desk", "listen"), exist_ok=True)
    path = os.path.join(ROOT, "desk", "listen", date + ".md")
    open(path, "w").write(text)
    print(f"Desk summary for {date}: {n} words, about {n / 105:.1f} minutes ({os.path.relpath(path, ROOT)}).")
    if "--script" in a:
        return
    sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "daily-newsletter"))
    import make_audio
    make_audio.main(["desk-" + date, "--voice", "af_heart"])


if __name__ == "__main__":
    main(sys.argv[1:])
