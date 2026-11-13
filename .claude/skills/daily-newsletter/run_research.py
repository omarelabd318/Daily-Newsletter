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
5. Scheduled data: US and Egyptian releases just out and due (TradingView's economic calendar, with actual, forecast
   and previous), how old each official figure in the data log is (T-bill yields, the central bank's rates,
   inflation, reserves), the dates already known for three days (calendar_facts.py), and for desk stocks reporting
   now: the SEC's filings and filed figures (US), or Mubasher's results headlines and their figures (Egypt).
6. Regional and world headlines, business and sports leads.
7. What it could not reach, so the run fetches those by hand.
8. editions/articles.md: the stories themselves for the leads most likely to run (stories several outlets carry, with
   a second outlet for the top ones, the running topics, and the first economy, region, wire, sports and world
   headlines): each page read with articles.py, its link at the outlet and its opening and figures (about 110
   words). Read it after the brief; open a page only where the excerpt is not enough. The pages read are logged.
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


CIK = {"AAPL": 320193, "MSFT": 789019, "NVDA": 1045810, "AMZN": 1018724, "GOOGL": 1652044, "META": 1326801, "TSLA": 1318605, "JPM": 19617,
       "XOM": 34088, "AVGO": 1730168, "BRK.B": 1067983, "WMT": 104169, "V": 1403161, "ORCL": 1341439, "COST": 909832, "NFLX": 1065280, "INTC": 50863, "LLY": 59478}
LOGGED = [("cbe_usd_sell", "Central bank dollar rate (sell)", 4), ("tbill_91", "91-day T-bill", 8), ("tbill_182", "182-day T-bill", 8), ("tbill_273", "273-day T-bill", 8),
          ("tbill_364", "364-day T-bill", 8), ("cbe_deposit", "Overnight deposit rate", 60), ("infl_headline", "Headline inflation", 35), ("infl_core", "Core inflation", 35),
          ("reserves_usd", "Net international reserves, $bn", 35)]


def get_json(url, name, headers=None):
    try:
        return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})}), timeout=30).read())
    except Exception as e:
        FAILED.append(f"{name} ({type(e).__name__})")
        return None


def scheduled(date):
    """Releases due and just out (TradingView's economic calendar, US and Egypt), and how old the logged official
    figures are, so an auction or a monthly release since the last log is not missed."""
    d0 = datetime.date.fromisoformat(date)
    out = ["## Scheduled data"]
    a, b = (d0 - datetime.timedelta(days=1)).isoformat(), (d0 + datetime.timedelta(days=3)).isoformat()
    cal = get_json(f"https://economic-calendar.tradingview.com/events?from={a}T00:00:00.000Z&to={b}T00:00:00.000Z&countries=US,EG", "TradingView economic calendar", {"Origin": "https://www.tradingview.com"})
    rows = []
    for e in (cal or {}).get("result", []):
        if e.get("country") == "US" and (e.get("importance") or -1) < 0:
            continue
        when = datetime.datetime.fromisoformat(e["date"].replace("Z", "+00:00")) + datetime.timedelta(hours=2)   # Cairo, UTC+2
        val = lambda k: None if e.get(k) is None else f"{e[k]}{e.get('unit') or ''}{e.get('scale') or ''}"
        bits = [f"{k} {val(k)}" for k in ("actual", "forecast", "previous") if val(k)]
        rows.append((when, f"- {when:%a %b %-d, %H:%M} Cairo | {e['country']} | {e['title']}" + (" | " + ", ".join(bits) if bits else "") + (" | HIGH" if e.get("importance") == 1 else "")))
    rows.sort()
    out.append("Out since yesterday (figures to check at the source before use):")
    out += [r for w, r in rows if w.date() < d0 or (w.date() == d0 and "actual" in r)] or ["- Nothing listed."]
    out.append("Due today and in the next two days:")
    out += [r for w, r in rows if w.date() >= d0 and "actual" not in r][:40] or ["- Nothing listed."]
    if cal is None:
        out.append("- The calendar could not be reached: check the day's US and Egyptian releases by hand.")
    days = json.load(open(os.path.join(ROOT, "data", "markets.json")))["days"]
    out.append("Official figures in the data log, and how old each is (fetch_figures.py refreshes what it can; the central bank's own site does not load from here):")
    for k, name, limit in LOGGED:
        hit = next(((e["date"], e[k]) for e in reversed(days) if isinstance(e.get(k), (int, float)) and e["date"] <= date), None)
        if not hit:
            continue
        first = next(e["date"] for e in days if e.get(k) == hit[1] and e["date"] <= hit[0] and all(x.get(k) in (hit[1], None) for x in days if e["date"] <= x["date"] <= hit[0]))
        age = (d0 - datetime.date.fromisoformat(first)).days
        out.append(f"- {name}: {hit[1]} (unchanged since {first}, {age} days)" + ("  <- likely a newer figure is out: check" if age > limit else ""))
    return out + [""]


def us_filing(t, d0):
    cik = CIK.get(t)
    if not cik:
        return [f"- {t}: no SEC number on file."]
    out, c10 = [], f"CIK{cik:010d}"
    sub = get_json(f"https://data.sec.gov/submissions/{c10}.json", f"SEC filings list, {t}")
    r = ((sub or {}).get("filings") or {}).get("recent") or {}
    new = [(r["form"][i], r["filingDate"][i], r["accessionNumber"][i], r["primaryDocument"][i]) for i in range(len(r.get("form", [])))
           if (r["form"][i] in ("10-Q", "10-K") or (r["form"][i] == "8-K" and "2.02" in (r["items"][i] or ""))) and (d0 - datetime.date.fromisoformat(r["filingDate"][i])).days <= 5]
    for form, filed, acc, doc in new[:3]:
        out.append(f"- {t}: {form}{' (results release)' if form == '8-K' else ''} filed {filed}: https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}")
    if not new:
        out.append(f"- {t}: no results release (8-K item 2.02) or quarterly report filed with the SEC in the last five days yet.")
    # the last filed quarter's figures from the SEC's own data (they appear once the 10-Q or 10-K is in)
    for label, concepts, unit in (("Revenue", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues"], "USD"), ("Net income", ["NetIncomeLoss"], "USD"), ("Diluted EPS", ["EarningsPerShareDiluted"], "USD/shares")):
        cands = []
        for c in concepts:
            d = get_json(f"https://data.sec.gov/api/xbrl/companyconcept/{c10}/us-gaap/{c}.json", f"SEC figures, {t} {c}")
            q = [x for x in ((d or {}).get("units") or {}).get(unit, []) if x.get("start") and 80 <= (datetime.date.fromisoformat(x["end"]) - datetime.date.fromisoformat(x["start"])).days <= 100]
            if q:
                cands.append(q)
        for q in sorted(cands, key=lambda q: max(x["end"] for x in q), reverse=True)[:1]:   # companies change the tag they report revenue under: take the one still in use
            if q:
                last = max(q, key=lambda x: (x["end"], x["filed"]))
                end = datetime.date.fromisoformat(last["end"])
                ago = next((x for x in q if abs((end - datetime.date.fromisoformat(x["end"])).days - 365) <= 10), None)
                f = (lambda v: f"${v / 1e9:,.2f}bn") if unit == "USD" else (lambda v: f"${v:,.2f}")
                out.append(f"    {label}, quarter to {last['end']} ({last['form']} filed {last['filed']}): {f(last['val'])}" + (f"; a year earlier {f(ago['val'])} ({(last['val'] / ago['val'] - 1) * 100:+.1f}%)" if ago and ago["val"] else ""))
    return out


def egx_filing(t):
    try:
        page = urllib.request.urlopen(urllib.request.Request(f"https://www.mubasher.info/markets/EGX/stocks/{t}/news", headers={"User-Agent": UA}), timeout=30).read().decode("utf-8", "replace")
    except Exception as e:
        FAILED.append(f"Mubasher news, {t} ({type(e).__name__})")
        return [f"- {t}: Mubasher's news page did not load; find the disclosure by hand."]
    items = [(u, html.unescape(x).strip(" \u200b")) for u, x in re.findall(r'href="(/news/\d+/[^"]+)"[^>]*>\s*([^<]{15,200})<', page)]
    hits = [(u, x) for u, x in items if re.search("أرباح|نتائج|القوائم المالية|خسائر|صافي ربح", x)][:4]
    hits.sort(key=lambda h: not (re.search("أرباح|خسائر|صافي ربح", h[1]) and re.search(r"\d", h[1])))   # a headline with the figure first
    out = [f"- {t}: " + (f"{len(hits)} results headlines on Mubasher" if hits else "no results headline on Mubasher yet") + f" (https://www.mubasher.info/markets/EGX/stocks/{t}/news)"]
    for u, x in hits:
        out.append(f"    {x[:170]}")
    if hits:   # the newest one's own sentences with figures
        try:
            art = urllib.request.urlopen(urllib.request.Request("https://www.mubasher.info" + hits[0][0], headers={"User-Agent": UA}), timeout=30).read().decode("utf-8", "replace")
            art = re.sub(r"<(script|style)[^>]*>.*?</\1>|<!--.*?-->", " ", art, flags=re.S)
            m = re.search(r'class="article__content-text"[^>]*>(.*?)<div[^>]+class="mi-article__(?:labels|source|attachments)', art, re.S)
            text = html.unescape(re.sub(r"<[^>]+>", "\n", m.group(1) if m else ""))
            sents = [x.strip() for x in re.split(r"(?<=[.؛])\s+|\n", text) if re.search(r"\d", x) and 40 < len(x.strip()) < 420]
            out += [f"      > {x[:330]}" for x in sents[:6]]
        except Exception as e:
            out.append(f"      (the article did not load: {type(e).__name__})")
    return out


def last_edition(date):
    files = sorted(f for f in os.listdir(os.path.join(ROOT, "editions")) if re.match(r"\d{4}-\d{2}-\d{2}(-v\d+)?\.md$", f) and f[:10] < date)
    return files[-1] if files else None


def stories_of(md):
    """{lead-in: paragraph} for the bold lead-in items of an edition."""
    out = {}
    for m in re.finditer(r"^(?:[-*]\s+)?\*\*([^*\n]{3,80}?):?\*\*:?\s*(.+)$", md, re.M):
        out[m.group(1).strip().rstrip(":")] = m.group(2).strip()
    return out


def read_articles(date, want):
    """editions/articles.md: the likeliest stories read in one go (articles.py), so the run opens pages only where an
    excerpt is not enough. Returns how many pages were read."""
    import articles
    seen, picks = set(), []
    for label, it in want:
        k = re.sub(r"\W+", "", it["title"].lower())[:50]
        if it.get("url") and k not in seen:
            seen.add(k)
            picks.append((label, it))
    picks = picks[:45]
    pages = articles.read_many([it["url"] for _, it in picks])
    A = [f"# Stories read for {date}", "",
         "Read by run_research.py with articles.py: each page's link at the outlet, then its opening and the sentences with "
         "figures. The outlet's words, not checked: confirm what moves a story against a second outlet. Open a page only "
         "where this is not enough, or run articles.py with several URLs at once.", ""]
    ok, bad = [], []
    for (label, it), pg in zip(picks, pages):
        if pg["error"]:
            bad.append(f"- {it['title'][:120]} | {it.get('outlet') or it['source']}: {pg['error']}" + (f" ({pg['url']})" if "news.google" not in pg["url"] else ""))
            continue
        ok.append(pg["url"])
        A += [f"## {it['title'][:160]}", f"{label} | {it.get('outlet') or it['source']} | {articles.short(pg['url'])}",
              articles.excerpt(pg["text"], 110), ""]
    if bad:
        A += ["## Not read (open by hand if the story matters)"] + bad + [""]
    open(os.path.join(ROOT, "editions", "articles.md"), "w").write("\n".join(A) + "\n")
    articles.log_pages(date, "newsletter", ok)
    return len(ok)


def main():
    date = next((a for a in sys.argv[1:] if re.match(r"\d{4}-\d{2}-\d{2}$", a)), datetime.date.today().isoformat())
    L = [f"# Newsletter brief for {date}", "", "Built by run_research.py. Leads to open and check, not facts; not for publication.", ""]
    add = L.append
    # no links: Google's feed gives only its own long redirect addresses, so find the story on the outlet's site
    fmt = lambda i: f"- {i['title'][:190]} | {i.get('outlet') or i['source']}{(' | ' + i['when'].strftime('%a %H:%M')) if i['when'] else ''}"
    short = lambda i: f"- {i['title'][:160]}{(' | ' + i['when'].strftime('%a %H:%M')) if i['when'] else ''}"   # under its outlet's heading
    # the brief stays in the run's memory for the whole run, so it carries no junk and nothing twice: tag and archive
    # pages go, a headline already in the shared-stories list is not listed again under its outlet, lists are capped
    junk = re.compile(r"^(Tag:|Category:|Blog\b|#)|\bPage \d{2,}\b", re.I)
    clean = lambda xs: [x for x in xs if not junk.search(x["title"])]
    # Egyptian outlets
    per, allitems = {}, []
    for name, q, ar in EGYPT:
        got = search("site:" + q.split()[0] + (" " + " ".join(q.split()[1:]) if " " in q else ""), name, bool(ar))
        for g in got:
            g["outlet"], g["ar"] = name, ar
        got = clean(got)
        per[name] = got[:14]
        allitems += got[:25]
    shown, want = set(), []
    for ar, label in ((0, "English"), (1, "Arabic")):
        cl = clusters([i for i in allitems if i["ar"] == ar])
        add(f"## Stories several Egyptian outlets carry ({label})")
        if not cl:
            add("- None found by headline; scan the lists below.")
        for gi, g in enumerate(cl[:18]):
            if gi < (12 if ar == 0 else 5):
                want.append(("Several outlets", g[0]))
                if gi < 6 and len(g) > 1:
                    want.append(("Several outlets (second outlet)", next(i for i in g if i["outlet"] != g[0]["outlet"])))
            shown.update(id(i) for i in g)
            outlets = sorted({i["outlet"] for i in g})
            add(f"- **{len(outlets)} outlets** ({', '.join(outlets)}): {g[0]['title'][:170]}")
            for o in outlets[1:]:
                other = next(i for i in g if i["outlet"] == o)
                if other["title"][:60] != g[0]["title"][:60]:
                    add(f"    {o}: {other['title'][:170]}")
        add("")
    add("## Each outlet's other headlines, last 24 hours (those not in the lists above)")
    for name, _, _ in EGYPT:
        rest = [i for i in per[name] if id(i) not in shown][:10]
        if rest:
            add(f"### {name}")
            L.extend(short(i) for i in rest)
    add("")
    # regional, world, leads
    wires = []
    add("## Regional outlets and wires on Egypt (two days)")
    for name, q in REGION:
        got = clean(search("site:" + q, name, days=2))[:6]
        for g in got:
            g["outlet"] = name
        wires += got
        want += [("Regional and wires", i) for i in got[:1]]
        L.extend(fmt(i) for i in got)
    add("")
    for name, q, ar in LEADS:
        got = clean(search(q, name, bool(ar)))[:10]
        want += [(name, i) for i in got[:(4 if name == "Egypt economy" else 2)]]
        wires += got
        add(f"## {name}")
        L.extend(fmt(i) for i in got)
        add("")
    for name, code in TOPICS:
        got = feed(f"https://news.google.com/rss/headlines/section/topic/{code}?hl=en-US&gl=US&ceid=US:en", "Google News " + name)[:12]
        want += [("Top: " + name, i) for i in got[:3]]
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
    block = ["## Running topics"]
    for tp in T.get("topics", []):
        try:
            rx = re.compile(tp["match"], re.I)
        except re.error:
            continue
        hits = [i for i in allitems + wires if rx.search(i["title"])]
        if not hits:   # nothing on it today: one line, not the whole block (the brief stays in the run's memory)
            block.append(f"### {tp['name']}: no headline on it today in what was gathered")
            continue
        block.append(f"### {tp['name']}")
        want.append(("Topic: " + tp["name"], hits[0]))
        if tp.get("now"):
            block.append(f"- Where it stood ({tp.get('now_date')}): {tp['now'][:420]}")
        # the last edition that carried the topic (data/topics.json tags every story), with its full text and figures
        mine = [x for x in T.get("stories", []) if tp["id"] in (x.get("topics") or []) and x["ed"][:10] < date]
        if mine:
            ed = max(x["ed"] for x in mine)
            try:
                full = stories_of(open(os.path.join(ROOT, "editions", ed + ".md")).read())
            except OSError:
                full = {}
            for x in [x for x in mine if x["ed"] == ed][:2]:
                text = full.get(x["lead"], x.get("text", ""))
                figs = re.findall(r"(?:EGP|\$|€)\s?[\d.,]+(?:\s?(?:bn|billion|million|trillion|m))?|\b\d[\d.,]*\s?(?:%|percent|people|killed|injured|dead)", text)
                block.append(f"- Last carried {ed}, \"{x['lead']}\": {text[:320]}" + (f"  [figures then: {', '.join(dict.fromkeys(figs))[:220]}]" if figs else ""))
        else:
            block.append("- No earlier edition carried it.")
        seen = set()
        for i in hits[:40]:
            k = i["title"][:60]
            if k not in seen and len(seen) < 5:
                seen.add(k)
                block.append(fmt(i))
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
    forced = next((a.split("=")[1].split(",") for a in sys.argv[1:] if a.startswith("--filings=")), None)
    now = [c for c in cal if c.get("kind") == "results" and c.get("date") and -2 <= (datetime.date.fromisoformat(c["date"]) - d0).days <= 0]
    if forced:
        now = [{"t": t, "market": "us" if t in CIK else "egx", "date": date} for t in forced]
    tail += ["", "## Reporting now: the filing and its figures",
             "US: the SEC's list of filings and its own figures (the documents themselves do not load from here: read the release on the company's investor page). Egypt: Mubasher's results headlines and the newest one's figures. Check each against the filing before use."]
    for c in now:
        tail += us_filing(c["t"], d0) if c.get("market") == "us" else egx_filing(c["t"])
    if not now:
        tail.append("- No desk stock has results dated today or in the last two days.")
    tail = scheduled(date) + tail
    tail += ["", "## Could not be reached (fetch by hand if needed)", "- " + (", ".join(FAILED) if FAILED else "Nothing: every feed answered.")]
    empty = [n for n, _, _ in EGYPT if not per[n]]
    if empty:
        tail.append("- No headlines came back for: " + ", ".join(empty) + " (open their front pages directly).")
    L[head + len(block):head + len(block)] = tail + [""]
    open(os.path.join(ROOT, "editions", "brief.md"), "w").write("\n".join(L) + "\n")
    nread = read_articles(date, want)
    print(f"run_research: read {nread} story pages into editions/articles.md;  {sum(len(v) for v in per.values())} Egyptian headlines from {sum(1 for v in per.values() if v)} of {len(EGYPT)} outlets, "
          f"{len(wires)} regional and world leads; {len(FAILED)} feeds failed; read editions/brief.md ({len(L)} lines)")


if __name__ == "__main__":
    main()
