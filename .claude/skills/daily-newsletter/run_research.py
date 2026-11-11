#!/usr/bin/env python3
"""The newsletter's gathering in one command: editions/brief.md, a worksheet to read before researching.

Usage:
  python3 .claude/skills/daily-newsletter/run_research.py [DATE]      # DATE defaults to today

It collects, and never judges:
1. Stories several outlets carry: the day's headlines from the Egyptian outlets the skill lists, grouped where two
   or more outlets report the same thing (a lead for Egypt News, and the cross-check is half done).
2. Each outlet's headlines, so the front pages are scanned in one place.
3. Running topics: for each topic in data/topics.json, where it stood, what the last edition said about it with its
   figures, and today's headlines on it. Check new figures against the old ones before writing.
4. Yesterday's "What to watch today", to follow up on what was expected.
5. Dates already known for the next three days (calendar_facts.py), and the desk stocks reporting now, with where
   their filing is.
6. Regional and world headlines, business and sports leads.
7. What it could not reach, so the run fetches those by hand.
Headlines come through Google News's feeds (one request per outlet), so each line is a lead with no link: find the
story on the outlet's own site and read it there before using it, as always. The file is a worksheet: not committed (.gitignore), never linked.
"""
import datetime
import html
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "markets-desk"))
try:
    import sources
    sources.install()
except Exception:
    sources = None
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGYPT = [("Egypt Independent", "egyptindependent.com", 0), ("Daily News Egypt", "dailynewsegypt.com", 0), ("Egyptian Streets", "egyptianstreets.com", 0),
         ("Zawya", "zawya.com Egypt", 0), ("Arab Finance", "arabfinance.com", 0), ("Middle East Observer", "meobserver.org", 0),
         ("Amwal Al Ghad", "en.amwalalghad.com", 0), ("EnterpriseAM", "enterpriseam.com", 0), ("CairoScene", "cairoscene.com", 0),
         ("Ahram Online", "english.ahram.org.eg", 0), ("Egypt Today", "egypttoday.com", 0), ("Mada Masr", "madamasr.com", 0),
         ("Youm7", "youm7.com", 1), ("Masrawy", "masrawy.com", 1), ("Al-Shorouk", "shorouknews.com", 1), ("Al Mal", "almalnews.com", 1)]
REGION = [("The National", "thenationalnews.com Egypt"), ("Al-Monitor", "al-monitor.com Egypt"), ("Asharq Al-Awsat", "english.aawsat.com Egypt"),
          ("Middle East Eye", "middleeasteye.net Egypt"), ("Reuters", "reuters.com Egypt"), ("AP", "apnews.com Egypt")]
LEADS = [("Gulf and region", "Saudi OR UAE OR Qatar OR Gaza OR Sudan OR Libya OR Houthi", 0), ("Egypt economy", "Egypt (pound OR inflation OR IMF OR \"central bank\" OR EGX OR remittances OR Suez)", 0),
         ("Sports", "(\"Al Ahly\" OR Zamalek OR Pyramids OR \"Mohamed Salah\" OR \"Egypt national team\" OR Marmoush)", 0), ("Sports, Arabic", "الأهلي OR الزمالك OR \"منتخب مصر\" OR \"محمد صلاح\"", 1),
         ("Culture and tech", "Egypt (film OR festival OR museum OR startup OR antiquities OR concert)", 0)]
TOPICS = [("World", "WORLD"), ("Business", "BUSINESS"), ("Technology", "TECHNOLOGY")]
STOP = set("the a an and or of to in on for with from at by as is are was were be been it its this that after over into than new says say said will has have had not more amid".split())
FAILED = []


def feed(url, name):
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=25).read().decode("utf-8", "replace")
    except Exception as e:
        FAILED.append(f"{name} ({type(e).__name__})")
        return []
    out = []
    for item in re.findall(r"<item>(.*?)</item>", raw, re.S):
        g = lambda tag: html.unescape(re.sub(r"<[^>]+>", "", (re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", item, re.S) or [None, ""])[1])).strip()
        title, src = g("title"), g("source")
        if src and title.endswith(" - " + src):
            title = title[: -len(src) - 3]
        try:
            when = datetime.datetime.strptime(g("pubDate")[:25].strip(), "%a, %d %b %Y %H:%M:%S")
        except ValueError:
            when = None
        out.append({"title": title, "url": g("link"), "source": src, "when": when})
    return out


def search(q, name, arabic=False, days=1):
    lang = "hl=ar&gl=EG&ceid=EG:ar" if arabic else "hl=en-US&gl=US&ceid=US:en"
    return feed(f"https://news.google.com/rss/search?q={urllib.parse.quote(q + f' when:{days}d')}&{lang}", name)


def tokens(t):
    w = re.findall(r"[A-Za-z؀-ۿ][\w؀-ۿ'-]{2,}|\d[\d.,]*%?", t.lower())
    return {x.strip(".,") for x in w if x not in STOP}


def clusters(items):
    """Headlines from different outlets that share enough of their words to be one story."""
    groups = []
    for it in items:
        tk = tokens(it["title"])
        if len(tk) < 3:
            continue
        best = None
        for g in groups:
            inter = len(tk & g["tk"])
            score = inter / max(1, min(len(tk), len(g["tk"])))
            if inter >= 3 and score >= 0.5 and (not best or score > best[0]):
                best = (score, g)
        if best:
            best[1]["items"].append(it)
            best[1]["tk"] |= tk
        else:
            groups.append({"tk": set(tk), "items": [it]})
    out = [g["items"] for g in groups if len({i["outlet"] for i in g["items"]}) >= 2]
    return sorted(out, key=lambda g: -len({i["outlet"] for i in g}))


def last_edition(date):
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "editions")) if re.match(r"\d{4}-\d{2}-\d{2}(-v\d+)?\.md$", f) and f[:10] < date)
    return files[-1] if files else None


def stories_of(md):
    """{lead-in: paragraph} for the bold lead-in items of an edition."""
    out = {}
    for m in re.finditer(r"^(?:[-*]\s+)?\*\*([^*\n]{3,80}?):?\*\*:?\s*(.+)$", md, re.M):
        out[m.group(1).strip().rstrip(":")] = m.group(2).strip()
    return out


def main():
    date = next((a for a in sys.argv[1:] if re.match(r"\d{4}-\d{2}-\d{2}$", a)), datetime.date.today().isoformat())
    L = [f"# Newsletter brief for {date}", "", "Built by run_research.py. Leads to open and check, not facts; not for publication.", ""]
    add = L.append
    # no links: Google's feed gives only its own long redirect addresses, so find the story on the outlet's site
    fmt = lambda i: f"- {i['title'][:190]} | {i.get('outlet') or i['source']}{(' | ' + i['when'].strftime('%a %H:%M')) if i['when'] else ''}"
    # Egyptian outlets
    per, allitems = {}, []
    for name, q, ar in EGYPT:
        got = search("site:" + q.split()[0] + (" " + " ".join(q.split()[1:]) if " " in q else ""), name, bool(ar))
        for g in got:
            g["outlet"], g["ar"] = name, ar
        per[name] = got[:14]
        allitems += got[:25]
    for ar, label in ((0, "English"), (1, "Arabic")):
        cl = clusters([i for i in allitems if i["ar"] == ar])
        add(f"## Stories several Egyptian outlets carry ({label})")
        if not cl:
            add("- None found by headline; scan the lists below.")
        for g in cl[:18]:
            outlets = sorted({i["outlet"] for i in g})
            add(f"- **{len(outlets)} outlets** ({', '.join(outlets)}): {g[0]['title'][:170]}")
            for o in outlets[1:]:
                other = next(i for i in g if i["outlet"] == o)
                if other["title"][:60] != g[0]["title"][:60]:
                    add(f"    {o}: {other['title'][:170]}")
        add("")
    add("## Each outlet's headlines, last 24 hours")
    for name, _, _ in EGYPT:
        add(f"### {name} ({len(per[name])})")
        L.extend(fmt(i) for i in per[name])
    add("")
    # regional, world, leads
    wires = []
    add("## Regional outlets and wires on Egypt (two days)")
    for name, q in REGION:
        got = search("site:" + q, name, days=2)[:8]
        for g in got:
            g["outlet"] = name
        wires += got
        L.extend(fmt(i) for i in got)
    add("")
    for name, q, ar in LEADS:
        got = search(q, name, bool(ar))[:12]
        wires += got
        add(f"## {name}")
        L.extend(fmt(i) for i in got)
        add("")
    for name, code in TOPICS:
        got = feed(f"https://news.google.com/rss/headlines/section/topic/{code}?hl=en-US&gl=US&ceid=US:en", "Google News " + name)[:18]
        wires += got
        add(f"## Top headlines: {name}")
        L.extend(fmt(i) for i in got)
        add("")
    # running topics
    T = json.load(open(os.path.join(ROOT, "data", "topics.json")))
    prev = last_edition(date)
    prev_md = open(os.path.join(ROOT, "editions", prev)).read() if prev else ""
    prev_stories = stories_of(prev_md)
    head = [L.index(x) for x in L if x.startswith("## Each outlet")][0]
    block = [f"## Running topics (last edition: {prev})"]
    for tp in T.get("topics", []):
        try:
            rx = re.compile(tp["match"], re.I)
        except re.error:
            continue
        block.append(f"### {tp['name']}")
        if tp.get("now"):
            block.append(f"- Where it stood ({tp.get('now_date')}): {tp['now'][:420]}")
        for lead, text in prev_stories.items():
            if rx.search(lead + " " + text):
                figs = re.findall(r"(?:EGP|\$|€)\s?[\d.,]+(?:\s?(?:bn|billion|million|trillion|m))?|\b\d[\d.,]*\s?(?:%|percent|people|killed|injured|dead)", text)
                block.append(f"- Last edition, \"{lead}\": {text[:260]}" + (f"  [figures then: {', '.join(dict.fromkeys(figs))[:200]}]" if figs else ""))
        hits = [i for i in allitems + wires if rx.search(i["title"])]
        seen = set()
        for i in hits[:40]:
            k = i["title"][:60]
            if k not in seen and len(seen) < 8:
                seen.add(k)
                block.append(fmt(i))
        if not hits:
            block.append("- No headline on it today in what was gathered.")
    block.append("")
    L[head:head] = block
    # yesterday's watch line, and the dates already known
    m = re.search(r"\*\*What to watch today:\*\*\s*(.+)", prev_md)
    tail = ["## Expected yesterday: what happened?", f"- {m.group(1)[:900]}" if m else "- No watch line found.", "", "## Dates already known (calendar_facts.py, three days)"]
    try:
        out = subprocess.run([sys.executable, os.path.join(HERE, "calendar_facts.py"), date, "3"], cwd=ROOT, capture_output=True, text=True, timeout=60).stdout
        tail += [x[:220] for x in out.splitlines() if x.strip()][:40]
    except Exception as e:
        tail.append(f"- calendar_facts.py failed ({e})")
    cal = (json.load(open(os.path.join(ROOT, "desk", "calendar.json"))) or {}).get("items", [])
    d0 = datetime.date.fromisoformat(date)
    now = [c for c in cal if c.get("kind") == "results" and c.get("date") and -1 <= (datetime.date.fromisoformat(c["date"]) - d0).days <= 0]
    tail += ["", "## Reporting now: read the filing"]
    for c in now:
        where = (f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={c['t'].replace('.', '-')}&type=8-K&dateb=&owner=include&count=5" if c.get("market") == "us"
                 else f"https://www.mubasher.info/markets/EGX/stocks/{c['t']}/news")
        tail.append(f"- {c['t']} ({c['date']}{', expected' if c.get('expected') else ''}): {where}")
    if not now:
        tail.append("- No desk stock has results dated today or yesterday.")
    tail += ["", "## Could not be reached (fetch by hand if needed)", "- " + (", ".join(FAILED) if FAILED else "Nothing: every feed answered.")]
    empty = [n for n, _, _ in EGYPT if not per[n]]
    if empty:
        tail.append("- No headlines came back for: " + ", ".join(empty) + " (open their front pages directly).")
    L[head + len(block):head + len(block)] = tail + [""]
    open(os.path.join(ROOT, "editions", "brief.md"), "w").write("\n".join(L) + "\n")
    print(f"run_research: {sum(len(v) for v in per.values())} Egyptian headlines from {sum(1 for v in per.values() if v)} of {len(EGYPT)} outlets, "
          f"{len(wires)} regional and world leads; {len(FAILED)} feeds failed; read editions/brief.md ({len(L)} lines)")


if __name__ == "__main__":
    main()
