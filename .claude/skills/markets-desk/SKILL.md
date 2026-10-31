---
name: markets-desk
description: House rules for the Markets Desk, the daily markets analysis page planned next to the Daily Newsletter (what moved and why, which EGX sectors it helps or hurts, the desk's 32 stocks, the week ahead, open views). Use whenever writing, designing or reviewing the desk.
---

# Markets Desk

Status: written every day by the newsletter's scheduled runs, after the edition is published (see Daily run).
The first desk is 30 October 2026.
These are the rules agreed so far; add to them as the desk is finished.

## Daily run

Run after the newsletter edition is pushed, from the same research, so a desk problem never holds up the
edition. On days with no session (Friday and Saturday for the EGX, Saturday and Sunday for the US) the
closes are the last session's; the news, stock research and analysis are still updated.

1. Copy the newest `desk/days/*.json` as a template to `desk/days/DATE.json` (DATE is the edition date) and
   rewrite every part for today: set `date`, `asOf` (the latest close, the day before DATE on a trading
   day), `fetched`, and remove `"sample": true`. The close card figures come from today's logged figures.
2. Run `python3 .claude/skills/markets-desk/stock_news.py` (`3` on Sundays) and do the stock research
   below; update `desk/stocks.json`.
3. Write each section: finding, one to three stories (`calls`), who it helps and hurts, the Stocks note,
   the week ahead and open views, then update `desk/views.json` (see Views: the record): new entries, news, and judgements.
4. Write `pages`: EGX (finding, session, news, outlook), EGP (finding, rates, drivers, news, view), US
   (finding, rates, afterBell, news, outlook), Global (finding, notes, news). Carry each projection
   forward until its date, and score it when the date passes.
5. Run `python3 .claude/skills/markets-desk/fetch_intraday.py` to save the last finished session's prices
   through the day (`desk/intraday.json`, for the 1D charts: the EGX30, the Nasdaq and the desk's stocks, and
   the last 24 hours of Bitcoin; the S&P 500 and Dow from Yahoo or else traced from the SPY and DIA funds;
   Brent, gold and the dollar index only when Yahoo answers).
   It keeps the saved session if a market is still trading, and takes under a minute. The dollar in pounds
   has no 1D chart: the official rate barely moves within a day. Then run
   `python3 .claude/skills/markets-desk/fetch_valuation.py` to refresh each stock's Valuation card in
   `desk/stocks.json` (Mubasher for Egyptian stocks, Nasdaq for US ones; P/E and P/B are worked out at the
   latest close, with the results period they rest on). It keeps a stock's card if its fetch fails.
   Then run `python3 .claude/skills/markets-desk/fetch_movers.py` for the whole market's biggest gainers and
   losers of the last session (`desk/movers.json`): all EGX stocks that traded at least EGP 1m, and US
   companies worth $10bn or more. The EGX and Wall Street pages show them under "Whole market"; mention a
   standout mover from outside the desk's stocks in the stories or News when there is a reason behind it.
   Run it with `--leads` to list news for the top five each way, find why each moved (a disclosure,
   results, a deal, a rating, a sector move), check it at the outlet, and add `why`, `source` and `url` to
   that stock's row in `desk/movers.json`. One short line; leave it out when no reason is found, and write
   "No company news found." only for moves of 5% or more. Never guess a reason.
6. Add the session's flows to `desk/flows.json` when the EGX traded, and the date to `desk/index.json`
   with a one-line summary. When the central bank has published a new month of reserves (about the 7th;
   `fetch_figures.py` shows a new `reserves_usd`), add that month to `desk/reserves.json`: total, foreign
   currencies, gold and `sdr` (the rest: total minus the other two), from the bank's release or a news report
   of it that gives all three (Daily News Egypt, Arab Finance, Egypt Today), with `source` and `url`.
7. Run `python3 .claude/skills/markets-desk/check_desk.py`, fix every ERROR, then commit and push as for
   the edition (message `Desk DATE`).

## The desk's stocks

17 Egyptian: the newsletter's 12 Stocks Watch names (CIB, Talaat Moustafa, Telecom Egypt, Palm Hills,
Elsewedy, Orascom Construction, Fawry, Abu Qir, EFG Holding, Cleopatra, Juhayna, Alexandria Containers)
plus MOPCO, Eastern Company, e-finance, Emaar Misr and Banque du Caire (trading from 2 November 2026).
15 US: the 12 Stocks Watch names plus Visa, Oracle and Costco. The extra eight are desk-only: they are
logged daily (fetch_figures.py lists them as "Desk only") but are not rows in the newsletter's tables.

## Pages

- **EGY dashboard** `/desk/egypt/` and **US dashboard** `/desk/usa/`: the day on one screen for each market (below): the stories,
  the index chart (EGX30; or S&P 500, Nasdaq and Dow, in that order), the whole market's three biggest gainers and
  losers with reasons, the dollar in pounds with inflation, the real yield and reserves, flows, stocks, the week and views.
- **EGX** `/desk/egx/`: EGX30 chart and the session, biggest movers (the whole market, or the desk's stocks), who
  bought and who sold with the foreign-flow history, the desk's Egyptian stocks, then Bullish and bearish.
- **EGP** `/desk/egp/`: the dollar in pounds, the central bank's and banks' rates (with net international
  reserves), Pound or dollar?, what is moving the pound, inflation with a switch to the real one-year yield, the other currencies and the desk's view on the pound.
- **Wall Street** `/desk/us/`: S&P 500, Nasdaq and Dow, rates and data, biggest movers (US companies worth $10bn or more, or the desk's stocks),
  results after the bell, the desk's US stocks, then Bullish and bearish.
- **Global** `/desk/global/`: Brent, gold, the dollar index and Bitcoin, each with one line on why it
  matters for Egypt, and gold prices in Egypt.
- **EGY stocks** `/desk/stocks/egypt/` and **US stocks** `/desk/stocks/us/`: all 12 of each as cards (price, change over
  the chosen period, trend line, YTD, 52-week range, market value, latest news, open views), sortable by
  list order, market value (largest first), or best and worst; each opens its stock's page. fetch_movers.py
  refreshes the market values (`cap` in desk/stocks.json) each morning.
- **Stock page** `/desk/stock/?t=TICKER`: one page per stock: chart against its index, performance,
  valuation, trading, dates coming up, the desk's projections and views on it, and its news.

The menu is grouped by market: Egypt (EGY dashboard, EGP, EGX, EGY stocks), USA (US dashboard, Wall Street,
US stocks), then Global and Views. Shared code is
`desk/desk.js` and `desk/desk.css`. The two dashboards share `desk/dash.js` and `desk/dash.css` (their own copy of the styles: change
both together); each page names its section on `<body data-section>`. `/desk/` forwards to the EGY dashboard.

## Files

- `desk/days/DATE.json`: one day's desk in two sections, `egypt` and `global` (shown as "USA"),
  each with its own finding, close figures, top call, board, note under Stocks, week ahead and open views.
  `desk/days/2026-10-30.json` is the reference for its shape. `"sample": true` marks sample content.
- `desk/days/DATE.json` also holds `pages`: `egx` (finding, session, news, outlook), `egp` (finding, rates,
  drivers, news, view), `us` (finding, rates, afterBell, news, outlook) and `global` (finding, notes, news).
- Each section's `calls` holds the dashboard's stories, one to three, the top call first.
- `desk/index.json`: `{"desks": [{"date": "DATE", "summary": "..."}]}`; every page opens the newest.
- `desk/stocks.json`: one entry per stock for its page: sector, valuation (written by fetch_valuation.py: source, date, results
  period and basis), the
  latest session's trading, dates coming up, views and news. News and views are added newest first and
  never deleted. Valuation figures older than about a quarter are flagged on the page, not hidden.
- `desk/flows.json`: net equity flows by investor group, one entry per session, for the flow history.
- `desk/reserves.json`: net international reserves by what they are held in, one entry per month, oldest
  first; the EGP page shows the latest month, split by what the reserves are held in.
- Stock pages read each stock's volume (`vol`) from the data log and compare the last session with the
  average of the 30 before it; the EGP page reads the central bank's dollar rate, policy rates, the one-year T-bill
  yield and inflation from the log. The day's file only adds what the log does not hold.
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

## Two or three stories

The dashboard shows up to three stories in each section, one at a time, with arrows, dots and a swipe
between them. The first is the top call (above); add a second and third only when another story moves
markets or the reader's stocks in its own right, each written like the top call (below). One strong
story is better than three thin ones.

## How a call is written

Follow the morning-note skill in this repo (lead with the one thing that matters, always take a view,
"no news" is a valid answer). Every call, in the top call and on the winners and losers board, has:

- **what happened**, in figures, from checked sources;
- **the view**: a plain statement, kept apart from the facts;
- **the stocks it moves**, named;
- **wrong if**: what would show the view is wrong, specific enough to check (thesis-tracker skill);
- **a confidence level**: high, medium or low. "Momentum, not news" or "no company news found" means low.

Never present an unconfirmed claim as fact. A claim from a single source goes in a notice under the call
("reported by one source, not confirmed; the view does not rely on it"), and the view is written without it.

## Winners and losers

Two short lists, helped and hurt: EGX sectors or stocks, each with its driver, one line of reasoning
grounded in real figures, and a confidence level. Use the sector-overview skill for what drives a sector.

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
each with a headline, one or two sentences in figures, the outlet and a link to the story's own page.
Tag every story with the tickers it names or clearly affects (`"tickers": ["COMI"]`); a tagged story also
shows on those stocks' pages. Take them from the newsletter's research and from the stock research below.

## Stock research, every day

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

No news is a valid result: never pad a stock with filler. Its page then shows its figures and older news.

## The week ahead

The events that can move Egyptian markets and the reader's stocks, each rated high, medium or low impact,
with one line on why it matters (catalyst-calendar skill). Dates are checked like any other fact.

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
3. **Judge** an entry when its date passes, or earlier when its "wrong if" happens: set `status` to right
   or wrong and add `result` (date and one line with the figures). `on track` marks an open entry whose
   figures are going its way. Never delete or rewrite a judged entry: wrong calls stay on the record.

The dashboard's Open views card shows the day's views and links to the full record.
## Figures

The same sources and checks as the newsletter: `fetch_figures.py` first, a second source for every figure,
closing prices only, and a grey dash for any figure not confirmed that morning. Trend lines, changes over
periods and YTD come from `data/markets.json`.

## Wording

Label the stock tables "Egyptian stocks" and "US stocks" (the list page and menu item are "EGY stocks"), and the dashboard's "Stocks": never "your stocks",
in labels or in the text.

## Design

The achromatic-ledger style from the design-taste-frontend skill, on the newsletter's colours and fonts
with its dark mode. Dashboard: a close column on the left with a side card (Egypt: the dollar in pounds;
USA: oil) and, for Egypt, who bought and who sold; on the right the stories first, then the index chart
(EGX30 or Nasdaq) as its own card, then who it helps and hurts, Stocks with the 1D–1Y switch, the week
ahead and open views. On a phone the stories come first.
