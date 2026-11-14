#!/usr/bin/env python3
"""News research in a few hundred words a query: search the news feeds, read the top pages, print only what matters.

Usage (from the repo root):
  python3 .claude/skills/daily-newsletter/search.py [--log DATE newsletter|desk] [--days N] [--ar] [--pages N] "query" ["query" ...]

For each query it searches Google News (the free RSS feed, as the desk's stock_news.py does; an Arabic query, or
--ar, searches the Arabic edition for Egypt), resolves Google's links to the outlets' own pages, reads the top pages
(--pages, default 4) all at once with articles.py, and prints for each: outlet, date, the link, and an excerpt of
about 80 words (the opening and the sentences with figures, keeping what each figure is measured on). Pages with the
same wording are marked as one source; pages that would not load are listed, to open by hand if they matter; a few
more headlines are listed under "Also". About 500 words a query, against 2,000 to 5,000 for a web search and the
pages it leads to. All queries run at once: send several per call.

--days N limits the search to the last N days (default 2). --log records each query as a search and each page whose
excerpt was printed as read (research_log.py, one call for the batch), so the research floors count them. The
excerpt is the outlet's own words: confirm a figure that moves a story at a second, independent outlet as always,
and open the page (articles.py --full, or a web fetch) when the excerpt is not enough.
"""
import concurrent.futures
import datetime
import os
import re
import subprocess
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, ".claude", "skills", "markets-desk"))
import articles      # noqa: E402
import stock_news    # noqa: E402

ARABIC = re.compile(r"[؀-ۿ]")
EXCERPT = 80          # words per page
BUDGET = 500          # words per query, all told
CAIRO = datetime.timezone(datetime.timedelta(hours=2))
TRACKING = re.compile(r"^(utm_\w+|ocid|cmpid|fbclid|gclid|mc_\w+|ref|src|smid|taid|guccounter|guce_\w+)$", re.I)


def tidy(url):
    """The outlet's link without tracking parameters, Arabic addresses decoded (the same page, far fewer characters)."""
    try:
        p = urllib.parse.urlsplit(url)
        q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query, keep_blank_values=True) if not TRACKING.match(k)]
        url = urllib.parse.urlunsplit((p.scheme, p.netloc, p.path, urllib.parse.urlencode(q), ""))
    except Exception:
        pass
    return articles.short(url)


def words(s):
    return len(s.split())


def research(query, days, arabic, pages):
    """One query: {"query", "rows": [(when, outlet, title, url)], "read": [page dicts], "error"}."""
    out = {"query": query, "rows": [], "read": [], "error": None}
    try:
        rows = stock_news.google(query, days, arabic)
    except Exception as e:
        out["error"] = f"search failed ({type(e).__name__})"
        return out
    seen, keep = set(), []
    for r in rows:   # the feed's own order: relevance, as a search engine's
        key = re.sub(r"\W+", "", r[2].lower())[:60]
        if key in seen:
            continue
        seen.add(key)
        keep.append(r)
    keep = keep[: pages + 6]
    # read one or two past the number wanted, so a paywalled page does not leave the query short
    n = min(len(keep), pages + 2)
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        urls = list(pool.map(stock_news.resolve, [r[3] for r in keep[:n]]))
    got = articles.read_many(urls) if urls else []
    out["rows"] = [(w, o, t, u) for (w, o, t, _), u in zip(keep[:n], urls)] + keep[n:]
    out["read"] = got
    return out


def show(res, pages):
    """The query's printed block, about BUDGET words, and the URLs whose excerpts it printed."""
    lines, logged = [f"## {res['query']}"], []
    if res["error"]:
        return lines + [f"- {res['error']}", ""], logged
    rows, got = res["rows"], res["read"]
    if not rows:
        return lines + ["- nothing found in the feed for these days: try other words or --days", ""], logged
    good = [i for i, g in enumerate(got) if not g["error"]][:pages]
    failed = [i for i, g in enumerate(got) if g["error"]]
    same = articles.copies([got[i]["text"] for i in good])
    used = words(lines[0])
    for k, i in enumerate(good):
        when, outlet, title, _ = rows[i]
        g = got[i]
        head = f"{k + 1}. {outlet} | {when.astimezone(CAIRO):%d %b %H:%M} | {title}\n   {tidy(g['url'])}"
        if same[k] is not None:
            body = f"   (same wording as {same[k] + 1}: one source, not two)"
        else:
            room = max(25, min(EXCERPT, BUDGET - used - words(head) - 40))
            body = "   > " + articles.excerpt(g["text"], room)
        lines += [head, body]
        used += words(head) + words(body)
        logged.append(g["url"])
    if not good:
        lines.append("- no page could be read: open the links below by hand if the story matters")
    if failed:
        lines.append("Not read: " + "; ".join(f"{rows[i][1]} ({got[i]['error'].split(' (')[0].split(':')[0]}) {tidy(got[i]['url'])}"
                                             for i in failed[:4]))
    also = [r for j, r in enumerate(rows) if j not in good and j not in failed][:4]
    if also:
        lines.append("Also: " + " | ".join(f"{o}: {t}" for _, o, t, _ in also))
    lines.append("")
    return lines, logged


def log(date, part, queries, urls):
    tool = os.path.join(HERE, "research_log.py")
    for cmd, items in (("search", queries), ("read", urls)):
        if items:
            try:
                subprocess.run([sys.executable, tool, date, part, cmd, *items], cwd=ROOT, capture_output=True, timeout=30)
            except Exception:
                pass


def main(a):
    days, ar, pages, logto, queries = 2, False, 4, None, []
    i = 0
    while i < len(a):
        x = a[i]
        if x == "--days":
            days, i = int(a[i + 1]), i + 1
        elif x == "--pages":
            pages, i = max(1, min(6, int(a[i + 1]))), i + 1
        elif x == "--ar":
            ar = True
        elif x == "--log":
            logto, i = (a[i + 1], a[i + 2]), i + 2
            datetime.date.fromisoformat(logto[0])
            if logto[1] not in ("newsletter", "desk"):
                sys.exit("--log DATE newsletter|desk")
        elif x.startswith("--"):
            sys.exit(__doc__)
        else:
            queries.append(x)
        i += 1
    if not queries:
        sys.exit(__doc__)
    with concurrent.futures.ThreadPoolExecutor(min(6, len(queries))) as pool:
        results = list(pool.map(lambda q: research(q, days, ar or bool(ARABIC.search(q)), pages), queries))
    logged = []
    for r in results:
        lines, urls = show(r, pages)
        print("\n".join(lines))
        logged += urls
    if logto:
        log(logto[0], logto[1], queries, logged)
        print(f"Logged {len(queries)} searches and {len(logged)} pages read ({logto[1]}, {logto[0]}).")


if __name__ == "__main__":
    main(sys.argv[1:])
