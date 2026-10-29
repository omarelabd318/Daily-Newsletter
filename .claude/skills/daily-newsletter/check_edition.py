#!/usr/bin/env python3
"""Check a Daily Newsletter edition before it is committed.

Usage: python3 .claude/skills/daily-newsletter/check_edition.py editions/YYYY-MM-DD.md

Errors exit with code 1. Warnings are printed for a human (or Claude) to judge.
"""
import json
import os
import re
import sys

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
    "Currency and Commodities Watch": (110, 160), "Tech and AI": (130, 170), "Sports": (150, 200),
    "Health and Science": (70, 100), "Entertainment and Culture": (120, 150),
    "Economic Calendar": (130, 170), "Worth Knowing": (160, 200),
}
TOTAL = (2850, 3450)
# Words that break the voice rules. "US" is left out on purpose: it is usually the country.
VOICE = re.compile(r"\b(I|I'm|I've|we|We|we're|We're|our|Our|ours|my|My|me|Omar)\b")
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
            m = re.search(r"\(([A-Z.]{2,6})\)", cells[0]) if len(cells) >= 3 else None
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
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
