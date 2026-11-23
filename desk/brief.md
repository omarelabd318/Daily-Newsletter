# Desk brief, Monday, November 23, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 293s. GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-20 (35.89); Treasury yields to 2026-11-20 (10-year 4.92%).
- **valuation**: ok in 20s (GitHub Actions). LLY: $1.27tn, P/E (last 12 months) 42.2, Forecast P/E (fiscal 2026) 37.8 (the four quarters to Sep 2026)
- **movers**: ok in 9s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 234s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 41.1
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.4%, median P/E 9.6; cheapest MASR +78%, PHAR +52%, MFPC +44%; dearest ARAB -62%, MOIN -64%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). 2026-11-11-jufo-results: open -> wrong  (Juhayna closed at 21.77 on November 22, below the 22 that makes the call wrong.)
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 104s (GitHub Actions). 
- **leads**: ok in 74s (GitHub Actions). 
- **sources**: api.nasdaq.com: 42 failed, 0 needed a retry (fetch_intraday.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py).

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
- None: every one has a reason or is under 5%.

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-22 (TradingView's closes; Mubasher's list refused), 207 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (211)
US: 2026-11-20, 807 companies
US week and month: US companies worth $10bn or more (805)
EGX30 heatmap: 2026-11-22, 31 members
US heatmap: 2026-11-20, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-22
## INEG +63.9%  Integrated Engineering Group
- no headlines found
## CPME +3.6%  Catalyst Partners Middle East
- no headlines found
## CSAG +0.4%  Canal Shipping Agencies
- no headlines found
## PHTV +0.2%  Pyramisa Hotels
- no headlines found
## MOIL +0.0%  Maridive & Oil Services
- no headlines found
## CRST -19.9%  Creast mark For Contracting
- no headlines found
## AMII -12.4%  Arabian Metal Industries and Industrial Investments
- no headlines found
## GSSC -11.8%  General Silos & Storage
- no headlines found
## AALR -11.7%  General Co. for Land Reclamation Development & Reconstruction
- no headlines found
## GTWL -10.5%  Goldentex
- no headlines found

# US 2026-11-20
## GPN +9.9%  Global Payments
- Sun 22 Nov | Yahoo Finance Australia | Global Payments Inc. (GPN) Stock forecasts
  https://au.finance.yahoo.com/research/reports/MS_0P000002G8_AnalystReport_1795207236000
- Sat 21 Nov | Yahoo Finance | Global Payments (GPN) Gets a Potential Lifeline as New Takeover Buzz Heats Up
  https://finance.yahoo.com/markets/stocks/articles/global-payments-gpn-gets-potential-065105957.html
- Sat 21 Nov | Yahoo! Finance Canada | Global Payments Inc. (GPN) Stock Forecasts
  https://ca.finance.yahoo.com/research/reports/MS_0P000002G8_AnalystReport_1795207236000
- Sat 21 Nov | Crain's Chicago Business | GTCR weighs $50 billion Global Payments buyout
  https://www.chicagobusiness.com/banking-finance/ccb-gtcr-global-payments-buyout-20261120/
## BIP +4.5%  Brookfield Infrastructure Partners L.P
- Mon 23 Nov | Yahoo! Finance Canada | Brookfield Asset Management Ltd. (BAM.TO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BAM.TO/
- Mon 23 Nov | Yahoo Finance | Brookfield Infrastructure (BIPC) is Back on Investors’ Radar Ahead of This Key Event
  https://finance.yahoo.com/markets/stocks/articles/brookfield-infrastructure-bipc-back-investors-043222176.html
- Sun 22 Nov | CoinGecko | RBIP to MYR: Brookfield Infrastructure Partners L.P. Tokenized Stock (Reality) Price in Malaysian Ringgit
  https://www.coingecko.com/en/coins/brookfield-infrastructure-partners-l-p-rstock/myr
- Sun 22 Nov | Yahoo! Finance Canada | Brookfield Infrastructure Partners L.P. (BIP-PF.TO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BIP-PF.TO/
## RKT +4.2%  Rocket Companies
- Mon 23 Nov | MarketBeat | Rocket Companies, Inc. (NYSE:RKT) Stock Rated "Moderate Buy" by Sell-Side Analysts
  https://www.marketbeat.com/instant-alerts/consensus-rocket-companies-inc-nyse-rkt-stock-rated-moderate-buy-by-sell-side-analysts-2026-11-23/
- Sun 22 Nov | Yahoo! Finance Canada | Rocket Companies, Inc. (RKT) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance Singapore | Rocket Companies, Inc. (RKT) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance | Rocket Companies (RKT) Just Got a Major Win — Wall Street Is Reacting
  https://finance.yahoo.com/markets/stocks/articles/rocket-companies-rkt-just-got-071103140.html
## MKC.V +3.8%  McCormick & Company, Incorporated
- Sun 22 Nov | Investing.com Australia | Form 4 McCormick & Co: Margaret M. V. Preston (Director) For: 26 October
  https://au.investing.com/news/stock-market-news/form-4-mccormick--co-margaret-m-v-preston-director-for-26-october-93CH-4788496
- Sun 22 Nov | Yahoo! Finance Canada | McCormick & Company, Incorporated (MKC) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/MKC/
- Sat 21 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Stock Breaks Above 50 Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-stock-breaks-above-50-day-moving-average-whats-next-2026-11-21/
- Sat 21 Nov | Timothy Sykes | McCormick & Company Incorporated (MKC) Stock Price | Live Quotes & Charts | NYSE
  https://www.timothysykes.com/quote/MKC/
## GIS +3.7%  General Mills
- Sun 22 Nov | Simply Wall St | How Operating Reorganization Will Impact General Mills (GIS) Investors
  https://simplywall.st/stocks/us/food-beverage-tobacco/nyse-gis/general-mills/news/how-operating-reorganization-will-impact-general-mills-gis-i
- Sun 22 Nov | Yahoo Finance | General Mills vs. Kraft Heinz: Which Food Dividend Is Better for Retirees?
  https://finance.yahoo.com/markets/stocks/articles/general-mills-vs-kraft-heinz-200733902.html
- Sun 22 Nov | Yahoo! Finance Canada | General Mills, Inc. (GIS) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/GIS/
- Sat 21 Nov | Investing.com Australia | Form 4 General Mills: Pankaj MN Sharma (Segment President) For: 17 November
  https://au.investing.com/news/stock-market-news/form-4-general-mills-pankaj-mn-sharma-segment-president-for-17-november-93CH-4788287
## NBIS -16.1%  Nebius Group
- Mon 23 Nov | Simply Wall St | Is Nebius Group (NBIS) Cheap On Lower 2026 Guidance And AI Cloud Risks?
  https://simplywall.st/stocks/us/software/nasdaq-nbis/nebius-group/news/is-nebius-group-nbis-cheap-on-lower-2026-guidance-and-ai-clo
- Sun 22 Nov | Pluang | Nebius stock plunges 16%, down 72% from its pea...
  https://pluang.com/en/news-feed/michael-burry-peringatkan-nebius-saham-turun-16-persen-72-persen-dari-rekor
- Sun 22 Nov | Yahoo! Finance Canada | Nebius Group N.V. (NBIS) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/NBIS/
- Sun 22 Nov | TradingKey | Nebius Stock Forecast: How Did NBIS Secure $44B in Contracts and What's Next?
  https://www.tradingkey.com/analysis/stocks/us-stocks/261948514-nbis-stock-forecast-can-44bn-in-ai-contracts-drive-more-upside-tradingkey
## CLS -16.1%  Celestica
- Mon 23 Nov | MarketBeat | Celestica (NYSE:CLS) Upgraded to Buy at Wall Street Zen
  https://www.marketbeat.com/instant-alerts/analyst-celestica-nyse-cls-upgraded-to-buy-at-wall-street-zen-2026-11-23/
- Sun 22 Nov | Kalkine Media | What Shapes Celestica (TSX:CLS)'s Role in AI Hardware Manufacturing?
  https://kalkinemedia.com/ca/stocks/technology/what-shapes-celestica-tsxclss-role-in-ai-hardware-manufacturing
- Fri 20 Nov | StockInvest.us | Celestica Stock Price Forecast. Should You Buy CLS.TO?
  https://stockinvest.us/stock/CLS.TO
- Fri 20 Nov | MarketBeat | Celestica (NYSE:CLS) Stock Price Down 16.3% - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-celestica-nyse-cls-stock-price-down-163-time-to-sell-2026-11-20/
## SNDK -16.1%  Sandisk
- Mon 23 Nov | FinanceFeeds | Sandisk Stock $79.24: 5% Overnight Rebound Before Dell, HP
  https://financefeeds.com/sandisk-sndk-stock-79-monday-5-percent-overnight-rebound-dell-hp-results-tuesday-bull-90-bear-73/
- Mon 23 Nov | TipRanks | Why AMD, Micron, and Sandisk Stocks Are Bouncing Back Overnight After Friday’s Crash — and Which Has the Most Upside Ahead
  https://www.tipranks.com/news/why-amd-micron-and-sandisk-stocks-are-bouncing-back-overnight-after-fridays-crash-and-which-has-the-most-upside-ahead
- Mon 23 Nov | JournalArta | Micron and Sandisk Pitched as Cheaper AI Bets Than Nvidia
  https://journalarta.com/en/2026/11/23/micron-sandisk-pitched-cheaper-ai-bets-than-nvidia/
- Sun 22 Nov | The Globe and Mail | Micron Technology vs. Sandisk: Which Technology Stock Is a Better Buy for 2027?
  https://www.theglobeandmail.com/investing/markets/markets-news/motley/8957101/micron-technology-vs-sandisk-which-technology-stock-is-a-better-buy-for-2027/
## BE -15.3%  Bloom Energy
- Mon 23 Nov | Trefis | What Moved Bloom Energy Stock?
  https://www.trefis.com/stock/be/articles/627709/what-moved-bloom-energy-stock/2026-11-23
- Sun 22 Nov | Pluang | Bloom Energy's stock drops despite doubling rev...
  https://pluang.com/en/news-feed/haruskah-anda-investasi-1000-dolar-di-bloom-energy-sekarang
- Sun 22 Nov | Pluang | Bloom Energy's revenue soars 138% but stock dro...
  https://pluang.com/en/news-feed/peluang-atau-penurunan-lanjutan-saham-bloom-energy
- Sun 22 Nov | The Motley Fool | Bloom Energy Stock Has Crashed Nearly 60%. Is It a Once-in-a-Decade Opportunity at $145, or Should You Keep Waiting for a Bigger Drop?
  https://www.fool.com/investing/2026/11/22/bloom-energy-stock-has-crashed-nearly-60-is-it-a-once-in-a-decade-opportunity-at-usd145-or-should-you-keep-waiting-for-a-bigger-drop/
## CRDO -15.2%  Credo Technology Group Holding
- Sun 22 Nov | Simply Wall St | What Investors Got Wrong About Credo Technology Group Before The Drop
  https://simplywall.st/stocks/us/semiconductors/nasdaq-crdo/credo-technology-group-holding/news/what-investors-got-wrong-about-credo-technology-group-before/amp
- Sat 21 Nov | Benzinga | Benzinga Bulls and Bears: Nvidia, Credo, Red Cat
  https://www.benzinga.com/markets/market-summary/26/11/63515125/benzinga-bulls-and-bears-nvidia-credo-red-cat
- Sat 21 Nov | GuruFocus | Credo Technology Group Holding Ltd (CRDO) Stock Down 15.2% -- No
  https://www.gurufocus.com/news/9213649/credo-technology-group-holding-ltd-crdo-stock-down-152-now-undervalued-gf-score-75100
- Fri 20 Nov | GuruFocus | Credo Technology Group (CRDO) Shares Plunge Nearly 14% Amid Tech Sector Sell-Off
  https://www.gurufocus.com/news/9213209/credo-technology-group-crdo-shares-plunge-nearly-14-amid-tech-sector-selloff
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: WMT, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-23 CLHO results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (on track)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
    2026-11-11-jufo-results: open -> wrong  (Juhayna closed at 21.77 on November 22, below the 22 that makes the call wrong.)

## Fair value
- Changed since the last run: nothing by 10 points or more.
- In the ten cheapest or dearest with no note: MCQE, ADIB, EMFD, MTIE, AMOC, AMIA, LCSW, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-23. Open each story before using it.
## COMI  (8 leads)
- Mon 23 Nov | بنكي | شهادة 3 سنوات عائد متغير — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cds/21
  > شهادة 3 سنوات عائد متغير شهادة متغيرة العائد تقدم حاليًا 20.25% عند صرف العائد يوميًا و20.50% عند صرفه شهريًا، مع حد أدنى منخفض يبدأ من 1,000 جنيه وإمكانية الاقتراض بضمانها حتى 95% من قيمتها. - 20.25% – 20.5% - يومي 20.25% · شهري 20.5% | 180 | 2.5% | السنة الأولى (بعد ٦ شهور) |
- Mon 23 Nov | بنكي | تفعيل CIB Pay والدفع بالموبايل عبر NFC من البنك التجاري الدو
  https://www.bankygate.com/202975
  > أطلق البنك التجاري الدولي CIB تطبيق CIB Pay لهواتف أندرويد، والذي يتيح لعملاء البنك استخدام بطاقاتهم البنكية المؤهلة للدفع لدى التجار من خلال الهواتف المحمولة وتقنية الاتصال قريب المدى NFC، دون الحاجة إلى استخدام البطاقة البلاستيكية عند إتمام عملية الشراء.
- Sun 22 Nov | ad-hoc-news.de | Commercial International Bank stock: 9M net income reaches EGP 63.1bn
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/commercial-international-bank-stock-9m-net-income-reaches-egp-63-1bn/70544867
  > Commercial International Bank reported consolidated revenue of EGP 103 billion and net income of EGP 63.1 billion for the nine months ended September 30, 2026. The results were released on Monday, November 9, and later filed with the Egyptian Exchange. The bank's nine-month earnings release showed reported net income up 2 percent year over year. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## TMGH  (3 leads)
- Sun 22 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | صندوق الاستثمارات يوقع مذكرة تفاهم مع مجموعة طلعت مصطفى لتعزيز فرص التعاون
  https://www.argaam.com/ar/article/articledetail/id/1910794
  (page read: it never names the company, so probably not about it: skip)
- Sun 22 Nov | Mubasher | مع تهاوي بورصة مصر.. كيف جاء أداء "التجاري الدولي" و"طلعت مصطفى"؟
  https://www.mubasher.info/news/21588660/مع-تهاوي-بورصة-مصر-كيف-جاء-أداء-التجاري-الدولي-و-طلعت-مصطفى
  > القاهرة - مباشر: قاد سهم التجاري الدولي هبوط المؤشر الرئيسي للبورصة "EGX30 دون 50000 نقطة، مع تراجعه في ختام اليوم نحو 2%. وفي ختام البوم انخفض سهم التجاري الدولي عند مستوى 125 جنيه مستقطبا تداولات قيمتها 267.2 مليون جنيه، فيما هبط كل من القلعة وطلعت مصطفى 4% و4.3% على التوالي.
- Sat 21 Nov | شبكة تواصل الإخبارية | النائب عبدالرحمن بشاري يبحث مع هشام طلعت مصطفى أولوية توظيف أبناء الأقصر
  https://twaslnews1.twaslnews.com/8087323/
  (page: did not load (403))
## PHDC  (2 leads)
- Sun 22 Nov | اليوم السابع | خريطة تحركات الكبار بالبورصة.. مشتريات في فوري ومصر الجديدة وتخارجات من بالم هيلز
  https://www.youm7.com/story/2026/11/22/خريطة-تحركات-الكبار-بالبورصة-مشتريات-في-فوري-ومصر-الجديدة-وتخارجات/7627730
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية خلال جلسة تداول يوم الخميس الماضي، تنفيذ عدد من عمليات الشراء والبيع على أسهم الشركات المقيدة، تصدرتها عمليات الشراء على سهم شركة نهر الخير للتنمية والاستثمار الزراعي والخدمات البيئية، إلى جانب تداولات على أسهم مينا للاستثمار السياحي والعقاري، وفوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، وبالم هيلز ...
- Sat 21 Nov | نيوز رووم | سمسار عقارات يحرر محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» بسبب تلفيات بسيارته في أكتوبر أول
  https://www.newsroom.info/487470
  > سمسار عقارات يحرر محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» بسبب تلفيات بسيارته في أكتوبر أول حرر سمسار عقارات محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» تحت الإنشاء، بسبب تعرض سيارته لتلفيات أثناء تواجده بالكمبوند، واتهمهم بالإهمال، وتحرر محضر بالواقعة.
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
## FWRY  (3 leads)
- Sun 22 Nov | موقع القيادي | قصة نجاح فوري.. من دفع الفواتير إلى أرباح 2.9 مليار جنيه
  https://www.alqiyady.com/قصة-نجاح-فوري-من-دفع-الفواتير-إلى-أرباح-29-مليار-جنيه-897363.html
  (page: only 42 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | CairoScene | Fawry Allocates $1.6 Million for Cybersecurity Investments
  https://cairoscene.com/Business/Fawry-Allocates-1-6-Million-for-Cybersecurity-Investments
  > Fawry Allocates $1.6 Million for Cybersecurity Investments The fintech company is directing LE 80 million towards technology upgrades by the end of 2026. Egyptian fintech company Fawry plans to allocate LE 80 million (approximately $1.6 million) towards technology investments by the end of 2026, prioritising cybersecurity and improvements to its digital infrastructure.
- Sun 22 Nov | اليوم السابع | خريطة تحركات الكبار بالبورصة.. مشتريات في فوري ومصر الجديدة وتخارجات من بالم هيلز
  https://www.youm7.com/story/2026/11/22/خريطة-تحركات-الكبار-بالبورصة-مشتريات-في-فوري-ومصر-الجديدة-وتخارجات/7627730
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية خلال جلسة تداول يوم الخميس الماضي، تنفيذ عدد من عمليات الشراء والبيع على أسهم الشركات المقيدة، تصدرتها عمليات الشراء على سهم شركة نهر الخير للتنمية والاستثمار الزراعي والخدمات البيئية، إلى جانب تداولات على أسهم مينا للاستثمار السياحي والعقاري، وفوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، وبالم هيلز ...
## ABUK  (1 leads)
- Sun 22 Nov | www.marketscreener.com | Abu Qir Fertilizers & Chemical Industries Company (S.A.E) Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
  https://www.marketscreener.com/news/abu-qir-fertilizers-chemical-industries-company-s-a-e-reports-earnings-results-for-the-third-qua-ce785ed3d088f024
  (page: did not load (403))
## HRHO  (6 leads)
- Mon 23 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page read: it never names the company, so probably not about it: skip)
- Mon 23 Nov | ad-hoc-news.de | EFG Holding stock: Q3 revenue rises 5%, profit falls 15%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/efg-holding-stock-q3-revenue-rises-5-profit-falls-15/70544966
  > EFG Holding reported a mixed third quarter on November 18, 2026, as stronger investment-bank and non-bank finance revenue was offset by higher expenses and weaker commercial-bank performance. In its EFG Holding earnings release, the group reported net operating revenue of EGP6.652 billion for 3Q26 and net profit after tax and minority interest of EGP720 million. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Sun 22 Nov | آراب فاينانس | إي اف جي هيرميس تتم إصدار سندات توريق لصالح كليفر للتمويل الاستهلاكي
  https://www.arabfinance.com/ar/news/newdetails/إي-اف-جي-هيرميس-تتم-إصدار-سندات-توريق-لصالح
  > آراب فاينانس: أعلنت إي اف جي هيرميس، بنك الاستثمار التابع لمجموعة إي اف چي (HRHO) والرائد في أسواق الشرق الأوسط وشمال إفريقيا، عن نجاح قسم أسواق الدين بقطاع الترويج وتغطية الاكتتاب في إتمام الخدمات الاستشارية لإصدار سندات توريق بقيمة 301 مليون جنيه لصالح شركة كليفر للتمويل الاستهلاكي (Klivvr)، وفقا لما ذكره البيان المرسل بتاريخ 17 ...
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
  (page read: it never names the company, so probably not about it: skip)
- Sun 22 Nov | ايكونومي بلس | "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو"
  https://economyplusme.com/ar/news/34326
  > "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو" أبقت شركة "سي آي كابيتال" على توصيتها المحايدة لسهمي "أبو قير للأسمدة" و"مصر لإنتاج الأسمدة – موبكو"، مع رفع السعر المستهدف للسهمين، في ظل تذبذب أسعار اليوريا والتوترات الجيوسياسية المرتبطة بمضيق هرمز.
- Sun 22 Nov | بوابة الزهراء | سي آي كابيتال ترفع السعر المستهدف لسهمي أبوقير وموبكو في السوق المالية
  https://zahraa.mr/1348/سي-آي-كابيتال-ترفع-السعر-المستهدف-لسهم/
  > أكدت شركة “سي آي كابيتال” على موقفها المحايد لسهمي “أبو قير للأسمدة” و”موبكو” مع رفع السعر المستهدف لهما، وسط تقلبات أسعار اليوريا والتوترات الجيوسياسية في مضيق هرمز. رفع الأسعار المستهدفة لسهمي “أبو قير” و”موبكو” وسط تقلبات السوق
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
- Sun 22 Nov | فيتو | مواصفات ماكينات الصراف الآلي المخصصة لصرف الحوالات في بنك القاهرة
  https://www.vetogate.com/5776040
  > مواصفات ماكينات الصراف الآلي المخصصة لصرف الحوالات في بنك القاهرة يبحث الكثير من عملاء بنك القاهرة عن مواصفات ماكينات الصراف الآلي المخصصة لصرف الحوالات.
- Sun 22 Nov | عالم المال | هشام قنديل: طرح بنك القاهرة يعزز جاذبية البورصة ويفتح فرصا جديدة أمام السهم
  https://alamalmal.net/article/943860/هشام-قنديل-طرح-بنك-القاهرة-يعزز-جاذبية
  > يمثل طرح بنك القاهرة في البورصة المصرية خطوة مهمة ضمن برنامج الطروحات الحكومية، لما يحمله من انعكاسات على سوق المال والاقتصاد المصري، سواء من حيث زيادة السيولة وجذب شرائح جديدة من المستثمرين، أو تعزيز ثقة المؤسسات الأجنبية والمحلية في فرص الاستثمار بالسوق المصرية، فضلاً عن دعم توجه الدولة نحو توسيع مشاركة القطاع الخاص في النشاط ...
- Sun 22 Nov | بنكي | بنك القاهرة يحصد 3 جوائز من «جلوبال براند» لعام 2026
  https://www.bankygate.com/202967
  > حصد بنك القاهرة ثلاث جوائز ضمن جوائز Global Brand Awards 2026، التي تنظمها مجلة Global Brands Magazine، بعدما فاز بجوائز «أفضل حملة تسويقية»، و«العلامة المصرفية الأكثر موثوقية»، و«التميز في المسؤولية المجتمعية والأثر المجتمعي»، ضمن فئات الجوائز المخصصة للسوق المصرية.
- Sun 22 Nov | التعمير | بنك القاهرة يحصد 3 جوائز دولية في التسويق المصرفي وثقة العملاء والمسئولية المجتمعية لعام 2026
  https://eltaameer.com/archives/486063
  > سجل بنك القاهرة حضورًا لافتًا ضمن المؤسسات المصرفية الفائزة بجوائز «جلوبال براند أووردز» لعام 2026، بعدما حصد ثلاث جوائز منحتها مجلة «جلوبال براندز»، تقديرًا لتميزه في عدد من المجالات المرتبطة بتعزيز مكانة العلامة التجارية، وتطوير الحملات التسويقية، ودعم المسئولية المجتمعية وتحقيق التأثير الإيجابي في المجتمع.
- Sun 22 Nov | صحيفة الخليج | «مؤسسة التمويل الدولية» تستثمر 100مليون دولار في الطرح العام الأولي لبنك القاهرة
  https://www.alkhaleej.ae/2026-11-22/اقتصاد/أسواق-عربية-وعالمية/مؤسسة-التمويل-الدولية-تستثمر-100مليون-دولار-في-الطرح-العام-الأولي-لبنك-القاهرة
- Sun 22 Nov | بنكي | الوديعة الشهرية ذات العائد عند الاستحقاق — بنك القاهرة
  https://www.bankygate.com/products/deposits/2125
- Sun 22 Nov | بنكي | وظيفة خالية ببنك القاهرة .. مسؤول أول رقابة تكنولوجيا المعلو
  https://www.bankygate.com/202941
- Sun 22 Nov | عالم المال | محمد عبد الهادي: طرح بنك القاهرة يعزز سيولة البورصة
  https://alamalmal.net/article/943859/محمد-عبد-الهادي-طرح-بنك-القاهرة-يعزز
## EGAL  (1 leads)
- Sun 22 Nov | دار المعارف | طلائع مركز شباب قنا في ضيافة شركة مصر للألومنيوم
  https://daralmaref.com/News/2611455.aspx
  (page: did not load (403))
## EFID  (6 leads)
- Mon 23 Nov | القاهرة 24 | الرقابة المالية توافق على نشر إفصاح «إيديتا» بشأن تخفيض رأس المال بإعدام 11.3 مليون سهم خزينة
  https://www.cairo24.com/2534225
  > الرقابة المالية توافق على نشر إفصاح «إيديتا» بشأن تخفيض رأس المال بإعدام 11.3 مليون سهم خزينة أعلنت الهيئة العامة للرقابة المالية عدم ممانعتها على نشر تقرير إفصاح شركة إيديتا للصناعات الغذائية، بشأن تخفيض رأس المال المصدر والمدفوع بقيمة 2.2 مليون جنيه، ليصل إلى 416.7 مليون جنيه، مقارنة بنحو 418.9 مليون جنيه. تخفيض رأس مال إيديتا
- Mon 23 Nov | جريدة حابي | الرقابة المالية تقر دعوة عمومية إيديتا للنظر في تخفيض رأس المال المُصدر والمدفوع
  https://hapijournal.com/2026/11/23/الرقابة-المالية-تقر-دعوة-عمومية-إيديت/
  > الرقابة المالية تقر دعوة عمومية إيديتا للنظر في تخفيض رأس المال المُصدر والمدفوع عن طريق إعدام 11.006 مليون سهم خزينة رنا ممدوح _ وافقت الهيئة العامة للرقابة المالية، على نشر تقرير إفصاح شركة إيديتا للصناعات الغذائية، تمهيدًا للسير في إجراءات دعوة الجمعية العامة غير العادية للنظر في تخفيض رأس المال المُصدر والمدفوع.
- Mon 23 Nov | اليوم السابع | 11 مليون سهم خارج الخدمة.. كواليس خفض رأس مال "إيديتا" بالبورصة
  https://www.youm7.com/story/2026/11/23/11-مليون-سهم-خارج-الخدمة-كواليس-خفض-رأس-مال-إيديتا/7628895
  > تعتزم شركة إيديتا للصناعات الغذائية، تخفيض رأس المال المصدر والمدفوع بقيمة 2.2 مليون جنيه، من خلال إعدام 11 مليون سهم خزينة، ليصل رأس المال من 418.91 مليون جنيه إلى 416.71 مليون جنيه، وذلك بعد حصول الشركة على عدم ممانعة الهيئة العامة للرقابة المالية على نشر تقرير الإفصاح تمهيدًا لدعوة الجمعية العامة غير العادية للنظر في ...
- Mon 23 Nov | www.youlyou.com | الرقابة المالية توافق على خفض رأسمال إيديتا إلى 4.167 مليار جنيه
  https://www.youlyou.com/100748
  > وافقت الهيئة العامة للرقابة المالية على نشر تقرير الإفصاح الخاص بشركة إيديتا للصناعات الغذائية، بشأن تخفيض رأس المال المصدر والمدفوع للشركة عن طريق إعدام أسهم خزينة، تمهيدا لدعوة الجمعية العامة غير العادية للنظر في اعتماد التخفيض. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Mon 23 Nov | Mubasher | الرقابة المالية تقر تخفيض رأسمال"إيديتا" عبر إعدام 11 مليون سهم خزينة
  https://www.mubasher.info/news/21588786/الرقابة-المالية-تقر-تخفيض-رأسمال-إيديتا-عبر-إعدام-11-مليون-سهم-خزينة
- Sun 22 Nov | Assabah | انفصال “ديسلوغ” و “إيديتا” يضع حكامة استثمارات بلخياط تحت المجهر
  https://assabah.ma/964597.html
## AAPL  (7 leads)
- Mon 23 Nov | MarketBeat | Apple Stock Earnings Estimates Decreased by Erste Group Bank
  https://www.marketbeat.com/instant-alerts/estimates-apple-stock-earnings-estimates-decreased-by-erste-group-bank-2026-11-23/
  > Apple Stock Earnings Estimates Decreased by Erste Group Bank - Erste Group Bank trimmed its FY2027 Apple EPS forecast to $9.50 from $9.57, slightly above the $9.45 consensus estimate. The bank also projected FY2028 EPS of $10.55.
- Sun 22 Nov | AOL.com | Apple Is Now 25% of Berkshire Hathaway's Stock Portfolio. Here's What Holding Every Share Tells Investors.
  https://www.aol.com/articles/apple-now-25-berkshire-hathaways-225502000.html
  > - Berkshire Hathaway hasn't sold a single Apple share in 2026, despite its price soaring 29%. - With Apple's stock now trading at almost 40 times earnings, the decision to stay put suggests valuation is weighing less on the conglomerate’s thinking.
- Sun 22 Nov | BeInCrypto | Why is Apple Stock Holding Strong While the Rest of the Market Falls?
  https://beincrypto.com/apple-stock-market-crash-price-outlook/
  (page: did not load (403))
## MSFT  (8 leads)
- Mon 23 Nov | blockchain.news | Microsoft (MSFT) Stock Price Prediction: Earnings strength meets a still-fragile technical setup
  https://blockchain.news/news/20261123-price-prediction-msft-earnings-strength-meets-a-still-fragile
  > Strong quarter, but the tape is not confirming it yet Microsoft’s latest reported quarter was solid: revenue came in at $92.3 billion, up 19%, operating income rose 21% to $45.9 billion, and diluted EPS reached $4.92 on a GAAP basis, up 32%, according to Microsoft’s October 28, 2026 results release.
- Mon 23 Nov | Simply Wall St | Akamai Stock and Microsoft Edge Mobile Security Deal What's Changed
  https://simplywall.st/stocks/us/software/nasdaq-akam/akamai-technologies/news/akamai-stock-and-microsoft-edge-mobile-security-deal-whats-c
  > Akamai Technologies recently expanded its enterprise security reach by integrating Workforce Protector into Microsoft Edge for Business on iOS and Android, giving mobile users web, SaaS, and generative AI protections within a familiar browser.
- Sun 22 Nov | Fortune | Microsoft’s CFO admits she joined the tech giant without even knowing her salary—and then missed her first day of work
  https://fortune.com/article/microsoft-cfo-amy-hood-career-advice-duke-university-commencement-class-of-2026/
  > As an economics undergraduate at Duke University in the 1990s, Amy Hood had no master plan that would one day land her the top finance job at one of the world’s biggest tech companies.
- Sun 22 Nov | Barchart.com | Microsoft Remains Attractively Valued as Azure and Cloud Drive Growth
  https://www.barchart.com/story/news/8957349/microsoft-remains-attractively-valued-as-azure-and-cloud-drive-growth
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | ad-hoc-news.de | Microsoft Faces Washington Scrutiny Over ByteDance Deal as It Untangles a Two-Month-Old Outlook Bug
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/microsoft-faces-washington-scrutiny-over-bytedance-deal-as-it-untangles-a-two-month-old-outlook-bug/70544740
- Sun 22 Nov | TradingKey | Microsoft (MSFT) Q4 FY2026 Earnings Preview: $87.7B Revenue, Azure 40%, FY2027 Capex $255-260B
  https://www.tradingkey.com/analysis/stocks/us-stocks/262060902-microsoft-msft-q4-fy2026-earnings-preview-july-29-azure-capex-tradingkey
- Sun 22 Nov | Yahoo Finance Singapore | Is Microsoft (MSFT) Building A Bigger AI Role In Scientific Labs?
  https://sg.finance.yahoo.com/news/microsoft-msft-building-bigger-ai-160715680.html
- Sun 22 Nov | TheStreet | Bank of America sends strong signal to Microsoft stock investors
  https://www.thestreet.com/investing/stocks/bank-of-america-sends-strong-signal-to-microsoft-stock-investors
## NVDA  (8 leads)
- Mon 23 Nov | Yahoo Finance | Nvidia News Has Investors Rethinking These U.S. AI Chip Stocks
  https://finance.yahoo.com/technology/ai/articles/nvidia-news-investors-rethinking-u-070751605.html
  > AI chip stocks just came through a sharp sentiment swing, with Nvidia's leadership drama, export control worries and U.S.–China security concerns colliding with a sudden rebound in futures. That mix of anxiety and optimism can reset prices quickly, which matters if you care about where capital flows next. This article walks through 3 U.S.
- Mon 23 Nov | Yahoo Finance | Nvidia (NVDA) Stock Looks Below Fair Value After Recent Turmoil
  https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-stock-looks-below-070752587.html
  > NVIDIA has dropped sharply in recent weeks after a long multi year climb, and with leadership turmoil and regulatory probes now in the mix, the key issue for investors is whether the current share price still lines up with what its earnings can reasonably support.
- Mon 23 Nov | Trefis | Verizon Cut Its Buying In 2002. Can Nvidia’s Buyers Stop Now?
  https://www.trefis.com/stock/nvda/articles/627418/verizon-cut-its-buying-in-2002-can-nvidia-s-buyers-stop-now/2026-11-23
  > Verizon Cut Its Buying In 2002. Can Nvidia’s Buyers Stop Now? Today’s big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? In an earlier piece, we looked at the phone companies that cut their spending in 2002.
- Mon 23 Nov | Trefis | Google Can Spend $48 Billion More On AI From Its Own Cash. Is That Enough For Nvidia?
  https://www.trefis.com/stock/googl/articles/627438/google-can-spend-48-billion-more-on-ai-from-its-own-cash-is-that-enough-for-nvidia/2026-11-23
  > Google Can Spend $48 Billion More On AI From Its Own Cash. Is That Enough For Nvidia? Today’s big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? It can spend about $48 billion more in 2027 than it is likely to spend in 2026, without new debt. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 23 Nov | Trefis | Nvidia Stock At $125: Where’s The Floor?
  https://www.trefis.com/stock/nvda/articles/627453/nvidia-stock-at-125-where-s-the-floor/2026-11-23
- Mon 23 Nov | Trefis | Nvidia’s Forecast Needs $1.4 Trillion Of AI Spending In 2027. Who Pays?
  https://www.trefis.com/stock/nvda/articles/627446/nvidia-s-forecast-needs-1-4-trillion-of-ai-spending-in-2027-who-pays/2026-11-23
- Mon 23 Nov | Trefis | Oracle Or The Fed: What Really Moves Nvidia Stock?
  https://www.trefis.com/stock/nvda/articles/627412/oracle-or-the-fed-what-really-moves-nvidia-stock/2026-11-23
- Mon 23 Nov | Trefis | Can The Fed Rescue Nvidia Stock Before Christmas?
  https://www.trefis.com/stock/nvda/articles/627410/can-the-fed-rescue-nvidia-stock-before-christmas/2026-11-23
## AMZN  (8 leads)
- Mon 23 Nov | Blockchain News | Amazon (AMZN) Stock Price Prediction: Pullback Holds Above Key Support as AI Spending Keeps the Tape Heavy
  https://blockchain.news/news/20261123-price-prediction-amzn-pullback-holds-above-key-support-as
  > Price action still looks corrective, not impulsive Amazon (AMZN) is at $255.47, with the latest 24-hour range running from $251.74 to $257.36.
- Mon 23 Nov | ad-hoc-news.de | Amazon's Satellite Setback and a Sold-Out Hedge Fund Stake Overshadow a Bullish Analyst Call
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-satellite-setback-and-a-sold-out-hedge-fund-stake-overshadow-a-bullish-analyst-call/70545362
  > A failed rocket launch and a quiet exit by one prominent investor gave Amazon shareholders plenty to digest this week, even as Wall Street's price targets moved in the opposite direction. Third Point disclosed on November 16 that it had fully liquidated its Amazon position by September 30.
- Mon 23 Nov | JournalArta | Nasdaq Falls Near 19% as Options Trader Eyes Amazon Strangle
  https://journalarta.com/en/2026/11/23/nasdaq-falls-near-19-percent-amazon-options-strangle/
  > Nasdaq Falls Near 19% as Options Trader Eyes Amazon Strangle The Nasdaq Composite is down nearly 19% from its recent high and the VIX touched 40 on Friday. Mike Khouw sees elevated options premiums on Amazon, which is off 14%, and outlines a December strangle trade that pays a $5.90 credit per share.
- Mon 23 Nov | IGN | The PlayStation 5 Pro Console Is Going In and Out of Stock at Amazon
  https://www.ign.com/articles/the-playstation-5-pro-console-is-going-in-and-out-of-stock-at-amazon
  > The PlayStation 5 Pro will certainly not be discounted on Black Friday. In fact, you'd be lucky just to find one for retail price. Fortunately, Amazon appears to be restocking PlayStation 5 Pro consoles on a very sporadic basis. The least expensive bundle is the PS5 Pro with charging station for $928.99 with free shipping.
- Sun 22 Nov | Beinsure | Jeff Bezos Amazon stock donation reaches $629 mn in 2026
  https://beinsure.com/news/jeff-bezos-amazon-stock-donation-reaches-629mn/
- Sun 22 Nov | bsinews.id | Bezos Donates 771492 Amazon Shares to Nonprofits
  https://bsinews.id/en/bezos-amazon-share-donations
- Sun 22 Nov | SuaraGarut.ID | Jeff Bezos Donates Nearly $199 Million in Amazon Shares
  https://suaragarut.id/en/bezos-amazon-stock-donations-2026
- Sun 22 Nov | cwibc.co.id | Jeff Bezos Donates 771492 Amazon Shares Worth Nearly 199 Million
  https://cwibc.co.id/en/bezos-amazon-charity-donations-2026
## GOOGL  (8 leads)
- Mon 23 Nov | blockchain.news | Alphabet (GOOGL) Stock Price Prediction: Price Rebounds, but Trend Still Needs Confirmation
  https://blockchain.news/news/20261123-price-prediction-price-googl-rebounds-but-trend-still-needs-confirmation
  > What the tape says now Alphabet (Google) (GOOGL) traded at $277.03, with a 24-hour range of $271.76 to $278.28 and volume of $91.4 million on Binance Futures. That puts the stock just above its pivot point of $275.69, but still below immediate resistance at $279.62 and strong resistance at $282.21. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 23 Nov | JournalArta | Alphabet (GOOGL) Stock: $265.29, Down 2.70% Nov 20
  https://journalarta.com/en/2026/11/23/alphabet-googl-stock-update-slides-2-70-down-17-2-in-a-month/
  > Alphabet (GOOGL) Stock Update: Slides 2.70%, Down 17.2% in a Month Technical analysis of GOOGL stock on November 20, 2026: price 265.29 USD, trend downtrend, RSI 27.7, support 265.29, resistance 324.89.
- Sun 22 Nov | TheStreet | Jim Cramer sends a strong signal to Google stock investors
  https://www.thestreet.com/investing/stocks/jim-cramer-sends-a-strong-signal-to-google-stock-investors
  (page: did not load (403))
- Sun 22 Nov | Investing.com India | Form 4 Alphabet Inc Class A For: 22 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-22-november-93CH-5719850
  (page: did not load (403))
- Sun 22 Nov | Pluang | Alphabet's stock drops 34% as it borrows $10.9B for data center expansion amid AI demand uncertainty.
  https://pluang.com/en/news-feed/saham-alphabet-terendah-1-tahun-induk-google-pinjam-besar
- Sun 22 Nov | TradingKey | Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?
  https://www.tradingkey.com/analysis/stocks/us-stocks/262008961-alphabet-googl-stock-price-forecast-2026-google-cloud-tradingkey
- Sun 22 Nov | Stockhouse | 2026-11-22 | GOOG Investors Have Opportunity to Lead Alphabet Inc. Class Action Lawsuit - Contact Bronstein, Gewirtz and Grossman, LLC Today! | TSX:GOOG | Press Release
  https://stockhouse.com/news/press-releases/2026/11/22/goog-investors-have-opportunity-to-lead-alphabet-inc-class-action-lawsuit
- Sun 22 Nov | Kalkine Media | Will Alphabet Inc. (NASDAQ:GOOGL) Keep Moving Forward From Here?
  https://kalkinemedia.com/us/stocks/communication/will-alphabet-inc-nasdaqgoogl-keep-moving-forward-from-here
## META  (8 leads)
- Mon 23 Nov | Wisevoter | Meta Shares Fall 12.6% on Week
  https://wisevoter.com/world/us/2026/11/23/meta-platforms-shares-fall-week-litigation
  > Meta Shares Fall 12.6% on Week Meta stock closed at $560.84 on Friday after a weekly decline tied to Delaware shareholder litigation and reported problems with its Muse AI agent. 23, 2026 in Public Companies
- Mon 23 Nov | blockchain.news | Meta Platforms (META) Stock Price Prediction: Bulls have analyst support, but the chart is still fighting the trend
  https://blockchain.news/news/20261123-price-prediction-meta-bulls-have-analyst-support-but-the
  > Price action says the rebound still needs proof Meta Platforms (META) is changing hands at $580.28, up 1.61% on the latest read, but the broader technical picture remains soft.
- Mon 23 Nov | FinanceFeeds | Meta Stock $560.84: Muse Safety Report After 13% Weekly Fall
  https://financefeeds.com/meta-stock-560-monday-muse-safety-report-after-13-percent-weekly-fall-bull-626-bear-520/
  (page: did not load (403))
- Mon 23 Nov | Investing.com UK | Form 4 Meta Platforms Inc For: 23 November By Investing.com
  https://uk.investing.com/news/stock-market-news/form-4-meta-platforms-inc-for-23-november-93CH-4998336
  (page: did not load (403))
- Mon 23 Nov | Trefis | Is Meta Stock Worth More Than Its Tech Rivals?
  https://www.trefis.com/stock/meta/articles/627551/is-meta-stock-worth-more-than-its-tech-rivals/2026-11-22
- Mon 23 Nov | Gotrade | Meta Stock Falls 5.9% as AI Stocks Slide (Nov 20)
  https://www.heygotrade.com/en/news/meta-meta-stock-news-november-23-2026/
- Mon 23 Nov | Yahoo Finance | After Blockbuster Anthropic IPO, OpenAI Wants AI Rivals To Agree On Development ‘Limits’, While Meta Calls For Controlled Approach
  https://finance.yahoo.com/technology/ai/articles/blockbuster-anthropic-ipo-openai-wants-031510105.html
- Sun 22 Nov | Pluang | Alphabet and Meta Platforms show strong growth but face distinct risks and valuation differences for 2027.
  https://pluang.com/en/news-feed/alphabet-vs-meta-platforms-saham-media-terbaik-untuk-2027
## TSLA  (8 leads)
- Mon 23 Nov | ad-hoc-news.de | Tesla stock gains 0.77% to EUR 327.25 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/tesla-stock-gains-0-77-to-eur-327-25-before-xetra/70545927
  > Tesla designs, manufactures and sells electric vehicles as well as energy generation and storage systems. On Xetra, the stock closed at EUR 324.75 on Friday, November 20, 2026. Tesla designs, manufactures and sells electric vehicles and energy generation and storage systems.
- Mon 23 Nov | Stocktwits | Cathie Wood Says TSLA Holders ‘Will Get’ A Premium If SpaceX Buys Tesla — HSBC Puts It At Over 30%
  https://stocktwits.com/news-articles/markets/equity/cathie-wood-tsla-holders-premium-if-spacex-buys-tesla-hsbc/cNbYtWbR9Si
  > If SpaceX wants Tesla shareholders to approve a buyout, ARK Investment Management CEO Cathie Wood believes it will have to offer them a premium, and HSBC estimates that a bid 33% above Tesla’s 30-day average would value the stock at $507 per share.
- Mon 23 Nov | cwibc.co.id | Musk Loses 64 Billion as Tesla and SpaceX Shares Fall
  https://cwibc.co.id/en/musk-wealth-tesla-spacex-decline
  (page: did not load (520))
- Mon 23 Nov | Trefis | Could Tesla Stock Really Fall To $140?
  https://www.trefis.com/stock/tsla/articles/627621/could-tesla-stock-really-fall-to-140/2026-11-23
  > Could Tesla Stock Really Fall To $140? Tesla stock closed at $345.82 on Friday, Nov 20, down 7.6% in one day. Nvidia dropped 14.0%, and the S&P 500 lost 3.7%. So could Tesla go to $140? Our read: that would be deeper than anything Tesla did in any past Nvidia crash.
- Mon 23 Nov | TIKR.com | Musk Says Tesla’s Real-World AI Will Get Smarter by “About an Order of Magnitude per Year”
  https://www.tikr.com/blog/musk-says-teslas-real-world-ai-will-get-smarter-by-about-an-order-of-magnitude-per-year?
- Mon 23 Nov | Reuters | Tesla Inc (TSLA.O) | Stock Price & Latest News
  https://www.reuters.com/markets/companies/TSLA.O/
- Mon 23 Nov | Gotrade | Tesla Stock (TSLA) Falls 7.6% as Growth Stocks Slide (Nov 20)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-23-2026/
- Mon 23 Nov | The Motley Fool | Forget Flying Roadsters. Tesla Investors Have 3 Bigger Challenges to Watch.
  https://www.fool.com/investing/2026/11/22/forget-flying-roadsters-tesla-investors-have-3-bigger-challenges-to-watch/
## JPM  (8 leads)
- Mon 23 Nov | Investing.com | JPMorgan initiates HudBay Minerals stock coverage with overweight rating
  https://www.investing.com/news/analyst-ratings/jpmorgan-initiates-hudbay-minerals-stock-coverage-with-overweight-rating-93CH-5044525
  (page: did not load (403))
- Mon 23 Nov | Yahoo Finance | JPMorgan Chase (JPM) CEO Warns UK Tax Rise Could Threaten £3 Billion HQ
  https://finance.yahoo.com/economy/policy/articles/jpmorgan-chase-jpm-ceo-warns-070656078.html
  > - JPMorgan Chase (NYSE:JPM) CEO Jamie Dimon warned that higher UK bank taxes could affect the bank's new £3b Canary Wharf headquarters plan. - Dimon linked the UK Labour government's increase to the bank surcharge to a review of JPMorgan's long term British investment commitments.
- Mon 23 Nov | TradingView | Weekly Recap: Bond-conversion loan and JPMorgan economic interest
  https://www.tradingview.com/news/tradingview:ac14f711b5722:0-weekly-recap-bond-conversion-loan-and-jpmorgan-economic-interest/
  > Weekly Recap: Bond-conversion loan and JPMorgan economic interest Sibanye Stillwater Limited Sponsored ADR (JSE:SSW) approved a share loan and guarantee for Stillwater Mining bond conversions, with up to 398,946,781 ordinary shares potentially issued if all bondholders convert. It also reported that JPMorgan Chase acquired an economic interest in its securities.
- Mon 23 Nov | Insajderi | Hackers stole customer data linked to Visa, Mastercard and JPMorgan Chase
  https://insajderi.org/en/Hackers-steal-customer-data-linked-to-Visa--MasterCard-and-JPMorgan-Chase/
  (page: did not load (403))
- Sun 22 Nov | Kalkine | Champion Iron Sees JPMorgan Chase & Co. Lift Stake to 6.07% in 18 November 2026 Notice
  https://kalkine.com.au/news/announcements/champion-iron-sees-jpmorgan-chase-co-lift-stake-to-607-in-18-november-2026-notice
- Sun 22 Nov | Kalkine | JPMorgan Chase & Co. Ceases to Be Substantial Holder in Lindian Resources on 18 November 2026
  https://kalkine.com.au/news/announcements/jpmorgan-chase-co-ceases-to-be-substantial-holder-in-lindian-resources-on-18-november-2026
- Sun 22 Nov | Kalkine | JPMorgan Chase & Co. Becomes Substantial Holder in Liontown Resources with 5.07% Voting Power
  https://kalkine.com.au/news/announcements/jpmorgan-chase-co-becomes-substantial-holder-in-liontown-resources-with-507-voting-power
- Sun 22 Nov | TIKR.com | Trump Backs a 10% Card Rate Cap With Democrats. That’s a Big Risk for JPMorgan and Citigroup
  https://www.tikr.com/blog/trump-backs-a-10-card-rate-cap-with-democrats-thats-a-big-risk-for-jpmorgan-and-citigroup?
## XOM  (8 leads)
- Mon 23 Nov | Trending Now Sustainable Construction | ExxonMobil and partners approve $4bn investment in Angola's Block 15
  https://www.sustainableconstruction-now.com/article/564162/exxonmobil-and-partners-approve-4bn-investment-in-angolas-block-15
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | Construction Review | Greater Makarem: Oman Signs $400M+ Gas and LNG Deal with ExxonMobil and EDO
  https://constructionreviewonline.com/greater-makarem-oman-signs-400m-gas-and-lng-deal-with-exxonmobil-and-edo/
  > Oman inked a concession agreement with Energy Development Oman (EDO) and ExxonMobil to appraise and develop discovered natural gas resources in the Greater Makarem area (Block 20). The total initial investments of the development are expected to exceed $400 million. The minister said ExxonMobil’s investment reflects the attractiveness of Oman’s energy sector to international companies.
- Mon 23 Nov | MarketBeat | Erste Group Bank Predicts Stronger Earnings for ExxonMobil
  https://www.marketbeat.com/instant-alerts/estimates-erste-group-bank-predicts-stronger-earnings-for-exxonmobil-2026-11-23/
  > Erste Group Bank Predicts Stronger Earnings for ExxonMobil - Erste Group raised its FY2027 EPS forecast for ExxonMobil to $12.12 from $11.82 and maintained a Buy rating. - ExxonMobil beat quarterly expectations, reporting EPS of $4.23 versus $4.12 forecast and revenue of $110.50 billion versus $104.89 billion expected.
## AVGO  (8 leads)
- Mon 23 Nov | Trefis | Why Did Broadcom Stock Drop On Friday?
  https://www.trefis.com/stock/avgo/articles/627781/why-did-broadcom-stock-drop-on-friday/2026-11-23
  > Why Did Broadcom Stock Drop On Friday? Today’s big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Broadcom (AVGO) stock fell 12.2% on Friday, November 20, 2026, while the S&P 500 lost 3.7%. Anthropic buys custom AI chips from Broadcom, and Broadcom bought roughly 13 million Anthropic shares for $1 billion. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Mon 23 Nov | blockchain.news | Broadcom (AVGO) Stock Price Prediction: Support is holding for now, but trend damage still needs repair
  https://blockchain.news/news/20261123-price-prediction-avgo-support-is-holding-for-now-but
  > What happened and why it matters Broadcom (AVGO) is trying to recover after a violent reset in the shares. The latest print at $320.08 sits below the 7-day SMA of $331.96, the 20-day SMA of $328.18 and the 50-day SMA of $336.57, which tells you the stock has not yet reclaimed the near-term trend.
- Mon 23 Nov | Trefis | Is Broadcom Stock’s Drop A Chance To Buy?
  https://www.trefis.com/stock/avgo/articles/627646/is-broadcom-stocks-drop-a-chance-to-buy/2026-11-23
  > Is Broadcom Stock’s Drop A Chance To Buy? Today’s big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? Broadcom (AVGO) designs custom AI chips for a few large customers, such as Google, and that business may be what its bulls are betting on.
- Mon 23 Nov | Gotrade | Broadcom Stock (AVGO) Falls 12.2% on Reports of Google Cut (Nov 20)
  https://www.heygotrade.com/en/news/broadcom-avgo-stock-news-november-23-2026/
  > AI-powered contentSome parts of this article are powered by AI. Broadcom (AVGO) fell 12.19% to $304.41 on Friday, November 20, 2026, on volume of 60.1 million shares.
- Mon 23 Nov | BigGo Finance | Google Cuts Broadcom TPU Orders by a Million Units; MediaTek Seen Capturing the Shift, Goldman Sachs Trims Broadcom Price Target
  https://finance.biggo.com/news/2ae2d9ae-617c-4d3d-8a18-01c9472586f6
- Sun 22 Nov | Yahoo Finance | Here's What a $1,000 Investment in Broadcom Stock Could Be Worth By 2035
  https://finance.yahoo.com/markets/stocks/articles/heres-1-000-investment-broadcom-192202429.html
- Sun 22 Nov | Simply Wall St | Broadcom Stock Faces Google Order Cuts And AI Customer Concentration Risk
  https://simplywall.st/stocks/us/semiconductors/nasdaq-avgo/broadcom/news/broadcom-stock-faces-google-order-cuts-and-ai-customer-conce
- Sun 22 Nov | Investing.com India | Form 4 Broadcom Inc For: 22 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-broadcom-inc-for-22-november-93CH-5719820
## BRK.B  (8 leads)
- Mon 23 Nov | ad-hoc-news.de | Berkshire's AI Story Runs Through the Grid, Not the Trading Desk
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-s-ai-story-runs-through-the-grid-not-the-trading-desk/70545918
  > Berkshire Hathaway's most plausible route into the artificial intelligence boom may not involve buying a technology stock at all. It runs through the power plants, pipelines and utilities the conglomerate already owns — a thesis that has more to do with infrastructure economics than with any announced AI venture. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 23 Nov | The Motley Fool | Nvidia Just Reported Its First Quarter Without Jensen Huang. If the AI Trade Is Cracking, Warren Buffett’s Advice Comes Down to 1 Move.
  https://www.fool.com/investing/2026/11/23/nvidia-just-reported-its-first-quarter-without-jensen-huang-if-the-ai-trade-is-cracking-warren-buffett-s-advice-comes-down-to-1-move/
  > By Brett Schafer – - Nvidia just reported strong quarterly results, but investors are worried about the future with Jensen Huang gone. - Warren Buffett harps on avoiding complicated businesses like Nvidia for your portfolio. - Buffett survived for decades by avoiding the hottest stocks of the day, not buying them.
- Mon 23 Nov | Pluang | Berkshire Hathaway holds $360B in stocks, led b...
  https://pluang.com/en/news-feed/pengganti-warren-buffett-greg-abel-investasi-47-persen-portofolio-berkshire-tiga
  (page: did not load (403))
## WMT  (8 leads)
- Mon 23 Nov | Stocktwits | Michael Burry Names Apple, Costco And Walmart Early Crash Havens — The ‘Generals’ Fell Months After 2000 And 2007 Peaks
  https://stocktwits.com/news-articles/markets/equity/michael-burry-apple-costco-walmart-havens-generals-2000-2007-peaks/cNbYM9pR9Sk
  > With tech leaders now caught in the broader market slide, “The Big Short” investor Michael Burry is watching Apple (AAPL), Costco (COST) and Walmart (WMT) for a pattern that took six months to play out after the 2000 peak and seven to eight months after the 2007 peak.
- Mon 23 Nov | ad-hoc-news.de | Walmart stock: EUR 115.81, down 2.19% before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/walmart-stock-eur-115-81-down-2-19-before-xetra/70545834
  > Walmart stock traded at EUR 115.81 on Lang & Schwarz at 08:34 CET on Monday, November 23, 2026, 2.19% below the Xetra close of Friday, November 20, 2026, at EUR 118.40. Walmart reported fiscal third-quarter results on November 19, with revenue growth, stronger operating income and an upgraded annual outlook.
- Mon 23 Nov | JournalArta | Walmart Beats Estimates, Lifts Forecast, Extends Dividend Streak to 53 Years
  https://journalarta.com/en/2026/11/23/walmart-beats-estimates-extends-dividend-streak-53-years/
  > Walmart Beats Estimates, Lifts Forecast, Extends Dividend Streak to 53 Years Walmart topped Wall Street estimates on November 19 and raised its full-year forecast, yet its shares fell about 2% in early trading. The retailer has raised its dividend for 53 straight years, and its next payout goes to holders of record on December 11.
## V  (8 leads)
- Mon 23 Nov | MarketBeat | Equities Analysts Set Expectations for Visa FY2028 Earnings
  https://www.marketbeat.com/instant-alerts/estimates-equities-analysts-set-expectations-for-visa-fy2028-earnings-2026-11-23/
  > Equities Analysts Set Expectations for Visa FY2028 Earnings - Erste Group raised its FY2028 EPS estimate for Visa slightly to $17.13 from $17.11 and maintained a Buy rating. Analysts overall are bullish, with a consensus Buy rating and a $443.35 price target.
- Mon 23 Nov | scanx.trade | MobiKwik's Zaakpay integrates Visa Payment Passkey for OTP-free checkout
  https://scanx.trade/stock-market-news/companies/mobikwik-s-zaakpay-integrates-visa-payment-passkey-otp-free-checkout/56954547
  > MobiKwik's Zaakpay integrates Visa Payment Passkey for OTP-free checkout - Zaakpay integrates Visa Payment Passkey to enable device-based authentication without SMS OTPs - Merchant Payments GMV grew 76% YoY to ₹13,300 crore in Q2FY27 - Merchant Payments revenue increased 150% YoY, reflecting strong monetization
- Mon 23 Nov | FourWeekMBA | Visa Opens Agent Wallet to US Cards; Chase, Prepaid Excluded
  https://fourweekmba.com/ai-visa-opens-agent-wallet-to-us-cards-chase-prepaid-excluded/
  (page: did not load (403))
## ORCL  (8 leads)
- Mon 23 Nov | GuruFocus | Oracle (ORCL) Stock Valuation Shows 31.4% Upside Potential, Says Bernstein
  https://www.gurufocus.com/news/9214363/oracle-orcl-stock-valuation-shows-314-upside-potential-says-bernstein
  (page: did not load (403))
- Mon 23 Nov | theopenpress.in | Oracle OpenAI Deal: Oracle Says $300 Billion Contract Is Fully Funded
  https://theopenpress.in/article/oracle-openai-300-billion-fully-funded
  > Oracle has told investors that every dollar is in place for its roughly $300 billion contract with OpenAI, saying a final capital raise earlier this month has made it the first of the big cloud companies to be fully funded for the current AI investment cycle. Why Oracle had to speak up
- Mon 23 Nov | Blockchain News | Oracle (ORCL) Stock Price Prediction: Oracle slips below key averages as buyers test lower-band support
  https://blockchain.news/news/20261123-price-prediction-orcl-oracle-slips-below-key-averages-as
  > Price action and why it matters Oracle (ORCL) closed around $105.57 in the latest technical snapshot, down from an intraday range of $107.13 to $103.53 and still below the 7-day SMA at $108.98, the 20-day SMA at $116.63 and the 50-day SMA at $126.49.
- Mon 23 Nov | Trefis | Oracle Or The Fed: What Really Moves Nvidia Stock?
  https://www.trefis.com/stock/nvda/articles/627412/oracle-or-the-fed-what-really-moves-nvidia-stock/2026-11-23
  > Oracle Or The Fed: What Really Moves Nvidia Stock? Today’s big story: Reported SEC Probe: Could Nvidia Stock Fall To $92? One is what Oracle says about its AI spending. We checked which one has mattered more since September 1. How much of Nvidia’s daily swings each one explains, since September 1:
- Mon 23 Nov | MarketBeat | Oracle Stock Earnings Estimates Boosted by Erste Group Bank
  https://www.marketbeat.com/instant-alerts/estimates-oracle-stock-earnings-estimates-boosted-by-erste-group-bank-2026-11-23/
- Mon 23 Nov | ad-hoc-news.de | Oracle's AI Bill Is Paid; The Payback Is Still Three Years Out
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-s-ai-bill-is-paid-the-payback-is-still-three-years-out/70545409
- Mon 23 Nov | Investor's Business Daily | Dow Jones Futures Jump As Oracle, Korea Try To Ease Market Fears; Look For These Absolute Losers
  https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-worst-week-covid-nvidia-anthropic-vix-fear-gauge/
- Mon 23 Nov | Gotrade | Oracle Stock (ORCL) Falls 8.5% as AI Stocks Slide (Nov 20)
  https://www.heygotrade.com/en/news/oracle-orcl-stock-news-november-23-2026/
## COST  (8 leads)
- Mon 23 Nov | Stocktwits | Michael Burry Names Apple, Costco And Walmart Early Crash Havens — The ‘Generals’ Fell Months After 2000 And 2007 Peaks
  https://stocktwits.com/news-articles/markets/equity/michael-burry-apple-costco-walmart-havens-generals-2000-2007-peaks/cNbYM9pR9Sk
  > With tech leaders now caught in the broader market slide, “The Big Short” investor Michael Burry is watching Apple (AAPL), Costco (COST) and Walmart (WMT) for a pattern that took six months to play out after the 2000 peak and seven to eight months after the 2007 peak.
- Mon 23 Nov | JournalArta | Shopify, Costco, e.l.f: Full Details
  https://journalarta.com/en/2026/11/23/shopify-costco-elf-stocks-buy-if-market-crashes/
  > Shopify, Costco, e.l.f.: Why One Writer Would Buy in a Crash Motley Fool writer Jennifer Saibil says she would buy Shopify, Costco and e.l.f. Beauty if the S&P 500 sold off, citing fast sales growth but valuations of 53 to 75 times earnings. The index is up 7% this year.
- Sun 22 Nov | Yahoo Finance | Costco (COST) Lifts Dividend After Strong 2026 Results And $7.5 Billion 2027 Plan
  https://finance.yahoo.com/markets/stocks/articles/costco-cost-lifts-dividend-strong-180659480.html
  > - Costco Wholesale (NasdaqGS:COST) reported strong fiscal 2026 results, reinforcing management's confidence in the warehouse retailer's growth plans. - The board approved a higher regular dividend for shareholders, signalling a larger ongoing cash return from the business.
## NFLX  (8 leads)
- Mon 23 Nov | Blockchain News | Netflix (NFLX) Price Prediction: Oversold Setup Meets Heavy Overhead Resistance
  https://blockchain.news/news/20261123-price-prediction-nflx-oversold-setup-meets-heavy-overhead-resistance
  > Price action is stabilizing, but the trend is still down Netflix (NFLX) is trading at $57.48, essentially pinned near its pivot point of $57.42 and just above immediate support at $57.01.
- Mon 23 Nov | MarketBeat | Brokers Set Expectations for Netflix FY2027 Earnings
  https://www.marketbeat.com/instant-alerts/estimates-brokers-set-expectations-for-netflix-fy2027-earnings-2026-11-23/
  > Brokers Set Expectations for Netflix FY2027 Earnings - Erste Group trimmed its FY2027 EPS forecast for Netflix slightly, to $3.74 from $3.75; the article cites a current-year consensus estimate of $3.59.
- Mon 23 Nov | Trefis | What Will Move Netflix Stock Over Six Months?
  https://www.trefis.com/stock/nflx/articles/627584/what-will-move-netflix-stock-over-six-months/2026-11-23
  > What Will Move Netflix Stock Over Six Months? For questions about this article or underlying research, email help@trefis.com. Netflix (NFLX) stock closed at $56.73 on November 20, 2026, its lowest close in a year. The shares fell 15.4% over the past month, while the S&P 500 dropped 9.7%. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sun 22 Nov | Simply Wall St | Netflix (NFLX) Stock Could Be 34% Undervalued Despite Ad Guidance Cuts
  https://simplywall.st/stocks/us/media/nasdaq-nflx/netflix/news/netflix-nflx-stock-could-be-34-undervalued-despite-ad-guidan
  > Netflix has seen its share price fall sharply over the past year, which puts a fresh spotlight on whether the current US$56.73 level is still in line with the cash it can generate for shareholders.
- Sun 22 Nov | BigGo Finance | Netflix Stock Split Halves Price: Burry Eyes $39 Entry as Ackman Adds $1.07 Billion
  https://finance.biggo.com/news/9b571bcb-c01d-45ce-8b7f-6ffa17379d2b
- Sun 22 Nov | TheStreet | Michael Burry’s Netflix warning puts investors in a $39 dilemma
  https://www.thestreet.com/entertainment/michael-burrys-netflix-warning-puts-investors-in-a-39-dilemma
- Sun 22 Nov | Yahoo Finance | What's Going On With Netflix's Stock?
  https://finance.yahoo.com/markets/stocks/articles/whats-going-netflixs-stock-172002682.html
- Sun 22 Nov | Investing.com Australia | Form 4 Netflix Inc For: 22 November By Investing.com
  https://au.investing.com/news/stock-market-news/form-4-netflix-inc-for-22-november-93CH-4788604
## INTC  (8 leads)
- Mon 23 Nov | blockchain.news | Intel (INTC) Stock Price Prediction: Weak post-earnings setup meets analyst target resets
  https://blockchain.news/news/20261123-price-prediction-target-intc-weak-post-earnings-setup-meets-analyst
  > Post-earnings pressure still defines the tape Intel’s latest read-through remains dominated by its October 29 third-quarter report and the weaker fourth-quarter outlook that followed.
- Sun 22 Nov | Simply Wall St | Intel (INTC) Chip Breakthrough Opens A Fresh Angle On Its AI Push
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-intc-chip-breakthrough-opens-a-fresh-angle-on-its-ai-p
  > Intel (NasdaqGS:INTC) announced a significant semiconductor manufacturing breakthrough, signaling progress in its chip process technology roadmap. The company also disclosed a new client partnership with RadixArk focused on open-source AI inference tuned for Intel hardware. RadixArk plans to optimize and distribute AI inference frameworks that are designed to run efficiently on Intel CPUs and accelerators.
- Sun 22 Nov | Yahoo Finance | Intel Just Landed Its First 18A-P Chip Customer. What That Means for INTC Stock.
  https://finance.yahoo.com/markets/stocks/articles/intel-just-landed-first-18a-193003252.html
  > Intel (INTC) has long been a prominent name in the semiconductor industry, supplying processors for personal computers and data centers. Its stock, however, has had a difficult run, losing more than half its value since the end of September.
- Sun 22 Nov | TradingKey | Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100
  https://www.tradingkey.com/analysis/stocks/us-stocks/262088803-intel-intc-q2-2026-earnings-data-center-ai-foundry-loss-tradingkey
  > Intel Q2 2026: Revenue Up 25%, Data Center +59%, Stock Surges Then Retreats to $100 Intel’s Q2 2026 results reflect a significant turnaround, highlighted by a 25% revenue increase and 59% growth in Data Center and AI segments.
- Sun 22 Nov | International Business Times Australia | Will Intel Stock Bounce Back? Chipmaker Faces Worst Two-Month Plunge on Record as the PC Slump Deepens
  https://www.ibtimes.com.au/intel-shares-plunge-weak-pc-outlook-1879169
- Sun 22 Nov | FinanceFeeds | Intel Stock $51: HP and Dell Results Test PC Demand Tuesday
  https://financefeeds.com/intel-intc-stock-51-sunday-week-ahead-hp-dell-results-thanksgiving-bull-56-bear-48/
- Sun 22 Nov | MarketBeat | 73,760 Shares of Intel Corporation $INTC Acquired by N.F.U. MUTUAL UNIT MANAGERS Ltd
  https://www.marketbeat.com/instant-alerts/filing-73760-shares-of-intel-corporation-intc-acquired-by-nfu-mutual-unit-managers-ltd-2026-11-22/
- Sun 22 Nov | MarketBeat | Intel Corporation $INTC Stake Lessened by BRITISH COLUMBIA INVESTMENT MANAGEMENT Corp
  https://www.marketbeat.com/instant-alerts/filing-intel-corporation-intc-stake-lessened-by-british-columbia-investment-management-corp-2026-11-22/
## LLY  (8 leads)
- Mon 23 Nov | https://hrtoday.in/ | Eli Lilly and Company Appoints Michael Kopach as Vice President
  https://hrtoday.in/eli-lilly-and-company-appoints-michael-kopach-as-vice-president/
  (page: did not load (403))
- Sun 22 Nov | Barchart.com | Eli Lilly's Next Obesity Drug Isn't Approved Yet, but Peptide Tracker Users Already Log It
  https://www.barchart.com/story/news/8957887/eli-lilly-s-next-obesity-drug-isn-t-approved-yet-but-peptide-tracker-users-already-log-it
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | JournalArta | Eli Lilly’s Next Weight-Loss Drug Shows 54.1-Pound Loss
  https://journalarta.com/en/2026/11/23/eli-lilly-next-weight-loss-drug-trial-results/
  > Eli Lilly’s Next Weight-Loss Drug Shows 54.1-Pound Loss Eli Lilly’s experimental EloraTZP produced average weight loss of up to 54.1 pounds in an early-stage trial of people with obesity and Type 2 diabetes.
Read 93 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ETEL, ALCN, EFIH, EMFD, AMOC, SKPC.
