# Go-to sources for figures

Check these pages first for the figures below, then search as usual for anything they do not cover.
Every page here loaded with real content when tested from the cloud environment on 28 October 2026.
Sites change, so if a page fails or looks stale, use the backup or search, and say in the edition when
a figure could not be confirmed. These pages are for figures; news still comes from many outlets.

| Figure | First choice | Backup |
|---|---|---|
| US dollar index (DXY) | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB?range=5d&interval=1d (fetch_figures.py gets it) | Search "dollar index" news for the day's level |
| Brent, gold in dollars, dollar index, S&P 500, Dow (backup and check) | Yahoo first; when Yahoo refuses (it often does from the cloud), fetch_figures.py takes them from TradingView's screener (Brent front-month and COMEX gold futures, the DXY, the S&P 500 and Dow), and when Yahoo answers it lists TradingView's Brent, gold and DXY as a "check" row to confirm against. Around a futures contract's expiry (Brent's front month rolls at the end of each month), sources can disagree on the day's change because they compare different contracts: compare like with like, and mark the change unconfirmed if they still differ. fetch_figures.py prints "CONTRACT SWITCH?" when it sees one; record it in desk/rolls.json as the markets-desk skill describes | FRED for the S&P 500 and Dow (a day behind); news reports of the day's settlement |
| EGP against USD, EUR, SAR, AED, KWD, QAR, GBP | The central bank's official buy and sell rates, https://www.cbe.org.eg/en/economic-research/statistics/cbe-exchange-rates (fetch_figures.py prints them and logs the dollar's); use the dollar's selling rate in the USD/EGP row. The logged pound rates and trend lines stay market mid-rates from https://open.er-api.com/v6/latest/EGP | EnterpriseAM's edition, or Egyptian news reports of the day's central bank rate |
| Gold in Egypt (21K, 24K, 18K per gram) | https://egypt.gold-price-today.com/ (Arabic: عيار 21 is 21K) | https://www.goldpricez.com/eg/gram |
| EGX30 close and daily change | https://english.mubasher.info/markets/EGX/indices/EGX30 (close, change, open, high, low) | https://tradingeconomics.com/egypt/stock-market |
| Egyptian stock prices (Stocks Watch) | https://english.mubasher.info/markets/EGX/stocks/TICKER, for example .../stocks/COMI (price, change, % change, previous close, time of last update) | Search |
| US stock prices (Stocks Watch) | https://query1.finance.yahoo.com/v8/finance/chart/TICKER?range=5d&interval=1d (JSON: the last two values in indicators.quote[0].close give the latest close and the change; timestamp gives the date). Do not use Yahoo for Egyptian stocks; its EGX data is years out of date | Nasdaq, then Polygon: fetch_figures.py tries both in turn, and check_edition.py confirms a US close against them (Polygon's key is a network secret on the environment, added by the proxy; five requests a minute) |
| Central bank interest rates | https://www.cbe.org.eg/en/economic-research/statistics/overnight-deposit-and-lending-rate (deposit and lending rates with the date they take effect; fetch_figures.py logs them) | https://tradingeconomics.com/egypt/interest-rate |
| Inflation (headline and core, annual) | https://www.cbe.org.eg/en/economic-research/statistics/inflation-rates (latest month; fetch_figures.py logs `infl_headline` and `infl_core`). The one-year T-bill yield minus headline inflation is the real return investors weigh | https://tradingeconomics.com/egypt/inflation-cpi |
| Net international reserves (monthly, $bn) | https://tradingeconomics.com/egypt/foreign-exchange-reserves (the central bank's figure, published about the 7th; its own reserves page has not been updated since 2023). fetch_figures.py logs `reserves_usd` | News reports of the central bank's announcement (Daily News Egypt, Ahram Online) |
| Treasury bill yields | The central bank's auction page, https://www.cbe.org.eg/en/auctions/egp-t-bills (latest results: weighted average accepted yield by tenor, with the auction date). fetch_figures.py reads it and logs each tenor once, on the first edition after its auction. 91- and 273-day bills are auctioned on Sundays, 182- and 364-day bills on Thursdays | News reports of the auction (Amwal Al Ghad, Al-Borsa, EnterpriseAM) |
| Public holidays and bank closures | https://www.officeholidays.com/countries/egypt/2026 (verify any holiday shift against a news report of the official announcement) | Search |
| Cairo weather, today and next two days | `python3 .claude/skills/daily-newsletter/weather.py` (two services side by side: Open-Meteo or MET Norway, and wttr.in) | Egyptian Meteorological Authority |
| Egyptian football | https://www.kingfut.com/ (English) | https://www.kooora.com/ (Arabic) |
| European football results | https://www.bbc.com/sport/football/scores-fixtures/YYYY-MM-DD (use the date of the matches) | https://www.espn.com/soccer/scoreboard |
| Tennis | https://www.bbc.com/sport/tennis | https://www.wtatennis.com/scores |

These block automated access from the cloud environment, so do not spend time on them: the Egyptian Exchange site (egx.com.eg), Ahram Online, Egypt Today,
Reuters, investing.com, timeanddate.com, the ATP Tour site and the Egyptian Meteorological Authority.
News reports that quote them are fine.

