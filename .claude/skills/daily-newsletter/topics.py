#!/usr/bin/env python3
"""Running topics across editions (data/topics.json): each story tagged with the topics it belongs to, shown on the
site as a label under the story, a Topics list and a page per topic.

Usage (from the repo root):
  topics.py tag EDITION             tag the edition's stories by each topic's keywords (EDITION: 2026-11-06, or a file
                                    key such as 2026-10-28-v2); keeps tags added or removed by hand
  topics.py add EDITION "Lead-in" TOPIC      put a story in a topic the keywords missed
  topics.py remove EDITION "Lead-in" TOPIC   take a story out of a topic it was wrongly matched to
  topics.py now TOPIC "One paragraph"        rewrite the topic's "Where it stands" (dated today)
  topics.py new TOPIC "Name" "keyword regex" create a running topic (then run tag on recent editions)
  topics.py list                             topics with their story counts and the last edition each appeared in
  topics.py backfill                         tag every edition in editions/

A story is a bold lead-in item (**Lead:** text) outside Today at a Glance, Quick Hits, Weather, the two watch tables,
Economic Calendar, Worth Knowing and Sources. Its id matches the anchor the site gives it (story-<slug of the lead>).
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PATH = os.path.join(ROOT, "data", "topics.json")
SKIP = {"Today at a Glance", "Quick Hits", "Weather", "Stocks Watch", "Currency and Commodities Watch", "Economic Calendar",
        "Worth Knowing", "Sources", "The Week in Brief", "Markets This Week", "The Week Ahead"}


def slug(s):
    return re.sub(r"^-+|-+$", "", re.sub(r"[^a-z0-9]+", "-", s.lower()))


def load():
    try:
        return json.load(open(PATH))
    except Exception:
        return {"topics": [], "stories": []}


def save(D):
    D["stories"].sort(key=lambda s: (s["ed"], s["id"]), reverse=True)
    with open(PATH, "w") as f:
        json.dump(D, f, indent=1, ensure_ascii=False)
        f.write("\n")


def stories(key):
    """The edition's stories as [{id, lead, sec, text}], with the same ids the site's anchors use."""
    md = open(os.path.join(ROOT, "editions", key + ".md")).read()
    out, used, sec = [], set(), ""
    for line in md.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            sec = re.sub(r"[*_`]", "", h.group(1)).strip()
            continue
        m = re.match(r"^\s*(?:[-*]|\d+[.)])?\s*\*\*([^*]+?):?\*\*:?\s*(.*)$", line)
        if not m or sec in SKIP:
            continue
        lead = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", m.group(1)).rstrip(":").strip()
        sid = "story-" + slug(lead)
        if sid == "story-" or sid in used:
            continue
        used.add(sid)
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", m.group(2)).replace("**", "").strip()
        out.append({"id": sid, "lead": lead, "sec": sec, "text": text})
    return out


def find(D, key, lead):
    sid = "story-" + slug(lead.rstrip(":"))
    return next((s for s in D["stories"] if s["ed"] == key and s["id"] == sid), None), sid


def short(t, n=240):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def tag(D, key, quiet=False):
    topics = {t["id"]: re.compile(t["match"], re.I) for t in D["topics"] if t.get("match")}
    old = {s["id"]: s for s in D["stories"] if s["ed"] == key}
    D["stories"] = [s for s in D["stories"] if s["ed"] != key]
    for st in stories(key):
        o = old.get(st["id"], {})
        # a story belongs to a topic when its lead-in names it, or its text mentions it at least twice: a passing
        # mention ("since the Iran war began") is not enough
        auto = [tid for tid, rx in topics.items() if rx.search(st["lead"]) or len(rx.findall(st["text"])) >= 2]
        tags = [t for t in auto if t not in o.get("removed", [])] + [t for t in o.get("added", []) if t not in auto]
        if tags:
            D["stories"].append({"ed": key, "id": st["id"], "lead": st["lead"], "sec": st["sec"], "text": short(st["text"]),
                                 "topics": tags, **({"added": o["added"]} if o.get("added") else {}),
                                 **({"removed": o["removed"]} if o.get("removed") else {})})
            if not quiet:
                print(f"{key} {st['lead']}: {', '.join(tags)}")
        elif o.get("removed"):   # keep a removal on record even when the story has no topic left
            D["stories"].append({"ed": key, "id": st["id"], "lead": st["lead"], "sec": st["sec"], "text": short(st["text"]),
                                 "topics": [], "removed": o["removed"]})


def main(a):
    if not a:
        sys.exit(__doc__)
    D = load()
    cmd = a[0]
    if cmd == "tag" and len(a) == 2:
        tag(D, a[1])
    elif cmd == "backfill":
        for f in sorted(os.listdir(os.path.join(ROOT, "editions"))):
            if f.endswith(".md"):
                tag(D, f[:-3], quiet=True)
    elif cmd in ("add", "remove") and len(a) == 4:
        key, lead, tid = a[1], a[2], a[3]
        if tid not in {t["id"] for t in D["topics"]}:
            sys.exit(f"No topic {tid}; create it with: topics.py new")
        s, sid = find(D, key, lead)
        if not s:
            st = next((x for x in stories(key) if x["id"] == sid), None)
            if not st:
                sys.exit(f"No story '{lead}' in {key}")
            s = {"ed": key, "id": sid, "lead": st["lead"], "sec": st["sec"], "text": short(st["text"]), "topics": []}
            D["stories"].append(s)
        if cmd == "add":
            s.setdefault("added", []).append(tid) if tid not in s.get("added", []) else None
            s["removed"] = [x for x in s.get("removed", []) if x != tid]
            if tid not in s["topics"]:
                s["topics"].append(tid)
        else:
            s.setdefault("removed", []).append(tid) if tid not in s.get("removed", []) else None
            s["added"] = [x for x in s.get("added", []) if x != tid]
            s["topics"] = [x for x in s["topics"] if x != tid]
        print(f"{key} {s['lead']}: {', '.join(s['topics']) or 'no topic'}")
    elif cmd == "now" and len(a) == 3:
        t = next((t for t in D["topics"] if t["id"] == a[1]), None)
        if not t:
            sys.exit(f"No topic {a[1]}")
        t["now"], t["now_date"] = a[2], datetime.date.today().isoformat()
        print(f"{t['name']}: where it stands updated.")
    elif cmd == "new" and len(a) == 4:
        if any(t["id"] == a[1] for t in D["topics"]):
            sys.exit(f"Topic {a[1]} exists")
        re.compile(a[3])
        D["topics"].append({"id": a[1], "name": a[2], "match": a[3], "now": "", "now_date": None, "related": [], "drivers": []})
        print(f"Created {a[1]}; now run: topics.py tag on the recent editions.")
    elif cmd == "list":
        for t in D["topics"]:
            ss = [s for s in D["stories"] if t["id"] in s["topics"]]
            eds = sorted({s["ed"][:10] for s in ss})
            print(f"{t['id']:16} {len(ss):3} stories, {len(eds):2} editions, last {eds[-1] if eds else '—'}  {t['name']}")
        return
    else:
        sys.exit(__doc__)
    save(D)


if __name__ == "__main__":
    main(sys.argv[1:])
