"""Polygon (api.polygon.io), the US backup source: bars for stocks and funds, shared by fetch_intraday.py,
fetch_figures.py and check_edition.py.

The API key is added to each request by the session's network proxy (a network secret on the environment), so it
is never stored in the repo or read here. The free plan allows five requests a minute: calls in one process wait
their turn. It has stocks and funds but not the indexes; the S&P 500, the Nasdaq Composite and the Dow are drawn
from the funds that track them (FUNDS), scaled by the caller to the index's close.
"""
import datetime
import json
import time
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
FUNDS = {"COMP": "ONEQ", "nasdaq": "ONEQ", "sp500": "SPY", "dow": "DIA"}
GAP = 12.5   # seconds between calls: five a minute
_last = [0.0]


def bars(sym, mult, span, frm, to):
    """Bars for a ticker: [{t (ms, UTC), o, h, l, c, v}, ...] from frm to to (dates, inclusive)."""
    wait = _last[0] + GAP - time.time()
    if wait > 0:
        time.sleep(wait)
    _last[0] = time.time()
    url = (f"https://api.polygon.io/v2/aggs/ticker/{urllib.parse.quote(sym)}/range/{mult}/{span}/{frm}/{to}"
           f"?adjusted=true&sort=asc&limit=50000")
    r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read())
    if r.get("status") not in ("OK", "DELAYED") or not r.get("results"):
        raise RuntimeError("Polygon: " + str(r.get("message") or r.get("status") or "no data"))
    return r["results"]


def daily(sym, days=10):
    """The last few daily closes: {date (New York): close}."""
    from zoneinfo import ZoneInfo
    end = datetime.date.today()
    out = {}
    for b in bars(sym, 1, "day", (end - datetime.timedelta(days=days)).isoformat(), end.isoformat()):
        out[datetime.datetime.fromtimestamp(b["t"] / 1000, datetime.timezone.utc).astimezone(ZoneInfo("America/New_York")).date().isoformat()] = b["c"]
    return out
