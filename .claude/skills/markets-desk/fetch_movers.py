#!/usr/bin/env python3
"""Save the last finished session's biggest gainers and losers across the whole market, for the desk.

Usage:
  python3 .claude/skills/markets-desk/fetch_movers.py

Writes desk/movers.json: the ten biggest rises and falls among all EGX stocks (Mubasher's price list) and
among US companies worth $10bn or more (Nasdaq's screener of every listed stock). Thinly traded stocks are
left out so a few trades cannot top the list: on the EGX, those that traded under EGP 1m in the session.
A market still trading keeps the session already saved. Prints one line per market.
"""
import datetime
import json
import os
import re
import sys
import urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "movers.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
NY, CAIRO = ZoneInfo("America/New_York"), ZoneInfo("Africa/Cairo")
MIN_TURNOVER_EGP, MIN_CAP_USD, TOP = 1e6, 10e9, 10


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40).read().decode("utf-8", "replace")


def num(s):
    s = re.sub(r"[^\d.\-]", "", str(s or ""))
    return float(s) if s not in ("", "-", ".") else None


def rank(rows):
    rows = sorted(rows, key=lambda r: r["pct"], reverse=True)
    return {"gainers": rows[:TOP], "losers": [r for r in reversed(rows) if r["pct"] < 0][:TOP], "count": len(rows)}


def egx():
    d = json.loads(get("https://english.mubasher.info/api/1/stocks/prices?country=eg"))
    session = d["lastUpdate"][:10]
    now = datetime.datetime.now(CAIRO)
    if session == now.date().isoformat() and now.strftime("%H:%M") < "14:45":
        return None, f"EGX: {session} is still trading; kept the saved session"
    rows = []
    for p in d["prices"]:
        pct, price, turnover = num(p.get("changePercentage")), num(p.get("value")), num(p.get("turnover"))
        if pct is None or price is None or (turnover or 0) < MIN_TURNOVER_EGP:
            continue
        rows.append({"t": p["code"], "name": p["name"], "price": price, "pct": pct, "turnover": turnover})
    out = rank(rows)
    out.update(session=session, basis=f"All EGX stocks that traded at least EGP 1m ({out['count']} on the day)")
    return out, f"EGX: {session}, {out['count']} stocks"


def us():
    now = datetime.datetime.now(NY)
    if now.weekday() < 5 and "09:30" <= now.strftime("%H:%M") < "16:15":
        return None, "US: the market is trading; kept the saved session"
    # the last finished session: today after the close, otherwise the weekday before
    d = now.date() if now.weekday() < 5 and now.strftime("%H:%M") >= "16:15" else now.date() - datetime.timedelta(days=1)
    while d.weekday() >= 5:
        d -= datetime.timedelta(days=1)
    rows = []
    for r in json.loads(get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true"))["data"]["rows"]:
        cap, pct, price = num(r.get("marketCap")), num(r.get("pctchange")), num(r.get("lastsale"))
        if not cap or cap < MIN_CAP_USD or pct is None or price is None or "^" in r["symbol"] or "/" in r["symbol"]:
            continue
        name = re.sub(r"\s+(Common Stock|Ordinary Shares|Class [A-C].*|American Depositary Shares.*|Inc\.?$).*$", "", r["name"]).strip(" ,.")
        rows.append({"t": r["symbol"], "name": name, "price": price, "pct": pct, "cap": cap})
    out = rank(rows)
    out.update(session=d.isoformat(), basis=f"US companies worth $10bn or more ({out['count']})")
    return out, f"US: {d}, {out['count']} companies"


def main():
    saved = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for name, fn in (("egx", egx), ("us", us)):
        try:
            data, line = fn()
        except Exception as e:
            data, line = None, f"{name.upper()}: failed ({e}); kept the saved session"
        if data and data["session"] >= (saved.get(name) or {}).get("session", ""):
            saved[name] = data
        print(line)
    saved["note"] = "Biggest gainers and losers of the last finished session across the whole market. Written by fetch_movers.py."
    with open(OUT, "w") as f:
        json.dump(saved, f, separators=(",", ":"), ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    sys.exit(main())
