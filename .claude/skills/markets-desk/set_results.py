#!/usr/bin/env python3
"""Record an Egyptian desk stock's newly filed results, so its P/E and P/B use them before TradingView or Mubasher do.

Usage:
  python3 .claude/skills/markets-desk/set_results.py TICKER --period 2026-09-30 --shares 1262000000 \\
      (--ttm 12970000000 | --ytd 9.8e9 --prior-fy 8.1e9 --prior-ytd 6.2e9) [--equity 41e9] \\
      --source "EGX disclosure" --url https://...

  --period     the last day of the results period (a quarter end)
  --ttm        net profit attributable to shareholders over the last 12 months, EGP
  --ytd, --prior-fy, --prior-ytd
               or the three figures it is worked out from, when the company reports the year to date:
               this year to date + last full year - last year's same period
  --shares     shares outstanding (after any bonus shares)
  --equity     shareholders' equity at the period end, EGP (for book value per share; optional)
  --source, --url  the filing or the outlet that carried it

Writes the stock's "filed" entry in desk/stocks.json and prints earnings and book value per share; then run
fetch_valuation.py TICKER, which takes the filing when it runs to a newer quarter than the screen sources.
"""
import argparse
import datetime
import json
import os

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
STOCKS = os.path.join(ROOT, "desk", "stocks.json")


def main():
    a = argparse.ArgumentParser()
    a.add_argument("ticker")
    a.add_argument("--period", required=True)
    a.add_argument("--ttm", type=float)
    a.add_argument("--ytd", type=float)
    a.add_argument("--prior-fy", type=float)
    a.add_argument("--prior-ytd", type=float)
    a.add_argument("--shares", type=float, required=True)
    a.add_argument("--equity", type=float)
    a.add_argument("--source", required=True)
    a.add_argument("--url", required=True)
    o = a.parse_args()
    datetime.date.fromisoformat(o.period)
    if o.ttm is None:
        if None in (o.ytd, o.prior_fy, o.prior_ytd):
            a.error("give --ttm, or --ytd with --prior-fy and --prior-ytd")
        o.ttm = o.ytd + o.prior_fy - o.prior_ytd
        how = f"{o.ytd:,.0f} this year to date + {o.prior_fy:,.0f} last year - {o.prior_ytd:,.0f} a year earlier"
    else:
        how = "12-month profit as filed"
    eps = o.ttm / o.shares
    bvps = o.equity / o.shares if o.equity else None
    data = json.load(open(STOCKS))
    t = o.ticker.upper()
    if t not in data["stocks"]:
        a.error(f"{t} is not a desk stock")
    data["stocks"][t]["filed"] = {"period": o.period, "eps_ttm": round(eps, 4), "bvps": round(bvps, 4) if bvps else None,
                                  "profit_ttm": o.ttm, "shares": o.shares, "how": how, "source": o.source, "url": o.url,
                                  "recorded": datetime.date.today().isoformat()}
    with open(STOCKS, "w") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"{t}: results to {o.period}: earnings per share EGP {eps:,.2f} ({how})"
          + (f", book value per share EGP {bvps:,.2f}" if bvps else "") + ". Now run fetch_valuation.py " + t)


if __name__ == "__main__":
    main()
