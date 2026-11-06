#!/usr/bin/env python3
"""The edition as spoken text: the blocks the site's Listen player reads, in order, with the figures written the way
they are said. Shared by the device-voice player (index.html mirrors these rules) and make_audio.py.

Usage (from the repo root):
  python3 .claude/skills/daily-newsletter/read_aloud.py EDITION      print the blocks (EDITION: 2026-11-06)

Read: every section but Sources and the two watch tables, and only its text: headings, paragraphs and list items.
Other tables are skipped, and so is a section with no text.
"""
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SKIP = {"Sources", "Stocks Watch", "Stocks This Week", "Currency and Commodities Watch"}   # tables: read on the page
WORDS = {"YTD": "year to date", "YoY": "year on year", "y/y": "year on year", "m/m": "month on month", "q/q": "quarter on quarter",
         "EGX30": "E G X thirty", "EGX70": "E G X seventy", "EGX100": "E G X one hundred", "S&P 500": "S and P five hundred",
         "S&P": "S and P", "CBE": "C B E", "IMF": "I M F", "GDP": "G D P", "OPEC+": "OPEC plus", "vs": "versus", "vs.": "versus",
         "Q1": "the first quarter", "Q2": "the second quarter", "Q3": "the third quarter", "Q4": "the fourth quarter"}
MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "Jun": "June", "Jul": "July", "Aug": "August",
          "Sep": "September", "Sept": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
UNITS = {"tn": "trillion", "bn": "billion", "mn": "million", "m": "million", "k": "thousand"}


def strip_md(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`]+", "", t)
    return re.sub(r"\s+", " ", t).strip()


def speakable(t):
    """Figures and abbreviations as they are said: EGP 54.01 -> 54.01 pounds, 3.9% -> 3.9 percent, $4bn -> 4 billion dollars."""
    num = r"(\d[\d,]*(?:\.\d+)?)"
    t = re.sub(r"\bEGP\s?" + num + r"\s?(tn|bn|mn|m|k)?\b", lambda m: m.group(1) + (" " + UNITS[m.group(2)] if m.group(2) else "") + " pounds", t)
    t = re.sub(r"\$" + num + r"\s?(tn|bn|mn|m|k)\b", lambda m: m.group(1) + " " + UNITS[m.group(2)] + " dollars", t)
    t = re.sub(r"\$" + num + r"(?:\s(trillion|billion|million|thousand))?", lambda m: m.group(1) + (" " + m.group(2) if m.group(2) else "") + " dollars", t)
    t = re.sub(r"\b" + num + r"\s?bps?\b", r"\1 basis points", t)
    t = re.sub(num + r"\s?%", r"\1 percent", t)
    t = re.sub(r"\s?°C\b", " degrees", t)
    t = re.sub(r"\b(\d{1,2}(?::\d\d)?)\s?(am|pm)\b", lambda m: m.group(1) + (" a.m." if m.group(2) == "am" else " p.m."), t)
    t = re.sub(r"(\d)\s?[–—-]\s?(\d)", r"\1 to \2", t)            # ranges: 7–20, 2026–27
    t = re.sub(r"\b(\d{1,2}) (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b", r"\2 \1", t)
    t = re.sub(r"(?<![\w.])([+−-])(\d)", lambda m: ("plus " if m.group(1) == "+" else "minus ") + m.group(2), t)
    for k, v in MONTHS.items():
        t = re.sub(r"\b" + k + r"\.?(?= \d)", v, t)
    for k, v in WORDS.items():
        t = re.sub(r"(?<![\w&])" + re.escape(k) + r"(?![\w&])", v, t)
    t = t.replace("&", " and ").replace("/", " ").replace("·", ",").replace("→", "")
    return re.sub(r"\s+", " ", t).strip()


def blocks(md):
    """[{sec, kind, text}] in reading order; kind is section, heading or text."""
    out, sec, para = [], None, []

    def flush():
        if para and sec:
            out.append({"sec": sec, "kind": "text", "text": strip_md(" ".join(para))})
        para.clear()

    for line in md.splitlines():
        s = line.strip()
        h = re.match(r"^(#{2,4})\s+(.*)$", s)
        if h:
            flush()
            title = strip_md(h.group(2))
            if len(h.group(1)) == 2:
                sec = None if title in SKIP else title
                if sec:
                    out.append({"sec": sec, "kind": "section", "text": title})
            elif sec:
                out.append({"sec": sec, "kind": "heading", "text": title})
            continue
        if not sec or s.startswith("# "):
            continue
        if not s or s.startswith("|") or re.match(r"^(-{3,}|\*{3,})$", s):
            flush()
            continue
        li = re.match(r"^(?:[-*+]|\d+[.)])\s+(.*)$", s)
        if li:
            flush()
            para.append(li.group(1))
            flush()
            continue
        para.append(re.sub(r"^>\s?", "", s))
    flush()
    out = [b for b in out if b["text"]]
    # a subhead with no text under it (Stocks Watch's "Egypt" over a table) is skipped, and so is a section with no text
    out = [b for i, b in enumerate(out) if b["kind"] != "heading" or (i + 1 < len(out) and out[i + 1]["kind"] == "text")]
    keep = {b["sec"] for b in out if b["kind"] == "text"}
    out = [b for b in out if b["sec"] in keep]
    n = {}
    for b in out:   # each block's place in its section: the key the site matches the audio's timings on
        b["n"] = n[b["sec"]] = n.get(b["sec"], -1) + 1
    return out


def load(key):
    return blocks(open(os.path.join(ROOT, "editions", key + ".md")).read())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    for b in load(sys.argv[1]):
        print(f"[{b['sec']} / {b['kind']}] {speakable(b['text'])}")
