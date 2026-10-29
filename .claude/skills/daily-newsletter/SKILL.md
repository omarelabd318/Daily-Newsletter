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
| Stocks Watch (two tables) | 100-180 | 5% |
| Currency and Commodities Watch | 110-160 | 5% |
| In Other News: Tech and AI | 130-170 | 5% |
| In Other News: Sports | 150-200 | 6% |
| In Other News: Health and Science | 70-100 | 3% |
| In Other News: Entertainment and Culture | 120-150 | 5% |
| Economic Calendar | 130-170 | 5% |
| Worth Knowing | 160-200 | 6% |

Sports is the deepest part of In Other News, but it no longer outweighs Markets. Global Markets got the
extra room: use it to explain what drives the moves and what they mean for Egypt and emerging markets.

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
  in a few words, but the figures and analysis live here.
- **Egypt News:** Egyptian government decisions and domestic stories. When Egypt acts on a regional
  matter (for example a parliamentary vote on a deployment), the Egyptian decision goes here and Regional
  and Gulf does not repeat it.
- **Stocks Watch:** two tables of figures only (see below). Markets keeps its own coverage, including
  stories about individual companies; Stocks Watch just lists the prices.
- **Currency and Commodities Watch:** figures and a short note for each row. No story narrative; the
  story behind a move belongs in Markets.
- **Economic Calendar:** upcoming events only, not news already covered above.

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

## Go-to sources for figures

Check these pages first for the figures below, then search as usual for anything they do not cover.
Every page here loaded with real content when tested from the cloud environment on 28 October 2026.
Sites change, so if a page fails or looks stale, use the backup or search, and say in the edition when
a figure could not be confirmed. These pages are for figures; news still comes from many outlets.

| Figure | First choice | Backup |
|---|---|---|
| US dollar index (DXY) | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=5d&interval=1d (fetch_figures.py gets it) | Search "dollar index" news for the day's level |
| EGP against USD, EUR, SAR, AED, KWD, QAR, GBP | https://open.er-api.com/v6/latest/EGP (JSON; rates are EGP per 1 unit when inverted; market mid-rates, not the central bank's official rate) | EnterpriseAM's edition, which usually quotes the central bank's dollar rate |
| Gold in Egypt (21K, 24K, 18K per gram) | https://egypt.gold-price-today.com/ (Arabic: عيار 21 is 21K) | https://www.goldpricez.com/eg/gram |
| EGX30 close and daily change | https://english.mubasher.info/markets/EGX/indices/EGX30 (close, change, open, high, low) | https://tradingeconomics.com/egypt/stock-market |
| Egyptian stock prices (Stocks Watch) | https://english.mubasher.info/markets/EGX/stocks/TICKER, for example .../stocks/COMI (price, change, % change, previous close, time of last update) | Search |
| US stock prices (Stocks Watch) | https://query1.finance.yahoo.com/v8/finance/chart/TICKER?range=5d&interval=1d (JSON: the last two values in indicators.quote[0].close give the latest close and the change; timestamp gives the date). Do not use Yahoo for Egyptian stocks; its EGX data is years out of date | Search |
| Central bank interest rates | https://tradingeconomics.com/egypt/interest-rate | EnterpriseAM's edition |
| Treasury bill yields | No page shows current yields. Search Arabic financial news for the latest auction, for example https://amwalalghad.com/?s=عائد+أذون or https://www.alborsaanews.com/?s=أذون (look for متوسط عائد, the average yield, by tenor). Results are not sorted by date: use only an auction from the last 7 days, and give its date | EnterpriseAM's edition, which reports some auctions; otherwise say the yield was not confirmed |
| Public holidays and bank closures | https://www.officeholidays.com/countries/egypt/2026 (verify any holiday shift against a news report of the official announcement) | Search |
| Cairo weather, today and next two days | https://wttr.in/Cairo?format=j1 (JSON: daily max and min °C) | Search |
| Egyptian football | https://www.kingfut.com/ (English) | https://www.kooora.com/ (Arabic) |
| European football results | https://www.bbc.com/sport/football/scores-fixtures/YYYY-MM-DD (use the date of the matches) | https://www.espn.com/soccer/scoreboard |
| Tennis | https://www.bbc.com/sport/tennis | https://www.wtatennis.com/scores |

These block automated access from the cloud environment, so do not spend time on them: the Central
Bank of Egypt site (cbe.org.eg), the Egyptian Exchange site (egx.com.eg), Ahram Online, Egypt Today,
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

After the fixed rows, add up to three rows for other stocks with a notable move or notable news that
day, marked in italics, for example `| *Ezz Steel (ESRS), notable mover* | 98.50 | +8.5% | n/a |`.
Leave them out when nothing stands out.

On weekends the EGX is closed Friday and Saturday and US markets Saturday and Sunday. Show the last
session's close with its date. On EGX holidays, listed in `data/holidays.json`, do the same and say why in
the italic line, for example `*EGX closed today for Sham el-Nessim; last close Sunday 2 May*`, and log
the figures as usual (the last close again). The checker warns when a listed closure is not mentioned. If a price cannot be confirmed, write `n/a` rather than guessing.

The checker compares every Stocks Watch row with the data log: the close with what was logged for the
date, and the change with the move from the previous logged close (from the previous close to the live
price for an intraday table). A warning there means one of the two figures is wrong: recheck both at the
source and fix the table or re-run log_figures.py before publishing.

## Egyptian holidays

`data/holidays.json` lists the public holidays that close the EGX. Use it in Today at a Glance's What to
watch line and the Economic Calendar (upcoming closures and long weekends). Dates marked `expected` are
projections, so always confirm them against current official announcements; when the Cabinet or the EGX
announces dates, update the file (dates, any day moved to a Thursday or Sunday, and `"status":
"confirmed"`) and commit it with the edition. When a new year's holidays are announced, add them.

## Currency and Commodities Watch table

Use three columns: `| Item | Level | Note |`. Keep each Note under about 10 words, so the table stays
easy to scan. On phones the site shows each row as a small card, so long notes still fit.

Right after the USD/EGP row, add `| US dollar index (DXY) | 102.19 | ... |`: the dollar against six major
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
- **Length:** about 1,850 to 2,150 words, an 8 to 9 minute read. A guide, not a limit.
- **First line:** an italic sentence with the week's dates and what it was about, for example
  `*Week of 25 to 31 October 2026: a rate hold, a weaker pound and Egypt's Saudi deployment vote.*`
- **Sections,** in this order, each as `##` with exactly these titles:
  1. **The Week in Brief:** a numbered list of 7 to 10 of the week's biggest stories, Egypt first, each
     `**Label:** one sentence`. No links.
  2. **Egypt This Week:** 4 to 6 items on the main Egyptian stories, each with where it stands now.
  3. **Region and World:** 4 to 6 items, regional first, then the rest of the world.
  4. **Markets This Week:** a short paragraph on the week, then a table
     `| Item | Week close | Weekly change |` covering EGX30, USD/EGP, gold 21K per gram in Egypt, Brent,
     S&P 500, Nasdaq and Bitcoin, then one line each on the week's best and worst EGX30 stocks if known.
  5. **Sports This Week:** the week's main results and stories as separate items, Egyptian football first,
     with no sport headings.
  6. **Culture and Tech:** 3 to 5 short items from tech, AI, entertainment and culture.
  On the first Saturday of a month, add **Month in Numbers** right after Markets This Week: one line on
     the month, then a table `| Item | Start of month | End of month | Change |` for EGX30, USD/EGP, gold
     21K, Brent, S&P 500 and Bitcoin, taken from the first and last entries of the previous month in
     `data/markets.json` (say "not logged" where a figure is missing).
  In the last Saturday recap of December, also add **Year in Numbers** right after Markets This Week (and
     after Month in Numbers if both appear): one line on the year, then the table that
     `python3 .claude/skills/daily-newsletter/market_facts.py DATE --year` prints, then one line each on
     the year's best and worst stocks from that table.
  7. **How It Played Out:** go through the What to watch today lines in this week's daily editions and
     pick the 4 to 6 events that mattered most (a rate decision, a vote, a data release, a big match).
     For each, one item: what was expected and what actually happened, for example
     `**Central bank meeting:** Expected to hold; it held rates at 22% and signalled cuts in December.`
     Skip anything already covered in full above; say "postponed" or "no decision yet" where that is the
     case. Do not mention the daily editions themselves.
  8. **The Week Ahead:** the key scheduled events for the coming week (central bank meetings, data,
     holidays and closures, big matches).
  9. **Sources:** the links used.
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
python3 .claude/skills/daily-newsletter/log_figures.py DATE usd_egp=56.20 eur_egp=62.57 sar_egp=14.99 aed_egp=15.30 kwd_egp=181.19 qar_egp=15.41 gbp_egp=74.69 dxy=102.19 gold21_egp=6385 gold24_egp=7295 gold18_egp=5475 goldpound_egp=51080 gold_usd=4076 brent=113.88 egx30=49723.72 sp500=7743.98 nasdaq=26549.85 btc=81231 egx.COMI=120.30 us.AAPL=347.10
```

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

Daily and recap runs do not need any of these.

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
- **Warnings:** first-person words or names outside quotes, sections far outside their word budget, and
  bold lead-ins that look like the same story in two sections. Read each one and fix the real problems;
  some are false alarms (a quoted "we", "US" as a country). A word-count warning is information only:
  never cut a worthwhile story to clear it.

If a story is flagged as appearing twice, keep it in the section the rules above give it and remove it
from the other.
