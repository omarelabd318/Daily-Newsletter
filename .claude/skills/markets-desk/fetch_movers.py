#!/usr/bin/env python3
"""Save the last finished session's biggest gainers and losers across the whole market, for the desk.

Usage:
  python3 .claude/skills/markets-desk/fetch_movers.py           save the movers
  python3 .claude/skills/markets-desk/fetch_movers.py --leads   then list news leads for the top five each way

For the reasons: open the leads, check the cause at the outlet, and write it into desk/movers.json as
"why" (one short line), "source" and "url" on that stock's row. Leave "why" out when no reason is found;
"no news found" is a fact worth stating only when the move is large (5% or more).

Writes desk/movers.json: the ten biggest rises and falls among all EGX stocks (Mubasher's price list) and
among US companies worth $10bn or more (Nasdaq's screener of every listed stock). Thinly traded stocks are
left out so a few trades cannot top the list: on the EGX, those that traded under EGP 1m in the session.
A market still trading keeps the session already saved. Prints one line per market.

It also refreshes each desk stock's market value in desk/stocks.json ("cap"), which the stock lists sort
by: Egyptian stocks from Mubasher's stock pages, US stocks from the same Nasdaq screener.
"""
import concurrent.futures
import datetime
import html
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
    try:   # Arabic names, for searching Egyptian news about smaller companies
        ar = {p["code"]: p["name"] for p in json.loads(get("https://www.mubasher.info/api/1/stocks/prices?country=eg"))["prices"]}
    except Exception:
        ar = {}
    session = d["lastUpdate"][:10]
    now = datetime.datetime.now(CAIRO)
    if session == now.date().isoformat() and now.strftime("%H:%M") < "14:45":
        return None, f"EGX: {session} is still trading; kept the saved session"
    rows = []
    for p in d["prices"]:
        pct, price, turnover = num(p.get("changePercentage")), num(p.get("value")), num(p.get("turnover"))
        if pct is None or price is None or (turnover or 0) < MIN_TURNOVER_EGP:
            continue
        rows.append({"t": p["code"], "name": p["name"], "ar": ar.get(p["code"]), "price": price, "pct": pct, "turnover": turnover})
    out = rank(rows)
    out.update(session=session, basis=f"All EGX stocks that traded at least EGP 1m ({out['count']} on the day)")
    return out, f"EGX: {session}, {out['count']} stocks"


DESK = {"egx": ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL"],
        "us": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST"]}
SCREENER = []
# listed but not yet trading: Mubasher's market value for them predates the offering
NOT_TRADING = {"BQDC"} if datetime.date.today() < datetime.date(2026, 11, 2) else set()


def screener():
    if not SCREENER:
        SCREENER.extend(json.loads(get("https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&download=true"))["data"]["rows"])
    return SCREENER


def mubasher_cap(t):
    page = get(f"https://english.mubasher.info/markets/EGX/stocks/{t}")
    text = re.sub(r"\s*\|[\s|]*", "|", html.unescape(re.sub(r"<[^>]+>", "|", re.sub(r"<(script|style)[^>]*>.*?</\1>", "", page, flags=re.S))))
    m = re.search(r"Market Cap\|([\d,.]+)", text)
    return num(m.group(1)) if m else None


def caps():
    """Market value of each desk stock, in billions of its currency, into desk/stocks.json."""
    path = os.path.join(ROOT, "desk", "stocks.json")
    data = json.load(open(path))
    today = datetime.date.today().isoformat()
    found = {}
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        for t, v in zip(DESK["egx"], pool.map(lambda t: _safe(mubasher_cap, t), DESK["egx"])):
            if v and t not in NOT_TRADING:
                found[t] = {"value": round(v / 1e9, 1), "currency": "EGP", "date": today, "source": "Mubasher"}
    try:
        rows = {r["symbol"]: r for r in screener()}
        for t in DESK["us"]:
            v = num((rows.get(t.replace(".", "/")) or {}).get("marketCap"))
            if v:
                found[t] = {"value": round(v / 1e9, 1), "currency": "USD", "date": today, "source": "Nasdaq"}
    except Exception:
        pass
    for t, c in found.items():
        data["stocks"].setdefault(t, {})["cap"] = c
    with open(path, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    return f"Market values: {len(found)} of {len(DESK['egx']) + len(DESK['us'])} updated"


def _safe(fn, *a):
    try:
        return fn(*a)
    except Exception:
        return None


def us():
    now = datetime.datetime.now(NY)
    if now.weekday() < 5 and "09:30" <= now.strftime("%H:%M") < "16:15":
        return None, "US: the market is trading; kept the saved session"
    # the last finished session: today after the close, otherwise the weekday before
    d = now.date() if now.weekday() < 5 and now.strftime("%H:%M") >= "16:15" else now.date() - datetime.timedelta(days=1)
    while d.weekday() >= 5:
        d -= datetime.timedelta(days=1)
    rows = []
    for r in screener():
        cap, pct, price = num(r.get("marketCap")), num(r.get("pctchange")), num(r.get("lastsale"))
        if not cap or cap < MIN_CAP_USD or pct is None or price is None or "^" in r["symbol"] or "/" in r["symbol"]:
            continue
        name = re.sub(r"\s+(Common Stock|Ordinary Shares|Class [A-C].*|American Depositary Shares.*|Inc\.?$).*$", "", r["name"]).strip(" ,.")
        rows.append({"t": r["symbol"], "name": name, "price": price, "pct": pct, "cap": cap})
    out = rank(rows)
    out.update(session=d.isoformat(), basis=f"US companies worth $10bn or more ({out['count']})")
    return out, f"US: {d}, {out['count']} companies"


def leads(saved):
    """News leads for the top five gainers and losers in each market, from the last two days."""
    sys.path.insert(0, os.path.dirname(__file__))
    import stock_news as sn
    for m in ("egx", "us"):
        X = saved.get(m)
        if not X:
            continue
        print(f"\n# {m.upper()} {X['session']}")
        for side in ("gainers", "losers"):
            for r in X[side][:5]:
                q = f'"{r["ar"]}"' if m == "egx" and r.get("ar") else f'"{r["name"]}" stock'
                core = (r.get("ar") or r["name"]).split()[0] if m == "egx" else r["name"].split()[0]
                try:
                    rows = sn.google(q, 3, arabic=(m == "egx" and bool(r.get("ar"))))
                except Exception as e:
                    rows = []
                rows = [x for x in sorted(rows, key=lambda x: x[0], reverse=True) if core in x[2]][:4]
                print(f"## {r['t']} {r['pct']:+.1f}%  {r['name']}")
                for w, o, t, l in rows:
                    print(f"- {w:%a %d %b} | {o} | {t}\n  {sn.resolve(l)}")
                if not rows:
                    print("- no headlines found")


def main():
    saved = json.load(open(OUT)) if os.path.exists(OUT) else {}
    for name, fn in (("egx", egx), ("us", us)):
        try:
            data, line = fn()
        except Exception as e:
            data, line = None, f"{name.upper()}: failed ({e}); kept the saved session"
        if data and data["session"] >= (saved.get(name) or {}).get("session", ""):
            old = saved.get(name) or {}
            if old.get("session") == data["session"]:   # same session again: keep the reasons already written
                notes = {r["t"]: r for side in ("gainers", "losers") for r in old.get(side, []) if r.get("why")}
                for side in ("gainers", "losers"):
                    for r in data[side]:
                        for k in ("why", "source", "url"):
                            if r["t"] in notes and k in notes[r["t"]]:
                                r[k] = notes[r["t"]][k]
            saved[name] = data
        print(line)
    print(caps())
    saved["note"] = "Biggest gainers and losers of the last finished session across the whole market. Written by fetch_movers.py."
    with open(OUT, "w") as f:
        json.dump(saved, f, separators=(",", ":"), ensure_ascii=False)
        f.write("\n")
    if "--leads" in sys.argv:
        leads(saved)


if __name__ == "__main__":
    sys.exit(main())
