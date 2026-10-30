#!/usr/bin/env python3
"""Save the last finished session's prices through the day, every 5 minutes, for the desk's 1D charts.

Usage:
  python3 .claude/skills/markets-desk/fetch_intraday.py

Writes desk/intraday.json: the EGX30 and the 12 Egyptian stocks from Mubasher (Cairo time), and the
Nasdaq Composite and the 12 US stocks from Nasdaq (New York time, regular session only). The S&P 500 and
the Dow have no free intraday source. A market whose fetch fails, or whose feed still shows an unfinished
session, keeps the session already saved. Prints one line per market; it takes about a minute.
"""
import datetime
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from zoneinfo import ZoneInfo

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "intraday.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN"]
US = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT"]
NY, CAIRO = ZoneInfo("America/New_York"), ZoneInfo("Africa/Cairo")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


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


def nasdaq(key):
    cls = "index" if key == "COMP" else "stocks"
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


def market(name, keys, fn, done):
    with ThreadPoolExecutor(6) as pool:
        res = dict(zip(keys, pool.map(lambda k: _try(fn, k), keys)))
    ok = {k: v for k, v in res.items() if v}
    if not ok:
        return None, f"{name}: nothing fetched"
    day = max(v[0] for v in ok.values())
    series = {k: v[1] for k, v in ok.items() if v[0] == day and len(v[1]) >= 6}
    if not done(day, series):
        return None, f"{name}: the feed shows {day}, a session still in progress; kept the saved one"
    missing = sorted(set(keys) - set(series))
    return {"session": day, "series": series}, f"{name}: {day}, {len(series)} series" + (f" (missing {', '.join(missing)})" if missing else "")


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
    for name, keys, fn, done in (("egx", ["EGX30"] + EGX, mubasher, egx_done), ("us", ["COMP"] + US, nasdaq, us_done)):
        data, line = market(name.upper(), keys, fn, done)
        if data and data["session"] >= (saved.get(name) or {}).get("session", ""):
            out[name] = data
        print(line)
    out["note"] = "Last finished session, every 5 minutes: EGX in Cairo time (Mubasher), US in New York time (Nasdaq). Written by fetch_intraday.py."
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"))
        f.write("\n")


if __name__ == "__main__":
    sys.exit(main())
