# The desk's data scripts, for reference

run_data.py runs all of these in order (SKILL.md, Daily run, step 5); the brief reports what each did. Read this
when a step fails, or its output needs judging. Moved here from SKILL.md so the daily run does not carry it.

`fetch_intraday.py` saves the last finished session's prices
   through the day (`desk/intraday.json`, for the 1D charts: the EGX30, the EGX70 EWI (from TradingView's chart feed,
   tradingview.py; it also fills the EGX month while it is short), the Nasdaq and the desk's stocks, and
   the last 24 hours of Bitcoin; the S&P 500 and Dow from Yahoo or else traced from the SPY and DIA funds;
   Brent, gold, the dollar index and Bitcoin from TradingView's chart feed, which also saves their last seven days
   hourly and 30 days two-hourly for the Global page's 1W and 1M charts). It also keeps the last five sessions every 15
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
