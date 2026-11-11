---
name: daily-newsletter
description: >-
  House rules for writing an edition of the Daily Newsletter in this repo (editions/YYYY-MM-DD.md):
  word budget per section, which section each kind of story belongs in, and a checker to run before
  committing. Use whenever writing, editing or reviewing a newsletter edition here.
---

# Daily Newsletter house rules

These rules add to the task prompt that asks for the edition. Where the prompt sets voice, sources,
section order or publishing steps, follow the prompt. This file sets how much space each section gets,
where each story goes, and the check to run before committing.

## US English

Write in US English: American spelling (organize, analyze, center, program, defense, labor, color, percent,
traveled, fertilizer) and month-first dates ("Thursday, November 5", "Nov 5", never "5 November"). Proper names
keep their own spelling (the Labour Party, Egypt Aluminium, the UK Ministry of Defence), and quotes keep the
speaker's words. The checker lists any British spelling or day-first date it finds.

## Word budget

Aim for about 3,050 to 3,150 words, not counting the Sources list. These numbers are a guide to
balance, never a limit. Never leave out a story that deserves a place because a section or the edition
is over its word count: include it, and let the section run long. Equally, do not pad a section to
reach its number on a quiet day.

| Section | Words | Share |
|---|---|---|
| Today at a Glance | 150-190 | 6% |
| Quick Hits | 70-100 | 3% |
| Weather | 50-80 | 2% |
| Egypt News | 450-550 | 17% |
| Top World Headlines | 300-380 | 11% |
| Regional and Gulf | 180-230 | 7% |
| Markets: Egypt Markets | 280-340 | 10% |
| Markets: Global Markets | 210-260 | 8% |
| Stocks Watch (two tables) | 140-240 | 6% |
| Currency and Commodities Watch | 180-260 | 7% |
| In Other News: Tech and AI | 130-170 | 5% |
| In Other News: Sports | 150-200 | 6% |
| In Other News: Health and Science | 70-100 | 3% |
| In Other News: Entertainment and Culture | 120-150 | 5% |
| Economic Calendar | 130-170 | 5% |
| Worth Knowing | 160-200 | 6% |

Sports is the deepest part of In Other News, but it no longer outweighs Markets. Global Markets got the
extra room: use it to explain what drives the moves and what they mean for Egypt and emerging markets.

### Minimum stories per section

A busy section, often Markets, must not crowd out the rest. Aim for at least this many separate stories:

| Section | At least |
|---|---|
| Egypt News | 4 |
| Top World Headlines | 6 |
| In Other News: Tech and AI | 3 |
| In Other News: Sports | 5 |
| In Other News: Entertainment and Culture | 3 |

Reach these with stories genuinely worth a reader's time, never filler: when a section is short, search
wider (more outlets, other regions, other leagues and sports, other parts of tech or culture) for real
news from the last day or two, rather than stretching minor items or splitting one story into several.
If, after a real search, a section truly has fewer worthwhile stories, keep it shorter and say so in the
final reply's Publishing note. The checker warns when a section is below its minimum.

## Today at a Glance

Each numbered item links to the full story further down. Make the headline a link to the story's
anchor, which the site builds from the story's bold lead-in: `story-` followed by the lead-in in lower
case, with every run of characters other than letters and digits turned into a single hyphen and no
hyphen at either end. For example, a story that opens `**Rate decision on Thursday:**` has the anchor
`#story-rate-decision-on-thursday`, so its item reads:

`2. **Economy:** [The central bank meets Thursday with rates expected to hold at 19%](#story-rate-decision-on-thursday)`

If a story has no bold lead-in of its own, link to its section or part instead, built the same way from
the heading, for example `#egypt-news` or `#tech-and-ai`. These
in-page links are the only links allowed in Today at a Glance.

After the numbered list, end the section with one line on the day's key scheduled events, such as a
central bank decision, a data release, a major vote or a big match, with times in Cairo where known:

`**What to watch today:** The central bank's rate decision at 2pm; Al Ahly vs Pyramids at 8pm.`

Only list events happening that day. On a day with nothing scheduled, say what to keep an eye on instead.

## Check every figure

Before publishing, check each figure in Stocks Watch and Currency and Commodities Watch, and any key
number in Egypt Markets (EGX30 close, central bank rates), against a second source: the backup in the
go-to sources table or another reputable outlet. Where the two agree within normal rounding, use the
figure. Where they disagree, use the more authoritative or more recent one and mark it `(unconfirmed)`,
for example `56.10 (unconfirmed)`. Never present a figure as confirmed when only one source had it and it
looks out of line with recent days. Never guess a figure; write `n/a` instead.

## Context from the data log

`data/markets.json` holds daily figures back to 2021. After logging the day's figures, run
`python3 .claude/skills/daily-newsletter/market_facts.py DATE`. For each item it prints the month-to-date
and year-to-date change, the 52-week range, and lines marked `NOTABLE:` for an item within 3% of its
52-week high or low, on a run of 4 or more sessions up or down, or at its highest or lowest in at least
three months. Use the notable facts for one or two context lines in Egypt Markets and Global Markets, for
example "The EGX30 closed at its highest since March" or "the pound has weakened for five sessions in a
row", and consider one for the Number of the day. Only use facts that fit the story; skip the rest. Take
the day's change from the source, not from this report, since a log entry can mix closing and intraday
values.

## Number of the day

Quick Hits always includes one item `**Number of the day:** ...`: a single striking figure from the day's
news, with one line on why it matters. Pick a number covered elsewhere in the edition or one that adds
something new, and check it like any other figure.

## Explained boxes

When a story relies on a term many readers may not know (for example carry trade, T-bill auction,
sourcing commission, oversubscription, core inflation), add a short explainer straight after that story,
as its own quote line:

`> **Explained: carry trade.** Borrowing in a low-interest currency to invest in a higher-yielding one,
such as Egyptian treasury bills, profiting from the gap as long as the exchange rate holds.`

One or two sentences, plain language, no figures that need checking. Use at most three per edition, only
where they genuinely help, and never explain the same term in Worth Knowing on the same day. The site
shows these as small boxes.

## Continuing stories

Before writing, read the most recent earlier edition in `editions/` (the newest file before today's date;
after a gap, such as a failed run, that may be two or more days old). Use it only to tell which stories
are new and which are continuing. Then:

- **Continuing story with a new development:** open with what is new, then give one sentence of
  background so a reader who missed earlier editions can follow it. Do not retell the whole backstory.
- **Continuing story with nothing new:** leave it out, or keep it to one line if it still matters today.
  Use the space for fresh news.
- **New story:** write it in full, as usual.

Every edition must still make full sense on its own. Never refer to earlier editions or assume the reader
saw them: no "as reported yesterday", "as covered in Tuesday's edition", "as noted previously" or "the
story continues". Write "Parliament's authorisation, approved on 26 October, …", not "the authorisation
covered yesterday …". This applies to every section, including Today at a Glance.

## Where each story goes

Each story appears in one section only. Today at a Glance is the exception: it is an index of stories
covered in full further down.

- **Top World Headlines:** stories outside the Middle East and North Africa.
- **Regional and Gulf:** Middle East and North Africa politics, security and diplomacy, including Iran,
  the Houthis, Israel, Gaza, Lebanon, Syria, Libya, Sudan and the Strait of Hormuz. Where a story has a
  clear, real effect on Egypt (for example on the Suez Canal, fuel costs or investment), add one line on
  it. Do not force an Egypt angle onto stories that have none.
- **Markets:** all prices and money. That covers oil, gold, Gulf stock markets, bonds, IPOs, earnings,
  deals and Gulf or foreign investment flowing into Egypt. Regional and Gulf may refer to a market move
  in a few words, but the figures and analysis live here. Global Markets gives the day's close and change
  for all three US indices every day, in this order: S&P 500, Nasdaq, Dow Jones, for example "The S&P 500
  lost 0.30% to 7,720.54, the Nasdaq 1.38% to 26,184.73 and the Dow 0.25% to 52,342.56".
- **Egypt News:** Egyptian government decisions and domestic stories. When Egypt acts on a regional
  matter (for example a parliamentary vote on a deployment), the Egyptian decision goes here and Regional
  and Gulf does not repeat it.
- **Stocks Watch:** two tables of figures only (see below). Markets keeps its own coverage, including
  stories about individual companies; Stocks Watch just lists the prices.
- **Currency and Commodities Watch:** figures, with a note only where it adds something the figures do not
  show: a cause in a few words ("Bank of England hiked", "Haven demand returns"), a source or basis ("Retail
  price" on the first gold row, "November 5 auction"), a milestone ("Lowest in a year"). Leave the Note cell
  empty otherwise: no "Down five sessions running" on row after row, no repeat of the day's change, which the
  site shows in its own column. Keep a note to about five words so the row stays one line. No story narrative;
  the story behind a move belongs in Markets. Keep every row: the site shows USD/EGP, the dollar index, EUR,
  GBP, gold 24K, gold in dollars, Brent and the rates first and folds the Gulf currencies (pegged to the dollar)
  and the other gold carats behind "Show all", but they are still checked and logged every day.
- **Economic Calendar:** upcoming events only, not news already covered above. Start from
  `python3 .claude/skills/daily-newsletter/calendar_facts.py DATE 14`, which lists the holidays and EGX closures,
  the desk's stocks' results dates ("expected" unless confirmed) and dividends already in the repo's data, so the
  dates known are in and right; add the rest (central bank meetings, data releases, auctions, fixtures) from research.
  Layout: the next few days each get their own item (`**Tuesday, November 10:** ...`). Events further out go
  under `**Coming up:**` as a list, one date per line, in date order, never one running paragraph:

  ```
  **Coming up:**

  - **Nov 15:** Air Cairo resumes Cairo–Damascus flights
  - **Nov 16–17:** World Economic Forum's first business meeting in Egypt, New Capital
  - **Dec 17:** Central bank rate meeting

  *No public holidays or EGX closures in the next two weeks.*
  ```

  Several events on one date share its line, separated by semicolons. The closing line on holidays and EGX
  closures is italic and goes last.

## Fetch the figures first

Start the figures with one command from the repo root:

```
python3 .claude/skills/daily-newsletter/fetch_figures.py DATE
```

It fetches the Egyptian stocks, the EGX30, the US stocks and indices, Brent, gold, Bitcoin and the
exchange rates (about 30 seconds), and prints a table with each value, its change, whether it is a
closing or a LIVE price, the quote time and the source. Then:

- **Anything under NOT FOUND:** look it up by hand from the go-to sources below (first choice, then
  backup, then search). If it still cannot be confirmed, write `n/a` in the edition. Never guess or carry
  over an old figure as if it were today's.
- **Check every figure against a second source** as usual; the script only replaces the first lookup.
- **Egyptian stocks:** the script works out the official close as the previous close plus the day's
  change, because the "last price" on Mubasher can be an earlier trade. Use its figures, not the last price.
- **Logging:** after checking, run the `log_figures.py` command it prints at the end, adding any figure
  found by hand and replacing any figure changed after checking (for example the central bank's dollar
  rate instead of the market mid-rate, when that is what the edition shows). It already holds closing
  prices only, including previous closes while the EGX is trading.

## Running topics

The site groups stories into running topics (Iran war and Hormuz, the pound and the central bank…): a label under
each story, a Topics list and a page per topic with every story on it (`data/topics.json`, managed with
`python3 .claude/skills/daily-newsletter/topics.py`).

After writing the edition (and the recap, as `DATE-recap`):
1. Run `topics.py tag DATE`. It tags each story whose lead-in names a topic, or whose text names it at least twice,
   and prints the list. Read it: `topics.py remove DATE "Lead-in" TOPIC` for a wrong match, `topics.py add DATE
   "Lead-in" TOPIC` for a story the keywords missed. Hand changes survive later re-tagging.
2. For each topic the edition moved, rewrite its "Where it stands" with `topics.py now TOPIC "..."`: two or three
   sentences on where the story stands today, figures checked, in the edition's voice and US English. The checker
   warns when a topic the edition moved still has an older one.
3. When a new story is likely to run for days (a war, a rate cycle, a listing, a scandal), start a topic:
   `topics.py new id "Name" "keyword regex"`, then tag the recent editions it appeared in. Keep names plain and the
   keywords specific (a company or place name, not a common word). Use `topics.py list` to see them all.
4. Commit `data/topics.json` with the edition. The checker blocks publishing when the edition has stories that
   match a topic but was never tagged.

## Research log

Log the research as you do it, with `python3 .claude/skills/daily-newsletter/research_log.py DATE newsletter search "query"`
for every web search and `... DATE newsletter page URL` for every page opened (read_enterprise.py counts as the pages it
prints). A full edition takes at least 25 searches across many outlets and 30 pages opened; the checker warns below
that and blocks publishing below half. The log is the honest record of the work: never log a search or a page that
was not made. End the final reply with the line `research_log.py DATE newsletter summary` prints.

## Attribution in the text

- **Name the outlet** whenever a claim is attributed: "according to Reuters", "Ahram Online reported",
  "per Bloomberg". A search result that summarises a story is not the source; credit the outlet behind it.
- **General credits** such as "according to news bulletins" or "market reports suggest" are fine when the
  point rests on more than one outlet. Never use them to stand in for a single source. The checker flags
  them only as a reminder to make sure several outlets back the point.
- **Attribute only where it adds something:** an exclusive, a disputed or unconfirmed claim, a forecast or
  an estimate, or a figure that differs between sources. Well-established facts need no credit in the text;
  the Sources list covers them.
- **Usually one credit per item:** if a point rests on several outlets, credit the main one, or use a
  general credit such as "according to news bulletins", and let the Sources list carry the rest. About
  10 to 20 credits in an edition reads naturally. The checker blocks publishing above 25 credits, when
  more than half the stories in a section carry a credit, or when one outlet is credited in more than half
  of a section's stories; it warns at 3 or more credits in one item.
- **EnterpriseAM and CairoScene are trusted, not the backbone:** treat both as very good, credible sources with
  strong stories, and use them freely, but check their stories against other outlets where they carry them too,
  and keep the two together under a third of the edition's sourced items (the checker warns above that). Never
  leave out a good story from either to balance the count: add strong stories from other outlets instead. Write
  in your own words so the edition never reads like a rewrite of either. Each story is still judged on its own
  merit and placed in the section where it belongs.
- **Spread the wire and world sources:** no other single outlet should carry more than about six of the
  edition's Sources links (EnterpriseAM and CairoScene fall under the one-third rule above instead). World and regional stories come from many outlets (Reuters, AP,
  AFP, BBC, the Financial Times, Bloomberg, The National, Asharq Al-Awsat, Al-Monitor, Al Jazeera and others):
  keep every story that deserves its place, but take it from the outlet with the fullest report, or the one
  closest to the news, rather than defaulting to one site, and check it against a second. Al Jazeera is a
  credible source for the region, but its own editorial line on Gulf and regional politics is one more reason
  to pair it with another outlet. The checker warns when one outlet passes six links.
- **Reuters via Yahoo Finance:** Yahoo Finance (finance.yahoo.com, and yahoo.com/news) republishes Reuters wire
  stories in full and free to read, marked "Reuters" at the top. It is Reuters' own reporting, word for word, so it
  is as reliable as Reuters itself: one of the most dependable sources there is for markets, economies, companies
  and world news. Use it freely, above all when reuters.com asks for a login or will not open. Credit Reuters in the
  text ("according to Reuters") and in Sources write `Reuters (via Yahoo Finance)` with the Yahoo link. It counts as
  Reuters, not Yahoo, for the six-links rule. The same goes for other wire stories Yahoo carries (AP, AFP): credit
  the agency. Yahoo's own articles and its contributor or partner pieces (Motley Fool, Zacks, Investopedia and the
  like) are not wire reporting: treat those as the outlet that wrote them. Summary services such as Finimize, which
  rewrite Reuters or Bloomberg stories, are leads only: find and cite the original.
- **FactIQ (connector, when the run has it, the mcp__factiq__ tools):** a read-only service of official statistics
  and filings. Use it where it holds the figure: Suez Canal, Bab el-Mandeb and Hormuz shipping (daily transits and
  cargo tonnage from IMF PortWatch, two to three weeks behind) for Suez, Red Sea and Iran-war stories; US data
  (payrolls, CPI, GDP from BLS and BEA, Treasury yields) and what Fed, ECB, Bank of England and other central bankers
  said, with quotes, for Global Markets; Brent, gold and FX as a second source for the currency table; company
  filings and earnings calls for a big company story; the IMF's forecasts for Egypt (yearly, marked as projections).
  It has no Egyptian news, EGX prices, monthly Egyptian figures or Central Bank of Egypt statements, and its
  dollar-pound rate is a market rate, not the central bank's: those stay with the usual sources. Credit the
  underlying source (IMF PortWatch, the BLS, the company's filing) with the link FactIQ returns, never FactIQ itself;
  log each lookup as a page (`research_log.py DATE newsletter page factiq:<what>`); without the connector, carry on.
- **Variety by adding, not dropping:** go through the whole EnterpriseAM edition (on weekdays) and
  CairoScene, and consider every item. Variety comes from adding strong stories from other outlets
  alongside them, never from leaving out a good EnterpriseAM or CairoScene story to balance the count.
- **Read EnterpriseAM with its script, not a web fetch:** on weekdays run
  `python3 .claude/skills/daily-newsletter/read_enterprise.py`. It prints the whole AM edition: every story
  in full with its own link, the smaller items inside each story (under their own subheadings), Today at a
  glance and the calendar. A web fetch only returns a summary, which can drop items and has no story
  links. Use a web fetch of https://enterpriseam.com/egypt/am-edition/ only if the script fails.
- **How research runs:** EnterpriseAM (on weekdays) and CairoScene are read in full on every run, as a
  core part of research, alongside many searches across many other outlets: Egyptian, regional and
  international. Neither comes first and neither is a fallback. Pick the day's stories from everything
  together, on merit, so the wider research shapes the edition as much as those two do.
- **Link each story's own page** in Sources, one link per story, for EnterpriseAM and CairoScene as for
  everyone else (for example `https://enterpriseam.com/egypt/2026/10/25/...`), not the homepage or the
  edition page. `enterpriseam.com/egypt/am-edition/` always shows the latest edition, so it points to the
  wrong day later. For items that appear only in the edition or on the homepage, use one line for that
  page and say how many items it was used for, for example
  `[EnterpriseAM Egypt, AM edition, 29 October 2026 (used for 3 items)](https://enterpriseam.com/egypt/am-edition/)`.
- **Dependence check:** the checker warns when EnterpriseAM and CairoScene make up more than a third of
  the links in Sources. The answer is wider research for more strong stories, never cutting a good one.
- **Merit, not origin:** the same bar applies the other way. Include an EnterpriseAM or CairoScene story
  because it is worth a reader's time, not because of where it came from; skip their minor items as you
  would anyone's. Each section should draw on a range of outlets, and the edition should never read like
  a summary of those two.
- **Credit every outlet the same way:** keep crediting EnterpriseAM and CairoScene whenever a point comes
  from them and the credit fits; they are trusted, daily sources. The aim is that other outlets are
  named just as readily when a point comes from them, not that these two are named less.

## Egyptian news outlets: read every day

On **every** run, weekdays and weekends alike, read the front pages of at least three of these outlets,
alongside EnterpriseAM and CairoScene, before choosing the Egypt News stories. All of them load from the
cloud (tested 30 October 2026):

- **English:** Egypt Independent (egyptindependent.com), Daily News Egypt (dailynewsegypt.com),
  Egyptian Streets (egyptianstreets.com), Zawya (zawya.com, Egypt pages), Arab Finance (arabfinance.com),
  Middle East Observer (meobserver.org), Amwal Al Ghad English (en.amwalalghad.com).
- **Arabic:** Youm7 (youm7.com), Masrawy (masrawy.com), Al-Shorouk (shorouknews.com).
- **Regional, for Egypt stories with a wider angle:** The National, Al-Monitor, Asharq Al-Awsat,
  Middle East Eye.
- **Blocked from the cloud:** Ahram Online, Mada Masr and Egypt Today do not load (SIS times out). Use
  them only through a search result that names the story, and credit the outlet, not the search.

Rules:

- **Egypt News draws on at least three outlets.** No one outlet supplies more than half its stories.
- **Cross-check:** check each Egypt News story against a second outlet where one carries it; a story only
  one outlet carries is either flagged as such or left out if it is a claim rather than an event.
- **Rotate:** vary which three or more you read most closely from day to day, but always scan the rest
  for anything big. Saturdays and Fridays, when EnterpriseAM has no edition, lean on these outlets more,
  never on CairoScene alone.
- If an outlet stops loading, say so in the run notes and use another from the list.

## Go-to sources for figures

Check these pages first for the figures below, then search as usual for anything they do not cover.
Every page here loaded with real content when tested from the cloud environment on 28 October 2026.
Sites change, so if a page fails or looks stale, use the backup or search, and say in the edition when
a figure could not be confirmed. These pages are for figures; news still comes from many outlets.

| Figure | First choice | Backup |
|---|---|---|
| US dollar index (DXY) | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=5d&interval=1d (fetch_figures.py gets it) | Search "dollar index" news for the day's level |
| Brent, gold in dollars, dollar index, S&P 500, Dow (backup and check) | Yahoo first; when Yahoo refuses (it often does from the cloud), fetch_figures.py takes them from TradingView's screener (Brent front-month and COMEX gold futures, the DXY, the S&P 500 and Dow), and when Yahoo answers it lists TradingView's Brent, gold and DXY as a "check" row to confirm against. Around a futures contract's expiry (Brent's front month rolls at the end of each month), sources can disagree on the day's change because they compare different contracts: compare like with like, and mark the change unconfirmed if they still differ. fetch_figures.py prints "CONTRACT SWITCH?" when it sees one; record it in desk/rolls.json as the markets-desk skill describes | FRED for the S&P 500 and Dow (a day behind); news reports of the day's settlement |
| EGP against USD, EUR, SAR, AED, KWD, QAR, GBP | The central bank's official buy and sell rates, https://www.cbe.org.eg/en/economic-research/statistics/cbe-exchange-rates (fetch_figures.py prints them and logs the dollar's); use the dollar's selling rate in the USD/EGP row. The logged pound rates and trend lines stay market mid-rates from https://open.er-api.com/v6/latest/EGP | EnterpriseAM's edition, or Egyptian news reports of the day's central bank rate |
| Gold in Egypt (21K, 24K, 18K per gram) | https://egypt.gold-price-today.com/ (Arabic: عيار 21 is 21K) | https://www.goldpricez.com/eg/gram |
| EGX30 close and daily change | https://english.mubasher.info/markets/EGX/indices/EGX30 (close, change, open, high, low) | https://tradingeconomics.com/egypt/stock-market |
| Egyptian stock prices (Stocks Watch) | https://english.mubasher.info/markets/EGX/stocks/TICKER, for example .../stocks/COMI (price, change, % change, previous close, time of last update) | Search |
| US stock prices (Stocks Watch) | https://query1.finance.yahoo.com/v8/finance/chart/TICKER?range=5d&interval=1d (JSON: the last two values in indicators.quote[0].close give the latest close and the change; timestamp gives the date). Do not use Yahoo for Egyptian stocks; its EGX data is years out of date | Nasdaq, then Polygon: fetch_figures.py tries both in turn, and check_edition.py confirms a US close against them (Polygon's key is a network secret on the environment, added by the proxy; five requests a minute) |
| Central bank interest rates | https://www.cbe.org.eg/en/economic-research/statistics/overnight-deposit-and-lending-rate (deposit and lending rates with the date they take effect; fetch_figures.py logs them) | https://tradingeconomics.com/egypt/interest-rate |
| Inflation (headline and core, annual) | https://www.cbe.org.eg/en/economic-research/statistics/inflation-rates (latest month; fetch_figures.py logs `infl_headline` and `infl_core`). The one-year T-bill yield minus headline inflation is the real return investors weigh | https://tradingeconomics.com/egypt/inflation-cpi |
| Net international reserves (monthly, $bn) | https://tradingeconomics.com/egypt/foreign-exchange-reserves (the central bank's figure, published about the 7th; its own reserves page has not been updated since 2023). fetch_figures.py logs `reserves_usd` | News reports of the central bank's announcement (Daily News Egypt, Ahram Online) |
| Treasury bill yields | The central bank's auction page, https://www.cbe.org.eg/en/auctions/egp-t-bills (latest results: weighted average accepted yield by tenor, with the auction date). fetch_figures.py reads it and logs each tenor once, on the first edition after its auction. 91- and 273-day bills are auctioned on Sundays, 182- and 364-day bills on Thursdays | News reports of the auction (Amwal Al Ghad, Al-Borsa, EnterpriseAM) |
| Public holidays and bank closures | https://www.officeholidays.com/countries/egypt/2026 (verify any holiday shift against a news report of the official announcement) | Search |
| Cairo weather, today and next two days | `python3 .claude/skills/daily-newsletter/weather.py` (two services side by side: Open-Meteo or MET Norway, and wttr.in) | Egyptian Meteorological Authority |
| Egyptian football | https://www.kingfut.com/ (English) | https://www.kooora.com/ (Arabic) |
| European football results | https://www.bbc.com/sport/football/scores-fixtures/YYYY-MM-DD (use the date of the matches) | https://www.espn.com/soccer/scoreboard |
| Tennis | https://www.bbc.com/sport/tennis | https://www.wtatennis.com/scores |

These block automated access from the cloud environment, so do not spend time on them: the Egyptian Exchange site (egx.com.eg), Ahram Online, Egypt Today,
Reuters, investing.com, timeanddate.com, the ATP Tour site and the Egyptian Meteorological Authority.
News reports that quote them are fine.

## Link every visual

The site shows text only, so a reader cannot see a photo, chart, video, map or infographic the
edition mentions. Whenever an item refers to one, link straight to it in the same sentence, for
example `[view the photo essay](https://...)` or `[watch the trailer](https://...)`. Link to the page
that shows the visual, not to a site's home page. If no direct link can be found, do not mention the
visual. Never embed images (`![...](...)`).

## Sports

Do not group Sports items under sport headings such as **Football**, **Tennis** or **Other Sports**, and
do not use any heading or standalone bold line inside Sports. Each match, result or story is its own item
with its own bold lead-in, for example `**Liverpool v Chelsea:** ...` or `**Paris Masters:** ...`. Order
them with Egyptian football first, then other football, then other sports.

## Stocks Watch tables

`## Stocks Watch` comes right after Markets and before Currency and Commodities Watch. It has two parts,
`### Egypt` first, then `### USA`. Each part is one table and nothing else: no paragraphs and no bullet
points. Under each heading, put one italic line saying which close the table shows, for example
`*EGX close, Tuesday 27 October*` or `*US close, Tuesday 27 October*`. If the run happens while the EGX is
trading, say so and give the time, for example `*EGX intraday, 11:49 Cairo*`.

The site adds a 1D / 1W / 1M / 6M / 1Y switch above each table: 1D shows the Change you write, the
other periods are worked out from the data log, and the trend line redraws over the same period.

Columns: `| Stock (ticker) | Close | Change | YTD |`, with the price in EGP or USD and the change as a
percentage with a sign, for example `+1.2%`. The site colours signed changes green or red with an arrow,
and bolds moves of 5% or more, so always write the sign. Take Change from the source. Take YTD (change
since the last close of the previous year) from the data log: log the day's figures first (see "Log the
day's figures"), then run `python3 .claude/skills/daily-newsletter/market_facts.py DATE --ytd`. Write
`n/a` for YTD when it prints n/a, and for notable movers that are not in the log.

List these every day, in this order:

| Egypt (EGX) | USA |
|---|---|
| Commercial International Bank (COMI) | Apple (AAPL) |
| Talaat Moustafa Group (TMGH) | Microsoft (MSFT) |
| Telecom Egypt (ETEL) | Nvidia (NVDA) |
| Palm Hills Developments (PHDC) | Amazon (AMZN) |
| Elsewedy Electric (SWDY) | Alphabet (GOOGL) |
| Orascom Construction (ORAS) | Meta (META) |
| Fawry (FWRY) | Tesla (TSLA) |
| Abu Qir Fertilizers (ABUK) | JPMorgan Chase (JPM) |
| EFG Holding (HRHO) | Exxon Mobil (XOM) |
| Cleopatra Hospital (CLHO) | Broadcom (AVGO) |
| Juhayna Food Industries (JUFO) | Berkshire Hathaway (BRK.B) |
| Alexandria Containers (ALCN) | Walmart (WMT) |

After the fixed rows, add up to three rows for other stocks with a notable move or notable news that
day, marked in italics, for example `| *Misr Cement Qena (MCQE), notable mover* | 167.85 | +8.5% | n/a |`.
Leave them out when nothing stands out. Every mover row shows its close, like the fixed rows: get it by
adding the tickers to the fetch command, for example
`python3 .claude/skills/daily-newsletter/fetch_figures.py DATE egx.MCQE us.ORCL`, which also gives YTD for
US stocks (write `n/a` for YTD when it has none). Movers are not logged.

On weekends the EGX is closed Friday and Saturday and US markets Saturday and Sunday. Show the last
session's close with its date. On EGX holidays, listed in `data/holidays.json`, do the same and say why in
the italic line, for example `*EGX closed today for Sham el-Nessim; last close Sunday 2 May*`, and log
the figures as usual (the last close again). The checker warns when a listed closure is not mentioned. If a price cannot be confirmed, write `n/a` rather than guessing.

The checker compares every Stocks Watch row with the data log: the close with what was logged for the
date, and the change with the move from the previous logged close (from the previous close to the live
price for an intraday table). A warning there means one of the two figures is wrong: recheck both at the
source and fix the table or re-run log_figures.py before publishing.

It also compares each logged close with the stock's last trade in the desk's intraday prices for that session. A
gap over 0.5% on the EGX or 1% in the US is an error that blocks publishing, unless the stock's own quote at its
source (Mubasher, Nasdaq) gives the logged figure as its close, which the checker looks up itself (an EGX close can
sit off the last trade, since the exchange sets it from the session's final trades). If it still errors, open the
quote: fix the log if it is wrong, or, where the close is right but the source would not answer the checker, record
it with `python3 .claude/skills/daily-newsletter/research_log.py DATE newsletter close TICKER PRICE "Mubasher"`.

## Egyptian holidays

`data/holidays.json` lists the public holidays that close the EGX. Use it in Today at a Glance's What to
watch line and the Economic Calendar (upcoming closures and long weekends). Dates marked `expected` are
projections, so always confirm them against current official announcements; when the Cabinet or the EGX
announces dates, update the file (dates, any day moved to a Thursday or Sunday, and `"status":
"confirmed"`) and commit it with the edition. When a new year's holidays are announced, add them.

## Currency and Commodities Watch table

Use four columns: `| Item | Level | Note | YTD |`.

- **Italic line first:** under the heading, one italic line saying which rates the table shows, for example
  `*USD/EGP is the central bank's rate; other currencies are market mid-rates.*` Then do not repeat
  "Market mid-rate" in the Notes.
- **Notes:** about 6 words, so rows stay on one line. Use them for one short point ("highest since
  March", "fourth rise running", "central bank rate"), or leave a Note empty when there is nothing to add.
  Do not repeat the day's change: the site adds a Change column to this table by itself, worked out from
  the data log, with a 1D / 1W / 1M / 6M / 1Y switch. That is one more reason to log every figure daily.
- **YTD:** the change since the last close of the previous year, from
  `python3 .claude/skills/daily-newsletter/market_facts.py DATE --ytd` after logging, with a sign
  (`+17.8%`). Write `n/a` when the figure is not in the log that day, and `—` for central bank rates,
  certificates and T-bills, which have no YTD.

Right after the USD/EGP row, add `| US dollar index (DXY) | 102.19 | ... | +4.0% |`: the dollar against six major
currencies, with the day's change in the Note, so readers can tell whether a move in the pound is the
dollar strengthening everywhere or something specific to Egypt. Say which in the Note when it is clear,
for example `+0.4%; dollar firmer worldwide` or `-0.3%; pound's fall is local`.

The site draws a trend line beside every row whose figure is in the data log: USD, EUR, SAR, AED, KWD,
QAR and GBP against the pound, the dollar index, 21K, 24K and 18K gold, the gold pound, global gold and
Brent. Log all of these every day so the lines stay up to date. Rates, certificates and T-bills change
too rarely for a line and get none.

Mark a figure the sources disagree on with `(unconfirmed)` right after it, in any table. The site shows
it as a small * that says "Unconfirmed" on hover, so it takes no extra space.

## Weekly Recap (Saturdays)

Every Saturday a separate run publishes a weekly recap alongside that day's regular edition. It sums up
the week from Sunday to Saturday. The daily rules on voice, sources, figure checks, linking visuals,
placement and standing alone all apply; the daily section list, word budgets, Today at a Glance links and
Stocks Watch do not.

- **File:** `editions/DATE-recap.md`, where DATE is the Saturday. In `editions/index.json` add
  `{"date": "DATE", "id": "DATE-recap", "label": "Weekly Recap", "summary": "..."}` and keep every other
  entry, including that day's regular edition.
- **Research:** start from that week's editions in `editions/` (Sunday to Saturday, including any second
  edition of a day), then search for how each big story developed and ended up. Report where things stand
  now, not what was said on each day. Check every figure as usual.
- **Length:** about 2,050 to 2,400 words, a 9 to 10 minute read. A guide, not a limit.
- **First line:** an italic sentence with the week's dates and what it was about, for example
  `*Week of 25 to 31 October 2026: a rate hold, a weaker pound and Egypt's Saudi deployment vote.*`
- **Sections,** in this order, each as `##` with exactly these titles:
  1. **The Week in Brief:** a numbered list of 7 to 10 of the week's biggest stories, Egypt first, each
     `**Label:** one sentence`. No links.
  2. **What Tied the Week Together:** the week's essay, 200 to 260 words in two or three paragraphs with no bold
     lead-ins: the thread that connects the week's biggest stories, told as cause and effect (a rate decision, the
     pound, who bought the bills, what that did to the EGX; a war headline, oil, the import bill). Say what changed
     for a reader in Egypt between last Saturday and this one, and what is still unresolved going into next week.
     It is analysis, not opinion or forecast: every link in the chain rests on a fact and figure already in the
     recap, and where the connection is the outlets' or analysts' reading, say whose. If the week had no single
     thread, say so and take the two that mattered. Write it last, after the other sections.
  3. **Egypt This Week:** 4 to 6 items on the main Egyptian stories, each with where it stands now.
  4. **Region and World:** 4 to 6 items, regional first, then the rest of the world.
  5. **Markets This Week:** a short paragraph on the week, then a table
     `| Item | Week close | Weekly change |` covering EGX30, USD/EGP, gold 21K per gram in Egypt, Brent,
     S&P 500, Nasdaq, Dow Jones and Bitcoin, then one line each on the week's best and worst EGX30 stocks if known.
  6. **Sports This Week:** the week's main results and stories as separate items, Egyptian football first,
     with no sport headings.
  7. **Culture and Tech:** 3 to 5 short items from tech, AI, entertainment and culture.
  On the first Saturday of a month, add **Month in Numbers** right after Markets This Week: one line on
     the month, then a table `| Item | Start of month | End of month | Change |` for EGX30, USD/EGP, gold
     21K, Brent, S&P 500, Dow Jones and Bitcoin, taken from the first and last entries of the previous month in
     `data/markets.json` (say "not logged" where a figure is missing).
  In the last Saturday recap of December, also add **Year in Numbers** right after Markets This Week (and
     after Month in Numbers if both appear): one line on the year, then the table that
     `python3 .claude/skills/daily-newsletter/market_facts.py DATE --year` prints, then one line each on
     the year's best and worst stocks from that table.
  8. **How It Played Out:** go through the What to watch today lines in this week's daily editions and
     pick the 4 to 6 events that mattered most (a rate decision, a vote, a data release, a big match).
     For each, one item: what was expected and what actually happened, for example
     `**Central bank meeting:** Expected to hold; it held rates at 22% and signalled cuts in December.`
     Skip anything already covered in full above; say "postponed" or "no decision yet" where that is the
     case. Do not mention the daily editions themselves.
  9. **The Week Ahead:** the key scheduled events for the coming week (central bank meetings, data,
     holidays and closures, big matches).
  10. **Sources:** the links used.
- On the recap page, the site draws year-long trend lines next to the Markets This Week rows by itself;
  nothing to add for that.
- **Data log check:** before committing, run
  `python3 .claude/skills/daily-newsletter/check_log.py DATE`. Fix any real problem it finds in
  `data/markets.json` with log_figures.py (checking the figure at the source first), commit the fix, and
  list anything left unfixed in the final reply's Publishing note. It does not go in the recap itself.
- Every item opens with a bold lead-in, as in the daily edition. Never refer to the daily editions
  themselves ("as reported on Tuesday"): write about the events and their dates.

## Log the day's figures

After the figures are checked, record them in `data/markets.json` so the site can draw small trend lines
next to table rows and the recap can compute weekly and monthly changes. From the repo root:

```
python3 .claude/skills/daily-newsletter/log_figures.py DATE usd_egp=56.20 eur_egp=62.57 sar_egp=14.99 aed_egp=15.30 kwd_egp=181.19 qar_egp=15.41 gbp_egp=74.69 dxy=102.19 gold21_egp=6385 gold24_egp=7295 gold18_egp=5475 goldpound_egp=51080 gold_usd=4076 brent=113.88 egx30=49723.72 sp500=7743.98 nasdaq=26549.85 dow=52475.10 btc=81231 egx.COMI=120.30 us.AAPL=347.10
```

Also log, every day, with the same command:

- **Volume:** the `vol.TICKER` values fetch_figures.py prints for all 24 stocks (shares traded in the last
  finished session; it leaves out Egyptian volumes while the EGX is trading).
- **The central bank's dollar rate:** `cbe_usd_buy` and `cbe_usd_sell` at the latest close, checked in two
  outlets (Egyptian news sites publish it daily, for example Al-Masry Al-Youm and Akhbar El-Youm).
- **Policy rates:** `cbe_deposit` and `cbe_lending`, every day, so the log shows when they change.
- **EGX turnover:** `egx_turnover`, the session's value traded in stocks in EGP bn.
- **T-bill yields:** fetch_figures.py logs all four tenors (`tbill_91` … `tbill_364`) from the central bank's
  results on the first edition after each auction; never repeat an old auction's yields. The edition and the
  desk show only the one-year (364-day) yield, the benchmark for foreign investors' carry trade, with its
  auction date (Thursdays): for example `| Treasury bills | 26.08% (1-year, 29 Oct auction) | ... |`.

The weekly log check does not expect the rates and T-bill yields every day.

**Bonus shares and splits:** every run, after logging, run
`python3 .claude/skills/daily-newsletter/corporate_actions.py --check`. When an Egyptian stock in the log
has passed its ex-date (the first session without the right to the free shares), confirm the ratio in the
company's disclosure (Mubasher or Arab Finance, cross-checked against the reference price the script
estimates), then run `corporate_actions.py --apply TICKER EXDATE BONUS` once (BONUS is free shares per
share: 0.25 for one for every four) and refresh the spreadsheet. Without it, the charts show a fall that
never happened to holders and the changes and YTD figures come out too low. Cash dividends are not adjusted.

**Gaps:** every run, after logging, run `python3 .claude/skills/daily-newsletter/fill_gaps.py DATE 10 --write`.
It finds figures missing from the last ten entries although the entries around them have them, and fills each
from a dated source (Yahoo, Nasdaq or CoinGecko history; the desk's intraday file for Egyptian stocks; the last
weekday's pound rates for Friday and Saturday closes), printing every value beside its neighbours. Check any line
it marks as more than 8% from a neighbour, and fill the `MANUAL` lines it lists by hand with log_figures.py when a
source confirms the figure (or leave them, and say so in the final reply).

**The week behind the trend lines:** then run `python3 .claude/skills/markets-desk/fetch_intraday.py` (brings the desk's
intraday prices up to the last session, about a minute) and `python3 .claude/skills/daily-newsletter/week_snapshot.py DATE`.
It saves `data/weeks/DATE.json`, the last five sessions hour by hour for the desk's stocks and the indexes, which the
site draws as this edition's "Last 7 days" lines; commit it, and `desk/intraday.json`, with the edition.

Then refresh the spreadsheet copy, `data/markets.xlsx`, and commit it too:

```
python3 .claude/skills/daily-newsletter/export_xlsx.py
```

Log the same numbers the edition shows (the central bank's selling rate for the dollar when that is what
the table shows), one value per key, with every Stocks Watch row as `egx.TICKER` or `us.TICKER`. Leave out
anything marked n/a or unconfirmed. Log closing prices only, never live prices: if the
EGX is still trading when the run happens, log each Egyptian stock's previous close (Mubasher shows it on
the stock's page) and the EGX30's previous close instead of the intraday figures the table shows. A live price
stays in the log for good and skews every change, streak and YTD figure worked out from it. Weekend editions log what they show; the recap does not log. Commit
`data/markets.json` together with the edition.

## Listen (the edition read aloud)

The site's Listen button reads every edition aloud with the device's own voice; each daily edition and the recap
also get a recorded natural voice. Once the edition is final and checked, run
`python3 .claude/skills/daily-newsletter/make_audio.py EDITION` (EDITION is the file key, e.g. 2026-11-06). It
records the edition in the site's two natural voices, Heart and Michael (around 10 minutes, plus a few minutes the
first time to install the voice model; a voice already recorded from the same text is kept), publishes the
MP3 on the repo's `audio` branch (which holds only the last 8 editions' audio, a week plus the recap, and is rewritten each time: never
commit an MP3 to main) and writes `data/audio/EDITION.json`; commit `data/audio/` with the edition. If it prints
"Audio not made", go on: the site falls back to the device's voice, and say so in the final reply.
It also rewrites the two podcast feeds (`data/audio/feed-heart.xml` and `feed-michael.xml`, served at
/podcast/heart.xml and /podcast/michael.xml, with `data/audio/cover.png` as their artwork), which list the editions
the audio branch holds; they go in with `data/audio/`.

What it reads is `read_aloud.py`'s list: every section but Sources and the two watch tables, headings, paragraphs,
list items and Explained boxes, with figures written as they are said (EGP 54.01 as "54.01 pounds", 3.9% as "3.9
percent"). `listen.js` on the site builds the same list from the page to highlight the block being read; change
both together.

## Corrections

Before writing, compare the previous edition's key figures and facts against what is now known (the
checked sources and `data/markets.json`). If something published was wrong in a way that matters, such as
a figure, a name, a date or a result, add one item at the end of Quick Hits:
`**Correction:** Tuesday's edition gave the EGX30 close as 51,050; it closed at 50,105.` Keep it to one
sentence, plain and factual, and fix that day's entry in `data/markets.json` with `log_figures.py`. Do not
edit the earlier edition itself, and leave out trivial slips. This is the only place an edition may refer
to an earlier one.

## Other skills for work on this repo

These are general Claude skills, not part of this repo; use them when the task calls for it:

- **dataviz:** read it before adding or changing any chart on the site, such as the trend lines drawn
  from `data/markets.json`, so charts stay consistent in light and dark mode.
- **xlsx:** for anything beyond the automatic `data/markets.xlsx` export, such as a custom analysis
  workbook or charts in Excel.
- **code-review:** run it on changes to `index.html` or the scripts before pushing them.

In this repo, for the Markets Desk page (copied from Anthropic's equity-research plugin, Apache 2.0):
**morning-note** (what moved and why, with a view), **sector-overview** (what drives a sector),
**catalyst-calendar** (upcoming events that move stocks) and **thesis-tracker** (keeping each view
falsifiable and checking whether it played out).

Daily and recap runs do not need dataviz, xlsx or code-review.

## Edit pass, before the checker

When the edition is written, read it once from the top as its editor, not its writer, and fix what you find:

- **Leads:** each item's first sentence states the news with its figure. Rewrite one that opens on background, a
  date or a quote.
- **Why it matters:** an Egypt, economy or markets item whose point for a reader in Egypt is not plain gets one
  closing clause that says it (what it does to prices, the pound, jobs, a stock). Never a moral, never filler.
- **Against earlier editions:** for each continuing story, open the last edition that carried it (`grep -l` the
  name in `editions/`) and check that names, titles, counts and figures agree; where they differ, check the source
  and say what changed ("revised from 125").
- **Arithmetic:** recompute every percentage change, total and "highest since" from the figures in the text and the
  data log.
- **Glance and text agree:** each Today at a Glance line says what its story says, with the same figure.
- **Once only:** no story, figure or explanation appears in two sections; no "today" or "yesterday" that is wrong
  for the edition's date; no term left unexplained on first use.

Then run the checker. End the final reply with one line, `Edit pass: N changes`, naming the biggest.

## The front page

The site builds a front page for each daily edition from the edition itself (index.html, `buildFront`), so write
with it in mind; nothing extra goes in the file:
- **Today at a Glance item 1** is the lead: its sentence becomes the headline and its story's paragraph the text.
  Items 2 to 4 sit beside it with their story's first sentence; items 5 on are listed as "Also today".
  So write each glance line as a headline, not a sentence: 12 words or fewer, who did what with the number
  ("Remittances hit a record $38.2 billion in nine months"), and make every story's first sentence carry the news
  alone: the lead's first sentence is printed as its standfirst, under the headline.
- **Quick Hits** become four large figures. Open Number of the day and Stat to know with the figure and a period
  ("$13 billion. What Egyptians abroad..."), and Quote of the day with the quote in quotation marks, then the speaker.
- **The markets strip** (EGX30, USD/EGP, gold 21K, Brent, S&P 500) reads the data log, so log the figures before
  publishing; Cairo's temperature comes from the first Weather paragraph ("a high of 24-25°C").
The Today at a Glance and Quick Hits sections are hidden on the page (the front page shows them) but stay in the
file for the archive, search and audio. The Saturday recap has no front page.

## Check before committing

Run the checker on the new edition from the repo root:

```
python3 .claude/skills/daily-newsletter/check_edition.py editions/YYYY-MM-DD.md
```

It reports:

- **Errors** (exit code 1): missing or misordered section titles, missing Markets, Stocks Watch or In Other News parts,
  a top-level `#` title, HTML, a first line that is not an italic intro, a Today at a Glance item with no
  link or a link to an anchor that does not exist, a missing What to watch today line, or an
  `editions/index.json` that does not parse or has no entry for the date. Fix all of these before committing.
- **Figures and links** (also errors or warnings): each currency-table level and each EGX30, S&P 500, Nasdaq, Dow,
  Brent and Bitcoin level written in the text is compared with the data log for the date; a mismatch is a warning
  to fix the text or the log. Every Sources link is opened: a dead page (not found) is an error, to be replaced with
  a working link to the same story; links a site refuses to check are only counted. `--no-links` skips the link
  check when offline.
- **Warnings:** first-person words or names outside quotes, sections far outside their word budget, and
  bold lead-ins that look like the same story in two sections. Read each one and fix the real problems;
  some are false alarms (a quoted "we", "US" as a country). A word-count warning is information only:
  never cut a worthwhile story to clear it.

If a story is flagged as appearing twice, keep it in the section the rules above give it and remove it
from the other.
