---
name: markets-desk
description: House rules for the Markets Desk, the daily markets analysis page planned next to the Daily Newsletter (what moved and why, which EGX sectors it helps or hurts, the desk's 39 stocks, the week ahead, open views). Use whenever writing, designing or reviewing the desk.
---

# Markets Desk

Status: written every day by the newsletter's scheduled runs, after the edition is published (see Daily run).
The first desk is 30 October 2026.
These are the rules agreed so far; add to them as the desk is finished.

## Daily run

**Batch, bring in less raw text, and research in side sessions.** As in the newsletter: news research through
`daily-newsletter/search.py --log DATE desk` first, several queries per call (web search and full pages for data
pages, filings and what its excerpts do not settle); several page reads, log lines and file reads per step, no file
read twice, a whole section per Write or Edit, each checker once per pass. Read the brief without its per-stock
news leads (`sed '/^## News leads by stock/,$d' desk/brief.md`; the stocks session reads them). Once the brief is read, start the two side sessions in
`refs/research-agents.md` together in one step (Stocks: results to record and the per-stock research, writing
desk/stocks.json; Markets and macro: notes only), and write the desk from their notes. Read that file before the
research starts.

The desk has its own scheduled run, about 45 minutes after the newsletter's, so a desk problem never holds up
the edition and the desk gets a full session to itself. Start from the day's research: pull the repo and read
the parts of today's edition the desk uses with `python3 .claude/skills/markets-desk/edition_for_desk.py DATE` (in
full: Today at a Glance, both Markets parts, Stocks Watch, the currency table and the calendar; the first sentence of
each Egypt, region, world and tech story; on a Saturday the whole recap), its figures already checked and logged.
Open `editions/DATE.md` itself only for a story you need in full or its links; if it is not there yet,
check again every few minutes for up to half an hour, then research the markets yourself. Add your own searches
for anything the desk needs beyond the edition (the stock research below, flows, movers' reasons), with search.py first. Do not write
or change the newsletter, and do not log figures the edition already logged. On days with no session (Friday and Saturday for the EGX, Saturday and Sunday for the US) the
closes are the last session's; the news, stock research and analysis are still updated.

**Saturdays (from November 14, 2026) are a lighter run.** There is no Saturday edition: start from the Weekly Recap
(`editions/DATE-recap.md`, which also logs Saturday's figures) and Friday's edition. The job is Friday's Wall Street
session (the USA section, its stories, movers and the US stocks that moved) and the week's figures. The EGX last
traded on Thursday and Friday's run already covered it: carry the Egypt section over from Friday, updating only what
changed (news since Friday, a view due, results published on Friday or Saturday), and skip the per-stock research for
Egyptian stocks unless one has news. The research floor is 10 searches and 5 pages opened on a Saturday.

1. Copy the newest `desk/days/*.json` as a template to `desk/days/DATE.json` (DATE is the edition date) and
   rewrite every part for today: set `date`, `asOf` (the latest close, the day before DATE on a trading
   day), `fetched`, and remove `"sample": true`. The close card figures come from today's logged figures. Egypt's group lists the EGX30, the EGX70 EWI, USD/EGP and gold 24K
   per gram (24K, not 21K: the dashboard's Gold in Egypt card has 21K, 18K and the gold pound).
2. Do the stock research below from the news leads in `desk/brief.md` (step 5 runs stock_news.py; do not run it
   again); update `desk/stocks.json`.
3. Write each section: finding (the page shows its first sentence in bold, so make that sentence the day's
   point; at most two more, about 50 words in all; the coming dates go in the week ahead, not here; `next` is no
   longer shown), three to five stories (`calls`), winners and losers (`board`), the Stocks note,
   the week ahead and open views, then update `desk/views.json` (see Views: the record): new entries, news, and judgements.
4. Write `pages`: EGX (finding, session, news, outlook), EGP (finding, rates, drivers, news, view), US
   (finding, rates: the day's extra items only, see step 5; afterBell, news, outlook), Global (finding, notes, news). Carry each projection
   forward until its date, and score it when the date passes.
5. **Start with `python3 .claude/skills/markets-desk/wait_desk_data.py DATE`** (it waits up to 9 minutes in one
   step for the edition and for GitHub Actions' desk data, then pulls): GitHub Actions runs run_data.py as soon as the
   edition is pushed and commits desk/brief.md. On READY read `desk/brief.md` up to its per-stock news leads (the
   `sed` line above; the stocks session reads those) and rerun only the steps it lists as
   FAILED (`run_data.py NAME`; the brief keeps the others). On WAITING run it again (30 minutes in all for the
   edition). On NO DESK DATA **run `python3 .claude/skills/markets-desk/run_data.py` once, then read
   `desk/brief.md`**. It runs every fetch and
   calculation below in order (intraday, rates, valuation, movers, calendar, indicators, fair value, judging the
   views, the stock news leads and the movers' leads), each with a time limit, over one shared fetch layer
   (`sources.py`: retries, pacing between requests, a short shared memory so the same table is not fetched twice). A
   step that fails is reported and the rest carry on; rerun one with `run_data.py NAME`. Do not run the scripts one by
   one or read their output: the brief has what each did, which sources were flaky, what moved, the movers that still
   need a reason with their leads, every stock's news leads, results and events in the next seven days (and which
   need a preview), views due or judged without a lesson, what changed in the fair values, and the standing jobs due
   today. Work from it. It is a worksheet, not a page: nothing links to it and it is not committed (.gitignore). What each script does, for when one fails or its output needs judging, is in `refs/data-scripts.md` (read it
   then, not every run). The rules from it the writing needs: `pages.us.rates` holds only the day's extra items (a
   data release, Fed odds, a central bank decision), never the VIX or yields, which the page shows from
   desk/rates.json; mention a standout mover from outside the desk's stocks in the stories or News when there is a
   reason behind it; quote moving averages, RSI and MACD as description ("below its 200-day average"), never as a
   forecast or the only reason for a view. **Movers' reasons:** for the top five each way in both markets (the
   brief's "Movers that still need a reason", with their leads), find why each moved (a disclosure, results, a deal,
   a rating, a sector move), check it at the outlet, and add `why`, `source` and `url` to that stock's row in
   `desk/movers.json`: one short line, left out when no reason is found, and "No company news found." only for moves
   of 5% or more. Never guess a reason. check_desk.py warns about any top-five mover of 5% or more left without one.
6. Add the session's flows to `desk/flows.json` when the EGX traded, and the date to `desk/index.json`
   with a one-line summary. When the central bank has published a new month of reserves (about the 7th;
   `fetch_figures.py` shows a new `reserves_usd`), add that month to `desk/reserves.json`: total, foreign
   currencies, gold and `sdr` (the rest: total minus the other two), from the bank's release or a news report
   of it that gives all three (Daily News Egypt, Arab Finance, Egypt Today), with `source` and `url`.
7. Run `python3 .claude/skills/markets-desk/check_desk.py`, fix every ERROR, then commit and push as for
   the edition (message `Desk DATE`).
8. The spoken summary is recorded by GitHub Actions once the desk is pushed (`.github/workflows/publish.yml` runs
   desk_audio.py DATE and commits `Desk DATE: audio`): do not run it in the run.

## The desk's stocks

21 Egyptian: the newsletter's 12 Stocks Watch names (CIB, Talaat Moustafa, Telecom Egypt, Palm Hills,
Elsewedy, Orascom Construction, Fawry, Abu Qir, EFG Holding, Cleopatra, Juhayna, Alexandria Containers)
plus MOPCO, Eastern Company, e-finance, Emaar Misr, Banque du Caire (trading from 2 November 2026), Egypt
Aluminium, Alexandria Mineral Oils, Sidi Kerir Petrochemicals and Edita Food Industries.
18 US: the 12 Stocks Watch names plus Visa, Oracle, Costco, Netflix, Intel and Eli Lilly (the last three added
November 11, 2026, with their history back to 2021). The extra 15 are desk-only: they are
logged daily (fetch_figures.py lists them as "Desk only") but are not rows in the newsletter's tables.

## Pages

What each page shows and where it lives is in `refs/pages.md`. A daily run writes data, not pages: open it only when changing a page or checking where something appears.

## Files

What each file under desk/ holds and who writes it: `refs/files.md` (read it when you need to change a file you have
not changed before).

## What it is

A daily page of well-informed market analysis for one reader in Cairo who knows finance: terms such as
basis points, T-bills, YTD and P/E need no explanation. The newsletter says what happened; the desk says
what it means for Egyptian markets and the reader's stocks. It is published every day, from the same run
and the same research as the newsletter.

## Two sections

The desk has two sections, each with its own dashboard page (`/desk/egypt/`, `/desk/usa/`): **Egypt** (the EGX, the pound,
Egyptian gold and rates, the desk's Egyptian stocks) and **USA** (US markets and the desk's US stocks; its close
card lists the S&P 500 first, then the Nasdaq and the Dow Jones). Both close
cards also carry a Global group: oil, gold in dollars, the dollar index and Bitcoin. Each has its own top call, winners and losers, stocks, week ahead
and open views. A story goes in the section whose markets it moves; a global story that clearly reaches
Egypt goes in both, told from each side.

## The top call: Egypt first

In the Egypt section, the top call is the one story that matters most for **Egyptian markets and the
reader's Egyptian stocks**. In USA, it is the story that matters most for US markets and the
reader's US stocks.

- **A global story leads only when it clearly reaches Egypt**, through a channel the call names: oil
  prices, US interest rates and the dollar, money flowing in or out of emerging markets, Gulf investment,
  or Suez and Red Sea traffic. A big move abroad with no such link is not the top call, however large it
  is (for example, Alphabet falling 12.6% on its results: the EGX30 rose the same day).
- **Global stories still have a place**: in the USA section, where such a story can be the top
  call (Alphabet's fall was). When it does not reach Egypt, the Egypt section leaves it out.
- **Prefer the story that ties the day together**: the pound, the EGX30's move and who was buying, the
  central bank, rather than the loudest headline.

## Three to five stories

The dashboard shows the top call in full (above), then up to four more as compact cards under "Also today":
headline, the one-sentence `line`, the tags, and the body, view and wrong-if behind a tap. Aim for three to
five: each extra story must move markets or the reader's stocks in its own right and is written like the top
call (below). On a quiet day fewer is right; never pad with a thin story to reach five.

## Tags: what a story moves (`affects`)

Stories and news items carry `affects`, a list of tags drawn as chips (desk/tags.js):
`{"kind": "sector" | "stock" | "market", "name": "Banks", "dir": "up" | "down" | "mixed", "t": "COMI", "chg": 2.5}`.

The EGP page's own view (`pages.egp.view`) carries `affects` the same way, in place of a `moves` sentence.

- **Sector first**, then the stocks most exposed, then markets (`EGX30`, `Pound`, `Brent`, `T-bill yields`,
  `Rate-cut odds`). Two to eight tags on a story, one to four on a news item.
- **Any stock, not only the desk's**: name the companies the story is about or most exposed to, with `t` for
  their ticker. A desk stock links to its page (its `name` can be left out); others show as plain chips.
  Never tag a desk stock just because it is on the desk's list.
- `dir` is the story's effect on it (up, down or mixed), not necessarily the day's move. `chg` is the % change
  the source gives for the session, only when it does (the page never fills it in).
- On a news item, tag only what the headline or text names (check_desk warns otherwise); a story's tags may
  add the stocks most exposed, as the view argues.

## How a call is written

Follow the morning-note skill in this repo (lead with the one thing that matters, always take a view,
"no news" is a valid answer). Every call, in the top call and on the winners and losers board, has:

- **what happened**, in figures, from checked sources;
- **the view**: a plain statement, kept apart from the facts;
- **what it moves**: the sectors first, then the stocks most exposed and the markets (`affects`, above);
- **wrong if**: what would show the view is wrong, specific enough to check (thesis-tracker skill);
- **a confidence level**: high, medium or low. "Momentum, not news" or "no company news found" means low.

Never present an unconfirmed claim as fact. A claim from a single source goes in a notice under the call
("reported by one source, not confirmed; the view does not rely on it"), and the view is written without it.

## Winners and losers

Two short lists, helped and hurt: EGX sectors or stocks, each with its driver, one line of reasoning
grounded in real figures, and a confidence level. They come from the whole day's news and moves, not only
the top call, over the next one to four weeks (the dashboard card is titled "Winners and losers"). Use the sector-overview skill for what drives a sector.

## Who bought and who sold

In the Egypt section, a card with the EGX's net equity flows for the latest session by investor group
(Egyptian, Arab and foreign; institutions and individuals), in EGP bn, from the EGX's daily report as
carried by Mubasher, EnterpriseAM, Youm7 or Arab Finance. Check the six figures against a second report
and that they net to about zero; until they match, set `"confirmed": false` with the source named. Reports
can disagree: check each against the session's turnover and investor shares (Egyptian, foreign and Arab
percentages of trading), and reject one whose buying and selling add up to more than the session traded.
Name the agreeing outlets in `sub`. Say in
one line what drove them, and flag a day distorted by an offering or block trade (as 29 October was by
Banque du Caire's), so the reader does not read it as a vote on the market. Never write who bought or
sold elsewhere on the desk without these figures behind it.

## Bullish and bearish

On the EGX and US pages, after the stocks table: the sectors and stocks the desk expects to rise or fall
over the next one to three months.

- **Sectors:** a name, a confidence level and one or two sentences on the driver, with real figures.
- **Stocks:** a projected price range and a date (for example `EGP 128–132 by end of December`), the
  reasoning, what would prove it wrong, and a confidence level. Ground the range in figures from the data
  log (the 50-day average, the 52-week high or low, a recent level) and in checked news; never a round
  guess. The page works out the percentages from the latest close.
- **Confidence:** high when several independent reasons and the figures agree; medium for a clear driver
  with cross-currents; low for momentum or a single reason. Say low when it is low.
- **Scoring:** every projection is kept until its date passes and then marked right or wrong against the
  data log, on the stock's page and on the Views page, like any other view. Only list stocks with a real case;
  an empty side is better than a filler pick.

## News

The EGX, EGP, US and Global pages each have a News card: the day's stories for that market, two to six,
each with a headline, one or two sentences in figures, `affects` (tags, above), an `impact`, the outlet and a
link to the story's own page. Take them from the newsletter's research and from the stock research below.

- **Headline:** who did what, with the number, in 12 words or fewer: "Pharma and food stocks lead a 2.8%
  EGX30 jump; locals sell", not "EGX30 jumps 2.8% to 50,650 as local investors sell". Lead with what the
  reader's money cares about.
- **Affects:** one to four tags for what the story names; a desk stock tagged with `t` also shows the story on
  its page.
- **Impact** on every item: `"bullish"`, `"bearish"` or `"mixed"`, for the market the page covers (the EGX and
  Wall Street pages: the stocks it names, or the market; EGP: the pound and rates; Global: oil, gold and world
  markets). Judge the effect on the price, not whether the news is good in general (a strong economy that brings
  rate-hike bets is mixed).

## Results days

The stocks side session reads `refs/results.md` and does this work (previews, reading the filing, `lastResults`,
set_results.py for every desk stock that reported, from the brief's "Results to record" list). Read it yourself
only when you do that work in the main run.

## Stock research, every day

The stocks side session reads `refs/stock-research.md` and does this work (judging each lead from its excerpt, a
second outlet for what moves a stock, `news` in desk/stocks.json, one research-log line per stock, the calendar).
The research floor still holds for the whole run: at least 15 searches and 8 pages opened beyond the edition (10 and
5 on a Saturday), side sessions included; every desk stock that moved 3% or more or has a lead gets a stock line.

## The desk's note on a stock

`brief` in `desk/stocks.json`, shown on the stock's page as "The desk's note": the standing view of the company, as
opposed to the day's news. `{"written", "business", "drivers": [{"name", "text"}], "value", "risks": [...], "change"}`:
- `business`: what it is and how it makes money, in two sentences with its key figure.
- `drivers`: the three or four things that move its profit, each with the latest figure the desk has checked.
- `value`: its multiples and the desk's fair value, in two sentences, with the catch.
- `risks`: three, specific to the company.
- `change`: what would change the desk's view, something that can be observed (a results date, a figure, a decision).
Only facts already checked for the desk (its news, results, valuation card and fair-value table) or checked now at
the source; no figure from memory. All 21 Egyptian stocks had one by November 11, 2026; the 18 US stocks do not yet. Write two US notes each Sunday
until every desk stock has one, then rewrite a
stock's note on the day it reports and whenever it is three months old.

## The week ahead

The events that can move Egyptian markets and the reader's stocks, each rated high, medium or low impact,
with one line on why it matters (catalyst-calendar skill). Dates are checked like any other fact. Rate impact
the same way every day (the dashboards print this key under the card):
- **High:** could move the whole market on the day: the EGX30, the pound or the S&P 500. Central bank decisions
  (the CBE, the Fed), inflation, jobs and GDP releases, the IMF review, a results day for one of the market's
  largest companies (CIB, Nvidia, Apple), and a large state offering or auction that sets rates.
- **Medium:** could move a sector or a few stocks: other desk stocks' results, a sector's data (fertilizer gas
  allocations, oil inventories), a T-bill auction with no expected change, a company's general assembly or
  dividend date.
- **Low:** worth knowing but unlikely to move prices much: minor data, conferences, scheduled speeches with
  nothing new expected, holidays (rate a closure that shuts the market for several days medium).

## The week

`/desk/week/` (The week, in the menu) builds itself from the files the desk already keeps: the markets' moves over
seven days, each day's top calls, the weekly movers, the foreign flows, the views judged that week and next week's
dates. It needs no writing; it is only as good as those files, so keep flows.json, movers.json, views.json and
calendar.json current every day.

## Views: the record

`desk/views.json` holds every view and projection the desk has made, shown on the Views page
(`/desk/views/`) and on each stock's page. Each entry: `id` (date and a short slug), `opened`, `market`
(egx, egp, us or global), `kind` (view or projection), `title`, `detail`, `wrong`, `confidence`, `due`
(the date it is judged by, or null), `track` (the figure it rests on: `key` such as `egx.COMI`, `usd_egp`
or `brent`, its `start` value, and for projections the `target` range and `side`), `tickers`, `status`
and `updates`.

Every day:

1. **Add** each new view and projection the day's desk makes (the open views and the Bullish and bearish
   stocks), with its start figure from the data log. A projection carried over from an earlier day is the
   same entry, not a new one.
2. **Add news** that bears on an open entry to its `updates`: date, one line, source, url, and `effect`
   (supports, against or neutral). Take it from the day's research and the stock research; only news
   checked at the outlet. The same story can go on several entries.
   **Confidence moves with the news.** When an update changes how likely the call now looks, give it a
   `confidence` (the new level, one step at a time: low, medium, high); the update's text is the reason, so say
   why in it ("the CBE held rates, removing the main risk"). Change it for evidence: news checked at the outlet,
   a figure the view rests on (rates, flows, supply, earnings), not because the price moved its way for a day or
   two, which the status already shows. The entry's own `confidence` stays the level it opened at; the pages show
   the latest level, with "opened at low confidence" and each change in the news list. It cannot change once
   the entry is judged.
3. **Judge** with `python3 .claude/skills/markets-desk/judge_views.py --write`, after logging the day's figures.
   It marks an entry wrong as soon as a close (or, for tests marked `"intraday": true`, a price inside the
   session) meets one of its `wrongIf` tests, judges each entry on its due date from its `track`, keeps
   "on track" and "open" current, and writes each verdict's result line. Judge by hand only what it reports it
   cannot decide (a wrong-if that is not a price, such as "the gas allocations are restored"). Never delete or
   rewrite a judged entry: wrong calls stay on the record.

4. **Write the lesson** for every entry judged that day (right, wrong or closed), in its `lesson`:
   `{"date", "text", "tag"}`. `text` is two sentences: what decided it, in figures (the driver that moved, by how
   much, against what the view assumed), and what the desk does differently because of it, or "nothing: the reasoning
   held" when a right call was right for its stated reason. A call that came right for a different reason than the one
   given says so. `tag` is a short slug for the kind of lesson (`one-driver`, `level-too-close`, `news-priced-in`,
   `horizon-too-short`, `reasoning-held`...). The Views page shows it under the verdict. When the same tag appears
   on two wrong calls, turn it into a rule under "Lessons from judged views" below, and apply it from then on.

**Lessons from judged views** (add to this list; never remove):
- `one-driver`: three calls that all needed oil to stay high broke on one 18% fall in Brent. At most two open
  entries on one driver.
- `level-too-close`: a wrong-if within 1.5 times the usual daily move is decided by noise, not by the view.

**Every new entry needs:**
- `wrongIf`: the price test behind its "wrong if", e.g. `[{"key": "brent", "op": "<", "level": 100}]`, keys as in
  the data log. A comparison view instead has a `track` with `vs` (one series) or `basket` and `vsBasket` (lists of
  keys) and is judged on its date.
- `driver`: the one thing it rests on, as a short slug (`oil`, `egp-rates`, `ai-spending`, `gas-supply`…).

**Make views that can be meaningfully right or wrong:**
- **Room to be right:** put the wrong-if level well beyond an ordinary day's move. judge_views.py warns when a
  level sits within 1.5 times the series' usual daily move of the start (a $245 test on Amazon at $243.79, a floor
  at the exact offer price): one routine day would decide it, which tests nothing.
- **One idea, one entry:** never record the same call as a view and a projection, and keep at most two open
  entries on one driver. When three calls all need oil to stay high, they are one bet: make the best-grounded one
  and leave the rest as notes. Early on, three calls broke on the same 18% fall in Brent.
- **Reason, not the day's move:** ground each in a driver with figures (rates, earnings, flows, supply), say what
  the market already prices, and set the confidence by the evidence, not the story. Low is a fine answer.
- A view can be proven wrong on any day but right only on its due date, so a young record shows wrong calls first;
  never shorten due dates to collect quick wins.

The dashboard's views card shows the day's views, including any judged that day, and links to the full record.
## Fair value

Read `refs/fairvalue.md` when the fair values need judgement: the Sunday review, a stock flagged by the checker or
fetch_fairvalue.py, or a one-off in results (`eps_norm`). fetch_fairvalue.py refreshes the figures every day by itself.

## Figures

The same sources and checks as the newsletter: `fetch_figures.py` first, a second source for every figure,
closing prices only, and a grey dash for any figure not confirmed that morning. Trend lines, changes over
periods and YTD come from `data/markets.json`.

**News for the US stocks and world markets: Reuters first.** Reuters is the original, most dependable report for
company results, deals, guidance, analyst moves and market wraps, and Yahoo Finance republishes its stories in full,
free to read (see the newsletter skill's "Reuters via Yahoo Finance"). When stock_news.py turns up a story from a site
that rewrites others (24/7 Wall St., TheStreet, TradingKey, Motley Fool, Zacks, Benzinga, Investing.com's rewrites),
search "Reuters <company> <subject>" and use the Reuters story where there is one, credited `Reuters (via Yahoo
Finance)` with the Yahoo link; otherwise the company's own release or filing, then CNBC, the FT, Bloomberg, the WSJ
or AP. Keep the rewrite sites as leads, not as the source a reader is sent to.

**FactIQ (connector, when the run has it): use it wherever it holds the answer, not only for US companies.** It is a
read-only data service of official statistics and filings. What it has that the desk can use:
- **Shipping through Suez, Bab el-Mandeb and Hormuz:** daily transit calls and cargo tonnage by ship type (IMF PortWatch,
  satellite AIS, `portwatch` schema, about two to three weeks behind). The hard figures for any story on Suez Canal
  revenue, the Red Sea or the Iran war: compare the latest weeks with the same weeks a year earlier.
- **Central banks and macro abroad:** Fed, Treasury, BLS and BEA figures (payrolls, CPI, PCE, GDP, yields), ECB and
  Bank of England data, BIS policy rates, and what central bankers said (search_media_appearances: the Fed, ECB, BoE,
  BoJ and others; not the Central Bank of Egypt).
- **Companies:** filed results, segments and guidance (search_company_filings) and what management said on earnings
  calls, with verbatim quotes (search_earnings_transcripts), for the desk's US stocks and any company a story turns on.
- **Commodities and currencies:** Brent, gold, gas and FX (get_market_data), as a check on fetch_figures.py, and the
  IMF's forecasts for Egypt and other countries (World Economic Outlook, yearly, marked as projections).
It has nothing for Egypt's own markets or months: no EGX prices, no monthly Egyptian inflation, reserves or central-bank
rates, no Central Bank of Egypt statements, and almost no Egyptian news; its dollar-pound rate is a market rate, not the
central bank's. Those stay with the usual sources. Credit the underlying source (IMF PortWatch, the company's 10-Q, the
BLS), not FactIQ, link the source URL it returns, and check a figure that moves a story against a second source as
always. Log a FactIQ lookup as a page (`research_log.py DATE desk page factiq:<what>`). If the connector is missing or
signed out, carry on without it.

## Wording

US English throughout, as in the newsletter's skill: American spelling (fertilizer, favor, organize, percent) and
month-first dates ("Thu, Nov 5", "November 5"). The checker flags British spellings and day-first dates in the day's file.

Label the stock tables "Egyptian stocks" and "US stocks" (the list pages and menu items are "EGX stocks" and "Wall Street stocks"), and the dashboard's "Stocks": never "your stocks",
in labels or in the text.

## Design

The achromatic-ledger style from the design-taste-frontend skill, on the newsletter's colours and fonts
with its dark mode. Dashboard: a close column on the left with a side card (Egypt: the dollar in pounds;
USA: oil) and, for Egypt, who bought and who sold; on the right the stories first, then the index chart
(EGX30 or Nasdaq) as its own card, then winners and losers, Stocks with the 1D–1Y switch, the week
ahead and open views. On a phone the stories come first.
