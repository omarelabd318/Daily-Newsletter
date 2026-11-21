# Desk brief, Saturday, November 21, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 92s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-20 (35.89); Treasury yields to 2026-11-20 (10-year 4.92%).
- **valuation**: ok in 20s (GitHub Actions). LLY: $1.27tn, P/E (last 12 months) 42.2, Forecast P/E (fiscal 2026) 37.8 (the four quarters to Sep 2026)
- **movers**: ok in 21s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 turning down, RSI 49.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.0%, median P/E 10.0; cheapest MASR +74%, PHAR +48%, MFPC +44%; dearest ARAB -62%, MOIN -65%, BTFH -68%
- **views**: ok in 0s (GitHub Actions). 2026-11-05-brent-hormuz: on track -> right  (Judged on its date: Brent at 92.57 from 94.62 (-2.2%).)
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 107s (GitHub Actions). 
- **leads**: ok in 79s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 1 needed a retry.

## What moved (latest close against the one before)
- EGX30 51,458.00 (-0.17%); EGX70 EWI 17,505.80 (-0.33%); USD/EGP 53.81 (-0.12%); Gold 21K 5,460.00 (-3.79%); Brent 92.57 (+0.64%); S&P 500 6,910.39 (-3.70%); Nasdaq 22,617.73 (-5.28%); Bitcoin 57,837.00 (-5.99%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): NVDA -14.0%, AVGO -12.2%, ORCL -8.5%, INTC -8.0%, TSLA -7.6%, META -5.9%, AMZN -4.1%, ETEL -3.5%, JPM -3.0%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - AMZN: No clear trend: 3.2% below its 50-day average and 0.7% above the 200-day; RSI 42, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - GOOGL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 28, washed out: below 30; momentum turned down today (MACD crossed its signal line).
    - INTC: Turning down: below both its 50-day average (43.2% under) and its 200-day (41.4% under), though the 50-day is still above the 200-day; RSI 28, washed out: below 30; momentum turned up 2 sessions ago (MACD crossed its signal line).
    - META: Turning down: below both its 50-day average (17.1% under) and its 200-day (10.8% under), though the 50-day is still above the 200-day; RSI 30, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - NFLX: In a downtrend: below its 50-day average, which is below the 200-day; RSI 27, washed out: below 30; momentum turned down 3 sessions ago (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (39.4% under) and its 200-day (38.3% under), though the 50-day is still above the 200-day; RSI 15, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- US GPN (Global Payments) +9.9%; US NBIS (Nebius Group) -16.1%; US CLS (Celestica) -16.1%; US SNDK (Sandisk) -16.1%; US BE (Bloom Energy) -15.3%; US CRDO (Credo Technology Group Holding) -15.2%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-19 (TradingView's closes; Mubasher's list refused), 200 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (212)
US: 2026-11-20, 812 companies
US week and month: US companies worth $10bn or more (810)
EGX30 heatmap: 2026-11-19, 31 members
US heatmap: 2026-11-20, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-19
## ZEOT +17.0%  Extracted Oils & Derivatives
- no headlines found
## MOSC +12.0%  Misr Oils & Soap
- no headlines found
## VERT +10.0%  Vertika for Industry & Trade
- no headlines found
## COSG +9.3%  Cairo Oils & Soap
- no headlines found
## FIRE +8.2%  First Investment & Real Estate Development
- no headlines found
## ADRI -5.1%  Arab Development & Real Estate Investment
- no headlines found
## ICFC -5.0%  International Co. for Fertilizers & Chemicals
- no headlines found
## EASB -4.9%  Egyptian Arabian Company for Securities Brokerage EAC
- no headlines found
## AMER -4.8%  Amer Group Holding
- no headlines found
## NINH -4.7%  Nozha International Hospital
- no headlines found

# US 2026-11-20
## GPN +9.9%  Global Payments
- Sat 21 Nov | Yahoo Finance | Global Payments (GPN) Gets a Potential Lifeline as New Takeover Buzz Heats Up
  https://finance.yahoo.com/markets/stocks/articles/global-payments-gpn-gets-potential-065105957.html
  > (NYSE:GPN) is one of the 10 Stocks With Monster Gains Amid Market Turmoil. (NYSE:GPN) soared by 9.95 percent on Friday to end at $91.83 apiece, as investor sentiment was bolstered by news that its largest shareholder, GTCR, is weighing a full takeover of the company for $50 billion.
- Sat 21 Nov | Yahoo! Finance Canada | Global Payments Inc. (GPN) Stock Forecasts
  https://ca.finance.yahoo.com/research/reports/MS_0P000002G8_AnalystReport_1795207236000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | GuruFocus | A Look at Global Payments Inc (GPN) After 9.9% Gain -- GF Value $121.89 vs Price $91.83
  https://www.gurufocus.com/news/9213621/a-look-at-global-payments-inc-gpn-after-99-gain-gf-value-12189-vs-price-9183
  (page: did not load (403))
- Sat 21 Nov | Crain's Chicago Business | GTCR weighs $50 billion Global Payments buyout
  https://www.chicagobusiness.com/banking-finance/ccb-gtcr-global-payments-buyout-20261120/
  (page: did not load (403))
## BIP +4.5%  Brookfield Infrastructure Partners L.P
- Sat 21 Nov | Yahoo Finance | Brookfield Infrastructure (BIPC) Is Getting Wall Street Excited — Here’s Why
  https://finance.yahoo.com/markets/stocks/articles/brookfield-infrastructure-bipc-getting-wall-071324504.html
- Sat 21 Nov | GuruFocus | Brookfield Infrastructure Partners LP (BIP) Stock Up 4.2% but GF Value Says Overvalued -- GF Score: 83/100
  https://www.gurufocus.com/news/9213642/brookfield-infrastructure-partners-lp-bip-stock-up-42-but-gf-value-says-overvalued-gf-score-83100
- Sat 21 Nov | Timothy Sykes | Brookfield Infrastructure Partners LP Limited Partnership Units (BIP) Stock Price | Live Quotes & Charts | NYSE
  https://www.timothysykes.com/quote/BIP/
- Fri 20 Nov | MarketBeat | Brookfield Infrastructure Partners LP (NYSE:BIP) Shares to Pay Quarterly Dividend of $0.46
  https://www.marketbeat.com/instant-alerts/dividend-brookfield-infrastructure-partners-lp-nyse-bip-shares-to-pay-quarterly-dividend-of-046-2026-11-20/
## RKT +4.2%  Rocket Companies
- Sat 21 Nov | Yahoo Finance Singapore | Rocket Companies, Inc. (RKT) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance | Rocket Companies (RKT) Just Got a Major Win — Wall Street Is Reacting
  https://finance.yahoo.com/markets/stocks/articles/rocket-companies-rkt-just-got-071103140.html
- Sat 21 Nov | GuruFocus | Rocket Companies Inc (RKT) Shares Surge 4.2% -- What GF Score of 65 Tells Investors
  https://www.gurufocus.com/news/9213506/rocket-companies-inc-rkt-shares-surge-42-what-gf-score-of-65-tells-investors
- Fri 20 Nov | Stock Titan | Daniel Gilbert put Rocket Companies (RKT) shares into a trust he oversees as part of estate planning.
  https://www.stocktitan.net/sec-filings/RKT/form-3-rocket-companies-inc-initial-statement-of-beneficial-ownership-cdcbc3f791c3.html
## MKC.V +3.8%  McCormick & Company, Incorporated
- Sat 21 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Stock Breaks Above 50 Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-stock-breaks-above-50-day-moving-average-whats-next-2026-11-21/
- Sat 21 Nov | Timothy Sykes | McCormick & Company Incorporated (MKC) Stock Price | Live Quotes & Charts | NYSE
  https://www.timothysykes.com/quote/MKC/
- Fri 20 Nov | kalkine.ca | McCormick & Company Incorporated (NYSE: MKC.V) Stock Price, News & Analysis
  https://kalkine.ca/company/nyse-mkc-v/
- Fri 20 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Shares Climb 4.8% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-shares-climb-48-heres-why-2026-11-20/
## GIS +3.7%  General Mills
- Sat 21 Nov | Yahoo Finance | General Mills (GIS) is Suddenly Drawing Wall Street’s Attention
  https://finance.yahoo.com/markets/stocks/articles/general-mills-gis-suddenly-drawing-071603982.html
- Fri 20 Nov | MarketWatch | General Mills Inc. stock outperforms competitors on strong trading day
  https://www.marketwatch.com/data-news/general-mills-inc-stock-outperforms-competitors-on-strong-trading-day-843bf29a-db3de02c90f1?mod=goog_fin_scmw
- Fri 20 Nov | Barchart.com | B&G Foods, Monster, Conagra, General Mills, and Post stocks trade up, what you need to know
  https://www.barchart.com/story/news/8942102/bg-foods-monster-conagra-general-mills-and-post-stocks-trade-up-what-you-need-to-know
- Fri 20 Nov | Yahoo Finance | Better Dividend Stock for Retirees: General Mills vs. Bristol Myers Squibb
  https://finance.yahoo.com/markets/stocks/articles/better-dividend-stock-retirees-general-182025894.html
## NBIS -16.1%  Nebius Group
- Sat 21 Nov | The Globe and Mail | Cipher Digital, Kingsoft Cloud Holdings, Keel Infrastructure, Nebius Group, and D-Wave Quantum shares are falling, what you need to know
  https://www.theglobeandmail.com/investing/markets/stocks/NBIS-Q/pressreleases/8942374/cipher-digital-kingsoft-cloud-holdings-keel-infrastructure-nebius-group-and-d-wave-quantum-shares-are-falling-what-you-need-to-know/
  > Cipher Digital, Kingsoft Cloud Holdings, Keel Infrastructure, Nebius Group, and D-Wave Quantum shares are falling, what you need to know
- Sat 21 Nov | TradingView | Nebius Group N.V. Stock 12‑Month Price Target Cut to $234.85, Implies 189% Upside
  https://www.tradingview.com/news/tradingview:9287e9754f79b:0-nebius-group-n-v-stock-12-month-price-target-cut-to-234-85-implies-189-upside/
  > Stock 12‑Month Price Target Cut to $234.85, Implies 189% Upside Less than 1 min read - According to estimates from 20 analysts, Nebius Group N.V. stock's average price target has fallen from $236.76 to $234.85, with forecasts ranging from $84 to $380 per share
- Sat 21 Nov | 24/7 Wall St. | Michael Burry Says He Tried to Warn You About Nebius. The Stock Just Crashed 16% and Is 72% Below Its Record
  https://247wallst.com/investing/2026/11/20/michael-burry-says-he-tried-to-warn-you-about-nebius-the-stock-just-crashed-16-and-is-72-below-its-record/
  > Michael Burry Says He Tried to Warn You About Nebius. The Stock Just Crashed 16% and Is 72% Below Its Record Nebius Group (NASDAQ: NBIS) closed at $81.31 on Friday, down 16% from $96.92.
- Fri 20 Nov | MarketBeat | Nebius Group (NASDAQ:NBIS) Shares Down 16.2% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-nebius-group-nasdaq-nbis-shares-down-162-heres-what-happened-2026-11-20/
  > Nebius Group (NASDAQ:NBIS) Shares Down 16.2% - Here's What Happened - Nebius shares fell 16.2% to about $81.21 in Friday’s mid-day trading, with trading volume 156% above its average. - The company cut its 2026 revenue outlook to $3 billion–$3.2 billion after data-center delays shifted some capacity growth into 2027.
## CLS -16.1%  Celestica
- Fri 20 Nov | MarketBeat | Celestica (NYSE:CLS) Stock Price Down 16.3% - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-celestica-nyse-cls-stock-price-down-163-time-to-sell-2026-11-20/
  > Celestica (NYSE:CLS) Stock Price Down 16.3% - Time to Sell? - Celestica shares fell 16.3% to about $201 on Friday, with trading volume roughly 105% above its average.
- Fri 20 Nov | Global Banking & Finance Review | Celestica falls 16.38% in Friday's session
  https://www.globalbankingandfinance.com/celestica-cls-to-falls-2026-11-20/
- Fri 20 Nov | GuruFocus | Celestica (CLS) Shares Drop 15% Amid Tech Selloff on November 20, 2026
  https://www.gurufocus.com/news/9213149/celestica-cls-shares-drop-15-amid-tech-selloff-on-november-20-2026
  (page: did not load (403))
- Fri 20 Nov | Seeking Alpha | Celestica drops 15% amid broad tech selloff (CLS:NYSE)
  https://seekingalpha.com/news/4675283-celestica-drops-15-percent-amid-broad-tech-selloff
  (page: did not load (403))
## SNDK -16.1%  Sandisk
- Sat 21 Nov | FourWeekMBA | Sandisk Splits 8-for-1 as Shares Sit 72.9% Below June High
  https://fourweekmba.com/ai-sandisk-splits-8-for-1-as-shares-sit-72-9-below-june-high/
  > Sandisk’s eight-for-one stock split took effect at 4:01 p.m. Eastern Time on 19 November, and its shares began trading at the new, lower price on Friday, according to the company’s SEC filing.
- Sat 21 Nov | FinanceFeeds | Sandisk Stock $79.24: 16% Split-Day Drop on NAND Warning
  https://financefeeds.com/sandisk-sndk-stock-79-saturday-week-ahead-after-16-percent-split-day-drop-bull-91-bear-72/
  > - Friday close: $79.24, down 16.05 percent from Thursday’s split-adjusted $94.40 (StockAnalysis; Yahoo Finance; Finviz). - Friday’s range: open $89.98, high $90.67, low $78.25 (StockAnalysis). The stock opened 4.7 percent lower and fell for most of the session.
- Sat 21 Nov | Yahoo Finance | Sandisk (SNDK) Implements 8 For 1 Stock Split
  https://finance.yahoo.com/markets/stocks/articles/sandisk-sndk-implements-8-1-042529050.html
  > - Sandisk (NasdaqGS:SNDK) has approved and implemented an 8-for-1 forward stock split of its common shares. - The company amended its corporate charter to reflect the split and adjust key share capital provisions.
- Sat 21 Nov | Startup Fortune | Sandisk falls 14% on its first day after the 8-for-1 split as TrendForce warns NAND prices will fall
  https://startupfortune.com/sandisk-falls-14-on-its-first-day-after-the-8-for-1-split-as-trendforce-warns-nand-prices-will-fall/
  > A split doesn't change what a company is worth, only the number on the ticker. Sandisk shareholders got the reminder on day one, when a price forecast mattered more than the extra shares.
## BE -15.3%  Bloom Energy
- Sat 21 Nov | ad-hoc-news.de | Bloom Energy stock: BMO upgrades rating, cuts target to $230
  https://www.ad-hoc-news.de/boerse/news/corporate-news/bloom-energy-stock-bmo-upgrades-rating-cuts-target-to-230/70541720
  > Bloom Energy stock heads into the weekend after BMO Capital Markets upgraded its rating on November 19 from Hold to Buy. The bank also lowered its price target from 260 to 230 US dollars, according to Markets Insider.
- Sat 21 Nov | Pluang | Bloom Energy, Vertiv, and Vistra show strong gr...
  https://pluang.com/en/news-feed/saham-pusat-data-bloom-energy-vertiv-vistra-beli-hingga-2030
  (page: did not load (403))
- Fri 20 Nov | MarketBeat | Bloom Energy (NYSE:BE) Stock Falls 15.6% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-bloom-energy-nyse-be-stock-falls-156-heres-why-2026-11-20/
  > Bloom Energy (NYSE:BE) Stock Falls 15.6% - Here's Why - Bloom Energy shares fell 15.6% to $141.82 in Friday’s midday trading, on volume 105% above its average. - Recent fundamentals were strong: quarterly revenue rose 138.1% year over year to $1.24 billion and EPS beat estimates.
- Fri 20 Nov | Barron's | Anthropic, Nvidia, AMD, Micron, Sandisk, Bloom Energy, and More Stocks That Explain Today’s Market
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: NVDA, WMT, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-23 CLHO results (expected)
- 2026-11-23 EAST results (expected)  <- write its preview
- 2026-11-23 EFID results (expected)
- 2026-11-23 EFIH results (expected)  <- write its preview
- 2026-11-23 JUFO results (expected)
- 2026-11-23 PHDC results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
- judged right with no lesson yet: Brent stays below $105 while Iran talks continue  <- write its `lesson`
    2026-10-30-rotation: open -> on track
    2026-11-05-brent-hormuz: on track -> right  (Judged on its date: Brent at 92.57 from 94.62 (-2.2%).)

## Fair value
- Changed since the last run: ETEL +20% -> +32% (medium -> medium); CLHO -16% -> -32% (medium -> low).
- In the ten cheapest or dearest with no note: ADIB, MCQE, CSAG, MTIE, AMOC, LCSW, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-21. Open each story before using it.
## COMI  (8 leads)
- Sat 21 Nov | شبكة تواصل الإخبارية | قبل ما تغير فلوسك.. أسعار الدولار اليوم في البنك الأهلي وبنك مصر وCIB
  https://twaslnews1.twaslnews.com/8049002/
  (page: did not load (403))
- Fri 20 Nov | بوابة بلوم | دون حظر بيع.. تفاصيل قرض السيارة من CIB حتى 13.5 مليون جنيه
  https://bloom-gate.com/بنوك-وتمويل/دون-حظر-بيع-تفاصيل-قرض-السيارة-من-cib-حتى-13-5/
  > تفاصيل قرض السيارة من CIB حتى 13.5 مليون جنيه يتيح البنك التجاري الدولي CIB قرضاً لتمويل شراء السيارات الجديدة للموظفين، بقيمة تصل إلى 13.5 مليون جنيه، مع إمكانية تمويل كامل قيمة السيارة دون مقدم، وفترة سداد تمتد إلى 8 سنوات، بسعر عائد يبلغ 21.5%. تفاصيل قرض السيارة من البنك التجاري الدولي CIB
- Fri 20 Nov | شبكة تواصل الإخبارية | شروط استخراج دفتر شيكات من البنك التجاري الدولي CIB.. الحد الأدنى للحساب الجاري
  https://twaslnews1.twaslnews.com/8016191/
  (page: did not load (403))
## TMGH  (2 leads)
- Sat 21 Nov | اليوم السابع | فى سوق المشتقات.. الكبار يراهنون على أسعار "طلعت مصطفى" وCIB حتى 2027
  https://www.youm7.com/story/2026/11/21/فى-سوق-المشتقات-الكبار-يراهنون-على-أسعار-طلعت-مصطفى-وCIB/7625715
  > سجلت تداولات سوق المشتقات المالية في البورصة المصرية قيمة إجمالية بلغت 9.374 مليون جنيه خلال الأسبوع، من خلال تنفيذ 60 عملية، على كمية متداولة بلغت 642 عقدًا، وفقًا للتقرير الأسبوعي الخاص بالمشتقات المالية.
- Thu 19 Nov | مجلة البوصلة الاقتصادية | تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم
  https://alboslanews.com/أسواق-مال/تراجع-العقود-المستقبلية-لـ-egx30-وطلعت-مصطفى-هامشيًا-وانخفاض-البنك-التجاري-الدولي-بنسب-تتخطى-1-اليوم-431143
  > تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم الخميس 19 نوفمبر 2026 -03:56
## ETEL  (4 leads)
- Fri 20 Nov | مجلة البوصلة الاقتصادية | المصرية للاتصالات شريك التكنولوجيا لمشروع «نيفيرا».. شبكة ألياف ضوئية وحلول المدن الذكية
  https://alboslanews.com/اتصالات-وتكنولوجيا/المصرية-للاتصالات-شريك-التكنولوجيا-لمشروع-نيفيرا-شبكة-ألياف-ضوئية-وحلول-المدن-الذكية-431092
  > المصرية للاتصالات شريك التكنولوجيا لمشروع «نيفيرا».. شبكة ألياف ضوئية وحلول المدن الذكية الأربعاء 18 نوفمبر 2026 -11:08
- Fri 20 Nov | المصري اليوم | الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026.. الرابط والخطوات وطرق السداد
  https://www.almasryalyoum.com/news/details/4415474
  > الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026.. الرابط والخطوات وطرق السداد يتزايد اهتمام عملاء الشركة المصرية للاتصالات WE بالبحث عن طريقة الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026، لمعرفة قيمة الاشتراك الشهري ومتابعة موعد التجديد، وتجنب انقطاع خدمة الإنترنت المنزلي نتيجة التأخر في سداد المستحقات.
- Thu 19 Nov | Masrawy | المصرية للاتصالات يهزم الترسانة في عقر داره ويرتقي بجدول الترتيب
  https://www.masrawy.com/sports/sports_news/details/2026/11/19/3081357/المصرية-للاتصالات-يهزم-الترسانة-في-عقر-داره-ويرتقي-بجدول-الترتيب
  > حقق فريق المصرية للاتصالات (وي) فوزًا مهمًا على حساب منافسه الترسانة بنتيجة 2-1، في المباراة التي جمعت الفريقين اليوم الخميس، ضمن منافسات الجولة الثالثة عشرة من دوري المحترفين المصري.
- Thu 19 Nov | بوابة العمال | المصرية للاتصالات توقع اتفاقية تعاون مع «نيفيرا» لتصبح شريك الاتصالات والتكنولوجيا للمشروع
  https://elommal.com/archives/395320
  > كتب عاطف عبد الستار وقّع المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، والمهندس عبد الخالق عواد، الرئيس التنفيذي للشؤون العقارية بشركة «نيفيرا»، اتفاقية تعاون تتولى بموجبها المصرية للاتصالات دور شريك الاتصالات والتكنولوجيا للمشروع، وذلك بحضور الدكتور مصطفى مدبولي، رئيس مجلس الوزراء.
## PHDC  (1 leads)
- Thu 19 Nov | Masrawy | من فيلا بالم هيلز إلى عصابة الشرطة المزيفة ضربتان أمنيتان بأكتوبر
  https://www.masrawy.com/news/news_cases/details/2026/11/19/3081493/من-فيلا-بالم-هيلز-إلى-عصابة-الشرطة-المزيفة-ضربتان-أمنيتان-بأكتوبر
  > تسلل في الظلام من فيلا تحت الإنشاء، وكمين مفاجئ بـ30 ألف جنيه قدام نادي الصيد، خيطان لوقعتين مختلفتين في قسم أول أكتوبر، لكن كاميرات المراقبة والتحريات جمعتهم في نقطة واحدة: سقوط المتهمين. قفزة داخل بالم هيلز ومع تتبع الملابسات ومواجهة المتهم، اتضح أنه كان يتردد على منطقة بالم هيلز بحكم طبيعة عمله؛
## SWDY  (1 leads)
- Thu 19 Nov | جريدة باور نيوز الاخبارية | أحمد السويدي يلتقي رئيس شركة Gonvarri Industries في مدريد لبحث شراكات استراتيجية بقطاعي الطاقة والبنية التحتية
  https://powernews.cc/?p=294462
  > عقد المهندس أحمد السويدي، الرئيس التنفيذي لمجموعة السويدي إليكتريك، اجتماعًا مع السيد جون ريبيراس، رئيس مجلس الإدارة التنفيذي لشركة Gonvarri Industries، بمقر الشركة في العاصمة الإسبانية مدريد، بحضور السيد نيستور لاكارا، مدير الاستراتيجية، وعدد من أعضاء فريق القيادة بالشركة.
## ORAS  (8 leads)
- Fri 20 Nov | SaudiGulf Projects | Orascom Construction Backlog Rises to $11.6 Billion in Q3 2026
  https://www.saudigulfprojects.com/2026/11/orascom-construction-q3-2026-results-11-6-billion-backlog/
  (page: did not load (403))
- Fri 20 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تبدأ تشييد واحدة من أكبر محطات تحلية المياه عالمياً في الأردن
  https://cnnbusinessarabic.com/finance-markets/1152977/أوراسكوم-كونستراكشون-تبدأ-تشييد-واحدة-من-أكبر-محطات-تحلية-المياه-عالميا-في-الأردن
  > أوراسكوم تضع حجر الأساس لمشروع نقل المياه من العقبة إلى عمّان (شترستوك) أعلنت شركة «أوراسكوم كونستراكشون» وضع حجر الأساس لمشروع تحلية ونقل المياه من العقبة إلى عمّان في الأردن، وهو مشروع ضخم يتضمن إنشاء واحدة من أكبر محطات تحلية المياه على مستوى العالم.
- Thu 19 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | مجلس أوراسكوم كونستراكشون يقر زيادة رأس المال بـ 88.2% لصالح شركة OCI N.V
  https://www.argaam.com/ar/article/articledetail/id/1950993
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## FWRY  (5 leads)
- Fri 20 Nov | بوابة التكنولوجيا المالية | تقريرلـ «AfricaNenda» : أفريقيا بها أكثر من 39 نظاما للمدفوعات الفورية تغطي 43 دولة
  https://fintechgate.net/258034
  > 1.8 تريليون دولار قيمة المدفوعات الفورية في أفريقيا خلال 2025 عبر 71.4 مليار معاملة تقريرلـ «AfricaNenda» : أفريقيا بها أكثر من 39 نظاما للمدفوعات الفورية تغطي 43 دولة
- Thu 19 Nov | السودان اليوم | نقلة جديدة في المعاملات المالية.. السودان يتجه نحو الدفع الفوري
  https://alsudantoday.com/business/economic-news/568347
  (page: did not load (403))
- Thu 19 Nov | موقع الحرية الإخباري | عبر 46 منفذًا.. الجيزة تُفعّل سداد مستحقات تقنين أراضي أملاك الدولة من خلال «فوري بلس»
  https://alhorianews.com/عبر-46-منفذًا-الجيزة-تُفعّل-سداد-مستحقا/
  > كشف الدكتور أحمد الأنصاري، محافظ الجيزة، عن تفعيل خدمة السداد الإلكتروني عبر منافذ «فوري بلس» لتحصيل كافة المستحقات المالية المتعلقة بملف تقنين أوضاع أراضي أملاك الدولة، وذلك تنفيذًا لأحكام القانون رقم 168 لسنة 2025 ولائحته التنفيذية، وفي إطار خطة المحافظة لتبسيط الإجراءات وتخفيف الأعباء عن المواطنين. بنود السداد المتاحة دون الذهاب للمقار الحكومية
- Thu 19 Nov | بوابة المصرف | 10 بروتوكولات لتحديث التجارة الخارجية.. فوري وفيزا ومايكروسوفت ضمن الشركاء
  https://www.almasraf.news/10-بروتوكولات-لتحديث-التجارة-الخارجية/
  > وقّع المختبر التنظيمي ومركز الابتكار لتكنولوجيا التجارة (TradeTech Sandbox) 10 بروتوكولات تعاون مع مؤسسات وشركات مصرية ودولية، لتسريع تحديث التجارة الخارجية وتطوير حلول رقمية تستهدف تقليل الوقت والتكلفة المرتبطين بالإجراءات التجارية. وتضم الشراكات شركات متخصصة في التكنولوجيا والاتصالات والمدفوعات والخدمات المالية، من بينها فوري وفيزا ومايكروسوفت. 10 بروتوكولات تجمع شركات التكنولوجيا والمدفوعات لتطوير التجارة
- Thu 19 Nov | آراب فاينانس | فوري وفيزا ومايكروسوفت ضمن 10 جهات تتعاون مع الحكومة لتطوير التجارة الخارجية
  http://www.arabfinance.com/ar/news/newdetails/فوري-وفيزا-ومايكروسوفت
## ABUK  (1 leads)
- Thu 19 Nov | لحظات نيوز | العربية للتصنيع توقع اتفاقا لبناء محطات طاقة شمسية لشركة أبوقير للأسمدة
  https://nl7za.com/economy/العربية-للتصنيع-توقع-اتفاقا-لبناء-محطات-طاقة-شمسية
  > وقعت الهيئة العربية للتصنيع عقدا استراتيجيا موسعا مع شركة أبوقير للأسمدة والصناعات الكيماوية لتنفيذ منظومة متكاملة من محطات توليد الطاقة الكهربائية النظيفة باستخدام الخلايا الشمسية بقدرات تشغيلية عالية، ويهدف المشروع الصناعي الضخم إلى تزويد المجمعات الإنتاجية للشركة بالطاقة المتجددة وخفض تكاليف التشغيل وترشيد استهلاك الوقود التقليدي بما يتوافق مع المعايير البيئية العالمية والتنمية المستدامة للدولة ...
## HRHO  (1 leads)
- Fri 20 Nov | Africa Business Communities | Emirates NBD Egypt and EFG Hermes expand investment partnership
  https://africabusinesscommunities.com/finance/emirates-nbd-egypt-and-efg-hermes-expand-investment-partnership/
  (page: did not load (403))
## JUFO  (1 leads)
- Thu 19 Nov | مستقبل وطن نيوز | «كُحل الجبل» يوثق بطولة أبناء جهينة في مواجهة الحملة الفرنسية بالمهرجان القومي للمسرح المدرسي
  https://www.mwatan.news/1040342
  (page: did not load (403))
## EMFD  (1 leads)
- Thu 19 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس
  https://www.osoulmisrmagazine.com/452994
  > الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس تباين أداء أسهم الشركات العقارية المقيدة بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الخميس، إذ ارتفعت أسعار أسهم 4 شركات، مقابل تراجع أسهم 4 شركات، بينما استقر سهما مصر الجديدة للإسكان والتعمير والمطورون العرب القابضة دون تغيير.
## BQDC  (8 leads)
- Fri 20 Nov | قناة صدى البلد | بنك القاهرة يحذر العملاء من تأثر بعض الخدمات المصرفية السبت.. التفاصيل
  https://elbaladtv.net/بنك-القاهرة-يحذر-العملاء-من-تأثر-بعض-ال
  > أعلن بنك القاهرة تنفيذ أعمال صيانة وتطوير للبنية التحتية للأنظمة المصرفية، فجر السبت 21 نوفمبر 2026، بدءًا من الساعة 12 منتصف الليل وحتى الساعة 6 صباحًا، بهدف رفع كفاءة الأنظمة وتحسين مستوى الخدمات المقدمة للعملاء. توقف متقطع لخدمات بنك القاهرة
- Fri 20 Nov | elmaser.com | محمد معيط: التضخم «ورم خبيث» يهدد الاقتصاد.. وبيع بنك القاهرة وأرض علم الروم إيرادات استثنائية لمرة واحدة
  https://elmaser.com/article/202632
  (page read: it never names the company, so probably not about it: skip)
- Fri 20 Nov | أصول مصر | غدًا.. بنك القاهرة يعلن توقفًا متقطعًا لعدد من خدماته المصرفية بسبب الصيانة
  https://www.osoulmisrmagazine.com/453100
  > بنك القاهرة يعلن توقفًا متقطعًا لعدد من خدماته المصرفية بسبب الصيانة أعلن بنك القاهرة تنفيذ أعمال صيانة وتطوير للبنية التحتية للأنظمة المصرفية، يوم السبت الموافق 21 نوفمبر 2026، اعتبارًا من الساعة 12 صباحًا وحتى الساعة 6 صباحًا، في إطار حرصه على تحسين كفاءة الأنظمة المصرفية وتطوير الخدمات المقدمة للعملاء.
## EFID  (2 leads)
- Thu 19 Nov | Investing.com | Earnings call transcript: Edita Food posts record Q3 2026 revenue, shares rise
  https://www.investing.com/news/transcripts/earnings-call-transcript-edita-food-posts-record-q3-2026-revenue-shares-rise-93CH-5039005
  (page: did not load (403))
- Thu 19 Nov | TradingView | Edita Food Industries Company Q3 2026 Earnings Call Is Live
  https://www.tradingview.com/news/urn:live_audio:quartr.com:800175:0-edita-food-industries-company-q3-2026-earnings-call-is-live/
  > Edita Food Industries Company Q3 2026 Earnings Call Is Live Edita Food Industries Company's quarterly earnings call has just begun.
## AAPL  (8 leads)
- Sat 21 Nov | Seeking Alpha | Apple: Shows Us How To Win Without Joining The AI Bubble
  https://seekingalpha.com/article/4970798-apple-shows-us-how-to-win-without-joining-the-ai-bubble
  (page: did not load (403))
- Fri 20 Nov | Investor's Business Daily | Look Out Below And Watch For This; Apple, Palomar, Interparfums In Focus - Video
  https://www.investors.com/ibd-videos
  > Nov 20, 2026|05:14 PM ET|ALISSA CORAM, JUSTIN NIELSEN Alissa Coram and Justin Nielsen walk through Friday's market action with a discussion of key stocks to watch in Stock Market Today. Look Out Below And Watch For This; Apple, Palomar, Interparfums In Focus [Figures on the page: first half; one quarter. Check which one each figure is.]
- Fri 20 Nov | TradingView | Apple Stock Has a New AI Catalyst -- It Could Take on OpenAI, Meta and Anthropic
  https://www.tradingview.com/news/gurufocus:b4b6c702c094b:0-apple-stock-has-a-new-ai-catalyst-it-could-take-on-openai-meta-and-anthropic/
  > Apple Stock Has a New AI Catalyst -- It Could Take on OpenAI, Meta and Anthropic Apple AAPL is building an autonomous AI agent and has posted a job opening for a senior engineering manager to lead the project, according to a Bloomberg report.
## MSFT  (8 leads)
- Sat 21 Nov | Investing.com Australia | Form 4 Microsoft Corporation For: 21 November By Investing.com
  https://au.investing.com/news/stock-market-news/form-4-microsoft-corporation-for-21-november-93CH-4788027
  (page: did not load (403))
- Sat 21 Nov | Blockchain News | Microsoft (MSFT) Stock Price Prediction: Pullback tests support as analysts stay constructive
  https://blockchain.news/news/20261121-price-prediction-msft-pullback-tests-support-as-analysts-stay
  > Microsoft’s latest setup: softer price, firmer fundamental backdrop Microsoft (MSFT) is trading through a short-term pullback rather than a broken thesis. The stock’s last reported close was $487.31, with a 24-hour range of $504.49 to $481.86.
- Sat 21 Nov | Yahoo Finance | Did Microsoft AI Partnership Just Shift Danaher's (DHR) Investment Narrative?
  https://finance.yahoo.com/technology/ai/articles/did-microsoft-ai-partnership-just-051538591.html
  > - Danaher announced a partnership with Microsoft to build AI assisted, cloud based scientific instruments and lab software, with early tools such as MetaXpress Acquire AI Assistant already moving toward commercial rollout.
- Sat 21 Nov | Moneycontrol.com | From No. 1 to No. 4: Nvidia falls behind Apple, Microsoft and Alphabet as shares tumble
  https://www.moneycontrol.com/news/business/from-no-1-to-no-4-nvidia-falls-behind-apple-microsoft-and-alphabet-as-shares-tumble-14085980.html
  > 4: Nvidia falls behind Apple, Microsoft and Alphabet as shares tumble Nvidia slipped behind Alphabet in market value as its shares plunged 14% on Friday, extending a seven-week losing streak despite record quarterly revenue and a stronger sales forecast. November 21, 2026 / 09:53 IST The AI chipmaker's shares plunged 14% on Friday.
- Sat 21 Nov | Yahoo Finance | Is Danaher (DHR) Undervalued After Its Microsoft AI Lab Partnership?
  https://finance.yahoo.com/markets/stocks/articles/danaher-dhr-undervalued-microsoft-ai-042011998.html
- Sat 21 Nov | Yahoo Finance UK | Microsoft Corporation (MSFT) stock price, news, quote and history
  https://uk.finance.yahoo.com/quote/MSFT/
- Fri 20 Nov | 24/7 Wall St. | Mets Owner Steve Cohen's Fund Dumped Nearly All of Its AMD and Bet $1 Billion That Microsoft Is the Safer AI Stock. AMD Has Fallen 31% Since
  https://247wallst.com/investing/2026/11/20/mets-owner-steve-cohens-fund-dumped-nearly-all-of-its-amd-and-bet-1-billion-that-microsoft-is-the-safer-ai-stock-amd-has-fallen-31-since/
- Fri 20 Nov | Yahoo Finance | International Business Machines (IBM) Opens Lightwell Access On Microsoft Marketplace, Is It Still Undervalued?
  https://finance.yahoo.com/markets/stocks/articles/international-business-machines-ibm-opens-231452605.html
## NVDA  (8 leads)
- Sat 21 Nov | Yahoo Finance | Could SpaceX Be the Ultimate Winner of the Nvidia-Jensen Huang Split?
  https://finance.yahoo.com/markets/stocks/articles/could-spacex-ultimate-winner-nvidia-092002478.html
  > Few companies that have undergone more radical changes recently than Nvidia (NASDAQ:NVDA), whose co-founder and chief executive officer, Jensen Huang, abruptly resigned earlier this month. Although there are calls from investors and employees to bring him back, the board of directors has stated that it has no interest in doing that.
- Sat 21 Nov | Morningstar | Investor Focus: Anthropic’s Record-Breaking IPO, Nvidia’s Earnings, and an Undervalued UK Defense Stock
  https://global.morningstar.com/en-gb/columns/uk-investor-focus-anthropics-ipo-inflation-bae-systems
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | The Motley Fool | Here’s My Top AI Stock to Buy With Nvidia in Uncertain Territory
  https://www.fool.com/investing/2026/11/21/here-s-my-top-ai-stock-to-buy-with-nvidia-in-uncertain-territory/
  > Nvidia (NVDA -14.01%) has been a rough stock to own over the past few weeks. It has lost its co-founder and CEO, Jensen Huang, and some investors worry it may never recover.
- Sat 21 Nov | BeInCrypto | Nvidia and SanDisk Bets Joined Bitcoin in a $1.76 Billion Liquidation Wave
  https://beincrypto.com/crypto-liquidations-nvidia-sandisk-stock-bets/
  (page: did not load (403))
- Sat 21 Nov | The Motley Fool | After Its Worst Week in 18 Years, Nvidia Now Faces an SEC Investigation. What It Means for Investors
  https://www.fool.com/investing/2026/11/21/after-its-worst-week-in-18-years-nvidia-now-faces-an-sec-investigation-what-it-means-for-investors/
- Sat 21 Nov | Axios | Nvidia shares plunge as Anthropic can't stop the AI selloff
  https://www.axios.com/2026/11/20/anthropic-ipo-nvidia-ai-tech-selloff
- Sat 21 Nov | Ticker News | Nvidia stock slumps 14%, setting longest losing streak since 2008
  https://tickernews.co/nvidia-stock-slumps-14-setting-longest-losing-streak-since-2008/
- Sat 21 Nov | Yahoo Finance | NVDA Stock Sees Biggest Fall In 22 Months, But Top Analyst Says Nvidia’s AI Boom Isn’t Over Yet — Here Are 5 Reasons Why
  https://finance.yahoo.com/markets/stocks/articles/nvda-stock-sees-biggest-fall-024825298.html
## AMZN  (8 leads)
- Sat 21 Nov | MarketBeat | First Nebraska Trust Co Makes New Investment in Amazon.com, Inc. $AMZN
  https://www.marketbeat.com/instant-alerts/filing-first-nebraska-trust-co-makes-new-investment-in-amazoncom-inc-amzn-2026-11-21/
  > First Nebraska Trust Co Makes New Investment in Amazon.com, Inc. - First Nebraska Trust Co. opened a new Amazon position in the third quarter, buying 49,927 shares valued at about $12.4 million. Amazon now represents approximately 1% of the firm’s portfolio. - Institutional investors own 72.2% of Amazon shares.
- Sat 21 Nov | ad-hoc-news.de | Amazon stock: AWS signs $5 billion data-center deal
  https://www.ad-hoc-news.de/boerse/news/corporate-news/amazon-stock-aws-signs-5-billion-data-center-deal/70541708
  > Amazon Web Services signed an agreement with Blackstone on November 16, 2026, under which Blackstone Digital Infrastructure Trust will acquire a 75% majority interest in two joint ventures for approximately 5 billion US dollars. The transaction gives AWS a continuing minority position in the facilities while supporting its cloud infrastructure expansion. [Figures on the page: one quarter; attributable to shareholders. Check which one each figure is.]
- Sat 21 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: GRIMES & Co WEALTH MANAGEMENT LLC Grows Stake
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-grimes-co-wealth-management-llc-grows-stake-2026-11-21/
  > $AMZN Stock: GRIMES & Co WEALTH MANAGEMENT LLC Grows Stake - GRIMES & Co Wealth Management increased its Amazon stake by 1.9% in the third quarter, adding 3,285 shares to hold 178,432 shares valued at about $44.5 million.
- Sat 21 Nov | MarketBeat | 583,892 Shares of Amazon.com, Inc. $AMZN Purchased by Associated Banc Corp
  https://www.marketbeat.com/instant-alerts/filing-583892-shares-of-amazoncom-inc-amzn-purchased-by-associated-banc-corp-2026-11-21/
  > 583,892 Shares of Amazon.com, Inc. $AMZN Purchased by Associated Banc Corp - Associated Banc Corp bought 583,892 Amazon shares in the third quarter, valued at about $145.5 million; Amazon now represents 3.4% of its portfolio and is its sixth-largest holding.
- Sat 21 Nov | MarketBeat | Amazon.com (NASDAQ:AMZN) Stock Price Crosses Below 50 Day Moving Average Following Insider Selling
  https://www.marketbeat.com/instant-alerts/price-amazoncom-nasdaq-amzn-stock-price-crosses-below-50-day-moving-average-following-insider-selling-2026-11-20/
- Sat 21 Nov | The Globe and Mail | Amazon's re:Invent Conference Starts Nov. 30. Here's What the Stock Did in the Month After the Last 10.
  https://www.theglobeandmail.com/investing/markets/markets-news/motley/8945814/amazon-s-reinvent-conference-starts-nov-30-here-s-what-the-stock-did-in-the-month-after-the-last-10/
- Sat 21 Nov | Pluang | Amazon stock shows no consistent rally after AWS re:Invent conferences, despite strong AWS growth.
  https://pluang.com/en/news-feed/analisis-kinerja-saham-amazon-setelah-konferensi-reinvent-2026-2
- Sat 21 Nov | Yahoo Finance | Generac Stock In Focus After Earnings Beat And Amazon Supply Deal
  https://finance.yahoo.com/markets/stocks/articles/generac-stock-focus-earnings-beat-001937973.html
## GOOGL  (8 leads)
- Sat 21 Nov | Yahoo Finance | Prediction: Here’s Where Alphabet Stock Will Be in 5 Years
  https://finance.yahoo.com/markets/stocks/articles/prediction-where-alphabet-stock-5-081002070.html
  > There's a lot of concern over what the future holds for Alphabet (NASDAQ:GOOG) (NASDAQ:GOOGL). The internet company has transformed from an asset-light business into an extremely asset-heavy business, as it and its hyperscaler peers are set to spend trillions of dollars building new data centers for artificial intelligence over the next few years.
- Sat 21 Nov | Pluang | Alphabet's heavy AI data center spending weighs on stock, but strong cloud growth hints at huge future cash flow.
  https://pluang.com/en/news-feed/prediksi-saham-alphabet-investasi-pusat-data-ai-lima-tahun-2
  (page: did not load (403))
- Sat 21 Nov | GuruFocus | Alphabet Stock Slides Nearly 20%. Trader Sees Rebound Clues
  https://www.gurufocus.com/news/9212594/alphabet-stock-slides-nearly-20-trader-sees-rebound-clues
  (page: did not load (403))
- Sat 21 Nov | Times Now | Nvidia Stock Slides, Falls Behind Alphabet In Market Value As Selloff Continues
  https://www.timesnownews.com/business-economy/markets/nvidia-stock-slides-falls-behind-alphabet-in-market-value-as-selloff-continues-article-156544904
  > Nvidia has slipped below Google's parent firm Alphabet and now become the fourth-most valuable US company following the prolonged decline in its shares. The chipmaker's shares fell as much as 3 percent on Friday and the market capitalisation is now at approximately 3.4 trillion dollars.
- Sat 21 Nov | JournalArta | Nvidia Drops Below Alphabet as Stock Falls About 3%
  https://journalarta.com/en/2026/11/21/nvidia-stock-falls-below-alphabet-market-value/
- Sat 21 Nov | Moomoo | Alphabet-A(GOOGL) Stock Price Today | Quotes & News
  https://www.moomoo.com/stock/GOOGL-US?chain_id=Name1K9-3FXPhg.1lg1r8g&global_content={"promote_id":13764,"sub_promote_id":57,"f":"www.moomoo.com/stock/TSLA-CA"}
- Fri 20 Nov | Traders Union | Launch of first Asian bond sale may deepen liquidity options for Alphabet in volatile technology markets
  https://tradersunion.com/news/stocks/show/4351627-alphabet-stock-down-as-ai/
- Fri 20 Nov | Global Banking & Finance Review | Alphabet Inc Class C falls 2.59% in Friday's session
  https://www.globalbankingandfinance.com/alphabet-inc-class-c-goog-falls-2026-11-20/
## META  (8 leads)
- Sat 21 Nov | blockchain.news | Meta Platforms (META) Stock Price Prediction: AI optimism meets a broken trend after the post-earnings fade
  https://blockchain.news/news/20261121-price-prediction-meta-ai-optimism-meets-a-broken-trend
  > What changed in the tape Meta Platforms (META) is trying to digest a sharp de-rating after a recent slide in price. The stock is at $567.25, down 3.18% over 24 hours, with the current range marked by $590.40 on the high side and $559.77 on the low side.
- Sat 21 Nov | Yahoo Finance | George Soros Raised His Meta (META) Stake by 596%. Then the Stock Fell
  https://finance.yahoo.com/markets/stocks/articles/george-soros-raised-meta-meta-011000430.html
  > We just published a list of the Top 10 Stocks to Buy According to Billionaire George Soros, and Meta Platforms, Inc. (NASDAQ:META) ranked 7th on this list. Born in Budapest in 1930, he built his fortune running the Quantum Fund, and the firm that carries his name has been investing for more than five decades.
- Sat 21 Nov | Simply Wall St | Meta Platforms (META) Taps Euro Bond Market As Fair Value Debate Heats Up
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/meta-platforms-meta-taps-euro-bond-market-as-fair-value-deba
  > Meta Platforms (META) has just tapped the euro bond market, issuing several tranches of long dated senior notes across maturities from 2031 to 2065. That fresh funding immediately puts the balance sheet in focus.
- Fri 20 Nov | Nacionale | Why is Meta stock down today? About 6% lower as the AI sell-off and an Apple agent report hit
  https://www.nacionale.com/en/articles/why-is-meta-stock-down-today-ai-selloff-apple-ai-agent-insider-sales-november-20
  (page: did not load (403))
- Fri 20 Nov | GuruFocus | Meta Platforms Inc (META) Stock Down 5.8% -- Now Undervalued? GF Score: 99/100
  https://www.gurufocus.com/news/9213337/meta-platforms-inc-meta-stock-down-58-now-undervalued-gf-score-99100
- Fri 20 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Shares Down 5.9% After Insider Selling
  https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-shares-down-59-after-insider-selling-2026-11-20/
- Fri 20 Nov | Yahoo Finance | Shots Fired: Meta Will Reportedly Sell a $300 Muse Charm With Free Verizon 5G as Apple Builds Its Agent
  https://finance.yahoo.com/technology/articles/shots-fired-meta-reportedly-sell-220018004.html
- Fri 20 Nov | Rolling Out | Meta stock faces a triple threat on a brutal Friday
  https://rollingout.com/2026/11/20/meta-stock-faces-triple-threat-friday/
## TSLA  (8 leads)
- Sat 21 Nov | TradingView | Key facts: Tesla-SpaceX Committees Explore Combination; Italy Approves Driving System
  https://www.tradingview.com/news/tradingview:ec3ed755f078c:0-key-facts-tesla-spacex-committees-explore-combination-italy-approves-driving-system/
  > Key facts: Tesla-SpaceX Committees Explore Combination; Italy Approves Driving System - Tesla and SpaceX formed board committees to explore a possible combination, but no deal has been agreed. A merger may be discussed at Tesla’s Dec. 3 annual shareholder meeting. - Tesla shares fell over 3% Friday amid merger speculation.
- Sat 21 Nov | 24/7 Wall St. | In 2000, Elon Musk Crashed His Uninsured $1 Million McLaren Trying to Show Peter Thiel What It Could Do. In 2025, Thiel's Fund Quietly Sold Every Tesla Share It Owned
  https://247wallst.com/investing/2026/11/20/in-2000-elon-musk-crashed-his-uninsured-1-million-mclaren-trying-to-show-peter-thiel-what-it-could-do-in-2025-thiels-fund-quietly-sold-every-tesla-share-it-owned/
  > In 2000, Elon Musk Crashed His Uninsured $1 Million McLaren Trying to Show Peter Thiel What It Could Do. In 2025, Thiel’s Fund Quietly Sold Every Tesla Share It Owned
- Fri 20 Nov | Stocks Down Under | Why Is Tesla (NASDAQ:TSLA) Stock Crashing? Shares Fall 7.6% Despite HSBC Upgrade and SpaceX Merger Talks
  https://stocksdownunder.com/why-is-tesla-tsla-stock-crashing-hsbc-spacex/
  (page: did not load (403))
- Fri 20 Nov | SmartAsset.com | Tesla-SpaceX Merger: Potential Gains and Risks for Investors
  https://smartasset.com/investing/tesla-spacex-merger
  > A Tesla-SpaceX merger has moved from speculation to formal board review, but investors still have no price, exchange ratio or agreed structure.1 Both companies have formed special committees, and either could decide not to proceed. The key question is not whether the companies will be stronger together.
- Fri 20 Nov | GuruFocus | Tesla Inc (TSLA) Shares Fall 7.5% -- What GF Score of 86 Tells I
  https://www.gurufocus.com/news/9213338/tesla-inc-tsla-shares-fall-75-what-gf-score-of-86-tells-investors
- Fri 20 Nov | Global Banking & Finance Review | Tesla falls 7.64% in Friday's session
  https://www.globalbankingandfinance.com/tesla-tsla-falls-2026-11-20/
- Fri 20 Nov | TheStreet | Elon Musk sends stark signal to Tesla stock investors
  https://www.thestreet.com/automotive/elon-musk-sends-stark-signal-to-tesla-stock-investors-model-yl-cybercab
- Fri 20 Nov | TIKR.com | Tesla Sinks 8%, SpaceX Down 7%, Rivian Down 8% as AI Sell-Off Swamps HSBC Upgrade
  https://www.tikr.com/blog/tesla-sinks-8-spacex-down-7-rivian-down-8-as-ai-sell-off-swamps-hsbc-upgrade?
## JPM  (8 leads)
- Sat 21 Nov | MarketBeat | JPMorgan Chase & Co. (JPM) - What Are Brokerages Thinking About This Stock?
  https://www.marketbeat.com/instant-alerts/consensus-jpmorgan-chase-co-jpm-what-are-brokerages-thinking-about-this-stock-2026-11-21/
  > JPMorgan Chase & Co. (JPM) - What Are Brokerages Thinking About This Stock? - Analysts remain moderately positive: 28 firms give JPMorgan a “Moderate Buy” consensus, with 13 buy, 2 strong-buy, and 13 hold ratings; the average 12-month price target is $368.33.
- Fri 20 Nov | Law360 | 9th Circ. May Punt On JPMorgan Chase 401(k) Suit Appeal
  https://www.law360.com/washington/articles/2552994?utm_source=rss&utm_medium=rss&utm_campaign=section
  (page: only 55 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 20 Nov | Global Banking & Finance Review | JPMorgan Chase falls 2.98% in Friday's session
  https://www.globalbankingandfinance.com/jpmorgan-chase-jpm-falls-2026-11-20/
  (page read: it never names the company, so probably not about it: skip)
- Fri 20 Nov | Quantisnow | JP Morgan Chase & (JPM): Auto-callable note tied to lowest of three indices, due 2029
  https://www.quantisnow.com/insight/sec-form-fwp-filed-by-jp-morgan-chase-co-6802546
  (page: did not load (403))
- Fri 20 Nov | Quantisnow | JPM: SEC Form FWP filed by JP Morgan Chase & Co.
  https://www.quantisnow.com/insight/sec-form-fwp-filed-by-jp-morgan-chase-co-6802537
- Fri 20 Nov | MarketWatch | JPMorgan Chase & Co. stock
  https://www.marketwatch.com/data-news/jpmorgan-chase-co-stock-1248510f-2defcd8845b6
- Fri 20 Nov | Cybersecurity Dive | JPMorgan, Visa confirm customer data taken in third-party vendor hacks
  https://www.cybersecuritydive.com/news/jpmorgan-visa-customer-data-leaked-third-party-hacks/875333/
- Fri 20 Nov | The Joplin Globe | JPMorgan Chase Financial Company LLC Declares Quarterly Coupon on Alerian MLP Index ETN
  https://www.joplinglobe.com/region/national_business/jpmorgan-chase-financial-company-llc-declares-quarterly-coupon-on-alerian-mlp-index-etn/article_f5ff9d1d-c3f0-5e5e-96ea-b0c569e84d64.html
## XOM  (8 leads)
- Sat 21 Nov | MarketBeat | ExxonMobil Corporation $XOM Position Cut by Barrow Hanley Mewhinney & Strauss LLC
  https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-position-cut-by-barrow-hanley-mewhinney-strauss-llc-2026-11-21/
  > ExxonMobil Corporation $XOM Position Cut by Barrow Hanley Mewhinney & Strauss LLC - Barrow Hanley cut its ExxonMobil stake by 38.8% in the third quarter, selling about 1.33 million shares; it still held 2.09 million shares valued at roughly $340.5 million.
- Sat 21 Nov | Machine Maker | TechnipFMC Secures Subsea Contracts for ExxonMobil’s Longtail Development in Guyana
  https://themachinemaker.com/news/technipfmc-secures-subsea-contracts-for-exxonmobils-longtail-development-in-guyana/
  > TechnipFMC (NYSE: FTI) has secured two contracts from ExxonMobil Guyana Limited for the Longtail development in Guyana’s Stabroek Block, strengthening its involvement in the country’s offshore oil and gas sector. The awards cover the supply of subsea production systems and the design and manufacture of flexible production risers for the gas condensate project.
- Sat 21 Nov | Simply Wall St | Did Longtail Approval Just Shift ExxonMobil Stock's Investment Narrative?
  https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/did-longtail-approval-just-shift-exxonmobil-stocks-investmen
  > ExxonMobil has approved a final US$12.5b investment for the Longtail project offshore Guyana, alongside progress at Rovuma LNG in Mozambique and cumulative Guyana output passing 1 million barrels, reinforcing its focus on large international upstream developments.
## AVGO  (8 leads)
- Sat 21 Nov | MarketBeat | Allianz SE Purchases 6,782 Shares of Broadcom Inc. $AVGO
  https://www.marketbeat.com/instant-alerts/filing-allianz-se-purchases-6782-shares-of-broadcom-inc-avgo-2026-11-21/
  > Allianz SE Purchases 6,782 Shares of Broadcom Inc. - Allianz SE increased its Broadcom stake by 4.2% in the third quarter, buying 6,782 shares to hold 167,837 shares valued at about $58.9 million.
- Fri 20 Nov | The Globe and Mail | Broadcom, Intel, Nvidia, and Qualcomm stocks trade down, what you need to know
  https://www.theglobeandmail.com/investing/markets/stocks/QCOM/pressreleases/8942091/broadcom-intel-nvidia-and-qualcomm-stocks-trade-down-what-you-need-to-know/
  > Broadcom, Intel, Nvidia, and Qualcomm stocks trade down, what you need to know A number of stocks fell in the afternoon session as AI-linked shares continued to pull back. Anthropic slid more than 10% following its debut, failing to revive confidence in the sector's spending boom.
- Fri 20 Nov | MLQ.ai | Broadcom falls 11% after analyst Ming-Chi Kuo says Google cut 2027 orders for its TPU chips
  https://mlq.ai/news/broadcom-falls-11-after-analyst-ming-chi-kuo-says-google-cut-2027-orders-for-its-tpu-chips/
  (page: did not load (403))
- Fri 20 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Falls 12.4% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-stock-falls-124-heres-what-happened-2026-11-20/
  > Broadcom (NASDAQ:AVGO) Stock Falls 12.4% - Here's What Happened - Broadcom shares fell 12.4% to about $303.53 on Friday, with trading volume 131% above average.
- Fri 20 Nov | Global Banking & Finance Review | Broadcom falls 11.10% in Friday's session
  https://www.globalbankingandfinance.com/broadcom-avgo-falls-2026-11-20/
- Fri 20 Nov | MarketWatch | Broadcom Inc. stock outperforms competitors despite losses on the day
  https://www.marketwatch.com/data-news/broadcom-inc-stock-outperforms-competitors-despite-losses-on-the-day-23e0a2ed-0427b43c6d7d
- Fri 20 Nov | TOKENPOST | Broadcom Shares Fall Just Over 12% to $304.65 on Nov. 20
  https://www.tokenpost.com/news/business/62338
- Fri 20 Nov | Coinpaper | Cathie Wood Buys $90M Anthropic as AMD, Broadcom Stocks Crash
  https://coinpaper.com/39162/cathie-wood-buys-90-m-anthropic-as-amd-broadcom-stocks-crash
## BRK.B  (8 leads)
- Sat 21 Nov | WSJ | Intuit Selling Mailchimp for $3.68 Billion to Berkshire Hathaway-Backed Bending Spoons
  https://www.wsj.com/business/earnings/intuit-to-sell-mailchimp-for-3-68-billion-33f03f9c
  (page: did not load (401))
- Sat 21 Nov | openPR.com | Kimberly Heaney of Berkshire Hathaway HomeServices PenFed
  https://www.openpr.com/news/4696192/kimberly-heaney-of-berkshire-hathaway-homeservices-penfed
  (page: did not load (403))
- Sat 21 Nov | Inc.com | Warren Buffett Spent Years Doing the 1 Thing Jensen Huang Failed to Do
  https://www.inc.com/soren-kaplan/warren-buffett-spent-years-doing-the-1-thing-jensen-huang-failed-to-do/91440049
  (page: did not load (403))
## WMT  (8 leads)
- Sat 21 Nov | TIKR.com | 16 Big Funds Bought Walmart Last Quarter, While 16 Sold. Who’s Right?
  https://www.tikr.com/blog/16-big-funds-bought-walmart-last-quarter-while-16-sold-whos-right
  > - Of the 460 big funds that have filed 13Fs for the quarter ended Sept. 30, 16 bought Walmart and 16 sold it. The biggest moves were a $177 million new stake and a $168 million exit. - Walmart stock is up 21% since Sept.
- Sat 21 Nov | Nacionale | What are defensive stocks? Why Walmart and other staples rose Friday as the market fell
  https://www.nacionale.com/en/articles/what-are-defensive-stocks-walmart-consumer-staples-rose-market-fell-november-20
  (page: did not load (403))
- Sat 21 Nov | Nacionale | Why did Walmart stock go up when the market fell? It rose Friday as investors left AI stocks
  https://www.nacionale.com/en/articles/why-is-walmart-stock-up-today-market-falls-earnings-raised-outlook-november-20
  (page: did not load (403))
## V  (8 leads)
- Fri 20 Nov | Investor's Business Daily | Visa And Regeneron Are Thriving Despite The Market Meltdown
  https://www.investors.com/research/visa-and-regeneron-are-thriving-despite-the-market-meltdown/
  > These stocks have been putting in outstanding performances and landed on best stock lists Friday. Berkley (WRB) shot to a record high Friday. And credit card giant Visa (V) finished the week down but that's after hitting an all-time high on Nov. Copyright ©2026 Investor's Business Daily, LLC.
- Fri 20 Nov | ad-hoc-news.de | Adyen stock: Company joins Visa AI payment program
  https://www.ad-hoc-news.de/boerse/news/corporate-news/adyen-stock-company-joins-visa-ai-payment-program/70540556
  > Adyen will work with Visa on infrastructure for AI-initiated payments after Visa announced the expansion of its Agentic Ready program on November 17, 2026. The program brings payment service providers, merchants, acquirers and commerce platforms into a framework for testing agent-led transactions.
- Fri 20 Nov | Benzinga | Visa Short Interest Rises But Remains Below August Peak
  https://www.benzinga.com/trading-ideas/short-ideas/26/11/63482454/visa-short-interest-rises-but-remains-below-august-peak
  (page: did not load (403))
## ORCL  (8 leads)
- Sat 21 Nov | The Globe and Mail | Snowflake, C3.ai, SentinelOne, DigitalOcean, and Oracle shares are falling, what you need to know
  https://www.theglobeandmail.com/investing/markets/stocks/ORCL-N/pressreleases/8942344/snowflake-c3-ai-sentinelone-digitalocean-and-oracle-shares-are-falling-what-you-need-to-know/
  > Snowflake, C3.ai, SentinelOne, DigitalOcean, and Oracle shares are falling, what you need to know A number of stocks fell in the afternoon session after AI-linked shares continued to pull back. Anthropic slid more than 10% following its debut, failing to revive confidence in the sector's spending boom.
- Sat 21 Nov | Startup Fortune | Oracle says its $300 billion OpenAI buildout is fully funded after a $20 billion raise
  https://startupfortune.com/oracle-says-its-300-billion-openai-buildout-is-fully-funded-after-a-20-billion-raise/
  > Oracle wants you to stop asking who's paying for its OpenAI data centres. Whether a company can say "funded" and still be the market's favourite AI borrower is the question that matters.
- Sat 21 Nov | NewsBytes | Oracle raises $20B for OpenAI deal to add 4.5 gigawatts
  https://www.newsbytesapp.com/news/business/oracle-raises-20b-for-openai-deal-to-add-45-gigawatts/tldr
  (page: did not load (403))
- Sat 21 Nov | ad-hoc-news.de | Oracle Refutes OpenAI Funding Doubts After Shares Slide to 52-Week Low
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-refutes-openai-funding-doubts-after-shares-slide-to-52-week-low/70541319
  > Oracle has moved to shut down speculation that its infrastructure contract with OpenAI is short of cash, insisting the deal is fully funded even as its stock slumped to a fresh 52-week low.
- Sat 21 Nov | Cryptopolitan | OpenAI build no longer hinges on extra vendor deals, Oracle says
  https://www.cryptopolitan.com/openai-build-no-longer-hinges-vendor-deals/
- Sat 21 Nov | ABC Money | Oracle says OpenAI deal is fully funded after final capital raise
  https://www.abcmoney.co.uk/2026/11/oracle-says-openai-deal-is-fully-funded-after-final-capital-raise/
- Fri 20 Nov | MLQ.ai | Oracle says its OpenAI infrastructure contract is fully funded after a final capital raise
  https://mlq.ai/news/oracle-says-its-openai-infrastructure-contract-is-fully-funded-after-a-final-capital-raise/
- Fri 20 Nov | BigGo Finance | Oracle Says OpenAI Compute Build Is Fully Funded, Touts $20 Billion Raise
  https://finance.biggo.com/news/21dc133e-29cc-4e48-880d-0d10195069ca
## COST  (8 leads)
- Fri 20 Nov | kalkine.ca | Unusual Volume Alert: Costco (NASDAQ:COST) Shares Rise in Active Trading
  https://kalkine.ca/news/retail/unusual-volume-alert-costco-nasdaqcost-shares-rise-in-active-trading
  (page: did not load (403))
- Fri 20 Nov | Pluang | Costco to pay $30 special dividend on Dec 4, do...
  https://pluang.com/en/news-feed/costco-dividen-spesial-ganda-2026-saham-konsumer-tangguh
  (page: did not load (403))
- Fri 20 Nov | CryptoRank | Wrapped Costco Tokenized Stock (xStock): Funding, Investors, Team and Key Events
  https://cryptorank.io/price/wrapped-costco-tokenized-stock-xstock
  (page: did not load (403))
## NFLX  (8 leads)
- Fri 20 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Stock Falls 3% - What's Next?
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-stock-falls-3-whats-next-2026-11-20/
  > Netflix (NASDAQ:NFLX) Stock Falls 3% - What's Next? - Netflix shares fell 3% to $56.73 in Friday’s mid-day trading, while volume ran 53% above its daily average. - Near-term concerns include a softer fourth-quarter outlook and a reduced 2026 advertising-revenue forecast of about $2.7 billion, alongside reports of slower growth and weaker viewer engagement.
- Fri 20 Nov | TIKR.com | Prediction: Netflix and Disney Will “Blame Grand Theft Auto” for Falling Viewership, per Scott Galloway
  https://www.tikr.com/blog/prediction-netflix-and-disney-will-blame-grand-theft-auto-for-falling-viewership-per-scott-galloway?
  > - Grand Theft Auto VI sold an estimated $2.36 billion of digital copies on its first day, and Scott Galloway predicts Netflix and Disney will blame it for weaker viewership. - Netflix’s growth already comes from price increases and ads, since its view hours grew just 2% in the first half of 2026. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Fri 20 Nov | Traders Union | Netflix stock forecast: Bearish outlook persists with sellers maintaining control
  https://tradersunion.com/news/stocks/show/4351067-netflix-drops-2-91percent-today-to/
  (page: did not load (403))
- Fri 20 Nov | kalkine.ca | Netflix (NASDAQ:NFLX) Stock Today: Unusual Volume as Shares Move Lower
  https://kalkine.ca/news/technology/netflix-nasdaqnflx-stock-today-unusual-volume-as-shares-move-lower
  (page: did not load (403))
- Fri 20 Nov | ChartMill | S&P 500 Most Active Stocks: Netflix and Ford Lead Volume
  https://www.chartmill.com/news/MRVL/Chartmill-59009-SP-500-Most-Active-Stocks-Netflix-and-Ford-Lead-Volume
- Fri 20 Nov | BigGo Finance | Disney and Netflix Converge Near 16x Forward Earnings as Streaming Profit Gap Narrows
  https://finance.biggo.com/news/6d5c3be5-bd27-43d7-af09-9e20816a769c
- Fri 20 Nov | TipRanks | Netflix Stock (NASDAQ:NFLX) Slips, Frequent Downgrades a Mistake
  https://www.tipranks.com/news/netflix-stock-nasdaqnflx-slips-frequent-downgrades-a-mistake
- Fri 20 Nov | Yahoo Finance | Netflix Stock Is Down 36% and Wall Street Keeps Downgrading It. History Says That's a Mistake.
  https://finance.yahoo.com/markets/stocks/articles/netflix-stock-down-36-wall-142700910.html
## INTC  (8 leads)
- Sat 21 Nov | Seeking Alpha | Intel: The 54% Collapse Changes My Rating, But Not My Caution
  https://seekingalpha.com/article/4970794-intel-the-54-percent-collapse-changes-my-rating-but-not-my-caution
  (page: did not load (403))
- Sat 21 Nov | Seeking Alpha | Intel: Valuation Meets Reality, Product Cycle Decides Next Move
  https://seekingalpha.com/article/4970785-intel-valuation-meets-reality-product-cycle-decides-next-move
  (page: did not load (403))
- Fri 20 Nov | GuruFocus | A Look at Intel Corp (INTC) After 7.8% Decline -- GF Value $34.1
  https://www.gurufocus.com/news/9213351/a-look-at-intel-corp-intc-after-78-decline-gf-value-3412-vs-price-5137
  (page: did not load (403))
- Fri 20 Nov | MarketBeat | Intel (NASDAQ:INTC) Stock Falls 8.1% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-intel-nasdaq-intc-stock-falls-81-heres-what-happened-2026-11-20/
  > Intel (NASDAQ:INTC) Stock Falls 8.1% - Here's What Happened - Intel shares fell 8.1% to about $51.22 in Friday mid-day trading, with volume 72% above the average. - Investor signals were mixed: CEO Lip-Bu Tan bought 150,000 shares, while Nvidia cut its Intel stake by 25% in the third quarter.
- Fri 20 Nov | MarketWatch | Intel Corp. stock outperforms competitors despite losses on the day
  https://www.marketwatch.com/data-news/intel-corp-stock-outperforms-competitors-despite-losses-on-the-day-5d4bb1a1-ee89965323d8?mod=goog_fin_scmw
- Fri 20 Nov | Investor's Business Daily | Could Jensen Huang Land At Nvidia Rival Intel?
  https://www.investors.com/news/technology/nvidia-stock-could-jensen-huang-land-at-intel/
- Fri 20 Nov | StockStory | Broadcom, Intel, Nvidia, and Qualcomm stocks trade down, what you need to know
  https://stockstory.org/us/stocks/nasdaq/avgo/news/why-up-down/broadcom-intel-nvidia-and-qualcomm-stocks-trade-down-what-you-need-to-know
- Fri 20 Nov | The Motley Fool | AMD Is Down 26% and Intel Is Down 42%. Which AI Stock Is Worth Buying on the Dip?
  https://www.fool.com/coverage/better-buy/2026/11/20/amd-is-down-26-and-intel-is-down-42-which-ai-stock-is-worth-buying-on-the-dip/
## LLY  (8 leads)
- Sat 21 Nov | Fox Business | Eli Lilly, United Healthcare amid popular non-AI investment opportunities
  https://www.foxbusiness.com/video/6408680373112
  (page read: it never names the company, so probably not about it: skip)
- Fri 20 Nov | Yahoo Finance | Eli Lilly (LLY) After ObesityWeek Is The Stock Still Undervalued
  https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-obesityweek-stock-201358942.html
  > Eli Lilly (LLY) is back in focus after ObesityWeek 2026, where the company released fresh clinical data on its obesity and sleep apnea pipeline, including EloraTZP, retatrutide and Foundayo. The latest ObesityWeek data arrived in a choppy tape for Eli Lilly.
- Fri 20 Nov | BigGo Finance | Biotech's Rough Week: Only 14% of M&A Rumors Pan Out, and Lilly Is Buying Everything in Sight
  https://finance.biggo.com/news/d18f03a2aa0fc696
  (page: did not load (429))
Read 62 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, ALCN, MFPC, EAST, EFIH, EGAL, AMOC, SKPC.
