---
name: daily-newsletter
description: >-
  House rules for writing an edition of the Daily Newsletter in this repo (editions/YYYY-MM-DD.md):
  word budget per section, which section each kind of story belongs in, and a checker to run before
  committing. Use whenever writing, editing or reviewing a newsletter edition here.
---

# Daily Newsletter house rules

**How the run works (read first): batch, bring in less raw text, and research in side sessions.** Every step of a
run pays again for everything already open, so (1) put independent actions in one step: several queries per
`search.py` call (news research goes through it first: four pages' excerpts a query, about 400 words, logged by
itself; web search and full page reads for data pages and what its excerpts do not settle), several pages per
`articles.py` call, several queries or URLs per research_log.py call, a whole section per Write or Edit, each checker
once per pass, and no file read twice; and (2) after
choosing the day's stories, do the research in five side sessions (sub-agents, started together in one step) that
read the pages, confirm the figures at a second outlet and return short notes, and write the edition from the notes.
`refs/research-agents.md` has the blocks, the prompt to give each one and the notes format: read it before
researching. The research itself is unchanged: the same searches, outlets and checks, and the main run still chooses
the stories, writes every word and opens any page a note leaves unclear. The task prompt's instructions to read
EnterpriseAM and CairoScene are met by the Egypt side session, which reads them in full.

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
| Quick Hits | 90-130 | 3% |
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

**Company results:** the percentage change must match the two figures it compares, and the year-earlier figure
must come from the company's filing or a second outlet, not one report. Outlets sometimes take the wrong base (on
November 12, 2026 Mubasher compared Telecom Egypt's profit with EGP 12.98bn instead of 16.97bn and reported +88%
for a 43.7% rise). Use profit attributable to shareholders, and say so.

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

## Quick Hits: the same four every day

Quick Hits has exactly these four items, in this order, every day (the front page shows them as a band of four; a
missing one leaves a hole, and before November 12, 2026 only the first was required, so Stat to know came and went):
`**Number of the day:**`, `**Quote of the day:**`, `**This day in history:**` and `**Stat to know:**`. Stat to know
is a second figure from a different story than Number of the day, one that explains something rather than
surprises: a rate, a share, a count, a comparison ("825 million. The number of shares..."). A correction, when
there is one, is a fifth item after them. The checker fails an edition missing any of the four.

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
after a gap, such as a failed run, that may be two or more days old) as a digest:
`python3 .claude/skills/daily-newsletter/week_digest.py --edition editions/YYYY-MM-DD.md` (its glance, and each
story's lead-in and first sentence: about half the words). Use it only to tell which stories are new and which are
continuing; the brief's running topics already carry what the last edition said with its figures. Then:

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
prints). `search.py --log DATE newsletter` logs its queries as searches and its pages as read, by itself. Pages the
scripts read for you (run_research.py's editions/articles.md, articles.py, search.py) are logged by them
separately, as "read by scripts", and do not count as pages you opened. A full edition takes at least 25 searches
across many outlets and 12 pages you opened yourself (to confirm a figure at a second outlet, or to read past an
excerpt), on top of the scripts' reading (usually 20 or more); the checker warns below that and blocks publishing
below half of the searches and pages.

**Reading excerpts.** Two pages the reader marks as having the same wording are one release copied by two outlets:
they count as one source, never as the second outlet that confirms a figure. When an excerpt ends with "Figures on
the page: standalone; consolidated ..." (or nine months and the quarter), the page gives more than one basis: say
which one each figure is, and for results use the consolidated profit attributable to shareholders unless the
story is about the other. The log is the honest record of the work: never log a search or a page that
was not made. End the final reply with the line `research_log.py DATE newsletter summary` prints.

## Attribution in the text

When you write the sources into the text and the Sources list, read `refs/attribution.md` first (once, at that point,
not before). In short: credit the outlet that reported a fact the first time it matters, never more than the
checker allows; EnterpriseAM and CairoScene are trusted sources among several, not the backbone of a section;
paraphrase, never copy; every story's links go in Sources.

## Start from the brief

Before any search, run `python3 .claude/skills/daily-newsletter/run_research.py` (about 20 seconds) and read
`editions/brief.md`. It gathers, and never judges: the day's headlines from every Egyptian outlet below, with the
stories two or more of them carry listed first; for each running topic, where it stood, what the last edition said
with its figures, and today's headlines on it; the last edition that carried each topic, in full; yesterday's What to watch today, to
follow up; scheduled data (US and Egyptian releases just out and due, with actual, forecast and previous, and how old
each official figure in the data log is, flagged when a newer one is probably out); the dates already known for the
next three days; for desk stocks reporting now, the SEC's filings and filed figures (US) or Mubasher's results
headlines with the article's figures (Egypt); regional outlets and
wires on Egypt, the Gulf, the economy, sports, culture, and the world, business and technology top headlines; and
which outlets it could not reach. Use it to choose what to research, not as research: every line is a headline
with no link, so open the story at its outlet, check it against a second one, and log it with research_log.py as
usual. A story the brief shows in several outlets still needs reading; a story it does not show may still matter
(it sees headlines, not front-page placement). An outlet listed as unreachable is read by hand.

**Then read `editions/articles.md`** (written by the same command): the likeliest stories already read at their outlets
(about 30: those several outlets carry, with a second outlet for the top ones, the running topics, and the first
economy, region, wire, sports and world headlines), each with its link at the outlet and its opening and figures.
Write from these where they are enough, and open a page only for what an excerpt leaves out, a figure to confirm at a
second outlet, or a story it lists under "Not read". To find more on a story, or a second outlet, run several
queries at once with `python3 .claude/skills/daily-newsletter/search.py --log DATE newsletter "q1" "q2" ...` before
any web search. To read pages, pass several at once to
`python3 .claude/skills/daily-newsletter/articles.py --log DATE newsletter URL URL ...` (one step of the run instead
of one per page; `--full` for a whole article) rather than opening them one by one. The file is a
worksheet and is not committed.

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

`fetch_figures.py` and the brief cover most figures. For one they do not give, or to confirm one, the list of tested pages for each figure (with backups) is in `refs/sources.md`: open it then, not before.

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

Read `refs/tables.md` when you build the Stocks Watch tables (the fixed lists, columns, formats and extra rows).

## Egyptian holidays

`data/holidays.json` lists the public holidays that close the EGX. Use it in Today at a Glance's What to
watch line and the Economic Calendar (upcoming closures and long weekends). Dates marked `expected` are
projections, so always confirm them against current official announcements; when the Cabinet or the EGX
announces dates, update the file (dates, any day moved to a Thursday or Sunday, and `"status":
"confirmed"`) and commit it with the edition. When a new year's holidays are announced, add them.

## Currency and Commodities Watch table

Read `refs/tables.md` when you build the table (rows, notes, YTD column and formats).

## Weekly Recap (Saturdays)

Saturday's separate recap run only: read `refs/saturday.md` in this folder first and follow it. Daily runs skip it.

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

The spreadsheet copy, `data/markets.xlsx`, is rewritten by GitHub Actions after the push (the "Audio and chores"
workflow, `export_xlsx.py`): do not run it in the run.

Log the same numbers the edition shows (the central bank's selling rate for the dollar when that is what
the table shows), one value per key, with every Stocks Watch row as `egx.TICKER` or `us.TICKER`. Leave out
anything marked n/a or unconfirmed. Log closing prices only, never live prices: if the
EGX is still trading when the run happens, log each Egyptian stock's previous close (Mubasher shows it on
the stock's page) and the EGX30's previous close instead of the intraday figures the table shows. A live price
stays in the log for good and skews every change, streak and YTD figure worked out from it. Weekend editions log what they show; the recap does not log. Commit
`data/markets.json` together with the edition.

## Listen (the edition read aloud)

GitHub Actions records it after the push (`.github/workflows/publish.yml`, "Audio and chores": make_audio.py in both
voices, the podcast feeds, then a commit "Newsletter DATE: audio", about 15 minutes): **do not run make_audio.py to
record**. Before the push, when the edition has names the voice may say wrong, run `make_audio.py --names EDITION`
and fix them in pronounce.json (refs/listen.md), and commit pronounce.json with the edition: Actions reads it. If
the edition text changes after the push, push the fix: Actions records again (voices with unchanged text are kept).

## Corrections

Before writing, compare the previous edition's key figures and facts against what is now known (the
checked sources and `data/markets.json`). If something published was wrong in a way that matters, such as
a figure, a name, a date or a result, add one item at the end of Quick Hits:
`**Correction:** Tuesday's edition gave the EGX30 close as 51,050; it closed at 50,105.` Keep it to one
sentence, plain and factual, and fix that day's entry in `data/markets.json` with `log_figures.py`. Do not
edit the earlier edition itself, and leave out trivial slips. This is the only place an edition may refer
to an earlier one.

## Other skills for work on this repo

For work on the site itself rather than an edition, `refs/other-skills.md` lists the general skills to use.

## Edit pass, before the checker

When the edition is written, read it once from the top as its editor, not its writer, and fix what you find:

- **Leads:** each item's first sentence states the news with its figure. Rewrite one that opens on background, a
  date or a quote.
- **Why it matters:** an Egypt, economy or markets item whose point for a reader in Egypt is not plain gets one
  closing clause that says it (what it does to prices, the pound, jobs, a stock). Never a moral, never filler.
- **Against earlier editions:** for each continuing story, find the last edition that carried it and read only
  that story (`grep -n -A3 "Name" editions/*.md | tail`, not the whole file) and check that names, titles, counts and figures agree; where they differ, check the source
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
  alone. The lead story's first sentence is printed as its standfirst, under the headline, with the rest in two
  columns: keep that sentence to 20 words or fewer ("Egypt's foreign minister gave the first official confirmation that
  Egyptian forces are in Saudi Arabia."), and put the detail in the sentences after it.
- **Quick Hits** become four large figures. Open Number of the day and Stat to know with the figure and a period
  ("$13 billion. What Egyptians abroad..."), and Quote of the day with the quote in quotation marks, then the speaker.
- **The markets strip** (EGX30, USD/EGP, gold 24K, Brent, S&P 500) reads the data log, so log the figures before
  publishing; Cairo's temperature comes from the first Weather paragraph ("a high of 24-25°C").
The Today at a Glance and Quick Hits sections are hidden on the page (the front page shows them) but stay in the
file for the archive, search and audio. The Saturday recap has no front page.

## The lead image (paper mode)

Read `refs/lead-image.md` at the step where you choose the lead image (licenses, captions, `lead_image.py`).

## Puzzles (every edition)

Read `refs/puzzles.md` at the puzzles step (`puzzles.py make`, clues, check), every edition.

## Check before committing

Read `refs/check.md` before running check_edition.py (what it checks, which warnings to fix, which are information).
