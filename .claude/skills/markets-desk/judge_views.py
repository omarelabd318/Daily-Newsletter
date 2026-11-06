#!/usr/bin/env python3
"""Judge the desk's views (desk/views.json) against the data log, every morning.

Usage:
  python3 .claude/skills/markets-desk/judge_views.py [--write]

For every open entry ("open" or "on track"):
  - wrongIf: a list of tests, each {"key": "brent", "op": "<", "level": 100} (keys as in data/markets.json: brent,
    usd_egp, cbe_usd_sell, egx30, egx.COMI, us.AAPL ...). A close after the view opened that meets any test makes the
    view wrong at once. Add "intraday": true to a test on an Egyptian or US stock or the EGX30 to also count prices
    inside the session (the desk's intraday file), for wording such as "trades below".
  - on its due date (once the log has the due date's close) it is judged from its track:
      projection with target [lo, hi] and side bull: right if the close is at or above lo; bear: at or below hi;
      view with good up or down: right if the close moved that way from start;
      view with vs and good lead or lag: right if it beat (lead) or trailed (lag) the vs series over the period;
      view with basket and vsBasket (lists of keys): the same, on each basket's average change.
  - otherwise its status is kept current: "on track" when the figures are going its way, "open" when not.
Judged entries ("right", "wrong", "closed") are never touched. Each verdict gets a result line with the figures.

It also warns about views that cannot mean much:
  - a wrongIf level closer to the start than 1.5 times the series' usual daily move (20 sessions): one ordinary day
    could decide it;
  - more than two open entries resting on the same driver (the "driver" field, e.g. "oil"): one move would judge
    them all together;
  - a view and a projection on the same stock opened the same day pointing the same way: one call counted twice.
Without --write it prints what it would change; with --write it saves desk/views.json.
"""
import datetime
import json
import os
import statistics
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VIEWS = os.path.join(ROOT, "desk", "views.json")
LOG = os.path.join(ROOT, "data", "markets.json")
INTRA = os.path.join(ROOT, "desk", "intraday.json")
OPS = {"<": lambda a, b: a < b, ">": lambda a, b: a > b, "<=": lambda a, b: a <= b, ">=": lambda a, b: a >= b}


def get(e, k):
    if "." in k:
        a, b = k.split(".", 1)
        return (e.get(a) or {}).get(b)
    v = e.get(k)
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def session_of(entry_date, key):
    """The session an entry's close belongs to: the last trading day before the entry's date."""
    d = datetime.date.fromisoformat(entry_date) - datetime.timedelta(days=1)
    egypt = key.startswith(("egx", "cbe_")) or key.endswith("_egp")
    while (egypt and d.weekday() in (4, 5)) or (not egypt and key != "btc" and d.weekday() in (5, 6)):
        d -= datetime.timedelta(days=1)
    return d


def fmt(v):
    t = f"{v:,.2f}" if abs(v) < 100000 else f"{v:,.0f}"
    return t[:-3] if t.endswith(".00") else t


NAMES = {"brent": "Brent", "gold_usd": "Gold", "dxy": "The dollar index", "btc": "Bitcoin", "usd_egp": "The dollar (USD/EGP)",
         "cbe_usd_sell": "The central bank's dollar rate", "egx30": "The EGX30", "egx70": "The EGX70 EWI", "sp500": "The S&P 500",
         "nasdaq": "The Nasdaq", "dow": "The Dow"}


def name(v, k):
    tr = v.get("track") or {}
    return tr.get("label") if tr.get("key") == k and tr.get("label") else NAMES.get(k, k.split(".", 1)[-1])


def day(d):
    return f"{d:%B} {d.day}"


def series(days, key, after):
    """[(entry date, value)] for entries after `after`, dropping weekend repeats of the same close."""
    out, last = [], None
    for e in days:
        if e["date"] <= after:
            continue
        v = get(e, key)
        if v is None:
            continue
        s = session_of(e["date"], key)
        if last and s == last:
            continue
        out.append((e["date"], v))
        last = s
    return out


def intraday_extremes(key):
    """{session: (low, high)} from the desk's intraday file, for an Egyptian or US stock or the EGX30."""
    try:
        I = json.load(open(INTRA))
    except Exception:
        return {}
    mk = "egx" if key.startswith("egx") else "us"
    t = "EGX30" if key == "egx30" else key.split(".", 1)[-1]
    out = {}
    for w in (I.get("week") or {}).get(mk, []):
        s = (w.get("series") or {}).get(t) or []
        if s:
            vals = [x[1] for x in s]
            out[w["session"]] = (min(vals), max(vals))
    return out


def daily_move(days, key):
    vals = [get(e, key) for e in days[-40:] if get(e, key) is not None]
    moves = [abs(b / a - 1) for a, b in zip(vals, vals[1:]) if a and b != a]
    return statistics.mean(moves[-20:]) if len(moves) >= 5 else None


def chg(days, key, start, upto):
    s = [v for d, v in series(days, key, "0000") if d <= upto]
    return (s[-1] / start - 1) * 100 if s and start else None


def going_its_way(v, days, upto):
    tr = v.get("track") or {}
    k, st = tr.get("key"), tr.get("start")
    s = [x for d, x in series(days, k, "0000") if d <= upto] if k else []
    if not s or not st:
        return None, None
    now = s[-1]
    if tr.get("target"):
        lo, hi = tr["target"]
        ok = now >= lo if tr.get("side") == "bull" else now <= hi
        return ok, f"{tr.get('label', k)} closed at {fmt(now)} against the {fmt(lo)}–{fmt(hi)} range"
    if tr.get("basket"):   # several stocks against several: {"basket": [...], "vsBasket": [...]}, each from its close at the start
        def avg(keys):
            cs = []
            for kk in keys:
                s0 = next((get(e, kk) for e in reversed(days) if e["date"] <= v["opened"] and get(e, kk) is not None), None)
                c = chg(days, kk, s0, upto)
                if c is not None:
                    cs.append(c)
            return sum(cs) / len(cs) if len(cs) == len(keys) else None
        a, b = avg(tr["basket"]), avg(tr["vsBasket"])
        if a is None or b is None:
            return None, None
        ok = a > b if tr.get("good") == "lead" else a < b
        return ok, f"{tr.get('label', 'the basket')} {a:+.1f}% on average against {tr.get('vsLabel', 'the other')} {b:+.1f}% since {v['opened']}"
    if tr.get("vs"):
        a, b = chg(days, k, st, upto), chg(days, tr["vs"], tr.get("vsStart"), upto)
        if a is None or b is None:
            return None, None
        ok = a > b if tr.get("good") == "lead" else a < b
        return ok, f"{tr.get('label', k)} {a:+.1f}% against {tr.get('vsLabel', tr['vs'])} {b:+.1f}% since {v['opened']}"
    if tr.get("good") in ("up", "down"):
        ok = now > st if tr["good"] == "up" else now < st
        return ok, f"{tr.get('label', k)} at {fmt(now)} from {fmt(st)} ({(now / st - 1) * 100:+.1f}%)"
    return None, None


def main(args):
    write = "--write" in args
    D = json.load(open(VIEWS))
    days = json.load(open(LOG))["days"]
    last_entry = days[-1]["date"]
    changes, warns = [], []
    for v in D["views"]:
        if v.get("status") not in ("open", "on track"):
            continue
        tr = v.get("track") or {}
        # 1. a wrong-if test met by a close (or a price inside the session) since the view opened
        hit = None
        for t in v.get("wrongIf") or []:
            k, op, lvl = t["key"], t["op"], t["level"]
            for d, x in series(days, k, v["opened"]):
                if v.get("due") and session_of(d, k).isoformat() > v["due"]:
                    break
                if OPS[op](x, lvl):
                    hit = (session_of(d, k), f"{name(v, k)} closed at {fmt(x)} on {day(session_of(d, k))}, "
                           f"{'below' if '<' in op else 'above'} the {fmt(lvl)} that makes the call wrong")
                    break
            if not hit and t.get("intraday"):
                for sess, (lo, hi) in sorted(intraday_extremes(k).items()):
                    if sess < v["opened"] or (v.get("due") and sess > v["due"]):
                        continue
                    x = lo if "<" in op else hi
                    if OPS[op](x, lvl):
                        hit = (datetime.date.fromisoformat(sess), f"{name(v, k)} traded at {fmt(x)} on {day(datetime.date.fromisoformat(sess))} "
                               f"(the desk's intraday prices), {'below' if '<' in op else 'above'} the {fmt(lvl)} that makes the call wrong")
                        break
            if hit:
                break
        if hit:
            changes.append((v, "wrong", {"date": last_entry, "text": hit[1] + "."}))
            continue
        # 2. the due date has passed and its close is in the log: judge from the track
        if v.get("due") and any(session_of(e["date"], tr.get("key") or "x").isoformat() >= v["due"] for e in days[-3:]):
            ok, why = going_its_way(v, days, last_entry)
            if ok is None:
                warns.append(f"{v['id']}: due {v['due']} but its track cannot decide it: judge it by hand.")
            else:
                changes.append((v, "right" if ok else "wrong", {"date": last_entry, "text": f"Judged on its date: {why}."}))
            continue
        # 3. still open: keep the status current
        ok, _ = going_its_way(v, days, last_entry)
        if ok is not None:
            new = "on track" if ok else "open"
            if new != v["status"]:
                changes.append((v, new, None))

    # warnings about views that cannot mean much
    opn = [v for v in D["views"] if v.get("status") in ("open", "on track")]
    for v in opn:
        if not v.get("wrongIf") and not (v.get("track") or {}).get("vs"):
            warns.append(f"{v['id']}: no wrongIf test, so it cannot be judged wrong automatically: add one.")
        for t in v.get("wrongIf") or []:
            st = (v.get("track") or {}).get("start") if (v.get("track") or {}).get("key") == t["key"] else None
            if st is None:
                st = next((get(e, t["key"]) for e in reversed(days) if e["date"] <= v["opened"] and get(e, t["key"]) is not None), None)
            dm = daily_move(days, t["key"])
            if st and dm and abs(t["level"] / st - 1) < 1.5 * dm:
                warns.append(f"{v['id']}: wrong if {t['key']} {t['op']} {t['level']} is {abs(t['level'] / st - 1) * 100:.1f}% from the start, "
                             f"inside 1.5 times its usual daily move ({dm * 100:.1f}%): one ordinary day could decide it.")
    drivers = {}
    for v in opn:
        if v.get("driver"):
            drivers.setdefault(v["driver"], []).append(v["id"])
    for dr, ids in drivers.items():
        if len(ids) > 2:
            warns.append(f"{len(ids)} open entries rest on the driver '{dr}' ({', '.join(ids)}): one move would judge them together.")
    for a in opn:
        for b in opn:
            ta, tb = a.get("track") or {}, b.get("track") or {}
            if a["id"] < b["id"] and a["opened"] == b["opened"] and ta.get("key") and ta.get("key") == tb.get("key") and a["kind"] != b["kind"]:
                side = lambda t: t.get("side") or {"up": "bull", "down": "bear"}.get(t.get("good"))
                if side(ta) and side(ta) == side(tb):
                    warns.append(f"{a['id']} and {b['id']}: the same call on {ta['key']} as a view and a projection; keep one.")

    for v, status, result in changes:
        print(f"{v['id']}: {v['status']} -> {status}" + (f"  ({result['text']})" if result else ""))
        if write:
            v["status"] = status
            if result:
                v["result"] = result
    for w in warns:
        print("WARNING " + w)
    if not changes and not warns:
        print("Views: nothing to change.")
    if write and changes:
        with open(VIEWS, "w") as f:
            json.dump(D, f, indent=1, ensure_ascii=False)
            f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1:])
