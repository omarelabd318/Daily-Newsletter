#!/usr/bin/env python3
"""Trend and momentum for every series in the data log: desk/indicators.json, shown on each stock's page.

Usage:
  python3 .claude/skills/markets-desk/indicators.py          # write desk/indicators.json
  python3 .claude/skills/markets-desk/indicators.py --test   # check the formulas against worked examples
  python3 .claude/skills/markets-desk/indicators.py COMI     # print one series

No network: everything comes from data/markets.json. The definitions, so the figures can be checked by hand:
- Sessions: the log repeats the last close on a day the market was shut, so a close equal to the one before it is
  dropped (a real unchanged close is rare, and counting holidays as sessions would flatten every average).
- SMA(n): the plain average of the last n closes. EMA(n): seeded with the SMA of the first n closes, then
  ema = close * k + ema * (1 - k), k = 2 / (n + 1).
- RSI(14), Wilder's: the first average gain and loss are plain averages of the first 14 changes; after that
  avg = (avg * 13 + today's) / 14. RSI = 100 - 100 / (1 + avg gain / avg loss); 100 when there are no losses.
- MACD: EMA(12) - EMA(26); signal: EMA(9) of the MACD line; histogram: MACD - signal.
- Trend: "up" when close > SMA50 > SMA200, "down" when close < SMA50 < SMA200; "turning down" (or "turning up")
  when the close is below (above) both averages but they have not yet crossed; otherwise "mixed".
- Crosses: SMA50 through SMA200 (golden or death cross) in the last 10 sessions; MACD through its signal in the
  last 5. `read` puts these in one plain sentence. They describe the price so far; they forecast nothing.
A figure that needs more history than the series has (Banque du Caire's 200-day average) is left out, never guessed.
"""
import json
import os
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
LOG = os.path.join(ROOT, "data", "markets.json")
OUT = os.path.join(ROOT, "desk", "indicators.json")
TOP = ["egx30", "egx70", "sp500", "nasdaq", "dow", "usd_egp", "brent", "gold_usd", "dxy", "btc"]


def sma(v, n):
    return sum(v[-n:]) / n if len(v) >= n else None


def ema_series(v, n):
    """EMA for every point from index n-1 on (None before): seeded with the SMA of the first n values."""
    if len(v) < n:
        return [None] * len(v)
    k, e = 2 / (n + 1), sum(v[:n]) / n
    out = [None] * (n - 1) + [e]
    for x in v[n:]:
        e = x * k + e * (1 - k)
        out.append(e)
    return out


def rsi(v, n=14):
    if len(v) < n + 1:
        return None
    ch = [b - a for a, b in zip(v, v[1:])]
    gain = sum(max(c, 0) for c in ch[:n]) / n
    loss = sum(max(-c, 0) for c in ch[:n]) / n
    for c in ch[n:]:
        gain = (gain * (n - 1) + max(c, 0)) / n
        loss = (loss * (n - 1) + max(-c, 0)) / n
    return 100.0 if loss == 0 else 100 - 100 / (1 + gain / loss)


def macd(v, fast=12, slow=26, sig=9):
    """(macd, signal, histogram) series aligned to v; None where there is not enough history."""
    f, s = ema_series(v, fast), ema_series(v, slow)
    line = [a - b if a is not None and b is not None else None for a, b in zip(f, s)]
    have = [x for x in line if x is not None]
    signal = [None] * (len(line) - len(have)) + ema_series(have, sig)
    hist = [a - b if a is not None and b is not None else None for a, b in zip(line, signal)]
    return line, signal, hist


def cross(a, b, within):
    """'up' or 'down' if series a crossed b in the last `within` points (the latest cross), and how many sessions ago."""
    pts = [(x - y) for x, y in zip(a, b) if x is not None and y is not None]
    for back in range(1, min(within, len(pts) - 1) + 1):
        now, prev = pts[-back], pts[-back - 1]
        if prev <= 0 < now:
            return "up", back - 1
        if prev >= 0 > now:
            return "down", back - 1
    return None, None


def sessions(days, pick):
    out = []
    for e in days:
        x = pick(e)
        if isinstance(x, (int, float)) and (not out or x != out[-1][1]):
            out.append((e["date"], x))
    return out


def measure(s):
    v = [x for _, x in s]
    if len(v) < 15:
        return None
    r = lambda x, d=2: None if x is None else round(x, d)
    last = v[-1]
    s20, s50, s200 = sma(v, 20), sma(v, 50), sma(v, 200)
    line, signal, hist = macd(v)
    sma50s = [sma(v[:i], 50) for i in range(len(v) - 11, len(v) + 1)] if len(v) >= 212 else []
    sma200s = [sma(v[:i], 200) for i in range(len(v) - 11, len(v) + 1)] if len(v) >= 212 else []
    gx, gx_ago = cross(sma50s, sma200s, 10) if sma50s else (None, None)
    mx, mx_ago = cross(line, signal, 5)
    R = rsi(v)
    trend = None if s50 is None or s200 is None else "up" if last > s50 > s200 else "down" if last < s50 < s200 else "turning down" if last < min(s50, s200) else "turning up" if last > max(s50, s200) else "mixed"
    yr = v[-250:]
    out = {"asOf": s[-1][0], "sessions": len(v), "close": last, "sma20": r(s20), "sma50": r(s50), "sma200": r(s200),
           "vs50": r((last / s50 - 1) * 100, 1) if s50 else None, "vs200": r((last / s200 - 1) * 100, 1) if s200 else None,
           "rsi": r(R, 1), "macd": r(line[-1], 3), "signal": r(signal[-1], 3), "hist": r(hist[-1], 3), "trend": trend,
           "goldenCross": {"dir": gx, "ago": gx_ago} if gx else None, "macdCross": {"dir": mx, "ago": mx_ago} if mx else None,
           "range": r((last - min(yr)) / (max(yr) - min(yr)) * 100, 0) if max(yr) > min(yr) else None}
    # one plain sentence
    bits = []
    if trend:
        bits.append({"up": "In an uptrend: above its 50-day average, which is above the 200-day",
                     "down": "In a downtrend: below its 50-day average, which is below the 200-day",
                     "turning down": f"Turning down: below both its 50-day average ({abs(out['vs50'])}% under) and its 200-day ({abs(out['vs200'])}% under), though the 50-day is still above the 200-day",
                     "turning up": f"Turning up: above both its 50-day average ({abs(out['vs50'])}% over) and its 200-day ({abs(out['vs200'])}% over), though the 50-day is still below the 200-day",
                     "mixed": f"No clear trend: {abs(out['vs50'])}% {'above' if out['vs50'] >= 0 else 'below'} its 50-day average and {abs(out['vs200'])}% {'above' if out['vs200'] >= 0 else 'below'} the 200-day"}[trend])
    elif s50:
        bits.append(f"{abs(out['vs50'])}% {'above' if out['vs50'] >= 0 else 'below'} its 50-day average; too little history for the 200-day")
    if R is not None:
        bits.append(f"RSI {R:.0f}, " + ("stretched after a run: above 70" if R >= 70 else "washed out: below 30" if R <= 30 else "neither stretched nor washed out"))
    if gx:
        bits.append(f"the 50-day average crossed {'above' if gx == 'up' else 'below'} the 200-day {'today' if not gx_ago else str(gx_ago) + ' sessions ago'}")
    if mx:
        bits.append(f"momentum turned {'up' if mx == 'up' else 'down'} {'today' if not mx_ago else str(mx_ago) + ' sessions ago'} (MACD crossed its signal line)")
    out["read"] = "; ".join(bits) + "." if bits else None
    return out


def build():
    days = json.load(open(LOG))["days"]
    out = {}
    for k in TOP:
        m = measure(sessions(days, lambda e, k=k: e.get(k)))
        if m:
            out[k] = m
    for g in ("egx", "us"):
        for t in sorted({t for e in days for t in (e.get(g) or {})}):
            m = measure(sessions(days, lambda e, g=g, t=t: (e.get(g) or {}).get(t)))
            if m:
                out[f"{g}.{t}"] = m
    return out


def test():
    # Wilder's worked example (the one StockCharts publishes): first RSI(14) of these closes is 70.46
    c = [44.34, 44.09, 44.15, 43.61, 44.33, 44.83, 45.10, 45.42, 45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28]
    assert abs(rsi(c) - 70.46) < 0.1, rsi(c)
    c2 = c + [46.00, 46.03, 46.41, 46.22, 45.64]
    assert abs(rsi(c2) - 57.9) < 0.6, rsi(c2)                       # 57.97 in the published table
    assert rsi(list(range(1, 30))) == 100.0 and rsi([5] * 10) is None
    assert abs(rsi(list(range(30, 1, -1))) - 0.0) < 1e-9
    assert sma([1, 2, 3, 4, 5], 5) == 3 and sma([1, 2], 5) is None
    e = ema_series([1, 2, 3, 4, 5, 6], 3)                           # seed 2, k = 0.5: 3, 4, 5
    assert e == [None, None, 2.0, 3.0, 4.0, 5.0], e
    flat = [10.0] * 60
    line, signal, hist = macd(flat)
    assert abs(line[-1]) < 1e-12 and abs(hist[-1]) < 1e-12 and line[24] is None and line[25] is not None and signal[32] is None and signal[33] is not None
    up = [100 + i for i in range(60)]                               # a steady rise: fast EMA above slow, MACD positive
    assert macd(up)[0][-1] > 0 and cross([1, 1, 3], [2, 2, 2], 5) == ("up", 0) and cross([3, 1, 1], [2, 2, 2], 5) == ("down", 1)
    assert sessions([{"date": "a", "x": 1}, {"date": "b", "x": 1}, {"date": "c", "x": 2}, {"date": "d"}], lambda e: e.get("x")) == [("a", 1), ("c", 2)]
    assert measure([("d", 1.0)] * 3) is None
    print("indicators: all formula checks pass")


if __name__ == "__main__":
    if "--test" in sys.argv:
        test()
    else:
        test()
        data = build()
        args = [a for a in sys.argv[1:] if not a.startswith("-")]
        if args:
            for k, v in data.items():
                if k.split(".")[-1].upper() in [a.upper() for a in args]:
                    print(k, json.dumps(v, indent=1))
        else:
            json.dump({"note": "Trend and momentum from the data log, by indicators.py (its docstring has every formula). They describe the price so far and forecast nothing.", "series": data}, open(OUT, "w"), indent=1)
            open(OUT, "a").write("\n")
            ex = data.get("egx30", {})
            print(f"indicators: {len(data)} series; EGX30 {ex.get('trend')}, RSI {ex.get('rsi')}")
