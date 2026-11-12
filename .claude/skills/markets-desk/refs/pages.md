# The desk's pages

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
- The Wall Street page's Movers tab also carries a heatmap of the 100 largest S&P 500 companies by sector (`us.heat` in
  desk/movers.json, one screener request in fetch_movers.py; shown when its session is the desk's US session).
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

