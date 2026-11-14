# Files

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
