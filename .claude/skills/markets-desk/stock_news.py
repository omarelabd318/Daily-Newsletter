#!/usr/bin/env python3
"""List recent news for each of the desk's 24 stocks, as leads for the stock pages.

Usage:
  python3 .claude/skills/markets-desk/stock_news.py [DAYS] [TICKER ...]

DAYS defaults to 2 (use 3 on Sundays, to cover the weekend). With no tickers it covers all 24.
For each stock it prints headlines from Google News (English, plus Arabic for the Egyptian stocks), newest
first, each with its date, outlet and the story's own link at the outlet (Google's redirect is resolved;
if that fails the Google link is shown). Headlines are leads, not facts: open the story at the outlet
before using it, check it against a second outlet where it matters, and keep only news about the company,
its stock, or something that clearly affects it (results, disclosures, deals, ratings, management,
regulation, prices of what it sells). Market wraps that only list the stock's move are skipped.
"""
import datetime
import concurrent.futures
import email.utils
import html
import json
import re
import sys
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
# Each stock's search terms: the English query and, for the EGX, an Arabic one.
STOCKS = {
    "COMI": ('"Commercial International Bank" OR "CIB Egypt"', '"البنك التجاري الدولي"'),
    "TMGH": ('"Talaat Moustafa"', '"طلعت مصطفى"'),
    "ETEL": ('"Telecom Egypt"', '"المصرية للاتصالات"'),
    "PHDC": ('"Palm Hills Developments" OR "Palm Hills Egypt"', '"بالم هيلز"'),
    "SWDY": ('"Elsewedy Electric"', '"السويدي إليكتريك"'),
    "ORAS": ('"Orascom Construction"', '"أوراسكوم كونستراكشون"'),
    "FWRY": ('"Fawry" Egypt', '"فوري" مدفوعات'),
    "ABUK": ('"Abu Qir Fertilizers"', '"أبوقير للأسمدة"'),
    "HRHO": ('"EFG Holding" OR "EFG Hermes"', '"إي إف جي القابضة" OR "هيرميس"'),
    "CLHO": ('"Cleopatra Hospital"', '"مستشفى كليوباترا"'),
    "JUFO": ('"Juhayna"', '"جهينة"'),
    "ALCN": ('"Alexandria Container"', '"الإسكندرية لتداول الحاويات"'),
    "AAPL": ('Apple stock OR "Apple Inc"', None),
    "MSFT": ('Microsoft stock', None),
    "NVDA": ('Nvidia stock', None),
    "AMZN": ('Amazon stock', None),
    "GOOGL": ('Alphabet stock OR "Alphabet Inc"', None),
    "META": ('Meta Platforms stock', None),
    "TSLA": ('Tesla stock', None),
    "JPM": ('JPMorgan stock OR "JPMorgan Chase"', None),
    "XOM": ('"Exxon Mobil" OR ExxonMobil', None),
    "AVGO": ('Broadcom stock', None),
    "BRK.B": ('"Berkshire Hathaway"', None),
    "WMT": ('Walmart stock', None),
}
# A headline must name the company (one of these words) to count.
MUST = {
    "COMI": ["Commercial International", "CIB", "التجاري الدولي"], "TMGH": ["Talaat", "TMG", "طلعت مصطفى"],
    "ETEL": ["Telecom Egypt", "WE ", "المصرية للاتصالات"], "PHDC": ["Palm Hills", "بالم هيلز"],
    "SWDY": ["Elsewedy", "السويدي"], "ORAS": ["Orascom Construction", "أوراسكوم كونستراكشون", "أوراسكوم للإنشاءات"],
    "FWRY": ["Fawry", "فوري"], "ABUK": ["Abu Qir Fertil", "أبوقير للأسمدة", "أبو قير للأسمدة"],
    "HRHO": ["EFG", "هيرميس", "إي إف جي"], "CLHO": ["Cleopatra", "كليوباترا"],
    "JUFO": ["Juhayna", "جهينة"], "ALCN": ["Alexandria Container", "الحاويات"],
    "AAPL": ["Apple"], "MSFT": ["Microsoft"], "NVDA": ["Nvidia"], "AMZN": ["Amazon"], "GOOGL": ["Alphabet", "Google"],
    "META": ["Meta"], "TSLA": ["Tesla"], "JPM": ["JPMorgan", "JP Morgan", "Dimon"], "XOM": ["Exxon"],
    "AVGO": ["Broadcom"], "BRK.B": ["Berkshire", "Buffett"], "WMT": ["Walmart"],
}
# Sports clubs share some company names, and daily price lists mention banks: skip both.
NOISE = re.compile(r"(league|coach|match|fixtures|vs\.? |\bfc\b|football|olympic|دوري|مباراة|تشكيل|المدرب|لاعب|كورة|"
                   r"نادي|الرياضي|أولمبياد|مستشفى جهينة|shares (acquired|sold|bought) by|sells [\d,]+ shares|buys [\d,]+ shares|"
                   r"etfs? (are )?(buying|bought)|net etf|acquires [\d,]+ shares|holdings (lifted|cut|raised|trimmed|lowered) by|"
                   r"stock (bought|sold) by|position in|بمركز جهينة|محمد جهينة|سوهاج|"
                   r"سعر (الدولار|الريال|اليورو|الجنيه|الدرهم|الدينار)|أسعار العملات|exchange rate today)", re.I)
WRAPS = re.compile(r"(stocks to watch|market wrap|top gainers|top losers|biggest movers|stock market today|"
                   r"premarket|pre-market movers|why .* stock is (up|down) today)", re.I)


def google(query, days, arabic=False):
    lang = "hl=ar&gl=EG&ceid=EG:ar" if arabic else "hl=en-US&gl=US&ceid=US:en"
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query + f' when:{days}d')}&{lang}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    feed = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    out = []
    for item in re.findall(r"<item>(.*?)</item>", feed, re.S):
        title = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<title>(.*?)</title>", item, re.S).group(1)))
        link = re.search(r"<link>(.*?)</link>", item, re.S).group(1).strip()
        src = re.search(r"<source[^>]*>(.*?)</source>", item, re.S)
        outlet = html.unescape(src.group(1)) if src else ""
        when = email.utils.parsedate_to_datetime(re.search(r"<pubDate>(.*?)</pubDate>", item).group(1))
        if outlet and title.endswith(" - " + outlet):
            title = title[: -len(outlet) - 3]
        out.append((when, outlet, title, link))
    return out


def resolve(link):
    """Google News links redirect through a script; ask Google for the outlet's own URL instead."""
    aid = re.search(r"/articles/([^?]+)", link)
    if not aid:
        return link
    aid = aid.group(1)
    try:
        req = urllib.request.Request(f"https://news.google.com/rss/articles/{aid}", headers={"User-Agent": UA})
        page = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
        sg = re.search(r'data-n-a-sg="([^"]+)"', page).group(1)
        ts = re.search(r'data-n-a-ts="([^"]+)"', page).group(1)
        inner = json.dumps(["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None, None, None,
                                            None, 0, 1], "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0], aid, int(ts), sg])
        body = "f.req=" + urllib.parse.quote(json.dumps([[["Fbv4je", inner, None, "generic"]]]))
        req = urllib.request.Request("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body.encode(),
                                     headers={"User-Agent": UA, "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
        out = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
        return json.loads(json.loads(out.split("\n\n", 1)[1])[0][2])[1]
    except Exception:
        return link


def main(args):
    days = int(args.pop(0)) if args and args[0].isdigit() else 2
    tickers = [a.upper() for a in args] or list(STOCKS)
    bad = [t for t in tickers if t not in STOCKS]
    if bad:
        sys.exit(f"Not one of the desk's stocks: {', '.join(bad)}")
    print(f"News leads for the last {days} days, {datetime.date.today()}. Open each story before using it.\n")
    for t in tickers:
        en, ar = STOCKS[t]
        rows, errors = [], []
        for q, arabic in ((en, False), (ar, True)):
            if not q:
                continue
            try:
                rows += google(q, days, arabic)
            except Exception as e:
                errors.append(f"{'Arabic' if arabic else 'English'} search failed: {e}")
        seen, keep = set(), []
        for r in sorted(rows, key=lambda r: r[0], reverse=True):
            key = re.sub(r"\W+", "", r[2].lower())[:60]
            if key in seen or WRAPS.search(r[2]) or NOISE.search(r[2]) or not any(m.lower() in r[2].lower() for m in MUST[t]):
                continue
            seen.add(key)
            keep.append(r)
        keep = keep[:8]
        with concurrent.futures.ThreadPoolExecutor(8) as pool:
            urls = list(pool.map(resolve, [r[3] for r in keep]))
        keep = [(w, o, ti, u) for (w, o, ti, _), u in zip(keep, urls)]
        print(f"## {t}  ({len(keep)} leads)")
        for e in errors:
            print(f"- {e}")
        for when, outlet, title, link in keep:
            print(f"- {when:%a %d %b} | {outlet} | {title}\n  {link}")
        if not keep and not errors:
            print("- nothing found")
        print()


if __name__ == "__main__":
    main(sys.argv[1:])
