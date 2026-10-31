#!/usr/bin/env python3
"""Check the Markets Desk files before publishing: the newest day in desk/index.json, desk/stocks.json and
desk/flows.json. Prints ERROR lines (fix before committing; a broken file blanks the pages) and WARNING lines.

Usage:
  python3 .claude/skills/markets-desk/check_desk.py [DATE]

DATE defaults to the newest desk in desk/index.json.
"""
import json
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
TICKERS = {"egx": ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL"],
           "us": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST"]}
ALL = set(TICKERS["egx"]) | set(TICKERS["us"])
LEVELS = {"high", "medium", "low"}
errors, warnings = [], []


def load(rel):
    try:
        with open(os.path.join(ROOT, rel)) as f:
            return json.load(f)
    except FileNotFoundError:
        errors.append(f"{rel} is missing.")
    except json.JSONDecodeError as e:
        errors.append(f"{rel} is not valid JSON: {e}")
    return None


def need(obj, keys, where):
    for k in keys:
        if not isinstance(obj, dict) or obj.get(k) in (None, "", []):
            errors.append(f"{where}: missing {k}.")


def level(v, where):
    if v not in LEVELS:
        errors.append(f"{where}: confidence must be high, medium or low, not {v!r}.")


def texts(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from texts(v)
    elif isinstance(o, list):
        for v in o:
            yield from texts(v)
    elif isinstance(o, str):
        yield o


def last_close(log, t):
    group = "egx" if t in TICKERS["egx"] else "us"
    for d in reversed(log.get("days", [])):
        v = (d.get(group) or {}).get(t)
        if isinstance(v, (int, float)):
            return v
    return None


def main(args):
    idx = load("desk/index.json")
    if not idx:
        return
    dates = sorted(d["date"] for d in idx.get("desks", []))
    date = args[0] if args else (dates[-1] if dates else None)
    if not date or date not in dates:
        errors.append(f"desk/index.json has no entry for {date}.")
        return
    D = load(f"desk/days/{date}.json")
    log = load("data/markets-recent.json") or {}
    if not D:
        return
    need(D, ["date", "asOf"], date)
    if D.get("sample"):
        warnings.append(f"{date} is marked sample: remove \"sample\": true from a real desk.")

    for key, name in (("egypt", "Egypt"), ("global", "USA")):
        X = D.get(key) or {}
        need(X, ["finding", "close", "calls", "board", "week", "views"], name)
        calls = X.get("calls") or []
        if not 1 <= len(calls) <= 3:
            errors.append(f"{name}: one to three stories in calls, not {len(calls)}.")
        for i, c in enumerate(calls):
            need(c, ["headline", "body", "view", "moves", "wrong", "confidence"], f"{name} story {i + 1}")
            level(c.get("confidence"), f"{name} story {i + 1}")
        for side in ("helped", "hurt"):
            for r in (X.get("board") or {}).get(side, []):
                need(r, ["name", "why", "confidence"], f"{name} board")
                level(r.get("confidence"), f"{name} board, {r.get('name')}")
        for w in X.get("week") or []:
            if w.get("impact") not in LEVELS:
                errors.append(f"{name} week ahead: impact must be high, medium or low ({w.get('event')}).")
        F = X.get("flows")
        if F:
            net = sum(r.get("net", 0) for r in F.get("rows", []))
            if abs(net) > 0.5:
                warnings.append(f"{name} flows net to {net:+.2f}bn, not about zero: check the six figures.")

    P = D.get("pages") or {}
    for page in ("egx", "egp", "us", "global"):
        X = P.get(page)
        if not X:
            errors.append(f"pages.{page} is missing.")
            continue
        need(X, ["finding"], f"pages.{page}")
        news = X.get("news") or []
        if not news:
            warnings.append(f"pages.{page}: no news today. Fine if there was none; otherwise add the day's stories.")
        for n in news:
            need(n, ["headline", "text", "source", "url"], f"pages.{page} news")
            if n.get("url") and not str(n["url"]).startswith("http"):
                errors.append(f"pages.{page} news: link is not a URL ({n.get('headline')}).")
            for t in n.get("tickers", []):
                if t not in ALL:
                    errors.append(f"pages.{page} news: unknown ticker {t}.")
            if n.get("impact") not in (None, "bullish", "bearish", "mixed"):
                errors.append(f"pages.{page} news: impact must be bullish, bearish or mixed ({n.get('headline')}).")
        O = X.get("outlook")
        if page in ("egx", "us"):
            if not O:
                errors.append(f"pages.{page}: missing outlook (Bullish and bearish).")
                continue
            for side in ("bull", "bear"):
                for r in (O.get(side) or {}).get("sectors", []):
                    need(r, ["name", "why", "confidence"], f"{page} {side} sector")
                    level(r.get("confidence"), f"{page} {side} sector {r.get('name')}")
                for r in (O.get(side) or {}).get("stocks", []):
                    where = f"{page} {side} {r.get('t')}"
                    need(r, ["t", "range", "by", "why", "wrong", "confidence"], where)
                    level(r.get("confidence"), where)
                    if r.get("t") not in TICKERS[page if page == "us" else "egx"]:
                        errors.append(f"{where}: not one of the page's 12 stocks.")
                        continue
                    rg = r.get("range") or []
                    if len(rg) != 2 or not all(isinstance(v, (int, float)) for v in rg) or rg[0] >= rg[1]:
                        errors.append(f"{where}: range must be two numbers, low then high.")
                        continue
                    v = last_close(log, r["t"])
                    if v:
                        mid = (rg[0] + rg[1]) / 2 / v - 1
                        if (side == "bull" and mid <= 0) or (side == "bear" and mid >= 0):
                            errors.append(f"{where}: the range sits on the wrong side of the last close ({v}).")
                        if abs(mid) > 0.4:
                            warnings.append(f"{where}: the range is {mid:+.0%} from the last close; check it is grounded.")

    S = load("desk/stocks.json") or {}
    for t, e in (S.get("stocks") or {}).items():
        if t not in ALL:
            errors.append(f"desk/stocks.json: unknown ticker {t}.")
        for n in e.get("news", []):
            need(n, ["date", "text", "source"], f"stocks.json {t} news")
            if not n.get("url") and not n.get("edition"):
                errors.append(f"stocks.json {t} news: needs a url or an edition ({n.get('text', '')[:50]}).")
        dates_ = [n.get("date", "") for n in e.get("news", [])]
        if dates_ != sorted(dates_, reverse=True):
            warnings.append(f"stocks.json {t}: news is not newest first.")
    load("desk/flows.json")
    RS = load("desk/reserves.json") or {}
    months = [r.get("month", "") for r in RS.get("months", [])]
    if months != sorted(months):
        errors.append("desk/reserves.json: months must be oldest first.")
    for r in RS.get("months", []):
        need(r, ["month", "total", "fx", "gold", "sdr", "source", "url"], f"reserves.json {r.get('month')}")
        parts = sum(r.get(k) or 0 for k in ("fx", "gold", "sdr"))
        if r.get("total") and abs(parts - r["total"]) > 0.05:
            errors.append(f"reserves.json {r.get('month')}: the parts add to {parts:.3f}, not the total {r['total']}.")
    logged = [v for v in (d.get("reserves_usd") for d in log.get("days", [])) if v]
    if logged and months and abs(logged[-1] - RS["months"][-1]["total"]) > 0.05:
        warnings.append(f"desk/reserves.json ends at {months[-1]} ({RS['months'][-1]['total']}bn) but the log has {logged[-1]}bn: add the new month.")
    VL = load("desk/views.json") or {}
    ids = set()
    for v in VL.get("views", []):
        where = f"views.json {v.get('id')}"
        need(v, ["id", "opened", "market", "kind", "title", "detail", "wrong", "confidence", "status"], where)
        level(v.get("confidence"), where)
        if v.get("id") in ids:
            errors.append(f"{where}: the id is used twice.")
        ids.add(v.get("id"))
        if v.get("status") not in ("open", "on track", "right", "wrong", "closed"):
            errors.append(f"{where}: status must be open, on track, right, wrong or closed.")
        if v.get("status") in ("right", "wrong", "closed") and not (v.get("result") or {}).get("text"):
            errors.append(f"{where}: a judged view needs a result (date and text).")
        if v.get("due") and v["due"] < D["date"] and v.get("status") in ("open", "on track"):
            warnings.append(f"{where}: its date ({v['due']}) has passed; judge it right or wrong.")
        for t in v.get("tickers", []):
            if t not in ALL:
                errors.append(f"{where}: unknown ticker {t}.")
        for x in v.get("updates", []):
            need(x, ["date", "text", "source", "effect"], f"{where} update")
            if x.get("effect") not in ("supports", "against", "neutral"):
                errors.append(f"{where} update: effect must be supports, against or neutral.")

    for s in list(texts(D)) + list(texts(S)):
        if re.search(r"\byour (stocks?|names|egyptian|us)\b", s, re.I):
            errors.append(f"Says \"your\": {s[:70]}")
            break


if __name__ == "__main__":
    main(sys.argv[1:])
    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARNING:", w)
    if not errors and not warnings:
        print("Desk OK")
    sys.exit(1 if errors else 0)
