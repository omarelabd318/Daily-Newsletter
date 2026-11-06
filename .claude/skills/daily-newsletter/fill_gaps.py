#!/usr/bin/env python3
"""Find and fill gaps in data/markets.json: figures missing from a recent entry although the entries around it have them.

Usage:
  python3 .claude/skills/daily-newsletter/fill_gaps.py [DATE] [DAYS] [--write]

Looks at the DAYS entries up to DATE (default today, 10 days). An entry dated D holds the closes of the last session
before D, so each gap is filled with that session's close:
  - gold, the dollar index, Brent, bitcoin, the US indices and the US stocks from Yahoo's daily history, or when
    Yahoo refuses, Nasdaq's (US stocks, the Nasdaq Composite) and CoinGecko's (bitcoin);
  - the Egyptian stocks and the EGX30 from the desk's intraday file (desk/intraday.json), the session's last price;
  - pound rates and Egyptian gold on Friday and Saturday closes: the last weekday's figure, as the market is shut.
Pound rates, Egyptian gold, rates and other figures have no dated history to draw on: they are listed for a manual
check. Without --write it only prints what it would fill; with --write it logs the values through log_figures.py.
A filled value is printed beside its neighbours, so a jump that looks wrong can be checked.
"""
import datetime
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
LOG = os.path.join(ROOT, "data", "markets.json")
INTRA = os.path.join(ROOT, "desk", "intraday.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
YAHOO = {"gold_usd": "GC=F", "dxy": "DX-Y.NYB", "brent": "BZ=F", "btc": "BTC-USD", "sp500": "^GSPC", "nasdaq": "^IXIC", "dow": "^DJI"}
# set only on some days (auctions, decisions, monthly releases) or not every session: not gaps
SKIP = ("tbill_", "cbe_", "egx_turnover", "infl_", "reserves_", "egx30_vol", "vol.", "seed")


def flat(e):
    out = {}
    for k, v in e.items():
        if isinstance(v, dict):
            out.update({f"{k}.{t}": x for t, x in v.items() if isinstance(x, (int, float))})
        elif isinstance(v, (int, float)) and not isinstance(v, bool):
            out[k] = v
    return out


_cache = {}


def yahoo(sym):
    """Daily closes as {date: close} for about the last three months."""
    if sym not in _cache:
        err = None
        for attempt, host in enumerate(("query1", "query2", "query1", "query2")):
            try:
                u = f"https://{host}.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=3mo&interval=1d"
                j = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30).read())
                break
            except Exception as e:   # Yahoo refuses bursts (HTTP 429): wait and try the other host
                err = e
                time.sleep(3 * attempt + 2)
        else:
            raise err
        r = j["chart"]["result"][0]
        _cache[sym] = {datetime.datetime.fromtimestamp(t, datetime.timezone.utc).date().isoformat(): c
                       for t, c in zip(r["timestamp"], r["indicators"]["quote"][0]["close"]) if c}
    return _cache[sym]


def nasdaq(sym, cls):
    """Daily closes from Nasdaq's price history (US stocks, and the Nasdaq Composite as COMP)."""
    to = datetime.date.today()
    u = f"https://api.nasdaq.com/api/quote/{urllib.parse.quote(sym)}/historical?assetclass={cls}&fromdate={to - datetime.timedelta(days=90)}&todate={to}&limit=100"
    rows = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30).read())["data"]["tradesTable"]["rows"]
    out = {}
    for r in rows:
        m, d, y = r["date"].split("/")
        out[f"{y}-{m}-{d}"] = float(r["close"].replace("$", "").replace(",", ""))
    return out


def coingecko_btc():
    """Bitcoin's daily closes: CoinGecko's price at midnight UTC is the close of the day before."""
    u = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=90&interval=daily"
    pts = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=30).read())["prices"]
    out = {}
    for t, v in pts:
        ts = datetime.datetime.fromtimestamp(t / 1000, datetime.timezone.utc)
        if ts.hour == 0 and ts.minute == 0:
            out[(ts.date() - datetime.timedelta(days=1)).isoformat()] = v
    return out


def intraday_last():
    """{session: {ticker: last price}} for the Egyptian stocks, from the desk's week of intraday prices."""
    try:
        I = json.load(open(INTRA))
    except Exception:
        return {}
    out = {}
    for w in (I.get("week") or {}).get("egx", []):
        out[w["session"]] = {t: s[-1][1] for t, s in (w.get("series") or {}).items() if s}
    return out


def value_for(key, date, before=None):
    """The close behind an entry dated `date`: the last session strictly before it."""
    prev = (datetime.date.fromisoformat(date) - datetime.timedelta(days=1)).isoformat()
    # Egyptian pound rates and gold prices do not trade on Friday or Saturday: those entries repeat Thursday's
    if (key.endswith("_egp") or key.startswith("cbe_usd")) and datetime.date.fromisoformat(prev).weekday() in (4, 5) and before is not None:
        return before, "carried from the last weekday (the Egyptian market is shut on Friday and Saturday)"
    if key in YAHOO or key.startswith("us."):
        sym = YAHOO.get(key) or key[3:].replace(".", "-")
        tries = [(f"Yahoo {sym}", lambda: yahoo(sym))]
        if key.startswith("us."):
            tries.append((f"Nasdaq {key[3:]}", lambda: nasdaq(key[3:], "stocks")))
        if key == "nasdaq":
            tries.append(("Nasdaq COMP", lambda: nasdaq("COMP", "index")))
        if key == "btc":
            tries.append(("CoinGecko", coingecko_btc))
        errs = []
        for name, fn in tries:
            try:
                hist = fn()
            except Exception as e:
                errs.append(f"{name}: {e}")
                continue
            days = [d for d in hist if d <= prev]
            if days:
                return round(hist[max(days)], 4), f"{name} {max(days)}"
        return None, "; ".join(errs) or None
    if key.startswith("egx.") or key == "egx30":
        t = "EGX30" if key == "egx30" else key[4:]
        il = intraday_last()
        sess = [s for s in il if s <= prev and t in il[s]]
        if sess:
            s = max(sess)
            # only a session the log's neighbours would also point to: no older than four days
            if (datetime.date.fromisoformat(prev) - datetime.date.fromisoformat(s)).days <= 4:
                return il[s][t], f"desk intraday {s} last print"
    return None, None


def main(args):
    write = "--write" in args
    args = [a for a in args if a != "--write"]
    end = args[0] if args else datetime.date.today().isoformat()
    n = int(args[1]) if len(args) > 1 else 10
    days = [d for d in json.load(open(LOG))["days"] if d["date"] <= end]
    window = days[-n:]
    fills, manual = {}, []
    for i, e in enumerate(window):
        j = days.index(e)
        before = flat(days[j - 1]) if j else {}
        after = flat(days[j + 1]) if j + 1 < len(days) else {}
        cur = flat(e)
        # a gap: the entry before has the figure, and so does the one after (or this is the newest entry)
        for k in sorted(set(before) - set(cur)):
            if k.startswith(SKIP) or (j + 1 < len(days) and k not in after):
                continue
            try:
                v, src = value_for(k, e["date"], before[k])
            except Exception as ex:
                v, src = None, f"failed: {ex}"
            if v is None:
                manual.append(f"{e['date']}: {k} missing ({src or 'no dated source'}; before {before[k]}, after {after.get(k, '—')})")
                continue
            fills.setdefault(e["date"], []).append(f"{k}={v}")
            flag = ""
            for nb in (before.get(k), after.get(k)):
                if nb and abs(v / nb - 1) > 0.08:
                    flag = "  <- more than 8% from a neighbour: check before trusting"
            print(f"{e['date']}: {k} = {v} from {src} (before {before[k]}, after {after.get(k, '—')}){flag}")
    for m in manual:
        print("MANUAL " + m)
    if not fills and not manual:
        print("No gaps in the last", n, "entries.")
    if write and fills:
        for d, kv in sorted(fills.items()):
            subprocess.run([sys.executable, os.path.join(HERE, "log_figures.py"), d, *kv], check=True)
    elif fills:
        print("Dry run: add --write to log these.")


if __name__ == "__main__":
    main(sys.argv[1:])
