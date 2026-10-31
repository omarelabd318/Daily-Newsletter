#!/usr/bin/env python3
"""Refresh each desk stock's valuation card in desk/stocks.json ("valuation").

Usage:
  python3 .claude/skills/markets-desk/fetch_valuation.py [TICKER ...]

With no tickers it covers all the desk's stocks. Egyptian stocks: trailing earnings and book value per share
from TradingView's screener and from each stock's Mubasher page, each with the results period it runs to; the
card takes the newer, and when both run to the same quarter it notes whether they agree. Market value from Mubasher. US stocks:
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
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL"]
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


TV = {}


def tradingview():
    """Egyptian stocks' trailing earnings and book value per share from TradingView's screener, with the quarter they
    run to: usually a quarter newer than Mubasher's. One request for all of them; an unofficial endpoint, so a
    failure leaves Mubasher to carry the cards."""
    body = json.dumps({"symbols": {"tickers": [f"EGX:{t}" for t in EGX]},
                       "columns": ["market_cap_basic", "earnings_per_share_basic_ttm", "book_value_per_share_fq", "fiscal_period_end_fq"]}).encode()
    req = urllib.request.Request("https://scanner.tradingview.com/egypt/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    for r in json.loads(urllib.request.urlopen(req, timeout=40).read())["data"]:
        cap, eps, bvps, end = r["d"]
        TV[r["s"].split(":")[1]] = (cap, eps, bvps, datetime.datetime.fromtimestamp(end, datetime.timezone.utc).date().isoformat() if end else None)


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
    return cap, eps, bvps, period


def egx(t):
    """The newest usable figures of the two sources; when both run to the same quarter, the other one checks it."""
    price, cands = last_close("egx", t), []
    if TV.get(t):
        cands.append(("TradingView", *TV[t]))
    try:
        cands.append(("Mubasher", *mubasher(t)))
    except Exception:
        pass
    if not cands:
        raise ValueError("neither TradingView nor Mubasher answered")
    cap = next((c[1] for c in sorted(cands, key=lambda c: c[0] != "Mubasher") if c[1]), None)
    # a sanity check: per-share figures that cannot match the price (Mubasher's for Orascom look dollar-based
    # though labelled in pounds) are left out rather than shown as ratios of 150 or more
    sane = lambda c: price and c[2] and c[3] and 0 < price / c[3] < 40 and (c[2] <= 0 or price / c[2] < 300)
    usable = sorted([c for c in cands if fresh(c[4]) and sane(c)], key=lambda c: c[4], reverse=True)
    rows = [{"label": "Market value", "value": big(cap, "EGP") if cap else None}]
    if not usable:
        why = "per-share figures that do not match the price" if any(fresh(c[4]) for c in cands) else "no recent results"
        rows.append({"label": "Ratios", "value": f"Not shown: {why}"})
        return {"source": " and ".join(c[0] for c in cands), "asOf": TODAY.isoformat(), "period": None, "basis": why, "price": price, "rows": rows}
    src, _, eps, bvps, period = usable[0]
    basis = f"results for the 12 months to {datetime.date.fromisoformat(period):%B %Y}"
    other = next((c for c in usable[1:] if c[4] == period), None)
    if other:
        basis += f"; {other[0]} agrees" if abs(other[2] - eps) <= 0.1 * abs(eps) else f"; {other[0]} gives EGP {other[2]:,.2f} a share for the same period"
    rows += [{"label": "P/E", "value": ratio(price, eps)}, {"label": "P/B", "value": ratio(price, bvps)},
             {"label": "Earnings per share (12 months)", "value": f"EGP {eps:,.2f}"},
             {"label": "Book value per share", "value": f"EGP {bvps:,.2f}"}]
    return {"source": src, "asOf": TODAY.isoformat(), "period": period, "basis": basis, "price": price, "rows": rows}


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
        return t, (egx if t in EGX else nasdaq)(t), None
    except Exception as e:
        return t, None, e


def main(args):
    tickers = [a.upper() for a in args] or EGX + US
    data = json.load(open(STOCKS))
    if any(t in EGX for t in tickers):
        try:
            tradingview()
        except Exception as e:
            print(f"TradingView: failed ({e}); Egyptian cards use Mubasher alone")
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
