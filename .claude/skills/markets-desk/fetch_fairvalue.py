#!/usr/bin/env python3
"""The desk's fair values for EGX stocks: desk/fairvalue.json, shown on the Views page under "Fair value".

Usage:
  python3 .claude/skills/markets-desk/fetch_fairvalue.py          # refresh the figures, keep the judgement
  python3 .claude/skills/markets-desk/fetch_fairvalue.py --show   # print the table without writing

What it answers: which EGX stocks are cheap or dear AGAINST THE REST OF THE EGX, given what they earn, own and
are forecast to be worth. It does not say whether the EGX as a whole is cheap (the file's `market` block gives
that reading separately). The method, in the order the code runs it (SKILL.md, "Fair value", has the reasoning):

1. Universe: EGX stocks priced in pounds, worth EGP 3bn or more, trading EGP 5m a day or more on the 30-day
   average, with positive 12-month earnings from results no older than nine months. The desk's own stocks are
   always in when they have earnings; their per-share figures come from desk/stocks.json (the valuation card,
   which prefers the company's filing), everything else from TradingView's screener.
2. Normalised earnings: 12-month EPS, unless `judgement[T].eps_norm` replaces it (a one-off gain, a cycle peak,
   new shares on the way), always with a written `eps_reason`.
3. Three estimates per stock:
   - earnings: normalised EPS x a fair P/E, where the fair P/E is three quarters its peer group's median P/E and
     one quarter the universe's (a group needs four members, else the universe's alone; non-bank financials have
     no group), moved up or down by as much as 25% for the stock's rank on ROE and profit growth;
   - assets: book value per share x a justified P/B = (ROE - g) / (k - g), with ROE pulled 40% of the way to
     the universe median and capped at 45%, g = 10% long-run growth, and k set so the median stock comes out
     fairly valued (banks get their own k: they are measured against banks). Skipped when P/B is above 6: book value says little about ports, tobacco or payments;
   - analysts: brokers' fair values recorded in `judgement[T].brokers` (last 180 days) and TradingView's
     consensus one-year target, the targets brought back one year at k less the dividend yield. A consensus
     more than 40% from the price and from every other estimate is taken as out of date and left out.
4. Fair value: the weighted average (earnings 0.4, assets 0.3, analysts 0.3; a lone analyst counts half), over
   the estimates a stock has; it needs at least two. `spread` is how far apart they are: the confidence.
5. Four grades (Excellent, Great, Good, Fair, Weak) from the stock's rank in the universe: profitability (ROE
   and net margin), growth (revenue and profit over 12 months, capped at +/-100%), financial health (debt to
   equity and net debt to market value; for banks, equity to assets) and cash flow (free cash flow margin and
   yield; not graded for banks).
   A stock with `judgement[T].exclude` (a reason) is listed as not rated, as is one whose results are too old.
6. `judgement[T].note` is the desk's own line on the stock (the catch, or why the gap is real): written by the
   run, never by this script, and kept between runs.
"""
import datetime
import json
import os
import statistics
import sys
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "desk", "fairvalue.json")
STOCKS = os.path.join(ROOT, "desk", "stocks.json")
LOG = os.path.join(ROOT, "data", "markets-recent.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
TODAY = datetime.date.today()
# long-run nominal growth for Egypt is 10%: the central bank's 7% inflation target plus about 3% real growth (CFG)
ROE_CAP, SHRINK = 45.0, 0.4
TILT = 0.25
W = {"earnings": 0.4, "assets": 0.3, "analysts": 0.3}
MAX_AGE = 275
COLS = ["name", "description", "sector", "industry", "currency", "close", "market_cap_basic", "average_volume_30d_calc", "indexes",
        "earnings_per_share_basic_ttm", "last_annual_eps", "book_value_per_share_fq", "fiscal_period_end_fq",
        "return_on_equity", "return_on_assets", "net_margin_ttm", "total_revenue_yoy_growth_ttm", "net_income_yoy_growth_ttm",
        "total_revenue_yoy_growth_fy", "debt_to_equity", "net_debt", "free_cash_flow_margin_ttm", "free_cash_flow",
        "dividends_yield_current", "price_target_average", "price_target_low", "price_target_high", "Perf.6M", "SMA200", "RSI"]
# peer groups, from TradingView's sectors and the desk's own
GROUP = {"Finance": "Financials", "Banks": "Banks", "Real estate": "Real estate", "Process Industries": "Materials",
         "Non-Energy Minerals": "Materials", "Energy Minerals": "Materials", "Consumer Non-Durables": "Consumer",
         "Consumer Durables": "Real estate", "Consumer Services": "Consumer", "Retail Trade": "Consumer",
         "Health Technology": "Healthcare", "Health Services": "Healthcare", "Producer Manufacturing": "Industrials",
         "Industrial Services": "Industrials", "Transportation": "Industrials", "Technology Services": "Technology",
         "Communications": "Technology", "Distribution Services": "Consumer", "Utilities": "Industrials"}
DESK_GROUP = {"Banks": "Banks", "Real estate": "Real estate", "Telecoms": "Technology", "Cables and electrical": "Industrials",
              "Construction": "Industrials", "Payments": "Technology", "Fertilizers": "Materials", "Investment banking": "Financials",
              "Healthcare": "Healthcare", "Food": "Consumer", "Ports": "Industrials", "Tobacco": "Consumer", "Metals": "Materials",
              "Oil refining": "Materials", "Petrochemicals": "Materials"}
INDUSTRY = {"Regional Banks": "Banks", "Major Banks": "Banks", "Real Estate Development": "Real estate", "Homebuilding": "Real estate",
            "Real Estate Investment Trusts": "Real estate"}
GRADES = ["Weak", "Fair", "Good", "Great", "Excellent"]


US = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST"]
# Wall Street: US-listed common stocks worth $50bn or more, the same three estimates; g is 6% (2% inflation, about 2%
# real growth and buybacks), and peer groups are TradingView's sectors
CFG = {"egx": {"market": "egypt", "cur": "EGP", "g": 10.0, "min_cap": 3e9, "min_traded": 5e6, "index": "EGX 30"},
       "us": {"market": "america", "cur": "USD", "g": 6.0, "min_cap": 50e9, "min_traded": 0, "index": "S&P 100",
              # US reported earnings carry more one-offs and US targets come from many analysts, so the weights lean to
              # analysts, and a P/E outside 4 to 60 gives no earnings estimate at all
              "w": {"earnings": 0.3, "assets": 0.2, "analysts": 0.5}, "pe_ok": (4, 60)}}


def scan(mkt="egx"):
    c = CFG[mkt]
    flt = [{"left": "is_primary", "operation": "equal", "right": True}]
    if mkt == "us":
        flt += [{"left": "market_cap_basic", "operation": "greater", "right": c["min_cap"]}, {"left": "type", "operation": "equal", "right": "stock"},
                {"left": "typespecs", "operation": "has", "right": ["common"]}]
    body = json.dumps({"filter": flt, "markets": [c["market"]],
                       "columns": COLS, "range": [0, 500], "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"}}).encode()
    req = urllib.request.Request(f"https://scanner.tradingview.com/{c['market']}/scan", data=body, headers={"User-Agent": UA, "Content-Type": "application/json"})
    return [dict(zip(COLS, r["d"])) for r in json.loads(urllib.request.urlopen(req, timeout=40).read())["data"]]


def num(s):
    try:
        return float(str(s).replace("EGP", "").replace(",", "").strip())
    except ValueError:
        return None


def desk_figures():
    """The desk's own per-share figures (the valuation card) and latest logged closes for its Egyptian stocks."""
    out, days = {}, json.load(open(LOG))["days"]
    for t, x in json.load(open(STOCKS))["stocks"].items():
        v = x.get("valuation") or {}
        rows = {r["label"]: r["value"] for r in v.get("rows", []) if r.get("value")}
        if "EGP" not in json.dumps(rows):
            continue
        price = next((e["egx"][t] for e in reversed(days) if isinstance((e.get("egx") or {}).get(t), (int, float))), None)
        out[t] = {"sector": x.get("sector"), "price": price, "eps": num(rows.get("Earnings per share (12 months)", "")),
                  "bvps": num(rows.get("Book value per share", "")), "period": v.get("period"), "source": v.get("source")}
    return out


def rate():
    """After-tax one-year T-bill yield: what a pound earns with no risk, for the `market` reading."""
    for e in reversed(json.load(open(LOG))["days"]):
        for k in ("tbill_364", "tbill_273", "tbill_182"):
            if e.get(k):
                return round(e[k] * 0.8, 2), k, e["date"]
    return None, None, None


def pct_rank(vals, v, low_good=False):
    xs = sorted(x for x in vals if x is not None)
    if v is None or len(xs) < 8:
        return None
    r = sum(1 for x in xs if x < v) + 0.5 * sum(1 for x in xs if x == v)
    r /= len(xs)
    return 1 - r if low_good else r


def grade(ranks):
    ranks = [r for r in ranks if r is not None]
    if not ranks:
        return None
    return GRADES[min(4, int(sum(ranks) / len(ranks) * 5))]


def clip(v, lo, hi):
    return None if v is None else max(lo, min(hi, v))


def us_closes():
    days = json.load(open(LOG))["days"]
    return {t: next((e["us"][t] for e in reversed(days) if isinstance((e.get("us") or {}).get(t), (int, float))), None) for t in US}


def build(saved, mkt="egx"):
    C, G = CFG[mkt], CFG[mkt]["g"]
    MIN_CAP, MIN_TRADED = C["min_cap"], C["min_traded"]
    W = C.get("w", globals()["W"])
    J = saved.get("judgement" if mkt == "egx" else "judgementUS", {})
    desk, tv = (desk_figures() if mkt == "egx" else {}), scan(mkt)
    usc = us_closes() if mkt == "us" else {}
    rows, excluded = [], []
    for r in tv:
        t = r["name"]
        if r["currency"] != C["cur"] or not r["close"]:
            continue
        d = desk.get(t)
        price = (d and d["price"]) or usc.get(t) or r["close"]
        end = datetime.datetime.fromtimestamp(r["fiscal_period_end_fq"], datetime.timezone.utc).date().isoformat() if r["fiscal_period_end_fq"] else None
        eps, bvps, period, basis = r["earnings_per_share_basic_ttm"], r["book_value_per_share_fq"], end, "12 months"
        swapped = None
        if d and d["eps"]:
            eps, period = d["eps"], d["period"]
            if "last full year" in (d["source"] or ""):
                basis = "last full year"
            bvps = d["bvps"] or bvps
            # Mubasher's per-share figures can rest on the parent company alone or on a share count from before a
            # bonus issue: when TradingView's last full-year EPS (consolidated profit over today's shares) is more
            # than 25% away, take TradingView's and say so
            la = r["last_annual_eps"]
            if "Mubasher" in (d["source"] or "") and "filing" not in (d["source"] or "") and la and la > 0 and abs(la / eps - 1) > 0.25:
                swapped, eps, basis, period = round(eps, 2), la, "last full year", end or period
                bvps = r["book_value_per_share_fq"] or bvps
        elif eps is None and r["last_annual_eps"]:
            eps, basis = r["last_annual_eps"], "last full year"
        traded = (r["average_volume_30d_calc"] or 0) * price
        age = (TODAY - datetime.date.fromisoformat(period)).days if period else 999
        if not eps or eps <= 0:
            continue
        if J.get(t, {}).get("exclude"):
            excluded.append({"t": t, "name": r["description"], "price": price, "period": period, "why": J[t]["exclude"]})
            continue
        if not d and ((r["market_cap_basic"] or 0) < MIN_CAP or traded < MIN_TRADED or age > MAX_AGE):
            continue
        j = J.get(t, {})
        roe = r["return_on_equity"] if r["return_on_equity"] is not None else (eps / bvps * 100 if bvps and bvps > 0 else None)
        rows.append({"t": t, "name": r["description"], "desk": bool(d) or t in usc, "egx30": any(i["name"] == C["index"] for i in (r["indexes"] or [])),
                     "group": (d and DESK_GROUP.get(d["sector"])) or INDUSTRY.get(r["industry"]) or (GROUP.get(r["sector"], "Other") if mkt == "egx" else (r["sector"] or "Other")),
                     "sector": (d and d["sector"]) or r["sector"], "price": price, "cap": r["market_cap_basic"], "traded": round(traded),
                     "eps": eps, "epsNorm": j.get("eps_norm") or eps, "epsBasis": basis, "bvps": bvps, "period": period, "stale": age > MAX_AGE, "epsSwapped": swapped,
                     "roe": roe, "dy": r["dividends_yield_current"] or 0, "_": r})
    # quality tilt: a stock's rank in the universe on profitability (ROE) and profit growth moves its fair P/E by up
    # to 25% either way; a missing figure counts as the middle
    roe_all = [x["roe"] for x in rows]
    gr_all = [clip(x["_"]["net_income_yoy_growth_ttm"], -100, 100) for x in rows]
    for x in rows:
        q = [pct_rank(roe_all, x["roe"]), pct_rank(gr_all, clip(x["_"]["net_income_yoy_growth_ttm"], -100, 100))]
        q = sum(0.5 if v is None else v for v in q) / 2
        x["tilt"] = round(1 + TILT * (q - 0.5) * 2, 3)
    # fair P/E: half the peer group's median, half the universe's
    pes = {x["t"]: x["price"] / x["epsNorm"] for x in rows}
    usable = lambda v: 1.5 < v < 40
    all_med = statistics.median(v for v in pes.values() if usable(v))
    groups = {}
    for x in rows:
        if usable(pes[x["t"]]) and x["group"] != "Financials":   # holding companies and brokers are not each other's peers
            groups.setdefault(x["group"], []).append(pes[x["t"]])
    gmed = {g: statistics.median(v) for g, v in groups.items() if len(v) >= 4}
    roe_med = statistics.median(x["roe"] for x in rows if x["roe"] is not None and x["roe"] > 0)
    for x in rows:
        x["roeS"] = None if x["roe"] is None else min(ROE_CAP, (1 - SHRINK) * x["roe"] + SHRINK * roe_med)
    pb_ok = lambda x: x["bvps"] and x["bvps"] > 0 and x["roeS"] and x["roeS"] > G + 2 and x["price"] / x["bvps"] <= 6

    def assets(x, k):
        return x["bvps"] * (x["roeS"] - G) / (k - G)
    # k: the discount rate at which the median stock is fairly valued on assets (bisection)
    def solve(members):
        lo, hi = G + 2, 80.0
        for _ in range(60):
            k = (lo + hi) / 2
            m = statistics.median(assets(x, k) / x["price"] for x in members)
            lo, hi = (k, hi) if m > 1 else (lo, k)
        return k
    is_bank = lambda x: x["group"] == "Banks"
    k_all = solve([x for x in rows if pb_ok(x) and not is_bank(x)])
    bank_set = [x for x in rows if pb_ok(x) and is_bank(x)]
    k_bank = solve(bank_set) if len(bank_set) >= 5 else k_all
    out, stale = [], []
    for x in rows:
        r, j, est = x.pop("_"), J.get(x["t"], {}), {}
        k = k_bank if is_bank(x) else k_all
        if x["stale"]:
            x.update({"fair": None, "upside": None, "pe": round(pes[x["t"]], 1), "grades": {}, "why": "latest results in the sources are more than nine months old"})
            stale.append(x)
            continue
        pe_fair = (0.75 * gmed.get(x["group"], all_med) + 0.25 * all_med) * x["tilt"]
        if not C.get("pe_ok") or C["pe_ok"][0] <= pes[x["t"]] <= C["pe_ok"][1]:
            est["earnings"] = x["epsNorm"] * pe_fair
        if pb_ok(x):
            est["assets"] = assets(x, k)
        back = 1 + max(0.0, (k - x["dy"])) / 100
        an, wa = [], W["analysts"]
        for b in j.get("brokers", []):
            if (TODAY - datetime.date.fromisoformat(b["date"])).days <= 180:
                an.append(b["value"] / (back if b.get("kind") == "target" else 1))
        tv_t = r["price_target_average"] / back if r["price_target_average"] else None
        # TradingView's consensus carries no date: one that sits more than 40% from every other estimate is taken as
        # out of date (targets set before a bonus issue or a doubling) and left out, with a flag
        others = list(est.values()) + an
        if tv_t and others and all(abs(tv_t / o - 1) > 0.4 for o in others) and abs(tv_t / x["price"] - 1) > 0.4:
            x["targetOut"] = True
        elif tv_t:
            an.append(tv_t)
            if r["price_target_low"] == r["price_target_high"] and not j.get("brokers"):
                wa /= 2
        if an:
            est["analysts"] = sum(an) / len(an)
        if len(est) < 2:
            continue
        w = {k2: (wa if k2 == "analysts" else W[k2]) for k2 in est}
        fair = sum(est[k2] * w[k2] for k2 in est) / sum(w.values())
        vals = sorted(est.values())
        spread = vals[-1] / vals[0] - 1
        x.update({"fair": round(fair, 2 if fair < 100 else 1), "upside": round((fair / x["price"] - 1) * 100, 1),
                  "est": {k2: round(v, 2) for k2, v in est.items()}, "peFair": round(pe_fair, 1), "pe": round(pes[x["t"]], 1),
                  "pb": round(x["price"] / x["bvps"], 1) if x["bvps"] and x["bvps"] > 0 else None,
                  "confidence": "high" if len(est) == 3 and spread <= 0.35 else "low" if spread > 0.8 or len(est) == 2 and spread > 0.5 else "medium",
                  "target": r["price_target_average"], "below200": bool(r["SMA200"] and x["price"] < r["SMA200"]), "perf6m": r["Perf.6M"], "rsi": round(r["RSI"]) if r["RSI"] else None,
                  "raw": {"margin": r["net_margin_ttm"], "rev": r["total_revenue_yoy_growth_ttm"] if r["total_revenue_yoy_growth_ttm"] is not None else r["total_revenue_yoy_growth_fy"],
                          "profit": r["net_income_yoy_growth_ttm"], "de": r["debt_to_equity"],
                          "ndcap": r["net_debt"] / r["market_cap_basic"] if r["net_debt"] is not None and r["market_cap_basic"] else None,
                          "eqa": r["return_on_assets"] / r["return_on_equity"] if r["return_on_assets"] and r["return_on_equity"] else None,
                          "fcfm": r["free_cash_flow_margin_ttm"], "fcfy": r["free_cash_flow"] / r["market_cap_basic"] if r["free_cash_flow"] is not None and r["market_cap_basic"] else None}})
        out.append(x)
    raws = [x["raw"] for x in out]
    col = lambda key: [w[key] for w in raws]
    roes = [x["roe"] for x in out]
    for x in out:
        w, bank = x.pop("raw"), x["group"] == "Banks"
        x["grades"] = {
            "profitability": grade([pct_rank(roes, x["roe"]), pct_rank(col("margin"), w["margin"])]),
            "growth": grade([pct_rank([clip(v, -100, 100) for v in col("rev")], clip(w["rev"], -100, 100)),
                             pct_rank([clip(v, -100, 100) for v in col("profit")], clip(w["profit"], -100, 100))]),
            "health": grade([pct_rank(col("eqa"), w["eqa"])] if bank else [pct_rank(col("de"), w["de"], True), pct_rank(col("ndcap"), w["ndcap"], True)]),
            "cash": None if bank else grade([pct_rank(col("fcfm"), w["fcfm"]), pct_rank(col("fcfy"), w["fcfy"])])}
        for k2 in ("roe", "roeS", "dy", "perf6m", "target"):
            x[k2] = None if x[k2] is None else round(x[k2], 1)
        x["eps"], x["epsNorm"] = round(x["eps"], 2), round(x["epsNorm"], 2)
        j = J.get(x["t"], {})
        for k2 in ("note", "eps_reason", "noted"):
            if j.get(k2):
                x[k2] = j[k2]
        if x.get("epsSwapped") and x["confidence"] == "high":
            x["confidence"] = "medium"
        if not x.get("epsSwapped"):
            x.pop("epsSwapped", None)
    out.sort(key=lambda x: -x["upside"])
    for x in stale:
        x.pop("_", None)
    rf, rf_key, rf_date = rate()
    med_pe = statistics.median(x["pe"] for x in out)
    return {"asOf": TODAY.isoformat(), "count": len(out), "cur": C["cur"], "k": round(k_all, 1), "kBanks": round(k_bank, 1), "g": G, "roeMedian": round(roe_med, 1), "peMedian": round(all_med, 1),
            "groupPE": {g: round(v, 1) for g, v in sorted(gmed.items())},
            "market": {"medianPE": round(med_pe, 1), "earningsYield": round(100 / med_pe, 1), **({"tbillAfterTax": rf, "tbillKey": rf_key, "tbillDate": rf_date} if mkt == "egx" else {})},
            "stocks": out, "notRated": [{k2: x[k2] for k2 in ("t", "name", "price", "period", "why")} for x in stale] + excluded}


def main():
    saved = json.load(open(OUT)) if os.path.exists(OUT) else {}
    new = build(saved)
    if "--us" in sys.argv:
        new = build(saved, "us")
    if "--show" in sys.argv:
        for x in new["stocks"]:
            g = x["grades"]
            print(f"{x['t']:6s} {x['group']:11s} px{x['price']:8.2f} fair{x['fair']:8.2f} {x['upside']:+6.1f}% {x['confidence']:6s} pe{x['pe']:5.1f}/{x['peFair']:4.1f} pb{x['pb'] or 0:4.1f} roe{x['roe'] or 0:5.1f} "
                  + " ".join(f"{k}={v:.1f}" for k, v in x["est"].items()) + f" | {g['profitability']},{g['growth']},{g['health']},{g['cash']}")
        print({k: v for k, v in new.items() if k != "stocks"})
        return
    note = ("The desk's fair values for EGX stocks, against the rest of the EGX. Figures are rebuilt by fetch_fairvalue.py; "
            "`judgement` (normalised earnings, brokers' fair values and the desk's note per stock) is written by the run and kept.")
    try:
        us = build(saved, "us")
        print(f"fair value, US: {us['count']} stocks, k {us['k']}%, median P/E {us['peMedian']}")
    except Exception as e:   # the Egyptian table never waits on the US one
        us = saved.get("us")
        print(f"fair value, US: failed ({e}); kept the saved table")
    json.dump({"note": note, **new, "judgement": saved.get("judgement", {}), "us": us, "judgementUS": saved.get("judgementUS", {})}, open(OUT, "w"), ensure_ascii=False, indent=1)
    open(OUT, "a").write("\n")
    top, bot = new["stocks"][:3], new["stocks"][-3:]
    print(f"fair value: {new['count']} stocks, k {new['k']}%, median P/E {new['peMedian']}; cheapest " + ", ".join(f"{x['t']} {x['upside']:+.0f}%" for x in top)
          + "; dearest " + ", ".join(f"{x['t']} {x['upside']:+.0f}%" for x in bot))


if __name__ == "__main__":
    main()
