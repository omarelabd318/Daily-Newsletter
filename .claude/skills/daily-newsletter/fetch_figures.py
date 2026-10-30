#!/usr/bin/env python3
"""Fetch the day's market figures in one go, for Stocks Watch, Currency and Commodities Watch and the log.

Usage:
  python3 .claude/skills/daily-newsletter/fetch_figures.py DATE [egx.TICKER ...] [us.TICKER ...]

Add notable movers after DATE, for example `egx.MCQE us.ORCL`: they are fetched and shown with their
close and change (and YTD for US stocks) but not put in the log command.

DATE is the edition date (Cairo). For every figure it prints the value, the change, whether it is a
closing or a live price, the time of the quote and the source. Anything it cannot get is listed as
NOT FOUND with the reason. It ends with a ready-to-run log_figures.py command holding closing prices only
(while the EGX is trading, each Egyptian stock's and the EGX30's previous close).

Sources: Mubasher for the EGX (the official close is the previous close plus the day's change; the
"last price" on the page can be an earlier trade), egypt.gold-price-today.com for 21K gold, open.er-api.com
for exchange rates (market mid-rates, not the central bank's rate), Yahoo Finance for US stocks, indices,
Brent, gold and Bitcoin, with Nasdaq's quote feed, FRED (for the Dow) and CoinGecko as backups.
"""
import datetime
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CAIRO = ZoneInfo("Africa/Cairo")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
EGX = ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN"]
US = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT"]
# The Markets Desk follows these too; they are logged every day but are not Stocks Watch rows.
DESK_EGX = ["MFPC", "EAST", "EFIH", "EMFD", "BQDC"]
DESK_US = ["V", "ORCL", "COST"]


def get(url, tries=2, ua=UA):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code in (403, 404, 429):  # refused or rate-limited: retrying now will not help
                raise RuntimeError(f"HTTP {e.code} {e.reason}")
            last = e
        except Exception as e:
            last = e
        time.sleep(2)
    raise RuntimeError(f"{type(last).__name__}: {last}")


def number(s):
    return float(s.replace(",", "").replace("$", "").replace("%", "").strip())


def egx_open(now):
    """EGX sessions run Sunday to Thursday, about 10:00 to 14:30 Cairo, except listed holidays."""
    try:
        hols = {h["date"] for h in json.load(open(os.path.join(ROOT, "data", "holidays.json")))["days"]
                if h.get("egx_closed")}
    except (OSError, ValueError):
        hols = set()
    return now.weekday() in (6, 0, 1, 2, 3) and now.date().isoformat() not in hols \
        and datetime.time(10, 0) <= now.time() <= datetime.time(14, 45)


def mubasher(path):
    page = get(f"https://english.mubasher.info/markets/EGX/{path}")
    field = lambda cls: re.search(rf'market-summary__{cls}[^"]*">\s*([^<]+)', page)
    prev = re.search(r'Previous Close</span>\s*<span[^>]*>([^<]+)', page)
    change, pct, when = field("change number"), field("change-percentage"), field("date")
    if not (prev and change and pct):
        raise RuntimeError("page layout changed (no previous close or change)")
    prev, change = number(prev.group(1)), number(change.group(1))
    vol = re.search(r'Volume</span>\s*<span[^>]*>([\d,]+)', page)
    return {"prev": prev, "value": round(prev + change, 4), "pct": number(pct.group(1)),
            "volume": number(vol.group(1)) if vol else None,
            "when": when.group(1).replace("Last update:", "").strip().rstrip(".") if when else "time not shown"}


YAHOO_DOWN = []


def yahoo(sym):
    if YAHOO_DOWN:  # after a refusal, skip Yahoo for the rest of the run and go to the backups
        raise RuntimeError(f"Yahoo skipped ({YAHOO_DOWN[0]})")
    q = urllib.parse.quote(sym)
    errors = []
    for host in ("query1", "query2"):
        try:
            j = json.loads(get(f"https://{host}.finance.yahoo.com/v8/finance/chart/{q}?range=5d&interval=1d"))
            res = j["chart"]["result"][0]
            pts = [(t, c) for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]) if c]
            meta = res["meta"]
            reg = meta.get("currentTradingPeriod", {}).get("regular", {})
            live = reg.get("start", 0) <= time.time() <= reg.get("end", 0)
            (t, c), (_, p) = pts[-1], pts[-2]
            return {"value": round(c, 4), "prev": round(p, 4), "pct": (c / p - 1) * 100, "live": live,
                    "when": datetime.datetime.fromtimestamp(t, CAIRO).strftime("%a %d %b"), "src": "Yahoo"}
        except Exception as e:
            errors.append(str(e))
    if any("HTTP 429" in e or "HTTP 403" in e for e in errors):
        YAHOO_DOWN.append(errors[-1])
    raise RuntimeError("Yahoo: " + "; ".join(errors))


def yahoo_ytd(sym):
    """Year-to-date change from Yahoo: the latest close against the last close of the previous year."""
    if YAHOO_DOWN:
        return None
    start = int(datetime.datetime(datetime.date.today().year - 1, 12, 15).timestamp())
    try:
        res = json.loads(get(f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}"
                             f"?period1={start}&period2={int(time.time())}&interval=1d"))["chart"]["result"][0]
    except Exception:
        return None
    year = datetime.date.today().year
    pts = [(datetime.datetime.fromtimestamp(t, CAIRO).year, c)
           for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]) if c]
    base = [c for y, c in pts if y < year]
    return (pts[-1][1] / base[-1] - 1) * 100 if base and pts else None


def nasdaq(sym, cls="stocks"):
    d = json.loads(get(f"https://api.nasdaq.com/api/quote/{sym}/info?assetclass={cls}"))["data"]
    if not d:
        raise RuntimeError(f"Nasdaq has no quote for {sym}")
    p, sec = d["primaryData"], d.get("secondaryData") or {}
    # Before the open and after hours, primaryData is extended-hours trading and secondaryData holds
    # the official close ("Closed at ..."): use the close.
    if "closed" in (sec.get("lastTradeTimestamp") or "").lower():
        p, live = sec, False
    else:
        live = d.get("marketStatus", "").lower() not in ("closed", "after hours", "after-hours", "pre market", "pre-market")
    value, change = number(p["lastSalePrice"]), number(p["netChange"])
    return {"value": value, "prev": value - change, "pct": number(p["percentageChange"]), "live": live,
            "when": p.get("lastTradeTimestamp", ""), "src": "Nasdaq"}


def nasdaq_volume(sym):
    """Shares traded in the latest completed US session, from Nasdaq's daily history."""
    today = datetime.date.today()
    url = (f"https://api.nasdaq.com/api/quote/{urllib.parse.quote(sym)}/historical?assetclass=stocks"
           f"&fromdate={today - datetime.timedelta(days=10)}&todate={today}&limit=10")
    rows = json.loads(get(url))["data"]["tradesTable"]["rows"]
    return number(rows[0]["volume"]), rows[0]["date"]


def cbe_tbills():
    """The central bank's latest T-bill auction results: [(tenor, auction date, weighted average accepted yield)]."""
    page = get("https://www.cbe.org.eg/en/auctions/egp-t-bills")
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S))))
    res = text[text.find("Results"):]
    tenors = re.search(r"Tenor \(days\) ((?:\d+ )+)", res).group(1).split()
    dates = re.search(r"Auction Date ((?:\d\d/\d\d/\d{4} ?)+)", res).group(1).split()
    yields = re.findall(r"Weighted Avg\. Yield \(%\) ((?:[\d.]+ ?)+)", res)[-1].split()   # the second one is accepted bids
    out = []
    for t, d, y in zip(tenors, dates, yields):
        out.append((int(t), datetime.datetime.strptime(d, "%d/%m/%Y").date().isoformat(), float(y)))
    return out


def cbe_page(path):
    page = get(f"https://www.cbe.org.eg/en/{path}")
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S))))


def cbe_official():
    """The central bank's official exchange rates (buy, sell), policy rates and latest inflation."""
    out = {}
    text = cbe_page("economic-research/statistics/cbe-exchange-rates")
    d = re.search(r"Rates for Date: (\d\d/\d\d/\d{4})", text)
    out["fx_date"] = d.group(1) if d else ""
    for name, code in (("US Dollar", "USD"), ("Euro", "EUR"), ("Pound Sterling", "GBP"), ("Saudi Riyal", "SAR"),
                       ("Kuwaiti Dinar", "KWD"), ("UAE Dirham", "AED"), ("Qatari Riyal", "QAR")):
        m = re.search(re.escape(name) + r" ([\d.]+) ([\d.]+)", text)
        if m:
            out[code] = (float(m.group(1)), float(m.group(2)))
    text = cbe_page("economic-research/statistics/overnight-deposit-and-lending-rate")
    m = re.search(r"Effective from: (\d\d \w+ \d{4}) Overnight Deposit Rate Overnight Lending Rate ([\d.]+)% ([\d.]+)%", text)
    if m:
        out["policy"] = (m.group(1), float(m.group(2)), float(m.group(3)))
    text = cbe_page("economic-research/statistics/inflation-rates")
    m = re.search(r"Inflation for Last Month: (\w+ \d{4}).*?Headline \(m/m\) Core \(m/m\) Headline \(y/y\) Core \(y/y\).*? ([\d.]+)% ([\d.]+)% ([\d.]+)% ([\d.]+)%", text)
    if m:
        out["inflation"] = (m.group(1), float(m.group(4)), float(m.group(5)))   # month, headline y/y, core y/y
    return out


def reserves():
    """Egypt's net international reserves, latest month and the one before, $bn (the central bank publishes about
    the 7th; its own reserves page has not been updated since 2023, so this reads Trading Economics' release table)."""
    page = get("https://tradingeconomics.com/egypt/foreign-exchange-reserves")
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page, flags=re.S))))
    m = re.search(r"Foreign Exchange Reserves ([\d.]+) ([\d.]+) USD Million (\w{3} \d{4})", text)   # last, previous, month
    return m.group(3), round(float(m.group(1)) / 1000, 2), round(float(m.group(2)) / 1000, 2)


def coingecko():
    j = json.loads(get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
                       "&include_24hr_change=true"))["bitcoin"]
    return {"value": j["usd"], "prev": None, "pct": j["usd_24h_change"], "live": False,
            "when": "now (24-hour change)", "src": "CoinGecko"}


def first(*fns):
    errors = []
    for fn in fns:
        try:
            return fn()
        except Exception as e:
            errors.append(str(e))
    raise RuntimeError(" | ".join(errors))


def fred(series):
    """St. Louis Fed's daily series: the latest close, a day behind at most; prev is the close before it.
    FRED refuses browser user agents, so this one sends its own."""
    start = datetime.date.today() - datetime.timedelta(days=14)
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}"
    rows = [l.split(",") for l in get(url, ua="daily-newsletter/1.0").splitlines()[1:]]
    rows = [(d, float(v)) for d, v in rows if v not in ("", ".")]
    (pd, prev), (d, value) = rows[-2], rows[-1]
    return {"value": value, "prev": prev, "pct": (value / prev - 1) * 100, "live": False,
            "when": f"close {d}", "src": "FRED"}


def main(args):
    if not args or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args[0]):
        sys.exit(__doc__)
    date, now = args[0], datetime.datetime.now(CAIRO)
    rows, missing, log = [], [], []
    egx_live = egx_open(now)

    def add(key, label, fn, log_key=None, live=None):
        try:
            r = fn()
        except Exception as e:
            missing.append(f"{label}: {e}")
            return
        is_live = r.get("live") if live is None else live
        rows.append((label, r, is_live))
        # The log keeps closing prices only; while a market is open that means the previous close.
        val = r["prev"] if is_live else r["value"]
        if log_key and val is not None:
            log.append(f"{log_key}={round(val, 4)}")
        # Volume only for a finished session: while the EGX trades, the page shows today's partial volume.
        if log_key and log_key.startswith("egx.") and r.get("volume") and not is_live:
            log.append(f"vol.{log_key[4:]}={int(r['volume'])}")

    extras = []
    for a in args[1:]:
        m = re.fullmatch(r"(egx|us)\.([A-Z.]{2,6})", a)
        if not m:
            sys.exit(f"Not a ticker: {a} (use egx.TICKER or us.TICKER)")
        extras.append((m.group(1), m.group(2)))

    for t in EGX:
        add(t, f"EGX {t}", lambda t=t: dict(mubasher(f"stocks/{t}"), src="Mubasher"), f"egx.{t}", egx_live)
    for t in DESK_EGX:
        add(t, f"Desk only: EGX {t}", lambda t=t: dict(mubasher(f"stocks/{t}"), src="Mubasher"), f"egx.{t}", egx_live)
    add("egx30", "EGX30", lambda: dict(mubasher("indices/EGX30"), src="Mubasher"), "egx30", egx_live)
    for t in US:
        add(t, f"US {t}", lambda t=t: first(lambda: yahoo(t.replace(".", "-")), lambda: nasdaq(t)), f"us.{t}")
        try:
            v, d = nasdaq_volume(t)
            log.append(f"vol.{t}={int(v)}")
        except Exception as e:
            missing.append(f"US {t} volume: {e}")
    for t in DESK_US:
        add(t, f"Desk only: US {t}", lambda t=t: first(lambda: yahoo(t.replace(".", "-")), lambda: nasdaq(t)), f"us.{t}")
        try:
            v, d = nasdaq_volume(t)
            log.append(f"vol.{t}={int(v)}")
        except Exception as e:
            missing.append(f"US {t} volume: {e}")
    add("sp500", "S&P 500", lambda: yahoo("^GSPC"), "sp500")
    add("nasdaq", "Nasdaq", lambda: first(lambda: yahoo("^IXIC"), lambda: nasdaq("COMP", "index")), "nasdaq")
    add("dow", "Dow Jones", lambda: first(lambda: yahoo("^DJI"), lambda: fred("DJIA")), "dow")
    add("brent", "Brent ($/bbl)", lambda: yahoo("BZ=F"), "brent")
    add("gold_usd", "Gold ($/oz)", lambda: yahoo("GC=F"), "gold_usd")
    add("btc", "Bitcoin ($)", lambda: first(lambda: yahoo("BTC-USD"), coingecko), "btc")
    add("dxy", "US dollar index (DXY)", lambda: yahoo("DX-Y.NYB"), "dxy")

    for group, t in extras:
        if group == "egx":
            add(t, f"Mover EGX {t} (YTD n/a)", lambda t=t: dict(mubasher(f"stocks/{t}"), src="Mubasher"), None, egx_live)
        else:
            sym = t.replace(".", "-")
            ytd = yahoo_ytd(sym)
            label = f"Mover US {t} (YTD {'n/a' if ytd is None else f'{ytd:+.1f}%'})"
            add(t, label, lambda t=t, sym=sym: first(lambda: yahoo(sym), lambda: nasdaq(t)))

    gold_page = []

    def gold(col):
        """The page's daily table: newest row first, columns 24K, 21K, 18K, gold pound."""
        if not gold_page:
            gold_page.append(get("https://egypt.gold-price-today.com/"))
        page = gold_page[0]
        i = page.find('<th class="col-popular">')
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "|", page[i:i + 6000])) if i >= 0 else ""
        row = re.search(r"\|([^|\d]+)\| ?(\d{1,2} [^|\d]+?) ?\|[ |]*([\d,]+)\|[ |]*([\d,]+)\|[ |]*([\d,]+)\|[ |]*([\d,]+)\|", text)
        if not row:
            raise RuntimeError("daily price table not found on the page")
        return {"value": number(row.group(3 + col)), "prev": None, "pct": None, "live": False,
                "when": f"{row.group(1).strip()} {row.group(2).strip()}", "src": "gold-price-today"}
    add("gold24", "Gold 24K (EGP/g)", lambda: gold(0), "gold24_egp")
    add("gold21", "Gold 21K (EGP/g)", lambda: gold(1), "gold21_egp")
    add("gold18", "Gold 18K (EGP/g)", lambda: gold(2), "gold18_egp")
    add("goldpound", "Gold pound (EGP)", lambda: gold(3), "goldpound_egp")

    def fx():
        j = json.loads(get("https://open.er-api.com/v6/latest/USD"))
        if j.get("result") != "success":
            raise RuntimeError(j.get("error-type", "bad response"))
        return j
    try:
        j = fx()
        egp = j["rates"]["EGP"]
        for code, key in (("USD", "usd_egp"), ("EUR", "eur_egp"), ("SAR", "sar_egp"), ("AED", "aed_egp"),
                          ("KWD", "kwd_egp"), ("QAR", "qar_egp"), ("GBP", "gbp_egp")):
            v = round(egp / j["rates"][code], 4)
            rows.append((f"{code}/EGP (mid)", {"value": v, "pct": None, "when": j["time_last_update_utc"],
                                              "src": "open.er-api"}, False))
            log.append(f"{key}={v}")
    except Exception as e:
        missing.append(f"Exchange rates: {e}")

    # the central bank's official rates and inflation
    try:
        cb = cbe_official()
        for code in ("USD", "EUR", "GBP", "SAR", "KWD", "AED", "QAR"):
            if code in cb:
                b, s_ = cb[code]
                rows.append((f"{code}/EGP central bank, buy / sell", {"value": s_, "pct": None, "when": f"{cb['fx_date']} (buy {b})", "src": "Central Bank of Egypt"}, False))
        if "USD" in cb:
            log += [f"cbe_usd_buy={cb['USD'][0]}", f"cbe_usd_sell={cb['USD'][1]}"]
        if "policy" in cb:
            eff, dep, lend = cb["policy"]
            rows.append(("Overnight deposit / lending rate (%)", {"value": dep, "pct": None, "when": f"lending {lend}, effective {eff}", "src": "Central Bank of Egypt"}, False))
            log += [f"cbe_deposit={dep}", f"cbe_lending={lend}"]
        if "inflation" in cb:
            month, head, core = cb["inflation"]
            rows.append((f"Inflation, {month} (headline y/y %)", {"value": head, "pct": None, "when": f"core {core}%", "src": "Central Bank of Egypt"}, False))
            log += [f"infl_headline={head}", f"infl_core={core}"]
    except Exception as e:
        missing.append(f"Central bank rates and inflation (cbe.org.eg): {e}")

    try:
        month, last, prev = reserves()
        rows.append((f"Net international reserves, {month} ($bn)", {"value": last, "pct": (last / prev - 1) * 100, "when": f"previous month {prev}", "src": "Trading Economics (central bank figures)"}, False))
        log.append(f"reserves_usd={last}")
    except Exception as e:
        missing.append(f"Net international reserves (tradingeconomics.com/egypt/foreign-exchange-reserves): {e}")

    # T-bills: the central bank's latest auction; log a tenor only when this edition is the first after its auction
    try:
        log_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "markets.json")
        logged = {d["date"]: d for d in json.load(open(log_path))["days"]}
        for ten, adate, y in cbe_tbills():
            rows.append((f"T-bill {ten} days (auction {adate})", {"value": y, "pct": None, "when": adate, "src": "Central Bank of Egypt"}, False))
            if ten in (91, 182, 273, 364) and adate < date:
                later = [d for d in logged if adate < d < date and f"tbill_{ten}" in logged[d]]
                if not later:
                    log.append(f"tbill_{ten}={y}")
    except Exception as e:
        missing.append(f"T-bill auction results (cbe.org.eg): {e}")

    print(f"Fetched {now:%a %d %b %H:%M} Cairo for edition {date}. EGX {'OPEN (live prices)' if egx_live else 'closed'}.\n")
    print("| Figure | Value | Change | Type | Quote time | Source |\n|---|---|---|---|---|---|")
    for label, r, is_live in rows:
        pct = "n/a" if r.get("pct") is None else f"{r['pct']:+.2f}%"
        print(f"| {label} | {r['value']:,.2f} | {pct} | {'LIVE' if is_live else 'close'} | {r['when']} | {r['src']} |")
    if missing:
        print(f"\nNOT FOUND ({len(missing)}): look these up by hand using the backups in the skill's go-to sources")
        print("table, and write n/a in the edition for any that still cannot be confirmed. Never guess.")
        for m in missing:
            print(f"- {m}")
    print("\nThese are first-source figures: still check them against a second source as the skill describes.")
    print("Exchange rates are market mid-rates; use the central bank's rate in the edition when you have it,")
    print("and log the figure the edition shows. Add any figure you found by hand to the command below.\n")
    print(f"python3 .claude/skills/daily-newsletter/log_figures.py {date} " + " ".join(log))


if __name__ == "__main__":
    main(sys.argv[1:])
