#!/usr/bin/env python3
"""Refresh desk/calendar.json: the desk's stocks' coming results dates and dividends, from TradingView's screener.

Usage:
  python3 .claude/skills/markets-desk/fetch_calendar.py

For each desk stock: the next results date (TradingView's, which for Egyptian companies is often its own estimate
until the company announces one, so the page calls every results date "expected"), the quarter it covers, and an upcoming dividend
(ex-date, payment date and amount per share). Only dates in the next 75 days are kept. One request per market; an
unofficial endpoint, so a failure keeps the file as it was. Dates the desk confirms itself go in each stock's "next"
in desk/stocks.json, which the pages show beside these.
"""
import datetime
import json
import os
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "calendar.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL", "AMOC", "SKPC", "EFID"]
US = {"AAPL": "NASDAQ", "MSFT": "NASDAQ", "NVDA": "NASDAQ", "AMZN": "NASDAQ", "GOOGL": "NASDAQ", "META": "NASDAQ", "TSLA": "NASDAQ", "JPM": "NYSE", "XOM": "NYSE",
      "AVGO": "NASDAQ", "BRK.B": "NYSE", "WMT": "NYSE", "V": "NYSE", "ORCL": "NYSE", "COST": "NASDAQ"}
COLS = ["earnings_release_next_date", "earnings_release_next_calendar_date", "earnings_release_next_time",
        "ex_dividend_date_upcoming", "dividend_payment_date_upcoming", "dividend_amount_upcoming"]
TODAY = datetime.date.today()


def scan(region, tickers):
    body = json.dumps({"symbols": {"tickers": tickers}, "columns": COLS}).encode()
    req = urllib.request.Request(f"https://scanner.tradingview.com/{region}/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=40).read())["data"]


def d(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date() if ts else None


def main():
    items = []
    for market, region, tickers, cur in (("egx", "egypt", [f"EGX:{t}" for t in EGX], "EGP"), ("us", "america", [f"{x}:{t}" for t, x in US.items()], "$")):
        try:
            rows = scan(region, tickers)
        except Exception as e:
            print(f"{market}: TradingView failed ({e}); calendar kept as it was")
            return
        for r in rows:
            t = r["s"].split(":", 1)[1]
            nxt, per, when, exd, pay, amt = r["d"]
            rd = d(nxt)
            if rd and TODAY <= rd <= TODAY + datetime.timedelta(days=75):
                q = d(per)
                items.append({"t": t, "market": market, "kind": "results", "date": rd.isoformat(),
                              "period": q.isoformat() if q else None,
                              "time": {1: "after the close", -1: "before the open"}.get(when),
                              "expected": True})
            ed = d(exd)
            if ed and TODAY <= ed <= TODAY + datetime.timedelta(days=75) and amt:
                items.append({"t": t, "market": market, "kind": "dividend", "date": ed.isoformat(),
                              "pay": d(pay).isoformat() if pay else None, "amount": round(amt, 4), "cur": cur})
    items.sort(key=lambda x: (x["date"], x["t"]))
    with open(OUT, "w") as f:
        json.dump({"note": "The desk's stocks' coming results and dividends, from TradingView (fetch_calendar.py). Results dates for "
                           "Egyptian companies are often TradingView's estimate until the company announces one.",
                   "fetched": TODAY.isoformat(), "items": items}, f, indent=1)
        f.write("\n")
    for x in items:
        print(x["date"], x["t"], x["kind"], x.get("amount", ""), x.get("period", "") or "")


if __name__ == "__main__":
    main()
