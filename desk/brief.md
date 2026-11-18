# Desk brief, Wednesday, November 18, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 28s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-17 (25.46); Treasury yields to 2026-11-17 (10-year 5.1%).
- **valuation**: ok in 25s (GitHub Actions). LLY: $1.35tn, P/E (last 12 months) 44.3, Forecast P/E (fiscal 2026) 39.6 (the four quarters to Sep 2026)
- **movers**: ok in 19s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 51.2
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.0%, median P/E 10.0; cheapest MASR +72%, PHAR +50%, ABUK +48%; dearest ARAB -61%, MOIN -64%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 57s (GitHub Actions). 
- **news**: ok in 113s (GitHub Actions). 
- **leads**: ok in 85s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 4 needed a retry.

## What moved (latest close against the one before)
- EGX30 51,681.60 (-0.99%); EGX70 EWI 17,592.80 (-2.42%); USD/EGP 53.80 (+0.22%); Gold 21K 5,900.00 (-0.17%); Brent 93.14 (+0.76%); S&P 500 7,340.53 (-1.03%); Nasdaq 24,328.38 (-0.74%); Bitcoin 64,491.00 (-0.17%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): EGAL -5.2%, PHDC -3.5%, ORCL -3.4%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 73, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (13.8% over) and its 200-day (13.6% over), though the 50-day is still below the 200-day; RSI 75, stretched after a run: above 70.
    - INTC: Turning down: below both its 50-day average (40.8% under) and its 200-day (36.9% under), though the 50-day is still above the 200-day; RSI 30, washed out: below 30.
    - JPM: No clear trend: 2.9% below its 50-day average and 1.5% above the 200-day; RSI 42, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - LLY: In an uptrend: above its 50-day average, which is above the 200-day; RSI 63, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - NFLX: In a downtrend: below its 50-day average, which is below the 200-day; RSI 33, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (26.6% under) and its 200-day (23.7% under), though the 50-day is still above the 200-day; RSI 23, washed out: below 30.
    - ORCL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 40, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).

## Movers that still need a reason (top five each way, 5% or more)
- EGX INFI (Foodico) +10.0%; EGX PRMH (Prime Holding) +6.9%; EGX SAUD (Al Baraka Bank Egypt) +5.3%; EGX CRST (Creast mark For Contracting) -19.7%; EGX AMES (Alexandria New Medical Center) -12.2%; EGX TYCN (Tycoon Holding Company For Financial Investments) -8.7%; EGX FTNS (Fitness Prime) -6.4%; EGX ZEOT (Extracted Oils & Derivatives) -6.2%; US ACM (AECOM) +11.1%; US ESLT (Elbit Systems) +5.8%; US NXT (Nextpower) -12.1%; US CRM (Salesforce) -9.5%; US WCN (Waste Connections) -8.0%; US QXO (QXO) -7.5%; US INTU (Intuit) -7.2%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-17 (TradingView's closes; Mubasher's list refused), 205 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (214)
US: 2026-11-17, 832 companies
US week and month: US companies worth $10bn or more (829)
EGX30 heatmap: 2026-11-17, 31 members
US heatmap: 2026-11-17, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-17
## INFI +10.0%  Foodico
- no headlines found
## PRMH +6.9%  Prime Holding
- no headlines found
## SAUD +5.3%  Al Baraka Bank Egypt
- no headlines found
## MIPH +3.8%  Minapharm Pharmaceuticals
- no headlines found
## PHTV +3.0%  Pyramisa Hotels
- no headlines found
## CRST -19.7%  Creast mark For Contracting
- Tue 17 Nov | جريدة حابي | كرستمارك للمقاولات: الجمل للاستثمارات تُخفض حصتها في الشركة إلى 4.37%
  https://hapijournal.com/2026/11/17/كرستمارك-للمقاولات-الجمل-للاستثمارا-2/
  > كرستمارك للمقاولات: الجمل للاستثمارات تُخفض حصتها في الشركة إلى 4.37% الصفقة تضمنت بيع 19.76 مليون سهم.. رنا ممدوح _ أعلنت شركة كرستمارك للمقاولات والاستثمار العقاري، عن قيام شركة الجمل للاستثمارات والتنمية بخفض حصتها في رأسمال الشركة من 6.134% إلى 4.37%.
- Tue 17 Nov | اليوم السابع | الجمل للاستثمارات تسيل 48.4 مليون جنيه من أسهمها في "كرستمارك للمقاولات" بالبورصة
  https://www.youm7.com/story/2026/11/17/الجمل-للاستثمارات-تسيل-48-4-مليون-جنيه-من-أسهمها-في/7622332
  > كشفت شركة كرستمارك للمقاولات والتطوير العقاري، عن تنفيذ شركة الجمل للاستثمارات والتنمية عملية بيع لنحو 19.76 مليون سهم من أسهم الشركة، بقيمة إجمالية بلغت 48.4 مليون جنيه، بمتوسط سعر بيع 2.45 جنيه للسهم، وفقًا لنموذج الإفصاح عن تعاملات المساهمين وأعضاء مجلس الإدارة والعاملين بالشركة والأطراف المرتبطة، المعد وفقًا لأحكام المادة ...
- Tue 17 Nov | https://www.youlyou.com/ | الجمل للاستثمارات تبيع نحو 20 مليون سهم في كرستمارك للمقاولات بـ48.4 مليون جنيه
  https://www.youlyou.com/96657
  > 1- باعت شركة الجمل للاستثمارات والتنمية 19.76 مليون سهم في كرستمارك للمقاولات. 2- بلغت القيمة الإجمالية للصفقة 48.42 مليون جنيه. 3- سجل متوسط سعر البيع 2.45 جنيه للسهم. 4- تراجعت ملكية الجمل للاستثمارات في الشركة من 6.134% إلى 4.37%.
- Mon 16 Nov | عالم المال | أخبار البورصة المصرية اليوم.. «إيديتا» تتصدر الرابحين و«كرستمارك» الأكثر تراجعًا
  https://alamalmal.net/article/943439/أخبار-البورصة-المصرية-اليوم-«إيديتا»-تتصدر-الرابحين
  > تباين أداء الأسهم بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الاثنين 16 نوفمبر 2026، حيث تصدر سهم شركة إيديتا للصناعات الغذائية قائمة الأسهم الأكثر ارتفاعًا بنسبة 7.44%، فيما جاء سهم شركة كرستمارك للمقاولات والتطوير العقاري في صدارة الأسهم الأكثر انخفاضًا بنسبة 20%. الأسهم الأكثر ارتفاعًا بالبورصة المصرية
## AMES -12.2%  Alexandria New Medical Center
- no headlines found
## TYCN -8.7%  Tycoon Holding Company For Financial Investments
- no headlines found
## FTNS -6.4%  Fitness Prime
- no headlines found
## ZEOT -6.2%  Extracted Oils & Derivatives
- no headlines found

# US 2026-11-17
## ACM +11.1%  AECOM
- Wed 18 Nov | Yahoo Finance | AECOM (ACM) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P00008SMH_AnalystReport_1794963268000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Wed 18 Nov | Yahoo Finance | Is AECOM (ACM) Fully Valued As Strong Earnings And 2027 Guidance Lift Interest?
  https://finance.yahoo.com/markets/stocks/articles/aecom-acm-fully-valued-strong-002355944.html
  > AECOM earnings jolt investor interest AECOM (ACM) has just delivered a busy earnings day, pairing fourth quarter results and fresh 2027 guidance with record operating margins, a higher backlog and a 10% dividend increase that sparked strong investor interest.
- Tue 17 Nov | TradingView | AECOM Stock 12‑Month Price Target Raised to $85.14, Implies 17% Upside
  https://www.tradingview.com/news/tradingview:541e5b09962b5:0-aecom-stock-12-month-price-target-raised-to-85-14-implies-17-upside/
  > AECOM Stock 12‑Month Price Target Raised to $85.14, Implies 17% Upside Less than 1 min read - According to estimates from 11 analysts, AECOM stock's average price target has risen from $80.91 to $85.14, with forecasts ranging from $73 to $103 per share
- Tue 17 Nov | Business Upturn | US Stock Movers: SLS Surges 156% as BILL and AECOM Post Double-Digit Gains
  https://businessupturn.com/usa/money/us-markets/us-stock-movers-sls-surges-156-as-bill-and-aecom-post-double-digit-gains/
  > US equities delivered a mixed session on Tuesday, 17 November 2026, with sharp moves in both directions across healthcare, technology, and infrastructure names. SELLAS Life Sciences Group (SLS) was the standout performer of the day, rocketing 156.36% to close at $19.15, dwarfing all other movers.
## ESLT +5.8%  Elbit Systems
- Wed 18 Nov | The Globe and Mail | Elbit Systems (ESLT) Gets a Buy from Bank of America Securities
  https://www.theglobeandmail.com/investing/markets/stocks/ESLT/pressreleases/8885475/elbit-systems-eslt-gets-a-buy-from-bank-of-america-securities/
  > Elbit Systems (ESLT) Gets a Buy from Bank of America Securities Bank of America Securities analyst Ronald Epstein maintained a Buy rating on Elbit Systems today. The company’s shares closed today at ILA223,860.00.
- Tue 17 Nov | Seeking Alpha | Elbit Systems shares rise on earnings beat as backlog reaches $33B (ESLT:NASDAQ)
  https://seekingalpha.com/news/4673889-elbit-systems-shares-rise-on-earnings-beat-as-backlog-reaches-33b?source=generic_rss
  (page: did not load (403))
- Tue 17 Nov | GuruFocus | Elbit Systems Stocks Jump 7.8% as Backlog Hits Record $33 Billio
  https://www.gurufocus.com/news/9205469/elbit-systems-stocks-jump-78-as-backlog-hits-record-33-billion?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141
  (page: did not load (403))
- Tue 17 Nov | TradingView | Elbit Systems Stocks Jump 7.8% as Backlog Hits Record $33 Billion
  https://www.tradingview.com/news/gurufocus:5dd290ba1094b:0-elbit-systems-stocks-jump-7-8-as-backlog-hits-record-33-billion/
  > Elbit Systems Stocks Jump 7.8% as Backlog Hits Record $33 Billion Elbit Systems ESLT shares jumped 7.8% to $733.83 at 9:49 a.m.
## ALAB +4.6%  Astera Labs
- Wed 18 Nov | TradingView | Astera Labs vs. Amphenol: Which Connectivity Stock Is the Better Buy?
  https://fr.tradingview.com/news/zacks:1f3e21118094b:0-astera-labs-vs-amphenol-which-connectivity-stock-is-the-better-buy/
- Wed 18 Nov | Yahoo Finance | Hyve Partnership Might Change The Case For Investing In Astera Labs Stock (ALAB)
  https://finance.yahoo.com/markets/stocks/articles/hyve-partnership-might-change-case-021401083.html
- Wed 18 Nov | Yahoo Finance Singapore | How Does Astera Labs (ALAB) New AI Infrastructure Partnership Change Its Enterprise Opportunity?
  https://sg.finance.yahoo.com/news/does-astera-labs-alab-ai-002259652.html
- Tue 17 Nov | TOKENPOST | Optical Communications Shares Rise as Astera Labs Gains 4.58%
  https://www.tokenpost.com/news/investing/59953
## VIK +4.4%  Viking Holdings
- Wed 18 Nov | TipRanks | Viking Holdings Earnings Call Highlights Growth Amid Disruption
  https://www.tipranks.com/news/company-announcements/viking-holdings-earnings-call-highlights-growth-amid-disruption
- Tue 17 Nov | AlphaStreet | Viking Holdings Falls Short on Q3 2026 EPS at $1.11
  https://news.alphastreet.com/viking-holdings-falls-short-on-q3-2026-eps-at-1-11/
- Tue 17 Nov | Yahoo Finance | Viking Holdings Ltd Q3 2026 Earnings Call Summary
  https://finance.yahoo.com/markets/stocks/articles/viking-holdings-ltd-q3-2026-215023724.html
- Tue 17 Nov | Stock Titan | Officer Minxuan Zhao proposes selling 5,300 Viking Holdings (VIK) shares.
  https://www.stocktitan.net/sec-filings/VIK/144-viking-holdings-ltd-sec-filing-0917130c388e.html
## AS +3.9%  Amer Sports
- Wed 18 Nov | Global Banking & Finance Review | Amer Sports rises 3.92% in Tuesday's session
  https://www.globalbankingandfinance.com/amer-sports-as-rises-2026-11-17/
- Wed 18 Nov | Seeking Alpha | Amer Sports: Unbeatable Momentum, Stock Remains Attractive
  https://seekingalpha.com/article/4969370-amer-sports-unbeatable-momentum-stock-remains-attractive
- Wed 18 Nov | Yahoo Finance | Amer Sports: 3 Key Takeaways for Long-Term Investors
  https://finance.yahoo.com/markets/stocks/articles/amer-sports-3-key-takeaways-000423324.html
- Tue 17 Nov | GuruFocus | Amer Sports Inc (AS) Stock Up 3.9% and Still Undervalued -- GF S
  https://www.gurufocus.com/news/9206216/amer-sports-inc-as-stock-up-39-and-still-undervalued-gf-score-69100
## NXT -12.1%  Nextpower
- Wed 18 Nov | Yahoo Finance | Nextpower (NXT) Just Got Hammered — These 2 Firms Hold The Reason
  https://finance.yahoo.com/markets/stocks/articles/nextpower-nxt-just-got-hammered-060420135.html
  > (NASDAQ:NXT) is one of the 10 Stocks Investors Are Fleeing. Nextpower saw its share prices fall by 12.13 percent on Tuesday to finish at $78.48 apiece, as investors took path from two investment firms' lower price targets for its stock.
- Wed 18 Nov | Yahoo Finance | Nextpower Inc. (NXT) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P0001QG0N_AnalystReport_1794963268000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | Benzinga | Why Is Nextpower Stock Sinking Tuesday?
  https://www.benzinga.com/trading-ideas/movers/26/11/63362677/why-is-nextpower-stock-sinking-tuesday
  (page: did not load (403))
- Tue 17 Nov | Investing.com | Mizuho raises Nextpower stock price target on storage growth
  https://www.investing.com/news/analyst-ratings/mizuho-raises-nextpower-stock-price-target-on-storage-growth-93CH-5033710
  (page: did not load (403))
## CRM -9.5%  Salesforce
- Wed 18 Nov | ad-hoc-news.de | Salesforce stock gains 0.74% to EUR 177.76 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/salesforce-stock-gains-0-74-to-eur-177-76-before-xetra/70530000
  > Salesforce operates an AI CRM platform that combines Agentforce, unified data and Customer 360 applications. On Xetra, the stock closed at EUR 176.46 on Wednesday, November 17, 2026. Salesforce combines CRM and AI Salesforce presents Agentforce, unified data and Customer 360 applications as parts of its AI CRM platform.
- Wed 18 Nov | TipRanks | Salesforce Reportedly Starts Another Round of Job Cuts as CRM Stock Plunges 9%
  https://www.tipranks.com/news/salesforce-reportedly-starts-another-round-of-job-cuts-as-crm-stock-plunges-9
  (page: did not load (403))
- Wed 18 Nov | Yahoo Finance | Salesforce (CRM) Gets Hammered as Traders Hit Sell Button
  https://finance.yahoo.com/markets/stocks/articles/salesforce-crm-gets-hammered-traders-045611127.html
  > (NYSE:CRM) is one of the 10 Stocks Investors Are Fleeing. Salesforce fell by 9.45 percent on Tuesday to end at $194.52 apiece, as investor focus shifted to reports of a new round of job cuts, shunning its newly clinched partnership with Microsoft Corp.
- Wed 18 Nov | Yahoo Finance | CRM Stock Faces Worst Week Since April: Fresh Layoffs Reportedly Surface Across Salesforce Teams
  https://finance.yahoo.com/markets/stocks/articles/crm-stock-faces-worst-week-031048815.html
  > - Salesforce has reportedly started another round of layoffs, with employees confirming recent departures. - Salesforce cut 86 California jobs in August across sales, administrative and technology roles. - AI disruption fears and the costly Braze deal are weighing on investor confidence in Salesforce.
## WCN -8.0%  Waste Connections
- Wed 18 Nov | Yahoo Finance | Waste Connections, Inc. (WCN) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P000005V0_AnalystReport_1794963268000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | GuruFocus | Is Waste Connections Inc (WCN) a Bargain After 8.0% Drop? GF Val
  https://www.gurufocus.com/news/9206109/is-waste-connections-inc-wcn-a-bargain-after-80-drop-gf-value-says-undervalued
  (page: did not load (403))
- Tue 17 Nov | GuruFocus | Waste Connections (WCN) Stock Drops 8% After Methane Gas Eruptio
```

## Results to record (results_due.py)
## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py
### NVDA
- NVDA: 8-K (results release) filed 2026-11-17: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/nvda-20261117.htm
    Revenue, quarter to 2026-07-26 (10-Q filed 2026-08-26): $96.22bn; a year earlier $46.74bn (+105.9%)
    Net income, quarter to 2026-07-26 (10-Q filed 2026-08-26): $59.69bn; a year earlier $26.42bn (+125.9%)
    Diluted EPS, quarter to 2026-07-26 (10-Q filed 2026-08-26): $2.46; a year earlier $1.08 (+127.8%)
### ORAS
- Wed 18 Nov | www.youlyou.com | أرباح أوراسكوم كونستراكشون تقفز 71% إلى 234.7 مليون دولار بأول 9 شهور من 2026
  https://www.youlyou.com/97145
  > 1- ارتفعت أرباح أوراسكوم كونستراكشون إلى 234.7 مليون دولار بنمو 71.1%. 2- صعدت الإيرادات إلى 4.78 مليار دولار خلال 9 شهور. 3- زادت الأرباح التشغيلية إلى 292.8 مليون دولار بنسبة 47.4%. 4- بلغ نصيب مساهمي الشركة الأم من الأرباح 218 مليون دولار. 5- ارتفعت ربحية السهم إلى 1.98 دولار مقابل 1.21 دولار. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | شبكة تواصل الإخبارية | أرباح «أوراسكوم كونستراكشون» المصرية تقفز 103% في الربع الثالث
  https://twaslnews1.twaslnews.com/7888823/
- Wed 18 Nov | Forbes Middle East | Orascom Construction Profit Surges 96% To $218M
  https://forbesmiddleeast.com/industry/real-estate/orascom-constructions-nine-month-profit-nearly-doubles-to-$218m-as-backlog-hits-$116b
- Wed 18 Nov | بوابة التكنولوجيا المالية | «أوراسكوم كونستراكشون » تحقق 218 مليون دولار صافي أرباح خلال 9 أشهر بنمو 95.9%
### HRHO
- Wed 18 Nov | TradingView | EFG Holding Q3 Consol Net Profit EGP 719.8 Million
  https://www.tradingview.com/news/reuters.com,2026:newsml_FWN46Y19U:0-efg-holding-q3-consol-net-profit-egp-719-8-million/
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-18 CLHO results (expected)
- 2026-11-18 EAST results (expected)  <- write its preview
- 2026-11-18 EFID results (expected)
- 2026-11-18 EFIH results (expected)  <- write its preview
- 2026-11-18 HRHO results (expected)
- 2026-11-18 JUFO results (expected)
- 2026-11-18 PHDC results (expected)
- 2026-11-19 MSFT dividend
- 2026-11-24 COST dividend

## Views
- due 2026-11-20: Brent stays below $105 while Iran talks continue (on track)
    Views: nothing to change.

## Fair value
- Changed since the last run: TMGH -5% -> -3% (medium -> low); NINH new at -34%.
- In the ten cheapest or dearest with no note: MCQE, ADIB, SCEM, EMFD, MTIE, AMOC, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-18. Open each story before using it.
## COMI  (8 leads)
- Wed 18 Nov | صحيفة اخبارنا | عروض CIB للجمعة البيضاء: تقسيط دون مقدم أو فوائد حتى نهاية نوفمبر
  https://www.akhbrna.ae/economy/arwd-albnk-altjary-aldwly-fy/
  > أطلق البنك التجاري الدولي - مصر (CIB) عروض الجمعة البيضاء لحاملي بطاقاته الائتمانية، متيحا تقسيط مشتريات مختارة دون مقدم أو فوائد أو مصاريف إدارية حتى نهاية نوفمبر الجاري.
- Tue 17 Nov | شبكة تواصل الإخبارية | 4 خطوات مبسطة.. افتح حسابك المصرفي رقميًا في البنك التجاري الدولي
  https://twaslnews1.twaslnews.com/7862548/
  (page: did not load (403))
- Tue 17 Nov | مجلة البوصلة الاقتصادية | 63 مليار جنيه أرباح البنك التجاري الدولي خلال 9 أشهر
  https://alboslanews.com/بنوك-و-تأمين/63-مليار-جنيه-أرباح-البنك-التجاري-الدولي-خلال-9-أشهر-430382
  > 63 مليار جنيه أرباح البنك التجاري الدولي خلال 9 أشهر الثلاثاء 10 نوفمبر 2026 -10:27 [Figures on the page: standalone; consolidated; nine months; first half. Check which one each figure is.]
## TMGH  (8 leads)
- Tue 17 Nov | هير نيوز | سفير العراق بالقاهرة يبحث مع هشام طلعت مصطفى فرص الاستثمار والتطوير العقاري في العراق
  https://www.her-news.com/135640
  > سفير العراق بالقاهرة يبحث مع هشام طلعت مصطفى فرص الاستثمار والتطوير العقاري في العراق استقبل االيوم سفير جمهورية العراق لدى جمهورية مصر العربية ومندوبها الدائم لدى جامعة الدول العربية، الدكتور قحطان طه خلف، الرئيس التنفيذي لمجموعة طلعت مصطفى، السيد هشام طلعت مصطفى، في مبنى السفارة بالقاهرة.
- Tue 17 Nov | https://www.youlyou.com/ | سحر طلعت مصطفى: أسوان تمتلك مقومات سياحية تؤهلها لجذب مزيد من السائحين
  https://www.youlyou.com/96668
  > أكدت النائبة سحر طلعت مصطفى، رئيسة لجنة السياحة والطيران المدني بمجلس النواب، أن محافظة أسوان تتمتع بمكانة سياحية استثنائية ومقومات فريدة تؤهلها لتكون واحدة من أبرز الوجهات السياحية على المستوى العالمي، مشيرة إلى أن المحافظة تحظى بمكانة خاصة في قلوب المصريين، وتمثل إحدى أهم الواجهات السياحية التي يجب العمل على تعزيز حضورها على خريطة السياحة ...
- Tue 17 Nov | https://www.youlyou.com/ | طلعت مصطفى تستقبل وفدا من المطورين العقاريين العُمانيين في مدينة نور
  https://www.youlyou.com/96482
  > 1- طلعت مصطفى تستقبل وفدا من المطورين العقاريين العُمانيين لزيارة مشروعي «نور» و«مدينتي». 2- الوفد يتعرف على تجربة المجموعة في تطوير المدن العمرانية المتكاملة وتطبيق معايير الاستدامة. 3- مدينة «نور» تقام على مساحة 21 مليون متر مربع وتستوعب أكثر من 600 ألف نسمة. 4- الوفد يشيد بالخدمات الذكية والحلول التكنولوجية والمساحات الخضراء في مدينة «نور».
## ETEL  (8 leads)
- Tue 17 Nov | https://www.youlyou.com/ | 24.4 مليار جنيه أرباح.. هل أصبحت المصرية للاتصالات أكثر جاذبية للمستثمرين؟
  https://www.youlyou.com/96699
  > - ارتفع صافي أرباح المصرية للاتصالات بنسبة 44% خلال أول 9 أشهر من 2026، ليصل إلى 24.4 مليار جنيه. - سجلت التدفقات النقدية الحرة 28 مليار جنيه، بما يعادل 65% من الأرباح التشغيلية قبل الفوائد والضرائب والإهلاك والاستهلاك. - تراجعت نسبة صافي الدين إلى الأرباح التشغيلية إلى 0.8 مرة مقابل 1.5 مرة خلال الفترة المقارنة. [Figures on the page: consolidated; unaudited or preliminary; nine months. Check which one each figure is.]
- Tue 17 Nov | اليوم السابع | كيف تخطط المصرية للاتصالات للتحول من صافي الدين إلى صافي النقدية خلال 5 سنوات؟
  https://www.youm7.com/story/2026/11/17/كيف-تخطط-المصرية-للاتصالات-للتحول-من-صافي-الدين-إلى-صافي/7622188
  > تواجه شركات الاتصالات تحديًا مستمرًا في الموازنة بين تمويل احتياجاتها والحفاظ على مستويات مديونية مناسبة، خاصة أن تطوير الشبكات وتحديث البنية التحتية يتطلبان إنفاقًا رأسماليًا متواصلًا، إلى جانب الالتزامات المالية المرتبطة بالتشغيل والتوسع، ما يجعل إدارة الديون والتدفقات النقدية من العوامل المؤثرة في قدرتها على النمو. [Figures on the page: unaudited or preliminary; nine months; first half. Check which one each figure is.]
- Tue 17 Nov | اليوم السابع | 700 مليون دولار سنويًا.. كيف تؤمن المصرية للاتصالات احتياجاتها الدولارية؟
  https://www.youm7.com/story/2026/11/17/700-مليون-دولار-سنويًا-كيف-تؤمن-المصرية-للاتصالات-احتياجاتها-الدولارية/7622148
  > تعتمد شركات الاتصالات على تدفقات مستمرة من النقد الأجنبي لتغطية جانب من احتياجاتها الاستثمارية والتشغيلية، في ظل ارتفاع المكون الدولاري في تكلفة المعدات والتكنولوجيا المستخدمة في تطوير الشبكات والبنية التحتية، وهو ما يجعل تنوع مصادر العملة الأجنبية عاملًا مهما في قدرة الشركات على تنفيذ خططها التوسعية.
## PHDC  (8 leads)
- Tue 17 Nov | أصول مصر | «بالم هيلز للتعمير» تحقق مبيعات قياسية بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://www.osoulmisrmagazine.com/452821
  > «بالم هيلز للتعمير» تحقق مبيعات قياسية بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
- Tue 17 Nov | YouTube | شقة للبيع 161 م كومباوند بالم هيلز - Palm Hills Alexandria
  https://youtu.be/VKY-tbMXNIM
  (page: did not load (429))
- Tue 17 Nov | جريدة المال | الأهلي فاروس: بالم هيلز تحافظ على قيمة عادلة عند 21.4 جنيه للسهم
  https://almalnews.com/2147896/الأهلي-فاروس-بالم-هيلز-تحافظ-على-قيمة/
  > أصدرت وحدة بحوث «الأهلي فاروس» تقريراً بشأن نتائج أعمال شركة «بالم هيلز للتعمير» خلال الأشهر التسعة الأولى من عام 2026، أكدت فيه إبقاءها على القيمة العادلة للسهم عند 21.4 جنيه مع الحفاظ على توصيتها القوية بـ شراء السهم، بما يمثل فرصة صعود تقارب 80% مقارنة بالمستويات الحالية، موضحة أن النتائج تعكس ضغوطاً واضحة لتكاليف الإنشاءات ... [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | almotawwer.com | «بالم هيلز» تحقق 214.1 مليار جنيه مبيعات خلال 9 أشهر بنمو 18%.. وياسين منصور يكشف تفاصيل الإنشاءات والتسليمات
  https://almotawwer.com/developers-and-builders/334362/
  > «بالم هيلز» تحقق 214.1 مليار جنيه مبيعات خلال 9 أشهر بنمو 18%.. وياسين منصور يكشف تفاصيل الإنشاءات والتسليمات ياسين منصور: 293 مليار جنيه أوراق قبض تدعم التدفقات النقدية المستقبلية.. وضخ 13 مليار جنيه في الإنشاءات وتسليم 1300 وحدة سكنية [Figures on the page: unaudited or preliminary; nine months. Check which one each figure is.]
- Mon 16 Nov | followict | ياسين منصور: بالم هيلز تضخ 13 مليار جنيه في الإنشاءات وتنهي 2,210 وحدة خلال 9 أشهر
  https://followict.news/ياسين-منصور-بالم-هيلز-تضخ-13-مليار-جنيه-ف/
- Mon 16 Nov | elnabaa elwatany newspaper | شركة بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه مصري
  https://www.elnabaa.net/1203650
- Mon 16 Nov | المصدر | بالم هيلز تحقق مبيعات بقيمة 214.1 مليار جنيه خلال 9 أشهر
  https://www.almasdar.com/176122
- Mon 16 Nov | شبكة تواصل الإخبارية | ياسين منصور: 293 مليار جنيه أوراق قبض توفر لبالم هيلز غطاءً نقديًا وتدعم خططها الإنشائية
  https://twaslnews1.twaslnews.com/7796579/
## SWDY  (8 leads)
- Tue 17 Nov | جريدة حابي | السويدي الوطنية: 70% نسبة المكون المحلي .. وخطة لسد فجوة استيراد المعدات
  https://hapijournal.com/2026/11/17/السويدي-الوطنية-70-نسبة-المكون-المحلي-و/
  > محمد أحمد _ قال المهندس تامر نافع، الرئيس التنفيذي لشركة السويدي الوطنية، التابعة لمجموعة السويدي إليكتريك، إن نسبة المكون المحلي في منتجات الشركة تصل إلى نحو 70%، مشيرًا إلى استمرار العمل على زيادتها من خلال فريق البحث والتطوير، الذي يتولى دراسة فرص توطين المزيد من المكونات وتطوير المنتجات.
- Tue 17 Nov | جريدة حابي | السويدي الوطنية تستهدف ضخ مليار جنيه استثمارات خلال 2027
  https://hapijournal.com/2026/11/17/السويدي-الوطنية-تستهدف-ضخ-مليار-جنيه-ا/
  > السويدي الوطنية تستهدف ضخ مليار جنيه استثمارات خلال 2027 تامر نافع: 6 مليارات جنيه مبيعات مستهدفة خلال 2027.. والتوسع في 40 دولة إفريقية
- Tue 17 Nov | بوابة التكنولوجيا المالية | «السويدي الوطنية» تستهدف ضخ مليار جنيه استثمارات وتحقيق 6 مليارات جنيه مبيعات خلال 2027
  https://fintechgate.net/257722
  (same wording as the جريدة حابي story above: one source, not two)
## ORAS  (8 leads)
- Wed 18 Nov | www.youlyou.com | أرباح أوراسكوم كونستراكشون تقفز 71% إلى 234.7 مليون دولار بأول 9 شهور من 2026
  https://www.youlyou.com/97145
  > 1- ارتفعت أرباح أوراسكوم كونستراكشون إلى 234.7 مليون دولار بنمو 71.1%. 2- صعدت الإيرادات إلى 4.78 مليار دولار خلال 9 شهور. 3- زادت الأرباح التشغيلية إلى 292.8 مليون دولار بنسبة 47.4%. 4- بلغ نصيب مساهمي الشركة الأم من الأرباح 218 مليون دولار. 5- ارتفعت ربحية السهم إلى 1.98 دولار مقابل 1.21 دولار. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | شبكة تواصل الإخبارية | أرباح «أوراسكوم كونستراكشون» المصرية تقفز 103% في الربع الثالث
  https://twaslnews1.twaslnews.com/7888823/
  (page: did not load (403))
- Wed 18 Nov | Forbes Middle East | Orascom Construction Profit Surges 96% To $218M
  https://forbesmiddleeast.com/industry/real-estate/orascom-constructions-nine-month-profit-nearly-doubles-to-$218m-as-backlog-hits-$116b
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## FWRY  (8 leads)
- Tue 17 Nov | CairoScene | Fawry Allocates $1.6 Million for Cybersecurity Investments
  https://cairoscene.com/Business/Fawry-Allocates-1-6-Million-for-Cybersecurity-Investments
  > Fawry Allocates $1.6 Million for Cybersecurity Investments The fintech company is directing LE 80 million towards technology upgrades by the end of 2026. Egyptian fintech company Fawry plans to allocate LE 80 million (approximately $1.6 million) towards technology investments by the end of 2026, prioritising cybersecurity and improvements to its digital infrastructure.
- Tue 17 Nov | بنكي | البنك العربى الافريقى الدولى يطلق عرضاً ترويجياً على القروض الشخصية بكاش باك فوري يصل إلى 100 ألف جنيه
  https://www.bankygate.com/202670
  > أطلق البنك العربى الافريقى الدولى عرضاً ترويجياً جديداً على القروض الشخصية، يتيح للعملاء الاستفادة من كاش باك فوري بنسبة 5%، يصل إلى 100 ألف جنيه مصري، وذلك في إطار حرص البنك على تقديم حلول تمويلية ومزايا حصرية تلبي احتياجات عملائه وتمنحهم المزيد من المرونة لتحقيق تطلعاتهم.
- Tue 17 Nov | اليوم السابع | كبار المستثمرين يقتنصون أسهم فوري ومصر للفنادق.. ويتخارجون من مرسيليا وباندا
  https://m.youm7.com/amp/2026/11/17/كبار-المستثمرين-يقتنصون-أسهم-فوري-ومصر-للفنادق-ويتخارجون-من-مرسيليا/7621720
  > كبار المستثمرين يقتنصون أسهم فوري ومصر للفنادق.. ويتخارجون من مرسيليا وباندا
- Tue 17 Nov | موقع متناهي | فوري تنجح في تحقيق أرباح بقيمة 2.88 مليار جنيه خلال 9 شهور
  https://motanahy.com/فوري-تنجح-في-تحقيق-أرباح-بقيمة-2-88-مليار-ج/
  > صعدت أرباح شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية بنسبة 32.7% خلال التسعة أشهر الأولى من العام الجاري لتصل 2.88 مليار جنيه . جاء ذلك مقارنة بربح 2.17 مليار جنيه خلال نفس الفترة من عام 2025. وفيما يخص حقوق مساهمي الشركة الأم، فقد سجلت الأرباح 2.69 مليار جنيه مقابل 2.04 مليار جنيه خلال فترة المقارنة. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Tue 17 Nov | موقع متناهي | أشرف صبري : "فوري" تدرس بشكل مبدئي ضح مليار جنيه في نشاط التخصيم خلال عام 2027
  https://motanahy.com/أشرف-صبري-فوري-تدرس-بشكل-مبدئي-ضح-مليا/
- Mon 16 Nov | EnterpriseAM | GB Corp’s income rises 9.9% in 3Q, Fawry’s climbs 37.5%
  https://enterpriseam.com/egypt/2026/11/17/gb-corps-income-rises-9-9-in-3q-fawrys-climbs-37-5/
- Mon 16 Nov | الحق والضلال | فوري تستعد لربط بطاقاتها الصفراء بتطبيق إنستاباي.. موعد الإتاحة
  https://www.christian-dogma.com/2305549
- Mon 16 Nov | CNN الاقتصادية | أرباح فوري المصرية تقفز 37% في الربع الثالث بدفعة من المدفوعات الرقمية
  https://cnnbusinessarabic.com/finance-markets/1152629/أرباح-فوري-المصرية-تقفز-37-في-الربع-الثالث-بدفعة-من-المدفوعات-الرقمية
## ABUK  (8 leads)
- Wed 18 Nov | ad-hoc-news.de | Abu Qir Fertilizers stock faces gas cost pressure through year-end
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/abu-qir-fertilizers-stock-faces-gas-cost-pressure-through-year-end/70529207
  > Abu Qir Fertilizers faces higher energy costs after Egypt adjusted the price of natural gas supplied to its plants from November 16 through December 31. The company disclosed the measure on Tuesday, November 17, in response to an inquiry from the Egyptian Exchange, according to Ahram Online.
- Tue 17 Nov | المصري اليوم | بعد أنباء زيادة الغاز بـ50%.. أول تعليق من «أبو قير للأسمدة» بشأن إنتاجها
  https://www.almasryalyoum.com/news/details/4412838
  > بعد أنباء زيادة الغاز بـ50%.. أول تعليق من «أبو قير للأسمدة» بشأن إنتاجها أعلنت شركة أبوقير للأسمدة والصناعات الكيماوية، تلقيها إخطارًا بتعديل سعر الغاز الطبيعي المورد لمصانعها، اعتبارًا من 16 نوفمبر الجاري، وحتى 31 ديسمبر المقبل، وذلك تعليقا على أنباء زيادة سعر الغاز لمصانع الأسمدة بنسبة 50%.
- Tue 17 Nov | Ahram Online | Egypt's Abu Qir Fertilizers confirms gas price hike through year-end - Energy - Business
  https://english.ahram.org.eg/News/582665.aspx
  (page: did not load (403))
## HRHO  (8 leads)
- Wed 18 Nov | TradingView | EFG Holding Q3 Consol Net Profit EGP 719.8 Million
  https://www.tradingview.com/news/reuters.com,2026:newsml_FWN46Y19U:0-efg-holding-q3-consol-net-profit-egp-719-8-million/
  (page: only 26 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Wed 18 Nov | شبكة تواصل الإخبارية | EFG Holding Reports Solid 3Q26 Revenues of EGP 6.7 Billion, Up 5% Y-o-Y Driven by Strong Performance at EFG Hermes and EFG Finance
  https://twaslnews1.twaslnews.com/7892165/
  (page: did not load (403))
- Wed 18 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page read: it never names the company, so probably not about it: skip)
## ALCN  (2 leads)
- Wed 18 Nov | ad-hoc-news.de | Alexandria Container stock posts 16% nine-month profit rise
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/alexandria-container-stock-posts-16-nine-month-profit-rise/70529211
  > Alexandria Container and Cargo Handling reported higher earnings for the nine months ended September 30, 2026, in a filing published by the Egyptian Exchange on November 15. Net income reached EGP 5,722.7 million, compared with EGP 4,951.8 million in the year-earlier period. Revenue increased to EGP 6,772.1 million from EGP 6,340.1 million. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | القاهرة 24 | الإسكندرية لتداول الحاويات تسجل تحفظًا محاسبيًا بشأن عقود حق الانتفاع بقيمة 3.4 مليار جنيه
  https://www.cairo24.com/2530264
  > الإسكندرية لتداول الحاويات تسجل تحفظًا محاسبيًا بشأن عقود حق الانتفاع بقيمة 3.4 مليار جنيه
## MFPC  (4 leads)
- Mon 16 Nov | Quantum Commodity Intelligence | Egyptian fertiliser producer Mopco sees 9M profits climb
  https://www.qcintel.com/ammonia/article/egyptian-fertiliser-producer-mopco-sees-9m-profits-climb-77634.html
  (page read: it never names the company, so probably not about it: skip)
- Mon 16 Nov | CNBC عربية | بدعم من نمو المبيعات.. أرباح "موبكو" المصرية ترتفع 56% في 9 أشهر
  https://www.cnbcarabia.com/159849/2026/15/11/بدعم-من-نمو-المبيعات..-أرباح-"موبكو"-المصرية-ترتفع-56--في-9-أشهر
  > ارتفعت الأرباح المجمعة لشركة مصر لإنتاج الأسمدة "موبكو" خلال الأشهر التسعة الأولى من العام بنسبة 56% لتصل إلى 12 مليار جنيه بعد خصم الضرائب، بدعم من زيادة المبيعات بنسبة 47% على أساس سنوي مسجلة نحو 27.5 مليار جنيه. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 16 Nov | Dealroom | MOPCO lands $165M loan for $265M plant overhaul
  https://app.dealroom.co/news/note/mopco-lands-165m-loan-for-265m-plant-overhaul
  (page: did not load (403))
## EFIH  (4 leads)
- Tue 17 Nov | موقع الحرية الإخباري | لتحديث منظومة المدفوعات.. «بنك ناصر» يوقع بروتوكول تعاون مع «e Novate» التابعة لـ «إي فاينانس»
  https://alhorianews.com/لتحديث-منظومة-المدفوعات-بنك-ناصر/
  > وقع بنك ناصر الاجتماعي، برئاسة الدكتورة مايا مرسي، وزيرة التضامن الاجتماعي ورئيسة مجلس إدارة البنك، بروتوكول تعاون مع شركة «e Novate» لتشغيل وإدارة الحلول الذكية للمدفوعات الرقمية، إحدى الشركات التابعة لمجموعة «إي فاينانس للاستثمارات المالية والرقمية»، وذلك في خطوة تستهدف تحديث الخدمات المالية والمصرفية للبنك ورفع كفاءة منظومة المدفوعات الإلكترونية.
- Tue 17 Nov | موقع الموقع | وزيرة التضامن تقود خطة تطوير الخدمات الرقمية ببنك ناصر بالتعاون مع «إي فاينانس»
  https://almawq3.com/وزيرة-التضامن-تقود-خطة-تطوير-الخدمات-ا/
  > وقع بنك ناصر الاجتماعي، برئاسة الدكتورة مايا مرسي، وزيرة التضامن الاجتماعي ورئيسة مجلس إدارة البنك، بروتوكول تعاون مع شركة «e Novate» المتخصصة في تشغيل وإدارة الحلول الذكية للمدفوعات الرقمية، وإحدى الشركات التابعة لشركة «إي فاينانس للاستثمارات المالية والرقمية»، وذلك في إطار خطة البنك لتطوير خدماته المالية والمصرفية، وتعزيز كفاءة منظومة المدفوعات الرقمية، ومواكبة التحول التكنولوجي ...
- Mon 16 Nov | موقع متناهي | رئيس مجموعة إي فاينانس يتوقع استكمال الإجراءات القانونية للاستحواذ على "تمويلي" خلال نوفمبر الجاري
  https://motanahy.com/رئيس-مجموعة-إي-فاينانس-يتوقع-استكمال-ا/
  > توقع إبراهيم سرحان رئيس مجلس الإدارة والعضو المنتدب في مجموعة إي فاينانس للاستثمارات المالية والرقمية استكمال الإجراءات القانونية للاستحواذ على “تمويلي” خلال نوفمبر الجاري . كما توقع مساهمة صفقة “تمويلي” بنحو 200 مليون جنيه في نتائج 2026 حال استكمالها.
## EMFD  (1 leads)
- Mon 16 Nov | FilFan | نيكول سابا تغني بالنظارة لـ"إعمار مصر"
  https://www.filfan.com/galleries/17385
  (page: only 16 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## BQDC  (7 leads)
- Tue 17 Nov | وكالة جراسا | بنك القاهرة عمان راعيًا فضيًا لجائزة الحسين لأبحاث السرطان لعام 2026
  https://www.gerasanews.com/article/611988
  > بنك القاهرة عمان راعيًا فضيًا لجائزة الحسين لأبحاث السرطان لعام 2026
- Mon 16 Nov | بوابة المصرف | 6,771 جنيهًا في شهر.. تفاصيل عائد 16.25% المعلن لودائع بنك القاهرة
  https://www.almasraf.news/6771-جنيهًا-في-شهر-تفاصيل-عائد-16-25-المعلن-لود/
  > أبرز تحديث لأسعار ودائع بنك القاهرة بالجنيه المصري عائدًا سنويًا يصل إلى 16.25% على الودائع لمدة شهر واحد، بحد أدنى يبلغ 500 ألف جنيه، ما يعادل نحو 6,771 جنيهًا خلال شهر عند صرف العائد في نهاية المدة، وفق حساب تقريبي يفترض تقسيم السنة إلى 12 شهرًا متساويًا.
- Mon 16 Nov | شبابيك | وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
  https://shbabbek.com/show/288015
  > وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
## EGAL  (2 leads)
- Mon 16 Nov | شبكة تواصل الإخبارية | اليوم.. نهاية حق توزيع 16 جنيهًا لسهم “مصر للألومنيوم”
  https://twaslnews1.twaslnews.com/7780978/
  (page: did not load (403))
- Mon 16 Nov | مجلة البوصلة الاقتصادية | اليوم.. نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم
  https://alboslanews.com/أسواق-مال/اليوم-نهاية-حق-الحصول-على-التوزيع-النقدي-لـ-مصر-للألومنيوم-430846
  > نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم الإثنين 16 نوفمبر 2026 -10:16 ينتهي مع ختام جلسة اليوم الإثنين حق الحصول على توزيع الكوبون النقدي لشركة مصر للألومنيوم، بواقع 16 جنيه للسهم. على أن يتم صرف التوزيع في 19 نوفمبر 2026، وتتولى التنفيذ شركة مصر للمقاصة والإيداع والقيد المركزي.
## SKPC  (1 leads)
- Tue 17 Nov | بترونيوز | بترومنت تجدد عقد الصيانة الشاملة مع سيدبك لتعزيز كفاءة التشغيل واستدامة الأصول
  https://petro-news.com/182015
  (page: did not load (403))
## EFID  (8 leads)
- Tue 17 Nov | Billionaires.Africa | Egyptian tycoon Hani Berzi's Edita posts 65% jump in nine-month profit
  https://www.billionaires.africa/2026/11/17/egyptian-tycoon-hani-berzis-edita-posts-65-jump-in-nine-month-profit/
  > Edita Food Industries SAE, the Egyptian snack maker founded and controlled by Hani Berzi, said profit for the first nine months of 2026 rose about 65% as record sales volumes lifted earnings despite pressure on margins in the third quarter. [Figures on the page: nine months; first half; one quarter; attributable to shareholders. Check which one each figure is.]
- Tue 17 Nov | CNN الاقتصادية | إيديتا لـCNN الاقتصادية: نتوقع مبيعات بـ27 مليار جنيه.. ونغيّر شبكة التوزيع في المغرب
  https://cnnbusinessarabic.com/finance-markets/1152802/إيديتا-لcnn-الاقتصادية-نتوقع-مبيعات-ب27-مليار-جنيه-ونغير-شبكة-التوزيع-في-المغرب
  > إيديتا لـCNN الاقتصادية: نتوقع مبيعات بـ27 مليار جنيه.. ونغيّر شبكة التوزيع في المغرب تاريخ النشر: قبل 17 ساعة آخر تعديل: قبل 15 ساعة
- Tue 17 Nov | Daily News Egypt | Edita’s Q3 profit jumps 41.5% on record sales
  https://dailynewsegypt.com/2026/11/16/editas-q3-profit-jumps-41-5-on-record-sales/
  > Edita Food Industries (EFID.CA), one of Egypt’s leading packaged snack-food makers, reported a 41.5% year-on-year rise in net profit to EGP 938.1m for the third quarter (Q3) of 2026. Revenues reached EGP 7.3bn, the highest quarterly figure in the company’s history. Q3 revenues rose 32.9% from the same quarter of 2025. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## AAPL  (8 leads)
- Wed 18 Nov | Yahoo Finance | A Retiree With $400,000 in His 401(k) Tries to Move Money Before Stocks Fall Further. Apple’s Widespread Outage Raises the Stakes of a Missed Trade
  https://finance.yahoo.com/markets/options/articles/retiree-400-000-401-k-030429558.html
  > - An AAPL outage costs a 401(k) investor little, since most plan funds price once daily at the close and phone exchanges bypass Apple. - Withdrawing $125,000 in cash to dodge a drop triggers about $8,000 in extra Social Security tax and Medicare surcharges, matching the feared loss.
- Tue 17 Nov | Reuters | Apple works to restore services after outage caused by internal update
  https://www.reuters.com/business/retail-consumer/apple-works-restore-services-after-outage-caused-by-internal-update-2026-11-17/
  (page: did not load (401))
- Tue 17 Nov | WTMJ | Apple joins a parade of technology hiccups in recent days
  https://wtmj.com/ap/ap-national/2026/11/17/apple-joins-a-parade-of-technology-hiccups-in-recent-days/
  > An update gone awry Tuesday at Apple followed a rash of major outages in recent days, including problems affecting the Federal Aviation Administration, United Airlines and Microsoft.
## MSFT  (8 leads)
- Wed 18 Nov | Investing.com India | Mizuho reiterates Microsoft stock rating on AI growth outlook By Investing.com
  https://in.investing.com/news/stock-market-news/mizuho-reiterates-microsoft-stock-rating-on-ai-growth-outlook-93CH-5711643
  (page: did not load (403))
- Wed 18 Nov | TIKR.com | Microsoft’s “Next Leg” Is Charging 500 Million Office Users More, Says RBC Analyst
  https://www.tikr.com/blog/microsofts-next-leg-is-charging-500-million-office-users-more-says-rbc-analyst
  > - Anthropic is giving away Office-style tools, but RBC analyst Rishi Jaluria says charging Microsoft’s roughly half a billion paying Office users more is the next leg of growth. - Microsoft’s September quarter backs him up: Microsoft 365 commercial cloud revenue grew 17% while seats grew 5%.
- Wed 18 Nov | www.marketscreener.com | Microsoft launches new specialized AI models to compete with Anthropic and OpenAI
  https://www.marketscreener.com/news/microsoft-launches-new-specialized-ai-models-to-compete-with-anthropic-and-openai-ce785edcdd80f623
  (page: did not load (403))
- Wed 18 Nov | marketscreener.com | Microsoft Corporation : JP Morgan gives a Buy rating
  https://www.marketscreener.com/news/microsoft-corporation-jp-morgan-gives-a-buy-rating-ce785edcd181f125
  (page: did not load (403))
- Wed 18 Nov | CryptoRank | Wrapped Microsoft Tokenized stock (xStock): Funding, Investors, Team and Key Events
  https://cryptorank.io/price/wrapped-microsoft-tokenized-stock-xstock
- Wed 18 Nov | Seeking Alpha | Microsoft: The Market Is Rewarding Financial Discipline, Not AI Monetization (NASDAQ:MSFT)
  https://seekingalpha.com/article/4969410-microsoft-the-market-is-rewarding-financial-discipline-not-ai-monetization
- Wed 18 Nov | Traders Union | Tokocrypto supports cash dividend distribution for Microsoft and Applied Materials tokenized stocks
  https://tradersunion.com/news/brokers-news/show/4295324-tokocrypto-to-distribute-stock-dividends/
- Wed 18 Nov | Yahoo Finance | Microsoft Stock Hits Seven-Week Low: Is a Bigger Drop Coming?
  https://finance.yahoo.com/markets/stocks/articles/microsoft-stock-hits-seven-week-022643923.html
## NVDA  (8 leads)
- Wed 18 Nov | Yahoo Finance | Nvidia Spending Pushes AI Data Center Infrastructure Stocks Into Focus
  https://finance.yahoo.com/technology/ai/articles/nvidia-spending-pushes-ai-data-070745601.html
  > Nvidia's huge Q3 beat, raised 2028 sales outlook and that eye catching US$150b buyback have turned the AI data center build out from a headline into a concrete spending plan. Capital is flowing into the plumbing behind AI, not just the chips in the spotlight.
- Wed 18 Nov | tastylive | Nvidia Isn’t the Problem. Why Are Stock Markets Really Falling?
  https://www.tastylive.com/news-insights/nvidia-isn-t-the-problem-why-are-stock-markets-really-falling-
  > Stock markets suffered another ugly day ahead of Nvidia’s third-quarter earnings report. Selling was broad across sectors and themes, though a few more stocks were in the green than at the start of the week.
- Wed 18 Nov | BBC | How important are Nvidia and Jensen Huang to the US economy?
  https://www.bbc.com/news/articles/c68798vdprwpo
  > How important are Nvidia and Jensen Huang to the US economy? Nvidia and its co-founder Jensen Huang have been at the centre of the Artificial Intelligence (AI) spending boom.
## AMZN  (8 leads)
- Wed 18 Nov | Yahoo Finance | A Rocket Failure Just Cost Amazon 40 Internet Satellites. It's Good News for SpaceX, but I'd Still Want a Lower Stock Price.
  https://finance.yahoo.com/markets/stocks/articles/rocket-failure-just-cost-amazon-030602654.html
  > A Rocket Failure Just Cost Amazon 40 Internet Satellites. It's Good News for SpaceX, but I'd Still Want a Lower Stock Price. Amazon (NASDAQ:AMZN) just lost a full rocket's worth of internet satellites.
- Wed 18 Nov | Simply Wall St | Will AI Champion Status Change Amazon Stock Narrative
  https://simplywall.st/stocks/us/retail/nasdaq-amzn/amazoncom/news/will-ai-champion-status-change-amazon-stock-narrative
  > Reports indicate Amazon.com is set to be named a U.S. artificial intelligence national champion and holds a large, non-controlling stake in Anthropic ahead of its IPO, deepening ties between AWS and a major AI customer.
- Wed 18 Nov | TheStreet | Peter Thiel makes new $161 million ETF bet, dethroning Amazon stock
  https://www.thestreet.com/investing/stocks/peter-thiel-161-million-dollar-ishares-semiconductor-etf
  (page: did not load (403))
## GOOGL  (8 leads)
- Wed 18 Nov | ad-hoc-news.de | Alphabet's Robotaxi Retreat and a $121 Billion AI Contract Collide With UBS Caution
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/alphabet-s-robotaxi-retreat-and-a-121-billion-ai-contract-collide-with-ubs-caution/70529523
  > Waymo pulled its robotaxis off U.S. highways on Tuesday, a day when Alphabet shares slipped 1.4% and a far larger number was making headlines elsewhere: a $121.3 billion compute commitment from Anthropic that cuts both ways for Google Cloud.
- Tue 17 Nov | Yahoo Finance | AI companies lost voters on narrative and execution, Alphabet's Porat says
  https://finance.yahoo.com/technology/ai/articles/ai-companies-lost-voters-narrative-200245609.html
  > Alphabet's longtime investment chief acknowledged that Google — and AI companies generally — have come up short convincing US voters that the trillions of dollars being plowed into data centers across the country are worth the cost.
- Tue 17 Nov | Kalkine Media | Will Alphabet (NASDAQ:GOOGL) Keep Moving Forward From Here?
  https://kalkinemedia.com/us/stocks/technical-analysis/will-alphabet-nasdaqgoogl-keep-moving-forward-from-here
  > - Alphabet shares have declined sharply as the government appeals the remedy ruling in the landmark search antitrust case, adding a fresh layer of legal uncertainty to the stock's chart dynamics.
## META  (8 leads)
- Wed 18 Nov | Investing.com Canada | Meta Platforms COO Javier Olivan sells $1 million in shares By Investing.com
  https://ca.investing.com/news/stock-market-news/meta-platforms-coo-javier-olivan-sells-1-million-in-shares-93CH-4965679
  (page: did not load (403))
- Wed 18 Nov | Investing.com Nigeria | Form 4 Meta Platforms Inc: Javier Olivan (COO) For: 15 November
  https://ng.investing.com/news/stock-market-news/form-4-meta-platforms-inc-javier-olivan-coo-for-15-november-93CH-2814652
  (page: did not load (403))
- Wed 18 Nov | Investing.com India | Form 4 Meta Platforms Inc: John Douglas Arnold (Director) For: 15 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-meta-platforms-inc-john-douglas-arnold-director-for-15-november-93CH-5711378
  (page: did not load (403))
## TSLA  (8 leads)
- Wed 18 Nov | TipRanks | Hanwha Investment & Securities Files Documents for KRW 50 Billion Tesla-Linked ELS
  https://www.tipranks.com/news/company-announcements/hanwha-investment-securities-files-documents-for-krw-50-billion-tesla-linked-els
  (page: did not load (403))
- Wed 18 Nov | shattered.io | Musk: Of Course $1.6T Tesla Prices In Cybercab
  https://shattered.io/musk-of-course-tesla-1-6-trillion-prices-in-moderate-cybercab-success/
  > Elon Musk spent two words on a $1.6 trillion argument. According to reports from Yahoo Finance, 36Kr, ArenaEV and USA Today, an X post dated November 16, 2026 said that “Moderate Cybercab success is already priced into $TSLA at $1.6T.” Musk’s reported reply was “Of course.”
- Wed 18 Nov | Yahoo Finance | “Of Course,” Musk Says When Told Tesla’s $1.6 Trillion Already Prices In Moderate Cybercab Success.
  https://finance.yahoo.com/markets/stocks/articles/course-musk-says-told-tesla-031857554.html
  > - Elon Musk replied "Of course" to an X post saying moderate Cybercab success is already priced into Tesla at $1.6 trillion. - That raises the bar for Cybercab to deliver further upside for Tesla shares. - Tesla traded at 178x forward earnings on Nov. 13, against a five-year average of 108x.
## JPM  (8 leads)
- Wed 18 Nov | AzerNews | Hackers threaten to leak alleged Visa and JPMorgan Chase data within 48 hours
  https://www.azernews.az/region/267619.html
  > Hackers threaten to leak alleged Visa and JPMorgan Chase data within 48 hours A newly emerged ransomware group known as n0n has threatened to publish allegedly stolen data belonging to global financial giants Visa and JPMorgan Chase unless negotiations take place within 48 hours.
- Wed 18 Nov | Benzinga | ‘Not Under Systemic Attack’: Marco Rubio Says ‘Zero Evidence’ Microsoft, JPMorgan and FAA Outages Due to
  https://www.benzinga.com/news/politics/26/11/63375808/not-under-systemic-attack-marco-rubio-says-zero-evidence-microsoft-jpmorgan-and-faa-outages-due-to-hostile-actors
  (page: did not load (403))
- Wed 18 Nov | The SOFX Report | JPMorgan Chase Software Bug Disrupts U.S. Banking, Spilling Into Zelle Transfer Rails
  https://www.sofx.com/jpmorgan-chase-software-bug-disrupts-u-s-banking-spilling-into-zelle-transfer-rails/
  > JPMorgan Chase said a software bug in its on-premise hardware, not a cyberattack, disrupted online banking and transactions across the US on Monday. An FBI official told Fox Business the fault came from a Monday software release, hitting only Chase and transactions with it.
- Tue 17 Nov | CNBC | JPMorgan is working on AI agent transactions that don’t involve humans
  https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html
  > Artificial intelligence agents have already proven to be helpful, or cause a lot of trouble, or both. One area seen as high-potential is in payments, where — if they're able to be trusted — the agents could deal with all sorts of money matters on behalf of people.
- Tue 17 Nov | StreetInsider | Guarantor: JPMorgan Chase & Co.
  https://www.streetinsider.com/SEC+Filings/Form+424B2+JPMORGAN+CHASE+&amp;+CO/27364809.html
- Tue 17 Nov | Global Banking & Finance Review | JPMorgan Chase falls 2.47% in Tuesday's session
  https://www.globalbankingandfinance.com/jpmorgan-chase-jpm-falls-2026-11-17/
- Tue 17 Nov | StreetInsider | Form FWP JPMORGAN CHASE & CO Filed by: JPMORGAN CHASE & CO
  https://www.streetinsider.com/SEC+Filings/Form+FWP+JPMORGAN+CHASE+&amp;+CO+Filed+by:+JPMORGAN+CHASE+&amp;+CO/27364411.html
- Tue 17 Nov | Yahoo Finance | JPMorgan’s CFO plans exit, company names internal successor
  https://finance.yahoo.com/markets/stocks/articles/jpmorgan-cfo-plans-exit-company-190454860.html
## XOM  (8 leads)
- Wed 18 Nov | Independent Newspaper Nigeria | ExxonMobil Deepens Push For Women’s Inclusion In Nigeria’s Energy Sector
  https://independent.ng/exxonmobil-deepens-push-for-womens-inclusion-in-nigerias-energy-sector/
  > ating as Esso Nigeria, have reaffirmed their commitment to increasing women’s participation in the energy industry through targeted inclusion initiatives, mentorship programmes and expanded business opportunities for women-owned enterprises.
- Wed 18 Nov | Offshore Technology | SBM Offshore wins FPSO contracts from ExxonMobil for Longtail project
  https://www.offshore-technology.com/news/sbm-offshore-fpso-exxonmobil-longtail/
  (page: did not load (403))
- Wed 18 Nov | iMarine | Saipem Receives Authorization to Proceed with ExxonMobil Guyana's Longtail SURF Project
  https://www.imarinenews.com/41005.html
  > Saipem has received from ExxonMobil Guyana Limited the authorization to proceed with the execution of the Longtail project, located in the Stabroek Block offshore Guyana, at a water depth of approximately 1,750 meters.
## AVGO  (8 leads)
- Wed 18 Nov | TIKR.com | Good News for Nvidia and Broadcom: Anthropic’s IPO Brings “$60, $80 Billion of New Capital”
  https://www.tikr.com/blog/good-news-for-nvidia-and-broadcom-anthropics-ipo-brings-60-80-billion-of-new-capital
  > - Anthropic’s IPO is expected to price on Nov. 18, and Cerity Partners’ Jim Lebenthal estimates it could bring in $60 billion to $80 billion of new capital. - That cash makes it more likely that Anthropic pays for the chips and compute that Nvidia’s and Broadcom’s growth forecasts count on.
- Wed 18 Nov | MarketBeat | Broadcom Inc. (AVGO) - What Are Analysts Saying About This Stock?
  https://www.marketbeat.com/instant-alerts/consensus-broadcom-inc-avgo-what-are-analysts-saying-about-this-stock-2026-11-18/
  > (AVGO) - What Are Analysts Saying About This Stock? - Analyst sentiment is broadly positive: Broadcom has a “Moderate Buy” consensus from 45 analysts, with an average 12-month price target of $525.19. - Quarterly results beat estimates: Broadcom reported earnings of $3.32 per share versus $3.22 expected, and revenue of $29.59 billion versus $29.24 billion.
- Wed 18 Nov | Benzinga | Micron Technology Shares Jump 4.69% After Hours - Taiwan Semiconductor (NYSE:TSM), Broadcom (NASDAQ:AVGO)
  https://www.benzinga.com/markets/equities/26/11/63375731/micron-technology-shares-after-hours-ai-chip-rally
  (page: did not load (403))
- Wed 18 Nov | TradingKey | Today’s Market Recap: Three Major US Indexes Tumble, Broadcom and Arm Buck Trend, Nvidia Earnings Beat Expectations
  https://www.tradingkey.com/analysis/stocks/us-stocks/262310037-us-tightens-ai-chip-remote-access-rules-nvidia-amd-apec-oil-xau-xag-gold-tradingkey
  > Today’s Market Recap: Three Major US Indexes Tumble, Broadcom and Arm Buck Trend, Nvidia Earnings Beat Expectations equities pulled back broadly as the Dow fell 1.64%, the S&P 500 dropped 1.03%, and the Nasdaq declined 0.74% amid cautious investor sentiment. Semiconductor stocks diverged, while Nvidia posted record third-quarter revenue exceeding $115 billion with strong guidance.
- Tue 17 Nov | TIKR.com | TD Cowen Cut Its Broadcom Target to $425. It Still Sees 24% Upside
  https://www.tikr.com/blog/td-cowen-cut-its-broadcom-target-to-425-it-still-sees-24-upside?ref=yahoofinance&tlnk=yf-261117-7jhqfrh2
- Tue 17 Nov | Simply Wall St | Broadcom (AVGO) Stock Looks Undervalued As AI Cash Flow Hopes Build
  https://simplywall.st/stocks/us/semiconductors/nasdaq-avgo/broadcom/news/broadcom-avgo-stock-looks-undervalued-as-ai-cash-flow-hopes
- Tue 17 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Shares Climb 2.5% - Should You Buy?
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-shares-climb-25-should-you-buy-2026-11-17/
- Tue 17 Nov | Yahoo Finance | AMD, Broadcom, CoreWeave stocks rise on Nvidia earnings beat
  https://finance.yahoo.com/markets/stocks/article/amd-broadcom-tsmc-stocks-rise-on-nvidia-earnings-coreweave-nebius-shares-also-rally-220159436.html
## BRK.B  (8 leads)
- Wed 18 Nov | 2oceansvibe News | Buffett Gives R93 Billion Away, Then Offers Advice
  https://www.2oceansvibe.com/business/warren-buffett-donation-kindness-november-2026/
  > Warren Buffett has announced another enormous charitable gift, pairing Berkshire Hathaway shares reportedly worth $5.5 billion (R93.3 billion) with a Thanksgiving letter about the people who helped him along the way. The 96-year-old investor’s donation goes to four family foundations, CBS News reports.
- Wed 18 Nov | Yahoo Finance | Berkshire Hathaway (BRK.B) Reveals New Stake And Nearly Doubles One Holding
  https://finance.yahoo.com/markets/stocks/articles/berkshire-hathaway-brk-b-reveals-052028795.html
  > - Berkshire Hathaway (NYSE: BRK.B) has disclosed a new stake in Bending Spoons, the parent of AOL, in its latest filing. - The conglomerate has nearly doubled its holding in homebuilder Lennar, signaling increased capital allocated to the housing sector.
- Wed 18 Nov | Investing.com India | Form 13D/A Berkshire Hathaway Inc. For: 17 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-13da-berkshire-hathaway-inc-for-17-november-93CH-5711363
  (page: did not load (403))
## WMT  (8 leads)
- Wed 18 Nov | Florida Daily | Walmart Gains Market Share as Online Sales Surge, but Lower-Income Shoppers Pull Back
  https://floridadaily.com/walmart-gains-market-share-as-online-sales-surge-but-lower-income-shoppers-pull-back/
  > Walmart continues to expand its share of the consumer goods market, driven by strong online sales and growing demand among higher-income households. However, new consumer spending data suggests the retail giant is losing ground with lower-income shoppers who are increasingly turning to competitors.
- Wed 18 Nov | StockStory | Walmart to report earnings tomorrow: Here is what to expect
  https://stockstory.org/us/stocks/nasdaq/wmt/news/earnings/walmart-to-report-earnings-tomorrow-here-is-what-to-expect
  > Retail behemoth Walmart (NASDAQ:WMT) will be reporting results this Thursday before market hours. Here’s what to expect. Walmart beat analysts’ revenue expectations last quarter, reporting revenues of $187.9 billion, up 5.9% year on year. Is Walmart a buy or sell going into earnings?
- Tue 17 Nov | Kalkine Media | Will Walmart (NYSE:WMT) Impress In Its Next Release?
  https://kalkinemedia.com/us/stocks/bluechip/will-walmart-nysewmt-impress-in-its-next-release
  > - The retailer updates in a week treated as a litmus test of holiday spending - Value-seeking shoppers keep crowding the aisles amid a cautious consumer backdrop Walmart (NYSE:WMT) WMT (NYSE:WMT) is back in focus after its latest company update.
## V  (8 leads)
- Wed 18 Nov | Seeking Alpha | Visa expands Agentic Ready program to merchants and PSPs with 140+ launch participants
  https://seekingalpha.com/news/4673991-visa-expands-agentic-ready-program-to-merchants-and-psps-with-140-launch-participants
  (page: did not load (403))
- Wed 18 Nov | Stock Titan | PayPal and Stripe join Visa to help merchants prepare for AI agents that buy things
  https://www.stocktitan.net/news/V/visa-expands-agentic-ready-to-help-scale-trusted-ai-commerce-b69gvbg78sva.html
  > Visa Expands Agentic Ready to Help Scale Trusted AI Commerce Globally Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Tue 17 Nov | Yahoo Finance UK | VISA INC-CLASS A (V-USD.SW) Analyst insights, Price targets and Recommendations
  https://uk.finance.yahoo.com/quote/V-USD.SW/analyst-insights/
  (page: did not load (404))
- Tue 17 Nov | Blockonomi | Visa (V) Stock: Slides as New Report Reveals 62% Rise in Cyberattacks
  https://blockonomi.com/visa-v-stock-slides-as-new-report-reveals-62-rise-in-cyberattacks/
  > - Visa shares drop 1.49% to $420.12 as its latest fraud report exposes new risks. - Third-party security incidents jump 62%, exposing weaknesses in payment networks. - Visa links third-party providers to 56% of compromised payment credentials. - Visa identifies over $1.4 billion in potential scams, up 40% in six months.
- Tue 17 Nov | Blockchain News | Visa (V) Stock Price Prediction: Visa holds near short-term support as analysts lift targets and traders lean slightly bullish
  https://blockchain.news/news/20261117-price-prediction-v-visa-holds-near-short-term-support
- Tue 17 Nov | ad-hoc-news.de | Visa stock: Citigroup raises price target to USD 490
  https://www.ad-hoc-news.de/boerse/news/corporate-news/visa-stock-citigroup-raises-price-target-to-usd-490/70527666
- Tue 17 Nov | Stock Titan | Visa identified more than $1.4 billion in potential fraud. Scam activity rose 40% in six months.
  https://www.stocktitan.net/news/V/visa-report-ai-enabled-fraud-and-third-party-attacks-are-scaling-jay6w7l9mknr.html
- Tue 17 Nov | Traders Union | Visa stock weekly forecast: Holds gains above key moving averages as traders eye momentum persistence
  https://tradersunion.com/news/stocks/show/4285891-visa-gains-0-16percent-over-the/
## ORCL  (8 leads)
- Wed 18 Nov | JournalArta | Oracle (ORCL) Stock: $115.00, Down 3.43% Nov 17
  https://journalarta.com/en/2026/11/18/oracle-orcl-stock-slides-3-43-november-17-2026-down-12-3-in-a-month/
  > Oracle (ORCL) Stock Slides 3.43% (November 17, 2026): Down 12.3% in a Month Technical analysis of ORCL stock on November 17, 2026: price 115.00 USD, trend downtrend, RSI 40.0, support 115.00, resistance 144.54. Oracle’s Tuesday close lands squarely on the fault line of its recent range — a test international investors should watch closely.
- Wed 18 Nov | Business Upturn | Oracle Financial Services Software allots 21,253 equity shares under stock plan
  https://businessupturn.com/business/oracle-financial-services-software-allots-21-253-equity-shares-under-stock-plan/
  > Oracle Financial Services Software Limited has announced the allotment of 21,253 equity shares to its eligible employees. This decision was approved by the ESOP Allotment Committee of the Board of Directors on 18 November 2026. 5, were allotted pursuant to the exercise of stock options under the OFSS Stock Plan 2014.
- Wed 18 Nov | Kalkine Media | Oracle Financial Services Software (NSE:OFSS) ESOP Share Allotment: Key Details and Investor Impact
  https://kalkinemedia.com/in/news/announcements/oracle-financial-services-software-nseofss-esop-share-allotment-key-details-and-investor-impact
  > On 18 November 2026, Oracle Financial Services Software (NSE:OFSS) OFSS (NSE:OFSS) notified the National Stock Exchange about its ESOP Allotment Committee's approval to allot 21,253 equity shares with a face value of Rs 5 each to eligible employees under the OFSS Stock Plan 2014.
- Wed 18 Nov | FXLeaders | ORCL Stock Heads to $100 as APLD Pushes Oracle for Financial Guarantees on Data-Centre Costs
  https://www.fxleaders.com/news/2026/11/17/orcl-stock-heads-to-100-as-apld-pushes-oracle-for-financial-guarantees-on-data-centre-costs/
  > ORCL Stock Heads to $100 as APLD Pushes Oracle for Financial Guarantees on Data-Centre Costs Oracle (NYSE: ORCL) faces selling pressure as Democratic midterm victories, rising data-centre infrastructure costs, a $20 billion funding package and execution delays intensify concerns about its debt burden and cloud expansion.
- Tue 17 Nov | MarketBeat | Oracle (NYSE:ORCL) Stock Price Down 3.4% - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-price-down-34-time-to-sell-2026-11-17/
- Tue 17 Nov | GuruFocus | Is Oracle Corp (ORCL) a Bargain After 3.4% Drop? GF Value Says U
  https://www.gurufocus.com/news/9206055/is-oracle-corp-orcl-a-bargain-after-34-drop-gf-value-says-undervalued
- Tue 17 Nov | 재경일보 | Oracle Shares Drop 3.4% as AI Data Center Costs and Local Resistance Draw Scrutiny : Finance : JKN
  https://news.jkn.co.kr/editions/english/post/1103146
- Tue 17 Nov | TradingView | Navan, Netskope, Vertex, Liftoff Mobile, and Oracle stocks trade down, what you need to know
  https://www.tradingview.com/news/stockstory:c64309089094b:0-navan-netskope-vertex-liftoff-mobile-and-oracle-stocks-trade-down-what-you-need-to-know/
## COST  (8 leads)
- Wed 18 Nov | TIKR.com | Costco Is Up 22% in a Year. Mizuho Sees Another 4%
  https://www.tikr.com/blog/costco-is-up-22-in-a-year-mizuho-sees-another-4
  > - Mizuho raised its Costco price target to $1,150 from $1,100 and kept its Outperform rating, but took the stock off its Top Pick list after its run. - Mizuho’s case is about sales: it thinks Costco’s U.S. comparable sales could top 10% in November.
- Wed 18 Nov | TIKR.com | Costco Is Near Its High. Bank of America Sees Another 13%
  https://www.tikr.com/blog/costco-is-near-its-high-bank-of-america-sees-another-13
  > 13, Bank of America raised its Costco price target to $1,257 from $1,095 and kept its Buy rating, 13% above the Nov. - Costco’s business is doing well: fourth-quarter comparable sales grew 6.7% excluding gas and currency, and a $30-a-share special dividend is on the way.
- Wed 18 Nov | Pluang | Costco's $10K investment in 1997 is now worth $833K with a $22.5K special dividend coming Dec 4.
  https://pluang.com/en/news-feed/charlie-munger-tidak-pernah-jual-saham-costco-dividen-spesial-2026
  (page: did not load (403))
## NFLX  (8 leads)
- Wed 18 Nov | JournalArta | Netflix (NFLX) Stock: $59.68, Down 1.76% Nov 17
  https://journalarta.com/en/2026/11/18/netflix-nflx-stock-falls-1-76-on-tuesday-down-13-1-in-a-month/
  > Netflix (NFLX) Stock Falls 1.76% on Tuesday, Down 13.1% in a Month Technical analysis of NFLX stock on November 17, 2026: price 59.68 USD, trend downtrend, RSI 33.0, support 59.68, resistance 67.05.
- Wed 18 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Shares Unloaded by Rep. Byron Donalds
  https://www.marketbeat.com/instant-alerts/congress-netflix-nasdaq-nflx-shares-unloaded-by-rep-byron-donalds-2026-11-18/
  > Netflix (NASDAQ:NFLX) Shares Unloaded by Rep. Byron Donalds disclosed selling $1,001–$15,000 of Netflix shares on October 2 from his MORAN WEALTH IRA. - Netflix shares opened at $59.68, near a reported one-year low of $59.40 and well below their $115.25 high. Analysts’ consensus remains “Moderate Buy,” with an average price target of $89.14. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Wed 18 Nov | Yahoo Finance | Michael Burry Passed On Nvidia Calls Before Earnings — Here’s What Caught His Eye At Alibaba, Netflix And JD
  https://finance.yahoo.com/markets/stocks/articles/michael-burry-passed-nvidia-calls-051535966.html
  > Michael Burry Passed On Nvidia Calls Before Earnings — Here’s What Caught His Eye At Alibaba, Netflix And JD - Michael Burry passed on Nvidia calls before earnings and held $140 puts expiring in February 2027.
## INTC  (8 leads)
- Wed 18 Nov | Stocktwits | INTC: Intel Corp Latest Stock Price, Analysis, News and Trading Ideas
  https://stocktwits.com/symbol/INTC
  > engages in the design, manufacture, and sale of computer products and technologies. It delivers computer, networking, data storage, and communications platforms. The firm operates through the following segments: Client Computing Group (CCG), Data Center and AI (DCAI), Intel Foundry Services (IFS), and All Other.
- Tue 17 Nov | CFO Dive | Intel shareholders sue CEO, CFO after stock rout
  https://www.cfodive.com/news/intel-shareholders-sue-ceo-cfo-stock-drop-ai-cpu/874979/
  (page: did not load (403))
- Tue 17 Nov | Yahoo Finance | Intel Stock Has Given Back About 60% Since June. Is It a Buy Now?
  https://finance.yahoo.com/markets/stocks/articles/intel-stock-given-back-60-215701490.html
  > Intel (NASDAQ:INTC) stock closed at a record of about $141 on June 22. As I write, it trades near $56, about 60% lower. 16, when shares fell 6% or more by late morning. Missed Nvidia in 2009? In 2009, a "Double Down" signal flashed for a little-known chipmaker called Nvidia. [Figures on the page: nine months; first half; one quarter. Check which one each figure is.]
## LLY  (8 leads)
- Wed 18 Nov | TIKR.com | Eli Lilly Is Up 39% in a Year. Barclays Sees Another 9%
  https://www.tikr.com/blog/eli-lilly-is-up-39-in-a-year-barclays-sees-another-9
  > - Barclays raised its Eli Lilly price target to $1,550 from $1,400 and kept its Overweight rating, with the stock close to a 52-week high. - Lilly’s third-quarter revenue rose 39% to $24.4 billion because it sold 53% more, which more than made up for a 15% drop in realized prices.
- Wed 18 Nov | Reuters | Breakingviews - COMMENTARY: Eli Lilly’s $1.4 trln valuation is heavy with hope
  https://www.reuters.com/commentary/breakingviews/eli-lillys-14-trln-valuation-is-heavy-with-hope-2026-11-18/
  (page: did not load (401))
- Wed 18 Nov | Kalkine Media | Eli Lilly Director Jon R. Moeller Purchases 167.6364 Shares on November 16, 2026
  https://kalkinemedia.com/us/news/announcements/eli-lilly-director-jon-r-moeller-purchases-1676364-shares-on-november-16-2026
  > On November 17, 2026, Director Jon R. Moeller submitted a Form 4 to the SEC, revealing his purchase of Eli Lilly common stock on November 16, 2026. Moeller, Director at Eli Lilly & Co (NYSE:LLY) LLY (NYSE:LLY) . - Transaction Type: Acquisition (code A) of 167.6364 shares on November 16, 2026.
Read 96 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, JUFO, EAST, AMOC.
