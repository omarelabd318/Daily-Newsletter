#!/usr/bin/env python3
"""Refresh desk/rates.json: the Wall Street page's fixed "Rates and data" rows, a year of daily closes each.

Usage:
  python3 .claude/skills/markets-desk/fetch_rates.py

  vix          the Cboe Volatility Index (Cboe's own daily history; Yahoo if Cboe fails)
  us3m, us2y,  US Treasury yields: 3-month bill, 2-, 10- and 30-year notes and bonds (the Treasury's daily par yield
  us10y, us30y curve, the official figures)
The dollar index comes from the data log (data/markets.json, dxy). The page shows each row's last close on or before
the desk's US date with its change on the day, then the day's extra items the desk writes in pages.us.rates (data
releases, Fed odds). A source that fails keeps its series as it was, so the page never loses its rows.
"""
import csv
import datetime
import io
import json
import os
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "rates.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
TODAY = datetime.date.today()
SINCE = (TODAY - datetime.timedelta(days=400)).isoformat()
TREASURY = {"us3m": "3 Mo", "us2y": "2 Yr", "us10y": "10 Yr", "us30y": "30 Yr"}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40).read().decode("utf-8", "replace")


def mdy(s):
    m, d, y = s.split("/")
    return f"{y}-{int(m):02d}-{int(d):02d}"


def vix():
    try:
        rows = csv.DictReader(io.StringIO(get("https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv")))
        out = [[mdy(r["DATE"]), round(float(r["CLOSE"]), 2)] for r in rows if r.get("CLOSE")]
        return [x for x in out if x[0] >= SINCE]
    except Exception as e:
        print(f"Cboe: {e}; trying Yahoo")
    j = json.loads(get("https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?range=2y&interval=1d"))["chart"]["result"][0]
    tz = datetime.timezone(datetime.timedelta(seconds=j["meta"].get("gmtoffset", 0)))
    out = [[datetime.datetime.fromtimestamp(t, tz).date().isoformat(), round(c, 2)]
           for t, c in zip(j["timestamp"], j["indicators"]["quote"][0]["close"]) if c is not None]
    return [x for x in out if x[0] >= SINCE]


def treasury():
    got = {k: {} for k in TREASURY}
    for year in sorted({TODAY.year - 1, TODAY.year}):
        url = (f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all"
               f"?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv")
        for r in csv.DictReader(io.StringIO(get(url))):
            d = mdy(r["Date"])
            for k, col in TREASURY.items():
                if r.get(col):
                    got[k][d] = float(r[col])
    return {k: [[d, v] for d, v in sorted(s.items()) if d >= SINCE] for k, s in got.items()}


def main():
    try:
        D = json.load(open(OUT))
    except Exception:
        D = {"series": {}}
    S = D.setdefault("series", {})
    done = []
    try:
        S["vix"] = vix()
        done.append(f"VIX to {S['vix'][-1][0]} ({S['vix'][-1][1]})")
    except Exception as e:
        print(f"VIX not updated: {e}")
    try:
        for k, v in treasury().items():
            if v:
                S[k] = v
        done.append(f"Treasury yields to {S['us10y'][-1][0]} (10-year {S['us10y'][-1][1]}%)")
    except Exception as e:
        print(f"Treasury yields not updated: {e}")
    D["fetched"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    D["note"] = "Daily closes. vix: Cboe Volatility Index; us3m/us2y/us10y/us30y: US Treasury par yields, percent."
    with open(OUT, "w") as f:
        json.dump(D, f, separators=(",", ":"))
    print("Rates: " + ("; ".join(done) if done else "nothing new") + ".")


if __name__ == "__main__":
    main()
