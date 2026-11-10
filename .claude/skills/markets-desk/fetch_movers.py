#!/usr/bin/env python3
"""Save the last finished session's biggest gainers and losers across the whole market, for the desk.

Usage:
  python3 .claude/skills/markets-desk/fetch_movers.py           save the movers
  python3 .claude/skills/markets-desk/fetch_movers.py --leads   then list news leads for the top five each way

For the reasons: open the leads, check the cause at the outlet, and write it into desk/movers.json as
"why" (one short line), "source" and "url" on that stock's row. Leave "why" out when no reason is found;
"no news found" is a fact worth stating only when the move is large (5% or more).

Also saves each market's biggest movers over the past week and month ("week", "month", from TradingView's screener)
and the reasons written in the last 31 days ("why_log"), which those lists reuse.

Writes desk/movers.json: the EGX session's breadth (how many stocks that traded rose, fell or were unchanged),
and the ten biggest rises and falls and the ten most traded by value ("active") among all EGX stocks (Mubasher's price list) and
among US companies worth $10bn or more (TradingView's screener). Thinly traded stocks are
left out so a few trades cannot top the list: on the EGX, those that traded under EGP 1m in the session.
While the EGX trades (the desk runs after its 10:00 open), the session that just finished is read from
TradingView's previous-bar closes; a US market still trading keeps the session already saved. Prints one line per market.

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
    """The ten biggest rises and falls, and the ten most active (by value traded, where the rows have it)."""
    by = sorted(rows, key=lambda r: r["pct"], reverse=True)
    out = {"gainers": by[:TOP], "losers": [r for r in reversed(by) if r["pct"] < 0][:TOP], "count": len(rows)}
    if any(r.get("turnover") for r in rows):
        out["active"] = sorted((r for r in rows if r.get("turnover")), key=lambda r: r["turnover"], reverse=True)[:TOP]
    return out


def weekly(market):
    """The past week's and past month's ten biggest rises and falls across the whole market, from TradingView's screener
    (its weekly and monthly changes, measured from slightly different days than the desk's own, so the page labels the
    source). Returns {"week": ..., "month": ...}. The
    same liquidity rules as the day's list: EGX stocks trading at least EGP 1m a day on average, US companies worth
    $10bn or more (common stock only)."""
    flt = [{"left": "type", "operation": "equal", "right": "stock"}]
    if market == "us":
        flt += [{"left": "market_cap_basic", "operation": "greater", "right": MIN_CAP_USD},
                {"left": "exchange", "operation": "in_range", "right": ["NYSE", "NASDAQ", "AMEX"]}]   # not over-the-counter shares
    body = json.dumps({"filter": flt, "columns": ["name", "description", "close", "Perf.W", "Perf.1M", "average_volume_10d_calc", "Perf.All"],
                       "range": [0, 3000]}).encode()
    req = urllib.request.Request(f"https://scanner.tradingview.com/{'egypt' if market == 'egx' else 'america'}/scan",
                                 data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    names = {}
    if market == "egx":   # Mubasher's company names, as on the day's list (TradingView's carry the odd typo)
        try:
            names = {p["code"]: p["name"] for p in json.loads(get("https://english.mubasher.info/api/1/stocks/prices?country=eg"))["prices"]}
        except Exception:
            pass
    rows = {"week": [], "month": []}
    # TradingView lists a few EGX stocks only by their ISIN (EGS3I0S1C019): find the ticker on Mubasher by company name
    namekey = lambda n: re.sub(r"[^a-z]", "", re.sub(r"\(.*?\)", "", n.lower()))[:24]
    by_name = {namekey(n): c for c, n in names.items()}
    for r in json.loads(urllib.request.urlopen(req, timeout=40).read())["data"]:
        sym, name, close, wk, mo, vol, alltime = r["d"]
        if market == "egx" and re.fullmatch(r"EG[A-Z0-9]{10}", sym or ""):
            sym = by_name.get(namekey(name or ""), sym)
        name = names.get(sym, name)
        if not close or "/" in sym or "." in sym and market == "egx":
            continue
        if market == "egx" and (vol or 0) * close < MIN_TURNOVER_EGP:
            continue
        name = re.sub(r"\s*\([A-Z0-9]{2,6}\)$", "", name)   # Mubasher's "(FCMI)" after a name
        name = re.sub(r"\s+Class [A-C]\b.*$", "", name)
        name = re.sub(r",?\s+(Inc\.?|Corp\.?|Corporation|Co\.?|plc|N\.V\.|S\.A\.E\.?|SAE|Ltd\.?|Company)$", "", name).strip(" ,.")
        for key, v in (("week", wk), ("month", mo)):
            # a stock listed within the period has no price before it: TradingView then measures the change from an
            # old reference price (Banque du Caire's EGP 4.00 par against its 5.30 offer), the same figure as its
            # all-time change, so it is left off that list
            if v is not None and alltime is not None and abs(v - alltime) < 0.01:
                continue
            if v is not None:
                rows[key].append({"t": sym, "name": name, "price": close, "pct": round(v, 2)})
    out = {}
    for key, label in (("week", "Past week, TradingView"), ("month", "Past month, TradingView")):
        out[key] = rank(rows[key])
        out[key].update(basis=label, note=("EGX stocks trading at least EGP 1m a day on average" if market == "egx" else "US companies worth $10bn or more") + f" ({out[key]['count']})")
    return out


def indices():
    """The EGX30 and the EGX70 EWI over the day, week, month and year so far, from TradingView's screener: the EGX70
    EWI has no history the desk can backfill (Mubasher carries the index it replaced), so its changes come from here."""
    body = json.dumps({"symbols": {"tickers": ["EGX:EGX30", "EGX:EGX70EWI"]}, "columns": ["close", "change", "Perf.W", "Perf.1M", "Perf.YTD"]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/egypt/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    out = {}
    for r in json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]:
        close, day, w, m, ytd = r["d"]
        out[r["s"].split(":")[1]] = {"close": close, "day": day, "week": w, "month": m, "ytd": ytd}
    return out


def previous_egx_session(today):
    """The last finished EGX session before today: the intraday file's session when it is earlier, otherwise the
    weekday (Sunday to Thursday) before today."""
    try:
        sess = json.load(open(os.path.join(ROOT, "desk", "intraday.json")))["egx"]["session"]
        if sess < today.isoformat():
            return sess
    except Exception:
        pass
    d = today - datetime.timedelta(days=1)
    while d.weekday() in (4, 5):   # Friday, Saturday
        d -= datetime.timedelta(days=1)
    return d.isoformat()


def egx_previous(d, ar, today):
    """The finished session's movers and breadth while the next session trades: each stock's last two closes
    (close[1], close[2]) and turnover (Value.Traded[1]) from TradingView's screener, named from Mubasher's list."""
    names = {p["code"]: p["name"] for p in d["prices"]}
    body = json.dumps({"filter": [{"left": "type", "operation": "equal", "right": "stock"}],
                       "columns": ["name", "description", "close[1]", "close[2]", "Value.Traded[1]"], "range": [0, 1000]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/egypt/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    rows, breadth = [], {"up": 0, "down": 0, "flat": 0}
    for r in json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]:
        code, desc, c1, c2, turnover = r["d"]
        if not c1 or not c2:
            continue
        pct = round((c1 / c2 - 1) * 100, 2)
        if (turnover or 0) > 0:
            breadth["up" if pct > 0 else "down" if pct < 0 else "flat"] += 1
        if (turnover or 0) < MIN_TURNOVER_EGP or code not in names:   # Mubasher's list names the stock and drops ISIN-coded duplicates
            continue
        rows.append({"t": code, "name": names[code], "ar": ar.get(code), "price": round(c1, 3), "pct": pct, "turnover": round(turnover, 2)})
    if len(rows) < 50:
        raise RuntimeError(f"only {len(rows)} stocks")
    session = previous_egx_session(today)
    out = rank(rows)
    out.update(session=session, basis=f"All EGX stocks that traded at least EGP 1m ({out['count']} on the day)", breadth=breadth, breadthSource="TradingView")
    return out, f"EGX: {session} (read during the next session from TradingView's previous closes), {out['count']} stocks"


def egx():
    d = json.loads(get("https://english.mubasher.info/api/1/stocks/prices?country=eg"))
    try:   # Arabic names, for searching Egyptian news about smaller companies
        ar = {p["code"]: p["name"] for p in json.loads(get("https://www.mubasher.info/api/1/stocks/prices?country=eg"))["prices"]}
    except Exception:
        ar = {}
    session = d["lastUpdate"][:10]
    now = datetime.datetime.now(CAIRO)
    if session == now.date().isoformat() and now.strftime("%H:%M") < "14:45":
        # the desk runs after the 10:00 open, so the session that just finished is read from TradingView's
        # previous-bar closes instead of Mubasher's live list
        try:
            return egx_previous(d, ar, now.date())
        except Exception as e:
            return None, f"EGX: {session} is still trading and the previous session could not be read ({e}); kept the saved session"
    rows, breadth = [], {"up": 0, "down": 0, "flat": 0}
    for p in d["prices"]:
        pct, price, turnover = num(p.get("changePercentage")), num(p.get("value")), num(p.get("turnover"))
        # market breadth: every stock that traded in the session, however little
        if pct is not None and (turnover or 0) > 0:
            breadth["up" if pct > 0 else "down" if pct < 0 else "flat"] += 1
        if pct is None or price is None or (turnover or 0) < MIN_TURNOVER_EGP:
            continue
        rows.append({"t": p["code"], "name": p["name"], "ar": ar.get(p["code"]), "price": price, "pct": pct, "turnover": turnover})
    out = rank(rows)
    out.update(session=session, basis=f"All EGX stocks that traded at least EGP 1m ({out['count']} on the day)", breadth=breadth)
    try:
        out["indices"] = indices()
    except Exception:
        pass
    return out, f"EGX: {session}, {out['count']} stocks"


DESK = {"egx": ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL", "AMOC", "SKPC", "EFID"],
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
    # TradingView's screener: Nasdaq's download serves the session before last even the next day, so its changes
    # would be a day late. New York exchanges, common stock, $10bn or more.
    body = json.dumps({"filter": [{"left": "type", "operation": "equal", "right": "stock"},
                                  {"left": "market_cap_basic", "operation": "greater", "right": MIN_CAP_USD},
                                  {"left": "exchange", "operation": "in_range", "right": ["NYSE", "NASDAQ", "AMEX"]}],
                       "columns": ["name", "description", "close", "change", "market_cap_basic", "Value.Traded"], "range": [0, 3000]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/america/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    rows = []
    for r in json.loads(urllib.request.urlopen(req, timeout=40).read())["data"]:
        sym, name, price, pct, cap, traded = r["d"]
        if pct is None or not price or "/" in sym:
            continue
        name = re.sub(r"\s+Class [A-C]\b.*$", "", name)
        name = re.sub(r",?\s+(Inc\.?|Corp\.?|Corporation|Co\.?|plc|N\.V\.|Ltd\.?|Company)$", "", name).strip(" ,.")
        rows.append({"t": sym, "name": name, "price": price, "pct": round(pct, 3), "cap": cap, "turnover": round(traded or 0)})
    out = rank(rows)
    out.update(session=d.isoformat(), basis=f"US companies worth $10bn or more ({out['count']})")
    return out, f"US: {d}, {out['count']} companies"


# the EGX30's members grouped as readers know them: TradingView files the property developers under "Finance";
# a member not listed here falls back to its TradingView sector, renamed by SECTOR_OF
HEAT_SECTOR = {**{t: "Banks" for t in ("COMI", "ADIB", "CIEB", "QNBE", "HDBK", "SAUD", "FAIT")},
               **{t: "Financial services" for t in ("HRHO", "CCAP", "BTFH", "VLMR", "VLMRA", "CNFN", "EKHO")},
               **{t: "Real estate" for t in ("TMGH", "PHDC", "EMFD", "HELI", "ORHD", "MASR", "OCDI")},
               **{t: "Technology" for t in ("FWRY", "EFIH", "RAYA")}, "ETEL": "Telecom",
               **{t: "Basic materials" for t in ("EGAL", "MCQE", "ABUK", "MFPC", "SKPC", "ESRS", "EGCH", "KIMA")},
               "AMOC": "Energy", **{t: "Industrials" for t in ("ORAS", "ALCN", "SWDY", "ELEC")},
               **{t: "Consumer" for t in ("EAST", "EFID", "JUFO", "GBCO", "ORWE", "AUTO")},
               **{t: "Healthcare" for t in ("ISPH", "RMDA", "CLHO", "PHAR")}}
SECTOR_OF = {"Finance": "Financial services", "Technology Services": "Technology", "Electronic Technology": "Technology",
             "Non-Energy Minerals": "Basic materials", "Process Industries": "Basic materials", "Energy Minerals": "Energy",
             "Consumer Durables": "Consumer", "Consumer Non-Durables": "Consumer", "Consumer Services": "Consumer",
             "Distribution Services": "Consumer", "Retail Trade": "Consumer", "Health Technology": "Healthcare",
             "Health Services": "Healthcare", "Communications": "Telecom", "Industrial Services": "Industrials",
             "Transportation": "Industrials", "Producer Manufacturing": "Industrials", "Utilities": "Utilities"}


def heatmap(upto=None):
    """The EGX30's members (TradingView's index membership, so a reshuffle is followed), each with its sector, market
    value, last close and shares traded, and change over the last finished session, five sessions and 21 sessions,
    from TradingView's daily bars."""
    import tradingview
    body = json.dumps({"filter": [{"left": "type", "operation": "equal", "right": "stock"}],
                       "columns": ["name", "description", "sector", "market_cap_basic", "indexes"], "range": [0, 1000]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/egypt/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    members = [r["d"] for r in json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]
               if any(i.get("proname") == "EGX:EGX30" for i in (r["d"][4] or []))]
    now = datetime.datetime.now(CAIRO)
    trading = now.weekday() not in (4, 5) and now.strftime("%H:%M") < "14:45"

    def closes(code):
        bars = [(t.astimezone(CAIRO).date().isoformat(), v, vol) for t, v, vol in tradingview.bars("EGX:" + code, "1D", 30, volume=True)]
        if trading and bars and bars[-1][0] == now.date().isoformat():
            bars = bars[:-1]   # today's session is still trading
        return [b for b in bars if not upto or b[0] <= upto]   # upto: a backfill for an earlier desk

    rows, sessions = [], []
    with concurrent.futures.ThreadPoolExecutor(4) as pool:
        got = list(zip(members, pool.map(lambda m: _safe(closes, m[0]), members)))
    # every member is measured to the same session, the one most of them end on: a member whose bars already hold
    # the next session's first trades (e-finance's did on Nov 10) is cut back to it
    ends = [b[-1][0] for _, b in got if b]
    common = max(set(ends), key=ends.count) if ends else None
    for (code, desc, sector, cap, _), bars in got:
        bars = [b for b in (bars or []) if b[0] <= common]
        if len(bars) < 22 or not cap or bars[-1][0] != common:
            continue
            c = [b[1] for b in bars]
            sessions.append(bars[-1][0])
            rows.append({"t": code, "name": desc, "sector": HEAT_SECTOR.get(code) or SECTOR_OF.get(sector, sector), "cap": round(cap), "price": c[-1], "vol": bars[-1][2],
                         "d1": round((c[-1] / c[-2] - 1) * 100, 2), "w1": round((c[-1] / c[-6] - 1) * 100, 2), "m1": round((c[-1] / c[-22] - 1) * 100, 2)})
    if len(rows) < 20:
        raise RuntimeError(f"only {len(rows)} members read")
    return {"session": max(set(sessions), key=sessions.count), "rows": rows,
            "basis": "EGX30 members, sized by market value, coloured by change; TradingView"}


def _safe(fn, *a):
    try:
        return fn(*a)
    except Exception:
        return None


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
    # reasons written for earlier sessions' movers, kept a month so the weekly and monthly lists can reuse them
    why_log = {}
    for name in ("egx", "us"):
        X = saved.get(name) or {}
        log = dict(X.get("why_log") or {})
        for side in ("gainers", "losers"):
            for r in X.get(side, []):
                if r.get("why"):
                    log[r["t"]] = {k: r[k] for k in ("why", "source", "url") if k in r} | {"session": X.get("session", "")}
        cutoff = (datetime.date.today() - datetime.timedelta(days=31)).isoformat()
        why_log[name] = {t: v for t, v in log.items() if v.get("session", "") >= cutoff}
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
        if saved.get(name) is not None:
            saved[name]["why_log"] = why_log.get(name, {})
            try:
                saved[name].update(weekly(name))
                print(f"{name.upper()} week and month: {saved[name]['week']['note']}")
            except Exception as e:
                print(f"{name.upper()} week and month: failed ({e}); kept the saved lists")
    if saved.get("egx") is not None:
        try:
            saved["egx"]["heat"] = heatmap()
            h = saved["egx"]["heat"]
            print(f"EGX30 heatmap: {h['session']}, {len(h['rows'])} members")
        except Exception as e:
            print(f"EGX30 heatmap: failed ({e}); kept the saved one")
    print(caps())
    saved["note"] = "Biggest gainers and losers of the last finished session across the whole market. Written by fetch_movers.py."
    with open(OUT, "w") as f:
        json.dump(saved, f, separators=(",", ":"), ensure_ascii=False)
        f.write("\n")
    if "--leads" in sys.argv:
        leads(saved)


if __name__ == "__main__":
    sys.exit(main())
