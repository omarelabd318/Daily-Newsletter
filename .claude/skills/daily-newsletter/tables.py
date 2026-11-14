#!/usr/bin/env python3
"""Stocks Watch and Currency and Commodities Watch, built from the data log, ready to paste.

Usage (from the repo root, after log_figures.py has logged DATE):
  python3 .claude/skills/daily-newsletter/tables.py DATE [MOVER ...]

MOVER adds an italic "notable mover" row (up to three per market):
  egx.EAST                  a stock the log already holds (the desk's stocks): close, change and YTD from the log
  egx.MCQE=167.85,+8.5      any other stock: close and change from fetch_figures.py's mover lines (YTD n/a)
  us.ORCL=128.38,+8.8,-34.1 the same with YTD, which fetch_figures.py prints for US movers

Prints both sections' content (italic lines and tables) in the edition's format:
  - Close is the logged close for DATE; Change is the move from the previous session's logged close (weekend and
    holiday editions repeat the last close, so it steps back by trading session, not by edition), which is what
    check_edition.py compares; YTD is market_facts.py's figure.
  - The currency table's Notes are filled only where the log shows something worth a note (highest or lowest in
    at least three months, within 2% of the 52-week high or low), plus the dollar index's change and whether the
    pound's move is local or the dollar's. Edit, add or clear notes as the skill describes.
  - The rates, certificate and T-bill rows come from the log where it has them and otherwise from the latest
    edition; anything carried over is listed under CHECK at the end. Confirm those before publishing.
Then still check the figures against a second source as the skill says, mark any disputed figure (unconfirmed),
and paste the tables in. The checker runs on the result as usual.
"""
import datetime
import glob
import json
import os
import re
import sys
from decimal import ROUND_HALF_UP, Decimal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import market_facts as mf  # noqa: E402

ROOT = mf.ROOT
EGX = [("Commercial International Bank", "COMI"), ("Talaat Moustafa Group", "TMGH"), ("Telecom Egypt", "ETEL"),
       ("Palm Hills Developments", "PHDC"), ("Elsewedy Electric", "SWDY"), ("Orascom Construction", "ORAS"),
       ("Fawry", "FWRY"), ("Abu Qir Fertilizers", "ABUK"), ("EFG Holding", "HRHO"), ("Cleopatra Hospital", "CLHO"),
       ("Juhayna Food Industries", "JUFO"), ("Alexandria Containers", "ALCN")]
US = [("Apple", "AAPL"), ("Microsoft", "MSFT"), ("Nvidia", "NVDA"), ("Amazon", "AMZN"), ("Alphabet", "GOOGL"),
      ("Meta", "META"), ("Tesla", "TSLA"), ("JPMorgan Chase", "JPM"), ("Exxon Mobil", "XOM"), ("Broadcom", "AVGO"),
      ("Berkshire Hathaway", "BRK.B"), ("Walmart", "WMT")]
# NYSE full-day closures (the run's edition shows the last session before the edition date).
US_HOLIDAYS = {"2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03",
               "2026-09-07", "2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26",
               "2027-05-31", "2027-06-18", "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24"}
# Currency table rows: label, log key, decimals
FX = [("USD/EGP", "usd_egp", 2), ("US dollar index (DXY)", "dxy", 2), ("EUR/EGP", "eur_egp", 2), ("SAR/EGP", "sar_egp", 2),
      ("AED/EGP", "aed_egp", 2), ("KWD/EGP", "kwd_egp", 2), ("QAR/EGP", "qar_egp", 2), ("GBP/EGP", "gbp_egp", 2),
      ("Gold 21K (EGP/g)", "gold21_egp", 0), ("Gold 24K (EGP/g)", "gold24_egp", 0), ("Gold 18K (EGP/g)", "gold18_egp", 0),
      ("Gold pound (EGP)", "goldpound_egp", 0), ("Gold ($/oz)", "gold_usd", 2), ("Brent ($/bbl)", "brent", 2)]

NOTED = {"usd_egp", "dxy", "eur_egp", "gbp_egp", "gold21_egp", "gold_usd", "brent"}


def load(rel):
    return json.load(open(os.path.join(ROOT, rel)))


def day_name(d):
    return f"{d:%A}, {d:%B} {d.day}"


def egx_closed():
    try:
        return {h["date"]: h["name"] for h in load("data/holidays.json")["days"] if h.get("egx_closed")}
    except Exception:
        return {}


def egx_session(date, closed):
    """Last EGX session before the edition date (sessions Sunday to Thursday, the run is before the open)."""
    d = date - datetime.timedelta(days=1)
    while d.weekday() in (4, 5) or d.isoformat() in closed:
        d -= datetime.timedelta(days=1)
    return d


def us_session(date):
    d = date - datetime.timedelta(days=1)
    while d.weekday() >= 5 or d.isoformat() in US_HOLIDAYS:
        d -= datetime.timedelta(days=1)
    return d


def pct(a, b):
    return (a / b - 1) * 100 if a is not None and b else None


def sgn(x, dec=1):
    return "n/a" if x is None else f"{x:+.{dec}f}%"


def level(v, dec):
    """Rounded half up, as prices are quoted (521.125 is 521.13)."""
    if v is None:
        return "n/a"
    q = Decimal(repr(v)).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP)
    return f"{q:,.{dec}f}"


class Log:
    def __init__(self, date):
        self.date = date
        self.days = [d for d in load("data/markets.json")["days"] if d["date"] <= date.isoformat()]
        self.today = self.days[-1] if self.days and self.days[-1]["date"] == date.isoformat() else None
        self.series = mf.series(self.days, date.isoformat())

    def pts(self, group, key):
        out = []
        for d in self.days:
            v = (d.get(group) or {}).get(key) if group else d.get(key)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                out.append((d["date"], float(v)))
        return out

    def move(self, group, key, session_of):
        """Close for the edition date and the change from the previous session's close."""
        pts = self.pts(group, key)
        if not pts or pts[-1][0] != self.date.isoformat():
            return None, None
        now = session_of(self.date)
        prev = [v for d, v in pts[:-1] if session_of(datetime.date.fromisoformat(d)) < now]
        return pts[-1][1], pct(pts[-1][1], prev[-1]) if prev else None

    def ytd(self, name):
        p = self.series.get(name)
        f = mf.facts(name, p, self.date.isoformat()) if p else None
        return f["ytd"] if f else None

    def facts(self, key):
        name = mf.NAMES.get(key, key)
        p = self.series.get(name)
        return mf.facts(name, p, self.date.isoformat()) if p else None


def latest_edition(date):
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "editions", "20*.md"))
                   if os.path.basename(f)[:10] < date.isoformat())
    return files[-1] if files else None


def known_names():
    names = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "editions", "20*.md")))[-60:]:
        for m in re.finditer(r"^\|\s*\*?([^|*()]+?) \(([A-Z.]{1,6})\)", open(f).read(), re.M):
            names[m.group(2)] = m.group(1).strip()
    return names


def prev_row(text, pattern):
    m = re.search(r"^\|\s*" + pattern + r"[^\n]*$", text or "", re.M)
    return m.group(0) if m else None


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")] if row else []


def since_note(f, year):
    if not f:
        return ""
    if f["from_hi"] is not None and f["from_hi"] > -0.05:
        return "52-week high"
    if f["from_lo"] is not None and f["from_lo"] < 0.05:
        return "52-week low"
    if f.get("since"):
        label, ref = f["since"]
        if ref:
            r = datetime.date.fromisoformat(ref)
            return f"{label.capitalize()} since {r:%B}" + (f" {r.year}" if r.year != year else "")
        return f"{label.capitalize()} in the whole log"
    if f["from_hi"] is not None and f["from_hi"] > -2:
        return "Near its 52-week high"
    if f["from_lo"] is not None and f["from_lo"] < 2:
        return "Near its 52-week low"
    return ""


def main(args):
    if not args or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        sys.exit(__doc__)
    date = datetime.date.fromisoformat(args[0])
    log = Log(date)
    if not log.today:
        sys.exit(f"No figures logged for {date}: run log_figures.py first.")
    closed = egx_closed()
    egx_of = lambda d: egx_session(d, closed)  # noqa: E731
    es, us = egx_of(date), us_session(date)
    names = known_names()
    check = []

    movers = {"egx": [], "us": []}
    for a in args[1:]:
        m = re.fullmatch(r"(egx|us)\.([A-Z.]{1,6})(?:=([\d.,]+),([+\-]?[\d.]+)(?:,([+\-]?[\d.]+|n/a))?)?", a)
        if not m:
            sys.exit(f"Not a mover: {a} (egx.TICKER, or egx.TICKER=CLOSE,CHANGE[,YTD])")
        movers[m.group(1)].append(m.groups()[1:])
    for g in movers:
        if len(movers[g]) > 3:
            sys.exit(f"At most three movers per market ({g} has {len(movers[g])}).")

    print("## Stocks Watch\n")
    for title, group, fixed, sess, of in (("Egypt", "egx", EGX, es, egx_of), ("USA", "us", US, us, us_session)):
        print(f"### {title}\n")
        if group == "egx" and date.isoformat() in closed:
            print(f"*EGX closed today for {closed[date.isoformat()]}; last close {day_name(sess)}*\n")
        else:
            print(f"*{'EGX' if group == 'egx' else 'US'} close, {day_name(sess)}*\n")
        print("| Stock (ticker) | Close | Change | YTD |\n|---|---|---|---|")
        for name, t in fixed:
            close, chg = log.move(group, t, of)
            if close is None:
                check.append(f"{t}: not logged for {date}; find the close by hand or write n/a.")
            print(f"| {name} ({t}) | {level(close, 2)} | {sgn(chg)} | {sgn(log.ytd(t))} |")
        for t, c, ch, y in movers[group]:
            name = names.get(t, t)
            if name == t:
                check.append(f"{t}: company name not found in earlier editions; write it in the mover row.")
            if c is None:
                close, chg = log.move(group, t, of)
                ytd = log.ytd(t)
                if close is None:
                    check.append(f"{t}: not in the log; pass it as {group}.{t}=CLOSE,CHANGE from fetch_figures.py.")
            else:
                close, chg = float(c.replace(",", "")), float(ch)
                ytd = None if y in (None, "n/a") else float(y)
            print(f"| *{name} ({t}), notable mover* | {level(close, 2)} | {sgn(chg)} | {sgn(ytd)} |")
        print()

    prev_file = latest_edition(date)
    prev_text = open(prev_file).read() if prev_file else ""
    prev_date = os.path.basename(prev_file)[:-3] if prev_file else "?"
    E = log.today
    usd, dxy = log.facts("usd_egp"), log.facts("dxy")
    print("## Currency and Commodities Watch\n")
    print(f"*USD/EGP is the central bank's selling rate at {es:%A}'s close; other currencies are market mid-rates. "
          f"Brent, gold and the dollar index are {us:%A} closes.*\n")
    print("| Item | Level | Note | YTD |\n|---|---|---|---|")
    for label, key, dec in FX:
        v = E.get(key)
        if not isinstance(v, (int, float)):
            check.append(f"{label}: not logged for {date}; log it or write n/a.")
            v = None
        f = log.facts(key)
        # Gulf currencies follow the dollar and the other carats follow 21K: no note, so it is not repeated row after row
        note = since_note(f, date.year) if key in NOTED else ""
        if key == "dxy" and f and f["day"] is not None:
            rel = ""
            if usd and usd["day"] is not None and abs(usd["day"]) >= 0.1:
                if usd["day"] > 0:
                    rel = "dollar firmer worldwide" if f["day"] > 0 else "pound's fall is local"
                else:
                    rel = "pound firmer despite the dollar" if f["day"] > 0 else "dollar weaker worldwide"
            note = f"{f['day']:+.1f}%" + (f"; {(note or rel)[0].lower() + (note or rel)[1:]}" if (note or rel) else "")
        if key == "gold21_egp":
            note = "Retail price" + (f"; {note[0].lower() + note[1:]}" if note else "")
        print(f"| {label} | {level(v, dec)} | {note or ''}".rstrip() + f" | {sgn(f['ytd']) if f else 'n/a'} |")

    # rates: from the log, notes carried from the last edition when the rate has not changed
    dep, lend = E.get("cbe_deposit"), E.get("cbe_lending")
    old = cells(prev_row(prev_text, r"Overnight deposit"))
    if isinstance(dep, (int, float)) and isinstance(lend, (int, float)):
        lv = f"{dep:g}% / {lend:g}%"  # 20% / 21%, or 19.25% / 20.25%
        note = old[2] if len(old) > 2 and old[1] == lv else ""
        if not note:
            check.append("Rates row: the rate changed or the last edition has no row; add the effective date to the Note.")
        print(f"| Overnight deposit / lending rate | {lv} | {note}".rstrip() + " | — |")
    elif old:
        print("| " + " | ".join(old) + " |")
        check.append(f"Rates row carried from {prev_date}: not in today's log; confirm it at the central bank.")
    cert = prev_row(prev_text, r"Fixed certificates")
    if cert:
        print(cert)
        check.append(f"Certificates row carried from {prev_date}: confirm NBE's rate is unchanged.")
    else:
        check.append("No certificates row in the last edition: add one by hand.")
    tb = [(d["date"], d["tbill_364"]) for d in log.days if isinstance(d.get("tbill_364"), (int, float))]
    old = cells(prev_row(prev_text, r"T-bills, 1-year"))
    if tb:
        lv = f"{level(tb[-1][1], 2)}%"
        note = old[2] if len(old) > 2 and old[1] == lv else ""
        if not note:
            check.append(f"T-bill row: new auction result {lv} (first logged {tb[-1][0]}); write its auction date in the Note.")
        print(f"| T-bills, 1-year | {lv} | {note}".rstrip() + " | — |")
    elif old:
        print("| " + " | ".join(old) + " |")
        check.append(f"T-bill row carried from {prev_date}: confirm it is still the latest auction.")

    print("\nThese are the log's figures. Check them against a second source as the skill says, mark any disputed "
          "figure (unconfirmed), and edit the Notes where a short cause or milestone fits better.")
    if check:
        print("\nCHECK:")
        for c in check:
            print(f"- {c}")


if __name__ == "__main__":
    main(sys.argv[1:])
