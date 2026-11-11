#!/usr/bin/env python3
"""The desk's whole mechanical step in one command, and one file to read afterwards: desk/brief.md.

Usage:
  python3 .claude/skills/markets-desk/run_data.py            # every step, then the brief
  python3 .claude/skills/markets-desk/run_data.py --brief    # only rebuild the brief from the saved files
  python3 .claude/skills/markets-desk/run_data.py movers fairvalue   # only the named steps, then the brief

It runs, each as its own process with a time limit and the shared fetch layer (sources.py) underneath:
intraday, rates, valuation, movers, calendar, indicators, fairvalue, views (judge_views.py --write), news
(stock_news.py, 3 days on a Sunday) and leads (fetch_movers.py --leads). A step that fails or runs out of time
is reported and the rest carry on: every script keeps its last saved output when its source fails.

desk/brief.md is what the run reads instead of each script's output: what every step did, which sources were
flaky, what moved, which movers still need a reason, the news leads per stock, results and events coming up,
views due or just judged, what changed in the fair values, and the standing jobs that fall due today. It lists
work for the run; it is not published and nothing links to it.
"""
import datetime
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
D = lambda *p: os.path.join(ROOT, "desk", *p)
TODAY = datetime.date.today()
SUNDAY = TODAY.weekday() == 6
STEPS = [("intraday", ["fetch_intraday.py"], 420), ("rates", ["fetch_rates.py"], 120), ("valuation", ["fetch_valuation.py"], 240),
         ("movers", ["fetch_movers.py"], 300), ("calendar", ["fetch_calendar.py"], 420), ("indicators", ["indicators.py"], 60),
         ("fairvalue", ["fetch_fairvalue.py"], 120), ("views", ["judge_views.py", "--write"], 60),
         ("news", ["stock_news.py", "3" if SUNDAY else "2"], 420), ("leads", ["fetch_movers.py", "--leads"], 300)]


def load(path, default=None):
    try:
        return json.load(open(path))
    except (OSError, ValueError):
        return default


def run(name, cmd, limit):
    env = dict(os.environ, DESK_SOURCES="1", DESK_STEP=cmd[0], PYTHONPATH=os.path.join(HERE, "_site") + os.pathsep + os.environ.get("PYTHONPATH", ""))
    t = time.time()
    try:
        p = subprocess.run([sys.executable, os.path.join(HERE, cmd[0])] + cmd[1:], cwd=ROOT, env=env, capture_output=True, text=True, timeout=limit)
        out, ok = (p.stdout + ("\n" + p.stderr if p.returncode else "")).strip(), p.returncode == 0
    except subprocess.TimeoutExpired as e:
        out, ok = ((e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")) + f"\nSTOPPED after {limit}s", False
    return {"name": name, "ok": ok, "secs": round(time.time() - t), "out": out}


def old_file(rel):
    """The file as last committed, to see what this run changed."""
    try:
        return json.loads(subprocess.run(["git", "show", "HEAD:" + rel], cwd=ROOT, capture_output=True, text=True, timeout=20).stdout)
    except (ValueError, subprocess.SubprocessError):
        return None


def brief(results, started):
    L = [f"# Desk brief, {TODAY:%A, %B %-d, %Y}", "", "Built by run_data.py. Work for the run, not for publication.", ""]
    add = L.append
    days = (load(os.path.join(ROOT, "data", "markets-recent.json")) or {}).get("days", [])
    stocks = (load(D("stocks.json")) or {}).get("stocks", {})
    # 1. the steps
    if results:
        add("## Steps")
        for r in results:
            tail = [x for x in r["out"].splitlines() if x.strip()]
            add(f"- **{r['name']}**: {'ok' if r['ok'] else 'FAILED'} in {r['secs']}s. " + (tail[-1][:260] if tail and r["name"] not in ("news", "leads") else ""))
            if not r["ok"]:
                for x in tail[-6:]:
                    add(f"    {x[:200]}")
        try:
            sys.path.insert(0, HERE)
            import sources
            bad = {h: v for h, v in sources.health(started).items() if v["failed"] or v["retried"]}
            add("- **sources**: " + ("; ".join(f"{h}: {v['failed']} failed, {v['retried']} needed a retry" + (f" ({', '.join(v['scripts'])})" if v["scripts"] else "") for h, v in bad.items()) if bad else "every source answered first time") + ".")
        except Exception:
            pass
        add("")
    # 2. what moved
    def last_two(pick):
        v = [x for x in (pick(e) for e in days) if isinstance(x, (int, float))]
        if len(v) < 2:
            return None
        i = len(v) - 2
        while i > 0 and v[i] == v[-1]:
            i -= 1
        return v[-1], (v[-1] / v[i] - 1) * 100 if v[i] != v[-1] else 0.0
    add("## What moved (latest close against the one before)")
    row = []
    for k, n in [("egx30", "EGX30"), ("egx70", "EGX70 EWI"), ("usd_egp", "USD/EGP"), ("gold21_egp", "Gold 21K"), ("brent", "Brent"), ("sp500", "S&P 500"), ("nasdaq", "Nasdaq"), ("btc", "Bitcoin")]:
        x = last_two(lambda e, k=k: e.get(k))
        if x:
            row.append(f"{n} {x[0]:,.2f} ({x[1]:+.2f}%)")
    add("- " + "; ".join(row))
    big = []
    for g in ("egx", "us"):
        for t in sorted({t for e in days[-3:] for t in (e.get(g) or {})}):
            x = last_two(lambda e, g=g, t=t: (e.get(g) or {}).get(t))
            if x and abs(x[1]) >= 3:
                big.append((abs(x[1]), f"{t} {x[1]:+.1f}%"))
    add("- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): " + (", ".join(s for _, s in sorted(big, reverse=True)) or "none") + ".")
    ind = (load(D("indicators.json")) or {}).get("series", {})
    ev = [f"{k.split('.')[-1]}: {v['read']}" for k, v in ind.items() if "." in k and (v.get("goldenCross") and v["goldenCross"]["ago"] == 0 or v.get("macdCross") and v["macdCross"]["ago"] == 0 or (v.get("rsi") or 50) >= 70 or (v.get("rsi") or 50) <= 30)]
    if ev:
        add("- Trend and momentum worth a mention (description only, never a reason on its own):")
        L.extend(f"    - {x}" for x in ev[:12])
    add("")
    # 3. movers without a reason
    mv = load(D("movers.json")) or {}
    need = []
    for mk in ("egx", "us"):
        for side in ("gainers", "losers"):
            for r in (mv.get(mk, {}).get(side) or [])[:5]:
                if not r.get("why") and abs(r.get("pct") or 0) >= 5:
                    need.append(f"{mk.upper()} {r['t']} ({r.get('name', '')}) {r['pct']:+.1f}%")
    add("## Movers that still need a reason (top five each way, 5% or more)")
    add("- " + ("; ".join(need) if need else "None: every one has a reason or is under 5%.") )
    leads = next((r["out"] for r in results if r["name"] == "leads"), "")
    if leads.strip():
        add("")
        add("Leads for them (open before using; never guess a reason):")
        add("```")
        L.extend(x[:230] for x in leads.splitlines()[:90])
        add("```")
    add("")
    # 4. results and events
    cal = (load(D("calendar.json")) or {}).get("items", [])
    soon = [c for c in cal if c.get("date") and 0 <= (datetime.date.fromisoformat(c["date"]) - TODAY).days <= 7]
    add("## Coming up (seven days)")
    for c in sorted(soon, key=lambda c: c["date"]):
        days_to = (datetime.date.fromisoformat(c["date"]) - TODAY).days
        flag = ""
        if c.get("kind") == "results" and days_to <= 3 and not (stocks.get(c["t"]) or {}).get("preview"):
            flag = "  <- write its preview"
        add(f"- {c['date']} {c['t']} {c.get('kind')}{' (expected)' if c.get('expected') else ''}{flag}")
    if not soon:
        add("- Nothing dated in the calendar.")
    add("")
    # 5. views
    views = (load(D("views.json")) or {}).get("views", [])
    add("## Views")
    for v in views:
        if v["status"] in ("open", "on track") and v.get("due") and (datetime.date.fromisoformat(v["due"]) - TODAY).days <= 7:
            add(f"- due {v['due']}: {v['title']} ({v['status']})")
        if v["status"] in ("right", "wrong", "closed") and not v.get("lesson"):
            add(f"- judged {v['status']} with no lesson yet: {v['title']}  <- write its `lesson`")
    j = next((r["out"] for r in results if r["name"] == "views"), "")
    if j.strip():
        L.extend(f"    {x[:220]}" for x in j.splitlines()[-8:])
    add("")
    # 6. fair value: what this run changed
    fv, was = load(D("fairvalue.json")) or {}, old_file("desk/fairvalue.json") or {}
    add("## Fair value")
    prev = {x["t"]: x for x in was.get("stocks", [])}
    ch = []
    for x in fv.get("stocks", []):
        o = prev.get(x["t"])
        if o and o.get("upside") is not None and (abs(x["upside"] - o["upside"]) >= 10 or x["confidence"] != o["confidence"]):
            ch.append(f"{x['t']} {o['upside']:+.0f}% -> {x['upside']:+.0f}% ({o['confidence']} -> {x['confidence']})")
        elif not o:
            ch.append(f"{x['t']} new at {x['upside']:+.0f}%")
    gone = [t for t in prev if t not in {x['t'] for x in fv.get('stocks', [])}]
    add("- Changed since the last run: " + ("; ".join(ch[:20]) or "nothing by 10 points or more") + (f". Dropped out: {', '.join(gone)}" if gone else "") + ".")
    odd = [f"{x['t']} (P/E {x['pe']}, {x['upside']:+.0f}%)" for x in fv.get("stocks", []) if x["pe"] < 3 or x["upside"] > 80]
    if odd:
        add("- Figures to check before trusting (a P/E under 3 or upside above 80%): " + ", ".join(odd) + ".")
    J = fv.get("judgement", {})
    stale = [t for t, v in J.items() if v.get("noted") and (TODAY - datetime.date.fromisoformat(v["noted"])).days > 31]
    firm = [x for x in fv.get("stocks", []) if x["confidence"] != "low"]
    edge = [x["t"] for x in firm[:10] + firm[-10:] if not J.get(x["t"], {}).get("note")]
    if stale:
        add("- Notes more than a month old: " + ", ".join(stale) + ".")
    if edge:
        add("- In the ten cheapest or dearest with no note: " + ", ".join(edge) + ".")
    add("")
    # 7. standing jobs
    add("## Due today")
    nobrief = [t for t, x in stocks.items() if not x.get("brief")]
    old = [t for t, x in stocks.items() if x.get("brief") and (TODAY - datetime.date.fromisoformat(x["brief"]["written"])).days > 92]
    if SUNDAY:
        add(f"- Sunday: write the desk's note for two more stocks ({len(nobrief)} still without one; next: {', '.join(nobrief[:2]) or 'none'}), and read the whole fair-value table for figures that cannot be right.")
        if TODAY.day <= 7:
            add("- First Sunday of the month: review desk/sectors.json.")
    if old:
        add("- Stock notes more than three months old: " + ", ".join(old) + ".")
    if not SUNDAY and not old:
        add("- Nothing beyond the daily steps.")
    add("")
    # 8. news leads
    news = next((r["out"] for r in results if r["name"] == "news"), "")
    if news.strip():
        add("## News leads by stock (stock_news.py)")
        L.extend(x[:230] for x in news.splitlines())
    open(D("brief.md"), "w").write("\n".join(L) + "\n")
    return len(L)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    started, results = time.time(), []
    if "--brief" not in sys.argv:
        for name, cmd, limit in STEPS:
            if args and name not in args:
                continue
            r = run(name, cmd, limit)
            results.append(r)
            print(f"{name}: {'ok' if r['ok'] else 'FAILED'} ({r['secs']}s)", flush=True)
    n = brief(results, started)
    bad = [r["name"] for r in results if not r["ok"]]
    print(f"run_data: {len(results) - len(bad)} of {len(results)} steps ok" + (f"; failed: {', '.join(bad)}" if bad else "") + f"; read desk/brief.md ({n} lines)")


if __name__ == "__main__":
    main()
