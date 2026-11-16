# Desk brief, Monday, November 16, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 35s. GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s. Rates: VIX to 2026-11-13 (19.3); Treasury yields to 2026-11-13 (10-year 5.15%).
- **valuation**: ok in 2s. LLY: failed (HTTP Error 403: Forbidden); kept the card it had
- **movers**: ok in 7s. Market values: 0 of 39 updated
- **calendar**: ok in 235s. 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s. indicators: 48 series; EGX30 mixed, RSI 53.7
- **fairvalue**: ok in 1s. fair value: 51 stocks, k 16.3%, median P/E 10.4; cheapest MASR +71%, PHAR +53%, ABUK +51%; dearest ARAB -63%, MOIN -66%, BTFH -71%
- **views**: ok in 0s. Views: nothing to change.
- **results**: ok in 100s. 
- **news**: ok in 194s. 
- **leads**: ok in 79s. 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); api.nasdaq.com: 62 failed, 0 needed a retry (fetch_intraday.py, fetch_valuation.py, fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

## What moved (latest close against the one before)
- EGX30 52,023.37 (-0.91%); EGX70 EWI 18,527.40 (-0.00%); USD/EGP 53.50 (-0.22%); Gold 21K 5,975.00 (+0.08%); Brent 95.84 (-0.06%); S&P 500 7,561.67 (-0.40%); Nasdaq 25,136.27 (-0.91%); Bitcoin 63,956.00 (-4.74%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): AVGO -4.8%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 81, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (14.4% over) and its 200-day (13.4% over), though the 50-day is still below the 200-day; RSI 76, stretched after a run: above 70.
    - NVDA: Turning down: below both its 50-day average (24.1% under) and its 200-day (20.2% under), though the 50-day is still above the 200-day; RSI 25, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- None: every one has a reason or is under 5%.

Leads for them (open before using; never guess a reason):
```
EGX: failed (HTTP Error 401: Unauthorized); kept the saved session
EGX week and month: EGX stocks trading at least EGP 1m a day on average (215)
US: 2026-11-13, 847 companies
US week and month: US companies worth $10bn or more (846)
EGX30 heatmap: 2026-11-15, 31 members
US heatmap: 2026-11-13, 100 members
Market values: 0 of 39 updated

# EGX 2026-11-12
## INFI +17.5%  Foodico
- no headlines found
## ATLC +8.7%  AT Lease
- no headlines found
## DTPP +8.0%  Delta for Printing & Packaging
- no headlines found
## ROTO +5.9%  Al Rowad
- Mon 16 Nov | المتداول العربي | الولايات المتحدة تختار إنفيديا وأنثروبيك ضمن «الرواد الوطنيين» للذكاء الاصطناعي
  https://www.arabictrader.com/ar/news/economy/236245/الولايات-المتحدة-تختار-إنفيديا-وأنثروبيك-ضمن-«الرواد-الوطنيين»-للذكاء-الاصطناعي
- Sun 15 Nov | شاهد الآن | اتحاد الرواد العرب يوسّع دوره المجتمعي بلجنتين للعمل الخيري وذوي الاحتياجات الخاصة
  https://shahdnow.sa/369889/
- Sun 15 Nov | الموقف الرياضي | بفوزه على الرواد.. الحرية يواصل الضغط على صدارة دوري كرة السلة للسيدات
  https://riadi.alwehda.gov.sy/?p=173711
- Sun 15 Nov | alkifahnews.com | تزامناً مع اليوم العالمي للسكري14 نوفمبر 2026م مكتب رواد ورائدات كشافة جدة ينظم ندوة توعوية بمشاركة نخبة من الأطباء بمقر مكتب رواد ورائدات كشافة محافظة جدة الرواد
  https://alkifahnews.com/archives/367187
## HDBK +5.8%  Housing & Development Bank
- Mon 16 Nov | بنكي | بنك التعمير والإسكان يتيح تقسيط اشتراك Castello Gym حتى 12 شهرًا دون فوائد أو مصاريف إدارية
  https://www.bankygate.com/202604
- Mon 16 Nov | التعمير | بنك التعمير والإسكان يتيح تقسيط اشتراكات Castello Gym حتى 12 شهرًا دون فوائد أو مصاريف إدارية
  https://eltaameer.com/archives/484646
- Sun 15 Nov | الأسبوع | سعر الريال في بنك مصر مقابل الجنيه اليوم الأحد 15 نوفمبر 2026.. آخر تحديث
  https://www.elaosboa.com/3022915/
- Sun 15 Nov | بنكي | الودائع تحت الطلب تستحوذ على 44.3% من محفظة ودائع بنك التعمير والاسكان بنهاية سبتمبر 2026
  https://www.bankygate.com/202551
## INEG -6.3%  Integrated Engineering Group
- no headlines found
## PRCL -6.0%  Sheeni
- no headlines found
## CCRS -5.0%  Gulf Canadian Real Estate Investment
- no headlines found
## BIOC -4.3%  Glaxo Smith Kline
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح “جلاكسو سميثكلاين” تقفز 314% إلى 125 مليون جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7737549/
- Sun 15 Nov | اخبارك نت | أرباح جلاكسو سميثكلاين المجمعة تقفز 314% إلى 125 مليون جنيه خلال 9 أشهر | أموال الغد
  https://www.akhbarak.net/news/details/49549642/4/أرباح-جلاكسو-سميثكلاين-المجمعة-تقفز-314-إلى-125-مليون-جنيه-خلال-9-أشهر-أموال-الغد
- Sun 15 Nov | Pioneers Misr | أرباح جلاكسو سميثكلاين تقفز 314% إلى 125 مليون جنيه خلال 9 أشهر
  https://pioneersmisr.com/123699/
- Sun 15 Nov | جريدة المال | أرباح جلاكسو سميثكلاين تقفز 314% خلال 9 أشهر
  https://almalnews.com/2147361/أرباح-جلاكسو-سميثكلاين-تقفز-314-خلال-9/
## COPR -3.3%  Copper For Commercial Investment
- no headlines found

# US 2026-11-13
## NU +11.8%  Nu Holdings
- Mon 16 Nov | Kalkine | Nu Holdings (NYSE: NU) Shares Jump 12% After Record Quarterly Profit and Revenue
  https://kalkine.com.au/news/financial/nu-holdings-nyse-nu-shares-jump-12-after-record-quarterly-profit-and-revenue
- Mon 16 Nov | Moomoo | Nu Holdings (NU) Stock Jumped 12% Friday: What the Options Flow Shows
  https://www.moomoo.com/community/feed/nu-holdings-nu-stock-jumped-12-friday-what-the-options-117623306060181
- Sun 15 Nov | Simply Wall St | Earnings Beat Might Change The Case For Nu Holdings (NU) Stock
  https://simplywall.st/stocks/us/banks/nyse-nu/nu-holdings/news/earnings-beat-might-change-the-case-for-nu-holdings-nu-stock/amp
- Sun 15 Nov | Yahoo Finance | Nu Holdings: 3 Key Takeaways for Long-Term Investors
  https://finance.yahoo.com/markets/stocks/articles/nu-holdings-3-key-takeaways-031048122.html
## CBRS +11.2%  Cerebras Systems
- Sun 15 Nov | MarketBeat | Cerebras Systems Inc. $CBRS Stock Purchased by Washington University
  https://www.marketbeat.com/instant-alerts/filing-cerebras-systems-inc-cbrs-stock-purchased-by-washington-university-2026-11-15/
- Sun 15 Nov | Benzinga | These Analysts Slash Their Forecasts On Cerebras Systems After Q3 Results
  https://www.benzinga.com/analyst-stock-ratings/price-target/26/11/63277335/these-analysts-slash-their-forecasts-on-cerebras-systems-after-q3-results
- Sun 15 Nov | Yahoo Finance Australia | Cerebras Systems Inc. (C1RB34.SA) stock price, news, quote and history
  https://au.finance.yahoo.com/quote/C1RB34.SA/
- Sat 14 Nov | Moomoo | Cerebras Systems (CBRS) Stock Week Ahead: Options Flow Braces for a 12.4% Swing by Friday
  https://www.moomoo.com/community/feed/cerebras-systems-cbrs-stock-week-ahead-options-flow-braces-for-117615595094037
## MOG.B +6.7%  Moog
- Sun 15 Nov | Simply Wall St | Moog (MOG.A) Sets Earnings Date, Is The Valuation Discount An Opportunity?
  https://simplywall.st/stocks/us/capital-goods/nyse-mog.a/moog/news/moog-moga-sets-earnings-date-is-the-valuation-discount-an-op
- Fri 13 Nov | StockInvest.us | Moog Stock Price Forecast. Should You Buy MOG-A?
  https://stockinvest.us/stock/MOG-A
- Fri 13 Nov | Stock Titan | Moog (MOG) director sells Class A shares in nine trades under a preset trading plan.
  https://www.stocktitan.net/sec-filings/MOG/form-4-moog-inc-insider-trading-activity-19dd5dc1dbe9.html
- Fri 13 Nov | Stock Titan | Moog's 10 a.m. ET results call is set for Nov. 20.
  https://www.stocktitan.net/news/MOG/moog-inc-to-announce-fiscal-2026-year-end-results-on-november-20-3l7xfb692nal.html
## ALNY +5.4%  Alnylam Pharmaceuticals
- Fri 13 Nov | Stock Titan | One investor reports owning 10.9 million shares of Alnylam (ALNY).
  https://www.stocktitan.net/sec-filings/ALNY/schedule-13g-a-alnylam-pharmaceuticals-inc-amended-passive-investment-8183041103fc.html
- Fri 13 Nov | Yahoo Finance Australia | Alnylam Pharmaceuticals, Inc. (ALNY) stock price, news, quote and history
  https://au.finance.yahoo.com/quote/ALNY/
- Fri 13 Nov | Traders Union | Alnylam Pharmaceuticals shares jump around 5.5% as strong Q3 product revenue drives commercial momentum
  https://tradersunion.com/news/stocks/show/4238510-alnylam-pharmaceuticals-rises-5-40percent-today/
- Fri 13 Nov | Stock Titan | An investment manager reports over 10% of Alnylam (ALNY), with no shared voting power.
  https://www.stocktitan.net/sec-filings/ALNY/schedule-13g-a-alnylam-pharmaceuticals-inc-amended-passive-investment-2b2a0b6dc3f8.html
## U +5.2%  Unity Software
- Mon 16 Nov | MarketBeat | Unity Software Inc. (NYSE:U) Stock Has Consensus Target Price of $57.22 According to Brokerages
  https://www.marketbeat.com/instant-alerts/consensus-unity-software-inc-nyse-u-stock-has-consensus-target-price-of-5722-according-to-brokerages-2026-11-16/
- Sun 15 Nov | Simply Wall St | Unity Software CEO, President & Director Matthew Bromberg Sells 29% Of Holding
  https://simplywall.st/stocks/us/software/nyse-u/unity-software/news/unity-software-ceo-president-director-matthew-bromberg-sells
- Sat 14 Nov | Investing.com Canada | Piper Sandler reiterates Unity Software stock rating at overweight By Investing.com
  https://ca.investing.com/news/stock-market-news/piper-sandler-reiterates-unity-software-stock-rating-at-overweight-93CH-4956998
- Fri 13 Nov | GuruFocus | Unity Software Inc (U) Shares Surge 5.2% -- What GF Score of 68 Tells Investors
  https://www.gurufocus.com/news/9198827/unity-software-inc-u-shares-surge-52-what-gf-score-of-68-tells-investors
## NBIS -9.9%  Nebius Group
- Mon 16 Nov | TIKR.com | Bad News for the AI Trade: Nebius’s 2027 Guide Works Out to “$8-9M per MW,” the Same as 2026 per Jim Chanos
  https://www.tikr.com/blog/bad-news-for-the-ai-trade-nebiuss-2027-guide-works-out-to-8-9m-per-mw-the-same-as-2026-per-jim-chanos?
- Mon 16 Nov | Benzinga | Nebius Shares Rise 8% After Key Trading Signal
  https://www.benzinga.com/opinion/26/11/63278565/nebius-shares-rise-8-percent-after-key-trading-signal
- Sun 15 Nov | Simply Wall St | Nebius Group (NBIS) Could Be 55% Undervalued After Guidance Shock
  https://simplywall.st/stocks/us/software/nasdaq-nbis/nebius-group/news/nebius-group-nbis-could-be-55-undervalued-after-guidance-sho
- Sun 15 Nov | Yahoo Finance | Nebius Keeps Sliding: Why Baird Still Sees 73% Upside
  https://finance.yahoo.com/markets/stocks/articles/nebius-keeps-sliding-why-baird-170036960.html
## AMD -8.8%  Advanced Micro Devices
- Mon 16 Nov | MarketBeat | Advanced Micro Devices, Inc. $AMD Stock: AlTi Global Inc. Decreases Holdings
  https://www.marketbeat.com/instant-alerts/filing-advanced-micro-devices-inc-amd-stock-alti-global-inc-decreases-holdings-2026-11-16/
- Mon 16 Nov | MarketBeat | Bessemer Group Inc. Acquires 114,673 Shares of Advanced Micro Devices, Inc. $AMD
  https://www.marketbeat.com/instant-alerts/filing-bessemer-group-inc-acquires-114673-shares-of-advanced-micro-devices-inc-amd-2026-11-16/
- Mon 16 Nov | Moomoo | Trending Industry Today: Advanced Micro Devices Leads Losses In Semiconductors Stocks
  https://www.moomoo.com/news/post/1004616523/trending-industry-today-advanced-micro-devices-leads-losses-in-semiconductors
- Mon 16 Nov | Yahoo Finance | Advanced Micro Devices And 2 Other High Growth Stocks
  https://finance.yahoo.com/markets/stocks/articles/advanced-micro-devices-2-other-051555106.html
## FN -7.3%  Fabrinet
- Sun 15 Nov | TipRanks | Fabrinet Earnings Call Signals Data Center Growth Surge
  https://www.tipranks.com/news/company-announcements/fabrinet-earnings-call-signals-data-center-growth-surge
- Sat 14 Nov | MarketBeat | Fabrinet (NYSE:FN) Stock Now Rated "Moderate Buy" by Wall Street Analysts
  https://www.marketbeat.com/instant-alerts/consensus-fabrinet-nyse-fn-stock-now-rated-moderate-buy-by-wall-street-analysts-2026-11-14/
- Fri 13 Nov | TradingKey | Fabrinet Stock (FN) Moved Down by 7.54% on Nov 13: What Signal Does It Send?
  https://www.tradingkey.com/news/market-movers/262305197-market-movers-fn-20261113
- Fri 13 Nov | StockStory | Everpure and Fabrinet shares plummet, what you need to know
  https://stockstory.org/us/stocks/nyse/p/news/why-up-down/everpure-and-fabrinet-shares-plummet-what-you-need-to-know
## DELL -7.2%  Dell Technologies
- Mon 16 Nov | TradingView | Dell Technologies Inc. Stock 12‑Month Price Target Cut to $590.73, Implies 71% Upside
  https://www.tradingview.com/news/tradingview:2befabea80c9a:0-dell-technologies-inc-stock-12-month-price-target-cut-to-590-73-implies-71-upside/
- Mon 16 Nov | Investing.com | Richard Rothberg, Dell general counsel, sells $3.29M in shares.
  https://www.investing.com/news/insider-trading-news/richard-rothberg-dell-general-counsel-sells-329m-in-shares-93CH-5028263
- Mon 16 Nov | Investing.com Australia | Dell Technologies president, global sales Peter Trizzino sells $21.1M stock
```

## Results to record (results_due.py)
## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py
### PHDC
- Mon 16 Nov | اليوم السابع | خريطة الأرباح والخسائر في البورصة.. قفزة قياسية لـ"إيديتا" وتراجع مفاجئ في أرباح "بالم هيلز"
  https://www.youm7.com/story/2026/11/16/خريطة-الأرباح-والخسائر-في-البورصة-قفزة-قياسية-لـ-إيديتا-وتراجع/7620117
  > كشفت النتائج المالية لعدد من الشركات المقيدة بالبورصة المصرية، عن أداء متباين خلال التسعة أشهر الأولى من عام 2026، إذ سجلت شركات بلتون القابضة وإيديتا للصناعات الغذائية وأسمنت سيناء نموًا في الأرباح، فيما حققت ممفيس للأدوية والألومنيوم العربية ارتفاعًا في صافي الربح، رغم تراجع الإيرادات في بعض الأنشطة، بينما أظهرت نتائج بالم هيلز للتعمير نموًا في الإيرادات والأرباح قبل الضرائب، مع انخفاض صافي الربح بعد الضرائب وحصة الأقلية. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | مجلة البوصلة الاقتصادية | أرباح "بالم هيلز" تتراجع إلى 3.6 مليار جنيه خلال 9 أشهر
  https://alboslanews.com/أسواق-مال/أرباح-بالم-هيلز-تتراجع-إلى-36-مليار-جنيه-خلال-9-أشهر-430850
  > أرباح "بالم هيلز" تتراجع إلى 3.6 مليار جنيه خلال 9 أشهر الإثنين 16 نوفمبر 2026 -10:35 أظهرت القوائم المالية المجمعة لشركة بالم هيلز للتعمير، عن الـ 9 أشهر الأولى من عام 2026، انخفاضًا في الأرباح، محققة 3.68 مليار جنيه، مقابل أرباح بقيمة 3.7 مليار جنيه عن الـ 9 أشهر الأولى من عام 2025. [Figures on the page: standalone; consolidated; nine months; first half. Check which one each figure is.]
### FWRY
- Sun 15 Nov | خبري نيوز | أرباح فوري ترتفع 32.2% إلى 2.7 مليار جنيه في أول 9 أشهر من العام الحالي
  https://khabrynews.com/213289/
  > سجلت شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية نموًا في صافي أرباحها المجمعة بنسبة 32.2% على أساس سنوي، ليبلغ 2.7 مليار جنيه تقريبا خلال الأشهر التسعة الأولى من عام 2026. كما صعدت إيرادات فوري خلال الفترة من يناير إلى سبتمبر بنسبة 38% لتصل إلى 8.351 مليار جنيه، مدفوعة بتوسع أنشطتها وتنوع مصادر دخلها في السوق المصرية. [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | بوابة بلوم | أرباح فوري ترتفع 32% إلى 2.87 مليار جنيه خلال 9 أشهر
  https://bloom-gate.com/أسواق/أرباح-فوري-ترتفع-32-إلى-2-87-مليار-جنيه-خلال-9/
  > أرباح فوري ترتفع 32% إلى 2.87 مليار جنيه خلال 9 أشهر سجلت شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية نمواً في صافي أرباحها المجمعة خلال التسعة أشهر الأولى من عام 2026، بدعم من زيادة إيرادات النشاط، وفقاً للقوائم المالية المرسلة إلى البورصة المصرية. [Figures on the page: standalone; consolidated; nine months. Check which one each figure is.]
- Sun 15 Nov | جريدة حابي | فوري تُحقق 2.69 مليار جنيه أرباحًا مجمعة في 9 أشهر بارتفاع 32.2%
  https://hapijournal.com/2026/11/15/فوري-تُحقق-2-69-مليار-جنيه-أرباحًا-مجمعة-ف/
  > فوري تُحقق 2.69 مليار جنيه أرباحًا مجمعة في 9 أشهر بارتفاع 32.2% أشرف صبري: تظل التكنولوجيا ركيزة أساسية لدعم خططنا التوسعية رنا ممدوح _ أعلنت شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، عن نتائجها المالية والتشغيلية المجمعة، حيث ارتفع صافي الربح بنسبة 32.2% على أساس سنوي، في أول تسعة أشهر من العام الجاري، ليصل إلى 2.690 مليار جنيه. إيرادات الشركة تنمو 38% إلى 8.35 مليار جنيه [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | followict | فوري تحقق 2.69 مليار جنيه صافي أرباح خلال 9 أشهر بنمو 32.2%
### ALCN
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح الإسكندرية لتداول الحاويات ترتفع 15% خلال 9 أشهر بدعم نمو حركة التداول
  https://twaslnews1.twaslnews.com/7731478/
- Sun 15 Nov | اخبارك نت | أرباح الإسكندرية لتداول الحاويات ترتفع 15% إلى 5.72 مليار جنيه خلال 9 أشهر | أموال الغد
  https://www.akhbarak.net/news/details/49549459/4/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-إلى-5-72-مليار-جنيه-خلال-9-أشهر-أموال-الغد
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع، ارتفاع صافي أرباح الشركة بنسبة 15% خلال التسعة أشهر الأولى من عام 2026، على أساس سنوي. وأوضحت الشركة، في بيان مرسل إلى بورصة مصر، أنها سجلت صافي ربح بعد الضرائب بلغ نحو 5.72 مليار جنيه خلال الفترة من يناير حتى نهاية سبتمبر 2026، مقابل 4.96 مليار جنيه خلال الفترة المقارنة من عام 2025.
- Sun 15 Nov | جريدة المال | أرباح الإسكندرية لتداول الحاويات ترتفع 15% لتسجل 5.72 مليار جنيه في 9 أشهر
  https://almalnews.com/2147339/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-لتسجل/
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع عن التسعة أشهر الأولى من العام الجاري، نمو أرباح الشركة على أساس سنوي بنسبة 15%. وبحسب البيان المرسل إلى البورصة المصرية، حققت الشركة صافي ربح بعد الضرائب بلغ نحو 5.72 مليار جنيه خلال التسعة أشهر الأولى من عام 2026، مقابل صافي ربح بلغ 4.96 مليار جنيه خلال الفترة المقارنة من عام 2025.
### MFPC
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح موبكو ترتفع 56% إلى 12 مليار جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7753826/
- Sun 15 Nov | جريدة باور نيوز الاخبارية | أرباح موبكو تقفز إلى 12.1 مليار جنيه في 9 أشهر بزيادة قدره نمو 56% مقابل الفترة المماثلة من العام السابق
  https://powernews.cc/?p=294107
  > حققت شركة مصر لإنتاج الأسمدة – موبكو، 56% نموًا في صافي أرباحها بعد الضريبة، ليصل إلى 12.139 مليار جنيه، في أول تسعة أشهر من العام الجاري، مقابل 7.784 مليار جنيه بالفترة المناظرة. وصعد مجمل الربح، وفقًا لقائمة الدخل المرسلة إلى البورصة المصرية اليوم، بنسبة 50% إلى 14.201 مليار جنيه، خلال الفترة يناير – سبتمبر 2026، مقابل 9.466 مليار جنيه بالفترة المناظرة.
- Sun 15 Nov | Egypt Oil & Gas | MOPCO Posts 56% Rise in Net Profit in 9M of 2026
  https://egyptoil-gas.com/news/mopco-posts-56-rise-in-net-profit-in-9m-of-2026/
  > Misr Fertilizers Production Company (MOPCO), Egypt’s largest nitrogen fertilizer producer, recorded a 56% year-on-year (YoY) increase in net profit after tax to EGP 12.14 billion in the first nine months of 2026, according to the company’s financial results report. Sales rose 47% YoY to EGP 27.39 billion during January-September 2026, while gross profit increased 50% to EGP 14.20 billion. Operating profit also grew 41% to EGP 12.48 billion. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح «موبكو» تقفز 56% خلال 9 أشهر مسجلة 12.14 مليار جنيه
### AMOC
- Sun 15 Nov | ad-hoc-news.de | Alexandria Mineral Oils stock posts 153.7% nine-month profit gain
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/alexandria-mineral-oils-stock-posts-153-7-nine-month-profit-gain/70518306
  > Alexandria Mineral Oils reported a sharp rise in nine-month net profit in a filing published on November 15, 2026. Consolidated net profit for the period ended September 30 reached EGP 3.4749 billion, compared with EGP 1.3700 billion a year earlier, according to The Edge, which calculated the figures from the company's disclosure to the Egyptian Exchange. [Figures on the page: standalone; consolidated. Check which one each figure is.]
### EFID
- Mon 16 Nov | مجلة البوصلة الاقتصادية | ارتفاع أرباح "إيديتا" إلى 2.6 مليار جنيه في 9 أشهر
  https://alboslanews.com/أسواق-مال/ارتفاع-أرباح-إيديتا-إلى-26-مليار-جنيه-في-9-أشهر-430853
  > ارتفاع أرباح "إيديتا" إلى 2.6 مليار جنيه في 9 أشهر الإثنين 16 نوفمبر 2026 -10:45 كشفت القوائم المالية المجمعة لشركة إيديتا للصناعات الغذائية، عن الـ 9 أشهر الأولى من عام 2026، صعودًا في الأرباح، مسجلة 2.61 مليار جنيه، مقابل أرباح بقيمة 1.72 مليار جنيه عن الـ 9 أشهر الأولى من عام 2025. [Figures on the page: standalone; consolidated; nine months; first half. Check which one each figure is.]
- Mon 16 Nov | ايكونومي بلس | أرباح "إيديتا" ترتفع 41.5% إلى 938 مليون جنيه بالربع الثالث
  https://economyplusme.com/ar/news/34197
  > أرباح "إيديتا" ترتفع 41.5% إلى 938 مليون جنيه بالربع الثالث ارتفع صافي ربح شركة "إيديتا للصناعات الغذائية" بنسبة 41.5% خلال الربع الثالث من عام 2026، على أساس سنوي، ليبلغ 938.1 مليون جنيه، مقارنة بالفترة المقابلة من العام السابق. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 16 Nov | اليوم السابع | خريطة الأرباح والخسائر في البورصة.. قفزة قياسية لـ"إيديتا" وتراجع مفاجئ في أرباح "بالم هيلز"
  https://www.youm7.com/story/2026/11/16/خريطة-الأرباح-والخسائر-في-البورصة-قفزة-قياسية-لـ-إيديتا-وتراجع/7620117
  > كشفت النتائج المالية لعدد من الشركات المقيدة بالبورصة المصرية، عن أداء متباين خلال التسعة أشهر الأولى من عام 2026، إذ سجلت شركات بلتون القابضة وإيديتا للصناعات الغذائية وأسمنت سيناء نموًا في الأرباح، فيما حققت ممفيس للأدوية والألومنيوم العربية ارتفاعًا في صافي الربح، رغم تراجع الإيرادات في بعض الأنشطة، بينما أظهرت نتائج بالم هيلز للتعمير نموًا في الإيرادات والأرباح قبل الضرائب، مع انخفاض صافي الربح بعد الضرائب وحصة الأقلية. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | جريدة المال | صافي ربح إيديتا للصناعات الغذائية يقفز إلى 2.6 مليار جنيه في 9 أشهر
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, SWDY, JUFO, EAST, EFIH.
- Already recorded: COMI, ABUK, ETEL, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-16 CLHO results (expected)
- 2026-11-16 EFID results (expected)
- 2026-11-16 JUFO results (expected)
- 2026-11-16 PHDC results (expected)
- 2026-11-16 XOM dividend
- 2026-11-17 EGAL dividend
- 2026-11-17 NVDA results (expected)
- 2026-11-18 EAST results (expected)  <- write its preview
- 2026-11-18 EFIH results (expected)  <- write its preview
- 2026-11-18 HRHO results (expected)
- 2026-11-19 MSFT dividend

## Views
- due 2026-11-20: Brent stays below $105 while Iran talks continue (open)
    Views: nothing to change.

## Fair value
- Changed since the last run: EMFD new at +33%; CANA -34% -> -30% (low -> medium); LCSW -50% -> -48% (medium -> low).
- In the ten cheapest or dearest with no note: EMFD, ADIB, MCQE, SCEM, AMOC, MTIE, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-16. Open each story before using it.
## COMI  (8 leads)
- Mon 16 Nov | بنكي | ياسر عبداللاه رئيسًا تنفيذيًا لقطاع التجزئة المصرفية والشمول المالي بالبنك التجاري الدولي مصر CIB
  https://www.bankygate.com/202578
  > تولى ياسر عبداللاه منصب الرئيس التنفيذي لقطاع التجزئة المصرفية والشمول المالي بالبنك التجاري الدولي – مصر CIB، بعد شغله منصب نائب الرئيس التنفيذي، مستندًا إلى مسيرة مهنية تمتد لنحو 28 عامًا داخل البنك، تولى خلالها عددًا من المسؤوليات والمناصب القيادية.
- Mon 16 Nov | ad-hoc-news.de | Commercial International Bank stock after EGP 63.1bn 9M net income
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/commercial-international-bank-stock-after-egp-63-1bn-9m-net-income/70518455
  > Commercial International Bank (CIB) reported consolidated revenue of EGP 103 billion and net income of EGP 63.1 billion for the first nine months of 2026. The figures were published in the bank's nine-month earnings release dated November 9. Reported net income increased 2 percent from the same period of 2025. [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | بنكي | نشرة بنكي| حسن عبد الله يحصد تقييم B+ من «جلوبال فاينانس».. البنك التجاري الدولي CIB يحصد جائزة أفضل بنك للصرف الأجنبي في مصر 2027 من «جلوبال فاينانس»
  https://www.bankygate.com/202589
  > ترصد نشرة "بنكي" أبرز الأحداث على الساحة المصرفية والمالية اليوم، وأهم ما جاء بها؛
## TMGH  (8 leads)
- Sun 15 Nov | EnterpriseAM | Edita, Valu, TMG, and Bonyan report 9M earnings
  https://enterpriseam.com/egypt/2026/11/16/edita-valu-tmg-and-bonyan-report-9m-earnings/
  > Our friends at Edita saw their net income rose 41.5% y-o-y to EGP 938.1 mn in 3Q 2026, faster than the 32.9% growth in revenue, which reached a record EGP 7.3 bn on 18.5% more packs sold, according to the company’s earnings release (pdf). [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Sun 15 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | صندوق الاستثمارات يوقع مذكرة تفاهم مع مجموعة طلعت مصطفى لتعزيز فرص التعاون
  https://www.argaam.com/ar/article/articledetail/id/1910794
  (page read: it never names the company, so probably not about it: skip)
- Sun 15 Nov | جريدة المال | هشام طلعت مصطفى: الطلب القوي على مجتمعاتنا العمرانية والقدرة على التنفيذ يدعمان مرحلة جديدة من النمو
  https://almalnews.com/2147483/هشام-طلعت-مصطفى-الطلب-القوي-على-مجتمعاتنا/
  > أعلنت مجموعة طلعت مصطفى القابضة تحقيق أداء مالي وتشغيلي قوي خلال الأشهر التسعة الأولى من عام 2026، إذ سجلت إيرادات مجمعة بقيمة 47.6 مليار جنيه، بنمو 24.1% مقارنة بالفترة نفسها من العام الماضي، فيما ارتفع صافي الربح بعد الضرائب بنسبة 18.6% ليصل إلى 15 مليار جنيه، مدعومًا بالنمو القوي لقطاع التطوير العقاري، وتحسن أداء أنشطة ... [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Sun 15 Nov | 25H | أرباح “طلعت مصطفى” تقفز إلى 15 مليار جنيه خلال 9 أشهر.. والإيرادات تسجل 47.6 مليار جنيه بنمو 24%
  https://25h.app/2026/11/15/أرباح-طلعت-مصطفى-تقفز-إلى-15-مليار-جنيه-خ/
  > أرباح “طلعت مصطفى” تقفز إلى 15 مليار جنيه خلال 9 أشهر.. والإيرادات تسجل 47.6 مليار جنيه بنمو 24% [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | www.marketscreener.com | Talaat Moustafa Group Holding Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
  https://www.marketscreener.com/news/talaat-moustafa-group-holding-reports-earnings-results-for-the-third-quarter-and-nine-months-ended-s-ce785ededf89ff21
- Sun 15 Nov | بوابة التكنولوجيا المالية | «طلعت مصطفى»: 4 فنادق قيد التطوير لتعزيز الإيرادات المتكررة بالعملات الأجنبية
  https://www.fintechgate.net/257541
- Sun 15 Nov | بالبلدي | بالبلدي : مجموعة طلعت مصطفى تقفز بأرباحها إلى 15 مليار جنيه خلال 9 أشهر من 2026.. بنمو 19% على أساس سنوي
  https://belbalady.net/7710785
- Sun 15 Nov | بوابة التكنولوجيا المالية | مبيعات مشروع «بنان» التابع ﻟـ«طلعت مصطفى» في السعودية تسجل 13.1 مليار جنيه خلال 9 أشهر
  https://www.fintechgate.net/257530
## ETEL  (8 leads)
- Mon 16 Nov | WebWire | Q3 2026 Results: Telecom Egypt Delivers Strong 9M 2026 Results as Strategy Execution Progresses
  https://www.webwire.com/ViewPressRel.asp?SESSIONID=&aId=364222
  > Q3 2026 Results: Telecom Egypt Delivers Strong 9M 2026 Results as Strategy Execution Progresses 9M 2026 Key Highlights - Total revenue increased 19% YoY to EGP 93.6bn, driven mainly by a 30% YoY increase in Data revenue, followed by a 25% YoY increase in International Incoming Calls revenue. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | https://ekhbary24.com/ | شادي حسين يقود هجوم المقاولون العرب أمام المصرية للاتصالات في كأس مصر
  https://ekhbary24.com/article/56873
  (page: only 68 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 15 Nov | مانكيش نت | المصرية للاتصالات تحقق فوزًا مثيرًا على كهرباء الإسماعيلية
  https://mangish.net/المصرية-للاتصالات-تحقق-فوزًا-مثيرًا-ع/
  (page read: it never names the company, so probably not about it: skip)
## PHDC  (4 leads)
- Mon 16 Nov | اليوم السابع | خريطة الأرباح والخسائر في البورصة.. قفزة قياسية لـ"إيديتا" وتراجع مفاجئ في أرباح "بالم هيلز"
  https://www.youm7.com/story/2026/11/16/خريطة-الأرباح-والخسائر-في-البورصة-قفزة-قياسية-لـ-إيديتا-وتراجع/7620117
  > كشفت النتائج المالية لعدد من الشركات المقيدة بالبورصة المصرية، عن أداء متباين خلال التسعة أشهر الأولى من عام 2026، إذ سجلت شركات بلتون القابضة وإيديتا للصناعات الغذائية وأسمنت سيناء نموًا في الأرباح، فيما حققت ممفيس للأدوية والألومنيوم العربية ارتفاعًا في صافي الربح، رغم تراجع الإيرادات في بعض الأنشطة، بينما أظهرت نتائج بالم هيلز للتعمير نموًا ... [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | مجلة البوصلة الاقتصادية | أرباح "بالم هيلز" تتراجع إلى 3.6 مليار جنيه خلال 9 أشهر
  https://alboslanews.com/أسواق-مال/أرباح-بالم-هيلز-تتراجع-إلى-36-مليار-جنيه-خلال-9-أشهر-430850
  > أرباح "بالم هيلز" تتراجع إلى 3.6 مليار جنيه خلال 9 أشهر الإثنين 16 نوفمبر 2026 -10:35 أظهرت القوائم المالية المجمعة لشركة بالم هيلز للتعمير، عن الـ 9 أشهر الأولى من عام 2026، انخفاضًا في الأرباح، محققة 3.68 مليار جنيه، مقابل أرباح بقيمة 3.7 مليار جنيه عن الـ 9 أشهر الأولى من عام 2025. [Figures on the page: standalone; consolidated; nine months; first half. Check which one each figure is.]
- Sat 14 Nov | نيوز رووم | محاضر بأول أكتوبر ضد «بالم هيلز» وياسين منصور بسبب نزاع على وحدات «بالم فالي»
  https://newsroom.info/484889
  (page: only 24 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 14 Nov | موقع الحرية الإخباري | محاضر ضد «بالم هيلز» وياسين منصور على خلفية بيع وحدات بكمبوند «بالم فالي».. ووزير سابق ضمن أطراف النزاع
  https://alhorianews.com/محاضر-ضد-بالم-هيلز-وياسين-منصور-على-خ/
  > تصاعدت الخلافات بين شركة السعودية للتطوير العمراني وشركة «بالم هيلز» للتعمير بشأن بيع عدد من الوحدات داخل كمبوند «بالم فالي»، لتصل إلى تحرير عدة محاضر ضد الشركة ورئيس مجلس إدارتها ياسين منصور، على خلفية نزاعات تتعلق بعمليات بيع وحدات سكنية لأكثر من طرف، وتضارب المراكز القانونية للمشترين.
## SWDY  (8 leads)
- Mon 16 Nov | Business Insider Africa | India courts Egypt’s $5.7 billion Elsewedy Electric for data centres and smart meters as 132-member business delegation lands in Cairo
  https://africa.businessinsider.com/local/markets/india-courts-egypts-dollar57-billion-elsewedy-electric-for-data-centres-and-smart/9ycb73f
  > - India is seeking deeper cooperation with Elsewedy Electric in data centres, smart meters and electrical equipment. - The Egyptian group recorded more than $5.7 billion in revenue in 2025 and says its meters have surpassed 100 million installations globally.
- Mon 16 Nov | Indian Television Dot Com | Piyush Goyal Meets ElSewedy Electric CEO, Discusses India Investment Opportunities
  https://indiantelevision.com/mam/piyush-goyal-meets-elsewedy-electric-ceo-discusses-india-investment-opportunities/
  > CAIRO: Commerce and Industry Minister Piyush Goyal on November 14 met Ahmed ElSewedy, the President and CEO of ElSewedy Electric, an Egyptian multinational, to explore investment opportunities in India, specifically within the electrical equipment, smart meters, and data centers sectors.
- Sun 15 Nov | ET Manufacturing | Union Minister Goyal meets ElSewedy Electric CEO; discusses investment opportunities in India
  https://manufacturing.economictimes.indiatimes.com/news/industry/union-minister-goyal-meets-elsewedy-electric-ceo-discusses-investment-opportunities-in-india/135854241
  > Cairo: Commerce and Industry Minister Piyush Goyal met Ahmed ElSewedy, President and CEO of the Egyptian multinational ElSewedy Electric, to discuss potential investment opportunities in India.electrical equipment, smart meters, and data centres," Goyal said in a social media post.business delegation.
## ORAS  (4 leads)
- Sun 15 Nov | بالبلدي | بالبلدي : أوراسكوم كونستراكشون تقود تحالفًا لإنشاء محطة رياح بقدرة 900 ميجاوات في مصر
  https://belbalady.net/7710787
  (page: did not load (522))
- Sun 15 Nov | Prop News Time | ENGIE, Aeolus and Orascom Construction achieve financial close for 900 MW wind farm in Egypt
  https://propnewstime.com/latestnewsstories/NDAyNzg=/engie-aeolus-and-orascom-construction-achieve-financial-close-for-900-mw-wind-farm-in-egypt
  > The Gulf conflict has disrupted global supply chains, pushed... REITs have changed the way commercial real estate is owned a... A consortium comprising ENGIE, Aeolus and Orascom Construction has achieved financial close for a 900 MW wind farm near Ras Shokeir on Egypt’s Gulf of Suez coast.
- Sun 15 Nov | شبكة تواصل الإخبارية | «أوراسكوم كونستراكشون» تشارك في تطوير محطة رياح جديدة بقدرة 900 ميغاوات
  https://twaslnews1.twaslnews.com/7723233/
  (page: did not load (URLError))
## FWRY  (8 leads)
- Sun 15 Nov | جريدة البورصة | "فوري" تقرر مضاعفة رأسمالها إلى 3.4 مليار جنيه عبر أسهم مجانية
  https://alborsaanews.com/2026/11/15/2006488
  > وافق مجلس إدارة شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، على توزيع أسهم مجانية على المساهمين بواقع سهم مجاني لكل سهم أصلي. على أن يمول التوزيع من الأرباح المرحلة وأرباح عام 2025، ليرتفع رأس المال المصدر والمدفوع من 1.7 مليار جنيه إلى 3.4 مليار جنيه.
- Sun 15 Nov | Masrawy | فوري تحقق مدفوعات إلكترونية تقترب من تريليون جنيه في 9 أشهر
  https://www.masrawy.com/news/news_economy/details/2026/11/15/3079110/فوري-تحقق-مدفوعات-إلكترونية-تقترب-من-تريليون-جنيه-في-9-أشهر
  > أعلنت شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية ارتفاع إجمالي قيمة المدفوعات خلال أول 9 أشهر من العام الجاري على أساس سنوي بنحو 51.6%، إلى 968.6 مليار جنيه وهو ما يعكس توسع نطاق أعمالها وزيادة حجم المعاملات عبر منصاتها، إلى جانب تنامي قاعدة عملائها وانتشار خدماتها في مختلف أنحاء السوق المصرية.
- Sun 15 Nov | جريدة المال | الأهلي فاروس: فوري تدرس توسعات استراتيجية كبرى برفع رأس المال المرخص إلى 17 مليار جنيه
  https://almalnews.com/2147388/الأهلي-فاروس-فوري-تدرس-توسعات-استراتيجية-كبرى/
  > أصدرت وحدة بحوث «الأهلي فاروس» تقريراً تحليلياً بشأن شركة «فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية»، مجددة توصيتها بشراء السهم مع تحديد قيمته العادلة عند 28.6 جنيه للسهم وفق تقديرات مارس 2026، مؤكدة أن قرارات مجلس الإدارة الأخيرة — وتحديداً مقترح رفع رأس المال المرخص به إلى 17.0 مليار جنيه — تستحضر السوابق التاريخية لأعوام 2021 و2022 ...
## ABUK  (8 leads)
- Sun 15 Nov | القاهرة 24 | هيثم شعبان يجتمع مع مسؤولي أبو قير للأسمدة لبحث تدعيم صفوف الفريق في يناير
  https://www.cairo24.com/2529932
  > هيثم شعبان يجتمع مع مسؤولي أبو قير للأسمدة لبحث تدعيم صفوف الفريق في يناير يعقد هيثم شعبان المدير الفني للفريق الأول لكرة القدم بـ نادي أبوقير للأسمدة اجتماعًا خلال الأسبوع الحالي مع مجلس إدارة النادي، لمناقشة عدد من الملفات الخاصة بالفريق الأول، وأبرزها المراكز التي تحتاج إلى تدعيم.
- Sun 15 Nov | عالم الطاقة | أبوقير للأسمدة تعزز ريادتها في الاستدامة.. توقيع اتفاقية مع الهيئة العربية للتصنيع لتنفيذ المرحلة الثانية
  https://www.alamaltaqa.com/52250
  > أبوقير للأسمدة تعزز ريادتها في الاستدامة.. توقيع اتفاقية مع الهيئة العربية للتصنيع لتنفيذ المرحلة الثانية
- Sun 15 Nov | أموال الغد | أبو قير للأسمدة تبدأ صيانة وتحديث مصنع «أبوقير 2» لمدة أسبوعين
  https://amwalalghad.com/2026/11/15/أبو-قير-للأسمدة-تبدأ-صيانة-وتحديث-مصنع/
  > كشفت شركة أبو قير للأسمدة والصناعات الكيماوية، بدء تنفيذ أعمال الصيانة الدورية وإجراء تحديثات لبعض المعدات بمصنع أبوقير (2)، في إطار خطة الشركة لإدارة وتوزيع الأحمال وتعظيم الاستفادة من حصص الغاز الطبيعي الموردة.
## HRHO  (6 leads)
- Mon 16 Nov | موقع متناهي | مجموعة إي اف چي القابضة تطلق برنامج الادخار لموظفيها بالتعاون مع شركة كاف للتأمين وإي اف چي هيرميس لإدارة الأصول
  https://motanahy.com/مجموعة-إي-اف-چي-القابضة-تطلق-برنامج-الا/
  > أعلنت اليوم مجموعة إي اف چي القابضة، المؤسسة المالية الرائدة التي تمتلك بنكًا شاملًا في مصر وبنك الاستثمار الرائد في الشرق الأوسط وشمال إفريقيا، عن إطلاق برنامج الادخار لموظفيها. وذلك في خطوة تعكس التزام المجموعة بتعزيز الأمان المالي لموظفيها على المدى الطويل، ودعم خططهم المالية لمرحلة التقاعد.
- Sun 15 Nov | ad-hoc-news.de | EFG Holding stock: EFG Hermes completes DIP Holding IPO role
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/efg-holding-stock-efg-hermes-completes-dip-holding-ipo-role/70518373
  > EFG Hermes, the investment-banking arm of EFG Holding, completed its role as joint bookrunner on DIP Holding's initial public offering on the Dubai Financial Market, according to Daily News Egypt. The report was updated on November 11, 2026.
- Sun 15 Nov | EnterpriseAM | THIS MORNING: Eyewa draws attention from KKR and Brookfield + EFG Hermes tapped as co-lead on Emaar Development buyout
  https://enterpriseam.com/uae/2026/11/16/this-morning-eyewa-draws-attention-from-kkr-and-brookfield-efg-hermes-tapped-as-co-lead-on-emaar-development-buyout/
  > When the regional conflict broke out earlier this year, the events calendar was one of the first casualties, with cancellations and postponements across the region. Nine months on, the halls are filling up again, but every booth now has to earn its keep. EFG Hermes is co-leading Emaar’s buyout of its construction arm.
## JUFO  (1 leads)
- Sun 15 Nov | ad-hoc-news.de | Juhayna stock: Nine-month net profit jumps 60.1%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/juhayna-stock-nine-month-net-profit-jumps-60-1/70518382
  > Juhayna Food Industries reported a sharp rise in nine-month earnings on November 11, as sales growth across its dairy, juice and fermented-products businesses lifted profitability. Arab Finance said consolidated net profit attributable to the parent company increased 60.1 percent year on year to EGP 2.035 billion for January through September 2026. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
## ALCN  (4 leads)
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح الإسكندرية لتداول الحاويات ترتفع 15% خلال 9 أشهر بدعم نمو حركة التداول
  https://twaslnews1.twaslnews.com/7731478/
  (page: did not load (URLError))
- Sun 15 Nov | اخبارك نت | أرباح الإسكندرية لتداول الحاويات ترتفع 15% إلى 5.72 مليار جنيه خلال 9 أشهر | أموال الغد
  https://www.akhbarak.net/news/details/49549459/4/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-إلى-5-72-مليار-جنيه-خلال-9-أشهر-أموال-الغد
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع، ارتفاع صافي أرباح الشركة بنسبة 15% خلال التسعة أشهر الأولى من عام 2026، على أساس سنوي.
- Sun 15 Nov | جريدة المال | أرباح الإسكندرية لتداول الحاويات ترتفع 15% لتسجل 5.72 مليار جنيه في 9 أشهر
  https://almalnews.com/2147339/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-لتسجل/
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع عن التسعة أشهر الأولى من العام الجاري، نمو أرباح الشركة على أساس سنوي بنسبة 15%.
## MFPC  (8 leads)
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح موبكو ترتفع 56% إلى 12 مليار جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7753826/
  (page: did not load (URLError))
- Sun 15 Nov | خاص عن مصر | "موبكو" المصرية تقترض 165 مليون دولار لزيادة طاقتها الإنتاجية من الأسمدة
  https://aboutmsr.com/موبكو-المصرية-تقترض-165-مليون-دولار-لزيا/
  > حصلت شركة مصر لإنتاج الأسمدة «موبكو» على موافقة للحصول على قرض بقيمة 165 مليون دولار من مجموعة بنوك، لتمويل جانب من برنامج تطوير وتحديث مصانعها، في خطوة تستهدف زيادة الطاقة الإنتاجية ورفع كفاءة التشغيل وتعزيز قدرتها على التوسع في الأسواق الجديدة. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Sun 15 Nov | جريدة باور نيوز الاخبارية | أرباح موبكو تقفز إلى 12.1 مليار جنيه في 9 أشهر بزيادة قدره نمو 56% مقابل الفترة المماثلة من العام السابق
  https://powernews.cc/?p=294107
  > حققت شركة مصر لإنتاج الأسمدة – موبكو، 56% نموًا في صافي أرباحها بعد الضريبة، ليصل إلى 12.139 مليار جنيه، في أول تسعة أشهر من العام الجاري، مقابل 7.784 مليار جنيه بالفترة المناظرة.
## EAST  (1 leads)
- Mon 16 Nov | ad-hoc-news.de | Eastern Company stock reports sharp nine-month profit growth
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/eastern-company-stock-reports-sharp-nine-month-profit-growth/70518391
  > Eastern Company reported a sharp increase in earnings for the first nine months of 2026, with consolidated net profit reaching about EGP 9 billion, according to Arab Finance. The report was published on November 11, 2026, and said profit increased 39 percent from EGP 6.48 billion in the comparable period. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## EFIH  (8 leads)
- Mon 16 Nov | بوابة التكنولوجيا المالية | «فاروس للبحوث» تتوقع ارتفاع سهم «إي فاينانس» بنسبة 40% من مستوياته الحالية بدعم نمو الأرباح وضم «تمويلي»
  https://fintechgate.net/257582
  > توقعات بوصول أرباح «إي فاينانس» إلى 3.5 مليار جنيه بنهاية 2026 «فاروس للبحوث» تتوقع ارتفاع سهم «إي فاينانس» بنسبة 40% من مستوياته الحالية بدعم نمو الأرباح وضم «تمويلي» [Figures on the page: consolidated; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | نيوز رووم | وزير الاتصالات يشهد توقيع مذكرة تفاهم مع النيابة العامة ووزارة التضامن الاجتماعي وأورنچ و«إي فاينانس»
  https://newsroom.info/485418
  > وزير الاتصالات يشهد توقيع مذكرة تفاهم مع النيابة العامة ووزارة التضامن الاجتماعي وأورنچ و«إي فاينانس» شهد الدكتور رأفت هندي، وزير الاتصالات وتكنولوجيا المعلومات، والمستشار محمد شوقي عياد، النائب العام، والدكتورة مايا مرسي، وزيرة التضامن الاجتماعي، مراسم احتفالية النيابة العامة التي سلطت الضوء على مسيرتها نحو التحول من «العدالة الرقمية» إلى «العدالة الذكية».
- Sun 15 Nov | بوابة المصرف | «الاتصالات» و«التضامن» توقعان بروتوكول تعاون مع «أورانج» و«إي فاينانس» لدعم التحول الرقمي .. تفاصيل
  https://www.almasraf.news/الاتصالات-والتضامن-توقعان-بروتو/
  > وقعت وزارة الاتصالات وتكنولوجيا المعلومات ووزارة التضامن الاجتماعي بروتوكول تعاون مشترك مع شركتي أورانج مصر وإي فاينانس، في إطار تعزيز التعاون بين القطاعين الحكومي والخاص، ودعم جهود الدولة لتطوير الخدمات الرقمية وتيسير وصول المواطنين إليها.
## BQDC  (8 leads)
- Sun 15 Nov | عالم المال | شهادات الادخار في بنك القاهرة
  https://alamalmal.net/tagnews/260946/شهادات-الادخار-في-بنك-القاهرة/1
  (page: only 18 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 15 Nov | صدى البلد | خبير: طرح بنك القاهرة بقيمة 36 مليار جنيه دفعة قوية لبرنامج الطروحات الحكومية
  https://www.elbalad.news/7181046
  > أكد الدكتور حسام عيد، الخبير الاقتصادي ومحلل أسواق المال، أن برنامج الطروحات الحكومية، واختيار بنك القاهرة ليكون أحد أبرز الطروحات المرتقبة، يمثل خطوة إيجابية لدعم سوق المال المصري، خاصة في ظل القيمة المستهدفة للطرح التي تبلغ نحو 36 مليار جنيه، بما يعزز من عمق السوق ويرفع من قدرته على جذب المزيد من الاستثمارات المحلية والأجنبية.
- Sun 15 Nov | شبكة تواصل الإخبارية | المدعى عليهم: أردنيون.. أقامها: بنك القاهرة عمان (أسماء)
  https://twaslnews1.twaslnews.com/7707790/
  (page: did not load (URLError))
## EGAL  (1 leads)
- Mon 16 Nov | مجلة البوصلة الاقتصادية | اليوم.. نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم
  https://alboslanews.com/أسواق-مال/اليوم-نهاية-حق-الحصول-على-التوزيع-النقدي-لـ-مصر-للألومنيوم-430846
  > نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم الإثنين 16 نوفمبر 2026 -10:16 ينتهي مع ختام جلسة اليوم الإثنين حق الحصول على توزيع الكوبون النقدي لشركة مصر للألومنيوم، بواقع 16 جنيه للسهم. على أن يتم صرف التوزيع في 19 نوفمبر 2026، وتتولى التنفيذ شركة مصر للمقاصة والإيداع والقيد المركزي.
## AMOC  (5 leads)
- Sun 15 Nov | ad-hoc-news.de | Alexandria Mineral Oils stock posts 153.7% nine-month profit gain
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/alexandria-mineral-oils-stock-posts-153-7-nine-month-profit-gain/70518306
  > Alexandria Mineral Oils reported a sharp rise in nine-month net profit in a filing published on November 15, 2026. [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Sat 14 Nov | Mubasher | «أموك»: الجمعية العامة توافق على تعديل بعض مواد النظام الأساسي
  https://www.mubasher.info/news/21587038/أموك-الجمعية-العامة-توافق-على-تعديل-بعض-مواد-النظام-الأساسي
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 14 Nov | المصري اليوم | «أموك» تستعد لمضاعفة الحصيلة الدولارية وتوسعات جديدة لزيادة الإنتاج وتنويع المنتجات
  https://www.almasryalyoum.com/news/details/4410264
  > «أموك» تستعد لمضاعفة الحصيلة الدولارية وتوسعات جديدة لزيادة الإنتاج وتنويع المنتجات عقدت شركة الإسكندرية للزيوت المعدنية «أموك» اجتماع الجمعية العامة غير العادية، اليوم، برئاسة الكيميائي ماجد الكُردي، رئيس مجلس الإدارة والعضو المنتدب، بحضور قيادات الهيئة المصرية العامة للبترول وممثلي المساهمين وأعضاء مجلس الإدارة.
## EFID  (8 leads)
- Mon 16 Nov | مجلة البوصلة الاقتصادية | ارتفاع أرباح "إيديتا" إلى 2.6 مليار جنيه في 9 أشهر
  https://alboslanews.com/أسواق-مال/ارتفاع-أرباح-إيديتا-إلى-26-مليار-جنيه-في-9-أشهر-430853
  > ارتفاع أرباح "إيديتا" إلى 2.6 مليار جنيه في 9 أشهر الإثنين 16 نوفمبر 2026 -10:45 كشفت القوائم المالية المجمعة لشركة إيديتا للصناعات الغذائية، عن الـ 9 أشهر الأولى من عام 2026، صعودًا في الأرباح، مسجلة 2.61 مليار جنيه، مقابل أرباح بقيمة 1.72 مليار جنيه عن الـ 9 أشهر الأولى من عام 2025. [Figures on the page: standalone; consolidated; nine months; first half. Check which one each figure is.]
- Mon 16 Nov | ايكونومي بلس | أرباح "إيديتا" ترتفع 41.5% إلى 938 مليون جنيه بالربع الثالث
  https://economyplusme.com/ar/news/34197
  > أرباح "إيديتا" ترتفع 41.5% إلى 938 مليون جنيه بالربع الثالث ارتفع صافي ربح شركة "إيديتا للصناعات الغذائية" بنسبة 41.5% خلال الربع الثالث من عام 2026، على أساس سنوي، ليبلغ 938.1 مليون جنيه، مقارنة بالفترة المقابلة من العام السابق. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 16 Nov | اليوم السابع | خريطة الأرباح والخسائر في البورصة.. قفزة قياسية لـ"إيديتا" وتراجع مفاجئ في أرباح "بالم هيلز"
  https://www.youm7.com/story/2026/11/16/خريطة-الأرباح-والخسائر-في-البورصة-قفزة-قياسية-لـ-إيديتا-وتراجع/7620117
  > كشفت النتائج المالية لعدد من الشركات المقيدة بالبورصة المصرية، عن أداء متباين خلال التسعة أشهر الأولى من عام 2026، إذ سجلت شركات بلتون القابضة وإيديتا للصناعات الغذائية وأسمنت سيناء نموًا في الأرباح، فيما حققت ممفيس للأدوية والألومنيوم العربية ارتفاعًا في صافي الربح، رغم تراجع الإيرادات في بعض الأنشطة، بينما أظهرت نتائج بالم هيلز للتعمير نموًا ... [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
## AAPL  (5 leads)
- Mon 16 Nov | MarketBeat | Apple Inc. $AAPL Position Lowered by Helium Advisors LLC
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-position-lowered-by-helium-advisors-llc-2026-11-16/
  > $AAPL Position Lowered by Helium Advisors LLC - Helium Advisors cut its Apple stake by 31.6% in the third quarter, selling 4,784 shares. It held 10,376 shares worth about $3.46 million at quarter-end; Apple remained its seventh-largest holding.
- Mon 16 Nov | Yahoo Finance | AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
  https://finance.yahoo.com/markets/stocks/articles/aapl-stock-posted-best-week-074605436.html
  > - The glasses, code-named N50, are said to be slimmer than Meta's 2nd Gen Ray-Ban smart glasses. - Apple is the best-performing Magnificent Seven stock in 2026, having risen over 31% already.
- Sun 15 Nov | TradingKey | Apple Stock Tests Key Support as iPhone Duo Launch Puts $318.64 Back in Focus
  https://www.tradingkey.com/analysis/stocks/us-stocks/262160633-apple-stock-iphone-duo-aapl-pivot-319-tradingekey
  > Apple Stock Tests Key Support as iPhone Duo Launch Puts $318.64 Back in Focus Apple’s recent launch of the $1,999 foldable iPhone Duo and pricing adjustments on the iPhone 18 Pro aim to protect gross margins and expand its premium category. [Figures on the page: standalone; one quarter. Check which one each figure is.]
## MSFT  (8 leads)
- Mon 16 Nov | InvestorDaily | Microsoft outage exposes digital resilience gaps
  https://www.investordaily.com.au/microsoft-outage-exposes-digital-resilience-gaps/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | TIKR.com | Microsoft Is the Only Tech Giant Not “Highly Reliant on Advertising” as AI Upends Search
  https://www.tikr.com/blog/microsoft-is-the-only-tech-giant-not-highly-reliant-on-advertising-as-ai-upends-search?
  > - Microsoft briefly passed NVIDIA in market value on November 10, and both ended November 13 near $3.9 trillion. - Ad veteran Joe Marchese says Microsoft is the only one of Alphabet, Meta, Amazon and Microsoft that isn’t highly reliant on advertising.
- Mon 16 Nov | Trefis | Has Microsoft Stock Become A Different Bet?
  https://www.trefis.com/stock/msft/articles/625201/has-microsoft-stock-become-a-different-bet/2026-11-16
  > Has Microsoft Stock Become A Different Bet? For questions about this article or underlying research, email help@trefis.com. Microsoft (MSFT) stock trades at 27.3 times earnings, against 21.9 for the S&P 500.
## NVDA  (8 leads)
- Mon 16 Nov | Bloomberg.com | Nvidia Fallout, Anthropic Listing Squeeze Asian Chip Stocks Anew
  https://www.bloomberg.com/news/articles/2026-11-16/nvidia-fallout-anthropic-listing-squeeze-asian-chip-stocks-anew
  (page: did not load (403))
- Mon 16 Nov | Trefis | NVIDIA Earnings Ahead: What Past Reactions Say About The Stock
  https://www.trefis.com/stock/nvda/articles/625122/nvidia-earnings-ahead-what-past-reactions-say-about-the-stock/2026-11-16
  > NVIDIA Earnings Ahead: What Past Reactions Say About The Stock NVIDIA (NASDAQ:NVDA) is set to report its earnings on Tuesday, November 17, 2026. The company has a market value of about $3.94 trillion.
- Mon 16 Nov | Yahoo Finance Singapore | November 2026 Cash Flow Stocks Like NVIDIA Stock
  https://sg.finance.yahoo.com/news/november-2026-cash-flow-stocks-080926567.html
  > Recent market selloffs have reminded investors that even so called safe havens like Treasuries and gold can drop at the same time as shares. When the usual shock absorbers misfire, predictable cash coming into a business becomes even more valuable, and mispriced cash flows can create quiet pockets of opportunity.
- Mon 16 Nov | Benzinga | Scott Bessent Gives Nvidia 10 Days to Explain China Chip Concerns, Calls for External CEO to Replace Jens
  https://www.benzinga.com/news/politics/26/11/63279833/scott-bessent-gives-nvidia-10-days-to-explain-china-chip-concerns-calls-for-external-ceo-to-replace-jensen-huang-dramatic-shakeup
  (page: did not load (403))
- Mon 16 Nov | CNBC | Jensen Huang's return would boost Nvidia stock: Analyst
  https://www.cnbc.com/video/2026/11/16/jensen-huang-nvidia-shah.html
- Mon 16 Nov | Investing.com | U.S. stock futures fall as investors await Nvidia earnings By Investing.com
  https://www.investing.com/news/stock-market-news/us-stock-futures-little-changed-as-investors-await-nvidia-earnings-5028292
- Mon 16 Nov | Yahoo Finance UK | 3 things to watch with the Nvidia share price
  https://uk.finance.yahoo.com/news/3-things-watch-nvidia-share-072600879.html
- Mon 16 Nov | shattered.io | Nvidia Down 30% as AI Selloff Resumes Before Earnings
  https://shattered.io/nvidia-down-30-percent-ai-selloff-resumes-before-earnings/
## AMZN  (8 leads)
- Mon 16 Nov | JournalArta | Pope Leo Says Blood of Amazon Defenders Demands Justice
  https://journalarta.com/en/2026/11/16/pope-leo-amazon-defenders-justice-pucallpa/
  > Pope Leo Says Blood of Amazon Defenders Demands Justice Pope Leo XIV called for justice for environmental defenders killed while protecting the Amazon during a visit to Pucallpa, Peru.
- Mon 16 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: Bokf Na Boosts Position
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-bokf-na-boosts-position-2026-11-16/
  > $AMZN Stock: Bokf Na Boosts Position - Bokf Na increased its Amazon stake by 2.3% in the third quarter, adding 9,857 shares to hold 437,417 shares valued at about $109 million. - Analyst sentiment remains broadly positive: Amazon has a “Moderate Buy” consensus rating and an average price target of $321.74.
- Mon 16 Nov | JournalArta | Amazon (AMZN) Stock: $266.66, Down 0.29% Nov 13
  https://journalarta.com/en/2026/11/16/amazon-amzn-stock-latest-falls-0-29-on-friday-up-2-8-in-five-sessions/
  > Amazon (AMZN) Stock Latest: Falls 0.29% on Friday, Up 2.8% in Five Sessions Technical analysis of AMZN stock on November 13, 2026: price 266.66 USD, trend uptrend, RSI 57.4, support 240.35, resistance 270.87. Amazon closed Friday, November 13, at $266.66, down 0.29% on the session, according to the Nasdaq market data in the supplied figures.
## GOOGL  (8 leads)
- Mon 16 Nov | Yahoo Finance | Google’s New Gemini Costs Just “$0.82 a Task.” Anthropic’s Best Runs $4.64, Days Before Its IPO
  https://finance.yahoo.com/technology/ai/articles/google-gemini-costs-just-0-021551363.html
  > - Zapier CEO Wade Foster found that Google's new Gemini 4 Hydrogen scored 51.1% on 657 business workflows at about $0.82 a task, against 51.4% at about $4.64 a task for Anthropic's Claude Fable 5.2.
- Sun 15 Nov | Investing.com Australia | Form 4 Alphabet Inc Class A For: 15 November By Investing.com
  https://au.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-15-november-93CH-4771845
  (page: did not load (403))
- Sun 15 Nov | Seeking Alpha | Alphabet: AI Hasn't Killed Search, Its Rebuilt It (NASDAQ:GOOG)
  https://seekingalpha.com/article/4968350-alphabet-ai-hasnt-killed-search-its-rebuilt-it
  (page: did not load (403))
## META  (8 leads)
- Mon 16 Nov | MarketBeat | Brooklyn FI LLC Purchases 3,116 Shares of Meta Platforms, Inc. $META
  https://www.marketbeat.com/instant-alerts/filing-brooklyn-fi-llc-purchases-3116-shares-of-meta-platforms-inc-meta-2026-11-16/
  > Brooklyn FI LLC Purchases 3,116 Shares of Meta Platforms, Inc. - Brooklyn FI LLC increased its Meta stake by 305.5% in the third quarter, buying 3,116 shares and bringing its holdings to 4,136 shares, valued at about $3.0 million.
- Mon 16 Nov | Moomoo | META 261116 850.00C (META261116C850000) Stock Options Chain | Quotes & News
  https://www.moomoo.com/options/META261116C850000-US
  (page: only 10 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | MarketBeat | Meta Platforms, Inc. $META Stock Purchased by Bahl & Gaynor LLC
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-purchased-by-bahl-gaynor-llc-2026-11-16/
  > $META Stock Purchased by Bahl & Gaynor LLC - Bahl & Gaynor increased its Meta stake by 9.4% in the third quarter, adding 15,088 shares to hold 175,233 shares valued at about $127.1 million.
- Mon 16 Nov | Yahoo Finance | AAPL Stock Posted Best Week In 4 Months Amid Nvidia Disruption: Apple Reportedly Plans Smart Glasses To Rival Meta Next Year
  https://finance.yahoo.com/markets/stocks/articles/aapl-stock-posted-best-week-074605436.html
  > - The glasses, code-named N50, are said to be slimmer than Meta's 2nd Gen Ray-Ban smart glasses. - Apple is the best-performing Magnificent Seven stock in 2026, having risen over 31% already.
- Mon 16 Nov | Britannica | Meta Platforms | Facebook, Instagram, WhatsApp, & AI
  https://www.britannica.com/money/Meta-Platforms
- Mon 16 Nov | Phemex | Who Is Mark Zuckerberg? Meta's Founder and CEO
  https://phemex.com/academy/who-is-mark-zuckerberg-meta-founder-and-ceo
- Mon 16 Nov | Investing.com Nigeria | Form 144 Meta Platforms For: 15 November By Investing.com
  https://ng.investing.com/news/stock-market-news/form-144-meta-platforms-for-15-november-93CH-2808746
- Sun 15 Nov | The Motley Fool | Is Meta Stock Still a Buy After Borrowing About $25 Billion This Month?
  https://www.fool.com/investing/2026/11/15/is-meta-stock-still-a-buy-after-borrowing-about-usd25-billion-this-month/
## TSLA  (8 leads)
- Mon 16 Nov | Yahoo Finance | TSLA, SPCX Diverge Overnight As Retail Traders Split On Merger Winner — Could SpaceX Get Tesla’s S&P 500 Seat?
  https://finance.yahoo.com/markets/stocks/articles/tsla-spcx-diverge-overnight-retail-083147590.html
  > TSLA, SPCX Diverge Overnight As Retail Traders Split On Merger Winner — Could SpaceX Get Tesla’s S&P 500 Seat? - A merger could give SpaceX a route into the S&P 500 if the combined company keeps Tesla's seat.
- Mon 16 Nov | Yahoo Finance | Tesla And 2 Top Insider Owned Growth Stocks
  https://finance.yahoo.com/markets/stocks/articles/tesla-2-top-insider-owned-061432207.html
  > Hotter than expected US inflation data has pushed traders to expect more interest rate hikes, which puts a spotlight on businesses that can still grow even as money gets more expensive.
- Mon 16 Nov | Gotrade | Tesla Stock (TSLA) Falls 1.8% to $390.22 (Nov 13)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-16-2026/
  > AI-powered contentSome parts of this article are powered by AI. Tesla (TSLA) closed at $390.22 on November 13, 2026, down 1.82%, while the Nasdaq Composite fell 0.91%. No Tesla-specific cause was reported during the session, as Investopedia said tech stocks fell on the fallout from Nvidia CEO Jensen Huang stepping down.
## JPM  (8 leads)
- Mon 16 Nov | CoinDesk | DBS and JPMorgan link blockchain deposit networks for 24/7 dollar transfers
  https://www.coindesk.com/business/2026/11/16/j-p-morgan-and-dbs-let-clients-move-dollars-across-borders-on-weekends
  (page: did not load (429))
- Mon 16 Nov | 파이낸셜뉴스 | JPMorgan Chase: AI-Driven U.S. Corporate Bond Issuance to Hit 2.8 Quadrillion Won Next Year, a Record
  https://en.fnnews.com/news/202611161030123064
  > JPMorgan Chase & Co. / Yonhap News Agency [Financial News] Spending by major technology companies on building artificial intelligence (AI) infrastructure, coupled with strong refinancing demand, is expected to push U.S. media reports on the 14th (local time), JPMorgan Chase & Co. investment-grade bond issuance at $2.1 trillion (about 2,807 trillion won) in a report.
- Mon 16 Nov | NDTV Profit | Nvidia Faces A New Challenge From The Very Companies Driving The AI Boom, JPMorgan Says
  https://www.ndtvprofit.com/markets/nvidia-faces-a-new-challenge-from-the-very-companies-driving-the-ai-boom-jpmorgan-says-earnings-nvidia-stock-valuations-wall-street-ai-12332210
  (page: did not load (403))
## XOM  (8 leads)
- Mon 16 Nov | Petroleum Australia | ExxonMobil approves next phase of Guyana development with Longtail project
  https://petroleumaustralia.com.au/projects/exxonmobil-approves-next-phase-of-guyana-development-with-longtail-project/
  > ExxonMobil has reached a final investment decision on its US$12.5 billion (AU$18.48 billion) Longtail project offshore Guyana, marking a shift toward natural gas and condensate production in the prolific Stabroek block.
- Mon 16 Nov | MLQ.ai | Exxon approves the $12.5 billion Longtail gas project off Guyana, targeting a 2030 start
  https://mlq.ai/news/exxon-approves-the-125-billion-longtail-gas-project-off-guyana-targeting-a-2030-start/
  > Exxon approves the $12.5 billion Longtail gas project off Guyana, targeting a 2030 start - ExxonMobil took a final investment decision on Nov. 12 to invest $12.5 billion in Longtail, the eighth project on Guyana's Stabroek block, with start-up targeted for 2030 [1][2]. [Figures on the page: unaudited or preliminary; one quarter. Check which one each figure is.]
- Mon 16 Nov | Kalkine | WTI Extends Weekly Decline as Surplus Builds for ExxonMobil (NYSE: XOM) and Woodside (ASX: WDS)
  https://kalkine.com.au/news/commodities/wti-extends-weekly-decline-as-surplus-builds-for-exxonmobil-nyse-xom-and-woodside-asx-wds
  (page: did not load (403))
## AVGO  (8 leads)
- Mon 16 Nov | MarketBeat | Broadcom Inc. $AVGO Stock: AlTi Global Inc. Trims Stake
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-alti-global-inc-trims-stake-2026-11-16/
  > $AVGO Stock: AlTi Global Inc. - AlTi Global cut its Broadcom stake by 43.9% in the third quarter, selling 10,185 shares; it retained 13,025 shares valued at about $4.6 million. - Analyst sentiment remains broadly positive: Broadcom has a “Moderate Buy” consensus and an average price target of $525.19.
- Mon 16 Nov | MarketBeat | Bernicke Wealth Management Ltd. Purchases 10,869 Shares of Broadcom Inc. $AVGO
  https://www.marketbeat.com/instant-alerts/filing-bernicke-wealth-management-ltd-purchases-10869-shares-of-broadcom-inc-avgo-2026-11-16/
  > Bernicke Wealth Management Ltd. Purchases 10,869 Shares of Broadcom Inc. - Bernicke Wealth Management opened a Broadcom position in the third quarter, buying 10,869 shares worth about $3.82 million. The stock represents 0.4% of its portfolio and is its 21st-largest holding.
- Mon 16 Nov | MarketBeat | 36,759 Shares in Broadcom Inc. $AVGO Acquired by BCV Asset Management Inc.
  https://www.marketbeat.com/instant-alerts/filing-36759-shares-in-broadcom-inc-avgo-acquired-by-bcv-asset-management-inc-2026-11-16/
  > 36,759 Shares in Broadcom Inc. $AVGO Acquired by BCV Asset Management Inc. - BCV Asset Management acquired 36,759 Broadcom shares in the third quarter, valued at approximately $12.96 million. - Analyst views were mixed, but the consensus rating remained “Moderate Buy”, with an average price target of $525.19.
- Mon 16 Nov | Trefis | The Dates That Matter Most For Broadcom Shareholders
  https://www.trefis.com/stock/avgo/articles/625174/the-dates-that-matter-most-for-broadcom-shareholders/2026-11-16
  > The Dates That Matter Most For Broadcom Shareholders For questions about this article or underlying research, email help@trefis.com. Broadcom (AVGO) stock lost 18.1% over the six months to November 13, 2026, while the S&P 500 gained 2.6%. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sun 15 Nov | Unisba Media | AVGO Stock Analysis: Is Broadcom Overvalued? (Oct 2026) Dsrb (StKsqJSnMJ)
  https://media.unisba.ac.id/10bd75ae/cc00371cKkgKAjF4HQABOic/?share=telegram&nb=1
- Sun 15 Nov | MarketBeat | Broadcom Inc. $AVGO Stock Acquired by Legacy Trust
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-acquired-by-legacy-trust-2026-11-15/
- Sun 15 Nov | MarketBeat | 11,069 Broadcom Inc. $AVGO Shares Purchased by ICICI Prudential Asset Management Co Ltd
  https://www.marketbeat.com/instant-alerts/filing-11069-broadcom-inc-avgo-shares-purchased-by-icici-prudential-asset-management-co-ltd-2026-11-15/
- Sun 15 Nov | MarketBeat | Broadcom Inc. $AVGO Stock: SVB Wealth LLC Reduces Holdings
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-svb-wealth-llc-reduces-holdings-2026-11-15/
## BRK.B  (8 leads)
- Mon 16 Nov | ad-hoc-news.de | Berkshire Hathaway stock: Yen bond plan, up 0.47% at 540.35 euros
  https://www.ad-hoc-news.de/boerse/news/vorboerse/berkshire-hathaway-stock-yen-bond-plan-up-0-47-at-540-35-euros/70519849
  > Berkshire Hathaway stock traded at 540.35 euros on Lang & Schwarz at 08:40 CET on Monday, November 16, 2026, 0.47 percent above the Xetra close of Friday, November 13, 2026. The conglomerate earns money through insurance, rail transportation, energy, manufacturing, services and investments.
- Mon 16 Nov | ad-hoc-news.de | Berkshire's Rails and Renewables Offset a Costlier GEICO as Buybacks Outrun Forecasts
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-s-rails-and-renewables-offset-a-costlier-geico-as-buybacks-outrun-forecasts/70518838
  > Berkshire Hathaway's third-quarter 2026 results landed with a split personality: the conglomerate's railroad and energy units pushed ahead, while its insurance engine sputtered under the weight of costlier claims.
- Mon 16 Nov | 24/7 Wall St. | In 1952, A North Carolina Man Was The Best Man At His Friend's Wedding. 10 Years Later, He Gave The Groom $125,000 To Invest. The Groom's Name Was Warren Buffett. In 2014, Fred Stanback Donated $397 
  https://247wallst.com/investing/2026/11/15/in-1952-a-north-carolina-man-was-the-best-man-at-his-friends-wedding-10-years-later-he-gave-the-groom-125000-to-invest-the-grooms-name-was-warren-buffett-in-2014-fred-stanback-donated-3
  > In 1952, A North Carolina Man Was The Best Man At His Friend’s Wedding. 10 Years Later, He Gave The Groom $125,000 To Invest. The Groom’s Name Was Warren Buffett. In 2014, Fred Stanback Donated $397 Million In Berkshire Stock To Charity.
## WMT  (8 leads)
- Mon 16 Nov | ad-hoc-news.de | Walmart stock gains 1.55% to EUR 117.35 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/walmart-stock-gains-1-55-to-eur-117-35-before-xetra/70519909
  > Walmart stock traded at 117.35 euros on Lang & Schwarz at 08:53 CET on Monday, November 16, 2026, 1.55 percent above the Xetra close of Friday, November 13, 2026, at EUR 115.56. Walmart has scheduled its fiscal third-quarter earnings conference call for Thursday, November 19, 2026.
- Mon 16 Nov | FXStreet | Walmart, Target, and Nvidia headline a pivotal week for Q3 earnings
  https://www.fxstreet.com/news/walmart-target-and-nvidia-headline-a-pivotal-week-for-q3-earnings-202611160751
  (page: did not load (403))
- Sun 15 Nov | scanx.trade | Walmart Q3FY26 Results: Revenue seen up 5.3% as valuation worries linger
  https://scanx.trade/stock-market-news/companies/walmart-q3fy26-results-revenue-seen-up-5-3-valuation-worries-linger/56307118
  > Walmart Q3FY26 Results: Revenue seen up 5.3% as valuation worries linger - Walmart expects Q3 revenue to rise 5.3% to $187.25 billion - Forward P/E stands at 44.4, exceeding retail sector median of 15 - E-commerce contributes nearly 30% of total sales - Stock formed a golden cross after rising from $102 to $128 [Figures on the page: unaudited or preliminary; one quarter. Check which one each figure is.]
## V  (8 leads)
- Mon 16 Nov | MarketBeat | Visa Inc. $V Stock Position Cut by Bessemer Group Inc.
  https://www.marketbeat.com/instant-alerts/filing-visa-inc-v-stock-position-cut-by-bessemer-group-inc-2026-11-16/
  > $V Stock Position Cut by Bessemer Group Inc. - Bessemer Group cut its Visa position by 6% in the third quarter, selling 111,684 shares and retaining 1.75 million shares valued at about $630 million.
- Mon 16 Nov | The Economic Times | UK student visa applications fall 20% in a year as tighter immigration rules affect overseas recruitment
  https://m.economictimes.com/nri/study/uk-student-visa-applications-fall-20-in-a-year-as-tighter-immigration-rules-affect-overseas-recruitment/articleshow/135875533.cms
  > The decline was particularly sharp in October 2026, when 5,800 applications were submitted, compared with 8,400 in October 2025. This was a year-on-year fall of 31%. Between July and October 2026, the UK received 236,100 student visa applications, down 16% from 282,200 during the same months in 2025.
- Mon 16 Nov | Kalkine Media | Visa (NYSE:V) Gains as Stablecoin Payments Expand
  https://kalkinemedia.com/us/stocks/financial/visa-nysev-gains-as-stablecoin-payments-expand
  > - Visas payments network recorded growth across stablecoin settlement, cross-border services and digital commerce. - Stablecoin settlement activity reached a reported annualised run rate across multiple blockchains. Visa continues to expand its role in global digital payments through stablecoin settlement, artificial intelligence-enabled commerce and cross-border services.
## ORCL  (8 leads)
- Mon 16 Nov | Gotrade | Oracle Stock (ORCL) Falls 1.4% as AI Stocks Slide (Nov 13)
  https://www.heygotrade.com/en/news/oracle-orcl-stock-news-november-16-2026/
  > AI-powered contentSome parts of this article are powered by AI. Oracle (ORCL) fell 1.38% to $125.35 on November 13, 2026, a drop 0.47 percentage points steeper than the Nasdaq Composite. No Oracle-specific cause was reported; per Investopedia, AI-linked tech stocks sank as the market kept reacting to Nvidia CEO Jensen Huang stepping down.
- Sun 15 Nov | FourWeekMBA | Oracle Stock (ORCL): Earnings, Cloud Backlog, Capex and News, Tracked
  https://fourweekmba.com/oracle-stock/
  (page: did not load (403))
- Sun 15 Nov | Yahoo Finance Australia | Oracle Stock And US AI Data Center Winners Worth Watching
  https://au.finance.yahoo.com/news/oracle-stock-us-ai-data-180739534.html
  > Washington is suddenly the main character in the AI chip story, and that pulls US onshore data center infrastructure into the spotlight. Export control noise around Nvidia and China is forcing investors to rethink where future AI computing gets built and who supplies the power, racks, and real estate.
## COST  (8 leads)
- Mon 16 Nov | Brit + Co | 11 New Costco Items To Try In November (Before They Sell Out!)
  https://www.brit.co/costco-new-items-november-2026/
  > Hello, holiday hosting season! A fresh month means Costco’s aisles are officially stocked with the ultimate lineup of festive finds, and trust us, you’ll definitely want to snag these seasonal goodies before they disappear.
- Mon 16 Nov | Investing.com UK | Form 4 Costco Wholesale Corp For: 15 November By Investing.com
  https://uk.investing.com/news/stock-market-news/form-4-costco-wholesale-corp-for-15-november-93CH-4983548
  (page: did not load (403))
- Mon 16 Nov | Yahoo Finance | Costco's $13 billion move challenges its core promise
  https://finance.yahoo.com/markets/stocks/articles/costcos-13-billion-move-challenges-001700350.html
  > Costco has traditionally been very careful when it comes to spending on its stores, its website, and anything that takes away from offering lower prices. CEO Ron Vachris bragged about the company's strategy during its fourth-quarter earnings call.
## NFLX  (8 leads)
- Mon 16 Nov | Trefis | Can Netflix Stock Fall 50%?
  https://www.trefis.com/stock/nflx/articles/625141/can-netflix-stock-fall-50-2/2026-11-16
  > Can Netflix Stock Fall 50%? For questions about this article or underlying research, email help@trefis.com. Netflix (NFLX) stock has fallen 50% or more before, from its high to its low in three of the 15 market shocks it has traded through: the 2011 debt ceiling crisis, the 2022 inflation shock and the 2008-2009 financial crisis.
- Mon 16 Nov | Yahoo | NFLXX-USD Gráfico interactivo de acciones | Netflix tokenized stock (xStock) USD Acciones
  https://es.finance.yahoo.com/chart/NFLXX-USD
  (page: did not load (404))
- Sun 15 Nov | Men's Journal | Tyler Perry’s New Christmas Movie Just Hit No. 1 on Netflix in the US
  https://www.mensjournal.com/entertainment/tyler-perrys-new-christmas-movie-just-hit-no-1-on-netflix-in-the-us
  (page: did not load (403))
## INTC  (8 leads)
- Mon 16 Nov | Seeking Alpha | Intel faces shareholder class action over earnings selloff
  https://seekingalpha.com/news/4672838-intel-faces-shareholder-class-action-over-earnings-selloff
  (page: did not load (403))
- Mon 16 Nov | Electronics For You BUSINESS | Soros Fund Spikes its Stake in Intel to 340M
  https://www.electronicsforyou.biz/industry-buzz/soros-fund-spikes-its-stake-in-intel-to-340m/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | Analytics Insight | Intel Hit with Investor Lawsuit Over Alleged Disclosure Failures, Stock Declines by 29%
  https://www.analyticsinsight.net/news/intel-hit-with-investor-lawsuit-over-alleged-disclosure-failures-stock-declines-by-29
  > Shareholders have sued Intel over hiding information about poor PC sales and unsold stock. The lawsuit comes after Intel's stock fell 28.6% on October 30, 2026, wiping out nearly USD 140 billion in value.
- Mon 16 Nov | TradingKey | Intel Faces Shareholder Class Action, Nvidia Risks Flagged as INTC Falls Nearly 4% Overnight, Threatening to Test $50 Mark
  https://www.tradingkey.com/analysis/stocks/us-stocks/262306500-intel-class-action-lawsuit-stock-falls-nvidia-risk-tradingkey
  > Intel Faces Shareholder Class Action, Nvidia Risks Flagged as INTC Falls Nearly 4% Overnight, Threatening to Test $50 Mark As of the close on November 13, Eastern Time, Intel shares fell 2.52% to $59.66 amid mounting legal pressures.
- Mon 16 Nov | Inshorts | Intel sued by shareholders after $140 bn in market value wiped out in 1 day | Intel shares are up by around 60% this year | Inshorts
  https://inshorts.com/en/news/intel-sued-by-shareholders-after--140-bn-in-market-value-wiped-out-in-1-day-1794812706539
- Mon 16 Nov | Benzinga | Intel Stock Down 3.8% Overnight on Robinhood as Lip-Bu Tan Faces Lawsuit Over PC Slowdown Disclosure
  https://www.benzinga.com/markets/tech/26/11/63279415/intel-lip-bu-tan-shareholder-lawsuit-pc
- Mon 16 Nov | The Statesman | Shareholders sue Intel after 29% stock plunge
  https://www.thestatesman.com/world/shareholders-sue-intel-after-29-stock-plunge-1503663079.html
- Mon 16 Nov | NewsBytes | Why shareholders are suing Intel
  https://www.newsbytesapp.com/news/business/intel-sued-by-shareholders-after-29-stock-plunge/story
## LLY  (8 leads)
- Mon 16 Nov | TradingView | SLS, IBRX And IOVA Join Merck And Lilly On BlackRock’s Q3 Buy List — A Vanguard Unit Adds All Of Them Too
  https://www.tradingview.com/news/stocktwits:a038181f8094b:0-sls-ibrx-and-iova-join-merck-and-lilly-on-blackrock-s-q3-buy-list-a-vanguard-unit-adds-all-of-them-too/
  > SLS, IBRX And IOVA Join Merck And Lilly On BlackRock’s Q3 Buy List — A Vanguard Unit Adds All Of Them Too - IBRX accounted for 5.15 million of the shares. Morgan Stanley cut its IBRX stake by nearly 38% and raised its SLS stake by 22%.
- Mon 16 Nov | TradingView | Price to earnings forward of Eli Lilly & Co Shs Unsponsored Brazilian Depositary Receipt Repr 1/2
  https://www.tradingview.com/symbols/BMFBOVESPA-LILY34/financials-statistics-and-ratios/price-earnings-fwd/
  (page: only 18 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | BigGo Finance | Alteogen's Once-Monthly Obesity Drug Cuts Weight 55.3% in 3 Weeks in Animal Study, Beating Lilly Candidate
  https://finance.biggo.com/news/d13b2a31-b7a7-4e4f-be5c-d24d67a18f50
  > Alteogen's Once-Monthly Obesity Drug Cuts Weight 55.3% in 3 Weeks in Animal Study, Beating Lilly Candidate An obesity treatment candidate that Alteogen (196170) is developing for once-monthly dosing showed greater weight-loss efficacy in animal studies than Eli Lilly's next-generation candidate.
Read 103 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, EMFD, SKPC.
