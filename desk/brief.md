# Desk brief, Monday, November 23, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 71s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-20 (35.89); Treasury yields to 2026-11-20 (10-year 4.92%).
- **valuation**: ok in 25s (GitHub Actions). LLY: $1.29tn, P/E (last 12 months) 42.2, Forecast P/E (fiscal 2026) 37.8 (the four quarters to Sep 2026)
- **movers**: ok in 20s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 41.1
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.1%, median P/E 9.8; cheapest MASR +74%, PHAR +52%, MFPC +47%; dearest ARAB -62%, MOIN -64%, BTFH -66%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 76s (GitHub Actions). 
- **news**: ok in 95s (GitHub Actions). 
- **leads**: ok in 68s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 7 failed, 0 needed a retry (fetch_intraday.py); api.polygon.io: 3 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 13 needed a retry.

## What moved (latest close against the one before)
- EGX30 49,989.80 (-2.85%); EGX70 EWI 16,534.40 (-5.55%); USD/EGP 54.50 (+1.16%); Gold 21K 5,570.00 (+1.09%); Brent 92.57 (+0.64%); S&P 500 6,910.39 (-3.70%); Nasdaq 22,617.73 (-5.28%); Bitcoin 61,450.00 (+4.06%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): NVDA -14.0%, AVGO -12.2%, ORCL -8.5%, INTC -8.0%, TSLA -7.6%, EMFD -6.3%, JUFO -6.0%, META -5.9%, EFIH -5.6%, ALCN -5.3%, MFPC -5.3%, PHDC -5.1%, AMOC -4.9%, BQDC -4.5%, EAST -4.3%, TMGH -4.3%, EFID -4.3%, AMZN -4.1%, SKPC -3.4%, ABUK -3.1%, JPM -3.0%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - ALCN: No clear trend: 6.4% below its 50-day average and 1.9% above the 200-day; RSI 39, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - EGAL: Turning down: below both its 50-day average (9.2% under) and its 200-day (0.8% under), though the 50-day is still above the 200-day; RSI 38, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - JUFO: Turning down: below both its 50-day average (11.3% under) and its 200-day (8.6% under), though the 50-day is still above the 200-day; RSI 35, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - ORAS: No clear trend: 5.1% below its 50-day average and 15.5% above the 200-day; RSI 42, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - AMZN: No clear trend: 3.2% below its 50-day average and 0.7% above the 200-day; RSI 42, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - GOOGL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 28, washed out: below 30; momentum turned down today (MACD crossed its signal line).
    - INTC: Turning down: below both its 50-day average (43.2% under) and its 200-day (41.4% under), though the 50-day is still above the 200-day; RSI 28, washed out: below 30; momentum turned up 2 sessions ago (MACD crossed its signal line).
    - META: Turning down: below both its 50-day average (17.1% under) and its 200-day (10.8% under), though the 50-day is still above the 200-day; RSI 30, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - NFLX: In a downtrend: below its 50-day average, which is below the 200-day; RSI 27, washed out: below 30; momentum turned down 3 sessions ago (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (39.4% under) and its 200-day (38.3% under), though the 50-day is still above the 200-day; RSI 15, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- EGX COPR (Cooper for Commercial Investment & Real Estate Development) +13.3%; EGX DTPP (Delta for Printing & Packaging) +12.2%; EGX OIH (Orascom Investment Holding) +10.8%; EGX ICFC (International Co. for Fertilizers & Chemicals) +9.9%; EGX GRCA (Grand Investment Capital) +9.4%; EGX CRST (Creast mark For Contracting) -8.3%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-23 (TradingView's closes; Mubasher's list refused), 198 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (211)
US: the market is trading; kept the saved session
US week and month: US companies worth $10bn or more (813)
EGX30 heatmap: 2026-11-23, 31 members
US heatmap: 2026-11-20, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-23
## COPR +13.3%  Cooper for Commercial Investment & Real Estate Development
- no headlines found
## DTPP +12.2%  Delta for Printing & Packaging
- no headlines found
## OIH +10.8%  Orascom Investment Holding
- no headlines found
## ICFC +9.9%  International Co. for Fertilizers & Chemicals
- no headlines found
## GRCA +9.4%  Grand Investment Capital
- no headlines found
## CRST -8.3%  Creast mark For Contracting
- no headlines found
## RKAZ -4.5%  REKAZ Financial Holding
- no headlines found
## ELWA -1.7%  Elwadi for International Investment & Development
- no headlines found
## CPCI -1.3%  Kahira Pharmaceuticals & Chemical Industries
- no headlines found
## MOIL -1.3%  Maridive & Oil Services
- no headlines found

# US 2026-11-20
## GPN +9.9%  Global Payments
- Mon 23 Nov | Benzinga | Why Is Global Payments Stock Rising Monday?
  https://www.benzinga.com/m-a/26/11/63524391/why-is-global-payments-stock-rising-monday
- Mon 23 Nov | Quantisnow | Citizens initiated coverage on Global Payments
  https://www.quantisnow.com/insight/citizens-initiated-coverage-on-global-payments-6803158
- Mon 23 Nov | TradingKey | Global Payments Jumps 10% on a GTCR Takeover Report, but Can GPN Clear $92.32?
  https://www.tradingkey.com/analysis/stocks/us-stocks/262317695-global-payments-jumps-10-percent-gtcr-takeover-report-gpn-92-32-pivot-november-23-2026-tradingkey
- Mon 23 Nov | Yahoo Finance | GTCR considers potential takeover of Global Payments
  https://finance.yahoo.com/news/gtcr-considers-potential-takeover-global-090254381.html
## BIP +4.5%  Brookfield Infrastructure Partners L.P
- Mon 23 Nov | Yahoo Finance Singapore | Brookfield Infrastructure Partners L.P. (BIP) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/BIP/
- Mon 23 Nov | Yahoo Finance | Brookfield Infrastructure (BIPC) is Back on Investors’ Radar Ahead of This Key Event
  https://finance.yahoo.com/markets/stocks/articles/brookfield-infrastructure-bipc-back-investors-043222176.html
- Sun 22 Nov | CoinGecko | RBIP to MYR: Brookfield Infrastructure Partners L.P. Tokenized Stock (Reality) Price in Malaysian Ringgit
  https://www.coingecko.com/en/coins/brookfield-infrastructure-partners-l-p-rstock/myr
- Sun 22 Nov | Yahoo! Finance Canada | Brookfield Infrastructure Partners L.P. (BIP-UN.TO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BIP-UN.TO/
## RKT +4.2%  Rocket Companies
- Mon 23 Nov | Yahoo Finance Singapore | Rocket Companies, Inc. (RKT) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/RKT/
- Mon 23 Nov | MarketBeat | Rocket Companies, Inc. (NYSE:RKT) Stock Rated "Moderate Buy" by Sell-Side Analysts
  https://www.marketbeat.com/instant-alerts/consensus-rocket-companies-inc-nyse-rkt-stock-rated-moderate-buy-by-sell-side-analysts-2026-11-23/
- Sat 21 Nov | Yahoo! Finance Canada | Rocket Companies, Inc. (RKT) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance | Rocket Companies (RKT) Just Got a Major Win — Wall Street Is Reacting
  https://finance.yahoo.com/markets/stocks/articles/rocket-companies-rkt-just-got-071103140.html
## MKC.V +3.8%  McCormick & Company, Incorporated
- Sun 22 Nov | Yahoo! Finance Canada | McCormick & Company, Incorporated (MKC) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/MKC/
- Sat 21 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Stock Breaks Above 50 Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-stock-breaks-above-50-day-moving-average-whats-next-2026-11-21/
- Sat 21 Nov | Timothy Sykes | McCormick & Company Incorporated (MKC) Stock Price | Live Quotes & Charts | NYSE
  https://www.timothysykes.com/quote/MKC/
- Fri 20 Nov | kalkine.com | McCormick & Company Incorporated (NYSE: MKC.V) Stock Price, News & Analysis
  https://kalkine.com/company/nyse-mkc-v/
## GIS +3.7%  General Mills
- Sun 22 Nov | Simply Wall St | How Operating Reorganization Will Impact General Mills (GIS) Investors
  https://simplywall.st/stocks/us/food-beverage-tobacco/nyse-gis/general-mills/news/how-operating-reorganization-will-impact-general-mills-gis-i
- Sun 22 Nov | Yahoo Finance | General Mills vs. Kraft Heinz: Which Food Dividend Is Better for Retirees?
  https://finance.yahoo.com/markets/stocks/articles/general-mills-vs-kraft-heinz-200733902.html
- Sun 22 Nov | 24/7 Wall St. | General Mills vs. Kraft Heinz: Which Food Dividend Is Better for Retirees?
  https://247wallst.com/investing/2026/11/22/general-mills-vs-kraft-heinz-which-food-dividend-is-better-for-retirees/?tpid=1713331&tv=link&tc=in_content
- Sun 22 Nov | Yahoo! Finance Canada | General Mills, Inc. (GIS) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/GIS/
## NBIS -16.1%  Nebius Group
- Mon 23 Nov | Benzinga | Why Is Nebius Stock Surging on Monday?
  https://www.benzinga.com/trading-ideas/movers/26/11/63529536/why-is-nebius-stock-surging-on-monday-2
- Mon 23 Nov | SuaraGarut.ID | Nebius Faces Stock Pressure After AI Capacity Delays
  https://suaragarut.id/en/nebius-stock-ai-capacity-delays
- Mon 23 Nov | bsinews.id | Nebius Shares Extend Losses as Revenue Delays Pressure Investors
  https://bsinews.id/en/nebius-shares-revenue-delays
- Mon 23 Nov | Kalkine | What Would USD 500 a Month in Nebius Group (NASDAQ:NBIS) Need to Reach USD 1 Million After a Monthly Drop of More Than 40%?
  https://kalkine.com.au/news/technology/what-would-usd-500-a-month-in-nebius-group-nasdaqnbis-need-to-reach-usd-1-million-after-a-monthly-drop-of-more-than-40
## CLS -16.1%  Celestica
- Mon 23 Nov | Kalkine Media | Celestica (NYSE:CLS) Upgraded As AI Server Demand Lifts Manufacturers
  https://kalkinemedia.com/us/stocks/technology/celestica-nysecls-upgraded-as-ai-server-demand-lifts-manufacturers
- Mon 23 Nov | Yahoo! Finance Canada | Celestica Inc. (CLS.TO) Interactive Stock Chart - Yahoo Finance
  https://ca.finance.yahoo.com/quote/CLS.TO/chart/
- Mon 23 Nov | Trefis | What Explains The Move In Celestica Stock?
  https://www.trefis.com/stock/cls/articles/627771/what-explains-the-move-in-celestica-stock/2026-11-23
- Mon 23 Nov | MarketBeat | Celestica (NYSE:CLS) Upgraded to Buy at Wall Street Zen
  https://www.marketbeat.com/instant-alerts/analyst-celestica-nyse-cls-upgraded-to-buy-at-wall-street-zen-2026-11-23/
## SNDK -16.1%  Sandisk
- Mon 23 Nov | GuruFocus | Evercore Has Strong Verdict on Beaten-Down Sandisk Stock
  https://www.gurufocus.com/news/9214560/evercore-has-strong-verdict-on-beatendown-sandisk-stock?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141
- Mon 23 Nov | Seeking Alpha | Sandisk climbs 12% as technology shares rally (SNDK:NASDAQ)
  https://seekingalpha.com/news/4675604-sandisk-climbs-12-as-technology-shares-rally
- Mon 23 Nov | TIKR.com | SK Hynix Soars 21%, Sandisk Up 22% as Memory Stocks Rebound From AI Rout
  https://www.tikr.com/blog/sk-hynix-soars-8-sandisk-up-6-as-memory-stocks-rebound-from-ai-rout?ref=yahoofinance&tlnk=yf-261123-3qjfmh53
- Mon 23 Nov | Yahoo Finance | Even If Sandisk's Profits Get Cut in Half, Here's What $5,000 in the Stock Could Be Worth by 2030
  https://finance.yahoo.com/markets/stocks/articles/even-sandisks-profits-cut-half-144301892.html
## BE -15.3%  Bloom Energy
- Mon 23 Nov | Seeking Alpha | Bloom Energy climbs 19% on AI rebound (BE:NYSE)
  https://seekingalpha.com/news/4675605-bloom-energy-climbs-19-on-ai-rebound
- Mon 23 Nov | Limapagi | Bloom Energy Shares Fall 60% as AI Power Stocks Slide
  https://www.limapagi.id/en/bloom-energy-ai-power-selloff
- Mon 23 Nov | Seeking Alpha | Bloom Energy: Its Low-Cost 5 GW Expansion Offers Strong Upside
  https://seekingalpha.com/article/4971029-bloom-energy-stock-its-low-cost-5-gw-expansion-offers-strong-upside
- Mon 23 Nov | Renewable Energy Industry | Stock Market, Week 47/26: RENIXX Loses 10.6 Percent and Falls Below 1,000 Points – Grenergy, Bloom Energy and Enphase Energy Plunge
  https://www.renewable-energy-industry.com/news/world/article-7778-stock-market-week-47-26-renixx-loses-106-percent-and-falls-below-1000-points-grenergy-bloom-energy-and-enphase-energy-plunge
## CRDO -15.2%  Credo Technology Group Holding
- Mon 23 Nov | Yahoo Finance | Credo Technology Group Stock And 2 Undervalued Stocks To Watch
  https://finance.yahoo.com/markets/stocks/articles/credo-technology-group-stock-2-111251300.html
- Sun 22 Nov | Simply Wall St | What Investors Got Wrong About Credo Technology Group Before The Drop
  https://simplywall.st/stocks/us/semiconductors/nasdaq-crdo/credo-technology-group-holding/news/what-investors-got-wrong-about-credo-technology-group-before/amp
- Sat 21 Nov | Benzinga | Benzinga Bulls and Bears: Nvidia, Credo, Red Cat
  https://www.benzinga.com/markets/market-summary/26/11/63515125/benzinga-bulls-and-bears-nvidia-credo-red-cat
- Sat 21 Nov | Simply Wall St | Credo Technology Group Holding (Nasdaq:CRDO) - Stock Analysis
  https://simplywall.st/stocks/us/semiconductors/nasdaq-crdo/credo-technology-group-holding
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: WMT, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-23 CLHO results (expected)
- 2026-11-23 EAST results (expected)  <- write its preview
- 2026-11-23 EFID results (expected)
- 2026-11-23 EFIH results (expected)  <- write its preview
- 2026-11-23 JUFO results (expected)
- 2026-11-23 PHDC results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (on track)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
    Views: nothing to change.

## Fair value
- Changed since the last run: LCSW -43% -> -45% (medium -> low).
- In the ten cheapest or dearest with no note: MCQE, ADIB, EMFD, ISPH, MTIE, AMOC, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-23. Open each story before using it.
## COMI  (8 leads)
- Mon 23 Nov | بوابة مولانا | البنك التجاري الدولي يطلق CIB Pay على هواتف أندرويد
  https://mwlana.com/details/362970/
  > أعلن البنك التجاري الدولي – مصر (CIB) الإطلاق والتشغيل الرسمي لتطبيق «CIB Pay» لجميع عملائه بدءًا من اليوم، 23 نوفمبر 2026، ليتيح إجراء معاملات الدفع الإلكتروني عبر الدفع عبر هواتف أندرويد باستخدام تقنية «اضغط للدفع» (Tap to Pay) دون الحاجة لاستخدام البطاقة البلاستيكية، استكمالًا للخدمة المتاحة سابقًا لعملاء هواتف «آيفون» العاملة بنظام iOS.
- Mon 23 Nov | جريدة المال | خطوة بخطوة.. طريقة تفعيل الدفع بالموبايل في بنوك الأهلي ومصر وCIB وQNB
  https://almalnews.com/2149113/خطوة-بخطوة-طريقة-تفعيل-الدفع-بالموبايل-في/
  > تتيح خدمة الدفع بالموبايل تحت عنوان (ترميز بطاقات الدفع) على تطبيقات الهواتف المحمولة العاملة بنظام أندرويد، التي أطلقها البنك المركزي المصري بالتعاون مع البنوك وشركات التكنولوجيا المالية، إضافة نسخة رقمية مشفرة من بطاقة الدفع الإلكترونية على الهاتف لاستخدامها في الشراء اللاتلامسي عبر نقاط البيع الإلكترونية (POS) أو المواقع والتطبيقات الإلكترونية (E-commerce).
- Mon 23 Nov | أصول مصر | CIB يرفع عائد الشهادة الثلاثية إلى 19%.. تفاصيل الشراء والصرف الشهري
  https://www.osoulmisrmagazine.com/453279
  > CIB يرفع عائد الشهادة الثلاثية إلى 19%.. تفاصيل الشراء والصرف الشهري أعلن البنك التجاري الدولي – مصر (CIB) زيادة سعر العائد على شهادة الادخار الثلاثية ذات العائد الثابت إلى 19% سنويًا، مع صرف الأرباح بشكل شهري، على أن يبدأ العمل بالسعر الجديد اعتبارًا من اليوم الاثنين 23 نوفمبر 2026. تفاصيل شهادة CIB الثلاثية بعائد 19%
## TMGH  (3 leads)
- Sun 22 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | صندوق الاستثمارات يوقع مذكرة تفاهم مع مجموعة طلعت مصطفى لتعزيز فرص التعاون
  https://www.argaam.com/ar/article/articledetail/id/1910794
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | Mubasher | مع تهاوي بورصة مصر.. كيف جاء أداء "التجاري الدولي" و"طلعت مصطفى"؟
  https://www.mubasher.info/news/21588660/مع-تهاوي-بورصة-مصر-كيف-جاء-أداء-التجاري-الدولي-و-طلعت-مصطفى
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | شبكة تواصل الإخبارية | النائب عبدالرحمن بشاري يبحث مع هشام طلعت مصطفى أولوية توظيف أبناء الأقصر
  https://twaslnews1.twaslnews.com/8087323/
  (page: did not load (403))
## ETEL  (1 leads)
- Sun 22 Nov | Mubasher | 6 أسهم ترتفع وتخالف الاتجاه الهابط لبورصة مصر.. منها المصرية للاتصالات
  https://www.mubasher.info/news/21588645/6-أسهم-ترتفع-وتخالف-الاتجاه-الهابط-لبورصة-مصر-منها-المصرية-للاتصالات
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## PHDC  (1 leads)
- Sun 22 Nov | اليوم السابع | خريطة تحركات الكبار بالبورصة.. مشتريات في فوري ومصر الجديدة وتخارجات من بالم هيلز
  https://www.youm7.com/story/2026/11/22/خريطة-تحركات-الكبار-بالبورصة-مشتريات-في-فوري-ومصر-الجديدة-وتخارجات/7627730
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية خلال جلسة تداول يوم الخميس الماضي، تنفيذ عدد من عمليات الشراء والبيع على أسهم الشركات المقيدة، تصدرتها عمليات الشراء على سهم شركة نهر الخير للتنمية والاستثمار الزراعي والخدمات البيئية، إلى جانب تداولات على أسهم مينا للاستثمار السياحي والعقاري، وفوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، وبالم هيلز ...
## SWDY  (7 leads)
- Mon 23 Nov | سولارابيك | باستطاعة 90 ميجاواط.. السويدي إليكتريك تنفّذ مشروعا للطاقة الشمسية في أنجولا
  https://solarabic.com/أخبار-الطاقة-المتجددة/2026/11/باستطاعة-90-ميجاواط-السويدي-إليكتريك-ت/
  > سولارابيك- دبي، الإمارات العربية المتحدة – 23 نوفمبر 2026: بدأت شركة السويدي إليكتريك لنقل وتوزيع الطاقة T&D تنفيذ مشروع كابيندا للطاقة الشمسية الكهروضوئية في أنجولا، بعد وضع حجر الأساس للمشروع بالتعاون مع شركة PRODEL-EP، الجهة المالكة، في خطوة تستهدف تعزيز إمدادات الكهرباء وتوسيع الاعتماد على مصادر الطاقة المتجددة في البلاد.
- Sun 22 Nov | almotawwer.com | السويدي إليكتريك تنفذ محطة طاقة شمسية بقدرة 90 ميجاوات في أنجولا لخدمة 30 ألف أسرة
  https://almotawwer.com/companies-and-investments/335050/
  > تواصل الشركات المصرية توسيع حضورها في سوق مشروعات الطاقة والبنية التحتية بالقارة الإفريقية، مستفيدة من خبراتها الهندسية وقدراتها التنفيذية في اقتناص مشروعات خارج السوق المحلية، بالتزامن مع توجه عدد من الدول الإفريقية إلى زيادة الاعتماد على مصادر الطاقة المتجددة وتطوير شبكات الكهرباء.
- Sun 22 Nov | خاص عن مصر | "السويدي إليكتريك" تعتزم رفع إنتاجها من شواحن السيارات الكهربائية بمصر لأكثر من 25 ألف سنويًا
  https://aboutmsr.com/السويدي-إليكتريك-تعتزم-رفع-إنتاجها-م/
  > تستهدف مجموعة السويدي إليكتريك زيادة الطاقة الإنتاجية لمصنعها المتخصص في تصنيع شواحن السيارات الكهربائية بمدينة العاشر من رمضان، لتتجاوز 25 ألف شاحن سنوياً، في خطوة تستهدف مواكبة نمو سوق التنقل الكهربائي في مصر، وتعزيز التصنيع المحلي لمكونات البنية التحتية اللازمة لتشغيل السيارات الكهربائية.
- Sun 22 Nov | موقع و جريدة أخبار الناس اليوم | السويدي اليكتريك لنقل و توزيع الطاقة (T&D) تضع حجر الأساس لمشروع كابيندا للطاقة الشمسية لخدمة أكثر من 30 ألف أسرة في أنجولا
  https://www.akhbarelnaselyoum.com/archives/208961
  > احتفلت شركة السويدي إليكتريك لنقل وتوزيع الطاقة T&Dمع شركة PRODEL-EP، الجهة المالكة للمشروع، بوضع حجر الأساس لمشروع كابيندا للطاقة الشمسية الكهروضوئية في أنجولا، لتبدأ أعمال تنفيذ المشروع الذي يستهدف دعم قدرات قطاع الكهرباء الأنجولي، وتوسيع نطاق الاعتماد على مصادر الطاقة المتجددة، من خلال توفير إمدادات كهربائية نظيفة ومستقرة لأكثر من 30 ألف أسرة، بما يعزز ...
- Sun 22 Nov | التعمير | السويدي إليكتريك تضع حجر الأساس لمشروع كابيندا للطاقة الشمسية في أنجولا لخدمة 30 ألف أسرة
  https://eltaameer.com/archives/486006
- Sun 22 Nov | أموال الغد | «السويدي إليكتريك» تنتج 25 ألف شاحن سيارات كهربائية سنويًا بمصنع العاشر من رمضان
  https://amwalalghad.com/2026/11/22/السويدي-إليكتريك-تنتج-25-ألف-شاحن-سيار/
- Sun 22 Nov | جريدة المال | السويدي إليكتريك تضع حجر أساس محطة شمسية بقدرة 90 ميجاوات بأنجولا لخدمة 30 ألف أسرة
  https://almalnews.com/2148863/السويدي-إليكتريك-تضع-حجر-أساس-محطة-شمسية/
## ORAS  (6 leads)
- Sun 22 Nov | https://www.youlyou.com/ | البورصة تفحص مستندات زيادة رأسمال أوراسكوم كونستراكشون إلى 207.4 مليون دولار
  https://www.youlyou.com/100438
  > تقدمت شركة أوراسكوم كونستراكشون بي إل سي بمستندات قيد أسهم زيادة رأس المال المصدر والمدفوع إلى البورصة المصرية، ليرتفع رأس المال من 110.24 مليون دولار إلى 207.44 مليون دولار، بزيادة قدرها 97.2 مليون دولار. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Sun 22 Nov | شبكة تواصل الإخبارية | «أوراسكوم كونستراكشون» تتقدم بمستندات زيادة رأس المال لـ207.4 مليون دولار
  https://twaslnews1.twaslnews.com/8126107/
  (page: did not load (403))
- Sun 22 Nov | جريدة المال | «أوراسكوم كونستراكشون» تقدم مستندات قيد زيادة رأسمالها لمبادلة أسهم «OCI N.V»
  https://almalnews.com/2148879/«أوراسكوم-كونستراكشون»-تقدم-مستندات-قيد-زيادة-رأسمالها/
  > أعلنت إدارة البورصة المصرية تقدم شركة أوراسكوم كونستراكشون بي إل سي بمستندات قيد أسهم زيادة رأس المال من 110.24 مليون دولار إلى 207.45 مليون دولار، بزيادة قدرها 97.20 مليون دولار.
- Sun 22 Nov | جريدة البورصة | "أوراسكوم كونستراكشون" تتقدم بمستندات زيادة رأسمالها إلى 207.4 مليون دولار
  https://alborsaanews.com/2026/11/22/2008136
  > تقدمت شركة أوراسكوم كونستراكشون بي ال سي، إلى إدارة البورصة بمستندات قيد أسهم زيادة رأس المال المصدر والمدفوع من 110.24 مليون دولار، إلى 207.44 مليون دولار. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sun 22 Nov | آراب فاينانس | أوراسكوم كونستراكشون تتقدم إلى البورصة بمستندات زيادة رأس المال
  http://www.arabfinance.com/ar/news/newdetails/أوراسكوم-كونستراكشون-تتقدم
- Sun 22 Nov | The Fintech Times | OCI Shareholders Approve Orascom Construction Combination at EGM
  https://thefintechtimes.com/oci-shareholders-approve-orascom-construction-combination-at-egm/
## FWRY  (4 leads)
- Mon 23 Nov | العربية | السودان يعلن تفاصيل نظام الدفع الفوري.. تحويلات بدون إنترنت
  https://www.alarabiya.net/aswaq/economy/2026/11/23/السودان-يعلن-تفاصيل-نظام-الدفع-الفوري-تحويلات-بدون-انترنت
  (page: did not load (403))
- Sun 22 Nov | موقع القيادي | قصة نجاح فوري.. من دفع الفواتير إلى أرباح 2.9 مليار جنيه
  https://www.alqiyady.com/قصة-نجاح-فوري-من-دفع-الفواتير-إلى-أرباح-29-مليار-جنيه-897363.html
  (page: only 42 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | CairoScene | Fawry Allocates $1.6 Million for Cybersecurity Investments
  https://cairoscene.com/Business/Fawry-Allocates-1-6-Million-for-Cybersecurity-Investments
  > Fawry Allocates $1.6 Million for Cybersecurity Investments The fintech company is directing LE 80 million towards technology upgrades by the end of 2026. Egyptian fintech company Fawry plans to allocate LE 80 million (approximately $1.6 million) towards technology investments by the end of 2026, prioritising cybersecurity and improvements to its digital infrastructure.
## ABUK  (1 leads)
- Sun 22 Nov | www.marketscreener.com | Abu Qir Fertilizers & Chemical Industries Company (S.A.E) Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
  https://www.marketscreener.com/news/abu-qir-fertilizers-chemical-industries-company-s-a-e-reports-earnings-results-for-the-third-qua-ce785ed3d088f024
  (page: did not load (403))
## HRHO  (6 leads)
- Mon 23 Nov | The TRADE | People Moves Monday: TD Securities, Verition Fund Management and EFG Holding
  https://www.thetradenews.com/people-moves-monday-td-securities-verition-fund-management-and-efg-holding/
  > Vinisha Minocha has joined TD Securities in New York as a director in electronic trading. She joins from Liquidnet, where she served as head of algos coverage for the US for more than eight years.
- Mon 23 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | ad-hoc-news.de | EFG Holding stock: Q3 revenue rises 5%, profit falls 15%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/efg-holding-stock-q3-revenue-rises-5-profit-falls-15/70544966
  > EFG Holding reported a mixed third quarter on November 18, 2026, as stronger investment-bank and non-bank finance revenue was offset by higher expenses and weaker commercial-bank performance. In its EFG Holding earnings release, the group reported net operating revenue of EGP6.652 billion for 3Q26 and net profit after tax and minority interest of EGP720 million. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
## CLHO  (1 leads)
- Mon 23 Nov | ad-hoc-news.de | Cleopatra Hospitals stock flags delay in financial statements
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/cleopatra-hospitals-stock-flags-delay-in-financial-statements/70544940
  > Cleopatra Hospital Company said on November 18, 2026, that it would submit its financial statements for the period ended September 30, 2026 later than scheduled. The disclosure was carried by Sigma Capital, citing a release from the Egyptian Exchange.
## JUFO  (3 leads)
- Mon 23 Nov | ad-hoc-news.de | Juhayna stock: Nine-month net profit jumps 60.1% in 2026
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/juhayna-stock-nine-month-net-profit-jumps-60-1-in-2026/70544931
  > Juhayna Food Industries reported a sharp rise in earnings for the first nine months of 2026. According to Arab Finance, the company said on November 11, 2026, that consolidated net profit attributable to the parent company reached EGP 2.035 billion for the January-September period, compared with EGP 1.271 billion a year earlier. [Figures on the page: standalone; consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Sun 22 Nov | INSITE OOH Media Platform | Juhayna Features Yasmina El Abd in Its Latest OOH Campaign in Egypt
  https://insiteooh.com/public/article/14829-juhayna-features-yasmina-el-abd-in-its-latest-ooh-campaign-in-egypt
  > Juhayna Features Yasmina El Abd in Its Latest OOH Campaign in Egypt Juhayna returns to Egypt’s out-of-home advertising scene with a campaign featuring Egyptian actress Yasmina El Abd, a refreshed brand identity and multiple products from its portfolio. The activity follows Juhayna’s May 2026 outdoor campaign promoting two Labna flavours.
- Sun 22 Nov | مصر الآن | صيانة كهرباء مرتقبة في جهينة وطهطا اليوم.. فصل 20 مغذيًا لمدة 5 ساعات
  https://misrelaan.com/article/143767/صيانة-كهرباء-مرتقبة-في-جهينة-وطهطا-اليوم
  > صيانة كهرباء مرتقبة في جهينة وطهطا اليوم.. فصل 20 مغذيًا لمدة 5 ساعات من المقرر فصل التيار الكهربائي، اليوم الأحد 22 نوفمبر، عن مناطق ومحطات خدمية في مركزي جهينة وطهطا بمحافظة سوهاج، من العاشرة صباحًا حتى الثالثة عصرًا، لتنفيذ الصيانة المبرمجة بلوحة توزيع جهينة «2» في نزلة علي.
## MFPC  (4 leads)
- Sun 22 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | ايكونومي بلس | "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو"
  https://economyplusme.com/ar/news/34326
  > "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو" أبقت شركة "سي آي كابيتال" على توصيتها المحايدة لسهمي "أبو قير للأسمدة" و"مصر لإنتاج الأسمدة – موبكو"، مع رفع السعر المستهدف للسهمين، في ظل تذبذب أسعار اليوريا والتوترات الجيوسياسية المرتبطة بمضيق هرمز.
- Sun 22 Nov | بوابة الزهراء | سي آي كابيتال ترفع السعر المستهدف لسهمي أبوقير وموبكو في السوق المالية
  https://zahraa.mr/1348/سي-آي-كابيتال-ترفع-السعر-المستهدف-لسهم/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | جريدة آخر الأخبار | سي آي كابيتال تعدل السعر المستهدف لسهمي أبوقير وموبكو
  https://akher.news/1204/سي-آي-كابيتال-تعدل-السعر-المستهدف-لسهم/
  (page: did not load (403))
## EAST  (2 leads)
- Sat 21 Nov | الهيئة الوطنية للإعلام | طائرة الزمالك تواصل الانتصارات.. ثلاثية نظيفة أمام إيسترن كومباني
  https://www.maspero.eg/sport/2026/11/22/1007679/طائرة-الزمالك-تواصل-الانتصارات--ثلاثية-نظيفة-أمام-إيسترن-كومباني
  > واصل الفريق الأول للكرة الطائرة بنادي الزمالك عروضه القوية في دوري الرجال، بعدما حقق فوزًا مستحقًا على إيسترن كومباني بثلاثة أشواط دون مقابل، ضمن منافسات الجولة السادسة من بطولة الدوري الممتاز للموسم المحلي 2026-2027.
- Sat 21 Nov | اليوم السابع | الزمالك يهزم إيسترن كومبانى فى دورى الطائرة
  https://www.youm7.com/story/2026/11/21/الزمالك-يهزم-إيسترن-كومبانى-فى-دورى-الطائرة/7627524
  > فاز فريق رجال الكرة الطائرة بنادي الزمالك على نظيره إيسترن كومباني بنتيجة 3-0 على صعيد الجولة السادسة بدورى رجال الكرة الطائرة الممتاز للموسم المحلى الجديد 2026 -2027. ويسعى الزمالك إلى مواصلة سلسلة الفوز، بعدما نجح في الفوز بجميع مبارياته في الجولات السابقة.
## BQDC  (8 leads)
- Mon 23 Nov | مجلة البوصلة الاقتصادية | 1 ديسمبر.. نهاية حق البيع في أسهم بنك القاهرة وفق آلية استقرار سعر السهم
  https://alboslanews.com/بنوك-و-تأمين/1-ديمسمبر-نهاية-حق-البيع-في-أسهم-بنك-القاهرة-وفق-آلية-استقرار-سعر-السهم-431365
  > نهاية حق البيع في أسهم بنك القاهرة وفق آلية استقرار سعر السهم الإثنين 23 نوفمبر 2026 -04:53 أعلنت شركة سي أي كابيتال لترويج وتغطية الاكتتابات في الأوراق المالية، أن نهاية الحق للراغبين في إيداع أوامر البيع لدى نظام الحساب المفتوح بالبورصة المصرية لإجمالي أسهم الطرح العام لـ بنك القاهرة، يوم الثلاثاء 1 ديسمبر 2026. [Figures on the page: standalone; consolidated; nine months. Check which one each figure is.]
- Mon 23 Nov | بوابة التكنولوجيا المالية | «بنك القاهرة» يحدد أول ديسمبر آخر موعد لتلقي أوامر بيع الأسهم ضمن آلية استقرار السعر
  https://fintechgate.net/258312
  > الآلية تشمل أسهم الطرح العام فقط «بنك القاهرة» يحدد أول ديسمبر آخر موعد لتلقي أوامر بيع الأسهم ضمن آلية استقرار السعر
- Mon 23 Nov | موقع الموقع | بنك القاهرة يحدد 1 ديسمبر آخر موعد لإعادة الأسهم المباعة ضمن آلية استقرار سعر السهم بالبورصة
  https://almawq3.com/بنك-القاهرة-يحدد-1-ديسمبر-آخر-موعد-لإعاد/
  > كتبت – ماري نادي حدد بنك القاهرة يوم الثلاثاء الموافق 1 ديسمبر 2026، موعدًا نهائيًا لتلقي طلبات بيع الأسهم من المستثمرين الراغبين في الاستفادة من آلية استقرار سعر السهم عقب الطرح في البورصة، وذلك بالنسبة للأسهم المخصصة لشريحة الطرح العام فقط، وفقًا للقواعد والإجراءات المحددة في نشرة الاكتتاب.
- Mon 23 Nov | مصر تايمز | بنك القاهرة يحدد موعد بيع الأسهم ضمن آلية استقرار سعر السهم في السوق
  https://www.masrtimes.com/780917
  > بنك القاهرة يحدد موعد بيع الأسهم ضمن آلية استقرار سعر السهم في السوق كشف بنك القاهرة تحديد يوم الثلاثاء الموافق 1 ديسمبر 2026، آخر موعد للراغبين في بيع أسهمهم ضمن آلية استقرار سعر السهم في السوق عقب الطرح بالبورصة المصرية، وذلك بالنسبة لأسهم الطرح العام فقط. بيع أسهم الطرح العام لبنك القاهرة
- Mon 23 Nov | إقرأ نيوز | بنك القاهرة يحدد 1 ديسمبر آخر موعد لتلقي أوامر البيع ضمن آلية استقرار السهم
  https://www.iqraa.news/252789/بنك-القاهرة-يحدد-1-ديسمبر-آخر-موعد-لتلقي/
- Mon 23 Nov | Mubasher | بورصة مصر تعلن آخر موعد لتلقي أوامر استقرار سعر سهم بنك القاهرة
  https://www.mubasher.info/news/21588951/بورصة-مصر-تعلن-آخر-موعد-لتلقي-أوامر-استقرار-سعر-سهم-بنك-القاهرة
- Mon 23 Nov | بنكي | «فيتش»: طرح بنك القاهرة خطوة مهمة نحو تحقيق مستهدفات مصر للتخارج من الأصول
  https://www.bankygate.com/202150
- Mon 23 Nov | اتحاد بنوك مصر | بنك القاهرة يتصدر ارتفاعات أسهم قطاع البنوك بالبورصة بمستهل التعاملات
  https://febanks.com/1357890/
## EGAL  (1 leads)
- Sun 22 Nov | دار المعارف | طلائع مركز شباب قنا في ضيافة شركة مصر للألومنيوم
  https://daralmaref.com/News/2611455.aspx
  (page: did not load (403))
## EFID  (8 leads)
- Mon 23 Nov | Food Business Middle East & Africa | Edita Food Industries profit jumps 65% in first nine months
  https://www.foodbusinessmea.com/edita-food-industries-profit-jumps-65-in-first-nine-months/
  > Record quarterly sales and higher volumes supported earnings growth, while the Egyptian snack maker continued investing in production capacity and expanding its regional operations. [Figures on the page: nine months; first half; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 23 Nov | جريدة البورصة | الرقابة المالية تعتمد تخفيض رأسمال "إيديتا" 416.7 مليون جنيه
  https://alborsaanews.com/2026/11/23/2008303
  > قالت الهيئة العامة للرقابة المالية، إنها لا مانع لديها على نشر تقرير الإفصاح لشركة إيديتا للصناعات الغذائية، تمهيداً للسير في إجراءات دعوة الجمعية العامة غير العادية للشركة، للنظر في تخفيض رأس المال المصدر من 418.9 إلى 416.7 مليون جنيه. [Figures on the page: unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Mon 23 Nov | عالم المال | الرقابة المالية توافق على نشر إفصاح «إيديتا» بشأن تخفيض رأس المال
  https://alamalmal.net/article/943955/الرقابة-المالية-توافق-على-نشر-إفصاح-«إيديتا»
  > أعلنت الهيئة العامة للرقابة المالية عدم ممانعتها على نشر تقرير إفصاح شركة إيديتا للصناعات الغذائية، بشأن تخفيض رأس المال المصدر والمدفوع بقيمة 2.2 مليون جنيه، ليصل إلى 416.7 مليون جنيه، مقارنة بنحو 418.9 مليون جنيه.
- Mon 23 Nov | موقع الحرية الإخباري | بقيمة 2.2 مليون جنيه.. الرقابة المالية توافق لإيديتا على السير في إجراءات تخفيض رأس المال
  https://alhorianews.com/بقيمة-2-2-مليون-جنيه-الرقابة-المالية-توا/
  > وافقت الهيئة العامة للرقابة المالية على نشر تقرير الإفصاح الخاص بشركة إيديتا للصناعات الغذائية، والمتعلق بالسير في إجراءات تخفيض رأس المال المصدر والمدفوع بقيمة 2.2 مليون جنيه، وذلك عبر إعدام أسهم خزينة مملوكة للشركة. نرشح لك: المركزي يطرح 5 عطاءات لسندات الخزانة بقيمة 46.5 مليار جنيه اليوم تفاصيل تخفيض رأس مال إيديتا وإعدام أسهم الخزينة [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Mon 23 Nov | أموال الغد | «الرقابة المالية» توافق على نشر إفصاح «إيديتا» لتخفيض رأس المال عبر إعدام أسهم خزينة
  https://amwalalghad.com/2026/11/23/الرقابة-المالية-توافق-على-نشر-إفصاح-4/
- Mon 23 Nov | جريدة الاستثمار العربى | «الرقابة المالية» توافق على تخفيض رأس مال «إيديتا» بنحو 2.2 مليون جنيه
  https://estsmararabe.com/الرقابة-المالية-توافق-على-تخفيض-رأس/
- Mon 23 Nov | Pioneers Misr | «إيديتا للصناعات الغذائية»: تخفيض رأس المال إلى 416.71 مليون جنيه بإعدام 11 مليون سهم خزينة
  https://pioneersmisr.com/124219/
- Mon 23 Nov | جريدة المال | الرقابة المالية تقر تخفيض رأسمال إيديتا عبر إعدام 11 مليون سهم خزينة
  https://almalnews.com/2148983/الرقابة-المالية-تقر-تخفيض-رأسمال-إيديتا-عبر/
## AAPL  (8 leads)
- Mon 23 Nov | marketscreener.com | Apple Inc. : Bernstein reiterates its Buy rating
  https://www.marketscreener.com/news/apple-inc-bernstein-reiterates-its-buy-rating-ce7851dada8dfe22
  (page: did not load (403))
- Mon 23 Nov | 24/7 Wall St. | Apple Is Up 29% This Year and Already Above Wall Street’s Target. Our Model Sees $400+
  https://247wallst.com/investing/2026/11/23/apple-is-up-29-this-year-and-already-above-wall-streets-target-our-model-sees-400/
  > Apple Is Up 29% This Year and Already Above Wall Street’s Target. Our Model Sees $400+ Apple (NASDAQ:AAPL | AAPL Price Prediction) has gained 28.64% year to date. At $348.76, it already trades above the $345.63 analyst consensus target. Our 24/7 Wall St. price target for Apple is $403.43 over the next 12 months.
- Mon 23 Nov | Traders Union | Apple stock forecast: Bearish momentum persists as sellers remain in control
  https://tradersunion.com/news/stocks/show/4373992-apple-drops-1-43percent-today-to/
  (page: did not load (403))
## MSFT  (8 leads)
- Mon 23 Nov | TipRanks | Microsoft (MSFT) Expands Quantum Cybersecurity Push with a New AI Team in Israel
  https://www.tipranks.com/news/microsoft-msft-expands-quantum-cybersecurity-push-with-a-new-ai-team-in-israel
  (page: did not load (403))
- Mon 23 Nov | TradingKey | Microsoft Corp Stock (MSFT) Opened Up by 3.39% on Nov 23: A Full Analysis
  https://www.tradingkey.com/news/market-movers/262318268-market-movers-msft-20261123
  > Microsoft Corp Stock (MSFT) Opened Up by 3.39% on Nov 23: A Full Analysis Microsoft Corp (MSFT) opened up by 3.39%. The Software & IT Services sector is up by 3.79%.
- Mon 23 Nov | Traders Union | Microsoft shares technical analysis: Downward price move persists under seller pressure
  https://tradersunion.com/news/stocks/show/4374329-microsoft-drops-2-53percent-to-usd485-68/
  (page: did not load (403))
- Mon 23 Nov | Investing.com | Bernstein reiterates Microsoft stock rating on AI strategy
  https://www.investing.com/news/analyst-ratings/bernstein-reiterates-microsoft-stock-rating-on-ai-strategy-93CH-5045469
  (page: did not load (403))
- Mon 23 Nov | Investing.com India | V2X expands Microsoft partnership for AI mission operations By Investing.com
  https://in.investing.com/news/stock-market-news/v2x-expands-microsoft-partnership-for-ai-mission-operations-93CH-5721009
- Mon 23 Nov | Metaintro | Microsoft Azure Staff Face Pay-for-Performance Shift With Extra Stock for Top Performers
  https://www.metaintro.com/blog/microsoft-azure-pay-for-performance-stock-top-performers
- Mon 23 Nov | Benzinga | Microsoft Unaware Ballroom Donation Meant East Wing Demolition - Microsoft (NASDAQ:MSFT)
  https://www.benzinga.com/markets/tech/26/11/63519782/microsoft-brad-smith-unaware-trump-ballroom-donation-meant-east-wing-demolition
- Mon 23 Nov | Trefis | Is Microsoft Stock Stronger Than It Looks?
  https://www.trefis.com/stock/msft/articles/627857/is-microsoft-stock-stronger-than-it-looks/2026-11-23
## NVDA  (8 leads)
- Mon 23 Nov | WMAR 2 News Baltimore | US stocks soar and recover much of last week's brutal loss after Jensen Huang returns to Nvidia
  https://www.wmar2news.com/us-news/us-stocks-soar-and-recover-much-of-last-weeks-brutal-loss-after-jensen-huang-returns-to-nvidia
  > A surprise return for Jensen Huang, the charismatic backer of the entire artificial intelligence industry, to Nvidia as its CEO is launching the U.S. stock market higher on Monday. It’s recovering much of its brutal loss from last week, which was one of its worst since the 2008 financial crisis.
- Mon 23 Nov | BankInfoSecurity | Nvidia reinstates Jensen Huang as CEO. Stock skyrockets 31%
  https://www.bankinfosecurity.com/nvidia-reinstates-jensen-huang-as-ceo-stock-skyrockets-31-a-33490
  (page: did not load (403))
- Mon 23 Nov | Fortune | Jensen Huang is back as Nvidia CEO, but now must grapple with a wave of investigations
  https://fortune.com/2026/11/23/nvidia-stock-jensen-huang-return-ceo-investigations-china-spy-scandal-fbi/
  > A week and a half after being forced out as Nvidia CEO, Jensen Huang has returned to the AI chip giant he founded, ensuring he remains the face of the company amid a wave of investigations.
- Mon 23 Nov | Benzinga | Donald Trump Gets His Nvidia Wish as Company Brings Back Jensen Huang: ‘Great Patriot and National Treasu
  https://www.benzinga.com/news/politics/26/11/63532073/donald-trump-gets-his-nvidia-wish-as-company-brings-back-jensen-huang-great-patriot-and-national-treasure
  (page: did not load (403))
- Mon 23 Nov | Yahoo Finance | Nvidia reinstates Jensen Huang as CEO, stock rockets
  https://finance.yahoo.com/technology/article/nvidia-reinstates-jensen-huang-as-ceo-stock-rockets-141145439.html
- Mon 23 Nov | TheWrap | Nvidia Stock Surges Over 27% on Jensen Huang’s Reinstatement as CEO
  https://www.thewrap.com/industry-news/business/nvidia-jensen-huang-return-stock-reaction/
- Mon 23 Nov | Business Insider | AI stocks roar back from brutal rout after Jensen Huang is reinstated as Nvidia CEO
  https://www.businessinsider.com/ai-stock-rally-jensen-huang-nvidia-reinstated-ceo-2026-11
- Mon 23 Nov | 24/7 Wall St. | Nvidia Lost $901 Billion Last Week. It Won Back All of It Before the Opening Bell
  https://247wallst.com/investing/2026/11/23/nvidia-lost-901-billion-last-week-it-won-back-all-of-it-before-the-opening-bell/
## AMZN  (8 leads)
- Mon 23 Nov | 24/7 Wall St. | Billionaire Seth Klarman Has 18% of His $5 Billion Stock Portfolio in Amazon
  https://247wallst.com/investing/2026/11/23/billionaire-seth-klarman-has-18-of-his-5-billion-stock-portfolio-in-amazon/
  > Billionaire Seth Klarman Has 18% of His $5 Billion Stock Portfolio in Amazon This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 23 Nov | Quiver Quantitative | Amazon Rises as Tech Rebound and AI-Related Optimism Lift Shares
  https://www.quiverquant.com/news/Amazon+Rises+as+Tech+Rebound+and+AI-Related+Optimism+Lift+Shares
  > Amazon.com (AMZN) is up 5.4% today. Here is some analysis on what might have caused this price movement. Amazon also seems to be benefiting from renewed enthusiasm around its AI positioning, including strong recent AWS growth and fresh attention on the value of its Anthropic stake after a weekend analyst target increase.
- Mon 23 Nov | Yahoo Finance | Amazon deal to outlast MTN's bid for telecoms operator Telkom
  https://finance.yahoo.com/technology/articles/amazon-deal-outlast-mtns-bid-134102117.html
  > South African telecoms operator Telkom's new agreement to distribute Amazon's satellite broadband would survive a takeover by MTN, its senior executive told Semafor. This would give Africa's largest mobile operator a foothold in Amazon's challenge to Starlink if its renewed bid for Telkom succeeds.
- Mon 23 Nov | Benzinga | Verizon, Amazon And A Major Retailer On CNBC’s 'Final Trades'
  https://www.benzinga.com/trading-ideas/long-ideas/26/11/63522772/verizon-amazon-and-a-major-retailer-on-cnbcs-final-trades
  (page: did not load (403))
- Mon 23 Nov | Happy Gamer | Saros on PS5 Drops to $29.97 at Amazon, Walmart Has Local Stock
  https://happygamer.com/saros-ps5-price-drop-amazon-29-97-179555/
- Mon 23 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: StrongBox Wealth LLC Grows Position
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-strongbox-wealth-llc-grows-position-2026-11-23/
- Mon 23 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock Acquired by Smallwood Wealth Investment Management LLC
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-acquired-by-smallwood-wealth-investment-management-llc-2026-11-23/
- Mon 23 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock Acquired by Pathway Financial Advisers LLC
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-acquired-by-pathway-financial-advisers-llc-2026-11-23/
## GOOGL  (8 leads)
- Mon 23 Nov | TradingKey | Alphabet Inc Class C Stock (GOOG) Opened Up by 4.22% on Nov 23: What Investors Need To Know
  https://www.tradingkey.com/news/market-movers/262318269-market-movers-goog-20261123
  > Alphabet Inc Class C Stock (GOOG) Opened Up by 4.22% on Nov 23: What Investors Need To Know Alphabet Inc Class C (GOOG) opened up by 4.22%. The Software & IT Services sector is up by 3.79%.
- Mon 23 Nov | TradingKey | Alphabet Inc Class A Stock (GOOGL) Opened Up by 4.63% on Nov 23: Drivers Behind the Movement
  https://www.tradingkey.com/news/market-movers/262318267-market-movers-googl-20261123
  > Alphabet Inc Class A Stock (GOOGL) Opened Up by 4.63% on Nov 23: Drivers Behind the Movement Alphabet Inc Class A (GOOGL) opened up by 4.63%. The Software & IT Services sector is up by 3.79%.
- Mon 23 Nov | Traders Union | Alphabet stock price prediction: Seller pressure remains as downside risk persists
  https://tradersunion.com/news/stocks/show/4375613-alphabet-slides-1-16percent-to-usd269-5/
  (page: did not load (403))
- Mon 23 Nov | Blockonomi | Alphabet (GOOGL) Stock Near 52-Week Low as Jim Cramer Sees a Buying Opportunity
  https://blockonomi.com/alphabet-googl-stock-near-52-week-low-as-jim-cramer-sees-a-buying-opportunity/
  > - Jim Cramer said Nov. 19 that Alphabet looks ready to rebound, citing chartist Larry Williams. - Alphabet trades near 15 times 2026 earnings, versus a five-year range of 20 to 30 times. - The stock fell nearly 13% on Oct. 29, its worst day on record. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 23 Nov | Pluang | Alphabet shares plunge over 30% amid earnings m...
  https://pluang.com/en/news-feed/apa-masalah-saham-alphabet-penurunan-laba-kekhawatiran-ai-2
- Mon 23 Nov | The Globe and Mail | What's Wrong With Alphabet Stock?
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8963658/whats-wrong-with-alphabet-stock/
- Mon 23 Nov | Investing.com | Truist reiterates Alphabet stock rating on AI monetization view
  https://www.investing.com/news/analyst-ratings/truist-reiterates-alphabet-stock-rating-on-ai-monetization-view-93CH-5045314
- Mon 23 Nov | Simply Wall St | Alphabet (GOOGL) Stock Trades Below Fair Value Despite AI Chip Expansion
  https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-stock-trades-below-fair-value-despite-ai-chip
## META  (8 leads)
- Mon 23 Nov | Traders Union | Meta Platforms faces rising AI costs and profitability doubts: Can META avoid further losses?
  https://tradersunion.com/news/stocks/show/4375466-meta-platforms-drops-5-27percent-to/
  (page: did not load (403))
- Mon 23 Nov | Kalkine | Is AI Breaking the 2030 Net Zero Promise of Meta Platforms (NASDAQ:META) as Emissions Rose 45%?
  https://kalkine.com.au/news/technology/is-ai-breaking-the-2030-net-zero-promise-of-meta-platforms-nasdaqmeta-as-emissions-rose-45
  (page: did not load (403))
- Mon 23 Nov | The Globe and Mail | Zacks Investment Ideas feature highlights: Anthropic, SpaceX and Meta Platforms
  https://www.theglobeandmail.com/investing/markets/stocks/SPCX/pressreleases/8965659/zacks-investment-ideas-feature-highlights-anthropic-spacex-and-meta-platforms/
  > Zacks Investment Ideas feature highlights: Anthropic, SpaceX and Meta Platforms Chicago, IL – November 23, 2026– Today, Zacks Investment Ideas feature highlights Anthropic ANT, SpaceX SPCX and Meta Platforms META. Lessons from 2 High-Profile IPOs: ANT & SPCX
- Mon 23 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Stock Price Target Lowered at Morgan Stanley
  https://www.marketbeat.com/instant-alerts/analyst-meta-platforms-nasdaq-meta-stock-price-target-lowered-at-morgan-stanley-2026-11-23/
  > Meta Platforms (NASDAQ:META) Stock Price Target Lowered at Morgan Stanley - Morgan Stanley lowered its Meta price target from $820 to $720 but kept an “overweight” rating; the new target implies 28.31% upside from the stock’s current price.
- Mon 23 Nov | Rolling Out | Meta’s free cash flow fell to $28.6B: Why it matters
  https://rollingout.com/2026/11/23/why-meta-stock-fell-3-reasons/
- Mon 23 Nov | ad-hoc-news.de | Meta Platforms stock: Loop Capital cuts price target to $890
  https://www.ad-hoc-news.de/boerse/news/corporate-news/meta-platforms-stock-loop-capital-cuts-price-target-to-890/70546635
- Mon 23 Nov | Demokratis.co.id | Meta Shares Drop 5.9% as AI Spending Weighs on Tech Stocks
  https://demokratis.co.id/en/meta-shares-ai-spending-selloff
- Mon 23 Nov | Limapagi | Meta Shares Fall 5.9% as AI Spending Concerns Hit Tech Stocks
  https://www.limapagi.id/en/meta-stock-slide-ai-spending
## TSLA  (8 leads)
- Mon 23 Nov | TIKR.com | Tesla Bulls Banking on SpaceX “Don’t Get the Dilution Math,” Says Gary Black. Tesla Trades at 3.4x SpaceX’s 2027 Multiple
  https://www.tikr.com/blog/tesla-bulls-banking-on-spacex-dont-get-the-dilution-math-says-gary-black-tesla-trades-at-3-4x-spacexs-2027-multiple?ref=yahoofinance&tlnk=yf-261123-mfw83vf8
  > - Gary Black puts Tesla’s 2027 P/E at 168x and SpaceX’s at 30.6x, and he expects a binding merger agreement before year end. - With SpaceX as the buyer in a stock-for-stock deal, Tesla holders would swap a high-multiple stock for SpaceX shares priced much lower on earnings.
- Mon 23 Nov | ad-hoc-news.de | Tesla stock: JPMorgan keeps Neutral rating, USD 430 target
  https://www.ad-hoc-news.de/boerse/news/corporate-news/tesla-stock-jpmorgan-keeps-neutral-rating-usd-430-target/70546772
  > On Monday, November 23, 2026, JPMorgan analyst Rajat Gupta confirmed the bank's Neutral recommendation for Tesla and kept its USD 430 price target unchanged, according to MarketScreener, which carried the item with dpa-AFX Analyser.
- Mon 23 Nov | Barron's | SpaceX Stock Rebounds as Musk Starlink Talk Fuels Hopes of a Tesla Merger
  https://www.barrons.com/articles/spacex-stock-musk-starlink-tesla-merger-4fa1b482
  (page: did not load (401))
- Mon 23 Nov | TIKR.com | Musk Says Teslas Will Tap “Grok’s Real-Time X Feed.” Another Tie Between Tesla and SpaceX
  https://www.tikr.com/blog/musk-says-teslas-will-tap-groks-real-time-x-feed-another-tie-between-tesla-and-spacex?
  > - Elon Musk says Tesla’s cars will combine shared traffic data with Grok’s real-time X feed, a product SpaceX owns. - Uber and Lyft would have a hard time matching it, since their robotaxis come from partners like Avride and Waymo.
- Mon 23 Nov | Yahoo Finance | Tesla's autonomy ambitions just got a Wall Street vote of confidence
  https://finance.yahoo.com/markets/stocks/article/teslas-autonomy-ambitions-just-got-a-wall-street-vote-of-confidence-130035595.html
- Mon 23 Nov | Investor's Business Daily | Tesla FSD V15 Rolling Out, Goes 'Wide' Next Month. Elon Musk Says It's 'Something Special.'
  https://www.investors.com/news/tesla-fsd-v15-coming-next-month-elon-musk-says-something-special/
- Mon 23 Nov | TipRanks | Cathie Wood Says TSLA Holders ‘Will Get’ a Premium If SpaceX Buys Tesla — HSBC Sees 33% Bump
  https://www.tipranks.com/news/cathie-wood-says-tsla-holders-will-get-a-premium-if-spacex-buys-tesla-hsbc-sees-33-bump
- Mon 23 Nov | Barron's | Why Is Tesla Stock Rising Today? FSD Version 15 and a Tech Bounce.
  https://www.barrons.com/articles/tesla-stock-price-fsd-version-15-full-self-driving-d6a8e538
## JPM  (8 leads)
- Mon 23 Nov | TradingView | REG - JPMorgan Asset Mngt SEGRO PLC - Form 8.3-SEGRO plc
  https://www.tradingview.com/news/reuters.com,2026-11-23:newsml_RSW3157Ea:0-reg-jpmorgan-asset-mngt-segro-plc-form-8-3-segro-plc/
  > REG - JPMorgan Asset Mngt SEGRO PLC - Form 8.3-SEGRO plc PUBLIC OPENING POSITION DISCLOSURE/DEALING DISCLOSURE BY A PERSON WITH INTERESTS IN RELEVANT SECURITIES REPRESENTING 1% OR Rule 8.3 of the Takeover Code (the "Code") | (a) Full name of discloser: | JPMorgan Asset Management |
- Mon 23 Nov | MarketBeat | Casey's General Stores (NASDAQ:CASY) Given New $709.00 Price Target at JPMorgan Chase & Co.
  https://www.marketbeat.com/instant-alerts/analyst-caseys-general-stores-nasdaq-casy-given-new-70900-price-target-at-jpmorgan-chase-co-2026-11-23/
  > Casey's General Stores (NASDAQ:CASY) Given New $709.00 Price Target at JPMorgan Chase & Co. - JPMorgan raised its price target on Casey’s General Stores from $687 to $709, while maintaining a neutral rating; the new target implies 2.58% upside from the prior close.
- Mon 23 Nov | StreetInsider | Form 424B2 JPMORGAN CHASE & CO
  https://www.streetinsider.com/SEC+Filings/Form+424B2+JPMORGAN+CHASE+&amp;+CO/27385322.html
  (page: did not load (403))
- Mon 23 Nov | StreetInsider | Form FWP JPMorgan Chase Financial Filed by: JPMorgan Chase Financial Co. LLC
  https://www.streetinsider.com/SEC+Filings/Form+FWP+JPMorgan+Chase+Financial+Filed+by:+JPMorgan+Chase+Financial+Co.+LLC/27385147.html
  (page: did not load (403))
- Mon 23 Nov | MEXC | JPMorgan Chase Tests Key $310 Support After Multi-Week Pullback (NYSE:JPM)
  https://www.mexc.com/crypto-pulse/article/jpmorgan-chase-tests-key-310-support-after-multi-week-pullback-nyse-193180
- Mon 23 Nov | ad-hoc-news.de | Tesla stock: JPMorgan keeps Neutral rating, USD 430 target
  https://www.ad-hoc-news.de/boerse/news/corporate-news/tesla-stock-jpmorgan-keeps-neutral-rating-usd-430-target/70546772
- Mon 23 Nov | Yahoo Finance | Investors Heavily Search JPMorgan Chase & Co. (JPM): Here is What You Need to Know
  https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-jpmorgan-chase-130004248.html
- Mon 23 Nov | Investing.com India | JPMorgan reiterates Take-Two stock Overweight on GTA VI launch By Investing.com
  https://in.investing.com/news/stock-market-news/jpmorgan-reiterates-taketwo-stock-overweight-on-gta-vi-launch-93CH-5720783
## XOM  (8 leads)
- Mon 23 Nov | Investing.com | ExxonMobil completes $1.76 billion debt tender offer
  https://www.investing.com/news/company-news/exxonmobil-completes-176-billion-debt-tender-offer-93CH-5045799
  (page: did not load (403))
- Mon 23 Nov | TradingView | ExxonMobil Announces Terms and Results of Tender Offers for Four Note Issues
  https://www.tradingview.com/news/reuters.com,2026:newsml_TUA7KTJZH:0-exxonmobil-announces-terms-and-results-of-tender-offers-for-four-note-issues/
  (page: only 29 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | ExxonMobil | Announcing Pioneer and Exxon notes tender offer results
  https://corporate.exxonmobil.com/news/news-releases/2026/1123-exxonmobil-announces-pricing-terms-expiration-and-results-of-cash-tender-offers
  (page: did not load (403))
## AVGO  (8 leads)
- Mon 23 Nov | Seeking Alpha | Broadcom: Buy When Others Are Fearful (Earnings Preview) (NASDAQ:AVGO)
  https://seekingalpha.com/article/4971075-broadcom-buy-when-others-are-fearful-earnings-preview?source=generic_rss
  > remains a Buy after a decline exceeding 20% since my August update, as I see sustained AI demand and an attractive forward valuation. - AVGO's fiscal Q3 total revenue reached $29.59 billion, while adjusted EPS rose 96%; management guided for $34.8 billion in Q4 revenue.
- Mon 23 Nov | marketscreener.com | Broadcom Inc. : Bernstein keeps its Buy rating
  https://www.marketscreener.com/news/broadcom-inc-bernstein-keeps-its-buy-rating-ce7851dada8fff24
  (page: did not load (403))
- Mon 23 Nov | ad-hoc-news.de | Broadcom's $115 Billion AI Bet Rests on Customers Still Hunting for Cash
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/broadcom-s-115-billion-ai-bet-rests-on-customers-still-hunting-for-cash/70546792
  > Broadcom's ambitious AI revenue target is running into a less glamorous question: whether the customers behind those orders can actually foot the bill. That tension moved into sharper focus after a supply-chain report suggested Google may trim its 2027 chip purchases, a claim neither Google nor Broadcom has confirmed.
- Mon 23 Nov | Yahoo Finance | Nvidia, Broadcom, and AMD roar higher as chip stocks rebound from worst week since 2001
  https://finance.yahoo.com/markets/article/nvidia-broadcom-and-amd-roar-higher-as-chips-rebound-from-worst-week-since-2001-133109931.html
  > Chip giant Nvidia (NVDA) roared 30% on Monday after the board of the AI chip giant reinstated Jensen Huang as CEO in a stunning turn of events. "The Board of Directors voted unanimously to reinstate Mr. Shares of peers AMD (AMD) and Broadcom (AVGO) also bounced 4% after tanking by double-digit percentages last week.
- Mon 23 Nov | Yahoo Finance | Not Good: Broadcom Loses $200 Billion as Chips Crash and Google Reportedly Cuts AI Chip Plans
  https://finance.yahoo.com/technology/ai/articles/not-good-broadcom-loses-200-132528950.html
- Mon 23 Nov | MarketBeat | Broadcom Inc. $AVGO Stock Purchased by Mosaic Family Wealth Partners LLC
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-purchased-by-mosaic-family-wealth-partners-llc-2026-11-23/
- Mon 23 Nov | Investing.com | Lynx Equity sees Broadcom stock sentiment improving despite concerns
  https://www.investing.com/news/analyst-ratings/lynx-equity-sees-broadcom-stock-sentiment-improving-despite-concerns-93CH-5044981
- Mon 23 Nov | Finbold | How much will 100 AVGO shares earn from Broadcom’s last dividend of 2026?
  https://finbold.com/how-much-will-100-avgo-shares-earn-from-broadcoms-last-dividend-of-2026/
## BRK.B  (8 leads)
- Mon 23 Nov | Seeking Alpha | Berkshire Hathaway: Slightly Too Expensive To Be Worth It (Rating Downgrade) (NYSE:BRK.A)
  https://seekingalpha.com/article/4971074-berkshire-hathaway-slightly-too-expensive-to-be-worth-it?source=generic_rss
  (page: did not load (403))
- Mon 23 Nov | The Motley Fool | Berkshire Hathaway Owns 22.6% of American Express. Is the Stock a Buy, Sell, or Hold After a 17% Drop in 2026?
  https://www.fool.com/investing/2026/11/23/berkshire-hathaway-owns-22-6-of-american-express-is-the-stock-a-buy-sell-or-hold-after-a-17-drop-in-2026/
  > By James Brumley – - After big gains in 2024 and 2025, American Express’s stock has been stopped cold this year. It may be one of Berkshire Hathaway's (BRKA +0.27%) (BRKB +0.08%) largest and longest-held holdings.
- Mon 23 Nov | Kalkine | Is 41.6% of Berkshire Hathaway's (NYSE:BRK.B) Roughly USD 358 Billion Holdings Tied to AI Through Apple, Coca-Cola and Alphabet?
  https://kalkine.com.au/news/financial/is-416-of-berkshire-hathaways-nysebrkb-roughly-usd-358-billion-holdings-tied-to-ai-through-apple-coca-cola-and-alphabet
  (page: did not load (403))
## WMT  (8 leads)
- Mon 23 Nov | Investing.com Canada | Symbotic faces earnings test as Walmart backlog looms large By Investing.com
  https://ca.investing.com/news/stock-market-news/symbotic-faces-earnings-test-as-walmart-backlog-looms-large-93CH-4976214
  (page: did not load (403))
- Mon 23 Nov | The Globe and Mail | Should You Buy Walmart Stock Now or Wait for a Dip?
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA-Q/pressreleases/8965829/should-you-buy-walmart-stock-now-or-wait-for-a-dip/
  > - Walmart recently released its third-quarter results, which were better than expected. - The company also raised its guidance, expecting its growth rate for the fiscal year to be around 5%. - The stock trades at more than 46 times earnings, which is a significant premium for a business that's growing in single digits.
- Mon 23 Nov | Traders Union | Walmart shares weekly forecast: Seven-day volatility stays moderate with trend signals firm
  https://tradersunion.com/news/stocks/show/4375301-walmart-slips-0-06percent-this-week/
  (page: did not load (403))
## V  (8 leads)
- Mon 23 Nov | TradingView | Klarna stock rises as Visa partnership expands checkout reach
  https://www.tradingview.com/news/seekingalpha:3ed62df6e094b:0-klarna-stock-rises-as-visa-partnership-expands-checkout-reach/
  > Klarna stock rises as Visa partnership expands checkout reach Less than 1 min read - Klarna announced on Monday an expanded partnership with Visa , allowing merchants using the Visa Acceptance Platform to offer Klarna at checkout in the U.S., Canada, the U.K., and Europe.
- Mon 23 Nov | FinancialContent | Klarna Expands Collaboration With Visa, Bringing Flexible Payments to Merchants Using Visa Acceptance Platform
  https://markets.financialcontent.com/wral/article/bizwire-2026-11-23-klarna-expands-collaboration-with-visa-bringing-flexible-payments-to-merchants-using-visa-acceptance-platform
  > Klarna, the everyday finance network, has expanded its partnership with Visa, a world leader in digital payments, giving the merchants using Visa Acceptance Platform access to Klarna’s latest features. Merchants using Visa Acceptance Platform can now offer Klarna at checkout through their existing setup in the U.S., Canada, the U.K.
- Mon 23 Nov | ad-hoc-news.de | Visa stock: President Capital trims price target to USD 468
  https://www.ad-hoc-news.de/boerse/news/corporate-news/visa-stock-president-capital-trims-price-target-to-usd-468/70546759
  > President Capital lowered its price target for Visa from USD 474 to USD 468, according to a report published by MarketScreener on Monday, November 23, 2026. The report was carried by MT Newswires and identifies President Capital as the source of the adjustment. Fresh valuation signal for Visa
## ORCL  (8 leads)
- Mon 23 Nov | Stock Titan | Oracle gave Arrow two distributor awards and finalist honors in three more categories.
  https://www.stocktitan.net/news/ARW/arrow-electronics-recognized-as-2026-oracle-global-cloud-distributor-69qy76wmmfpv.html
  > Arrow Electronics recognized as 2026 Oracle Global Cloud Distributor and EMEA Growth Accelerator Distributor of the Year Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Mon 23 Nov | Traders Union | Oracle stock rises as oversold Stoch RSI signals potential upside
  https://tradersunion.com/news/stocks/show/4376156-oracle-jumps-12-62percent-after-ai/
  (page: did not load (403))
- Mon 23 Nov | FinanceFeeds | ORCL Stock: Oracle Says Its $300 Billion OpenAI Contract Is Fully Funded After a 19% Weekly Drop
  https://financefeeds.com/orcl-stock-openai-contract-fully-funded/
  > ORCL stock opened 14.87% higher at $116.24 at 9:30 a.m. ET on 23 November, according to TradingView, in the first session after Oracle said its OpenAI contract is fully funded.
- Mon 23 Nov | Yahoo Finance | Oracle Or The Fed: What Really Moves Nvidia Stock?
  https://finance.yahoo.com/markets/stocks/articles/oracle-fed-really-moves-nvidia-140003418.html
  > Today's big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Two kinds of news seem to move Nvidia stock. One is what Oracle says about its AI spending. We checked which one has mattered more since September 1. How much of Nvidia's daily swings each one explains, since September 1:
- Mon 23 Nov | ad-hoc-news.de | Oracle stock: OpenAI infrastructure deal fully funded
  https://www.ad-hoc-news.de/boerse/news/corporate-news/oracle-stock-openai-infrastructure-deal-fully-funded/70546807
- Mon 23 Nov | MarketBeat | Oracle Corporation $ORCL Stock Holdings Boosted by Pursue Wealth Partners LLC
  https://www.marketbeat.com/instant-alerts/filing-oracle-corporation-orcl-stock-holdings-boosted-by-pursue-wealth-partners-llc-2026-11-23/
- Mon 23 Nov | TIKR.com | Oracle’s “Big Permitting Win” Proves the Data Center Backlash Hasn’t Won Yet
  https://www.tikr.com/blog/oracles-big-permitting-win-proves-the-data-center-backlash-hasnt-won-yet?ref=yahoofinance&tlnk=yf-261123-4gcqcwvr
- Mon 23 Nov | MarketBeat | Oracle Corporation $ORCL Stock: Lifeworks Advisors LLC Raises Holdings
  https://www.marketbeat.com/instant-alerts/filing-oracle-corporation-orcl-stock-lifeworks-advisors-llc-raises-holdings-2026-11-23/
## COST  (8 leads)
- Mon 23 Nov | AOL.com | Will Costco Do a Stock Split Before the End of 2026?
  https://www.aol.com/articles/costco-stock-split-end-2026-145002000.html
  > - Alphabet's stock recently hit a new all-time high of more than $1,100. - The last time the company did a stock split was in 2000. Costco Wholesale (NASDAQ:COST) stock recently hit a new all-time high.
- Mon 23 Nov | Simply Wall St | Is Record $30 Dividend Altering The Investment Case For Costco (COST)?
  https://simplywall.st/stocks/us/consumer-retailing/nasdaq-cost/costco-wholesale/news/is-record-30-dividend-altering-the-investment-case-for-costc
  > Costco Wholesale declared a special cash dividend of $30 per share, totaling about $13.3b, alongside a new $4b share repurchase authorization and an update that the prior buyback program has been completed.
- Mon 23 Nov | Invezz | Michael Burry flags Apple, Costco and Walmart as market's 'generals' amid AI selloff
  https://invezz.com/ca/news/2026/11/23/michael-burry-flags-apple-these-two-names-as-markets-generals-amid-ai-selloff/
  > Michael Burry flags Apple, these two names as market's 'generals' amid AI selloff Buy AAPL as the “general” that holds up while AI/semis unwind. It fell far less than Nasdaq 100 last week, and its ecosystem + cash cushion should keep demand steadier than high-beta tech during the early phase of a downturn.
## NFLX  (8 leads)
- Mon 23 Nov | Peradaban.id | Netflix Shares Hit Yearly Low as Burry Eyes 38 Dollars
  https://peradaban.id/en/netflix-shares-burry-buying-price
  > Netflix Shares Hit Yearly Low as Burry Eyes 38 Dollars Netflix shares extended their decline to a one-year closing low of $56.73 on November 20, 2026, as investors assessed slowing revenue growth, advertising challenges, and upcoming financial guidance.
- Mon 23 Nov | Invezz | Netflix stock slides as a risky chart pattern signals further downside risk
  https://invezz.com/news/2026/11/23/netflix-stock-slides-as-a-risky-chart-pattern-signals-further-downside-risk/
  > Netflix stock slides as a risky chart pattern signals further downside risk Buy put spread on Netflix (e.g., NFLX 50-strike puts vs higher strike puts). This directly monetizes the “next level” call ($50) while limiting premium burn if NFLX bounces to retest ~$64 resistance.
- Mon 23 Nov | Foreign Policy Journal | Wall Street Sees 49% Upside In Netflix (NASDAQ: NFLX) Even As Analysts Trim Disney (NYSE: DIS) On Valuation
  https://www.foreignpolicyjournal.com/2026/11/23/wall-street-sees-49-upside-in-netflix-nasdaq-nflx-even-as-analysts-trim-disney-nyse-dis-on-valuation/
  > Analyst price targets tell a striking story about two of streaming’s biggest names, with Netflix commanding far greater implied upside despite a punishing year-to-date selloff. According to Koyfin data, the 12-month consensus price target on Netflix (NASDAQ: NFLX) sits at $84.55, representing roughly 49% upside from where shares closed Friday at $56.73.
- Mon 23 Nov | Seeking Alpha | Netflix: Still Bullish At 15 Times Earnings As The Cash Flow Keeps Compounding
  https://seekingalpha.com/article/4971048-netflix-still-bullish-at-15-times-earnings-as-the-cash-flow-keeps-compounding
  (page: did not load (403))
- Mon 23 Nov | GuruFocus | ETFs Are Net Sellers of Netflix (NFLX) on Nov. 19
  https://www.gurufocus.com/news/9214519/etfs-are-net-sellers-of-netflix-nflx-on-nov-19
- Mon 23 Nov | ad-hoc-news.de | Netflix stock: Evercore keeps Outperform rating at $90 target
  https://www.ad-hoc-news.de/boerse/news/corporate-news/netflix-stock-evercore-keeps-outperform-rating-at-90-target/70546694
- Mon 23 Nov | TradingPedia | Analyst Backing and Market Rally Lift Netflix Shares
  https://www.tradingpedia.com/2026/11/23/analyst-backing-and-market-rally-lift-netflix-shares/
- Mon 23 Nov | Investing.com India | Why is Netflix stock gaining today? By Investing.com
  https://in.investing.com/news/stock-market-news/why-is-netflix-stock-gaining-today-93CH-5720992
## INTC  (8 leads)
- Mon 23 Nov | TheStreet | Intel landed Microsoft, but now it needs something it can’t make
  https://www.thestreet.com/technology/intel-microsoft-emib-deal-ajinomoto-bottleneck
  (page: did not load (403))
- Mon 23 Nov | Yahoo Finance | NVIDIA Jumps 28% as Chip Stocks Rebound From Last Week’s AI Sell-Off; Intel Rallies 13%, AMD Gains 7%
  https://finance.yahoo.com/markets/stocks/articles/nvidia-jumps-28-chip-stocks-141339800.html
  > - NVIDIA surges 9% and Intel climbs 6% as chip stocks rebound, yet NVIDIA remains the only one of the three still down for the year. - AMD's 107% and Intel's 47% year-to-date gains mean both are recovering from dips, while NVIDIA climbs out of a 27% hole.
- Mon 23 Nov | 24/7 Wall St. | NVIDIA Jumps 28% as Jensen Huang Reportedly Reinstated as CEO; Intel Rallies 13%, AMD Gains 7%
  https://247wallst.com/investing/2026/11/23/nvidia-jumps-28-as-chip-stocks-rebound-from-last-weeks-ai-sell-off-intel-rallies-13-amd-gains-7/
  (same wording as the Yahoo Finance story above: one source, not two)
- Mon 23 Nov | marketscreener.com | Intel Corporation : Bernstein is Neutral
  https://www.marketscreener.com/news/intel-corporation-bernstein-is-neutral-ce7851dada8cf020
  (page: did not load (403))
- Mon 23 Nov | Investing.com Australia | Why is Intel stock surging today? By Investing.com
  https://au.investing.com/news/stock-market-news/why-is-intel-stock-surging-today-93CH-4790197
- Mon 23 Nov | 24/7 Wall St. | Intel Stock Could Have More Upside Than Its Current Valuation Suggests
  https://247wallst.com/investing/2026/11/23/intel-stock-could-have-more-upside-than-its-current-valuation-suggests/
- Mon 23 Nov | Intellectia AI | Intel Secures First External Customer for 18A Process, Boosting Foundry Prospects
  https://intellectia.ai/news/stock/intel-secures-first-external-customer-for-18a-process-boosting-foundry-prospects
- Mon 23 Nov | Investing.com | Why is Intel stock surging today?
  https://www.investing.com/news/stock-market-news/why-is-intel-stock-surging-today-93CH-5045296
## LLY  (8 leads)
- Mon 23 Nov | Eli Lilly | Lilly to host Innovation Day 2026
  https://investor.lilly.com/news-releases/news-release-details/lilly-host-innovation-day-2026
  (page: did not load (403))
- Mon 23 Nov | GenomeWeb | Lilly Scoops Up LoQus23 for $725M in Huntington’s Disease Push
  https://www.genomeweb.com/business-news/financial/mergers-acquisitions/gnw-lilly-buys-loqus23-huntingtons-disease-20261123/
  (page: did not load (403))
- Mon 23 Nov | BioSpace | Lilly’s 15th M&A deal of 2026 brings LoQus23’s Huntington’s work in house for $725M
  https://www.biospace.com/business/lillys-15th-m-a-deal-of-2026-brings-loqus23s-huntingtons-work-in-house-for-725m
  > LoQus23 Therapeutics is a good match for Eli Lilly’s professed goal of finding biotechs that provide small, early, risky bets.
Read 73 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ALCN, EFIH, EMFD, AMOC, SKPC.
