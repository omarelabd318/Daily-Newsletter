---
name: markets-desk
description: House rules for the Markets Desk, the daily markets analysis page planned next to the Daily Newsletter (what moved and why, which EGX sectors it helps or hurts, the desk's 36 stocks, the week ahead, open views). Use whenever writing, designing or reviewing the desk.
---

# Markets Desk

Status: written every day by the newsletter's scheduled runs, after the edition is published (see Daily run).
The first desk is 30 October 2026.
These are the rules agreed so far; add to them as the desk is finished.

## Daily run

The desk has its own scheduled run, about 45 minutes after the newsletter's, so a desk problem never holds up
the edition and the desk gets a full session to itself. Start from the day's research: pull the repo and read
today's edition (`editions/DATE.md`) in full, its figures already checked and logged; if it is not there yet,
check again every few minutes for up to half an hour, then research the markets yourself. Add your own searches
for anything the desk needs beyond the edition (the stock research below, flows, movers' reasons). Do not write
or change the newsletter, and do not log figures the edition already logged. On days with no session (Friday and Saturday for the EGX, Saturday and Sunday for the US) the
closes are the last session's; the news, stock research and analysis are still updated.

1. Copy the newest `desk/days/*.json` as a template to `desk/days/DATE.json` (DATE is the edition date) and
   rewrite every part for today: set `date`, `asOf` (the latest close, the day before DATE on a trading
   day), `fetched`, and remove `"sample": true`. The close card figures come from today's logged figures. Egypt's group lists the EGX30, the EGX70 EWI, USD/EGP and gold 24K
   per gram (24K, not 21K: the dashboard's Gold in Egypt card has 21K, 18K and the gold pound).
2. Run `python3 .claude/skills/markets-desk/stock_news.py` (`3` on Sundays) and do the stock research
   below; update `desk/stocks.json`.
3. Write each section: finding (the page shows its first sentence in bold, so make that sentence the day's
   point; at most two more, about 50 words in all; the coming dates go in the week ahead, not here; `next` is no
   longer shown), three to five stories (`calls`), winners and losers (`board`), the Stocks note,
   the week ahead and open views, then update `desk/views.json` (see Views: the record): new entries, news, and judgements.
4. Write `pages`: EGX (finding, session, news, outlook), EGP (finding, rates, drivers, news, view), US
   (finding, rates: the day's extra items only, see step 5; afterBell, news, outlook), Global (finding, notes, news). Carry each projection
   forward until its date, and score it when the date passes.
5. **Run `python3 .claude/skills/markets-desk/run_data.py` once, then read `desk/brief.md`.** It runs every fetch and
   calculation below in order (intraday, rates, valuation, movers, calendar, indicators, fair value, judging the
   views, the stock news leads and the movers' leads), each with a time limit, over one shared fetch layer
   (`sources.py`: retries, pacing between requests, a short shared memory so the same table is not fetched twice). A
   step that fails is reported and the rest carry on; rerun one with `run_data.py NAME`. Do not run the scripts one by
   one or read their output: the brief has what each did, which sources were flaky, what moved, the movers that still
   need a reason with their leads, every stock's news leads, results and events in the next seven days (and which
   need a preview), views due or judged without a lesson, what changed in the fair values, and the standing jobs due
   today. Work from it. It is a worksheet, not a page: nothing links to it and it is not committed (.gitignore). The scripts, for reference:
   `fetch_intraday.py` saves the last finished session's prices
   through the day (`desk/intraday.json`, for the 1D charts: the EGX30, the EGX70 EWI (from TradingView's chart feed,
   tradingview.py; it also fills the EGX month while it is short), the Nasdaq and the desk's stocks, and
   the last 24 hours of Bitcoin; the S&P 500 and Dow from Yahoo or else traced from the SPY and DIA funds;
   Brent, gold and the dollar index only when Yahoo answers). It also keeps the last five sessions every 15
   minutes (1W) and the last 23 every 30 minutes (1M). A US series Nasdaq refuses comes from Polygon, then Yahoo;
   Polygon also fills gaps in the saved US sessions (its key is a network secret on the environment, added by the
   proxy; five requests a minute, so a few gaps add a minute or two to the run).
   It keeps the saved session if a market is still trading, and takes under a minute. It also keeps the last
   five sessions (`week`, every 15 minutes), which the 1W charts draw once two or more are saved. The dollar in pounds
   has no 1D chart: the official rate barely moves within a day. Then run
   `python3 .claude/skills/markets-desk/fetch_rates.py` (`desk/rates.json`: the VIX from Cboe and the 3-month, 2-, 10- and
   30-year Treasury yields from the US Treasury, a year of daily closes): the Wall Street page's "Rates and data" shows
   them every day, with the dollar index from the log, each with its change on the day. So `pages.us.rates` holds only
   the day's extra items (a data release, Fed odds, a central bank decision), never the VIX or yields. Then run
   `python3 .claude/skills/markets-desk/fetch_valuation.py` to refresh each stock's Valuation card in
   `desk/stocks.json` (TradingView's screener and Mubasher for Egyptian stocks, taking whichever runs to the newer quarter; Nasdaq
   for US ones; P/E and P/B are worked out at the latest close, with the results period they rest on). It keeps a stock's card if its fetch fails.
   Then run `python3 .claude/skills/markets-desk/fetch_movers.py` for the whole market's biggest gainers and
   losers of the last session (`desk/movers.json`): all EGX stocks that traded at least EGP 1m, and US
   companies worth $10bn or more. The EGX and Wall Street pages show them under "Whole market"; mention a
   standout mover from outside the desk's stocks in the stories or News when there is a reason behind it.
   Then run `python3 .claude/skills/markets-desk/indicators.py` (`desk/indicators.json`: moving averages, RSI and MACD for
   every logged series, shown on stock pages as Trend and momentum; no network; its docstring has each formula, and
   `--test` checks them against worked examples). Quote them as description ("below its 200-day average"), never as a
   forecast, and never as the only reason for a view.
   Then run `python3 .claude/skills/markets-desk/fetch_fairvalue.py` (`desk/fairvalue.json`, the Fair value pages; see Fair value below).
   Run it with `--leads` to list news for the top five each way, find why each moved (a disclosure,
   results, a deal, a rating, a sector move), check it at the outlet, and add `why`, `source` and `url` to
   that stock's row in `desk/movers.json`. One short line; leave it out when no reason is found, and write
   "No company news found." only for moves of 5% or more. Never guess a reason. Do it for both markets, the EGX
   and the US: check_desk.py warns about any top-five mover of 5% or more left without a reason.
   The same script saves the past week's and month's biggest movers across each market (TradingView's changes, shown
   on the EGX and Wall Street pages under a 1D | 1W | 1M switch, labelled "Past week, TradingView" and "Past month,
   TradingView"); they reuse any reason written for that stock in the last 31 days, so no separate research is needed.
6. Add the session's flows to `desk/flows.json` when the EGX traded, and the date to `desk/index.json`
   with a one-line summary. When the central bank has published a new month of reserves (about the 7th;
   `fetch_figures.py` shows a new `reserves_usd`), add that month to `desk/reserves.json`: total, foreign
   currencies, gold and `sdr` (the rest: total minus the other two), from the bank's release or a news report
   of it that gives all three (Daily News Egypt, Arab Finance, Egypt Today), with `source` and `url`.
7. Run `python3 .claude/skills/markets-desk/check_desk.py`, fix every ERROR, then commit and push as for
   the edition (message `Desk DATE`).

## The desk's stocks

21 Egyptian: the newsletter's 12 Stocks Watch names (CIB, Talaat Moustafa, Telecom Egypt, Palm Hills,
Elsewedy, Orascom Construction, Fawry, Abu Qir, EFG Holding, Cleopatra, Juhayna, Alexandria Containers)
plus MOPCO, Eastern Company, e-finance, Emaar Misr, Banque du Caire (trading from 2 November 2026), Egypt
Aluminium, Alexandria Mineral Oils, Sidi Kerir Petrochemicals and Edita Food Industries.
15 US: the 12 Stocks Watch names plus Visa, Oracle and Costco. The extra 12 are desk-only: they are
logged daily (fetch_figures.py lists them as "Desk only") but are not rows in the newsletter's tables.

## Pages

- **EGY dashboard** `/desk/egypt/` and **US dashboard** `/desk/usa/`: the day on one screen for each market, kept short:
  the close as a strip of figures across the top, the stories, the index chart (EGX30; or S&P 500, Nasdaq and Dow, in
  that order), Gold in Egypt (EGY only), the whole market's three biggest gainers and losers with reasons, winners and
  losers, the week ahead and open views. The dollar, flows and the stock tables live on the EGP, EGX and stock-list
  pages. The EGX, EGP and Wall Street pages group their cards under small headings (Today, Why it moved, The stocks;
  the EGP page: The pound today, Why it's moving, The bigger picture, Reference).
- **How the pages divide the work:** a dashboard is the day (the close, what changed since yesterday, the stories,
  winners and losers, the week ahead, views) and carries no index chart or movers; those are on the market's own
  page (EGX, Wall Street), which is split into tabs (Today; Movers and heatmap; Flows; Stocks and views), kept in the
  address (`/desk/egx/#movers`). Valuation has its own pages: Sectors and Fair value.
- **EGX** `/desk/egx/`: EGX30 chart and the session, biggest movers (the whole market, or the desk's stocks), who
  bought and who sold with the foreign-flow history, the desk's Egyptian stocks, then Bullish and bearish.
- **EGP** `/desk/egp/`: the dollar in pounds, the central bank's and banks' rates (with net international
  reserves), Pound or dollar?, what is moving the pound, inflation with a switch to the real one-year yield, the other currencies and the desk's view on the pound.
- **Wall Street** `/desk/us/`: S&P 500, Nasdaq and Dow, rates and data, biggest movers (US companies worth $10bn or more, or the desk's stocks),
  results after the bell, the desk's US stocks, then Bullish and bearish.
- **Global** `/desk/global/`: Brent, gold, the dollar index and Bitcoin, each with one line on why it
  matters for Egypt. Gold in Egypt (24K, 21K, 18K, the gold pound) is on the EGP page and the EGY dashboard.
- **EGX stocks** `/desk/stocks/egypt/` and **Wall Street stocks** `/desk/stocks/us/`: all 12 of each as cards (price, change over
  the chosen period, trend line, YTD, 52-week range, market value, latest news, open views), sortable by
  list order, market value (largest first), or best and worst; each opens its stock's page. fetch_movers.py
  refreshes the market values (`cap` in desk/stocks.json) each morning.
- **Views** `/desk/views/`: the record of every view and projection. **Fair value** `/desk/fairvalue/` is its own page
  under each market (see Fair value below).
- **Sectors** `/desk/sectors/` (Egypt's menu): the EGX by sector, built from desk/fairvalue.json and the heatmap: each
  sector's P/E, return on equity, distance to fair value and moves, then its stocks ranked. The two lines of text per
  sector (`drivers`, `watch`) are in `desk/sectors.json`: review them on the first Sunday of the month and whenever a
  sector's driver changes (a rate decision, a gas cut, the end of a results season), with checked figures only.
- **Stock page** `/desk/stock/?t=TICKER`: one page per stock: chart against its index, performance,
  valuation, trading, dates coming up, the desk's projections and views on it, and its news.

The menu is grouped by market: Egypt (EGY dashboard, EGP, EGX, EGX stocks), USA (US dashboard, Wall Street,
Wall Street stocks), then Global and Views. Shared code is
`desk/desk.js` and `desk/desk.css`. The masthead and two-row menu on every page come from `desk/nav.js`. The look is style C (ivory paper, ink rules
instead of boxes, serif headlines and figures, navy data and red labels; dark is the newsletter's blue-black and teal),
set by the Style C blocks at the end of `desk/desk.css` and `desk/dash.css`. The two dashboards share `desk/dash.js` and `desk/dash.css` (their own copy of the styles: change
both together); each page names its section on `<body data-section>`. `/desk/` forwards to the EGY dashboard.

## Files

- `desk/days/DATE.json`: one day's desk in two sections, `egypt` and `global` (shown as "USA"),
  each with its own finding, close figures, top call, board, note under Stocks, week ahead and open views.
  `desk/days/2026-10-30.json` is the reference for its shape. `"sample": true` marks sample content.
- `desk/days/DATE.json` also holds `pages`: `egx` (finding, session, news, outlook), `egp` (finding, rates,
  drivers, news, view), `us` (finding, rates, afterBell, news, outlook) and `global` (finding, notes, news).
- Each section's `calls` holds the dashboard's stories, three to five (fewer only on a day with no more), the top call
  first. Each has `headline`, `body`, `view`, `affects` (tags, below), `wrong`, `confidence`, and from the second on a
  `line`: one sentence on why it matters, shown on its "Also today" card.
- `desk/index.json`: `{"desks": [{"date": "DATE", "summary": "..."}]}`; every page opens the newest.
- `desk/stocks.json`: one entry per stock for its page: sector, valuation (written by fetch_valuation.py: source, date, results
  period and basis), the
  latest session's trading, dates coming up, views and news. News and views are added newest first and
  never deleted. Valuation figures older than about a quarter are flagged on the page, not hidden.
- `desk/flows.json`: net equity flows by investor group, one entry per session, for the flow history. Each entry
  has `links`, `[{"source": "Youm7", "url": "https://..."}]`, the article for every report the figures came from
  (the EGX's own site blocks scripts, so the figures come from the outlets that carry its daily report); the EGX page
  shows them as links under the card, and check_desk.py fails an entry without them. `confirmed` is true once two
  reports agree. When only totals by nationality are reported, use the rows Egyptian, Arab and Foreign investors. A session dominated by a one-off deal (an IPO or block sale) gets `"oneoff": "<the deal>"`, so the foreign-investors chart leaves it out and names it.
- `desk/rolls.json`: futures contract switches (Brent's front month rolls each month). When fetch_figures.py
  prints "CONTRACT SWITCH?", add an entry (session = the first close on the new contract, from, to); the Global
  page's Brent chart marks the switch.
- `desk/reserves.json`: net international reserves by what they are held in, one entry per month, oldest
  first; the EGP page shows the latest month, split by what the reserves are held in.
- Stock pages read each stock's volume (`vol`) from the data log and compare the last session with the
  average of the 30 before it; the EGP page reads the central bank's dollar rate, policy rates, the one-year T-bill
  yield and inflation from the log. The day's file only adds what the log does not hold. The EGX page's session
  card reads turnover from the log (`egx_turnover`), advancers and decliners from desk/movers.json (which also
  holds the session's most active stocks and the EGX30 heatmap, `egx.heat`, from TradingView), and, until
  turnover has about 60 sessions logged, compares the EGX30 companies' shares traded (`egx30_vol`) with its 90-day
  average. Its "Blue chips against small and mid caps" table comes from the movers file (TradingView's EGX30 and
  EGX70 EWI); Give `session.breadth` in the day's
  file only when the exchange's official count is reported (it takes precedence over Mubasher's count).
- The charts, the Stocks tables and every change and YTD figure are drawn by the page from
  `data/markets-recent.json`, so log the day's figures before publishing a desk.

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

From mid-October to late November, and again each quarter, the desk's stocks report. Two steps, both kept in
`desk/stocks.json` and shown on the stock's page (Coming up) and, on the day, in the dashboards' Since yesterday:

- **Before (up to three days ahead):** follow the earnings-preview skill's Steps 1, 2 and 4 to write `"preview"`:
  `{"date", "period", "consensus", "watch": [...], "source", "url", "written"}`. `consensus` is one sentence with the
  published estimates and where they come from ("Analysts expect EPS of $1.25 on revenue of $35bn, LSEG"); leave it
  out when none is published, as for most Egyptian companies, rather than guessing. `watch` is the three to five
  things that will decide the reaction, ranked, one line each in figures (for a bank: net interest margin, loan
  growth, provisions; for a fertilizer maker: volumes after the gas cuts, urea prices). Skip the skill's
  scenario table and options-implied move unless a source publishes them. check_desk.py warns when a stock reports
  within three days without one.
- **Read the filing, not only the report of it.** For an Egyptian company: the earnings release or financial
  statements on its investor-relations page, or the disclosure the EGX publishes (Mubasher's news page for the stock
  links it). For a US company: the earnings release (8-K) and the 10-Q, through FactIQ's search_company_filings when
  the run has it, else the company's investor page. Take from it what outlets leave out: profit attributable to
  shareholders, one-off items (currency gains, provision releases, revaluations, asset sales), the share count, the
  segment figures and the guidance in the company's words. A one-off that moved profit by 10% or more goes in the
  headline and, for an Egyptian stock, into `eps_norm` in desk/fairvalue.json with the reason. If the filing cannot
  be opened, add `"basis": "outlet reports; the filing was not read"` to `lastResults`.
- **After (the day they come out):** follow the earnings-analysis skill's method, not its format (no 8-12 page
  report, no charts): lead with the verdict, quantify the gap, say why, and say what it means for the desk's view.
  Write `"lastResults"`: `{"date", "period", "verdict" (beat, miss, in line or mixed), "headline" (one line in
  figures), "points": [two to four lines: the numbers against the estimate or last year, the guidance], "thesis"
  (one sentence: what it changes for the desk's view or projection on the stock), "source", "url"}`. With no
  published estimate, judge against last year's quarter and the preview's watch list, and say so in the headline.
  For an Egyptian stock, also record the figures with set_results.py (step 7). Then add the news to any open view on
  the stock, and change its confidence if the results move the case (Views: the record).

## Stock research, every day

Log the desk's research as you go with `research_log.py DATE desk search|page ...`, and one line per stock with
`research_log.py DATE desk stock TICKER "what was found"` (or "no news"). A full desk takes at least 15 searches and
15 pages beyond the edition; every desk stock that moved 3% or more on the session, or has a lead in stock_news.py,
needs its leads opened and a stock line logged (the checker names any mover without one). Never log work not done.
End the final reply with the line `research_log.py DATE desk summary` prints.

Each of the desk's stocks gets its own search every morning, on top of the newsletter's research:

1. Run `python3 .claude/skills/markets-desk/stock_news.py` (add `3` on Sundays to cover the weekend). It
   lists each stock's headlines from the last two days, in English and, for the Egyptian stocks, Arabic.
2. Open every lead that is about the company, its stock or something that clearly affects it: results,
   disclosures to the exchange, deals and contracts, financing, dividends and capital changes, analysts'
   ratings and fair values, management changes, regulation, and prices of what it sells or buys. Skip
   market wraps, sponsorships, sports clubs that share a name, and fund-holding filings.
3. Check the facts at the outlet, and against a second outlet for anything that moves the stock.
4. Add each item to that stock in `desk/stocks.json` (`news`, newest first: date, text, source, url) and,
   when it matters to the market, to the page's News card with its ticker.
5. Let it change the analysis: news can move a stock onto or off the Bullish and bearish lists, change a
   projection or its confidence, or add a date to Coming up (results dates, general assemblies).

6. **Calendar:** run `python3 .claude/skills/markets-desk/fetch_calendar.py` (results dates and dividends for
   every desk stock, shown on the EGX and Wall Street pages). When a company announces its own results or
   assembly date, add it to that stock's `next` with `"date": "YYYY-MM-DD"` (an undated note carries
   `"added": "YYYY-MM-DD"` instead, and names dates, never "Thursday's"; check_desk.py flags notes that have passed or
   sat undated for ten days; the stock page adds the calendar's own dates beside them): the page then lists it as the desk's
   confirmed date in place of TradingView's estimate. For the US stocks it also takes the dividends their boards
   have declared and any stock splits from Polygon, refreshed once a week (about three minutes that day; the
   other days reuse the saved copy). After a split, check_desk.py warns until the data log's earlier prices are
   divided by the split's factor; do that the same day, or every chart shows a fake fall.
7. **Results:** when an Egyptian desk stock publishes results, record them the same day with
   `set_results.py TICKER --period QUARTER-END --ytd ... --prior-fy ... --prior-ytd ... --shares ... --equity ...
   --source ... --url ...` (profit attributable to shareholders, from the filing or two outlets that agree), then
   run `fetch_valuation.py TICKER`. The P/E then reflects the new quarter at once, instead of weeks later when
   TradingView or Mubasher catch up. Add the results date to Coming up when a company announces it.

No news is a valid result: never pad a stock with filler. Its page then shows its figures and older news.

## The desk's note on a stock

`brief` in `desk/stocks.json`, shown on the stock's page as "The desk's note": the standing view of the company, as
opposed to the day's news. `{"written", "business", "drivers": [{"name", "text"}], "value", "risks": [...], "change"}`:
- `business`: what it is and how it makes money, in two sentences with its key figure.
- `drivers`: the three or four things that move its profit, each with the latest figure the desk has checked.
- `value`: its multiples and the desk's fair value, in two sentences, with the catch.
- `risks`: three, specific to the company.
- `change`: what would change the desk's view, something that can be observed (a results date, a figure, a decision).
Only facts already checked for the desk (its news, results, valuation card and fair-value table) or checked now at
the source; no figure from memory. Six were written on November 11, 2026 (CIB, MOPCO, Palm Hills, Elsewedy, Fawry,
Talaat Moustafa). Write two more each Sunday until every desk stock has one, Egyptian stocks first, then rewrite a
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

`/desk/fairvalue/` (in Egypt's menu; `?m=us` in the United States menu) ranks stocks by how far they trade below or above the desk's own fair value, with four
grades each. `desk/fairvalue.json` holds it; `fetch_fairvalue.py` rebuilds the figures every morning and keeps the
`judgement` block, which only the run writes. The script's docstring is the exact method; the reasoning:

- **It is a ranking inside the EGX, not a verdict on the market.** At Egyptian rates an absolute model (discounting at
  the T-bill yield plus a premium) calls nearly every stock dear, because the market prices rates to fall. So the
  discount rate is solved for, not assumed: the rate at which the median stock is fairly priced on its assets. The
  page states the market-level reading separately (the median earnings yield against the after-tax T-bill yield).
- **Three estimates, because each fails differently.** Earnings (EPS times a peer P/E, tilted up to 25% for return on
  equity and profit growth) fails on one-off profits; assets (book value times the P/B its ROE justifies) fails on
  asset-light companies, so it is skipped above 6 times book; analysts fail when targets are stale, so an undated
  consensus far from everything else is dropped. Fair value is their weighted average (40, 30, 30) and needs two.
- **Banks are measured against banks** (their own discount rate and P/E): they always look cheap against industry.
- **Confidence is the spread between the estimates**, not a feeling. The two lists show medium and high only.

**Wall Street** (the tab's second market, `us` in the file): US common stocks worth $50bn or more, the same method
with three changes: long-run growth 6%, weights of earnings 30, assets 20 and analysts 50 (reported US earnings carry
more one-offs, and targets come from many analysts), and no earnings estimate when the P/E is outside 4 to 60. Its
judgement block is `judgementUS`, same fields. Notes are only needed for the desk's 15 US stocks.

What the run adds, in `judgement[TICKER]` (the script never touches it):
- `brokers`: a fair value or target found in the day's stock research and checked at the outlet:
  `{"firm", "value", "kind": "fair" or "target", "date", "url"}`. A target is brought back one year; entries count
  for 180 days. Add every one the research finds: this is the estimate that most needs the desk's own work.
- `eps_norm` with `eps_reason`: replace 12-month EPS when it misleads (a one-off gain or loss, a currency windfall, a
  commodity peak, new shares on the way). Use a figure from the filing or a broker, never a guess, and say which.
- `exclude`: a reason a stock cannot be rated on these terms at all (profit that is mostly revaluation, a merger that
  will change every per-share figure). It is then listed under Not rated with that reason.
- `note` and `noted`: the desk's line on the stock: the catch behind a cheap price or what a dear one is paying for.
  One or two sentences in figures. Write or refresh it for the ten cheapest and ten dearest and for every desk stock;
  review it when the company reports, when its confidence changes, or when it is more than a month old.

Each week (Sunday) read the whole table for figures that cannot be right (a P/E under 3, upside above 80%): the
cause is usually a bonus issue the source has not caught up with, parent-only earnings, or a stale target; fix it with
`eps_norm` or `exclude` and say why. When results come out for a desk stock, rerun the script after set_results.py.
The open view `2026-11-11-value-basket` scores the model (cheapest five desk stocks against the dearest five, to
February 11, 2027); when it is judged, open the next one from the table as it then stands, and if the model loses
twice running, rework the weights before opening a third. Never present a fair value as a forecast or advice: write
"the desk's fair value", and keep the page's line that a model and a judgement can both be wrong.

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
