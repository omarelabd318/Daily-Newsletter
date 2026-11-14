#!/usr/bin/env python3
"""The dated items the Economic Calendar can start from, out of the repo's own data.

Usage:
  python3 .claude/skills/daily-newsletter/calendar_facts.py [DATE] [DAYS] [--draft]

Lists, for the DAYS after DATE (defaults: today, 14):
  - Egyptian public holidays and EGX closures (data/holidays.json; "expected" until the government confirms them);
  - results dates and dividends for the desk's stocks (desk/calendar.json, from TradingView; results dates are often
    TradingView's estimate, so write "expected" unless a company announcement confirms them);
  - dates the desk confirmed itself (each stock's "next" in desk/stocks.json).
The calendar still needs the day's research for everything else (central bank meetings, data releases, auctions,
fixtures); this only makes sure the dates already known are in it, and right.

With --draft it also prints a DRAFT of the whole section in the edition's layout: the last edition's calendar items
whose dates are still ahead (central bank meetings, data releases, fixtures found in earlier research) merged with the
dates above, the next three days as their own items and the rest under Coming up. Carried items are what earlier runs
checked; drop any that the day's research shows have moved or passed, add the day's new events, and keep the
holidays line at the end.
"""
import datetime
import glob
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def load(rel):
    try:
        return json.load(open(os.path.join(ROOT, rel)))
    except Exception:
        return {}


def main(a):
    flags = [x for x in a if x.startswith("--")]
    a = [x for x in a if not x.startswith("--")]
    start = datetime.date.fromisoformat(a[0]) if a else datetime.date.today()
    end = start + datetime.timedelta(days=int(a[1]) if len(a) > 1 else 14)
    st = (load("desk/stocks.json").get("stocks") or {})
    rows, plain = [], []   # plain: (date, wording for the edition, ticker or None)
    names = stock_names()
    for h in load("data/holidays.json").get("days", []):
        d = datetime.date.fromisoformat(h["date"])
        if start <= d <= end:
            rows.append((d, f"{h['name']}" + (" (EGX closed)" if h.get("egx_closed") else "") + (f" [{h.get('status')}]" if h.get("status") else "")))
            plain.append((d, h["name"] + (" (EGX closed)" if h.get("egx_closed") else "") + (" (expected)" if h.get("status") == "expected" else ""), None))
    cal = load("desk/calendar.json")
    for x in cal.get("items", []):
        d = datetime.date.fromisoformat(x["date"])
        if not start <= d <= end:
            continue
        if x["kind"] == "results":
            q = x.get("period")
            rows.append((d, f"{x['t']} results" + (f" for the quarter to {datetime.date.fromisoformat(q):%b %Y}" if q else "") + (f", {x['time']}" if x.get("time") else "")
                         + " [expected, TradingView]"))
            plain.append((d, f"{names.get(x['t'], x['t'])} results" + (f" ({x['time']})" if x.get("time") else "") + " (expected)", x["t"]))
        elif x["kind"] == "split":
            rows.append((d, f"{x['t']} stock split, {x['ratio']} [Polygon]"))
            plain.append((d, f"{names.get(x['t'], x['t'])} {x['ratio']} stock split takes effect", x["t"]))
        else:
            rows.append((d, f"{x['t']} goes ex-dividend, {'$' if x.get('cur') == '$' else 'EGP '}{x['amount']} a share" + (f", paid {x['pay']}" if x.get("pay") else "")
                         + (f" [declared {x['declared']}, Polygon]" if x.get("declared") else " [TradingView]")))
            amt = f"${x['amount']:g}" if x.get("cur") == "$" else f"EGP {x['amount']:g}"
            plain.append((d, f"{names.get(x['t'], x['t'])} trades without its {amt} dividend", x["t"]))
    for t, e in st.items():
        for n in e.get("next", []) or []:
            if n.get("date"):
                d = datetime.date.fromisoformat(n["date"])
                if start <= d <= end:
                    rows.append((d, f"{t}: {n['event']} [desk, confirmed]"))
                    plain.append((d, f"{names.get(t, t)}: {n['event']}", t))
    if not rows:
        print(f"Nothing in the repo's data between {start} and {end}.")
    for d, text in sorted(rows):
        print(f"{d:%a %b} {d.day}: {text}")
    print(f"(desk/calendar.json fetched {cal.get('fetched', 'never')})")
    if "--draft" in flags:
        draft(start, end, plain)


def stock_names():
    """Company names as earlier editions' Stocks Watch rows give them, so draft lines read 'Palm Hills', not PHDC."""
    names = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "editions", "20*.md")))[-60:]:
        for m in re.finditer(r"^\|\s*\*?([^|*()]+?) \(([A-Z.]{1,6})\)", open(f).read(), re.M):
            names[m.group(2)] = m.group(1).strip()
    return names


MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def parse_day(text, ref):
    """'Thursday, November 12' or 'Nov 16' or 'Nov 16-17' -> (first date, label suffix such as '-17')."""
    m = re.search(r"([A-Z][a-z]+)\.? (\d{1,2})(?:\s*[-\u2013]\s*((?:[A-Z][a-z]+\.? )?\d{1,2}))?", text)
    if not m or m.group(1)[:3].lower() not in MONTHS:
        return None, ""
    mon, day = MONTHS[m.group(1)[:3].lower()], int(m.group(2))
    year = ref.year + (1 if mon < ref.month - 6 else 0) - (1 if mon > ref.month + 6 else 0)
    try:
        return datetime.date(year, mon, day), (f"-{m.group(3)}" if m.group(3) else "")
    except ValueError:
        return None, ""


def carried(start):
    """The latest edition's calendar items (Economic Calendar, or the recap's The Week Ahead) dated on or after
    start: (date, range suffix, text)."""
    files = sorted((f for f in glob.glob(os.path.join(ROOT, "editions", "20*.md")) if os.path.basename(f)[:10] < start.isoformat()),
                   reverse=True)
    for f in files[:3]:
        sec = re.search(r"^## (?:Economic Calendar|The Week Ahead)\n(.*?)(?=^## )", open(f).read(), re.M | re.S)
        if sec:
            break
    else:
        return [], None
    out = []
    for line in sec.group(1).splitlines():
        m = re.match(r"\s*(?:- )?\*\*([^*]+?):\*\*\s*(.+)", line)
        if not m or m.group(1).lower().startswith("coming up"):
            continue
        if m.group(1).lower().startswith("later"):   # "Al Ahly vs Pyramids on November 23; the Fed decides on December 9"
            for part in re.split(r";\s*", m.group(2).rstrip(".")):
                d, _ = parse_day(part, start)
                if d and d >= start:
                    text = re.sub(r",?(?: is| are)? (?:on|before|by) [A-Z][a-z]+ \d{1,2}\b", "", part).strip()
                    out.append((d, "", text[0].upper() + text[1:]))
            continue
        d, suffix = parse_day(m.group(1), start)
        if d and (d >= start or (suffix and d + datetime.timedelta(days=7) >= start)):
            out.append((d, suffix, m.group(2).strip()))
    return out, os.path.basename(f)[:-3]


def draft(start, end, plain):
    old, src = carried(start)
    by = {}
    for d, suffix, text in old:
        if d < start:   # a range that began earlier and is still running
            d = start
        by.setdefault((d, suffix), []).extend(t.strip() for t in re.split(r";\s*", text.rstrip(".")) if t.strip())
    for d, text, t in plain:
        items = by.setdefault((d, ""), [])
        # skip a repo date the carried line already has (same company, or the same holiday)
        # the company's first distinctive word ("Palm" for Palm Hills Developments), or the holiday's name
        if t:
            w = re.split(r" results| trades|:", text)[0].split()
            key = " ".join(w[:2]) if w and w[0] in ("Egypt", "Egyptian", "Abu", "Alexandria", "The", "Commercial") else (w[0] if w else t)
        else:
            key = text.split(" (")[0]
        if any(key.lower() in i.lower() or t and t in i for i in items):
            continue
        items.append(text)
    soon = start + datetime.timedelta(days=2)
    print(f"\nDRAFT (carried from the {src} edition and the repo's data; check each carried item still holds, drop "
          "what moved or passed, add the day's new events):\n")
    later = []
    for (d, suffix), items in sorted(by.items()):
        if not items:
            continue
        if d <= soon and not suffix:
            print(f"**{d:%A}, {d:%B} {d.day}:** {'; '.join(items)}.\n")
        else:
            later.append(f"- **{d:%b} {d.day}{suffix}:** {'; '.join(items)}")
    if later:
        print("**Coming up:**\n")
        print("\n".join(later) + "\n")
    hol = [(d, t) for d, t, k in plain if k is None]
    if not hol:
        n = (end - start).days
        print(f"*No public holidays or EGX closures fall in the next {'two weeks' if n == 14 else f'{n} days'}.*")

if __name__ == "__main__":
    main(sys.argv[1:])
