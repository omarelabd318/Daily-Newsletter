# Desk brief, Sunday, November 22, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 27s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-20 (35.89); Treasury yields to 2026-11-20 (10-year 4.92%).
- **valuation**: ok in 25s (GitHub Actions). LLY: $1.27tn, P/E (last 12 months) 42.2, Forecast P/E (fiscal 2026) 37.8 (the four quarters to Sep 2026)
- **movers**: ok in 21s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 turning down, RSI 49.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.1%, median P/E 10.0; cheapest MASR +74%, PHAR +48%, MFPC +43%; dearest ARAB -62%, MOIN -65%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 63s (GitHub Actions). 
- **news**: ok in 90s (GitHub Actions). 
- **leads**: ok in 77s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 6 needed a retry.

## What moved (latest close against the one before)
- EGX30 51,458.00 (-0.17%); EGX70 EWI 17,505.80 (-0.33%); USD/EGP 53.88 (+0.12%); Gold 21K 5,510.00 (+0.92%); Brent 92.57 (+0.64%); S&P 500 6,910.39 (-3.70%); Nasdaq 22,617.73 (-5.28%); Bitcoin 59,051.00 (+2.10%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): NVDA -14.0%, AVGO -12.2%, ORCL -8.5%, INTC -8.0%, TSLA -7.6%, META -5.9%, AMZN -4.1%, ETEL -3.5%, JPM -3.0%.
- Trend and momentum worth a mention (description only, never a reason on its own):
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
EGX: 2026-11-19 (TradingView's closes; Mubasher's list refused), 200 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (212)
US: 2026-11-20, 807 companies
US week and month: US companies worth $10bn or more (805)
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
- Sat 21 Nov | Yahoo! Finance Canada | Global Payments Inc. (GPN) Stock Forecasts
  https://ca.finance.yahoo.com/research/reports/MS_0P000002G8_AnalystReport_1795207236000
- Sat 21 Nov | Crain's Chicago Business | GTCR weighs $50 billion Global Payments buyout
  https://www.chicagobusiness.com/banking-finance/ccb-gtcr-global-payments-buyout-20261120/
- Fri 20 Nov | BigGo Finance | Global Payments Jumps 10% as Largest Holder GTCR Weighs $50 Billion Buyout
  https://finance.biggo.com/news/38051972-b0a9-43b9-b885-307db6a86767
## BIP +4.5%  Brookfield Infrastructure Partners L.P
- Sat 21 Nov | Yahoo Finance Australia | Brookfield Infrastructure Partners L.P. (BIP) stock price, news, quote and history
  https://au.finance.yahoo.com/quote/BIP/
- Sat 21 Nov | Yahoo! Finance Canada | Brookfield Infrastructure Corporation (BIPC.TO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BIPC.TO/
- Sat 21 Nov | Yahoo! Finance Canada | Brookfield Infrastructure Partners L.P. (BIP-PB) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BIP-PB/
- Sat 21 Nov | Yahoo! Finance Canada | Brookfield Infrastructure Partners L.P. (BIP) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BIP/
## RKT +4.2%  Rocket Companies
- Sat 21 Nov | Yahoo! Finance Canada | Rocket Companies, Inc. (RKT) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance Singapore | Rocket Companies, Inc. (RKT) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/RKT/
- Sat 21 Nov | Yahoo Finance | Rocket Companies (RKT) Just Got a Major Win — Wall Street Is Reacting
  https://finance.yahoo.com/markets/stocks/articles/rocket-companies-rkt-just-got-071103140.html
- Sat 21 Nov | GuruFocus | Rocket Companies Inc (RKT) Shares Surge 4.2% -- What GF Score of 65 Tells Investors
  https://www.gurufocus.com/news/9213506/rocket-companies-inc-rkt-shares-surge-42-what-gf-score-of-65-tells-investors
## MKC.V +3.8%  McCormick & Company, Incorporated
- Sat 21 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Stock Breaks Above 50 Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-stock-breaks-above-50-day-moving-average-whats-next-2026-11-21/
- Fri 20 Nov | kalkine.ca | McCormick & Company Incorporated (NYSE: MKC.V) Stock Price, News & Analysis
  https://kalkine.ca/company/nyse-mkc-v/
- Fri 20 Nov | MarketBeat | McCormick & Company, Incorporated (NYSE:MKC) Shares Climb 4.8% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-mccormick-company-incorporated-nyse-mkc-shares-climb-48-heres-why-2026-11-20/
- Thu 19 Nov | Yahoo Finance | Do Wall Street Analysts Like McCormick & Company Stock?
  https://finance.yahoo.com/markets/stocks/articles/wall-street-analysts-mccormick-company-121725694.html
## GIS +3.7%  General Mills
- Sat 21 Nov | Investing.com Australia | Form 4 General Mills: Elizabeth Mascolo (Segment President) For: 17 November
  https://au.investing.com/news/stock-market-news/form-4-general-mills-elizabeth-mascolo-segment-president-for-17-november-93CH-4788290
- Sat 21 Nov | The Motley Fool | Here's How Much $2,500 in General Mills Stock Could Pay You in Dividends in 2027
  https://www.fool.com/investing/2026/11/21/here-s-how-much-usd2-500-in-general-mills-stock-could-pay-you-in-dividends-in-2027/
- Sat 21 Nov | Yahoo! Finance Canada | General Mills, Inc. (GIS) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/GIS/
- Sat 21 Nov | Insider Monkey | General Mills (GIS) is Suddenly Drawing Wall Street’s Attention
  https://www.insidermonkey.com/news/general-mills-gis-is-suddenly-drawing-wall-streets-attention-1868407/
## NBIS -16.1%  Nebius Group
- Sun 22 Nov | Simply Wall St | Nebius Group (NBIS) Stock Still Looks Cheap After a 49% Slide
  https://simplywall.st/stocks/us/software/nasdaq-nbis/nebius-group/news/nebius-group-nbis-stock-still-looks-cheap-after-a-49-slide
- Sat 21 Nov | SSBCrack | Nebius Group N.V. Ranked 7th Among the 10 Most Overvalued AI Stocks According to Short Sellers
  https://news.ssbcrack.com/nebius-group-n-v-ranked-7th-among-the-10-most-overvalued-ai-stocks-according-to-short-sellers/
- Sat 21 Nov | Pluang | Nebius shares drop 40% despite strong growth; $...
  https://pluang.com/en/news-feed/investasi-500-bulan-nebius-pensiun-jutawan
- Sat 21 Nov | The Motley Fool | Could Investing $500 a Month in Nebius Help You Retire a Millionaire?
  https://www.fool.com/investing/2026/11/21/could-investing-500-a-month-in-nebius-help-you-retire-a-millionaire/
## CLS -16.1%  Celestica
- Fri 20 Nov | MarketBeat | Celestica (NYSE:CLS) Stock Price Down 16.3% - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-celestica-nyse-cls-stock-price-down-163-time-to-sell-2026-11-20/
- Fri 20 Nov | Global Banking & Finance Review | Celestica falls 16.38% in Friday's session
  https://www.globalbankingandfinance.com/celestica-cls-to-falls-2026-11-20/
- Fri 20 Nov | GuruFocus | Celestica (CLS) Shares Drop 15% Amid Tech Selloff on November 20, 2026
  https://www.gurufocus.com/news/9213149/celestica-cls-shares-drop-15-amid-tech-selloff-on-november-20-2026
- Fri 20 Nov | Seeking Alpha | Celestica drops 15% amid broad tech selloff (CLS:NYSE)
  https://seekingalpha.com/news/4675283-celestica-drops-15-percent-amid-broad-tech-selloff
## SNDK -16.1%  Sandisk
- Sun 22 Nov | FinanceFeeds | Sandisk Stock $79.24: Dell and HP Report Tuesday
  https://financefeeds.com/sandisk-sndk-stock-79-sunday-week-ahead-dell-hp-results-24-november-bull-88-bear-70/
- Sun 22 Nov | shattered.io | Huang Exit: 3 Flash Sale AI Stocks, Sandisk 60% Off High
  https://shattered.io/huang-resignation-flash-sale-3-ai-stocks-sandisk-amd-silicon-motion/
- Sat 21 Nov | MarketWatch | Micron and Sandisk stocks might look like bargains, but analysts say that’s actually a red flag
  https://www.marketwatch.com/story/micron-and-sandisk-stocks-might-look-like-bargains-but-analysts-say-thats-actually-a-red-flag-da1f1f5d
- Sat 21 Nov | ad-hoc-news.de | Sandisk stock completes split as adjusted trading begins
  https://www.ad-hoc-news.de/boerse/news/corporate-news/sandisk-stock-completes-split-as-adjusted-trading-begins/70542155
## BE -15.3%  Bloom Energy
- Sun 22 Nov | Pluang | Bloom Energy's stock drops despite doubling rev...
  https://pluang.com/en/news-feed/haruskah-anda-investasi-1000-dolar-di-bloom-energy-sekarang-2
- Sun 22 Nov | Yahoo Finance | Should You Invest $1,000 in Bloom Energy Right Now?
  https://finance.yahoo.com/markets/stocks/articles/invest-1-000-bloom-energy-005002138.html
- Sat 21 Nov | TIKR.com | Bloom Energy Sinks 26% in a Week, Vertiv Down 18%, as Nvidia’s Turmoil Hits AI Power Stocks. Time to Buy?
  https://www.tikr.com/blog/bloom-energy-sinks-26-in-a-week-vertiv-down-18-as-nvidias-turmoil-hits-ai-power-stocks-time-to-buy?ref=yahoofinance&tlnk=yf-261121-fv95h3w4
- Sat 21 Nov | Kalkine Media | Can Bloom Energy (NYSE:BE) Turn Data Center Demand Into Lasting Growth?
  https://kalkinemedia.com/us/stocks/energy/can-bloom-energy-nysebe-turn-data-center-demand-into-lasting-growth
## CRDO -15.2%  Credo Technology Group Holding
- Sat 21 Nov | Benzinga | Benzinga Bulls and Bears: Nvidia, Credo, Red Cat
  https://www.benzinga.com/markets/market-summary/26/11/63515125/benzinga-bulls-and-bears-nvidia-credo-red-cat
- Sat 21 Nov | GuruFocus | Credo Technology Group Holding Ltd (CRDO) Stock Down 15.2% -- No
  https://www.gurufocus.com/news/9213649/credo-technology-group-holding-ltd-crdo-stock-down-152-now-undervalued-gf-score-75100
- Fri 20 Nov | GuruFocus | Credo Technology Group (CRDO) Shares Plunge Nearly 14% Amid Tech Sector Sell-Off
  https://www.gurufocus.com/news/9213209/credo-technology-group-crdo-shares-plunge-nearly-14-amid-tech-sector-selloff
- Fri 20 Nov | TradingView | onsemi, Nova, Power Integrations, Credo Technology Group Holding, and Navitas Semiconductor shares plummet, what you need to know
  https://www.tradingview.com/news/stockstory:335186cea094b:0-onsemi-nova-power-integrations-credo-technology-group-holding-and-navitas-semiconductor-shares-plummet-what-you-need-to-know/
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
    Views: nothing to change.

## Fair value
- Changed since the last run: nothing by 10 points or more.
- In the ten cheapest or dearest with no note: ADIB, MCQE, CSAG, MTIE, AMOC, LCSW, AMIA, BINV.

## Due today
- Light run (no session since Saturday's desk): carry both sections over, update only news, the week ahead and views due; no movers' reasons; side sessions only if there is work for them.
- Sunday: write the desk's note for two more stocks (16 still without one; next: GOOGL, AVGO), and read the whole fair-value table for figures that cannot be right.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 3 days, 2026-11-22. Open each story before using it.
## COMI  (8 leads)
- Sat 21 Nov | الجريدة العقارية | أفضل شهادتي ادخار في البنك التجاري الدولي CIB خلال نوفمبر 2026.. العائد يصل إلى 20.50%
  https://www.aleqaria.com.eg/post/details/358976/أفضل-شهادتي-ادخار-في-البنك-التجاري-الدولي-cib-خلال-نوفمبر-2026..-العائد-يصل-إلى-20.50
  > تتصدر شهادات الادخار اهتمامات أصحاب المدخرات الراغبين في تحقيق عائد مناسب على أموالهم، خاصة مع استمرار البنوك في تقديم أوعية ادخارية متنوعة من حيث أسعار الفائدة ومدد الاستثمار ودوريات صرف العائد.
- Sat 21 Nov | بنكي | بطاقة وورلد (World) الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/410
  > - معدل الفائدة السنوي الفعلي 24 عرض ساري على البطاقة تقسيط بدون فوائد 13 · خصومات 12 · 11 بينتهوا خلال أيام - تقسيط المشتريات لمدة 12 شهرًا بدون فوائد Audio Technology شرف دي جي - تقسيط بدون فوائد + خصم حتى 25% Bosch بوش - خصم 10% DALYDRESS دالى دريس
- Sat 21 Nov | شبكة تواصل الإخبارية | قبل ما تغير فلوسك.. أسعار الدولار اليوم في البنك الأهلي وبنك مصر وCIB
  https://twaslnews1.twaslnews.com/8049002/
  (page: did not load (403))
## TMGH  (3 leads)
- Sat 21 Nov | إيجبتكِ | النائب عبدالرحمن بشاري يبحث مع هشام طلعت مصطفى أولوية توظيف أبناء الأقصر
  https://www.egyptke.com/305151
  > النائب عبدالرحمن بشاري يبحث مع هشام طلعت مصطفى أولوية توظيف أبناء الأقصر النائب عبدالرحمن بشاري يبحث مع هشام طلعت مصطفى أولوية توظيف أبناء الأقصر بفندق فور سيزونز ودعم مشروعات التنمية بالمحافظة التقى النائب عبدالرحمن بشاري عضو مجلس النواب  برجل الأعمال هشام طلعت مصطفى، لفتح ملف أولوية التوظيف لأبناء محافظة الأقصر بفندق فور سيزونز
- Sat 21 Nov | اليوم السابع | فى سوق المشتقات.. الكبار يراهنون على أسعار "طلعت مصطفى" وCIB حتى 2027
  https://www.youm7.com/story/2026/11/21/فى-سوق-المشتقات-الكبار-يراهنون-على-أسعار-طلعت-مصطفى-وCIB/7625715
  > سجلت تداولات سوق المشتقات المالية في البورصة المصرية قيمة إجمالية بلغت 9.374 مليون جنيه خلال الأسبوع، من خلال تنفيذ 60 عملية، على كمية متداولة بلغت 642 عقدًا، وفقًا للتقرير الأسبوعي الخاص بالمشتقات المالية.
- Thu 19 Nov | مجلة البوصلة الاقتصادية | تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم
  https://alboslanews.com/أسواق-مال/تراجع-العقود-المستقبلية-لـ-egx30-وطلعت-مصطفى-هامشيًا-وانخفاض-البنك-التجاري-الدولي-بنسب-تتخطى-1-اليوم-431143
  > تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم الخميس 19 نوفمبر 2026 -03:56
## ETEL  (3 leads)
- Fri 20 Nov | المصري اليوم | الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026.. الرابط والخطوات وطرق السداد
  https://www.almasryalyoum.com/news/details/4415474
  > الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026.. الرابط والخطوات وطرق السداد يتزايد اهتمام عملاء الشركة المصرية للاتصالات WE بالبحث عن طريقة الاستعلام عن فاتورة النت WE برقم التليفون الأرضي 2026، لمعرفة قيمة الاشتراك الشهري ومتابعة موعد التجديد، وتجنب انقطاع خدمة الإنترنت المنزلي نتيجة التأخر في سداد المستحقات.
- Thu 19 Nov | Masrawy | المصرية للاتصالات يهزم الترسانة في عقر داره ويرتقي بجدول الترتيب
  https://www.masrawy.com/sports/sports_news/details/2026/11/19/3081357/المصرية-للاتصالات-يهزم-الترسانة-في-عقر-داره-ويرتقي-بجدول-الترتيب
  > حقق فريق المصرية للاتصالات (وي) فوزًا مهمًا على حساب منافسه الترسانة بنتيجة 2-1، في المباراة التي جمعت الفريقين اليوم الخميس، ضمن منافسات الجولة الثالثة عشرة من دوري المحترفين المصري.
- Thu 19 Nov | بوابة مولانا | المصرية للاتصالات توقع اتفاقية تعاون مع نيفيرا
  https://mwlana.com/details/328560/
  > وقّع المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، والمهندس عبد الخالق عواد، الرئيس التنفيذي للشؤون العقارية بشركة «نيفيرا»، اتفاقية تعاون تتولى بموجبها المصرية للاتصالات دور شريك الاتصالات والتكنولوجيا للمشروع، وذلك بحضور الدكتور مصطفى مدبولي، رئيس مجلس الوزراء.
## PHDC  (2 leads)
- Sat 21 Nov | نيوز رووم | سمسار عقارات يحرر محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» بسبب تلفيات بسيارته في أكتوبر أول
  https://www.newsroom.info/487470
  > سمسار عقارات يحرر محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» بسبب تلفيات بسيارته في أكتوبر أول حرر سمسار عقارات محضرًا ضد القائمين على إدارة كمبوند «بي إكس بالم هيلز» تحت الإنشاء، بسبب تعرض سيارته لتلفيات أثناء تواجده بالكمبوند، واتهمهم بالإهمال، وتحرر محضر بالواقعة.
- Thu 19 Nov | Masrawy | من فيلا بالم هيلز إلى عصابة الشرطة المزيفة ضربتان أمنيتان بأكتوبر
  https://www.masrawy.com/news/news_cases/details/2026/11/19/3081493/من-فيلا-بالم-هيلز-إلى-عصابة-الشرطة-المزيفة-ضربتان-أمنيتان-بأكتوبر
  > تسلل في الظلام من فيلا تحت الإنشاء، وكمين مفاجئ بـ30 ألف جنيه قدام نادي الصيد، خيطان لوقعتين مختلفتين في قسم أول أكتوبر، لكن كاميرات المراقبة والتحريات جمعتهم في نقطة واحدة: سقوط المتهمين. قفزة داخل بالم هيلز ومع تتبع الملابسات ومواجهة المتهم، اتضح أنه كان يتردد على منطقة بالم هيلز بحكم طبيعة عمله؛
## SWDY  (2 leads)
- Thu 19 Nov | جريدة باور نيوز الاخبارية | أحمد السويدي يلتقي رئيس شركة Gonvarri Industries في مدريد لبحث شراكات استراتيجية بقطاعي الطاقة والبنية التحتية
  https://powernews.cc/?p=294462
  > عقد المهندس أحمد السويدي، الرئيس التنفيذي لمجموعة السويدي إليكتريك، اجتماعًا مع السيد جون ريبيراس، رئيس مجلس الإدارة التنفيذي لشركة Gonvarri Industries، بمقر الشركة في العاصمة الإسبانية مدريد، بحضور السيد نيستور لاكارا، مدير الاستراتيجية، وعدد من أعضاء فريق القيادة بالشركة.
- Thu 19 Nov | بوابة روز اليوسف | "السويدي الوطنية" تستعرض خطة 2027–2028 لزيادة الإنتاج والتوسع في إفريقيا والشرق الأوسط
  https://www.rosaelyoussef.com/1452967
  (page: did not load (403))
## ORAS  (8 leads)
- Fri 20 Nov | SaudiGulf Projects | Orascom Construction Backlog Rises to $11.6 Billion in Q3 2026
  https://www.saudigulfprojects.com/2026/11/orascom-construction-q3-2026-results-11-6-billion-backlog/
  (page: did not load (403))
- Fri 20 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تبدأ تشييد واحدة من أكبر محطات تحلية المياه عالمياً في الأردن
  https://cnnbusinessarabic.com/finance-markets/1152977/أوراسكوم-كونستراكشون-تبدأ-تشييد-واحدة-من-أكبر-محطات-تحلية-المياه-عالميا-في-الأردن
  > «أوراسكوم كونستراكشون» تبدأ تشييد واحدة من أكبر محطات تحلية المياه عالمياً في الأردن تاريخ النشر: قبل يومين أعلنت شركة «أوراسكوم كونستراكشون» وضع حجر الأساس لمشروع تحلية ونقل المياه من العقبة إلى عمّان في الأردن، وهو مشروع ضخم يتضمن إنشاء واحدة من أكبر محطات تحلية المياه على مستوى العالم.
- Thu 19 Nov | Water Tech Online | Orascom Construction breaks ground on Jordan desalination and conveyance project
  https://www.watertechonline.com/news-reports/news/55420378/orascom-construction-breaks-ground-on-jordan-desalination-and-conveyance-project
  (page: only 62 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## FWRY  (6 leads)
- Sat 21 Nov | بوابة التكنولوجيا المالية | الرئيس التنفيذي المشارك لشركة «CLOUD11»: «فوري» و«إنستاباي» أحدثتا تغييرات جوهرية في سوق المدفوعات المصري
  https://fintechgate.net/258082
  > الرئيس التنفيذي المشارك لشركة «CLOUD11»: «فوري» و«إنستاباي» أحدثتا تغييرات جوهرية في سوق المدفوعات المصري
- Fri 20 Nov | بوابة التكنولوجيا المالية | تقريرلـ «AfricaNenda» : أفريقيا بها أكثر من 39 نظاما للمدفوعات الفورية تغطي 43 دولة
  https://fintechgate.net/258034
  > 1.8 تريليون دولار قيمة المدفوعات الفورية في أفريقيا خلال 2025 عبر 71.4 مليار معاملة تقريرلـ «AfricaNenda» : أفريقيا بها أكثر من 39 نظاما للمدفوعات الفورية تغطي 43 دولة
- Thu 19 Nov | السودان اليوم | نقلة جديدة في المعاملات المالية.. السودان يتجه نحو الدفع الفوري
  https://alsudantoday.com/business/economic-news/568347
  (page: did not load (403))
- Thu 19 Nov | بوابة المصرف | 10 بروتوكولات لتحديث التجارة الخارجية.. فوري وفيزا ومايكروسوفت ضمن الشركاء
  https://www.almasraf.news/10-بروتوكولات-لتحديث-التجارة-الخارجية/
  > وقّع المختبر التنظيمي ومركز الابتكار لتكنولوجيا التجارة (TradeTech Sandbox) 10 بروتوكولات تعاون مع مؤسسات وشركات مصرية ودولية، لتسريع تحديث التجارة الخارجية وتطوير حلول رقمية تستهدف تقليل الوقت والتكلفة المرتبطين بالإجراءات التجارية. وتضم الشراكات شركات متخصصة في التكنولوجيا والاتصالات والمدفوعات والخدمات المالية، من بينها فوري وفيزا ومايكروسوفت. 10 بروتوكولات تجمع شركات التكنولوجيا والمدفوعات لتطوير التجارة
- Thu 19 Nov | آراب فاينانس | فوري وفيزا ومايكروسوفت ضمن 10 جهات تتعاون مع الحكومة لتطوير التجارة الخارجية
  http://www.arabfinance.com/ar/news/newdetails/فوري-وفيزا-ومايكروسوفت
- Thu 19 Nov | شبكة تواصل الإخبارية | «اتصالات» و«فوري» و«فيزا» ضمن 10 جهات تشارك في مختبر تكنولوجيا التجارة
  https://twaslnews1.twaslnews.com/7954189/
## ABUK  (1 leads)
- Thu 19 Nov | لحظات نيوز | العربية للتصنيع توقع اتفاقا لبناء محطات طاقة شمسية لشركة أبوقير للأسمدة
  https://nl7za.com/economy/العربية-للتصنيع-توقع-اتفاقا-لبناء-محطات-طاقة-شمسية
  > وقعت الهيئة العربية للتصنيع عقدا استراتيجيا موسعا مع شركة أبوقير للأسمدة والصناعات الكيماوية لتنفيذ منظومة متكاملة من محطات توليد الطاقة الكهربائية النظيفة باستخدام الخلايا الشمسية بقدرات تشغيلية عالية، ويهدف المشروع الصناعي الضخم إلى تزويد المجمعات الإنتاجية للشركة بالطاقة المتجددة وخفض تكاليف التشغيل وترشيد استهلاك الوقود التقليدي بما يتوافق مع المعايير البيئية العالمية والتنمية المستدامة للدولة ...
## HRHO  (2 leads)
- Sat 21 Nov | موقع ليالينا | من شانيل إلى هيرميس: جولة داخل مجموعة حقائب كيندال جينر
  https://www.layalina.com/من-شانيل-إلى-هيرميس-جولة-داخل-مجموعة-حقائب-كيندال-جينر-896577.html
  (page: only 41 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | الأسبوع | الأسهم الكبري تقود المشهد.. «هيرميس» تتوقع صعود البورصة المصرية بنسبة تصل لـ30% خلال 2027
  https://www.elaosboa.com/3029241/
  > الأسهم الكبري تقود المشهد.. «هيرميس» تتوقع صعود البورصة المصرية بنسبة تصل لـ30% خلال 2027 [Figures on the page: unaudited or preliminary; first half; one quarter. Check which one each figure is.]
## JUFO  (2 leads)
- Sun 22 Nov | مصر الآن | صيانة كهرباء مرتقبة في جهينة وطهطا اليوم.. فصل 20 مغذيًا لمدة 5 ساعات
  https://misrelaan.com/article/143767/صيانة-كهرباء-مرتقبة-في-جهينة-وطهطا-اليوم
  > صيانة كهرباء مرتقبة في جهينة وطهطا اليوم.. فصل 20 مغذيًا لمدة 5 ساعات من المقرر فصل التيار الكهربائي، اليوم الأحد 22 نوفمبر، عن مناطق ومحطات خدمية في مركزي جهينة وطهطا بمحافظة سوهاج، من العاشرة صباحًا حتى الثالثة عصرًا، لتنفيذ الصيانة المبرمجة بلوحة توزيع جهينة «2» في نزلة علي.
- Thu 19 Nov | مستقبل وطن نيوز | «كُحل الجبل» يوثق بطولة أبناء جهينة في مواجهة الحملة الفرنسية بالمهرجان القومي للمسرح المدرسي
  https://www.mwatan.news/1040342
  (page: did not load (403))
## EAST  (1 leads)
- Sat 21 Nov | شبكة تواصل الإخبارية | طائرة الزمالك تواصل الانتصارات.. ثلاثية نظيفة أمام إيسترن كومباني
  https://twaslnews1.twaslnews.com/8090062/
  (page: did not load (403))
## EMFD  (1 leads)
- Thu 19 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس
  https://www.osoulmisrmagazine.com/452994
  > الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس تباين أداء أسهم الشركات العقارية المقيدة بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الخميس، إذ ارتفعت أسعار أسهم 4 شركات، مقابل تراجع أسهم 4 شركات، بينما استقر سهما مصر الجديدة للإسكان والتعمير والمطورون العرب القابضة دون تغيير.
## BQDC  (8 leads)
- Sun 22 Nov | شبكة تواصل الإخبارية | المدعى عليهم: أردنيون.. أقامها: بنك القاهرة عمان (أسماء)
  https://twaslnews1.twaslnews.com/8101475/
  (page: did not load (403))
- Sat 21 Nov | بوابة الأهرام | صندوق النقد يشيد بأداء السياسة النقدية وقوة القطاع المصرفى المصرى.. نجاح طرح بنك القاهرة يعزز الثقة فى الاقتصاد مع الإسراع ببرنامج الطروحات
  https://www.ahram.org.eg/Daily/News/205779/117/1036465/الأحد-الأقتصادي/صندوق-النقد-يشيد-بأداء-السياسة-النقدية-وقوة-القطاع.aspx
  (page: did not load (403))
- Sat 21 Nov | بوابة المصرف | 100 مليون دولار مقابل 7% من بنك القاهرة.. وخطة لمضاعفة العملاء
  https://www.almasraf.news/100-مليون-دولار-مقابل-7-من-بنك-القاهرة-وخطة/
  > استثمرت مؤسسة التمويل الدولية (IFC)، التابعة لمجموعة البنك الدولي، 100 مليون دولار في الطرح العام الأولي لبنك القاهرة بالبورصة المصرية، مقابل حصة تقارب 7% من رأسمال البنك، في صفقة تعكس اهتمام المؤسسات المالية الدولية بالقطاع المصرفي المصري، وتدعم خطط البنك لتوسيع خدمات التمويل للشركات والأفراد خلال السنوات المقبلة.
## EFID  (2 leads)
- Thu 19 Nov | Investing.com | Earnings call transcript: Edita Food posts record Q3 2026 revenue, shares rise
  https://www.investing.com/news/transcripts/earnings-call-transcript-edita-food-posts-record-q3-2026-revenue-shares-rise-93CH-5039005
  (page: did not load (403))
- Thu 19 Nov | TradingView | Edita Food Industries Company Q3 2026 Earnings Call Is Live
  https://www.tradingview.com/news/urn:live_audio:quartr.com:800175:0-edita-food-industries-company-q3-2026-earnings-call-is-live/
  > Edita Food Industries Company Q3 2026 Earnings Call Is Live Edita Food Industries Company's quarterly earnings call has just begun.
## AAPL  (8 leads)
- Sat 21 Nov | Barchart.com | Apple Is Now Worth Over $5 Trillion Without Betting Big on AI Data Centers. AAPL Stock Now Trades Near Wall Street’s Targets.
  https://www.barchart.com/story/news/8950358/apple-is-now-worth-over-5-trillion-without-betting-big-on-ai-data-centers-aapl-stock-now-trades-near-wall-streets-targets
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | TradingKey | Apple Stock Forecast: Apple Posted $111.2B Revenue, So Why Did AAPL Fall After WWDC?
  https://www.tradingkey.com/analysis/stocks/us-stocks/261955127-apple-stock-forecast-apple-posted-111-2b-revenue-so-why-did-aapl-fall-after-wwdc-tradingkey
  > Apple Stock Forecast: Apple Posted $111.2B Revenue, So Why Did AAPL Fall After WWDC? Apple's stock pullback post-WWDC 2026 is attributed to a "buy the rumor, sell the news" sentiment, as key Apple Intelligence features are deferred to late 2026 or 2027, aligning with the iPhone 18 launch.
- Sat 21 Nov | Seeking Alpha | Apple: Shows Us How To Win Without Joining The AI Bubble
  https://seekingalpha.com/article/4970798-apple-shows-us-how-to-win-without-joining-the-ai-bubble
  (page: did not load (403))
## MSFT  (8 leads)
- Sun 22 Nov | Simply Wall St | Is Akamai Technologies (AKAM) Undervalued After $14b In Deals And A Microsoft Tie Up?
  https://simplywall.st/stocks/us/software/nasdaq-akam/akamai-technologies/news/is-akamai-technologies-akam-undervalued-after-14b-in-deals-a
  > Akamai Technologies (AKAM) is back in focus after management reported signing US$14b of large deals this year and highlighted power constraints that are limiting some AI infrastructure projects, even as new products and partnerships roll out.
- Sun 22 Nov | Simply Wall St | Microsoft (MSFT) Launches Life Sciences AI Alliance For Smart Lab Instruments
  https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-launches-life-sciences-ai-alliance-for-smart
  > Microsoft (NasdaqGS:MSFT) and Danaher Corporation announced a new life sciences AI alliance focused on agentic platforms for smart instruments. The partnership aims to connect laboratory instruments and workflows through Microsoft Azure and Danaher's Foundry-powered AI agents.
- Sun 22 Nov | 24/7 Wall St. | Nvidia Stock Has Crashed 48% and Now Trades at 15 Times Earnings, Its Cheapest in More Than a Decade and Cheaper Than Microsoft and Broadcom
  https://247wallst.com/investing/2026/11/21/nvidia-stock-has-crashed-48-and-now-trades-at-15-times-earnings-its-cheapest-in-more-than-a-decade-and-cheaper-than-microsoft-and-broadcom/
  > Nvidia Stock Has Crashed 48% and Now Trades at 15 Times Earnings, Its Cheapest in More Than a Decade and Cheaper Than Microsoft and Broadcom This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Sat 21 Nov | TIKR.com | Buy Microsoft and Amazon at More Than 70x 2028 Free Cash Flow? Here’s What Their Capex Must Return
  https://www.tikr.com/blog/buy-microsoft-and-amazon-at-more-than-70x-2028-free-cash-flow-heres-what-their-capex-must-return
  > - At the Nov. 20 close, Microsoft traded at about 77x the free cash flow analysts expect for fiscal 2028, and Amazon traded at about 75x. - Amazon plans to spend about $220 billion on capex this year and more next year, and analysts expect its free cash flow to stay negative until 2028.
- Sat 21 Nov | Simply Wall St | Intel Stock Gets A Foundry Win With Microsoft Backing
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-stock-gets-a-foundry-win-with-microsoft-backing
- Sat 21 Nov | Trefis | Microsoft Was The Only Big AI Buyer Paying Down Debt. How Much More Can It Spend?
  https://www.trefis.com/stock/msft/articles/627454/microsoft-was-the-only-big-ai-buyer-paying-down-debt-how-much-more-can-it-spend/2026-11-21
- Sat 21 Nov | TIKR.com | Hank Paulson Has “Never Seen So Much Money Chasing One Opportunity.” That’s a Problem for Microsoft, Amazon and Alphabet
  https://www.tikr.com/blog/hank-paulson-has-never-seen-so-much-money-chasing-one-opportunity-thats-a-problem-for-microsoft-amazon-and-alphabet?
- Sat 21 Nov | ad-hoc-news.de | Microsoft's Azure Paradox: Blistering Cloud Growth, Shrinking Free Cash Flow
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/microsoft-s-azure-paradox-blistering-cloud-growth-shrinking-free-cash-flow/70542715
## NVDA  (8 leads)
- Sun 22 Nov | Yahoo Finance | Chamath Palihapitiya Praises Jensen Huang As ‘Biblically Good,’ But Warns Bringing Him Back At Nvidia Could Put ‘Everybody’ At Risk
  https://finance.yahoo.com/markets/stocks/articles/chamath-palihapitiya-praises-jensen-huang-065225068.html
  > Chamath Palihapitiya Praises Jensen Huang As ‘Biblically Good,’ But Warns Bringing Him Back At Nvidia Could Put ‘Everybody’ At Risk - Palihapitiya acknowledged that Huang was an "exceptional, legendary founder and CEO" who built what he called "the most important company in the most important industry in the world."
- Sun 22 Nov | Yahoo Finance | Where Will Nvidia Stock Be in 20 Years? The Answer Might Surprise You.
  https://finance.yahoo.com/markets/stocks/articles/where-nvidia-stock-20-years-052002804.html
  > Nvidia (NASDAQ:NVDA) stock is currently the cheapest it has been in over a decade. Shares trade at just 16 times trailing earnings. That's even cheaper than the company's previous decade-low valuation set in early 2019. The GPU maker generated $43.8 billion in free cash flow last quarter.
- Sun 22 Nov | Yahoo Finance | Nvidia Shock Puts MongoDB Stock And Cloud Software Names Back In Focus
  https://finance.yahoo.com/technology/ai/articles/nvidia-shock-puts-mongodb-stock-051540855.html
  > AI infrastructure just absorbed a shock, with Nvidia's leadership turmoil, customer investigations and eye catching Q3 FY2027 numbers all hitting at once, and that ripple now runs straight through the cloud and data center operators that power this boom. Pricing for compute is changing, expectations are resetting and some stocks are suddenly being repriced.
- Sun 22 Nov | 조선일보 | Seohak Ants' 800 Billion Nvidia Buy Leads to 6 Trillion Loss
  https://www.chosun.com/english/market-money-en/2026/11/22/UFVTVQ2ZBNCCJEEFQRFSQDP534/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | Investor's Business Daily | Dow Jones Futures: After Nvidia, Anthropic Fuel Worst Week Since Covid, Look For These 'Absolute Losers'
  https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-worst-week-covid-nvidia-anthropic-vix-fear-gauge/
- Sun 22 Nov | Yahoo Finance | Should You Forget Nvidia and Buy These 2 AI Memory Stocks Instead?
  https://finance.yahoo.com/markets/stocks/articles/forget-nvidia-buy-2-ai-012302831.html
- Sun 22 Nov | 24/7 Wall St. | Nvidia Stock Has Crashed 48% and Now Trades at 15 Times Earnings, Its Cheapest in More Than a Decade and Cheaper Than Microsoft and Broadcom
  https://247wallst.com/investing/2026/11/21/nvidia-stock-has-crashed-48-and-now-trades-at-15-times-earnings-its-cheapest-in-more-than-a-decade-and-cheaper-than-microsoft-and-broadcom/
- Sun 22 Nov | Yahoo Finance | Nvidia Without Jensen Huang: 3 Things That Could Go Right and 3 That Could Go Wrong
  https://finance.yahoo.com/markets/stocks/articles/nvidia-without-jensen-huang-3-000101805.html
## AMZN  (8 leads)
- Sun 22 Nov | shattered.io | Amazon Decart Acquisition: Up to $7.5B Deal Explained
  https://shattered.io/amazon-nears-7-5-billion-decart-acquisition-cash-stock-deferred/
  > Amazon is closing in on a purchase of Decart, an Israeli AI startup, in a transaction valued at more than $7 billion, according to Crypto Briefing’s summary of the reporting. The Financial Times reported that contingent payments could lift the total to nearly $7.5 billion.
- Sun 22 Nov | The Motley Fool | ULA Vulcan Launch Ends in Disaster for Amazon's Satellite Internet Ambitions
  https://www.fool.com/investing/2026/11/21/ula-vulcan-launch-ends-in-disaster-for-amazon-s-satellite-internet-ambitions/
  > By Rich Smith – - A United Launch Alliance Vulcan Centaur rocket failed to reach orbit in its first attempt in nine months. - The rocket was carrying 40 Amazon Leo internet satellites -- all now lost. [Figures on the page: unaudited or preliminary; nine months. Check which one each figure is.]
- Sun 22 Nov | ad-hoc-news.de | Amazon's $5 Billion Handoff: Blackstone Takes the Keys, AWS Keeps the Lease
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-5-billion-handoff-blackstone-takes-the-keys-aws-keeps-the-lease/70543692
  > Amazon shares fell 3.8% on Friday, caught in a broad selloff of AI-linked and technology names. But the size of the drop is less telling than the question underneath it: what do all these artificial-intelligence investments actually have to earn to justify the data centers behind them — and the cost of financing that buildout?
- Sun 22 Nov | ad-hoc-news.de | Amazon's Capital Reckoning: New York Delivery Costs, a $5 Billion Data-Center Deal, and the AI Payof
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-capital-reckoning-new-york-delivery-costs-a-5-billion-data-center-deal-and-the-ai-payoff/70543669
  > Amazon shares shed 3.8% on Friday, caught in a broad selloff of AI-linked technology names. Reuters reported that investors were questioning whether the hefty sums being poured into artificial intelligence and data centers will earn an adequate return, pointing as well to restrictive signals from the Federal Reserve and worries about borrowing costs.
- Sat 21 Nov | TipRanks | Amazon Stock (AMZN) Forecast – Oppenheimer Lifts Price Target to $310 After Anthropic IPO
  https://www.tipranks.com/news/amazon-stock-amzn-forecast-oppenheimer-lifts-price-target-to-310-after-anthropic-ipo
- Sat 21 Nov | TIKR.com | Cathie Wood Just Sold $9 Million of Amazon
  https://www.tikr.com/blog/cathie-wood-just-sold-9-million-of-amazon
- Sat 21 Nov | TIKR.com | Jim Cramer: Amazon Could Sell Its Anthropic Stake and Say “Our CapEx Is Paid For.” Does the Math Work?
  https://www.tikr.com/blog/jim-cramer-amazon-could-sell-its-anthropic-stake-and-say-our-capex-is-paid-for-does-the-math-work
- Sat 21 Nov | Financial Times | Amazon closes in on $7.5bn deal to buy AI start-up Decart
  https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616?syn-25a6b1a6=1
## GOOGL  (8 leads)
- Sun 22 Nov | Kalkine Media | Why Is Alphabet (NASDAQ:GOOG) Under Focus Amid AI Market Shifts?
  https://kalkinemedia.com/us/stocks/communication/why-is-alphabet-nasdaqgoog-under-focus-amid-ai-market-shifts
  > enters focus as the present US session places greater emphasis on company-level execution. - The reassessment of ai spending keep platform demand, infrastructure use and commercial execution near the centre of the market discussion.
- Sun 22 Nov | Pluang | Alphabet's stock falls 34% as it borrows $10.9B for data center expansion amid AI demand uncertainty
  https://pluang.com/en/news-feed/saham-alphabet-terendah-1-tahun-orang-tua-google-pinjam-banyak
  (page: did not load (403))
- Sun 22 Nov | Yahoo Finance | Alphabet (GOOGL) Stock Gets Fair Value Trim As Analysts Weigh AI Spending And Monetization
  https://finance.yahoo.com/markets/stocks/articles/alphabet-googl-stock-gets-fair-001209637.html
  > The fair value estimate for Alphabet has been trimmed from US$408.09 to US$397.13, signalling a modest reset in how analysts are framing the stock. This shift aligns with fresh research that weighs heavy AI spending in Search, Google Cloud and custom TPUs against questions about near term monetization, margins and capital intensity.
- Sat 21 Nov | Crypto Briefing | Alphabet keeps borrowing as AI spending drags its stock 34% below its peak
  https://cryptobriefing.com/alphabet-debt-ai-spending-stock-decline/
  > Google's parent is tapping bond markets to fund a capex forecast of up to $205 billion while free cash flow has turned negative Alphabet shares closed Friday 34% below their May record. The AI selloff that has been chewing through tech stocks took another bite out of Google’s parent.
- Sat 21 Nov | The Motley Fool | Alphabet Stock Just Hit a 1-Year Low. Why Is Google's Parent Borrowing So Much Money?
  https://www.fool.com/investing/2026/11/21/alphabet-stock-just-hit-a-1-year-low-why-is-google-s-parent-borrowing-so-much-money/
- Sat 21 Nov | Wisevoter | Berkshire Hathaway Expands Alphabet Stake to 106 Million Shares
  https://wisevoter.com/world/us/2026/11/21/berkshire-hathaway-alphabet-stake-106-million-shares
- Sat 21 Nov | The Sunday Guardian | Nvidia Market Cap Drop 35 Percent: Share Slide Knocks Chipmaker Below Alphabet Valuation To Fourth Most Valuable US Company
  https://sundayguardianlive.com/business/nvidia-market-cap-drop-35-percent-share-slide-knocks-chipmaker-below-alphabet-valuation-to-fourth-most-valuable-us-company-325630/
- Sat 21 Nov | TradingKey | Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?
  https://www.tradingkey.com/analysis/stocks/us-stocks/262008961-alphabet-googl-stock-price-forecast-2026-google-cloud-tradingkey
## META  (8 leads)
- Sun 22 Nov | Kalkine Media | Can Meta Platforms (NASDAQ:META) Make Its Turnaround Stick?
  https://kalkinemedia.com/us/stocks/artificial-intelligence/can-meta-platforms-nasdaqmeta-make-its-turnaround-stick
  > - Meta Platforms enters focus as the present US session places greater emphasis on company-level execution. - The reassessment of ai spending keep platform demand, infrastructure use and commercial execution near the centre of the market discussion. Meta Platforms (NASDAQ:META) Communication Services Meta Platforms Inc. [Figures on the page: standalone; unaudited or preliminary. Check which one each figure is.]
- Sun 22 Nov | Simply Wall St | Meta (META) Stock Still Looks Cheap Despite AI Spending Concerns
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/meta-meta-stock-still-looks-cheap-despite-ai-spending-concer
  > Meta Platforms has pulled back sharply over the past month, and the question for anyone looking at the stock now is whether the current share price still lines up with what the company earns. Over the past 5 years, Meta has delivered a total return of 70.0%.
- Sun 22 Nov | The Motley Fool | Mark Zuckerberg’s Meta Platforms Is Pouring Up to $145 Billion Into AI This Year. Investors Should Watch This 1 Number.
  https://www.fool.com/investing/2026/11/21/mark-zuckerberg-s-meta-platforms-is-pouring-up-to-usd145-billion-into-ai-this-year-investors-should-watch-this-1-number/
  > By Neil Patel – - Meta Platforms' huge spending plans make it fair for investors to question the company’s strategy. - Advertising revenue jumped 26% in Q3 2026, driven by double-digit gains in pricing and impressions. Mark Zuckerberg founded Facebook in his Harvard dorm room in 2004.
- Sun 22 Nov | Billionaires.Africa | American billionaire Mark Zuckerberg's Meta freezes nonvoting share plan as investors sue
  https://www.billionaires.africa/2026/11/22/american-billionaire-mark-zuckerbergs-meta-freezes-nonvoting-share-plan-as-investors-sue/
  > American billionaire Mark Zuckerberg's Meta Platforms Inc. has agreed not to issue a new class of nonvoting shares while shareholders who say the plan entrenches his control pursue their lawsuit in Delaware.
- Sat 21 Nov | FinanceFeeds | Meta stock prediction: $664.52 bull, $460.13 bear
  https://financefeeds.com/meta-stock-prediction-560-84-bull-664-52-bear-460-13/
- Sat 21 Nov | TIKR.com | If the AI Trade Blows Up, Meta’s Saving Grace Is That Its Social Media Business Still “Generates a Ton of Cash”
  https://www.tikr.com/blog/if-the-ai-trade-blows-up-metas-saving-grace-is-that-its-social-media-business-still-generates-a-ton-of-cash
- Sat 21 Nov | Yahoo Finance | AI May Have Just Broken Meta’s Climate Promise
  https://finance.yahoo.com/technology/ai/articles/ai-may-just-broken-meta-170219234.html
- Sat 21 Nov | Yahoo Finance | Meta Platforms (META) Rethinks 2030 Climate Goals After 45% AI Emissions Jump
  https://finance.yahoo.com/technology/ai/articles/meta-platforms-meta-rethinks-2030-150951042.html
## TSLA  (8 leads)
- Sun 22 Nov | AOL.com | Tesla Just Started Selling Cybercabs, Here's What It Means for a SpaceX and Tesla Merger .
  https://www.aol.com/articles/tesla-just-started-selling-cybercabs-072502000.html
  > - A robotaxi ramp-up in 2027 could boost Tesla's valuation. - Tesla shareholders should be cautious about a SpaceX merger before robotaxi success. The news that Tesla(NASDAQ:TSLA)is inviting select customers to buy Cybercabs isn't a game changer from a financial perspective (at least not immediately).
- Sun 22 Nov | Reuters | Tesla Inc (TSLA.O) | Stock Price & Latest News
  https://www.reuters.com/markets/companies/TSLA.O/
  (page: did not load (401))
- Sun 22 Nov | Energy News Beat | Tesla's New 8-Year Warranty in Canada Isn't About Tailpipes. The Stock Is Asking What Comes After the Car
  https://energynewsbeat.co/electric-vehicles/teslas-new-8-year-warranty-in-canada-isnt-about-tailpipes-the-stock-is-asking-what-comes-after-the-car/
  > Tesla’s North American warranty, effective Sept. 1, 2026, adds an Emissions Performance Warranty for 2027 and later Model 3 and Model Y vehicles: 8 years or 128,700 kilometers, whichever comes first. Tesla stock closed Friday, Nov. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Sat 21 Nov | TradingKey | If SpaceX and Tesla Truly Merge, Should Investors Celebrate or Exit Early?
  https://www.tradingkey.com/analysis/stocks/us-stocks/261930373-stock-spacex-tsla-spcx-elon-musk-xai-terafab-fsd-x-tradingkey
  > If SpaceX and Tesla Truly Merge, Should Investors Celebrate or Exit Early? Elon Musk has reportedly discussed merging SpaceX with Tesla. A merger might offer synergies, integrate energy networks, and reduce "Musk premium risk" for Tesla shareholders.
- Sat 21 Nov | TradingKey | Tesla Stock Price Prediction: SpaceX Thruster-Equipped Roadster May Debut This Month, Could It Boost TSLA Stock?
  https://www.tradingkey.com/analysis/stocks/us-stocks/262110784-tesla-stock-forecast-spacex-roadster-tsla-stock-tradingkey
- Sat 21 Nov | Yahoo Finance | Cathie Wood, Brad Gerstner and 16 Other Big Funds Bought Tesla Last Quarter, While 15 Sold. Who’s Right?
  https://finance.yahoo.com/markets/stocks/articles/cathie-wood-brad-gerstner-16-211905292.html
- Sat 21 Nov | Yahoo Finance | Tesla (TSLA) Stock Looks Richly Priced After Its 47% Three Year Run
  https://finance.yahoo.com/markets/stocks/articles/tesla-tsla-stock-looks-richly-210854263.html
- Sat 21 Nov | Investor's Business Daily | Tesla FSD V15 Rolling Out, Goes 'Wide' Next Month. Elon Musk Says It's 'Something Special.'
  https://www.investors.com/news/tesla-fsd-v15-coming-next-month-elon-musk-says-something-special/
## JPM  (8 leads)
- Sun 22 Nov | Kalkine Media | Will JPMorgan Chase (NYSE:JPM) Keep Its Edge As Sentiment Shifts?
  https://kalkinemedia.com/us/stocks/bluechip/will-jpmorgan-chase-nysejpm-keep-its-edge-as-sentiment-shifts
  > - JPMorgan Chase enters focus as the present US session places greater emphasis on company-level execution. - Large-cap us conditions keep market leadership, operating resilience and capital discipline near the centre of the market discussion. [Figures on the page: standalone; unaudited or preliminary. Check which one each figure is.]
- Sun 22 Nov | shattered.io | JPMorgan Data Breach: Vendor Hit, 16,000 Unconfirmed
  https://shattered.io/jpmorgan-vendor-breach-names-emails-marketing-data-16000-unconfirmed/
  > JPMorgan Chase confirmed this week that third parties providing services to the bank were the target of a cyberattack, and that attackers likely reached marketing data those vendors held. The bank said that data may include some customer names and email addresses, and it said its own services kept running without disruption.
- Sat 21 Nov | Beinsure | JPMorgan Chase names Bregje de Best as CFO to succeed Jeremy Barnum in 2027
  https://beinsure.com/news/jpmorgan-chase-names-bregje-de-best-as-cfo-to-succeed-jeremy-barnum-in-2027/
  > JPMorgan Chase has appointed Bregje de Best as its next Chief Financial Officer, succeeding Jeremy Barnum after the bank reports its first-quarter 2027 financial results. De Best currently serves as CFO of JPMorgan Chase’s Commercial & Investment Bank (CIB).
- Sat 21 Nov | finchannel | JPMorgan Chase cyberattack disclosure points to vendor-held marketing data
  https://finchannel.com/jpmorgan-chase-cyberattack-disclosure-points-to-vendor-held-marketing-data/142607/american-business-trends/2026/11/
  > The JPMorgan Chase cyberattack disclosure concerns third-party service providers holding marketing information that may include customers’ names and email addresses, the bank said Thursday. Its investigation into the vendor incident comes days after a separate software problem delayed some transactions.
- Sat 21 Nov | MarketBeat | JPMorgan Chase & Co. $JPM Stock Position Cut by Voya Investment Management LLC
  https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-position-cut-by-voya-investment-management-llc-2026-11-21/
- Sat 21 Nov | Fox News | Visa, Mastercard and JPMorgan customer data leaked
  https://www.foxnews.com/tech/visa-mastercard-jpmorgan-customer-data-leaked
- Sat 21 Nov | Speaks Media | JP Morgan Chase Announces $0.5183 Quarterly Coupon for Alerian MLP Index ETN
  https://speaks.co.in/business/jp-morgan-chase-announces-0-5183-quarterly-coupon-for-alerian-mlp-index-etn/
- Sat 21 Nov | MarketBeat | JPMorgan Chase & Co. $JPM Stock: Cibc World Market Inc. Cuts Position
  https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-cibc-world-market-inc-cuts-position-2026-11-21/
## XOM  (8 leads)
- Sun 22 Nov | Business Insider Africa | ExxonMobil-led group approves $4 billion Angola oil project as Block 15 makes 21st discovery, with production-sharing deal extended to 2037
  https://africa.businessinsider.com/local/markets/exxonmobil-led-group-approves-dollar4-billion-angola-oil-project-as-block-15-makes/fsfsh5y
  > - Block 15 partners approved a $4 billion investment decision. - The plan covers Kizomba A and B and the Likembe field. - Tchihumba West is the block’s 21st discovery. - Angola produced 1.05 million barrels of oil a day in September.
- Sun 22 Nov | JournalArta | ExxonMobil Invokes Treaty to Challenge EU Carbon Storage Rules
  https://journalarta.com/en/2026/11/22/exxonmobil-investment-treaty-eu-carbon-storage-rules/
  > ExxonMobil Invokes Treaty to Challenge EU Carbon Storage Rules ExxonMobil subsidiaries have filed an arbitration notice against the European Commission over rules requiring oil and gas producers to help build carbon storage capacity.
- Sun 22 Nov | KHOU | All-clear issued after fire at ExxonMobil Baytown Olefins Plant
  https://www.khou.com/article/news/local/exxonmobil-baytown-olefins-plant-fire-all-clear/285-240e836f-9cc6-46e9-afc3-7661732cef78
  (page: did not load (403))
## AVGO  (8 leads)
- Sun 22 Nov | Crypto Briefing | David Tepper exits AMD and Broadcom, doubles down on Nvidia and Micron
  https://cryptobriefing.com/david-tepper-exits-amd-broadcom-ai-chips/
  > Appaloosa's third-quarter filing shows a selective bet on the AI chip supply chain rather than a retreat from it David Tepper has changed his AI chip lineup. His hedge fund, Appaloosa Management, sold its entire positions in Advanced Micro Devices and Broadcom during the third quarter.
- Sun 22 Nov | 24/7 Wall St. | Nvidia Stock Has Crashed 48% and Now Trades at 15 Times Earnings, Its Cheapest in More Than a Decade and Cheaper Than Microsoft and Broadcom
  https://247wallst.com/investing/2026/11/21/nvidia-stock-has-crashed-48-and-now-trades-at-15-times-earnings-its-cheapest-in-more-than-a-decade-and-cheaper-than-microsoft-and-broadcom/
  > Nvidia Stock Has Crashed 48% and Now Trades at 15 Times Earnings, Its Cheapest in More Than a Decade and Cheaper Than Microsoft and Broadcom This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Sat 21 Nov | Barchart.com | Why It’s Time to Buy the Pullback in Broadcom Stock
  https://www.barchart.com/story/news/8953006/why-its-time-to-buy-the-pullback-in-broadcom-stock
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | Seeking Alpha | Broadcom AI outlook in focus beyond quarterly results, Goldman says (AVGO:NASDAQ)
  https://seekingalpha.com/news/4675236-broadcom-ai-outlook-in-focus-beyond-quarterly-results-goldman-says
  (page: did not load (403))
- Sat 21 Nov | MarketBeat | 3,322 Broadcom Inc. $AVGO Shares Purchased by Intesa Sanpaolo Wealth Management
  https://www.marketbeat.com/instant-alerts/filing-3322-broadcom-inc-avgo-shares-purchased-by-intesa-sanpaolo-wealth-management-2026-11-21/
- Sat 21 Nov | MarketBeat | Broadcom Inc. $AVGO Holdings Increased by State Street Corp
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-holdings-increased-by-state-street-corp-2026-11-21/
- Sat 21 Nov | Yahoo Finance | The 1 Thing I'll Be Watching When Broadcom Reports on Dec. 9
  https://finance.yahoo.com/markets/stocks/articles/1-thing-ill-watching-broadcom-134602300.html
- Sat 21 Nov | MarketBeat | Broadcom Inc. $AVGO Stake Decreased by Resona Asset Management Co. Ltd.
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stake-decreased-by-resona-asset-management-co-ltd-2026-11-21/
## BRK.B  (8 leads)
- Sun 22 Nov | CEOWORLD magazine | Billionaire Warren Buffett’s $5.5 Billion Gift Opens a $160 Billion Handover
  https://ceoworld.biz/2026/11/22/billionaire-warren-buffetts-5-5-billion-gift-opens-a-160-billion-handover/
  > Each Warren Buffett donation now moves Berkshire Hathaway shares out of the hands that controlled the company for six decades, and the terms of the transfer matter more to shareholders than the size of any single gift.
- Sun 22 Nov | Vietnam.vn | Warren Buffett donated nearly $5.5 billion to family funds, bringing Berkshire Hathaway's market capitalization to $1.26 trillion.
  https://www.vietnam.vn/en/warren-buffett-quyen-gop-gan-5-5-ty-usd-cho-cac-quy-gia-dinh-von-hoa-berkshire-hathaway-cham-moc-1-260-ty-usd
  > Donating $5.47 billion to four family funds, setting a target of distributing over $155 billion by 2034. According to a Thanksgiving announcement from Berkshire Hathaway, Warren Buffett converted 6,150 Class A shares into 9,225,000 Class B shares, equivalent to approximately $5.47 billion.
- Sun 22 Nov | 24/7 Wall St. | Warren Buffett Bought a Farm in 1986 and Has Visited It Twice. Here's His Rule for a 66-Year-Old With $700,000 in an IRA and $2,900 a Month in Social Security
  https://247wallst.com/investing/2026/11/21/warren-buffett-bought-a-farm-in-1986-and-has-visited-it-twice-heres-his-rule-for-a-66-year-old-with-700000-in-an-ira-and-2900-a-month-in-social-security/
  > Warren Buffett Bought a Farm in 1986 and Has Visited It Twice. Here’s His Rule for a 66-Year-Old With $700,000 in an IRA and $2,900 a Month in Social Security
## WMT  (8 leads)
- Sun 22 Nov | Seeking Alpha | Walmart: A Boringly Solid Business At A Not-So-Boring Price (NASDAQ:WMT)
  https://seekingalpha.com/article/4970900-walmart-stock-boringly-solid-business-at-not-so-boring-price
  (page: only 43 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | Yahoo Finance | Walmart (WMT) Stock May Be Fully Valued After Earnings News
  https://finance.yahoo.com/markets/stocks/articles/walmart-wmt-stock-may-fully-010939760.html
  > Walmart has delivered a powerful long run for shareholders, and the latest burst of earnings news keeps attention squarely on whether the current share price is still backed by its profits.
- Sun 22 Nov | Yahoo Finance | Lawsuit accuses Build-A-Bear of misleading investors over Walmart deal
  https://finance.yahoo.com/markets/stocks/articles/lawsuit-accuses-build-bear-misleading-000619228.html
  > Lawsuit accuses Build-A-Bear of misleading investors over Walmart deal LOUIS - A new lawsuit accuses St. Louis-based retailer Build-A-Bear Workshop of misleading investors about the strength of its Walmart partnership and maintaining an overly optimistic financial outlook before later lowering its revenue forecast.
## V  (8 leads)
- Sat 21 Nov | TIKR.com | Prologis Has Gone Nowhere in a Year. Former Visa CEO Alfred Kelly Just Bought $587,000 of Stock
  https://www.tikr.com/blog/prologis-has-gone-nowhere-in-a-year-former-visa-ceo-alfred-kelly-just-bought-587000-of-stock
  > - Prologis director Alfred F. Kelly, Jr., Visa’s former CEO, bought $587,350 of Prologis stock on Nov. 18 at an average of $124.97 a share. - The stock is about 18% below its July closing high as higher interest rates weigh on property values, even though its third-quarter results held up. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sat 21 Nov | Yahoo! Finance Canada | Leverage Shares 2x Visa ETP Securities A (VIS2.PA) Stock Forum & Discussion - Yahoo Finance
  https://ca.finance.yahoo.com/quote/VIS2.PA/community/
  (page: only 13 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 21 Nov | MarketBeat | Visa Inc. $V Holdings Boosted by State Street Corp
  https://www.marketbeat.com/instant-alerts/filing-visa-inc-v-holdings-boosted-by-state-street-corp-2026-11-21/
  > $V Holdings Boosted by State Street Corp - State Street increased its Visa stake by 2.4% in the third quarter, adding nearly 2 million shares to bring its holding to about 84.9 million shares, valued at roughly $30.5 billion.
## ORCL  (8 leads)
- Sun 22 Nov | Kalkine Media | Will Oracle Corporation (NYSE:ORCL) Keep Its Recovery On Track?
  https://kalkinemedia.com/us/stocks/artificial-intelligence/will-oracle-corporation-nyseorcl-keep-its-recovery-on-track
  > - Oracle Corporation enters focus as the present US session places greater emphasis on company-level execution. - The reassessment of ai spending keep platform demand, infrastructure use and commercial execution near the centre of the market discussion. - The case around Oracle Corporation rests on how clearly the business translates strategy into measurable delivery.
- Sun 22 Nov | shattered.io | Oracle OpenAI Contract Fully Funded After $20B Raise
  https://shattered.io/oracle-says-openai-contract-fully-funded-20-billion-final-raise/
  > Oracle told investors on November 20, 2026 that it has locked down the money for its OpenAI infrastructure contract.
- Sat 21 Nov | ad-hoc-news.de | Oracle Has the OpenAI Money in Hand; Now the Concrete Has to Catch Up
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-has-the-openai-money-in-hand-now-the-concrete-has-to-catch-up/70543355
  > Oracle says the financing for its OpenAI infrastructure contract is fully assembled, closing a question that had dogged the stock. The harder question — whether the buildout can be delivered on time and on budget — is only now coming into focus.
- Sat 21 Nov | Simply Wall St | Oracle (ORCL) Unveiled New AI Tools For Life Sciences And Finance
  https://simplywall.st/stocks/us/software/nyse-orcl/oracle/news/oracle-orcl-unveiled-new-ai-tools-for-life-sciences-and-fina
  > Oracle (NYSE:ORCL) launched new AI agents for life sciences in the past week to support clinical trial workflows. The firm introduced AI-powered analytics tools for financial services clients aimed at risk management and enterprise reporting. Oracle issued a major Java security patch addressing vulnerabilities affecting healthcare systems, including U.S.
- Sat 21 Nov | ad-hoc-news.de | Oracle Says the OpenAI Bill Is Covered — the Hard Part Comes Next
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-says-the-openai-bill-is-covered-the-hard-part-comes-next/70542992
- Sat 21 Nov | 24/7 Wall St. | Oracle Stock Is Now Down Almost 70% From its Peak
  https://247wallst.com/investing/2026/11/21/oracle-stock-is-now-down-almost-70-from-its-peak/
- Sat 21 Nov | Wisevoter | Oracle Shares Fall as AI Data-Center Bets Weigh
  https://wisevoter.com/world/us/2026/11/21/oracle-shares-fall-ai-data-center-risk
- Sat 21 Nov | ad-hoc-news.de | Oracle's Credit Insurance Hits October Highs as AI Selloff Meets a Funding Rebuttal
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-s-credit-insurance-hits-october-highs-as-ai-selloff-meets-a-funding-rebuttal/70542629
## COST  (8 leads)
- Sat 21 Nov | The Economic Times | Costco makes major Thanksgiving closure decision as Americans rush to stock up on generators, canned food
  https://m.economictimes.com/news/international/world-news/costco-makes-major-thanksgiving-closure-decision-as-americans-rush-to-stock-up-on-generators-canned-food-and-emergency-supplies-amid-growing-us-doomsday-fears/articleshow
  > ALSO READ: Why is Melania Trump warning Barron about dating? Costco to close all US warehouses on Thanksgiving Costco has confirmed that all its US warehouses will remain closed on Thursday, November 26, in observance of Thanksgiving. According to TheStreet, Costco follows a longstanding policy of closing its warehouses on seven major holidays every year.
- Sat 21 Nov | Yahoo Finance | Tech Outages Drive Costco Surge: How Much Emergency Prep Should You Buy?
  https://finance.yahoo.com/markets/stocks/articles/tech-outages-drive-costco-surge-170042732.html
  > Bulk essentials and generators were wiped out as shoppers rushed to stock up on emergency supplies. The buying spree follows several widespread outages, including a Microsoft Outlook outage and a nationwide halt for all U.S.
- Sat 21 Nov | The Globe and Mail | Costco’s U.S. Comparable Sales Jumped 12.6% in October. Here’s the Number That Shows Its Moat Is Widening.
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8950139/costcos-us-comparable-sales-jumped-126-in-october-heres-the-number-that-shows-its-moat-is-widening/
  > - Even excluding the impact of gas and foreign exchange, Costco's domestic same-store sales were up a strong 8.1%. - As the business brings on more members, which is critical to its financial success, it proves that the warehouse value proposition still holds.
## NFLX  (8 leads)
- Sun 22 Nov | Yahoo Finance | Netflix Falls Below $60. Bill Ackman Explains Why That’s an Incredible Investment Opportunity.
  https://finance.yahoo.com/markets/stocks/articles/netflix-falls-below-60-bill-042002519.html
  > Netflix's (NASDAQ:NFLX) share price has been cut in half from the all-time high it reached last summer. The stock now trades below $60 per share, as of this writing.
- Sat 21 Nov | The Motley Fool | Michael Burry Says He's Looking at Netflix Stock in the High $30s. I'd Consider It Now, Well Above That.
  https://www.fool.com/investing/2026/11/21/michael-burry-says-he-s-looking-at-netflix-stock-in-the-high-usd30s-i-d-consider-it-now-well-above-that/
  > By Daniel Sparks – - Michael Burry has said he's now looking at Netflix stock in the high $30s. - That price would value Netflix at around 10 times analysts' average 2027 earnings estimate. - Netflix expects its operating margin to hit 31.5% this year, up from 29.5% in 2025.
- Sat 21 Nov | Stocktwits | Bill Ackman Takes Another Swing At NFLX After Colossal 2022 Loss: 'Netflix Has Effectively Won The Streaming Wars'
  https://stocktwits.com/news-articles/markets/equity/bill-ackman-takes-another-swing-at-nflx-after-colossal-2022-loss-netflix-has-effectively-won-the-streaming-wars/cZoqP0uRJhK
  > Billionaire investor William Ackman is taking a chance once again on Netflix Inc. (NFLX) by acquiring a fresh stake in the streaming giant through Pershing Square Holdings Ltd. In 2022, the investor sold NFLX shares after holding it for just three months, clocking a loss of more than $400 million.
- Sat 21 Nov | MarketBeat | Netflix, Inc. $NFLX Stock Position Lowered by Edgewood Management LLC
  https://www.marketbeat.com/instant-alerts/filing-netflix-inc-nflx-stock-position-lowered-by-edgewood-management-llc-2026-11-21/
  > $NFLX Stock Position Lowered by Edgewood Management LLC - Edgewood Management cut its Netflix stake by 31.9% in the third quarter, selling 1.85 million shares. It retained about 3.95 million shares, worth approximately $275 million, making Netflix 4.4% of its portfolio.
- Sat 21 Nov | Wisevoter | Netflix Shares First Reactions to Cliff Booth Film
  https://wisevoter.com/world/us/2026/11/21/netflix-cliff-booth-reactions-ai-accusations
- Fri 20 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Stock Falls 3% - What's Next?
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-stock-falls-3-whats-next-2026-11-20/
- Fri 20 Nov | TIKR.com | Prediction: Netflix and Disney Will “Blame Grand Theft Auto” for Falling Viewership, per Scott Galloway
  https://www.tikr.com/blog/prediction-netflix-and-disney-will-blame-grand-theft-auto-for-falling-viewership-per-scott-galloway?
- Fri 20 Nov | Traders Union | Netflix stock forecast: Bearish outlook persists with sellers maintaining control
  https://tradersunion.com/news/stocks/show/4351067-netflix-drops-2-91percent-today-to/
## INTC  (8 leads)
- Sun 22 Nov | The Globe and Mail | Intel Says It Just Signed Its First Customer for Its Most Advanced Chipmaking Process. The Stock Is Still More Than 60% Below Its June Record.
  https://www.theglobeandmail.com/investing/markets/stocks/INTC/pressreleases/8954290/intel-says-it-just-signed-its-first-customer-for-its-most-advanced-chipmaking-process-the-stock-is-still-more-than-60-below-its-june-record/
  > - Intel CEO Lip-Bu Tan said on Nov. 18 that the company had just signed the first customer for its 18A chipmaking process. - Intel's foundry unit brought in $411 million from outside customers in the third quarter, out of $6.7 billion in total revenue.
- Sun 22 Nov | Pluang | Intel signs first customer for its advanced 18A chipmaking process, marking a key foundry milestone.
  https://pluang.com/en/news-feed/intel-tandatangani-pelanggan-pertama-proses-chipmaking-18a-canggih
  (page: did not load (403))
- Sun 22 Nov | Seeking Alpha | Intel's Turnaround Story Remains Firmly Intact, Buy The Panic
  https://seekingalpha.com/article/4970889-intels-turnaround-story-remains-firmly-intact-buy-the-panic
  (page: did not load (403))
- Sat 21 Nov | Simply Wall St | Intel Stock Gets A Foundry Win With Microsoft Backing
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-stock-gets-a-foundry-win-with-microsoft-backing
  > Intel secured its first external customer for its advanced 18A and 18A-P chip manufacturing process and expanded a long-term agreement with Microsoft, which will use Intel Foundry EMIB packaging and commit to future Xeon supply for Azure cloud and AI infrastructure.
- Sat 21 Nov | Pluang | Intel's tech advances boost growth potential bu...
  https://pluang.com/en/news-feed/setelah-turun-62-persen-bisakah-membeli-saham-intel-menguntungkan
- Sat 21 Nov | Yahoo Finance | After Plummeting 62% This Year, Could Buying Intel Stock Today Set You Up for Life?
  https://finance.yahoo.com/markets/stocks/articles/plummeting-62-could-buying-intel-155002179.html
- Sat 21 Nov | Coinpaper | Intel Stock Crashes 21% Below CEO's $9.7M Insider Purchase Price
  https://coinpaper.com/39191/intel-stock-crashes-21-below-ceo-s-9-7-m-insider-purchase-price
- Sat 21 Nov | 富途牛牛 | Daily Short Sale Tracking: Intel's Short Volume Increased by 26 Million, With a Short Sale Ratio of 17%
  https://news.futunn.com/en/post/1005270457/daily-short-sale-tracking-intel-s-short-volume-increased-by
## LLY  (8 leads)
- Sat 21 Nov | Observer | Eli Lilly CEO David Ricks Is Using the Weight-Loss Boom to Buy His Next Bet
  https://observer.com/2026/11/eli-lilly-ceo-david-ricks-is-using-the-weight-loss-boom-to-buy-his-next-bet/
  > Eli Lilly CEO David Ricks Is Using the Weight-Loss Boom to Buy His Next Bet Flush with billions from Mounjaro and Zepbound, Lilly is snapping up biotechs in blood cancer, neuroscience, immunology and other fields, sometimes before their drugs have even reached human trials.
- Sat 21 Nov | Pluang | Eli Lilly's Zepbound shows strong weight loss r...
  https://pluang.com/en/news-feed/peluang-pertumbuhan-eli-lilly-zepbound-pasar-obesitas-remaja
  (page: did not load (403))
- Sat 21 Nov | https://hrtoday.in/ | Eli Lilly and Company Appoints Sheila Chaiban as Chief Marketing Officer – Gulf
  https://hrtoday.in/eli-lilly-and-company-appoints-sheila-chaiban-as-chief-marketing-officer-gulf/
  (page: did not load (403))
Read 80 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, ALCN, MFPC, EFIH, EGAL, AMOC, SKPC.
