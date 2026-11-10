"""TradingView's chart feed: a symbol's recent bars, for series no other free source publishes through the session
(the EGX70 EWI). Shared by fetch_intraday.py.

It speaks the feed's websocket as an anonymous visitor (delayed data, no account) and needs the websocket-client
package, which it installs with pip the first time if it is missing.
"""
import datetime
import json
import random
import re
import string
import subprocess
import sys


def _ws():
    try:
        import websocket
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "websocket-client"], check=False, capture_output=True)
        import websocket
    return websocket


def _msg(f, p):
    m = json.dumps({"m": f, "p": p}, separators=(",", ":"))
    return f"~m~{len(m)}~m~{m}"


def bars(symbol, resolution="5", count=2000):
    """[(datetime in UTC, close), ...] oldest first: the last `count` bars of e.g. "EGX:EGX70EWI" every `resolution` minutes."""
    websocket = _ws()
    ws = websocket.create_connection("wss://data.tradingview.com/socket.io/websocket", header=["Origin: https://www.tradingview.com"], timeout=30)
    cs = "cs_" + "".join(random.choice(string.ascii_lowercase) for _ in range(12))
    for f, p in [("set_auth_token", ["unauthorized_user_token"]), ("chart_create_session", [cs, ""]),
                 ("resolve_symbol", [cs, "symbol_1", '={"symbol":"' + symbol + '","adjustment":"splits"}']),
                 ("create_series", [cs, "s1", "s1", "symbol_1", resolution, count])]:
        ws.send(_msg(f, p))
    raw = ""
    try:
        while True:
            r = ws.recv()
            raw += r
            if re.match(r"~m~\d+~m~~h~", r):   # the feed's heartbeat, echoed back
                ws.send(r)
            if "series_completed" in r or "symbol_error" in r or "series_error" in r:
                break
    finally:
        ws.close()
    out = []
    for s in re.findall(r'"s":\[(.*?)\],"ns"', raw):
        for b in re.findall(r'"v":\[([^\]]+)\]', s):
            v = [float(x) for x in b.split(",")]
            out.append((datetime.datetime.fromtimestamp(v[0], datetime.timezone.utc), v[4]))
    if not out:
        raise RuntimeError("TradingView: no bars for " + symbol)
    return sorted(set(out))
