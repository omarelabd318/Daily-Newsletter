#!/usr/bin/env python3
"""Save the last finished session's prices through the day, every 5 minutes, for the desk's 1D charts.

Usage:
  python3 .claude/skills/markets-desk/fetch_intraday.py

Writes desk/intraday.json ("week" also keeps the last five sessions of each market every 15 minutes, for
the 1W charts, and "month" the last 23 every 30 minutes, for the 1M charts): the EGX30 and the 12 Egyptian stocks from Mubasher (Cairo time), the
EGX70 EWI from TradingView's chart feed (tradingview.py; no other free source publishes it through the session), and the
Nasdaq Composite and the 12 US stocks from Nasdaq (New York time, regular session only), and the last
24 hours of Bitcoin (CoinGecko). Yahoo adds the S&P 500, the Dow, Brent, gold and the dollar index on the
days it answers (it often refuses cloud requests). When it refuses, the S&P 500 and the Dow are drawn from
the funds that track them on Nasdaq (SPY, DIA), scaled so the line ends at the index's logged close; the
file names the fund under "proxy". Brent, gold and the dollar index are simply left out on other days. A market whose fetch fails, or whose feed still shows an unfinished
session, keeps the session already saved. A series the feed refuses is asked for again one at a time, then taken from
Polygon (polygon.py), then Yahoo; a stock missing from a saved US session is filled from Yahoo's last five sessions. Prints one line per market;
it takes about a minute.
"""
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from zoneinfo import ZoneInfo

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "daily-newsletter"))   # polygon.py
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "intraday.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL", "AMOC", "SKPC", "EFID"]
US = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST", "NFLX", "INTC", "LLY"]
NY, CAIRO = ZoneInfo("America/New_York"), ZoneInfo("Africa/Cairo")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def every15(points):
    """A session's 5-minute prices thinned to every 15 minutes, keeping the last: enough for a week's chart."""
    keep = [p for p in points if int(p[0][3:5]) % 15 == 0]
    return keep + ([points[-1]] if points and (not keep or keep[-1] != points[-1]) else [])


def every_n(points, step):
    """A session's prices thinned to every `step` minutes, keeping the last."""
    keep = [p for p in points if int(p[0][3:5]) % step == 0]
    return keep + ([points[-1]] if points and (not keep or keep[-1] != points[-1]) else [])


YMONTH = {"COMP": "^IXIC", "sp500": "^GSPC", "dow": "^DJI"}
# Polygon's free plan has stocks and funds but not the indexes: each index is drawn from the fund that tracks it,
# scaled each session so the line ends at the index's logged close
PFUND = {"COMP": ("ONEQ", "nasdaq"), "sp500": ("SPY", "sp500"), "dow": ("DIA", "dow")}


def polygon_bars(key, step, frm, to):
    """A US series from Polygon (shared helper polygon.py; five requests a minute), every `step` minutes, New York
    time, regular session only: {day: [[hm, v], ...]}. A bar's close is the price at the bar's end; the first point
    of each session is the open at 09:30. An index comes from its fund, scaled each day to the logged close."""
    import polygon
    sym, logkey = PFUND.get(key, (key, None))
    days = {}
    for b in polygon.bars(sym, step, "minute", frm, to):
        t = datetime.datetime.fromtimestamp(b["t"] / 1000, datetime.timezone.utc).astimezone(NY)
        if not ("09:30" <= t.strftime("%H:%M") < "16:00"):
            continue
        d = days.setdefault(t.date().isoformat(), [])
        if t.strftime("%H:%M") == "09:30":
            d.append(["09:30", float(b["o"])])
        d.append([(t + datetime.timedelta(minutes=step)).strftime("%H:%M"), float(b["c"])])
    if logkey:
        out = {}
        for d, pts in days.items():
            close = logged_close(logkey, d)
            if close and pts:
                k = close / pts[-1][1]
                out[d] = [[hm, round(v * k, 2)] for hm, v in pts]
        days = out
    return days


def polygon_month(key):
    """The last month every 30 minutes (the US month's backfill)."""
    end = datetime.date.today()
    return polygon_bars(key, 30, (end - datetime.timedelta(days=40)).isoformat(), end.isoformat())


def polygon_day(key, day):
    """One session every 5 minutes (the backup when Nasdaq refuses a series)."""
    return polygon_bars(key, 5, day, day).get(day)


def every5(points):
    """Keep the last price in each 5-minute slot: [("10:05", 120.4), ...]."""
    out = {}
    for hm, v in points:
        h, m = map(int, hm.split(":"))
        out[f"{h:02d}:{m - m % 5:02d}"] = v
    return [[k, out[k]] for k in sorted(out)]


def mubasher(key):
    """The page links a CSV of minute bars: date/time, open, high, low, close, volume."""
    page = get(f"https://english.mubasher.info/markets/EGX/{'indices/EGX30' if key == 'EGX30' else 'stocks/' + key}")
    url = re.search(r'intraday-data-url="([^"]+)"', page).group(1)
    rows = [l.split(",") for l in get(urllib.parse.urljoin("https://english.mubasher.info", url)).splitlines() if "/" in l]
    # Mubasher writes "market time" as UTC+2 all year; Cairo moves to UTC+3 in summer, so convert
    utc2 = datetime.timezone(datetime.timedelta(hours=2))
    pts = [(datetime.datetime.strptime(r[0], "%Y-%m-%d/%H:%M:%S").replace(tzinfo=utc2).astimezone(CAIRO), float(r[4])) for r in rows]
    day = max(t.date() for t, _ in pts)
    return day.isoformat(), every5([(t.strftime("%H:%M"), v) for t, v in pts if t.date() == day])


def nasdaq(key, cls=None):
    if key in ("sp500", "dow"):
        return us_index(key)
    cls = cls or ("index" if key == "COMP" else "stocks")
    d = json.loads(get(f"https://api.nasdaq.com/api/quote/{urllib.parse.quote(key)}/chart?assetclass={cls}"))["data"]
    pts = []
    for p in d["chart"]:
        t = datetime.datetime.fromtimestamp(p["x"] / 1000, datetime.timezone.utc)
        # Nasdaq's x is New York wall-clock time written as UTC
        hm = t.strftime("%H:%M")
        if "09:30" <= hm <= "16:00":
            pts.append((t.date().isoformat(), hm, float(p["y"])))
    day = max(p[0] for p in pts)
    return day, every5([(hm, v) for d_, hm, v in pts if d_ == day])


YAHOO = {"sp500": "^GSPC", "dow": "^DJI", "brent": "BZ=F", "gold_usd": "GC=F", "dxy": "DX-Y.NYB"}


def yahoo_points(key):
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(YAHOO[key])}?range=5d&interval=5m"
    r = json.loads(get(url))["chart"]["result"][0]
    return [(datetime.datetime.fromtimestamp(t, datetime.timezone.utc), float(c))
            for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c]


FUNDS = {"sp500": "SPY", "dow": "DIA"}
PROXY = {}


def logged_close(key, day):
    """The index's close for a session, from the data log (an entry holds the close of the session before its date)."""
    for e in json.load(open(os.path.join(ROOT, "data", "markets-recent.json")))["days"]:
        if e["date"] > day and isinstance(e.get(key), (int, float)):
            return e[key]
    return None


def us_index(key):
    """The S&P 500 or the Dow: the last regular session, New York time, from Yahoo or else from its fund."""
    try:
        return yahoo_index(key)
    except Exception:
        day, pts = nasdaq(FUNDS[key], "etf")
        close = logged_close(key, day)
        if not close:
            raise ValueError(f"no logged {key} close for {day}")
        k = close / pts[-1][1]
        PROXY[key] = FUNDS[key]
        return day, [[hm, round(v * k, 2)] for hm, v in pts]


def yahoo_index(key):
    pts = [(t.astimezone(NY), v) for t, v in yahoo_points(key)]
    pts = [(t, v) for t, v in pts if "09:30" <= t.strftime("%H:%M") <= "16:00"]
    day = max(t.date() for t, _ in pts)
    return day.isoformat(), every5([(t.strftime("%H:%M"), v) for t, v in pts if t.date() == day])


def last24(pts):
    """The last 24 hours, every 5 minutes, labelled in Cairo time (these markets trade round the clock)."""
    end = max(t for t, _ in pts)
    keep = {}
    for t, v in sorted(pts):
        if t > end - datetime.timedelta(hours=24):
            c = t.astimezone(CAIRO)
            keep[c.replace(minute=c.minute - c.minute % 5, second=0, microsecond=0)] = v
    return end.astimezone(CAIRO), [[k.strftime("%H:%M"), keep[k]] for k in sorted(keep)]


def coingecko_btc():
    d = json.loads(get("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1"))
    return last24([(datetime.datetime.fromtimestamp(t / 1000, datetime.timezone.utc), float(v)) for t, v in d["prices"]])


# round-the-clock markets on TradingView's chart feed: Brent's front-month future (the contract the log follows), spot
# gold, the dollar index and Bitcoin
TV_GLOBAL = {"brent": "ICEEUR:BRN1!", "gold_usd": "TVC:GOLD", "dxy": "TVC:DXY", "btc": "BITSTAMP:BTCUSD"}


def tv_last24(key):
    import tradingview
    return last24(tradingview.bars(TV_GLOBAL[key], "5", 330))


def global_history(out):
    """Hourly lines for the Global page's 1W and 1M charts: the last seven days every hour and the last 30 every two
    hours, by Cairo date, saved beside the markets' own weeks and months as `g_KEY` (a day a market was shut is
    simply absent). From TradingView's chart feed; a key that fails keeps what was saved."""
    import tradingview
    done = []
    for key, sym in TV_GLOBAL.items():
        try:
            days = {}
            for t, v in tradingview.bars(sym, "60", 760):
                c = t.astimezone(CAIRO)
                days.setdefault(c.strftime("%Y-%m-%d"), []).append((c.strftime("%H:%M"), round(v, 4), c.hour))
            dates = sorted(d for d in days if len(days[d]) > 1)
            if len(dates) < 5:
                continue
            out.setdefault("week", {})["g_" + key] = [{"session": d, "series": {key: [[t, v] for t, v, _ in days[d]]}} for d in dates[-7:]]
            out.setdefault("month", {})["g_" + key] = [{"session": d, "series": {key: [[t, v] for t, v, h in days[d] if h % 2 == 0] or [[t, v] for t, v, _ in days[d]][:2]}} for d in dates[-30:]]
            done.append(key)
        except Exception:
            pass
    return "GLOBAL week and month: hourly from TradingView, " + (", ".join(done) or "nothing fetched (kept what was saved)")


def global_market():
    series, ends = {}, []
    for key, fallback in (("btc", coingecko_btc), *[(k, lambda k=k: last24(yahoo_points(k))) for k in ("brent", "gold_usd", "dxy")]):
        for fn in (lambda key=key: tv_last24(key), fallback):
            try:
                end, pts = fn()
                if len(pts) >= 12:
                    series[key], ends = pts, ends + [end]
                    break
            except Exception:
                pass
    if not series:
        return None, "GLOBAL: nothing fetched"
    to = max(ends)
    return {"window": "24h", "to": to.strftime("%Y-%m-%d %H:%M"), "series": series}, f"GLOBAL: last 24 hours to {to:%a %H:%M} Cairo, {', '.join(series)}"


def yahoo_month(key):
    """A US series' last month from Yahoo, every 30 minutes, New York time: {day: [[hm, v], ...]}; the fallback when
    Polygon refuses the month's backfill."""
    sym = YMONTH.get(key, key.replace(".", "-"))
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=1mo&interval=30m"
    r = json.loads(get(url))["chart"]["result"][0]
    days = {}
    for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
        if c is None:
            continue
        n = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).astimezone(NY)
        if "09:30" <= n.strftime("%H:%M") <= "16:00":
            days.setdefault(n.date().isoformat(), []).append([n.strftime("%H:%M"), round(float(c), 4)])
    return days


def yahoo_sessions(key):
    """A US stock's last five regular sessions from Yahoo, every 5 minutes, New York time: {day: [[hm, v], ...]}.
    The fallback when Nasdaq refuses a stock, and the source that fills a stock missing from a saved session."""
    url = f"https://query2.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(key.replace('.', '-'))}?range=5d&interval=5m"
    r = json.loads(get(url))["chart"]["result"][0]
    days = {}
    for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]):
        if c is None:
            continue
        n = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).astimezone(NY)
        if "09:30" <= n.strftime("%H:%M") <= "16:00":
            days.setdefault(n.date().isoformat(), []).append((n.strftime("%H:%M"), float(c)))
    return {d: every5(v) for d, v in days.items()}


def market(name, keys, fn, done):
    with ThreadPoolExecutor(6) as pool:
        res = dict(zip(keys, pool.map(lambda k: _try(fn, k), keys)))
    # a feed that refuses some requests under load: ask again one at a time for what is missing
    for k in [k for k in keys if not res.get(k)]:
        res[k] = _try(fn, k)
    ok = {k: v for k, v in res.items() if v}
    # US series Nasdaq still refused: Polygon's copy of the same session, then Yahoo's
    if name == "US" and ok:
        day0 = max(v[0] for v in ok.values())
        for k in [k for k in keys if (k in US or k in PFUND) and not res.get(k)]:
            pts = _try(lambda k: polygon_day(k, day0), k)
            if pts and len(pts) >= 6:
                ok[k] = (day0, pts)
                continue
            y = _try(yahoo_sessions, k)
            if y and day0 in y:
                ok[k] = (day0, y[day0])
    if not ok:
        return None, f"{name}: nothing fetched"
    day = max(v[0] for v in ok.values())
    series = {k: v[1] for k, v in ok.items() if v[0] == day and len(v[1]) >= 6}
    if not done(day, series):
        return None, f"{name}: the feed shows {day}, a session still in progress; kept the saved one"
    missing = sorted(set(keys) - set(series))
    return {"session": day, "series": series}, f"{name}: {day}, {len(series)} series" + (f" (missing {', '.join(missing)})" if missing else "")


def tv_sessions(symbol, count=2500):
    """{session (Cairo date): [[HH:MM, close], ...]} from TradingView's 5-minute bars, inside the EGX's hours."""
    import tradingview
    by_day = {}
    for t, v in tradingview.bars(symbol, "5", count):
        c = t.astimezone(CAIRO)
        if "10:00" <= c.strftime("%H:%M") <= "14:30":
            by_day.setdefault(c.date().isoformat(), []).append([c.strftime("%H:%M"), v])
    return by_day


def egx_month(out, now_cairo):
    """The EGX month (every 30 minutes, for the 1M charts) is built one session a run from Mubasher, which cannot
    serve past sessions: while it is short, the finished sessions it lacks come from TradingView's bars."""
    month = out.setdefault("month", {})
    have = {x["session"]: x for x in month.get("egx", [])}
    if len(have) >= 21:
        return f"EGX month: {len(have)} sessions"
    today = now_cairo.date().isoformat()
    finished = lambda d: d < today or now_cairo.strftime("%H:%M") >= "14:45"
    got = {}
    with ThreadPoolExecutor(4) as pool:
        for k, res in zip(["EGX30"] + EGX, pool.map(lambda k: _try(tv_sessions, "EGX:" + k), ["EGX30"] + EGX)):
            if res:
                got[k] = res
    days = sorted(d for d in (got.get("EGX30") or {}) if finished(d) and d not in have)[-23:]
    for d in days:
        series = {k: every_n(v[d], 30) for k, v in got.items() if len(v.get(d, [])) >= 6}
        if "EGX30" in series:
            have[d] = {"session": d, "series": series}
    month["egx"] = [have[d] for d in sorted(have)][-23:]
    return f"EGX month: {len(month['egx'])} sessions ({len(days)} added from TradingView, {len(got)} of {1 + len(EGX)} series answered)"


def egx70(out):
    """Adds "EGX70EWI" to each saved EGX session that lacks it: every 5 minutes for the day, 15 for the week, 30 for
    the month, in Cairo time like Mubasher's series."""
    by_day = tv_sessions("EGX:EGX70EWI")
    added = 0
    targets = [(out.get("egx"), every5)] + [(x, every15) for x in out.get("week", {}).get("egx", [])] + [(x, lambda p: every_n(p, 30)) for x in out.get("month", {}).get("egx", [])]
    for x, thin in targets:
        pts = by_day.get((x or {}).get("session"))
        if x and pts and len(pts) >= 6 and "EGX70EWI" not in x["series"]:
            x["series"]["EGX70EWI"] = thin(pts)
            added += 1
    return f"EGX70 EWI: TradingView, {len(by_day)} sessions fetched, added to {added} saved session{'s' if added != 1 else ''}"


def _try(fn, k):
    try:
        return fn(k)
    except Exception:
        return None


def main():
    saved = json.load(open(OUT)) if os.path.exists(OUT) else {}
    now_cairo, now_ny = datetime.datetime.now(CAIRO), datetime.datetime.now(NY)
    # a session is finished once its day is over, or once its last bar is at the close
    egx_done = lambda day, s: day < now_cairo.date().isoformat() or now_cairo.strftime("%H:%M") >= "14:45"
    us_done = lambda day, s: day < now_ny.date().isoformat() or now_ny.strftime("%H:%M") >= "16:15"
    out = dict(saved)
    for name, keys, fn, done in (("egx", ["EGX30"] + EGX, mubasher, egx_done), ("us", ["COMP", "sp500", "dow"] + US, nasdaq, us_done)):
        data, line = market(name.upper(), keys, fn, done)
        if data and data["session"] >= (saved.get(name) or {}).get("session", ""):
            if name == "us" and PROXY:
                data["proxy"] = {k: f for k, f in PROXY.items() if k in data["series"]}
            out[name] = data
        print(line)
    # the week: the last five sessions of each market, every 15 minutes, for the 1W charts (built up one
    # session per run; a session saved again replaces its earlier copy)
    week = saved.get("week") or {}
    for name in ("egx", "us"):
        latest = out.get(name)
        if not latest:
            continue
        keep = [x for x in week.get(name, []) if x["session"] != latest["session"]]
        keep.append({"session": latest["session"], "series": {k: every15(v) for k, v in latest["series"].items()}})
        week[name] = sorted(keep, key=lambda x: x["session"])[-5:]
    # a stock missing from a saved US session (a fetch that failed that day) is filled from Yahoo's last five sessions
    holes = sorted({k for x in week.get("us", []) for k in US if k not in x["series"]})
    for k in holes:
        ss = [x["session"] for x in week.get("us", [])]
        y = (_try(lambda k: polygon_bars(k, 15, ss[0], ss[-1]), k) if ss else None) or _try(yahoo_sessions, k)
        for x in week.get("us", []):
            if k not in x["series"] and y and len(y.get(x["session"], [])) >= 6:
                x["series"][k] = every15(y[x["session"]])
    filled = [k for k in holes if all(k in x["series"] for x in week.get("us", []))]
    if holes:
        print(f"US week: filled {', '.join(filled) or 'nothing'} from Polygon or Yahoo" + (f"; still missing {', '.join(sorted(set(holes) - set(filled)))}" if set(holes) - set(filled) else ""))
    out["week"] = week
    # the month: the last 23 sessions of each market, every 30 minutes, for the 1M charts. Each run adds the week's
    # sessions (a session still in the week replaces its month copy); the EGX's past sessions cannot be fetched again,
    # so its month fills one session a run; the US month is filled from Yahoo while it is short
    month = saved.get("month") or {}
    for name in ("egx", "us"):
        have = {x["session"]: x for x in month.get(name, [])}
        for x in week.get(name, []):
            have[x["session"]] = {"session": x["session"], "series": {k: every_n(v, 30) for k, v in x["series"].items()}}
        month[name] = [have[k] for k in sorted(have)][-23:]
    holes_us = any(k not in x["series"] for x in month.get("us", []) for k in ["COMP", "sp500"] + US)
    if len(month.get("us", [])) < 21 or holes_us:
        got = 0
        for i, k in enumerate(["COMP", "sp500", "dow"] + US):
            # Polygon first (polygon.py paces it at five requests a minute), Yahoo if it fails
            y = _try(polygon_month, k) or _try(yahoo_month, k)
            if not y:
                continue
            got += 1
            have = {x["session"]: x for x in month.get("us", [])}
            for d, pts in y.items():
                if len(pts) >= 6 and d <= (out.get("us") or {}).get("session", d):
                    have.setdefault(d, {"session": d, "series": {}})["series"].setdefault(k, pts)
            month["us"] = [have[d] for d in sorted(have)][-23:]
        print(f"US month: {len(month.get('us', []))} sessions" + (" (Polygon and Yahoo refused the backfill)" if not got else f", {got} series filled"))
    out["month"] = month
    # the EGX70 EWI through each saved EGX session (day, week and month): only TradingView publishes it through the
    # session, so its bars are added beside Mubasher's, a whole month at a time
    try:
        print(egx_month(out, now_cairo))
    except Exception as e:
        print(f"EGX month: TradingView failed ({e}); kept what was saved")
    try:
        print(egx70(out))
    except Exception as e:
        print(f"EGX70 EWI: TradingView failed ({e}); its lines keep what was saved")
    data, line = global_market()
    if data:
        out["global"] = data
    print(line)
    print(global_history(out))
    out["note"] = "Last finished session, every 5 minutes: EGX in Cairo time (Mubasher), US in New York time (Nasdaq; S&P 500 and Dow from Yahoo when it answers, otherwise from the funds named under proxy, scaled to the index's close); global: the last 24 hours in Cairo time (Bitcoin from CoinGecko; Brent, gold and the dollar index from Yahoo when it answers). Written by fetch_intraday.py."
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"))
        f.write("\n")


if __name__ == "__main__":
    sys.exit(main())
