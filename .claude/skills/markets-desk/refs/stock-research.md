# Stock research, every day

Log the desk's research as you go with `research_log.py DATE desk search|page ...`, and one line per stock with
`research_log.py DATE desk stock TICKER "what was found"` (or "no news"). A full desk takes at least 15 searches and
8 pages you opened yourself beyond the edition, on top of the pages the scripts read for you (stock_news.py --read,
results_due.py, logged by them as "read by scripts"; usually 15 or more). Two leads marked "same wording" are one
release, one source; an excerpt ending "Figures on the page: standalone; consolidated ..." gives more than one
basis, so say which one each figure is; every desk stock that moved 3% or more on the session, or has a lead in stock_news.py,
needs its leads read (the brief's excerpts count) and a stock line logged (the checker names any mover without one). Never log work not done.
End the final reply with the line `research_log.py DATE desk summary` prints.

Each of the desk's stocks gets its own search every morning, on top of the newsletter's research:

1. Read the news leads in `desk/brief.md` (run_data.py runs `stock_news.py --read`, three days on Sundays): each
   stock's headlines from the last two days, in English and, for the Egyptian stocks, Arabic, and under the four
   newest the page's own opening and figures (`>` lines), already read and logged. A lead marked "never names the
   company" is skipped; one marked "did not load" is opened by hand if it matters. Write from the excerpt where it
   is enough, and open the page only for what it leaves out or a figure to confirm at a second outlet; to read
   several, pass them at once to `python3 .claude/skills/daily-newsletter/articles.py --log DATE desk URL ...`.
2. Judge every lead that is about the company, its stock or something that clearly affects it: results,
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
