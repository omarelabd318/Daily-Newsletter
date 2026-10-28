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
PARTS = {
    "Markets": ["Egypt Markets", "Global Markets"],
    "Stocks Watch": ["Egypt", "USA"],
    "In Other News": ["Tech and AI", "Sports", "Health and Science", "Entertainment and Culture"],
}
BUDGET = {
    "Today at a Glance": (150, 190), "Quick Hits": (70, 100), "Weather": (50, 80),
    "Egypt News": (450, 550), "Top World Headlines": (300, 380), "Regional and Gulf": (180, 230),
    "Egypt Markets": (280, 340), "Global Markets": (210, 260), "Stocks Watch": (100, 180),
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


def strip_quotes(line):
    return re.sub(r"\"[^\"]*\"|“[^”]*”", "", line)


def main(path):
    errors, warnings = [], []
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()

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

    if order != SECTIONS:
        missing = [s for s in SECTIONS if s not in order]
        extra = [s for s in order if s not in SECTIONS]
        msg = "Section titles or order do not match."
        if missing:
            msg += " Missing: " + ", ".join(missing) + "."
        if extra:
            msg += " Unexpected: " + ", ".join(extra) + "."
        errors.append(msg)
    for sec, parts in PARTS.items():
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
                if len(rows) < 10:
                    errors.append(f"Stocks Watch '{p}' should be a table with the 8 fixed stocks.")
                if prose:
                    warnings.append(f"Stocks Watch '{p}' should be a table only; found: {prose[0][:80]}")
            continue
        if sec["parts"]:
            for p, body in sec["parts"].items():
                counts[p] = words("\n".join(body))
        else:
            counts[name] = words("\n".join(sec["body"]))
    for name, (lo, hi) in BUDGET.items():
        n = counts.get(name)
        if n is not None and (n < lo * 0.7 or n > hi * 1.3):
            warnings.append(f"{name}: {n} words (budget {lo}-{hi}).")
    total = sum(counts.values())
    if not TOTAL[0] <= total <= TOTAL[1]:
        warnings.append(f"Total {total} words without Sources (target about 2,900-3,000).")

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

    # Same story in two sections: compare bold lead-ins outside Today at a Glance and Sources.
    leads = []
    for name, sec in sections.items():
        if name in ("Today at a Glance", "Sources"):
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

    # index.json must parse and list this date.
    date = os.path.splitext(os.path.basename(path))[0]
    index = os.path.join(os.path.dirname(path), "index.json")
    try:
        data = json.load(open(index, encoding="utf-8"))
        entry = next((e for e in data["editions"] if e.get("date") == date), None)
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
