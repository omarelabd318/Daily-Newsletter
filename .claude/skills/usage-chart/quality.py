#!/usr/bin/env python3
"""Quality index for each day's newsletter (or Saturday recap) and Markets Desk, so a cost cut (a cheaper model,
fewer steps) can be checked against what the runs published.

usage: quality.py START END [--baseline-end DATE] [--detail] [--blocks] [--json]

For every day from START to END it reads what the repo holds (editions/, editions/notes/, desk/days/,
desk/views.json, data/research/) and scores each run on six pillars, each 0-100:

  Newsletter
    Coverage      stories in all; stories in each section and part (Egypt News, Top World Headlines, Regional
                  and Gulf, Egypt Markets, Global Markets, the four In Other News parts); Today at a Glance items
    Depth         words per story in Egypt News and in the Markets parts; figures per 100 words in Markets;
                  Worth Knowing's length (each counts only when it falls below 80% of usual)
    Sourcing      source links, distinct outlets, Egyptian outlets, the biggest single outlet's share of links
    Verification  share of the side sessions' stories confirmed at a second outlet (editions/notes), in all and
                  per block (egypt, markets, world, other, checks); open points per story
    Freshness     share of dated source links dated within two days of the edition; share of lead-ins repeated
                  from the edition before (above usual counts against it; running stories repeat by design)
    Process       searches and pages opened against the skill's floors (25 and 12; the recap's 40 and 15)
  Desk
    Coverage      calls (Egypt and Wall Street), views, week-ahead items, news items on the four pages, stocks
                  researched (weekdays only: Saturdays are light by design)
    Depth         words per call (body and view), affects tags per call, figures per 100 words
    Sourcing      links and distinct outlets in the day file, pages opened in research
    Verification  flows confirmed (weekdays), searches and pages against the desk's floors (15 and 8, Saturday 10
                  and 5)
    Discipline    news headlines of 12 words or fewer, calls with a wrong-if and a confidence, news items with an
                  impact and affects tags (absolute: 100 means every item follows the rule)
  The desk's track record (views judged right or wrong up to the day) is shown, not scored: it follows markets.

Each relative measure is the day's figure as a share of a baseline, capped at 100%: the median of the same kind of
day (weekday edition, Saturday recap, weekday desk, Saturday desk) over the 7 such days up to --baseline-end
(default: the day before). Small counts (one or two stories in a part) may fall one short of usual without cost.
Set --baseline-end to the last day before a change (e.g. 2026-11-18 for the Nov 19 cuts) to compare every later
day with how the runs were before it.

Score: the weighted mean of the pillars (newsletter: Coverage 25, Verification 25, Sourcing 20, Depth 10,
Freshness 10, Process 10; desk: Coverage 25, Verification 20, Depth 20, Sourcing 15, Discipline 20), less 10 for
each missing section and 5 for each checker error.  95 and up: holding;  85-95: watch;  below 85: dropped.
--detail prints every pillar and measure; --blocks prints the newsletter's per-block verification, the place a
cheaper research model would show first.
"""
import argparse, datetime as dt, glob, json, os, re, statistics
from urllib.parse import urlparse

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DAILY_SECTIONS = ["Today at a Glance", "Quick Hits", "Weather", "Egypt News", "Top World Headlines",
                  "Regional and Gulf", "Markets", "In Other News", "Stocks Watch", "Currency and Commodities Watch",
                  "Economic Calendar", "Worth Knowing", "Sources"]
RECAP_SECTIONS = ["Since Friday", "The Week in Brief", "Egypt This Week", "Region and World", "Markets This Week",
                  "The Week Ahead", "Sources"]
DAILY_PARTS = ["Egypt News", "Top World Headlines", "Regional and Gulf", "Egypt Markets", "Global Markets",
               "Tech and AI", "Sports", "Health and Science", "Entertainment and Culture"]
RECAP_PARTS = ["Since Friday", "Egypt This Week", "Region and World", "Markets This Week"]
BLOCKS = ["egypt", "markets", "world", "other", "checks"]
LEADIN = re.compile(r"^(?:[-*]\s+|\d+\.\s+)?\*\*([^*]{3,90}):\*\*")
URL = re.compile(r"\]\((https?://[^)\s]+)")
RAWURL = re.compile(r"https?://[^\s\"'<>)\]]+")
NUM = re.compile(r"(?<![\w.])[-+$€£]?\d[\d,]*(?:\.\d+)?%?")
DATED = [re.compile(r"/(20\d\d)/(\d{1,2})/(\d{1,2})(?:/|$|-)"), re.compile(r"/(20\d\d)-(\d\d)-(\d\d)"),
         re.compile(r"[/_-](20\d\d)(\d\d)(\d\d)(?:[/_.-]|$)"), re.compile(r"news(\d\d)(\d\d)(20\d\d)")]
EG_HOSTS = ("youm7", "masrawy", "elbalad", "cairo24", "almasryalyoum", "egypttoday", "dailynewsegypt", "enterpriseam",
            "egyptianstreets", "cairoscene", "madamasr", "elwatannews", "shorouknews", "arabfinance", "almasdar",
            "elmaser", "see.news", "alboslanews", "amwalalghad", "alborsanews", "egyptindependent", "ahram",
            "egypt-business", "economymiddleeast", "egyptoil-gas", "akhbarelyom", "elaosboa", "dostor", "albawabhnews",
            "masress", "elfagr", "vetogate", "parlmany", "almalnews", "hapijournal", "mubasher.info/markets/EGX",
            "egx.com.eg", "cbe.org.eg", "fintechgate")
NL_W = {"coverage": 25, "verification": 25, "sourcing": 20, "depth": 10, "freshness": 10, "process": 10}
DK_W = {"coverage": 25, "verification": 20, "depth": 20, "sourcing": 15, "discipline": 20}
# measures where fewer is better (scored as baseline / day)
LOWER_BETTER = {"top_share", "open_per_story", "repeat_share"}
# measures that only count once they fall clearly below usual (guides are ceilings, not targets)
SOFT = {"words_per_story_egypt", "words_per_story_markets", "figs_markets", "worth_knowing_words",
        "words_per_call", "figs", "words"}


def p(*a):
    return os.path.join(ROOT, *a)


def load(path):
    try:
        return json.load(open(path))
    except Exception:
        return None


def host(u):
    return urlparse(u).netloc.lower().removeprefix("www.").removeprefix("m.").removeprefix("amp.")


def is_eg(u):
    h = host(u)
    return h.endswith(".eg") or any(k in h or k in u for k in EG_HOSTS)


def url_date(u):
    for rx in DATED:
        m = rx.search(u)
        if m:
            g = m.groups()
            y, mo, d = (g[2], g[0], g[1]) if rx is DATED[3] else g
            try:
                return dt.date(int(y), int(mo), int(d))
            except ValueError:
                return None
    return None


def words(s):
    return len(re.sub(r"[#*|>\-\[\]()]", " ", URL.sub("", s)).split())


def sections(text):
    """{heading: body} for every ## and ### heading."""
    out, cur, buf = {}, None, []
    for ln in text.splitlines():
        m = re.match(r"^#{2,3} (.+)$", ln)
        if m:
            if cur:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(ln)
    if cur:
        out[cur] = "\n".join(buf)
    return out


def leadins(body):
    return [m.group(1).strip().lower() for ln in body.splitlines() if (m := LEADIN.match(ln.strip()))]


def notes_check(key):
    """Per block: stories in the notes, how many confirmed at a second outlet, open points."""
    out = {}
    for f in glob.glob(p("editions", "notes", f"{key}-*.md")):
        name = os.path.basename(f)[len(key) + 1:-3]
        if not re.fullmatch(r"[a-z]+", name):
            continue
        t = open(f).read()
        stories = re.split(r"^### ", t, flags=re.M)[1:]
        conf = part = single = opens = 0
        if name == "checks":
            # the figure checks: one bullet per figure, marked CONFIRMED or unconfirmed / single source
            for ln in re.findall(r"^\s*-\s+.+$", t, re.M):
                if re.search(r"\bunconfirmed\b|single source", ln, re.I):
                    single += 1
                elif re.search(r"CONFIRMED|Chk:|matches", ln):
                    conf += 1
            opens = len(re.findall(r"\bOpen\b[:,]", t))
        for s in ([] if name == "checks" else stories):
            chk = re.findall(r"^\s*-?\s*Chk:(.*)$", s, re.M)
            op = re.findall(r"^\s*-?\s*Open[^:]*:(.*)$", s, re.M)
            opens += len(op)
            weak = [c for c in chk if re.search(r"single source|same wording|not opened|no second", c, re.I)]
            if chk and len(weak) < len(chk):
                # the main fact has a second outlet; a secondary figure left open makes it partly confirmed
                if any(re.search(r"unconfirmed|single source|only\b|not confirmed", o, re.I) for o in op):
                    part += 1
                else:
                    conf += 1
            elif chk or re.search(r"single source", s, re.I):
                single += 1
            # stories with no Chk line and no single-source note are context items: not counted
        n = conf + part + single
        out[name] = {"stories": len(stories), "checked": n, "full": conf, "partly": part, "single": single,
                     "confirmed": round((conf + part) / n, 3) if n else None,
                     "fully": round(conf / n, 3) if n else None, "open": opens}
    return out


def newsletter(date):
    key = date if os.path.exists(p("editions", f"{date}.md")) else f"{date}-recap"
    path = p("editions", f"{key}.md")
    if not os.path.exists(path):
        return None
    recap = key.endswith("recap")
    text = open(path).read()
    body = text.split("\n## Sources")[0]
    secs = sections(body)
    heads = re.findall(r"^## (.+)$", text, re.M)
    urls = list(dict.fromkeys(URL.findall(text)))
    hosts = [host(u) for u in urls]
    m = {"kind": "recap" if recap else "daily", "key": key, "words": words(body),
         "missing": [s for s in (RECAP_SECTIONS if recap else DAILY_SECTIONS) if s not in heads]}
    lis = leadins(body)
    m["stories"] = len(lis)
    for part in (RECAP_PARTS if recap else DAILY_PARTS):
        m[f"n:{part}"] = len(leadins(secs.get(part, "")))
    if not recap:
        m["glance"] = len(re.findall(r"^\d+\.\s+\*\*", secs.get("Today at a Glance", ""), re.M))

        def wps(parts):
            n = sum(m[f"n:{x}"] for x in parts)
            return round(sum(words(secs.get(x, "")) for x in parts) / n) if n else None
        m["words_per_story_egypt"] = wps(["Egypt News"])
        m["words_per_story_markets"] = wps(["Egypt Markets", "Global Markets"])
        mk = secs.get("Egypt Markets", "") + "\n" + secs.get("Global Markets", "")
        m["figs_markets"] = round(100 * len(NUM.findall(mk)) / max(words(mk), 1), 1) if mk.strip() else None
        m["worth_knowing_words"] = words(secs.get("Worth Knowing", "")) or None
    # sourcing
    m["links"] = len(urls)
    m["outlets"] = len(set(hosts))
    m["eg_outlets"] = len({h for u, h in zip(urls, hosts) if is_eg(u)})
    m["top_share"] = round(max(hosts.count(h) for h in set(hosts)) / len(hosts), 3) if hosts else None
    m["top_outlet"] = max(set(hosts), key=hosts.count) if hosts else None
    # freshness
    d0 = dt.date.fromisoformat(date)
    span = 8 if recap else 2
    dated = [x for x in (url_date(u) for u in urls) if x]
    m["dated_links"] = len(dated)
    m["fresh_share"] = round(sum(0 <= (d0 - x).days <= span for x in dated) / len(dated), 3) if len(dated) >= 5 else None
    m["stale_links"] = sum((d0 - x).days > (14 if recap else 7) for x in dated)
    if not recap:
        prev = None
        for i in range(1, 5):
            k = (d0 - dt.timedelta(i)).isoformat()
            if os.path.exists(p("editions", f"{k}.md")):
                prev = open(p("editions", f"{k}.md")).read().split("\n## Sources")[0]
                break
        if prev and lis:
            old = set(leadins(prev))
            m["repeat_share"] = round(sum(x in old for x in lis) / len(lis), 3)
    m["unconfirmed_marks"] = len(re.findall(r"\bunconfirmed\b", body, re.I))
    # verification (side-session notes)
    blocks = notes_check(key)
    m["blocks"] = blocks
    chk = sum(b["checked"] for b in blocks.values())
    full = sum(b["full"] for b in blocks.values())
    part = sum(b["partly"] for b in blocks.values())
    st = sum(b["stories"] for b in blocks.values())
    m["confirmed"] = round((full + part) / chk, 3) if chk else None
    m["fully_confirmed"] = round(full / chk, 3) if chk else None
    m["single_source"] = chk - full - part if chk else None
    m["open_per_story"] = round(sum(b["open"] for b in blocks.values()) / st, 3) if st else None
    for b in BLOCKS:
        if b in blocks:
            m[f"conf:{b}"] = blocks[b]["confirmed"]
    # process
    r = (load(p("data", "research", f"{date}.json")) or {}).get("recap" if recap else "newsletter") or {}
    chk_run = r.get("check") or {}
    m["errors"] = len(chk_run.get("errors", [])) if chk_run else None
    m["searches"] = len(r.get("searches", [])) or None
    m["pages"] = len([u for u in r.get("pages", []) if u.startswith("http")]) or None
    # since Nov 15 the log splits pages the main run opened ("pages") from pages scripts and side sessions read
    # ("read"); before that "pages" held both, so the volume compared with the baseline is the two together
    m["pages_all"] = len({u for u in r.get("pages", []) + r.get("read", []) if str(u).startswith("http")}) or None
    m["floor"] = (40, 15) if recap else (25, 12)
    return m


def strings(x, skip=("url", "src", "source", "date", "key", "id", "ticker", "t", "status", "confidence", "kind",
                     "dir", "impact", "day")):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in skip:
                yield from strings(v, skip)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v, skip)


def desk(date):
    day = load(p("desk", "days", f"{date}.json"))
    if not day:
        return None
    sat = dt.date.fromisoformat(date).weekday() == 5
    eg, gl, pages = day.get("egypt", {}), day.get("global", {}), day.get("pages", {})
    prose = [s for s in strings([eg, gl, pages]) if len(s.split()) > 3]
    w = sum(len(re.sub(r"<[^>]+>", " ", s).split()) for s in prose)
    calls = eg.get("calls", []) + gl.get("calls", [])
    news = [n for pg in pages.values() if isinstance(pg, dict) for n in pg.get("news", [])]
    raw = json.dumps(day, ensure_ascii=False)
    urls = list(dict.fromkeys(RAWURL.findall(raw)))
    r = (load(p("data", "research", f"{date}.json")) or {}).get("desk") or {}
    chk_run = r.get("check") or {}
    flows = eg.get("flows") or {}
    m = {"kind": "sat" if sat else "daily", "words": w,
         "calls_eg": len(eg.get("calls", [])), "calls_us": len(gl.get("calls", [])), "calls": len(calls),
         "views": len(eg.get("views", [])) + len(gl.get("views", [])),
         "week": len(eg.get("week", [])) + len(gl.get("week", [])),
         "news": len(news),
         "stocks": (len(r.get("stocks", {})) or None) if not sat else None,
         "stocks_seen": len(r.get("stocks", {})) or None,
         "words_per_call": round(sum(len((c.get("body", "") + " " + c.get("view", "")).split()) for c in calls)
                                 / len(calls)) if calls else None,
         "affects_per_call": round(sum(len(c.get("affects", [])) for c in calls) / len(calls), 1) if calls else None,
         "figs": round(100 * sum(len(NUM.findall(s)) for s in prose) / max(w, 1), 1),
         "links": len(urls), "outlets": len({host(u) for u in urls}),
         "pages": len([u for u in r.get("pages", []) if str(u).startswith("http")]) or None,
         "pages_all": len({u for u in r.get("pages", []) + r.get("read", []) if str(u).startswith("http")}) or None,
         "flows": None if sat or "confirmed" not in flows else (1.0 if flows["confirmed"] else 0.0),
         "missing": [k for k in ("egypt", "global", "pages") if not day.get(k)],
         "errors": len(chk_run.get("errors", [])) if chk_run else None,
         "searches": len(r.get("searches", [])) or None,
         "floor": (10, 5) if sat else (15, 8)}
    heads = [n.get("headline", "") for n in news] + [c.get("headline", "") for c in calls]
    m["short_heads"] = round(sum(len(h.split()) <= 12 for h in heads) / len(heads), 3) if heads else None
    m["calls_complete"] = round(sum(bool(c.get("wrong")) and bool(c.get("confidence")) for c in calls)
                                / len(calls), 3) if calls else None
    m["news_tagged"] = round(sum(bool(n.get("impact")) and bool(n.get("affects")) for n in news)
                             / len(news), 3) if news else None
    views = (load(p("desk", "views.json")) or {}).get("views", [])
    judged = [v for v in views if (v.get("result") or {}).get("date", "9") <= date and v.get("status") in ("right", "wrong")]
    m["record"] = {"right": sum(v["status"] == "right" for v in judged), "wrong": sum(v["status"] == "wrong" for v in judged),
                   "different_reason": sum((v.get("lesson") or {}).get("tag") == "right-different-reason" for v in judged),
                   "opened_today": sum(v.get("opened") == date for v in views)}
    return m


NL_PILLARS = {
    "coverage": ["stories", "glance"] + [f"n:{x}" for x in DAILY_PARTS + RECAP_PARTS],
    "depth": ["words_per_story_egypt", "words_per_story_markets", "figs_markets", "worth_knowing_words", "words"],
    "sourcing": ["links", "outlets", "eg_outlets", "top_share", "pages_all"],
    "verification": ["confirmed", "fully_confirmed"] + [f"conf:{b}" for b in BLOCKS] + ["open_per_story"],
    "freshness": ["fresh_share", "repeat_share"],
}
DK_PILLARS = {
    "coverage": ["calls_eg", "calls_us", "views", "week", "news", "stocks"],
    "depth": ["words_per_call", "affects_per_call", "figs", "words"],
    "sourcing": ["links", "outlets", "pages_all"],
    "verification": ["flows"],
    "discipline": [],
}
SMALL = {"calls_eg", "calls_us", "views", "week", "glance"}


def baseline(fn, date, kind, end, n=7):
    rows = []
    d = dt.date.fromisoformat(end)
    for i in range(n * 3):
        k = (d - dt.timedelta(i)).isoformat()
        if k >= date:
            continue
        m = fn(k)
        if m and m["kind"] == kind:
            rows.append(m)
        if len(rows) >= n:
            break
    out = {}
    keys = {k for r in rows for k, v in r.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
    for f in keys:
        v = [r[f] for r in rows if r.get(f) is not None]
        if v:
            out[f] = statistics.median(v)
    return out


def ratio(f, v, b):
    if f in LOWER_BETTER:
        if v is None or b is None:
            return None
        # a small absolute rise (a few points of share) is noise
        return 1.0 if v <= b + 0.05 else min(max(b, 0.02) / v, 1.0)
    if v is None or not b:
        return None
    if (f in SMALL or f.startswith("n:")) and v >= b - 1:
        return 1.0
    r = min(v / b, 1.0)
    if f in SOFT:
        return None if r >= 0.8 else r
    return r


def score(m, base, which):
    if not m:
        return None, [], {}
    pillars, detail, low = {}, {}, []
    spec, wts = (NL_PILLARS, NL_W) if which == "news" else (DK_PILLARS, DK_W)
    for pil, fields in spec.items():
        parts = []
        for f in fields:
            r = ratio(f, m.get(f), base.get(f))
            if r is None:
                continue
            parts.append(r)
            detail[f] = (m.get(f), base.get(f), round(r, 2))
            if r < 0.85:
                low.append(f"{f.replace('n:', '').replace('conf:', 'confirmed ')} {m[f]:g} vs {base[f]:g}")
        pillars[pil] = parts
    # absolute measures
    s, pg = m.get("searches"), m.get("pages")
    fs, fp = m["floor"]
    proc = []
    if s is not None:
        proc.append(min(s / fs, 1.0))
        if s < fs:
            low.append(f"searches {s} below the floor of {fs}")
    if pg is not None:
        proc.append(min(pg / fp, 1.0))
        if pg < fp:
            low.append(f"pages {pg} below the floor of {fp}")
    if which == "news":
        pillars["process"] = proc
    else:
        pillars["verification"] += proc
        disc = [m[f] for f in ("short_heads", "calls_complete", "news_tagged") if m.get(f) is not None]
        pillars["discipline"] = disc
        for f in ("short_heads", "calls_complete", "news_tagged"):
            if m.get(f) is not None and m[f] < 0.9:
                low.append(f"{f} {m[f]:.0%}")
    got = {k: 100 * sum(v) / len(v) for k, v in pillars.items() if v}
    if not got:
        return None, low, {}
    tot = sum(wts[k] * v for k, v in got.items()) / sum(wts[k] for k in got)
    sc = tot - 10 * len(m["missing"]) - 5 * (m.get("errors") or 0)
    if m["missing"]:
        low.append("missing: " + ", ".join(m["missing"]))
    if m.get("errors"):
        low.append(f"{m['errors']} checker error(s)")
    return round(max(sc, 0)), low, {"pillars": {k: round(v) for k, v in got.items()}, "measures": detail}


def verdict(s):
    return None if s is None else ("holding" if s >= 95 else "watch" if s >= 85 else "dropped")


def run(start, end, baseline_end=None):
    d0, d1 = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    out = {}
    for i in range((d1 - d0).days + 1):
        k = (d0 + dt.timedelta(i)).isoformat()
        be = baseline_end or (dt.date.fromisoformat(k) - dt.timedelta(1)).isoformat()
        row = {}
        for which, fn in (("news", newsletter), ("desk", desk)):
            m = fn(k)
            if not m:
                continue
            base = baseline(fn, k, m["kind"], be)
            s, low, det = score(m, base, which)
            row[which] = {**m, "score": s, "verdict": verdict(s), "low": low, "baseline": base, **det}
        if row:
            out[k] = row
    return out


def pct(x):
    return "-" if x is None else f"{x:.0%}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("start"); ap.add_argument("end")
    ap.add_argument("--baseline-end")
    ap.add_argument("--detail", action="store_true", help="print every pillar and measure against its baseline")
    ap.add_argument("--blocks", action="store_true", help="print the newsletter's per-block verification")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = run(a.start, a.end, a.baseline_end)
    if a.json:
        print(json.dumps(res, indent=1, default=str)); return
    short = {"coverage": "Cov", "depth": "Dep", "sourcing": "Src", "verification": "Ver", "freshness": "Fre",
             "process": "Pro", "discipline": "Dis"}
    for k, row in res.items():
        for which in ("news", "desk"):
            m = row.get(which)
            if not m:
                continue
            name = ("Recap" if m["kind"] == "recap" else "Newsletter") if which == "news" else "Desk"
            sc = "  -" if m["score"] is None else f"{m['score']:3d} {m['verdict']}"
            pil = " ".join(f"{short[p_]} {v:3d}" for p_, v in m.get("pillars", {}).items())
            if which == "news":
                facts = (f"{m['stories']} stories, {m['outlets']} outlets ({m['eg_outlets']} Egyptian), "
                         f"{m['links']} links, confirmed {pct(m['confirmed'])}, fresh {pct(m.get('fresh_share'))}")
            else:
                rec = m["record"]
                facts = (f"{m['calls']} calls, {m['views']} views, {m['news']} news, {m['stocks_seen']} stocks, "
                         f"flows {'n/a' if m['flows'] is None else 'ok' if m['flows'] else 'unconfirmed'}, "
                         f"record {rec['right']}-{rec['wrong']}")
            print(f"{k} {name:10s} {m['words']:5d} words  {sc:12s} [{pil}]  {facts}"
                  + (f"\n{'':16s}LOW: {'; '.join(m['low'])}" if m["low"] else ""))
            if a.blocks and which == "news" and m.get("blocks"):
                bl = "  ".join(f"{b} {pct(v['confirmed'])} ({v['full']}+{v['partly']} of {v['checked']}, {v['open']} open)"
                               for b, v in sorted(m["blocks"].items()))
                print(f"{'':16s}blocks: {bl}")
            if a.detail:
                for f, (v, b, r) in m.get("measures", {}).items():
                    print(f"{'':16s}{f:28s} {v!s:>8} vs {b!s:>8}  {r:.2f}")


if __name__ == "__main__":
    main()
