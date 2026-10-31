#!/usr/bin/env python3
"""Refresh each desk stock's valuation card in desk/stocks.json ("valuation").

Usage:
  python3 .claude/skills/markets-desk/fetch_valuation.py [TICKER ...]

With no tickers it covers all the desk's stocks. Egyptian stocks: earnings and book value per share from
each stock's Mubasher page, with the results period they are based on, and its market value. US stocks:
the last four reported quarters' earnings per share, the analysts' forecast P/E for this year, the dividend
yield, the analysts' one-year target and the market value, from Nasdaq.

P/E and P/B are worked out here at the latest logged close, not taken from the source, because a source's
ratio can be months old and priced at that day's close. Each card records the results period behind it
("period", the quarter's last day); the stock page flags figures based on results more than about half a
year old. Earnings older than two years (or missing) are left out rather than shown. Prints one line per
stock; a stock whose fetch fails keeps the card it had.
"""
import concurrent.futures
import datetime
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
STOCKS = os.path.join(ROOT, "desk", "stocks.json")
LOG = os.path.join(ROOT, "data", "markets-recent.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC"]
US = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST"]
# listed but not yet trading: nothing to value until the first session
NOT_TRADING = {"BQDC"} if datetime.date.today() < datetime.date(2026, 11, 2) else set()
QUARTER_END = {"First": "03-31", "Second": "06-30", "Third": "09-30", "Fourth": "12-31"}
MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
TODAY = datetime.date.today()


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40).read().decode("utf-8", "replace")


def num(s):
    s = re.sub(r"[^\d.\-]", "", str(s or ""))
    return float(s) if s not in ("", "-", ".") else None


def last_close(group, t):
    for e in reversed(json.load(open(LOG))["days"]):
        v = (e.get(group) or {}).get(t)
        if isinstance(v, (int, float)):
            return v
    return None


def big(v, cur):
    """Market value in billions, or trillions from 1,000bn: 'EGP 369.9bn', '$5.03tn'."""
    sym = "$" if cur == "USD" else "EGP "
    return f"{sym}{v / 1e12:.2f}tn" if v >= 1e12 else f"{sym}{v / 1e9:.1f}bn"


def ratio(price, per_share):
    if not price or per_share is None:
        return None
    return "n/m (loss)" if per_share <= 0 else f"{price / per_share:.1f}"


def fresh(period):
    return period and (TODAY - datetime.date.fromisoformat(period)).days <= 730


def mubasher(t):
    page = get(f"https://english.mubasher.info/markets/EGX/stocks/{t}")
    x = re.sub(r"\s+", " ", re.sub(r"\s*\|[\s|]*", "|", html.unescape(re.sub(r"<[^>]+>", "|", re.sub(r"<(script|style)[^>]*>.*?</\1>", "", page, flags=re.S)))))
    g = lambda pat: (re.search(pat, x) or [None, None])[1]
    cap, eps, bvps = num(g(r"Market Cap\|([\d.,]+)")), num(g(r"EPS\|([-\d.,]+)")), num(g(r"Book Value \(BVPS\)\|([-\d.,]+)"))
    based = g(r"EPS\|[-\d.,]+\|[^|]*\|Based on: (\w+ Quarter \d{4})") or g(r"Based on: (\w+ Quarter \d{4})")
    period = None
    if based:
        q, y = based.split(" Quarter ")
        period = f"{y}-{QUARTER_END[q]}"
    price = last_close("egx", t)
    rows = [{"label": "Market value", "value": big(cap, "EGP") if cap else None}]
    # a sanity check: per-share figures that cannot match the price (Orascom's, for one, look dollar-based though
    # labelled in pounds) are left out rather than shown as ratios of 150 or more
    sane = price and eps and bvps and 0 < price / bvps < 40 and (eps <= 0 or price / eps < 300)
    if fresh(period) and eps is not None and not sane:
        rows.append({"label": "Ratios", "value": "Not shown: Mubasher's per-share figures do not match the price"})
        basis, period = "per-share figures that do not match the price", None
    elif fresh(period) and eps is not None:
        rows += [{"label": "P/E", "value": ratio(price, eps)}, {"label": "P/B", "value": ratio(price, bvps)},
                 {"label": "Earnings per share (12 months)", "value": f"EGP {eps:,.2f}"},
                 {"label": "Book value per share", "value": f"EGP {bvps:,.2f}" if bvps is not None else None}]
        basis = f"results for the 12 months to {datetime.date.fromisoformat(period):%B %Y}"
    elif not period or not fresh(period):
        rows.append({"label": "Ratios", "value": "Not shown: no recent results on Mubasher"})
        basis, period = "no recent results on Mubasher", None
    return {"source": "Mubasher", "asOf": TODAY.isoformat(), "period": period, "basis": basis, "price": price, "rows": rows}


def nasdaq(t):
    sym = urllib.parse.quote(t)   # Nasdaq takes BRK.B as it is
    summ = json.loads(get(f"https://api.nasdaq.com/api/quote/{sym}/summary?assetclass=stocks"))["data"]["summaryData"]
    val = lambda k: (summ.get(k) or {}).get("value")
    price = last_close("us", t)
    rows = [{"label": "Market value", "value": big(num(val("MarketCap")), "USD") if num(val("MarketCap")) else None}]
    period, basis = None, "no reported earnings on Nasdaq"
    try:
        eps = json.loads(get(f"https://api.nasdaq.com/api/quote/{sym}/eps"))["data"]["earningsPerShare"]
        done = [q for q in eps if q["type"] == "PreviousQuarter"][-4:]
        if len(done) == 4:
            ttm = sum(q["earnings"] for q in done)
            mon, yr = done[-1]["period"].split()
            end = datetime.date(int(yr), MONTHS[mon] % 12 + 1, 1) - datetime.timedelta(days=1) if MONTHS[mon] < 12 else datetime.date(int(yr), 12, 31)
            period, basis = end.isoformat(), f"the four quarters to {done[-1]['period']}"
            rows += [{"label": "P/E (last 12 months)", "value": ratio(price, ttm)}]
            try:
                pe = json.loads(get(f"https://api.nasdaq.com/api/analyst/{sym}/peg-ratio"))["data"]["per"]["peRatioChart"]
                est = next((p for p in pe if "Estimate" in p["x"]), None)
                if est and est.get("y"):
                    rows.append({"label": f"Forecast P/E (fiscal {est['x'].split()[0]})", "value": f"{est['y']:.1f}"})
            except Exception:
                pass
            rows.append({"label": "Earnings per share (12 months)", "value": f"${ttm:,.2f}"})
    except Exception:
        pass
    y = val("Yield")
    rows.append({"label": "Dividend yield", "value": y if y and y not in ("N/A", "0%", "0.00%") else "None"})
    tgt = val("OneYrTarget")
    if tgt and tgt != "N/A":
        rows.append({"label": "Analysts' one-year target", "value": tgt})
    return {"source": "Nasdaq", "asOf": TODAY.isoformat(), "period": period, "basis": basis, "price": price, "rows": rows}


def one(t):
    try:
        return t, (mubasher if t in EGX else nasdaq)(t), None
    except Exception as e:
        return t, None, e


def main(args):
    tickers = [a.upper() for a in args] or EGX + US
    data = json.load(open(STOCKS))
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        results = list(pool.map(one, [t for t in tickers if t not in NOT_TRADING]))
    for t in tickers:
        if t in NOT_TRADING:
            print(f"{t}: not trading yet; left as it was")
    for t, v, err in results:
        if not v:
            print(f"{t}: failed ({err}); kept the card it had")
            continue
        data["stocks"].setdefault(t, {})["valuation"] = v
        shown = ", ".join(f"{r['label']} {r['value']}" for r in v["rows"][1:3] if r["value"])
        print(f"{t}: {v['rows'][0]['value']}, {shown or 'no ratios'} ({v['basis']})")
    with open(STOCKS, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1:])
