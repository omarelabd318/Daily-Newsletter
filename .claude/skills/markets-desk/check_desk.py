#!/usr/bin/env python3
"""Check the Markets Desk files before publishing: the newest day in desk/index.json, desk/stocks.json and
desk/flows.json. Prints ERROR lines (fix before committing; a broken file blanks the pages) and WARNING lines.

Usage:
  python3 .claude/skills/markets-desk/check_desk.py [DATE]

DATE defaults to the newest desk in desk/index.json.
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "daily-newsletter"))
import us_english  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
TICKERS = {"egx": ["COMI", "TMGH", "ETEL", "PHDC", "SWDY", "ORAS", "FWRY", "ABUK", "HRHO", "CLHO", "JUFO", "ALCN", "MFPC", "EAST", "EFIH", "EMFD", "BQDC", "EGAL", "AMOC", "SKPC", "EFID"],
           "us": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "XOM", "AVGO", "BRK.B", "WMT", "V", "ORCL", "COST", "NFLX", "INTC", "LLY"]}
ALL = set(TICKERS["egx"]) | set(TICKERS["us"])
LEVELS = {"high", "medium", "low"}
errors, warnings = [], []


def tags(lst, where, text, lo, hi, story):
    """The Moves / Affects tags (desk/tags.js): sector first, then the stocks most exposed, then markets."""
    if not isinstance(lst, list) or not lo <= len(lst) <= hi:
        (errors if isinstance(lst, list) and lst else warnings).append(
            f"{where}: {lo} to {hi} tags in affects ({'sectors, stocks and markets' if story else 'what the story affects'}), not {len(lst) if isinstance(lst, list) else 'none'}.")
        if not isinstance(lst, list):
            return
    low = text.lower()
    for x in lst:
        k, nm, t = x.get("kind"), x.get("name") or "", x.get("t") or ""
        if k not in ("sector", "stock", "market"):
            errors.append(f"{where}: tag kind must be sector, stock or market ({nm or t}).")
        if x.get("dir") not in ("up", "down", "mixed"):
            errors.append(f"{where}: tag dir must be up, down or mixed ({nm or t}).")
        if not (nm or t in ALL):
            errors.append(f"{where}: a tag needs a name (a desk stock's ticker alone will do).")
        if not story and k == "stock" and nm and not (t and t in text.upper()) and not any(w.lower() in low for w in re.findall(r"[A-Za-z][\w&'-]{2,}", nm)[:1]):
            warnings.append(f"{where}: the tag {nm} is not named in the story: tag what the story says, not the desk's list.")
        if x.get("chg") is not None and not isinstance(x["chg"], (int, float)):
            errors.append(f"{where}: chg must be a number ({nm or t}).")
    if story and lst and not any(x.get("kind") == "sector" for x in lst):
        warnings.append(f"{where}: no sector tag: name the sector the story moves first, then the stocks.")


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
    global CHECKED
    CHECKED = date
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
        if len(str(X.get("finding", "")).split()) > 55:
            warnings.append(f"{name} finding: {len(str(X['finding']).split())} words; keep it to the day's point in one sentence and up to two more (about 50 words). The coming dates belong in the week ahead.")
        calls = X.get("calls") or []
        if not 1 <= len(calls) <= 5:
            errors.append(f"{name}: one to five stories in calls, not {len(calls)}.")
        elif len(calls) < 3:
            warnings.append(f"{name}: {len(calls)} stories; three to five on a normal day (fewer only when the day has no more).")
        for i, c in enumerate(calls):
            w = f"{name} story {i + 1}"
            need(c, ["headline", "body", "view", "affects", "wrong", "confidence"], w)
            level(c.get("confidence"), w)
            tags(c.get("affects"), w, " ".join(str(c.get(k, "")) for k in ("headline", "body", "view")), 2, 8, True)
            if len(str(c.get("headline", "")).split()) > 20:
                warnings.append(f"{w}: the headline runs to {len(c['headline'].split())} words; keep it to 20.")
            if i and not c.get("line"):
                warnings.append(f"{w}: no line: one sentence on why it matters, shown on its card under \"Also today\".")
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
        if len(str(X.get("finding", "")).split()) > 55:
            warnings.append(f"pages.{page} finding: {len(str(X['finding']).split())} words; one sentence with the point, then up to two more (about 50 words).")
        if page == "egp" and X.get("view"):
            V = X["view"]
            need(V, ["headline", "body", "affects", "wrong", "confidence"], "pages.egp view")
            tags(V.get("affects"), "pages.egp view", f"{V.get('headline', '')} {V.get('body', '')}", 2, 8, True)
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
            if n.get("impact") not in ("bullish", "bearish", "mixed"):
                (errors if n.get("impact") else warnings).append(f"pages.{page} news: impact must be bullish, bearish or mixed ({n.get('headline')}).")
            tags(n.get("affects"), f"pages.{page} news ({str(n.get('headline'))[:40]})", f"{n.get('headline', '')} {n.get('text', '')}", 1, 4, False)
            if len(str(n.get("headline", "")).split()) > 12:
                warnings.append(f"pages.{page} news: the headline runs to {len(n['headline'].split())} words; keep it to 12 ({n['headline'][:50]}).")
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
    FLW = load("desk/flows.json") or {}
    # every session's flows carry a link to each report they came from, so a reader can check them
    for fday in (FLW.get("days") or [])[-10:]:
        links = fday.get("links") or []
        if not links or not all(isinstance(x, dict) and str(x.get("url", "")).startswith("http") and x.get("source") for x in links):
            errors.append(f"desk/flows.json {fday.get('date')}: add 'links', [{{'source': ..., 'url': ...}}], one for each report the figures came from.")
    # the EGX traded in the desk's session: its flows belong in the day's file and the flow history
    if D.get("asOf") and not any(d.get("date") == D["asOf"] for d in FLW.get("days", [])):
        warnings.append(f"desk/flows.json has no entry for the {D['asOf']} session: add who bought and who sold (and egypt.flows in the day's file).")
    if not (D.get("egypt") or {}).get("flows"):
        warnings.append("egypt.flows is missing from the day's file: the EGX page shows the flow history's entry instead, if there is one.")
    # views: open entries need a price test, and nothing judge_views.py would change should be left pending
    for v in (load("desk/views.json") or {}).get("views", []):
        if v.get("status") in ("open", "on track") and not v.get("wrongIf") and not (v.get("track") or {}).get("vs") \
                and not (v.get("track") or {}).get("basket"):
            errors.append(f"views.json {v.get('id')}: no wrongIf test (see Views: the record).")
        if v.get("status") in ("open", "on track") and not v.get("driver"):
            warnings.append(f"views.json {v.get('id')}: no driver.")
    import subprocess
    jv = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "judge_views.py")],
                        capture_output=True, text=True).stdout.strip().splitlines()
    pending = [l for l in jv if "->" in l]
    if pending:
        errors.append("judge_views.py has verdicts to record: run it with --write. " + "; ".join(pending[:3]))
    warnings.extend("judge_views: " + l[8:] for l in jv if l.startswith("WARNING "))

    # research: the day's log (research_log.py, desk part), and every desk stock that moved 3% or more checked
    import research_log
    RL = research_log.load(date).get("desk")
    if not RL:
        errors.append("Research: no desk log in data/research/DATE.json. Log searches, pages and each stock checked with research_log.py.")
    else:
        T = dict(research_log.TARGETS["desk"])
        if datetime.date.fromisoformat(date[:10]).weekday() == 5 and date[:10] >= "2026-11-14":
            T = {"searches": 10, "pages": 5, "read": 10}   # Saturday's lighter run (the skill's Daily run)
        for k in ("searches", "pages", "read"):
            n = len(set(RL.get(k, [])))
            if k == "read":   # pages the scripts read (stock_news.py --read, results_due.py): a warning only
                if n < T[k]:
                    warnings.append(f"Research: the scripts read only {n} pages (usually {T[k]}+): check the news step in desk/brief.md.")
                continue
            if n < T[k] / 2:
                errors.append(f"Research: only {n} desk {k} logged (aim for {T[k]}+).")
            elif n < T[k]:
                warnings.append(f"Research: {n} desk {k} logged, below the {T[k]} a full desk usually takes.")
        LOGD = (load("data/markets-recent.json") or {}).get("days", [])
        if len(LOGD) >= 2:
            a, b = LOGD[-2], LOGD[-1]
            for grp in ("egx", "us"):
                for t, v in (b.get(grp) or {}).items():
                    pv = (a.get(grp) or {}).get(t)
                    if t in ALL and pv and isinstance(v, (int, float)) and v != pv and abs(v / pv - 1) >= 0.03 and t not in RL.get("stocks", {}):
                        warnings.append(f"Research: {t} moved {(v / pv - 1) * 100:+.1f}% but no check is logged for it (research_log.py DATE desk stock {t} ...).")

    # US English across the day's text (links and quotes aside)
    us_txt = []
    def us_walk(o, k=""):
        if isinstance(o, dict):
            for kk, v in o.items():
                if kk not in ("url", "source", "sources", "sub"):
                    us_walk(v, kk)
        elif isinstance(o, list):
            for v in o:
                us_walk(v, k)
        elif isinstance(o, str):
            us_txt.append(re.sub(r"[\"“'‘][^\"”'’]{12,}[\"”'’]", "", o))
    us_walk(D)
    found = [x for t in us_txt for x in us_english.find(t)]
    if found:
        warnings.append(f"US English: {len(found)} British spelling(s) or day-first date(s) in the day's file: "
                        + "; ".join(f"{b} → {a}" for b, a in found[:12]) + (" …" if len(found) > 12 else "") + ".")
    # every top-five mover of 5% or more needs its reason, or "No company news found." after a search
    MV = load("desk/movers.json") or {}
    for m, label in (("egx", "EGX"), ("us", "US")):
        for side in ("gainers", "losers"):
            for r in (MV.get(m) or {}).get(side, [])[:5]:
                if abs(r.get("pct") or 0) >= 5 and not r.get("why"):
                    warnings.append(f"desk/movers.json: {label} {r.get('t')} {r.get('pct', 0):+.1f}% has no reason: research it (fetch_movers.py --leads) "
                                    "and add why, source and url, or write \"No company news found.\"")
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
    # each stock's "Coming up" notes (desk/stocks.json "next"): a dated note that has passed, an undated one with no
    # "added" date or added more than ten days ago, and one that names a day relative to when it was written
    # ("Thursday's hike") all go stale on the page: date them, refresh them or remove them
    ST_ = (load("desk/stocks.json") or {}).get("stocks", {})
    old_ = (datetime.date.fromisoformat(date) - datetime.timedelta(days=10)).isoformat()
    for t, e in ST_.items():
        for n in e.get("next") or []:
            w = f"desk/stocks.json {t} next '{n.get('event')}'"
            if n.get("date") and n["date"] < date:
                warnings.append(f"{w}: its date ({n['date']}) has passed; remove it or move it to the stock's news.")
            elif not n.get("date") and not n.get("added"):
                warnings.append(f"{w}: no date; give it \"date\" when known, else \"added\": \"{date}\" so it can be checked again.")
            elif not n.get("date") and n["added"] < old_:
                warnings.append(f"{w}: undated since {n['added']}; check it is still right and refresh \"added\", or remove it.")
            if re.search(r"\b(yesterday|today|tomorrow|this week|last week|(Sun|Mon|Tues|Wednes|Thurs|Fri|Satur)day'?s?)\b", f"{n.get('why', '')}", re.I) and not n.get("date"):
                warnings.append(f"{w}: says '{re.search(r'(yesterday|today|tomorrow|this week|last week|[A-Z][a-z]+day)', n.get('why', '')).group(0)}', which goes stale; name the date instead.")
    # results days: a desk stock reporting within three days needs a "preview" (what to watch), and one whose
    # previewed date has passed needs "lastResults" for that quarter (the beat-or-miss verdict)
    CALI = (load("desk/calendar.json") or {}).get("items", [])
    soon = (datetime.date.fromisoformat(date) + datetime.timedelta(days=3)).isoformat()
    for c in CALI:
        if c.get("kind") == "results" and date <= c["date"] <= soon:
            pv = (ST_.get(c["t"]) or {}).get("preview") or {}
            if pv.get("date") != c["date"] and pv.get("period") != c.get("period"):
                warnings.append(f"{c['t']} reports {c['date']} (expected): add its \"preview\" in desk/stocks.json, the three to five things that will decide "
                                f"the reaction, with the consensus where published (earnings-preview skill; see the desk skill's Results days).")
    for t, e in ST_.items():
        pv, R = e.get("preview") or {}, e.get("lastResults") or {}
        if pv.get("date") and pv["date"] < date and not (R.get("period") and pv.get("period") and R["period"] >= pv["period"]):
            warnings.append(f"{t}: its results were due {pv['date']}; if they are out, record \"lastResults\" (verdict, headline, the points, what it means for the desk's view, source); if delayed, move the preview's date.")
        if R:
            need(R, ["date", "period", "verdict", "headline", "source"], f"stocks.json {t} lastResults")
            if R.get("verdict") not in ("beat", "miss", "in line", "mixed"):
                errors.append(f"stocks.json {t} lastResults: verdict must be beat, miss, in line or mixed.")
    # a split in the last two weeks (desk/calendar.json, from Polygon): the log's prices before it must be adjusted,
    # or the charts and changes show a fall (or jump) of the split's size
    for x in (load("desk/calendar.json") or {}).get("recentSplits", []):
        days_ = (log or {}).get("days", [])
        before = [e["us"][x["t"]] for e in days_ if e["date"] <= x["date"] and (e.get("us") or {}).get(x["t"])]
        after = [e["us"][x["t"]] for e in days_ if e["date"] > x["date"] and (e.get("us") or {}).get(x["t"])]
        if before and after and abs(before[-1] / after[0] / x["factor"] - 1) < 0.25:
            warnings.append(f"{x['t']} split {x['ratio']} on {x['date']}, and the data log's prices before it are not adjusted: "
                            f"divide them by {x['factor']:g} (data/markets.json and markets-recent.json), or every chart shows a fake move.")
    # the 1D and 1W charts: the last session saved for each market should hold every desk stock
    IN = load("desk/intraday.json") or {}
    import importlib.util
    spec = importlib.util.spec_from_file_location("fi", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch_intraday.py"))
    fi = importlib.util.module_from_spec(spec); spec.loader.exec_module(fi)
    for mk, keys in (("egx", ["EGX30"] + fi.EGX), ("us", ["COMP"] + fi.US)):
        got = (IN.get(mk) or {}).get("series", {})
        miss = [k for k in keys if k not in got]
        if got and miss:
            warnings.append(f"desk/intraday.json: the {mk.upper()} session {IN[mk].get('session')} has no one-day line for {', '.join(miss)}; run fetch_intraday.py again (it retries, then tries Yahoo).")
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
        # confidence moves with the news: an update may set a new level, one step at a time, with the news as its reason
        RANK, cur = {"low": 0, "medium": 1, "high": 2}, v.get("confidence")
        for x in sorted(v.get("updates", []), key=lambda x: x.get("date", "")):
            c = x.get("confidence")
            if c is None:
                continue
            level(c, f"{where} update {x.get('date')}")
            if c in RANK and cur in RANK:
                if c == cur:
                    errors.append(f"{where} update {x.get('date')}: confidence is already {c}; set it only when it changes.")
                elif abs(RANK[c] - RANK[cur]) > 1:
                    errors.append(f"{where} update {x.get('date')}: confidence moves one step at a time ({cur} to {c}).")
            if (v.get("result") or {}).get("date") and x.get("date", "") > v["result"]["date"]:
                errors.append(f"{where} update {x.get('date')}: confidence cannot change after the view is judged.")
            cur = c

    for s in list(texts(D)) + list(texts(S)):
        if re.search(r"\byour (stocks?|names|egyptian|us)\b", s, re.I):
            errors.append(f"Says \"your\": {s[:70]}")
            break


if __name__ == "__main__":
    main(sys.argv[1:])
    for e in errors:
        print("ERROR:", e)
    # a fair-value stock that moved beyond the EGX's 20% daily limit: a bonus issue or split the screener has not
    # adjusted for (fetch_fairvalue.py marks it); its per-share figures need checking before its fair value is trusted
    try:
        for x in json.load(open(os.path.join(ROOT, "desk", "fairvalue.json"))).get("stocks", []):
            if x.get("action"):
                warnings.append(f"Fair value {x['t']}: {x['action']} Check the company's disclosure; if the per-share figures are pre-issue, put adjusted ones in the judgement block or leave it marked low confidence.")
    except Exception:
        pass
    from us_english import report
    report([], warnings, "--all" in sys.argv)   # errors were printed above
    if not errors and not warnings:
        print("Desk OK")
    if globals().get("CHECKED"):   # the result, for the Runs page
        try:
            import research_log
            research_log.record_check(CHECKED, "desk", errors, warnings)
        except Exception:
            pass
    sys.exit(1 if errors else 0)
