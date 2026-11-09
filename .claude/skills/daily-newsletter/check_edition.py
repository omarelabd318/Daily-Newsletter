#!/usr/bin/env python3
"""Check a Daily Newsletter edition before it is committed.

Usage: python3 .claude/skills/daily-newsletter/check_edition.py editions/YYYY-MM-DD.md [--no-links]

It opens every Sources link (about 20 seconds); --no-links skips that when offline.

Errors exit with code 1. Warnings are printed for a human (or Claude) to judge.
"""
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

SECTIONS = [
    "Today at a Glance", "Quick Hits", "Weather", "Egypt News", "Top World Headlines",
    "Regional and Gulf", "Markets", "Stocks Watch", "Currency and Commodities Watch", "In Other News",
    "Economic Calendar", "Worth Knowing", "Sources",
]
# The Saturday weekly recap (editions/YYYY-MM-DD-recap.md) has its own sections.
RECAP_SECTIONS = [
    "The Week in Brief", "Egypt This Week", "Region and World", "Markets This Week",
    "Sports This Week", "Culture and Tech", "How It Played Out", "The Week Ahead", "Sources",
]
RECAP_TOTAL = (1600, 2500)
# The fixed Stocks Watch rows, in order (see the skill).
FIXED = {
    "Egypt": ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN"],
    "USA": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT"],
}
PARTS = {
    "Markets": ["Egypt Markets", "Global Markets"],
    "Stocks Watch": ["Egypt", "USA"],
    "In Other News": ["Tech and AI", "Sports", "Health and Science", "Entertainment and Culture"],
}
BUDGET = {
    "Today at a Glance": (150, 190), "Quick Hits": (70, 100), "Weather": (50, 80),
    "Egypt News": (450, 550), "Top World Headlines": (300, 380), "Regional and Gulf": (180, 230),
    "Egypt Markets": (280, 340), "Global Markets": (210, 260), "Stocks Watch": (140, 240),
    "Currency and Commodities Watch": (180, 260), "Tech and AI": (130, 170), "Sports": (150, 200),
    "Health and Science": (70, 100), "Entertainment and Culture": (120, 150),
    "Economic Calendar": (130, 170), "Worth Knowing": (160, 200),
}
TOTAL = (2850, 3450)
MIN_ITEMS = {"Egypt News": 4, "Top World Headlines": 6, "Tech and AI": 3, "Sports": 5,
             "Entertainment and Culture": 3}
# Words that break the voice rules. "US" is left out on purpose: it is usually the country.
# "Omar" alone is the reader's name; Omar al-Bashir, Omar Marmoush and other full names are not
VOICE = re.compile(r"\b(I|I'm|I've|we|We|we're|We're|our|Our|ours|my|My|me|Omar(?![ -](?:al-|el-|bin |ibn |[A-Z])))\b")
# A single shared word in two lead-ins usually means the same running story.
STORY = set("""houthi houthis hormuz iran iranian saudi israel israeli gaza hamas hezbollah lebanon syria
sudan libya ukraine russia imf brent opec suez""".split())
STOP = set("""the a an and or of to in on for with at by from as is are was were be its it this that
these those after before over under into amid new more than not no up down off out per vs about
egypt egypt's egyptian""".split())


def words(text):
    return len(re.findall(r"\S+", text))


def slug(s):
    """Same rule as slug() in index.html."""
    return re.sub(r"^-+|-+$", "", re.sub(r"[^a-z0-9]+", "-", s.lower()))


def strip_quotes(line):
    return re.sub(r"\"[^\"]*\"|“[^”]*”", "", line)


def num(cell):
    m = re.match(r"\s*([+\-\u2212]?)\s*(\d[\d,]*(?:\.\d+)?)", cell)
    if not m:
        return None
    v = float(m.group(2).replace(",", ""))
    return -v if m.group(1) in "-\u2212" and m.group(1) else v


def check_stocks(parts, days, date):
    """Compare each Stocks Watch row with the data log: the close should match what was logged for this
    date, and the change should match the move from the previous logged close. A live (intraday) table is
    compared with the previous close, which is what the log holds while the market is open."""
    out = []
    for part, group in (("Egypt", "egx"), ("USA", "us")):
        body = parts.get(part, [])
        live = any("intraday" in l.lower() for l in body if l.strip().startswith("*"))
        series = [(d["date"], d.get(group) or {}) for d in days if d.get("date", "") <= date]
        for line in body:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            m = re.search(r"\(([A-Z.]{1,6})\)", cells[0]) if len(cells) >= 3 else None
            if not m:
                continue
            t, close, change = m.group(1), num(cells[1]), num(cells[2])
            vals = [(d, g[t]) for d, g in series if t in g]
            if close is None or not vals or vals[-1][0] != date:
                continue
            logged = vals[-1][1]
            if live:
                base = logged
            else:
                if abs(close / logged - 1) > 0.005:
                    out.append(f"Stocks Watch {t}: table close {close:,.2f} but the log has {logged:,.2f} for {date}.")
                    continue
                # Weekend and holiday editions repeat the last close: step back past repeats.
                earlier = [v for _, v in vals[:-1] if v != logged]
                base = earlier[-1] if earlier else None
            if base is None:
                continue
            implied = (close / base - 1) * 100
            if abs(implied) > 15:
                out.append(f"Stocks Watch {t}: {implied:+.1f}% from the previous close ({base:,.2f}); check the figure.")
            if change is not None and change != 0 and abs(implied - change) > 0.3:
                out.append(f"Stocks Watch {t}: table change {change:+.1f}% but the log implies {implied:+.1f}% "
                           f"({base:,.2f} to {close:,.2f}); check one of them.")
    return out


# Figures written in the edition against the data log entry for its date (the closes it shows).
TABLE_KEYS = [(r"USD/EGP|US dollar\b(?! index)", ["usd_egp", "cbe_usd_sell", "cbe_usd_buy"]), (r"dollar index|DXY", ["dxy"]), (r"EUR/EGP|Euro", ["eur_egp"]),
              (r"SAR/EGP|Saudi riyal", ["sar_egp"]), (r"AED/EGP|dirham", ["aed_egp"]), (r"KWD/EGP|Kuwaiti", ["kwd_egp"]), (r"QAR/EGP|Qatari", ["qar_egp"]),
              (r"GBP/EGP|sterling|British pound", ["gbp_egp"]), (r"Gold 21K|21K", ["gold21_egp"]), (r"Gold 24K|24K", ["gold24_egp"]), (r"Gold 18K|18K", ["gold18_egp"]),
              (r"Gold pound", ["goldpound_egp"]), (r"Gold \(\$|Gold, \$|Gold \$", ["gold_usd"]), (r"Brent", ["brent"])]
PROSE_KEYS = [("EGX30", r"EGX30", ["egx30"]), ("S&P 500", r"S&P 500", ["sp500"]), ("Nasdaq", r"Nasdaq(?![- ]100)(?: Composite)?", ["nasdaq"]),
              ("Dow", r"\bDow\b(?! Jones Transportation)", ["dow"]), ("Brent", r"\bBrent\b", ["brent"]), ("Bitcoin", r"\bBitcoin\b", ["btc"])]


def check_figures(text, date, warnings):
    try:
        days = json.load(open(os.path.join(ROOT, "data", "markets.json")))["days"]
    except Exception:
        return
    E = next((d for d in days if d["date"] == date), None)
    if not E:
        return
    numre = re.compile(r"(?<![\w.])\$?(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?![\d%])")
    # the currency table: each row's Level against the log
    sec = text.split("## Currency and Commodities Watch", 1)
    if len(sec) == 2:
        for line in sec[1].split("\n## ", 1)[0].splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or set(cells[1]) <= set("-: "):
                continue
            for pat, keys in TABLE_KEYS:
                if re.search(pat, cells[0], re.I):
                    m = numre.search(cells[1])
                    refs = [E[k] for k in keys if isinstance(E.get(k), (int, float))]
                    if m and refs:
                        v = float(m.group(1).replace(",", ""))
                        if not any(abs(v / r - 1) <= 0.005 for r in refs):
                            warnings.append(f"Figures: {cells[0]} is {cells[1]} in the table but the log has {', '.join(f'{r:,.2f}' for r in refs)} for {date}: "
                                            "fix the table or the log.")
                    break
    # levels in the text: near each mention, a number close to the logged close should be that close
    body = text.split("## Sources", 1)[0]
    for name, pat, keys in PROSE_KEYS:
        ref = E.get(keys[0])
        if not isinstance(ref, (int, float)):
            continue
        near, exact = [], False
        for m in re.finditer(pat, body):
            win = body[m.end(): m.end() + 120]
            for n in numre.finditer(win):
                raw = n.group(1)
                v = float(raw.replace(",", ""))
                # as precise as it is written: 51,152.73 must match to the cent, "about 95" within half a percent
                dec = len(raw.split(".")[1]) if "." in raw else 0
                tol = 0.5 * 10 ** -dec + 1e-9 if dec else max(0.5, abs(ref) * 0.005)
                if abs(v - ref) <= tol or (dec and abs(v - round(ref, dec)) <= 10 ** -dec + 1e-9):
                    exact = True
                elif abs(v / ref - 1) <= 0.03 and not re.search(r"(?:from|high|low|peak|since|above|below|record|target|forecast|range)\W+\S*\W*$", win[:n.start()][-40:], re.I):
                    near.append(n.group(1))
        if near and not exact:
            warnings.append(f"Figures: the text gives {name} as {', '.join(sorted(set(near))[:3])}, but the log has {ref:,.2f} for {date}: check which is right.")


def check_links(text, errors, warnings):
    """Open every Sources link: a page that is gone (404, 410, no such site) blocks publishing; one that refuses
    automated visits (401, 403, 429) or times out cannot be judged and is only counted."""
    import concurrent.futures
    import urllib.error
    import urllib.request
    src = text.split("## Sources", 1)[1] if "## Sources" in text else ""
    urls = sorted(set(re.findall(r"\((https?://[^)\s]+)\)", src)))
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"

    def one(u):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": ua}), timeout=15)
            return u, r.status
        except urllib.error.HTTPError as e:
            return u, e.code
        except urllib.error.URLError as e:
            return u, "gone" if "Name or service not known" in str(e.reason) or "nodename" in str(e.reason) else "timeout"
        except Exception:
            return u, "timeout"
    with concurrent.futures.ThreadPoolExecutor(10) as ex:
        res = list(ex.map(one, urls))
    dead = [u for u, c in res if c in (404, 410, "gone")]
    unsure = [u for u, c in res if c not in (404, 410, "gone") and not (isinstance(c, int) and c < 400)]
    for u in dead:
        errors.append(f"Sources: {u} is dead (page not found): replace it with a working link to the same story.")
    if unsure:
        warnings.append(f"Sources: {len(unsure)} of {len(urls)} links could not be checked (the site refused or timed out); open them by hand if in doubt.")


def source_close(mk, t, v):
    """True when the stock's quote at its source (Mubasher for the EGX, Nasdaq for the US) gives v as its latest close
    or the close before it, or for a US stock when Polygon has v as one of its last daily closes."""
    try:
        import fetch_figures as FF
        q = FF.mubasher(f"stocks/{t}") if mk == "egx" else FF.nasdaq(t)
        if any(x is not None and abs(x - v) <= max(0.005, abs(v) * 0.0005) for x in (q.get("value"), q.get("prev"))):
            return True
    except Exception:
        pass
    if mk == "us":   # Polygon's official daily closes for the last sessions
        try:
            import polygon
            return any(abs(x - v) <= max(0.005, abs(v) * 0.0005) for x in polygon.daily(t).values())
        except Exception:
            return False
    return False


def check_closes(date, errors, warnings):
    """Each stock's logged close against the desk's intraday prices for the same session (desk/intraday.json). A close
    left at the day before's figure while the stock traded elsewhere is an error, and so is a gap over 0.5% (EGX) or 1%
    (US, where the closing auction often sits a little off the last five-minute price) until the close is fixed or
    checked at its source and logged with research_log.py DATE newsletter close TICKER PRICE SOURCE. An EGX close can
    differ from the last trade (the exchange sets it from the session's final trades), so a gap alone is not proof."""
    try:
        days = json.load(open(os.path.join(ROOT, "data", "markets.json")))["days"]
        week = json.load(open(os.path.join(ROOT, "desk", "intraday.json"))).get("week") or {}
    except Exception:
        return
    try:
        ok = (json.load(open(os.path.join(ROOT, "data", "research", f"{date}.json"))).get("newsletter") or {}).get("closes") or {}
    except Exception:
        ok = {}
    i = next((k for k, d in enumerate(days) if d["date"] == date), None)
    if i is None:
        return
    E, P = days[i], (days[i - 1] if i else {})
    for mk, limit in (("egx", 0.005), ("us", 0.01)):
        sess = [w for w in week.get(mk, []) if w["session"] < date]
        if not sess:
            continue
        ser = sess[-1].get("series") or {}
        for t, v in (E.get(mk) or {}).items():
            pts = ser.get(t)
            if v is None or not pts:
                continue
            last = pts[-1][1]
            if abs(last - v) <= limit * abs(last):
                continue
            if v == (P.get(mk) or {}).get(t):
                errors.append(f"{t}: the log repeats the day before's close ({v}) but it traded at {last} at the end of the {sess[-1]['session']} session: take the session's close.")
            elif t in ok and abs(ok[t]["price"] - v) < 0.005:
                continue   # checked at its source by the run
            elif source_close(mk, t, v):
                continue   # the source's own quote has it as the close (before the open: the latest close, else the one before)
            else:
                errors.append(f"{t}: logged close {v}, but its last trade in the {sess[-1]['session']} session was {last} "
                              f"({abs(v / last - 1) * 100:.1f}% apart). Check the close at the source "
                              f"({'Mubasher' if mk == 'egx' else 'Nasdaq or Yahoo'}): fix the log if it is wrong, or record it with "
                              f"research_log.py {date} newsletter close {t} {v} SOURCE.")


def main(path):
    errors, warnings = [], []
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    recap = os.path.basename(path).endswith("-recap.md")
    expected = RECAP_SECTIONS if recap else SECTIONS

    first = next((l for l in lines if l.strip()), "")
    if not re.fullmatch(r"\*[^*].*[^*]\*", first.strip()):
        errors.append("First line should be a short italic intro sentence (*...*).")
    if re.search(r"^# ", text, re.M):
        errors.append("Remove the top-level '# ' title; the site already has one.")
    if re.search(r"<\s*/?\s*[a-zA-Z][^>]*>", text):
        errors.append("HTML found; use plain Markdown only.")

    # Split into ## sections and ### parts.
    sections, order, current, part = {}, [], None, None
    for line in lines:
        m2 = re.match(r"^## (.+?)\s*$", line)
        m3 = re.match(r"^### (.+?)\s*$", line)
        if m2:
            current, part = m2.group(1), None
            order.append(current)
            sections[current] = {"body": [], "parts": {}}
        elif m3 and current:
            part = m3.group(1)
            sections[current]["parts"][part] = []
        elif current:
            (sections[current]["parts"][part] if part else sections[current]["body"]).append(line)

    if recap:
        # Optional sections that go right after Markets This Week.
        extra_secs = [s for s in ("Month in Numbers", "Year in Numbers") if s in order]
        expected = expected[:4] + extra_secs + expected[4:]
    if order != expected:
        missing = [s for s in expected if s not in order]
        extra = [s for s in order if s not in expected]
        msg = "Section titles or order do not match."
        if missing:
            msg += " Missing: " + ", ".join(missing) + "."
        if extra:
            msg += " Unexpected: " + ", ".join(extra) + "."
        errors.append(msg)
    for sec, parts in ({} if recap else PARTS).items():
        have = list(sections.get(sec, {}).get("parts", {}))
        if have != parts:
            errors.append(f"'{sec}' should have parts {parts} in that order; found {have}.")

    # Word budgets.
    counts = {}
    for name, sec in sections.items():
        if name == "Sources":
            continue
        if name == "Stocks Watch":
            # Tables only: one budget for the whole section, and no prose in either part.
            counts[name] = sum(words("\n".join(b)) for b in sec["parts"].values())
            for p, body in sec["parts"].items():
                rows = [l for l in body if l.strip().startswith("|")]
                prose = [l for l in body if l.strip() and not l.strip().startswith("|")
                         and not re.fullmatch(r"\*[^*].*\*", l.strip()) and l.strip() != "---"]
                for r in rows:
                    cells = [c.strip() for c in r.strip().strip("|").split("|")]
                    if "notable mover" in cells[0].lower() and len(cells) > 1 and cells[1].lower().startswith("n/a"):
                        warnings.append(f"Stocks Watch '{p}': mover row has no close; add it with fetch_figures.py: {cells[0]}")
                fixed = FIXED.get(p, [])
                missing = [t for t in fixed if not any(f"({t})" in r for r in rows)]
                if missing:
                    errors.append(f"Stocks Watch '{p}' is missing fixed stocks: {', '.join(missing)}.")
                if prose:
                    warnings.append(f"Stocks Watch '{p}' should be a table only; found: {prose[0][:80]}")
                if rows and "YTD" not in rows[0]:
                    warnings.append(f"Stocks Watch '{p}' should have a YTD column: | Stock (ticker) | Close | Change | YTD |")
            continue
        if sec["parts"]:
            for p, body in sec["parts"].items():
                counts[p] = words("\n".join(body))
        else:
            counts[name] = words("\n".join(sec["body"]))
    # Currency and Commodities Watch: a YTD column, short notes, no repeated "Market mid-rate".
    if not recap:
        crows = [l for l in sections.get("Currency and Commodities Watch", {}).get("body", []) if l.strip().startswith("|")]
        if crows:
            head = [c.strip() for c in crows[0].strip().strip("|").split("|")]
            if "YTD" not in head:
                warnings.append("Currency and Commodities Watch should have four columns: | Item | Level | Note | YTD |")
            elif "Note" in head:
                ni = head.index("Note")
                for r in crows[2:]:
                    cells = [c.strip() for c in r.strip().strip("|").split("|")]
                    if len(cells) > ni and len(cells[ni].split()) > 9:
                        warnings.append(f"Currency note over about 6 words: {cells[0]}: {cells[ni]}")
            if sum("mid-rate" in r.lower() for r in crows[2:]) > 1:
                warnings.append("'Market mid-rate' is repeated in the currency table; say it once in the italic line above it.")

    # Minimum stories per section (bold lead-ins), so one busy section cannot crowd out the rest.
    for name, least in ({} if recap else MIN_ITEMS).items():
        body = next((sec["parts"][name] for sec in sections.values() if name in sec["parts"]),
                    sections.get(name, {}).get("body"))
        if body is None:
            continue
        n = sum(1 for l in body if re.match(r"^\s*(?:[-*]\s+|\d+\.\s+)?\*\*[^*]+\*\*", l))
        if n < least:
            warnings.append(f"{name}: {n} stories (aim for at least {least}). Search wider for real news; "
                            "never pad. If there truly are fewer, say so in the Publishing note.")
    for name, (lo, hi) in ({} if recap else BUDGET).items():
        n = counts.get(name)
        if n is not None and (n < lo * 0.7 or n > hi * 1.3):
            warnings.append(f"{name}: {n} words (guide {lo}-{hi}; fine if the stories justify it, never cut a story to fit).")
    total = sum(counts.values())
    lo, hi = RECAP_TOTAL if recap else TOTAL
    if not lo <= total <= hi:
        guide = "1,850-2,150" if recap else "3,050-3,150"
        warnings.append(f"Total {total} words without Sources (guide about {guide}; never cut a worthwhile story to fit).")

    # Voice: first person, names, authorship.
    current = None
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            current = line[3:].strip()
        if current == "Sources" or line.lstrip().startswith(">"):
            continue
        hit = VOICE.search(strip_quotes(line))
        if hit:
            warnings.append(f"Line {i}: '{hit.group(0)}' may break the voice rules: {line.strip()[:90]}")

    # US English: American spelling and month-first dates (quotes and Sources keep their own wording).
    import us_english
    found = []
    current = None
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            current = line[3:].strip()
        if current == "Sources" or line.lstrip().startswith(">"):
            continue
        found += [(i, b, a) for b, a in us_english.find(re.sub(r"\]\([^)]*\)", "]", strip_quotes(line)))]
    if found:
        shown = "; ".join(f"line {i}: {b} → {a}" for i, b, a in found[:12])
        warnings.append(f"US English: {len(found)} British spelling(s) or day-first date(s): {shown}"
                        + (" …" if len(found) > 12 else "") + ". Proper names keep their own spelling.")

    # Research: the day's log (research_log.py) shows how much was searched and read for the edition.
    m = re.match(r"(\d{4}-\d{2}-\d{2})(?:-v\d+)?\.md$", os.path.basename(path))
    if m and not recap:
        import research_log
        log = research_log.load(m.group(1)).get("newsletter")
        if not log:
            errors.append("Research: no log for this edition (data/research/DATE.json). Log every search and page opened "
                          "with research_log.py as you go.")
        else:
            T = research_log.TARGETS["newsletter"]
            for k in ("searches", "pages"):
                n = len(set(log.get(k, [])))
                if n < T[k] / 2:
                    errors.append(f"Research: only {n} {k} logged (aim for {T[k]}+): research more widely before publishing.")
                elif n < T[k]:
                    warnings.append(f"Research: {n} {k} logged, below the {T[k]} a full edition usually takes.")

    if m and not recap:
        check_figures(text, m.group(1), warnings)
        check_closes(m.group(1), errors, warnings)

    # Sources: every link opened (skip with --no-links when offline)
    if "--no-links" not in sys.argv:
        check_links(text, errors, warnings)

    # The week behind the Stocks Watch lines (week_snapshot.py), saved with each daily edition
    if m and not recap and not os.path.exists(os.path.join(ROOT, "data", "weeks", m.group(1) + ".json")):
        warnings.append(f"Trend lines: no data/weeks/{m.group(1)}.json: run fetch_intraday.py, then week_snapshot.py {m.group(1)}, "
                        "so Stocks Watch shows the week hour by hour.")

    # Listen: the recorded voice (make_audio.py), made once the edition is final
    ekey = os.path.basename(path)[:-3]
    if m and not os.path.exists(os.path.join(ROOT, "data", "audio", ekey + ".json")):
        warnings.append(f"Listen: no data/audio/{ekey}.json: once the edition is final, run make_audio.py {ekey} "
                        "(the site uses the device's voice until then).")

    # Running topics: the edition's stories tagged (topics.py tag), and each topic it moved given a fresh
    # "where it stands"
    key = os.path.basename(path)[:-3]
    try:
        import topics as TP
        TD = TP.load()
        mine = [x for x in TD.get("stories", []) if x["ed"] == key]
        rx = {t["id"]: re.compile(t["match"], re.I) for t in TD.get("topics", []) if t.get("match")}
        would = [st for st in TP.stories(key) if any(r.search(st["lead"]) or len(r.findall(st["text"])) >= 2 for r in rx.values())]
        if would and not mine:
            errors.append(f"Topics: {len(would)} stories match running topics but the edition is not tagged: run "
                          f"topics.py tag {key}, review the list, and commit data/topics.json.")
        elif not recap and m:
            moved = {tid for x in mine for tid in x.get("topics", [])}
            stale = [t["name"] for t in TD["topics"] if t["id"] in moved and (t.get("now_date") or "") < m.group(1)]
            if stale:
                warnings.append(f"Topics: 'where it stands' not updated today for {', '.join(stale)}: topics.py now TOPIC \"...\".")
    except FileNotFoundError:
        pass

    # Quick Hits carries a Number of the day (daily editions only).
    if not recap and not any(re.match(r"^\s*(?:[-*]\s+)?\*\*Number of the day:\*\*", l)
                             for l in sections.get("Quick Hits", {}).get("body", [])):
        errors.append("Quick Hits should include a '**Number of the day:**' item.")

    # The day's figures are logged for the site's trend lines (daily editions only).
    date = os.path.basename(path)[:10]
    data_dir = os.path.join(os.path.dirname(os.path.abspath(path)), "..", "data")
    if not recap:
        try:
            mdays = json.load(open(os.path.join(data_dir, "markets.json"))).get("days", [])
            day = next((d for d in mdays if d.get("date") == date), None)
            if not day or day.get("seed") or not (day.get("egx") or day.get("us") or day.get("usd_egp")):
                warnings.append("No figures logged for this date in data/markets.json; run log_figures.py.")
            else:
                warnings += check_stocks(sections.get("Stocks Watch", {}).get("parts", {}), mdays, date)
        except (OSError, ValueError):
            warnings.append("data/markets.json is missing or not valid JSON.")

    # EGX closures from data/holidays.json: the Egypt table must say the market is closed.
    if not recap:
        try:
            hols = json.load(open(os.path.join(data_dir, "holidays.json"))).get("days", [])
            hol = next((h for h in hols if h.get("date") == date and h.get("egx_closed")), None)
            egypt = sections.get("Stocks Watch", {}).get("parts", {}).get("Egypt", [])
            if hol and not any("closed" in l.lower() for l in egypt if l.strip().startswith("*")):
                warnings.append(f"The EGX is closed today ({hol['name']}, {hol.get('status', 'expected')}); "
                                "say so in the Egypt Stocks Watch line and show the last session's close.")
        except (OSError, ValueError):
            warnings.append("data/holidays.json is missing or not valid JSON.")

    # Sports: no sport-name headings or standalone bold lines.
    for line in sections.get("In Other News", {}).get("parts", {}).get("Sports", []):
        if re.fullmatch(r"\s*(\*\*[^*]+\*\*|#{4,}\s+.+)\s*", line):
            errors.append(f"Sports has a heading line; remove it and keep only items with lead-ins: {line.strip()}")

    # Editions stand alone: no references to earlier editions.
    backref = re.compile(r"(as (we )?(reported|covered|noted|mentioned) (yesterday|earlier|previously|on \w+day)|"
                         r"(yesterday's|previous|last|earlier) (edition|issue|newsletter)|"
                         r"see (yesterday|the previous)|the story continues)", re.I)
    for i, line in enumerate(lines, 1):
        hit = backref.search(line)
        if hit:
            warnings.append(f"Line {i}: '{hit.group(0)}' refers to an earlier edition; each edition must stand alone.")

    # Attribution: general credits are fine only when a point rests on several outlets.
    vague = re.compile(r"\b(according to|per|says|said|reported by|citing) (the )?(news|market|media|press|"
                       r"industry) (roundups?|reports?|bulletins?|coverage|sources)\b", re.I)
    for i, line in enumerate(lines, 1):
        hit = vague.search(line)
        if hit:
            warnings.append(f"Line {i}: '{hit.group(0)}': fine if several outlets back this point; otherwise name the outlet.")
    # Dependence: EnterpriseAM and CairoScene are core sources, but the edition should not rest on them.
    src = text.split("## Sources", 1)[1] if "## Sources" in text else ""
    # Each link counts once, or as many items as its "(used for N items)" note says.
    items = two = 0
    warned = set()
    general = re.compile(r"https?://(www\.)?(cairoscene\.com/?|enterpriseam\.com/egypt/am-edition/?)")
    for label, u in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", src):
        used = re.search(r"used for (\d+) items?", label, re.I)
        n = int(used.group(1)) if used else 1
        items += n
        if re.search(r"enterpriseam\.com|cairoscene\.com", u):
            two += n
            if general.fullmatch(u) and not used and u not in warned:
                warned.add(u)
                warnings.append(f"Sources: {u} is a homepage or edition page; link each story's own page, or add "
                                "'(used for N items)' to this line.")
    # Any other outlet: more than about six links means the world and regional news lean on one site.
    hosts = {}
    for label, u in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)\)", src):
        h = re.sub(r"^(www|en|english|m)\.", "", re.match(r"https?://([^/]+)", u).group(1).lower())
        # a wire story on Yahoo ("Reuters (via Yahoo Finance)") counts as the agency's
        if "yahoo." in h:
            wire = re.search(r"\b(Reuters|AP|Associated Press|AFP)\b", label)
            if wire:
                h = {"Reuters": "reuters.com", "AFP": "afp.com"}.get(wire.group(1), "apnews.com")
        if not re.search(r"enterpriseam\.com|cairoscene\.com", h):
            hosts[h] = hosts.get(h, 0) + 1
    for h, n in sorted(hosts.items(), key=lambda x: -x[1]):
        if n > 6:
            warnings.append(f"Sources: {n} links from {h}; keep the stories but source some from other outlets "
                            "(Reuters, AP, AFP, BBC, The National, Asharq Al-Awsat…) and check each against a second.")
    if not recap and items and two / items > 1 / 3:
        warnings.append(f"EnterpriseAM and CairoScene account for {two} of {items} sourced items; research wider "
                        "for more strong stories from other outlets (never cut a good one).")
    # Credits in the text: about one per item reads naturally.
    credit = re.compile(r"\b((?i:according to|reported|citing)|told [A-Z]|per (?=[A-Z]))")
    body_lines = lines[:next((i for i, l in enumerate(lines) if l.startswith("## Sources")), len(lines))]
    total_credits = 0
    for i, line in enumerate(body_lines, 1):
        n = len(credit.findall(line))
        total_credits += n
        if n >= 3:
            warnings.append(f"Line {i}: {n} source credits in one item; keep the main one and let Sources carry the rest.")
    if total_credits > 25:
        errors.append(f"{total_credits} source credits in the text (limit 25; about 10 to 20 reads naturally). "
                      "Keep credits only where they add something: an exclusive, a disputed claim, a forecast, differing figures.")

    # Per section: credits on most stories, or one outlet behind most of them, means the section leans on
    # attribution or on one source. Both block publishing.
    word = r"[A-Z][\w'&-]*(?:\.\w+)*"
    outlet_re = re.compile(rf"(?:according to|citing|per) ({word}(?: (?:{word}|of|al|el))*)"
                           rf"|({word}(?: {word})*) reported")
    generic = {"News", "The", "Egyptian", "Officials", "State", "Local", "Reports", "Market", "Figures"}
    lead_re = re.compile(r"^\s*(?:[-*]\s+|\d+\.\s+)?\*\*[^*]+\*\*")
    for name in ("Egypt News", "Top World Headlines", "Regional and Gulf", "Egypt Markets", "Global Markets",
                 "Tech and AI", "Sports", "Health and Science", "Entertainment and Culture"):
        body = next((sec["parts"][name] for sec in sections.values() if name in sec["parts"]),
                    sections.get(name, {}).get("body"))
        if not body:
            continue
        items = [l for l in body if lead_re.match(l)]
        if len(items) < 3:
            continue
        credited = [l for l in items if credit.search(l)]
        if len(credited) * 2 > len(items):
            errors.append(f"{name}: {len(credited)} of {len(items)} stories carry a source credit; credit only where it adds "
                          "something and let Sources carry plain facts.")
        counts = {}
        for l in items:
            seen = set()
            for m in outlet_re.finditer(l):
                o = (m.group(1) or m.group(2) or "").strip().rstrip(".,;:")
                if o and o.split()[0] not in generic:
                    seen.add(o)
            for o in seen:
                counts[o] = counts.get(o, 0) + 1
        for o, n in counts.items():
            if n * 2 > len(items):
                errors.append(f"{name}: {o} is credited in {n} of {len(items)} stories; draw the section from at least three "
                              "outlets and check each story against a second one.")

    # Same story in two sections: compare bold lead-ins outside Today at a Glance and Sources.
    leads = []
    for name, sec in sections.items():
        if name in ("Today at a Glance", "The Week in Brief", "Sources"):
            continue
        chunks = [(name, sec["body"])] + [(p, b) for p, b in sec["parts"].items()]
        for where, body in chunks:
            for line in body:
                m = re.match(r"^\s*(?:[-*]|\d+\.)?\s*\*\*([^*]+?):?\*\*", line)
                if m:
                    toks = {w for w in re.findall(r"[a-z][a-z'-]+", m.group(1).lower())
                            if w not in STOP and len(w) > 2}
                    leads.append((where, m.group(1).strip(), toks))
    for i in range(len(leads)):
        for j in range(i + 1, len(leads)):
            a, b = leads[i], leads[j]
            if a[0] == b[0] or not a[2] or not b[2]:
                continue
            shared = a[2] & b[2]
            if len(shared) >= 2 or shared & STORY:
                warnings.append(f"Possible repeat: '{a[1]}' ({a[0]}) and '{b[1]}' ({b[0]}).")

    # Today at a Glance: every item links to its story, and the list ends with a What to watch line.
    anchors = {slug(n) for n in sections} | {slug(p) for sec in sections.values() for p in sec["parts"]}
    for name, sec in sections.items():
        if name in ("Today at a Glance", "Sources"):
            continue
        for body in [sec["body"]] + list(sec["parts"].values()):
            for line in body:
                m = re.match(r"^\s*(?:[-*]|\d+\.)?\s*\*\*([^*]+?)\*\*", line)
                if m:
                    anchors.add("story-" + slug(m.group(1).rstrip(":")))
    glance = sections.get("Today at a Glance", {}).get("body", [])
    for line in glance:
        if re.match(r"^\s*\d+\.", line):
            link = re.search(r"\]\(#([a-z0-9-]+)\)", line)
            if not link:
                errors.append(f"Today at a Glance item has no link to its story: {line.strip()[:80]}")
            elif link.group(1) not in anchors:
                errors.append(f"Today at a Glance link #{link.group(1)} matches no story lead-in or section.")
    if not recap and not any(re.match(r"^\s*\*\*What to watch today:\*\*", l) for l in glance):
        errors.append("Today at a Glance should end with a '**What to watch today:**' line.")

    # index.json must parse and list this date.
    # the calendar's Coming up is a dated list, not one running paragraph
    cal = re.search(r"^## Economic Calendar\n(.*?)(?=^## )", text, re.M | re.S)
    if cal:
        for para in re.split(r"\n\s*\n", cal.group(1)):
            p = para.strip()
            if p.startswith("**Coming up:**") and len(p.split()) > 25 and not re.search(r"^\s*[-*] ", p, re.M):
                warnings.append("Economic Calendar: write Coming up as a list, one date per line (- **Nov 15:** ...), not one paragraph.")
    date = os.path.splitext(os.path.basename(path))[0]
    index = os.path.join(os.path.dirname(path), "index.json")
    try:
        data = json.load(open(index, encoding="utf-8"))
        entry = next((e for e in data["editions"] if (e.get("id") or e.get("date")) == date), None)
        if not entry:
            errors.append(f"editions/index.json has no entry for {date}.")
        elif len(entry.get("summary", "")) >= 140:
            errors.append("The index.json summary must be under 140 characters.")
    except (OSError, ValueError, KeyError, TypeError) as e:
        errors.append(f"editions/index.json is not valid: {e}")

    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARNING:", w)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s). Words without Sources: {total}.")
    try:   # the result, for the Runs page
        import research_log
        research_log.record_check(date[:10], "recap" if date.endswith("-recap") else "newsletter", errors, warnings, words=total)
    except Exception:
        pass
    return 1 if errors else 0


if __name__ == "__main__":
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(paths) != 1:
        sys.exit(__doc__)
    sys.exit(main(paths[0]))
