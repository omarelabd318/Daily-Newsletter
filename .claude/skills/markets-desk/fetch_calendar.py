#!/usr/bin/env python3
"""Refresh desk/calendar.json: the desk's stocks' coming results dates and dividends, from TradingView's screener, and
for the US stocks the dividends their boards have declared and any stock splits, from Polygon.

Usage:
  python3 .claude/skills/markets-desk/fetch_calendar.py

For each desk stock: the next results date (TradingView's, which for Egyptian companies is often its own estimate
until the company announces one, so the page calls every results date "expected"), the quarter it covers, and an upcoming dividend
(ex-date, payment date and amount per share). Only dates in the next 75 days are kept. One request per market; an
unofficial endpoint, so a failure keeps the file as it was. Dates the desk confirms itself go in each stock's "next"
in desk/stocks.json, which the pages show beside these.

Polygon (polygon.py; its key is a network secret added by the proxy) gives the US stocks' declared dividends, with the
date the board declared them, and stock splits. Its free plan takes one stock per request at five a minute, so it is
asked once a week (about three minutes) and the copy kept in calendar.json under "polygon" is reused between; pass
--polygon to ask now. A declared dividend replaces TradingView's for the same date. A split executed in the last two
weeks is listed under "recentSplits", and check_desk.py warns if the data log's earlier prices were not adjusted.
"""
import datetime
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "daily-newsletter"))   # polygon.py

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


def polygon_events(old):
    """The US stocks' declared dividends and splits from Polygon, reused for six days."""
    cache = (old or {}).get("polygon") or {}
    if "--polygon" not in sys.argv and cache.get("fetched", "") >= (TODAY - datetime.timedelta(days=6)).isoformat():
        return cache
    import polygon
    divs, splits, failed = [], [], []
    for t in US:
        try:
            for r in polygon.call(f"/v3/reference/dividends?ticker={t}&ex_dividend_date.gte={TODAY.isoformat()}&limit=10"):
                divs.append({"t": t, "date": r["ex_dividend_date"], "pay": r.get("pay_date"), "amount": r["cash_amount"],
                             "declared": r.get("declaration_date"), "cur": "$" if r.get("currency", "USD") == "USD" else r.get("currency")})
        except Exception as e:
            failed.append(t)
    try:
        frm, to = (TODAY - datetime.timedelta(days=14)).isoformat(), (TODAY + datetime.timedelta(days=75)).isoformat()
        for r in polygon.call(f"/v3/reference/splits?execution_date.gte={frm}&execution_date.lte={to}&limit=1000", pages=5):
            if r["ticker"] in US:
                splits.append({"t": r["ticker"], "date": r["execution_date"], "to": r["split_to"], "from": r["split_from"]})
    except Exception as e:
        failed.append("splits")
    if len(failed) > len(US) // 2:
        print(f"Polygon: failed ({', '.join(failed[:5])}...); kept the saved copy")
        return cache
    print(f"Polygon: {len(divs)} declared dividends, {len(splits)} splits" + (f" (failed: {', '.join(failed)})" if failed else ""))
    return {"fetched": TODAY.isoformat(), "dividends": divs, "splits": splits}


def main():
    try:
        old = json.load(open(OUT))
    except Exception:
        old = {}
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
    # the US: a dividend the board declared (Polygon) replaces TradingView's for the same ex-date; splits are added
    P = polygon_events(old)
    end = (TODAY + datetime.timedelta(days=75)).isoformat()
    declared = {(x["t"], x["date"]) for x in P.get("dividends", [])}
    items = [x for x in items if not (x["market"] == "us" and x["kind"] == "dividend" and (x["t"], x["date"]) in declared)]
    for x in P.get("dividends", []):
        if TODAY.isoformat() <= x["date"] <= end:
            items.append({"t": x["t"], "market": "us", "kind": "dividend", "date": x["date"], "pay": x.get("pay"),
                          "amount": round(x["amount"], 4), "cur": x.get("cur", "$"), "declared": x.get("declared"), "src": "Polygon"})
    recent = []
    for x in P.get("splits", []):
        ratio = f"{x['to']:g}-for-{x['from']:g}"
        if TODAY.isoformat() <= x["date"] <= end:
            items.append({"t": x["t"], "market": "us", "kind": "split", "date": x["date"], "ratio": ratio, "factor": x["to"] / x["from"], "src": "Polygon"})
        elif x["date"] < TODAY.isoformat():
            recent.append({"t": x["t"], "date": x["date"], "ratio": ratio, "factor": x["to"] / x["from"]})
    items.sort(key=lambda x: (x["date"], x["t"]))
    with open(OUT, "w") as f:
        json.dump({"note": "The desk's stocks' coming results and dividends, from TradingView (fetch_calendar.py); for the US stocks, "
                           "declared dividends and stock splits from Polygon. Results dates for Egyptian companies are often "
                           "TradingView's estimate until the company announces one.",
                   "fetched": TODAY.isoformat(), "items": items, "recentSplits": recent, "polygon": P}, f, indent=1)
        f.write("\n")
    for x in items:
        print(x["date"], x["t"], x["kind"], x.get("amount", x.get("ratio", "")), x.get("period", "") or "", "declared " + x["declared"] if x.get("declared") else "")


if __name__ == "__main__":
    main()
