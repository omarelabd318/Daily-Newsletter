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

## Go-to sources for figures

Check these pages first for the figures below, then search as usual for anything they do not cover.
Every page here loaded with real content when tested from the cloud environment on 28 October 2026.
Sites change, so if a page fails or looks stale, use the backup or search, and say in the edition when
a figure could not be confirmed. These pages are for figures; news still comes from many outlets.

| Figure | First choice | Backup |
|---|---|---|
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

Columns: `| Stock (ticker) | Close | Change |`, with the price in EGP or USD and the change as a
percentage with a sign, for example `+1.2%`.

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
day, marked in italics, for example `| *Ezz Steel (ESRS), notable mover* | 98.50 | +8.5% |`.
Leave them out when nothing stands out.

On weekends the EGX is closed Friday and Saturday and US markets Saturday and Sunday. Show the last
session's close with its date. If a price cannot be confirmed, write `n/a` rather than guessing.

## Currency and Commodities Watch table

Use three columns: `| Item | Level | Note |`. Keep each Note under about 10 words, so the table stays
easy to scan. On phones the site shows each row as a small card, so long notes still fit.

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
- **Length:** about 1,700 to 2,000 words, a 7 to 8 minute read. A guide, not a limit.
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
  7. **The Week Ahead:** the key scheduled events for the coming week (central bank meetings, data,
     holidays and closures, big matches).
  8. **Sources:** the links used.
- Every item opens with a bold lead-in, as in the daily edition. Never refer to the daily editions
  themselves ("as reported on Tuesday"): write about the events and their dates.

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
