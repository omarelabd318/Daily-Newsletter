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
WORDS = {"Sisi": "Seesee", "YTD": "year to date", "YoY": "year on year", "y/y": "year on year", "m/m": "month on month", "q/q": "quarter on quarter",
         "EGX30": "E G X thirty", "EGX70": "E G X seventy", "EGX100": "E G X one hundred", "S&P 500": "S and P 500",
         "S&P": "S and P", "CBE": "C B E", "IMF": "I M F", "GDP": "G D P", "OPEC+": "OPEC plus", "vs": "versus", "vs.": "versus",
         "Q1": "the first quarter", "Q2": "the second quarter", "Q3": "the third quarter", "Q4": "the fourth quarter"}
MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "Jun": "June", "Jul": "July", "Aug": "August",
          "Sep": "September", "Sept": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
SAY = {"NATO", "OPEC", "NASA", "FIFA", "UEFA", "COVID", "ASEAN", "BRICS", "SWIFT", "LIBOR", "SOFR", "MENA", "NEOM",
       "AFCON", "AIDS", "IKEA", "LEGO", "ISIS", "CAPMAS", "UNICEF", "UNESCO", "SIM", "PIN", "LASER", "RAM", "GIF"}
ROMAN = re.compile(r"(?:X{0,3})(?:IX|IV|V?I{0,3})")
UNITS = {"tn": "trillion", "bn": "billion", "mn": "million", "m": "million", "k": "thousand"}


def strip_md(t):
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_`]+", "", t)
    return re.sub(r"\s+", " ", t).strip()


def speakable(t):
    """Figures and abbreviations as they are said: EGP 54.01 -> 54.01 pounds, 3.9% -> 3.9 percent, $4bn -> 4 billion dollars."""
    num = r"(\d+(?:,\d{3})*(?:\.\d+)?)"   # 76,000 or 4.5, never a comma after it
    # EGP 48bn, EGP 48 billion and EGP 54.01: the amount, its unit, then "pounds" (48 billion pounds)
    t = re.sub(r"\bEGP\s?" + num + r"(?:\s?(tn|bn|mn|m|k)\b|\s(trillion|billion|million|thousand)\b)?",
               lambda m: m.group(1) + (" " + UNITS[m.group(2)] if m.group(2) else " " + m.group(3) if m.group(3) else "") + " pounds", t)
    t = re.sub(r"\$" + num + r"\s?(tn|bn|mn|m|k)\b", lambda m: m.group(1) + " " + UNITS[m.group(2)] + " dollars", t)
    t = re.sub(r"\$" + num + r"(?:\s(trillion|billion|million|thousand))?", lambda m: m.group(1) + (" " + m.group(2) if m.group(2) else "") + " dollars", t)
    # other currencies by code or sign: EUR 4.10 -> 4.1 euros (a price's trailing zero is not said)
    cur = {"EUR": "euros", "€": "euros", "GBP": "pounds sterling", "£": "pounds sterling", "AED": "dirhams", "SAR": "riyals", "QAR": "riyals", "KWD": "dinars"}
    t = re.sub(r"(?:\b(EUR|GBP|AED|SAR|QAR|KWD)\s?|([€£]))" + num + r"(?:\s?(tn|bn|mn|m|k)\b|\s(trillion|billion|million|thousand)\b)?",
               lambda m: re.sub(r"(\.\d*?)0+$", r"\1", m.group(3)).rstrip(".") + (" " + UNITS[m.group(4)] if m.group(4) else " " + m.group(5) if m.group(5) else "") + " " + cur[m.group(1) or m.group(2)], t)
    t = re.sub(r"(\d)-a-(share|day|year|month|week|barrel|ton|tonne|gram|head|night)\b", r"\1 a \2", t)
    t = re.sub(r"(dollars|pounds|euros|riyals|dirhams)-a-", r"\1 a ", t)
    t = re.sub(r"\b" + num + r"\s?bps?\b", r"\1 basis points", t)
    t = re.sub(num + r"\s?%", r"\1 percent", t)
    t = re.sub(r"\s?°C\b", " degrees", t)
    # times: 10pm and 10 p.m. -> "10 P-M", said as two letters (with full stops the voice paused after each)
    # (a full stop after "p.m." that also ends the sentence is kept)
    t = re.sub(r"\b(\d{1,2}(?::\d\d)?)\s?(a\.?m\.?|p\.?m\.?)(?=([\s,;)]|$))",
               lambda m: m.group(1) + (" A-M" if m.group(2)[0] == "a" else " P-M") + ("." if m.group(2).endswith(".") and re.match(r"\s+[A-Z\"\u201c]|\s*$", m.string[m.end():]) else ""), t)
    t = re.sub(r"(\d)\s?[–—-]\s?(\d)", r"\1 to \2", t)            # ranges: 7–20, 2026–27
    t = re.sub(r"\b(\d{1,2}) (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b", r"\2 \1", t)
    t = re.sub(r"(?<![\w.])([+−-])(\d)", lambda m: ("plus " if m.group(1) == "+" else "minus ") + m.group(2), t)
    for k, v in MONTHS.items():
        t = re.sub(r"\b" + k + r"\.?(?= \d)", v, t)
    for k, v in WORDS.items():
        t = re.sub(r"(?<![\w&])" + re.escape(k) + r"(?![\w&])", v, t)
    # short all-caps abbreviations are spelled out (IPO, CIB, US, AI), except those said as words (NATO, OPEC)
    t = re.sub(r"\b[A-Z]{2,5}\b", lambda m: m.group(0) if m.group(0) in SAY or ROMAN.fullmatch(m.group(0)) else " ".join(m.group(0)), t)
    # a unit said once: "207.4 million dollars from 110.2 million dollars" -> "207.4 million dollars from 110.2 million"
    t = re.sub(r"(\d[\d.,]*(?: (?:trillion|billion|million|thousand))? (dollars|pounds|euros|percent)) (from|to|against|versus) (\d[\d.,]*(?: (?:trillion|billion|million|thousand))?) \2\b", r"\1 \3 \4", t)
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


def source(key):
    """The text a key is read from: an edition, or the desk's spoken summary (desk-DATE, from desk_audio.py)."""
    if key.startswith("desk-"):
        return os.path.join(ROOT, "desk", "listen", key[5:] + ".md")
    return os.path.join(ROOT, "editions", key + ".md")


def load(key):
    return blocks(open(source(key)).read())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    for b in load(sys.argv[1]):
        print(f"[{b['sec']} / {b['kind']}] {speakable(b['text'])}")
