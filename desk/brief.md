# Desk brief, Monday, November 16, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 277s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-13 (19.3); Treasury yields to 2026-11-13 (10-year 5.15%).
- **valuation**: ok in 21s (GitHub Actions). LLY: $1.38tn, P/E (last 12 months) 45.2, Forecast P/E (fiscal 2026) 40.5 (the four quarters to Sep 2026)
- **movers**: ok in 19s (GitHub Actions). Market values: 18 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 54.5
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 51 stocks, k 16.4%, median P/E 10.1; cheapest MASR +70%, PHAR +52%, ABUK +45%; dearest ARAB -62%, MOIN -65%, BTFH -70%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 131s (GitHub Actions). 
- **leads**: ok in 113s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

## What moved (latest close against the one before)
- EGX30 52,187.20 (+0.31%); EGX70 EWI 18,732.50 (+1.11%); USD/EGP 53.86 (+0.66%); Gold 21K 5,955.00 (-0.33%); Brent 95.84 (-0.06%); S&P 500 7,561.67 (-0.40%); Nasdaq 25,136.27 (-0.91%); Bitcoin 64,355.00 (+0.62%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): AMOC +4.8%, AVGO -4.8%, MFPC +3.7%, ORAS +3.4%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - ORAS: No clear trend: 0.8% below its 50-day average and 23.4% above the 200-day; RSI 52, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 81, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (14.4% over) and its 200-day (13.4% over), though the 50-day is still below the 200-day; RSI 76, stretched after a run: above 70.
    - NVDA: Turning down: below both its 50-day average (24.1% under) and its 200-day (20.2% under), though the 50-day is still above the 200-day; RSI 25, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- None: every one has a reason or is under 5%.

Leads for them (open before using; never guess a reason):
```
EGX: failed (HTTP Error 401: Unauthorized); kept the saved session
EGX week and month: EGX stocks trading at least EGP 1m a day on average (215)
US: the market is trading; kept the saved session
US week and month: US companies worth $10bn or more (846)
EGX30 heatmap: 2026-11-16, 31 members
US heatmap: 2026-11-13, 100 members
Market values: 18 of 39 updated

# EGX 2026-11-12
## INFI +17.5%  Foodico
- no headlines found
## ATLC +8.7%  AT Lease
- no headlines found
## DTPP +8.0%  Delta for Printing & Packaging
- no headlines found
## ROTO +5.9%  Al Rowad
- Mon 16 Nov | صحيفة النهار السعودية | دارة الملك عبدالعزيز تنظم الورشة التعريفية الثانية لبرنامج (الأعمال الكاملة للمؤرخين الرواد) عبر الاتصال المرئي
  https://www.annahar-news.com/news/single/39908
- Mon 16 Nov | المتداول العربي | الولايات المتحدة تختار إنفيديا وأنثروبيك ضمن «الرواد الوطنيين» للذكاء الاصطناعي
  https://www.arabictrader.com/ar/news/economy/236245/الولايات-المتحدة-تختار-إنفيديا-وأنثروبيك-ضمن-«الرواد-الوطنيين»-للذكاء-الاصطناعي
- Sun 15 Nov | شاهد الآن | اتحاد الرواد العرب يوسّع دوره المجتمعي بلجنتين للعمل الخيري وذوي الاحتياجات الخاصة
  https://shahdnow.sa/369889/
- Sun 15 Nov | الموقف الرياضي | بفوزه على الرواد.. الحرية يواصل الضغط على صدارة دوري كرة السلة للسيدات
  https://riadi.alwehda.gov.sy/?p=173711
## HDBK +5.8%  Housing & Development Bank
- Mon 16 Nov | الأسبوع | أعلى عائد على شهادات الادخار 2026.. 19% من بنك التعمير والإسكان و18.85% بالأهلي
  https://www.elaosboa.com/3023462/
- Mon 16 Nov | شبكة تواصل الإخبارية | بنك التعمير والإسكان يوظف 40% من ودائعه في منح القروض بنهاية سبتمبر 2026
  https://twaslnews1.twaslnews.com/7778858/
- Mon 16 Nov | بنكي | بنك التعمير والإسكان يتيح تقسيط اشتراك Castello Gym حتى 12 شهرًا دون فوائد أو مصاريف إدارية
  https://www.bankygate.com/202604
- Mon 16 Nov | almotawwer.com | بنك التعمير والإسكان يطرح تقسيط اشتراك Castello Gym دون فوائد أو مقدم على 12 شهرًا
  https://almotawwer.com/bankers/334261/
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
- Mon 16 Nov | TradingKey | Nu Holdings Jumps 11.75% on a Record $1.1 Billion Profit, and NU Now Tests $13.31
  https://www.tradingkey.com/analysis/stocks/us-stocks/262306866-nu-holdings-jumps-record-profit-nu-tests-13-31-trendline-november-16-2026-tradingkey
- Mon 16 Nov | Simply Wall St | Nu Holdings (NU) Earnings Beat Puts Its Valuation Back In Focus
  https://simplywall.st/stocks/us/banks/nyse-nu/nu-holdings/news/nu-holdings-nu-earnings-beat-puts-its-valuation-back-in-focu
- Mon 16 Nov | Kalkine | Nu Holdings (NYSE: NU) Shares Jump 12% After Record Quarterly Profit and Revenue
  https://kalkine.com.au/news/financial/nu-holdings-nyse-nu-shares-jump-12-after-record-quarterly-profit-and-revenue
- Mon 16 Nov | Moomoo | Nu Holdings (NU) Stock Jumped 12% Friday: What the Options Flow Shows
  https://www.moomoo.com/community/feed/nu-holdings-nu-stock-jumped-12-friday-what-the-options-117623306060181
## CBRS +11.2%  Cerebras Systems
- Mon 16 Nov | Pluang | Cerebras Systems Q3 revenue jumps 55%, EPS beats expectations, signaling strong growth potential.
  https://pluang.com/en/news-feed/cerebras-laporan-keuangan-q3-2026-pertumbuhan-pendapatan-kuat-prospek-positif
- Mon 16 Nov | Trefis | What Moved Cerebras Stock?
  https://www.trefis.com/stock/cbrs/articles/625266/what-moved-cerebras-stock/2026-11-16
- Mon 16 Nov | MarketBeat | Cerebras Systems Inc. $CBRS Stock Sold by Eclipse Operations LLC
  https://www.marketbeat.com/instant-alerts/filing-cerebras-systems-inc-cbrs-stock-sold-by-eclipse-operations-llc-2026-11-16/
- Sun 15 Nov | MarketBeat | Cerebras Systems Inc. $CBRS Stock Purchased by Washington University
  https://www.marketbeat.com/instant-alerts/filing-cerebras-systems-inc-cbrs-stock-purchased-by-washington-university-2026-11-15/
## MOG.B +6.7%  Moog
- Mon 16 Nov | Seeking Alpha | Moog: Still A Buy, But The Easy Money Has Been Made
  https://seekingalpha.com/article/4968583-moog-still-buy-but-easy-money-made
- Sun 15 Nov | Simply Wall St | Moog (MOG.A) Sets Earnings Date, Is The Valuation Discount An Opportunity?
  https://simplywall.st/stocks/us/capital-goods/nyse-mog.a/moog/news/moog-moga-sets-earnings-date-is-the-valuation-discount-an-op
- Sat 14 Nov | Yahoo! Finance Canada | Moog Inc. (MOG-B) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/MOG-B/
- Fri 13 Nov | StockInvest.us | Moog Stock Price Forecast. Should You Buy MOG-A?
  https://stockinvest.us/stock/MOG-A
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
- Mon 16 Nov | Stock Titan | Unity Launches The Unity Fellowship to Support Indie Studios
  https://www.stocktitan.net/news/U/unity-launches-the-unity-fellowship-to-support-indie-kdz70f083mp6.html
- Mon 16 Nov | Yahoo Finance | Why Is Unity Stock Going Up?
  https://finance.yahoo.com/markets/stocks/articles/why-unity-stock-going-114211505.html
- Mon 16 Nov | MarketBeat | Unity Software Inc. (NYSE:U) Stock Has Consensus Target Price of $57.22 According to Brokerages
  https://www.marketbeat.com/instant-alerts/consensus-unity-software-inc-nyse-u-stock-has-consensus-target-price-of-5722-according-to-brokerages-2026-11-16/
- Sun 15 Nov | Simply Wall St | Unity Software CEO, President & Director Matthew Bromberg Sells 29% Of Holding
  https://simplywall.st/stocks/us/software/nyse-u/unity-software/news/unity-software-ceo-president-director-matthew-bromberg-sells
## NBIS -9.9%  Nebius Group
- Mon 16 Nov | Seeking Alpha | Nebius: An Interesting Neocloud Positioned For A Tougher Financing Environment (NASDAQ:NBIS)
  https://seekingalpha.com/article/4968581-nebius-an-interesting-neocloud-positioned-for-a-tougher-financing-environment
- Mon 16 Nov | Seeking Alpha | Nebius: With Jensen Huang Or Without Him, They'll Likely Thrive (Upgrade) (NASDAQ:NBIS)
  https://seekingalpha.com/article/4968577-nebius-with-jensen-huang-or-without-him-theyll-likely-thrive-upgrade
- Mon 16 Nov | Benzinga | Nebius Group Stock Slides Again Monday: What's Going On?
  https://www.benzinga.com/trading-ideas/movers/26/11/63288393/nebius-group-stock-slides-again-monday-whats-going-on
- Mon 16 Nov | Blockchain News | Nebius Group (NBIS) Stock Price Prediction: Data-center delays hit the stock, but brokers are still split on the magnitude of the reset
  https://blockchain.news/news/20261116-price-prediction-nbis-data-center-delays-hit-the-stock
## AMD -8.8%  Advanced Micro Devices
- Mon 16 Nov | Quantisnow | AMD: Amendment: Advanced Micro Devices Inc. filed SEC Form 8-K: Unregistered Sales of Equity Securities
  https://quantisnow.com/insight/amendment-advanced-micro-devices-inc-filed-sec-form-8-k-unregistered-6792810
- Mon 16 Nov | MarketBeat | Vista Capital Partners Inc. Buys 1,393 Shares of Advanced Micro Devices, Inc. $AMD
  https://www.marketbeat.com/instant-alerts/filing-vista-capital-partners-inc-buys-1393-shares-of-advanced-micro-devices-inc-amd-2026-11-16/
- Mon 16 Nov | MarketBeat | Advanced Micro Devices, Inc. $AMD Stock: Wellington Grp LLC Increases Holdings
  https://www.marketbeat.com/instant-alerts/filing-advanced-micro-devices-inc-amd-stock-wellington-grp-llc-increases-holdings-2026-11-16/
- Mon 16 Nov | MarketBeat | Advanced Micro Devices, Inc. $AMD Shares Purchased by Purkiss Capital Advisors LLC
  https://www.marketbeat.com/instant-alerts/filing-advanced-micro-devices-inc-amd-shares-purchased-by-purkiss-capital-advisors-llc-2026-11-16/
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
- Mon 16 Nov | Stock Titan | Dell Technologies Delivers the Trusted Data and AI Infrastructure Foundation Needed to Scale Agentic Enterprise AI
  https://www.stocktitan.net/news/DELL/dell-technologies-delivers-the-trusted-data-and-ai-infrastructure-hpnu89jn5574.html
- Mon 16 Nov | TipRanks | Dell Technologies (DELL) Can Reach New Highs on Backlog and Margins
  https://www.tipranks.com/news/article/dell-technologies-dell-can-reach-new-highs-on-backlog-and-margins
- Mon 16 Nov | Simply Wall St | What Does Dell Technologies (DELL) $95 Billion AI Backlog Mean For Investors?
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
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
- Changed since the last run: ETEL +17% -> +12% (low -> medium).
- In the ten cheapest or dearest with no note: MCQE, EMFD, ADIB, SCEM, MTIE, AMOC, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-16. Open each story before using it.
## COMI  (8 leads)
- Mon 16 Nov | أموال الغد | المصرية للاتصالات والتجاري الدولي وقرة تتصدر الأسهم النشطة بالبورصة بتداولات مليارية
  https://amwalalghad.com/2026/11/16/المصرية-للاتصالات-والتجاري-الدولي-وق/
  > تصدر سهم القاهرة للدواجن قائمة الأسهم المقيدة بالسوق الرئيسي بالبورصة المصرية من حيث قيمة التداول خلال تعاملات الاثنين 16 نوفمبر 2026، بقيمة بلغت 1.789 مليار جنيه، فيما جاء البنك التجاري الدولي – مصر في المركز الثاني بقيمة 1.122 مليار جنيه، تلاه سهم المصرية للاتصالات بقيمة 750.5 مليون جنيه، وفقًا للتقرير اليومي للبورصة المصرية الصادر عن ...
- Mon 16 Nov | بوابة المصرف | "البنك التجاري الدولي" يتصدّر قائمة البنوك المُدرجة بالبورصة في حقوق الملكية
  https://www.almasraf.news/البنك-التجاري-الدولي-يتصدّر-قائمة-ال/
  > تصدر البنك التجاري الدولي – مصر قائمة البنوك المدرجة بالبورصة من حيث قيمة حقوق الملكية، بعدما سجلت نحو 232.87 مليار جنيه بنهاية سبتمبر 2026، بمعدل نمو سنوي بلغ 57.1%، ليعزز صدارته للقائمة مستحوذًا على النصيب الأكبر من إجمالي حقوق الملكية لدى البنوك المدرجة. [Figures on the page: unaudited or preliminary; one quarter. Check which one each figure is.]
- Mon 16 Nov | بوابة المصرف | "التجاري الدولي" يتصدّر ارتفاعات أسهم البنوك بالبورصة.. و"قناة السويس" يتراجع 2.19%
  https://www.almasraf.news/التجاري-الدولي-يتصدّر-ارتفاعات-أسهم/
  > تصدّر سهم البنك التجاري الدولي – مصر (CIB) ارتفاعات قائمة الأسهم المدرجة بقطاع البنوك، بمستهل تعاملات اليوم الإثنين، بنسبة 0.25%، ليصل إلى مستوى 128.83 جنيه، وذلك عبر تداولات بلغت قيمتها على السهم 28.514 مليون جنيه، من خلال تداول 222.026 ألف سهم.
## TMGH  (8 leads)
- Mon 16 Nov | Billionaires.Africa | Egyptian billionaire Hisham Talaat Moustafa's TMG posts $271 million nine-month profit
  https://www.billionaires.africa/2026/11/16/egyptian-billionaire-hisham-talaat-moustafas-tmg-posts-271-million-nine-month-profit/
  > Talaat Moustafa Group Holding, the Egyptian property and hotel developer run by billionaire Hisham Talaat Moustafa, said its profit for the first nine months of 2026 rose 18.6% to EGP15.01 billion ($271.2 million), as home sales picked up and its first handovers at a new project began. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | بنوك اون لاين | بمناسبة البلاك فرايداي.. بنك الإمارات دبي الوطني مصر يقدم تقسيطًا بدون فوائد لمدة 12 شهرًا بالتعاون مع «طلعت مصطفى»
  https://www.bnokonline.com/28690
  > بنك الإمارات دبي الوطني مصر يقدم تقسيطًا بدون فوائد لمدة 12 شهرًا بالتعاون مع «طلعت مصطفى»
- Sun 15 Nov | EnterpriseAM | Edita, Valu, TMG, and Bonyan report 9M earnings
  https://enterpriseam.com/egypt/2026/11/16/edita-valu-tmg-and-bonyan-report-9m-earnings/
  > Our friends at Edita saw their net income rose 41.5% y-o-y to EGP 938.1 mn in 3Q 2026, faster than the 32.9% growth in revenue, which reached a record EGP 7.3 bn on 18.5% more packs sold, according to the company’s earnings release (pdf). [Figures on the page: consolidated; nine months. Check which one each figure is.]
## ETEL  (8 leads)
- Mon 16 Nov | أموال الغد | المصرية للاتصالات والتجاري الدولي وقرة تتصدر الأسهم النشطة بالبورصة بتداولات مليارية
  https://amwalalghad.com/2026/11/16/المصرية-للاتصالات-والتجاري-الدولي-وق/
  > تصدر سهم القاهرة للدواجن قائمة الأسهم المقيدة بالسوق الرئيسي بالبورصة المصرية من حيث قيمة التداول خلال تعاملات الاثنين 16 نوفمبر 2026، بقيمة بلغت 1.789 مليار جنيه، فيما جاء البنك التجاري الدولي – مصر في المركز الثاني بقيمة 1.122 مليار جنيه، تلاه سهم المصرية للاتصالات بقيمة 750.5 مليون جنيه، وفقًا للتقرير اليومي للبورصة المصرية الصادر عن ...
- Mon 16 Nov | جريدة المال | «المصرية للاتصالات» تخفض أرصدة القروض والتسهيلات الائتمانية إلى 56.7 مليار جنيه بنهاية سبتمبر 2026
  https://almalnews.com/2147728/«المصرية-للاتصالات»-تخفض-أرصدة-القروض-والتسهيلات-الائتمانية/
  > كشفت القوائم المالية المستقلة للشركة المصرية للاتصالات عن تراجع إجمالي أرصدة القروض والتسهيلات الائتمانية إلى نحو 56.7 مليار جنيه بنهاية سبتمبر 2026، مقابل 73.77 مليار بنهاية ديسمبر 2025، بانخفاض قدره نحو 17.06 مليار ، وبمعدل تراجع يقترب من 23.1%.
- Mon 16 Nov | ekhbary24.com | المقاولون العرب يهزم المصرية للاتصالات ويتأهل لدور الـ16 بكأس مصر
  https://ekhbary24.com/article/57272
  > حقق فريق المقاولون العرب فوزًا ثمينًا على حساب المصرية للاتصالات «وي» بهدف دون رد، في المباراة التي جمعتهما اليوم الثلاثاء 10 نوفمبر 2026، ضمن منافسات دور الـ32 من بطولة كأس مصر لموسم 2026-2027، ليحسم تأهله إلى دور الـ16. هدف حاسم في الدقائق الأخيرة
- Mon 16 Nov | WebWire | Q3 2026 Results: Telecom Egypt Delivers Strong 9M 2026 Results as Strategy Execution Progresses
  http://webwire.com/ViewPressRel.asp?SESSIONID=&aId=364222
  > Q3 2026 Results: Telecom Egypt Delivers Strong 9M 2026 Results as Strategy Execution Progresses 9M 2026 Key Highlights - Total revenue increased 19% YoY to EGP 93.6bn, driven mainly by a 30% YoY increase in Data revenue, followed by a 25% YoY increase in International Incoming Calls revenue. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | https://ekhbary24.com/ | شادي حسين يقود هجوم المقاولون العرب أمام المصرية للاتصالات في كأس مصر
  https://ekhbary24.com/article/56873
- Sun 15 Nov | مانكيش نت | المصرية للاتصالات تحقق فوزًا مثيرًا على كهرباء الإسماعيلية
  https://mangish.net/المصرية-للاتصالات-تحقق-فوزًا-مثيرًا-ع/
- Sun 15 Nov | آخر خبر | المصرية للاتصالات يهزم كهرباء الإسماعيلية بهدف ويشعل دورى المحترفين
  https://a5r5br.net/egypt/local-sports/8497708-المصرية-للاتصالات-يهزم-كهرباء-الإسماعيلية-بهدف-ويشعل-دورى-المحترفين
- Sun 15 Nov | اليوم السابع | بالأرقام.. المصرية للاتصالات من طفرة الأرباح إلى تطوير البنية التحتية وقفزة السهم 150%
  https://www.youm7.com/story/2026/11/15/بالأرقام-المصرية-للاتصالات-من-طفرة-الأرباح-إلى-تطوير-البنية-التحتية/7619549
## PHDC  (8 leads)
- Mon 16 Nov | جريدة حابي | بالم هيلز تُحقق 3.7 مليار جنيه أرباحًا مجمعة في 9 أشهر
  https://hapijournal.com/2026/11/16/بالم-هيلز-تُحقق-3-7-مليار-جنيه-أرباحًا-مج/
  > رنا ممدوح _ حققت شركة بالم هيلز للتعمير صافي أرباح مجمعة بقيمة 3.688 مليار جنيه، في أول تسعة أشهر من العام الجاري، مقابل 3.700 مليار جنيه بالفترة المناظرة، بانخفاض 0.32%، مع الأخذ في الاعتبار حقوق الأقلية. مجمل ربح النشاط يصعد إلى 11.158 مليار جنيه [Figures on the page: standalone; consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | ArabFinance | بالم هيلز تحقق 3.374 مليار جنيه بنهاية سبتمبر 2026
  https://www.arabfinance.com/ar/news/newdetails/بالم-هيلز-تحقق-3و374-مليار-جنيه-بنهاية-سبتمبر-2026
  > آراب فاينانس: أعلنت شركة بالم هيلز للتعمير (PHDC)، عن نتائج أعمالها المجمعة عن الفترة المالية المنتهية فى 30/09/2026، والتي أظهرت تحقيق صافي ربح بلغ 3.374 مليار جنيه مقابل صافي ربح بلغ 3.542 مليار جنيه عن نفس الفترة من العام السابق. [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Mon 16 Nov | Pioneers Misr | رغم تسجيل 31.8 مليار جنيه إيرادات ..أرباح بالم هيلز للتعمير تتراجع خلال 9 أشهر
  https://pioneersmisr.com/123778/
  > حققت شركة بالم هيلز للتعمير صافي أرباح مجمعة بعد الضرائب بقيمة 3.69 مليار جنيه خلال التسعة أشهر الأولى من عام 2026، مقابل نحو 3.70 مليار جنيه خلال الفترة المقارنة من عام 2025، بتراجع طفيف، فيما ارتفعت إيرادات النشاط إلى 31.8 مليار جنيه مقابل 25.55 مليار جنيه. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## SWDY  (8 leads)
- Mon 16 Nov | Billionaires.Africa | Elsewedy Electric profit rises 20.7% in nine months
  https://www.billionaires.africa/2026/11/16/egyptian-billionaire-ahmed-elsewedys-elsewedy-electric-raises-nine-month-profit-20-7/
  > Egyptian billionaire Ahmed Elsewedy’s industrial group, Elsewedy Electric, increased its net profit by 20.7% in the first nine months of 2026, supported by stronger revenue across its cables, engineering and electrical products businesses. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | Business Insider Africa | India courts Egypt’s $5.7 billion Elsewedy Electric for data centres and smart meters as 132-member business delegation lands in Cairo
  https://africa.businessinsider.com/local/markets/india-courts-egypts-dollar57-billion-elsewedy-electric-for-data-centres-and-smart/9ycb73f
  > - India is seeking deeper cooperation with Elsewedy Electric in data centres, smart meters and electrical equipment. - The Egyptian group recorded more than $5.7 billion in revenue in 2025 and says its meters have surpassed 100 million installations globally.
- Mon 16 Nov | Indian Television Dot Com | Piyush Goyal Meets ElSewedy Electric CEO, Discusses India Investment Opportunities
  https://indiantelevision.com/mam/piyush-goyal-meets-elsewedy-electric-ceo-discusses-india-investment-opportunities/
  > CAIRO: Commerce and Industry Minister Piyush Goyal on November 14 met Ahmed ElSewedy, the President and CEO of ElSewedy Electric, an Egyptian multinational, to explore investment opportunities in India, specifically within the electrical equipment, smart meters, and data centers sectors.
## ORAS  (3 leads)
- Mon 16 Nov | جريدة باور نيوز الاخبارية | تحالف يضم أوراسكوم كونستراكشون يحقق الإغلاق المالي لمشروع رياح جديد في مصر
  https://powernews.cc/?p=294167
  > أعلنت شركة أوراسكوم كونستراكشون أن تحالف «شقير لطاقة الرياح»، الذي يضم شركة إنجي الفرنسية بنسبة 35%، وشركة Aeolus اليابانية بنسبة 40%، وشركة أوراسكوم كونستراكشون بنسبة 25%، قد حقق الإغلاق المالي لمشروع محطة جديدة لطاقة الرياح بقدرة 900 ميغاوات، بالقرب من منطقة رأس شقير على خليج السويس في مصر.
- Sun 15 Nov | Prop News Time | ENGIE, Aeolus and Orascom Construction achieve financial close for 900 MW wind farm in Egypt
  https://propnewstime.com/latestnewsstories/NDAyNzg=/engie-aeolus-and-orascom-construction-achieve-financial-close-for-900-mw-wind-farm-in-egypt
  > The Gulf conflict has disrupted global supply chains, pushed... REITs have changed the way commercial real estate is owned a... A consortium comprising ENGIE, Aeolus and Orascom Construction has achieved financial close for a 900 MW wind farm near Ras Shokeir on Egypt’s Gulf of Suez coast.
- Sun 15 Nov | شبكة تواصل الإخبارية | «أوراسكوم كونستراكشون» تشارك في تطوير محطة رياح جديدة بقدرة 900 ميغاوات
  https://twaslnews1.twaslnews.com/7723233/
  (page: did not load (403))
## FWRY  (8 leads)
- Mon 16 Nov | waya.media | Fawry Allocates USD 1.6M for Technology Investments by End of 2026
  https://waya.media/fawry-allocates-usd-1-6m-for-technology-investments-by-end-of-2026/
  > Fawry is allocating EGP 80 million (approx. USD 1.6M) for investments through the end of 2026. The company also plans to introduce a microinsurance service in 2027. The investment plans reflect Fawry’s continued focus on technology development, with approximately 10% of its revenues directed towards technology investments.
- Sun 15 Nov | جريدة البورصة | "فوري" تقرر مضاعفة رأسمالها إلى 3.4 مليار جنيه عبر أسهم مجانية
  https://alborsaanews.com/2026/11/15/2006488
  > وافق مجلس إدارة شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، على توزيع أسهم مجانية على المساهمين بواقع سهم مجاني لكل سهم أصلي. على أن يمول التوزيع من الأرباح المرحلة وأرباح عام 2025، ليرتفع رأس المال المصدر والمدفوع من 1.7 مليار جنيه إلى 3.4 مليار جنيه.
- Sun 15 Nov | Masrawy | فوري تحقق مدفوعات إلكترونية تقترب من تريليون جنيه في 9 أشهر
  https://www.masrawy.com/news/news_economy/details/2026/11/15/3079110/فوري-تحقق-مدفوعات-إلكترونية-تقترب-من-تريليون-جنيه-في-9-أشهر
  > أعلنت شركة فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية ارتفاع إجمالي قيمة المدفوعات خلال أول 9 أشهر من العام الجاري على أساس سنوي بنحو 51.6%، إلى 968.6 مليار جنيه وهو ما يعكس توسع نطاق أعمالها وزيادة حجم المعاملات عبر منصاتها، إلى جانب تنامي قاعدة عملائها وانتشار خدماتها في مختلف أنحاء السوق المصرية.
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
## HRHO  (8 leads)
- Mon 16 Nov | جريدة المال | التابعة لـ «إي إف چي هيرميس».. «مصر للتعليم» تفتح باب التقديم لمدرستها البريطانية الأولى بالإسكندرية
  https://almalnews.com/2147699/التابعة-لـ-«إي-إف-چي-هيرميس»-«مصر/
  > فتحت منصة مصر للتعليم -المملوكة والمدعومة من إي إف چي هيرميس- باب التقديم للالتحاق بأكاديمية الإسكندرية البريطانية، أول مدرسة تابعة لها في المدينة تعتمد المنهج البريطاني، والمقرر بدء تشغيلها خلال سبتمبر 2027، مع انطلاق العام الدراسي 2027/2028، بطاقة استيعابية مستهدفة تبلغ نحو 1800 طالب عند اكتمال مراحل التشغيل.
- Mon 16 Nov | Forbes Middle East | هيرميس الإمارات تنضم إلى إدارة عرض إعمار للاستحواذ على إعمار للتطوير
  https://www.forbesmiddleeast.com/ar/industry/business/efg-hermes-uae-joins-management-of-emaars-offer-to-acquire-emaar-development
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | زهرة الخليج | «هيرميس» تحتفي ببهجة الرسم في المجمع الثقافي بأبوظبي
  https://www.zahratalkhaleej.ae/article/4706210/-هيرميس--تحتفي-ببهجة-الرسم-في-المجمع-الثقافي-بأبوظبي
  > «هيرميس» تحتفي ببهجة الرسم في المجمع الثقافي بأبوظبي على مدار أربعة أيام حافلة بالحيوية والبهجة، من 12 إلى 15 نوفمبر 2026، تحوّل «المجمع الثقافي» في العاصمة أبوظبي إلى مساحة إبداعية نابضة بالحياة مع استضافة فعالية دار «هيرميس» (Hermès) المتنقلة تحت عنوان «Hermès، من الرسم إلى الحِرفة: حين تعانق الأقلام الورق».
## JUFO  (1 leads)
- Sun 15 Nov | ad-hoc-news.de | Juhayna stock: Nine-month net profit jumps 60.1%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/juhayna-stock-nine-month-net-profit-jumps-60-1/70518382
  > Juhayna Food Industries reported a sharp rise in nine-month earnings on November 11, as sales growth across its dairy, juice and fermented-products businesses lifted profitability. Arab Finance said consolidated net profit attributable to the parent company increased 60.1 percent year on year to EGP 2.035 billion for January through September 2026. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
## ALCN  (4 leads)
- Mon 16 Nov | القاهرة 24 | الإسكندرية لتداول الحاويات تسجل تحفظًا محاسبيًا بشأن عقود حق الانتفاع بقيمة 3.4 مليار جنيه
  https://www.cairo24.com/2530264
  > الإسكندرية لتداول الحاويات تسجل تحفظًا محاسبيًا بشأن عقود حق الانتفاع بقيمة 3.4 مليار جنيه
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح الإسكندرية لتداول الحاويات ترتفع 15% خلال 9 أشهر بدعم نمو حركة التداول
  https://twaslnews1.twaslnews.com/7731478/
  (page: did not load (403))
- Sun 15 Nov | اخبارك نت | أرباح الإسكندرية لتداول الحاويات ترتفع 15% إلى 5.72 مليار جنيه خلال 9 أشهر | أموال الغد
  https://www.akhbarak.net/news/details/49549459/4/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-إلى-5-72-مليار-جنيه-خلال-9-أشهر-أموال-الغد
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع، ارتفاع صافي أرباح الشركة بنسبة 15% خلال التسعة أشهر الأولى من عام 2026، على أساس سنوي.
## MFPC  (8 leads)
- Mon 16 Nov | Dealroom | MOPCO lands $165M loan for $265M plant overhaul
  https://app.dealroom.co/news/note/mopco-lands-165m-loan-for-265m-plant-overhaul
  (page: did not load (403))
- Mon 16 Nov | Egypt Oil & Gas | MOPCO Unveils $265Mn Financing Package for Plant Upgrades
  https://egyptoil-gas.com/news/mopco-secures-165-mn-loan-to-modernize-production-facilities/
  > Misr Fertilizers Production Company (MOPCO), one of Egypt’s largest nitrogen fertiliser and petrochemical producers, has secured a $165 million loan from a banking consortium to finance the development and modernisation of its production facilities.
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح موبكو ترتفع 56% إلى 12 مليار جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7753826/
  (page: did not load (403))
- Sun 15 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 15 Nov | خاص عن مصر | "موبكو" المصرية تقترض 165 مليون دولار لزيادة طاقتها الإنتاجية من الأسمدة
  https://aboutmsr.com/موبكو-المصرية-تقترض-165-مليون-دولار-لزيا/
- Sun 15 Nov | جريدة باور نيوز الاخبارية | أرباح موبكو تقفز إلى 12.1 مليار جنيه في 9 أشهر بزيادة قدره نمو 56% مقابل الفترة المماثلة من العام السابق
  https://powernews.cc/?p=294107
- Sun 15 Nov | جريدة باور نيوز الاخبارية | موبكو تحصل على تمويل بقيمة 165 مليون دولار لتطوير وتحديث مصانعها
  https://powernews.cc/?p=294102
- Sun 15 Nov | شبكة تواصل الإخبارية | موبكو تحصد تمويلًا بـ165 مليون دولار لتحديث مصانعها وتعزيز كفاءتها الإنتاجية
  https://twaslnews1.twaslnews.com/7739727/
## EAST  (1 leads)
- Mon 16 Nov | ad-hoc-news.de | Eastern Company stock reports sharp nine-month profit growth
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/eastern-company-stock-reports-sharp-nine-month-profit-growth/70518391
  > Eastern Company reported a sharp increase in earnings for the first nine months of 2026, with consolidated net profit reaching about EGP 9 billion, according to Arab Finance. The report was published on November 11, 2026, and said profit increased 39 percent from EGP 6.48 billion in the comparable period. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## EFIH  (8 leads)
- Mon 16 Nov | موقع متناهي | رئيس مجموعة إي فاينانس يتوقع استكمال الإجراءات القانونية للاستحواذ على "تمويلي" خلال نوفمبر الجاري
  https://motanahy.com/رئيس-مجموعة-إي-فاينانس-يتوقع-استكمال-ا/
  > توقع إبراهيم سرحان رئيس مجلس الإدارة والعضو المنتدب في مجموعة إي فاينانس للاستثمارات المالية والرقمية استكمال الإجراءات القانونية للاستحواذ على “تمويلي” خلال نوفمبر الجاري . كما توقع مساهمة صفقة “تمويلي” بنحو 200 مليون جنيه في نتائج 2026 حال استكمالها.
- Mon 16 Nov | بوابة التكنولوجيا المالية | «فاروس للبحوث» تتوقع ارتفاع سهم «إي فاينانس» بنسبة 40% من مستوياته الحالية بدعم نمو الأرباح وضم «تمويلي»
  https://fintechgate.net/257582
  > توقعات بوصول أرباح «إي فاينانس» إلى 3.5 مليار جنيه بنهاية 2026 «فاروس للبحوث» تتوقع ارتفاع سهم «إي فاينانس» بنسبة 40% من مستوياته الحالية بدعم نمو الأرباح وضم «تمويلي» [Figures on the page: consolidated; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | نيوز رووم | وزير الاتصالات يشهد توقيع مذكرة تفاهم مع النيابة العامة ووزارة التضامن الاجتماعي وأورنچ و«إي فاينانس»
  https://newsroom.info/485418
  > وزير الاتصالات يشهد توقيع مذكرة تفاهم مع النيابة العامة ووزارة التضامن الاجتماعي وأورنچ و«إي فاينانس» شهد الدكتور رأفت هندي، وزير الاتصالات وتكنولوجيا المعلومات، والمستشار محمد شوقي عياد، النائب العام، والدكتورة مايا مرسي، وزيرة التضامن الاجتماعي، مراسم احتفالية النيابة العامة التي سلطت الضوء على مسيرتها نحو التحول من «العدالة الرقمية» إلى «العدالة الذكية».
## BQDC  (6 leads)
- Mon 16 Nov | شبابيك | وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
  https://shbabbek.com/show/288015
  > وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
- Mon 16 Nov | Zawya | Banque du Caire posts $243mln consolidated net profit in 9M 2026
  https://www.zawya.com/en/capital-markets/corporate-earnings/banque-du-caire-posts-243mln-consolidated-net-profit-in-9m-2026-2277116
  > Banque du Caire delivered solid financial performance during the first nine months of 2026, supported by robust core profitability, healthy business growth, an improving funding mix and a strong capital position. [Figures on the page: standalone; consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Sun 15 Nov | عالم المال | شهادات الادخار في بنك القاهرة
  https://alamalmal.net/tagnews/260946/شهادات-الادخار-في-بنك-القاهرة/1
  (page: only 18 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EGAL  (2 leads)
- Mon 16 Nov | شبكة تواصل الإخبارية | اليوم.. نهاية حق توزيع 16 جنيهًا لسهم “مصر للألومنيوم”
  https://twaslnews1.twaslnews.com/7780978/
  (page: did not load (403))
- Mon 16 Nov | مجلة البوصلة الاقتصادية | اليوم.. نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم
  https://alboslanews.com/أسواق-مال/اليوم-نهاية-حق-الحصول-على-التوزيع-النقدي-لـ-مصر-للألومنيوم-430846
  > نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم الإثنين 16 نوفمبر 2026 -10:16 ينتهي مع ختام جلسة اليوم الإثنين حق الحصول على توزيع الكوبون النقدي لشركة مصر للألومنيوم، بواقع 16 جنيه للسهم. على أن يتم صرف التوزيع في 19 نوفمبر 2026، وتتولى التنفيذ شركة مصر للمقاصة والإيداع والقيد المركزي.
## AMOC  (3 leads)
- Sun 15 Nov | ad-hoc-news.de | Alexandria Mineral Oils stock posts 153.7% nine-month profit gain
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/alexandria-mineral-oils-stock-posts-153-7-nine-month-profit-gain/70518306
  > Alexandria Mineral Oils reported a sharp rise in nine-month net profit in a filing published on November 15, 2026. [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Sat 14 Nov | Mubasher | «أموك»: الجمعية العامة توافق على تعديل بعض مواد النظام الأساسي
  https://www.mubasher.info/news/21587038/أموك-الجمعية-العامة-توافق-على-تعديل-بعض-مواد-النظام-الأساسي
  > القاهرة- مباشر: عقدت شركة الإسكندرية للزيوت المعدنية «أموك» اجتماع الجمعية العامة غير العادية، اليوم، برئاسة الكيميائي ماجد الكُردي، رئيس مجلس الإدارة والعضو المنتدب، وبحضور قيادات الهيئة المصرية العامة للبترول وممثلي المساهمين وأعضاء مجلس الإدارة.
- Sat 14 Nov | المصري اليوم | «أموك» تستعد لمضاعفة الحصيلة الدولارية وتوسعات جديدة لزيادة الإنتاج وتنويع المنتجات
  https://www.almasryalyoum.com/news/details/4410264
  (same wording as the Mubasher story above: one source, not two)
## EFID  (8 leads)
- Mon 16 Nov | عالم المال | أخبار البورصة المصرية اليوم.. «إيديتا» تتصدر الرابحين و«كرستمارك» الأكثر تراجعًا
  https://alamalmal.net/article/943439/أخبار-البورصة-المصرية-اليوم-«إيديتا»-تتصدر-الرابحين
  > تباين أداء الأسهم بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الاثنين 16 نوفمبر 2026، حيث تصدر سهم شركة إيديتا للصناعات الغذائية قائمة الأسهم الأكثر ارتفاعًا بنسبة 7.44%، فيما جاء سهم شركة كرستمارك للمقاولات والتطوير العقاري في صدارة الأسهم الأكثر انخفاضًا بنسبة 20%. الأسهم الأكثر ارتفاعًا بالبورصة المصرية
- Mon 16 Nov | شبكة تواصل الإخبارية | “إيديتا” تقرر تخفيض رأسمالها إلى 416.7 مليون جنيه عبر إعدام أسهم خزينة
  https://twaslnews1.twaslnews.com/7792952/
  (page: did not load (403))
- Mon 16 Nov | جريدة المال | «إيديتا للصناعات الغذائية» تقرر تخفيض رأس المال عبر إعدام أسهم خزينة
  https://almalnews.com/2147686/«إيديتا-للصناعات-الغذائية»-تقرر-تخفيض-رأس-المال/
  > وافق مجلس إدارة شركة إيديتا للصناعات الغذائية، على دعوة الجمعية العامة غير العادية للنظر في تخفيض رأسمال الشركة عبر إعدام أسهم الخزينة. [Figures on the page: standalone; consolidated. Check which one each figure is.]
## AAPL  (8 leads)
- Mon 16 Nov | Traders Union | Apple stock holds steady as buyers defend $353.98 support
  https://tradersunion.com/news/stocks/show/4267825-apple-rises-0-21percent-to-usd355-61/
  (page: did not load (403))
- Mon 16 Nov | MarketBeat | Apple Inc. $AAPL Stock Acquired by One Wealth Capital Management LLC
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-stock-acquired-by-one-wealth-capital-management-llc-2026-11-16/
  > $AAPL Stock Acquired by One Wealth Capital Management LLC - One Wealth Capital Management increased its Apple stake by 91% in the third quarter, adding 9,870 shares to hold 20,716 shares worth about $6.9 million. - Institutional investors own 67.73% of Apple shares.
- Mon 16 Nov | MarketBeat | Apple Inc. $AAPL Stock: Madrona Financial Services LLC Grows Position
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-stock-madrona-financial-services-llc-grows-position-2026-11-16/
  > $AAPL Stock: Madrona Financial Services LLC Grows Position - Madrona Financial Services increased its Apple stake by 12.5% in the third quarter, adding 4,959 shares to hold 44,573 shares worth about $14.8 million.
## MSFT  (8 leads)
- Mon 16 Nov | Traders Union | Proposed policy on Chinese transceivers may raise supply chain uncertainty for Microsoft
  https://tradersunion.com/news/stocks/show/4267817-microsoft-declines-on-us-ban/
  (page: did not load (403))
- Mon 16 Nov | ColombiaOne.com | Microsoft Overtakes Nvidia and Regains Second Place Among the Most Valuable Companies
  https://colombiaone.com/2026/11/16/microsoft-market-value-overtakes-nvidia/
  > Microsoft overtook Nvidia to become the world’s second-most valuable publicly traded company on Nov. 10, 2026, as Nvidia shares fell more than 6% to about US$167, while Microsoft slipped just 0.4% to US$543.25.
- Mon 16 Nov | Seeking Alpha | Microsoft: Assessing The Threat To Office Tools, Reiterate Buy
  https://seekingalpha.com/article/4968441-microsoft-assessing-the-threat-to-office-tools-reiterate-buy
  (page: did not load (403))
## NVDA  (8 leads)
- Mon 16 Nov | The Washington Post | Trump’s stake in Nvidia grew to as much as $62 million before scandal broke out
  https://www.washingtonpost.com/business/2026/11/16/trumps-stake-nvidia-grew-much-62-million-before-scandal-broke-out/
  (page: did not load (TimeoutError))
- Mon 16 Nov | Investing.com | How much could Nvidia stock move tomorrow after earnings?
  https://www.investing.com/news/stock-market-news/how-much-could-nvidia-stock-move-tomorrow-after-earnings-93CH-5030156
  (page: did not load (403))
- Mon 16 Nov | Yahoo Finance | Nvidia can replace Jensen Huang, but not the handshakes behind its chips: Chart of the Day
  https://finance.yahoo.com/markets/article/nvidia-can-replace-jensen-huang-but-not-the-handshakes-behind-its-chips-chart-of-the-day-141658786.html
  > A Jensen Huang comeback is a 1-in-9 long shot on prediction markets, and Dan Ives calls it "ridiculous." Nvidia's (NVDA) supply chain, built on his handshakes, makes it less ridiculous than it sounds.
- Mon 16 Nov | Investing.com | Should investors buy the rare Nvidia stock correction before tomorrow’s earnings? By Investing.com
  https://www.investing.com/news/stock-market-news/should-investors-buy-the-rare-nvidia-stock-correction-before-tomorrows-earnings-93CH-5030072
  (page: did not load (403))
- Mon 16 Nov | Investing.com | TD Cowen cuts Nvidia stock price target on CEO resignation uncertainty
  https://www.investing.com/news/analyst-ratings/td-cowen-cuts-nvidia-stock-price-target-on-ceo-resignation-uncertainty-93CH-5030081
- Mon 16 Nov | Investing.com | Analyst says these are 3 key things for Nvidia’s stock from here
  https://www.investing.com/news/stock-market-news/analyst-says-these-are-3-key-things-for-nvidias-stock-from-here-5029999
- Mon 16 Nov | Yahoo Finance | Buy Nvidia stock or wait? A guide to making the call on any stock.
  https://finance.yahoo.com/personal-finance/investing/article/buy-nvidia-stock-or-wait-a-guide-to-making-the-call-on-any-stock-140000333.html
- Mon 16 Nov | Yahoo Finance | Why neoclouds like CoreWeave probably want to see Jensen Huang return to Nvidia
  https://finance.yahoo.com/technology/article/why-neoclouds-like-coreweave-probably-want-to-see-jensen-huang-return-to-nvidia-133223732.html
## AMZN  (8 leads)
- Mon 16 Nov | Yahoo Finance | Amazon's AWS Strikes $5B Data Center Deal With Blackstone Digital — A Look At Some Key Highlights
  https://finance.yahoo.com/real-estate/articles/amazons-aws-strikes-5b-data-140435240.html
  > - AWS will retain a 25% interest and lease back 100% of the portfolio, comprising 13 newly constructed powered shells across two data center campuses. - The agreement carries a 7% initial capitalization rate and a 12-year initial lease term, extendable to 32 years.
- Mon 16 Nov | Barron's | Vulcan Rocket Mishap Hurts Amazon’s Satellite Aspirations
  https://www.barrons.com/articles/amazon-stock-vulcan-rocket-spacex-ad56d465
  (page: did not load (401))
- Mon 16 Nov | Yahoo Finance | Amazon Just Lost 40 Leo Satellites. The Bigger Problem Is the Rocket It Booked 38 Launches On
  https://finance.yahoo.com/technology/articles/amazon-just-lost-40-leo-124036342.html
  > - A Vulcan rocket failure destroyed 40 Amazon Leo satellites, yet the larger risk is schedule, since Vulcan is the first of 38 launches Amazon bought. - Amazon's backups are thin: New Glenn has been grounded since a May explosion, leaving an Ariane 6 launch as the next flight.
## GOOGL  (8 leads)
- Mon 16 Nov | ad-hoc-news.de | Alphabet's Asian Debt Debut Overshoots Target as AdSense Fine Returns to the Docket
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/alphabet-s-asian-debt-debut-overshoots-target-as-adsense-fine-returns-to-the-docket/70521231
  > Alphabet has raised roughly $3.8 billion from its first-ever bond sales denominated in Hong Kong and Singapore dollars, comfortably clearing the $3 billion combined target it set out with, Reuters reported on Thursday.
- Mon 16 Nov | Seeking Alpha | Seth Klarman's Baupost cuts stake in Alphabet, Union Pacific; adds to CME among Q3 moves
  https://seekingalpha.com/news/4672970-seth-klarmans-baupost-cuts-stake-in-alphabet-union-pacific-adds-to-cme-among-q3-moves
  (page: did not load (403))
- Mon 16 Nov | GuruFocus | Ruane Cunniff's Top Q3 2026 Move: Alphabet Inc at a -3.99% Portf
  https://www.gurufocus.com/news/9201208/ruane-cunniffs-top-q3-2026-move-alphabet-inc-at-a-399-portfolio-impact
  (page: did not load (403))
## META  (8 leads)
- Mon 16 Nov | MarketBeat | Meta's Access to Capital Remains Strong, But Borrowing Is Becoming More Expensive
  https://www.marketbeat.com/articles/metas-access-to-capital-remains-strong-but-borrowing-is-becoming-more-expensive/
  (page: did not load (403))
- Mon 16 Nov | 24/7 Wall St. | Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later
  https://247wallst.com/investing/2026/11/16/meta-plunged-after-earnings-in-2025-too-heres-what-buyers-got-a-year-later/
  > Meta Plunged After Earnings in 2025 Too. Here’s What Buyers Got a Year Later Although Meta Platforms (NASDAQ:META | META Price Prediction) grew third-quarter revenue 26.1%[1] to $64.6 billion, Wall Street sold the stock afterward.
- Mon 16 Nov | MarketBeat | Meta Platforms, Inc. $META Stock: Vestor Capital LLC Decreases Holdings
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-vestor-capital-llc-decreases-holdings-2026-11-16/
  > $META Stock: Vestor Capital LLC Decreases Holdings - Vestor Capital cut its Meta stake by 71.5% in the third quarter, selling 14,391 shares and ending the period with 5,747 shares worth about $4.17 million.
- Mon 16 Nov | MarketBeat | Meta Platforms, Inc. $META Stock Holdings Increased by University of Texas Texas AM Investment Management Co.
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-holdings-increased-by-university-of-texas-texas-am-investment-management-co-2026-11-16/
  > $META Stock Holdings Increased by University of Texas Texas AM Investment Management Co. - University of Texas Texas AM Investment Management Co. increased its Meta stake by 14.3% in the third quarter, adding 3,487 shares to hold 27,856 shares valued at about $20.2 million.
- Mon 16 Nov | MarketBeat | 874 Meta Platforms, Inc. $META Shares Purchased by Fulcrum Asset Management LLP
  https://www.marketbeat.com/instant-alerts/filing-874-meta-platforms-inc-meta-shares-purchased-by-fulcrum-asset-management-llp-2026-11-16/
- Mon 16 Nov | MarketBeat | StoneRidge PMG Advisors LLC Makes New Investment in Meta Platforms, Inc. $META
  https://www.marketbeat.com/instant-alerts/filing-stoneridge-pmg-advisors-llc-makes-new-investment-in-meta-platforms-inc-meta-2026-11-16/
- Mon 16 Nov | MarketBeat | Meta Platforms, Inc. $META Stock: Walter Public Investments Inc. Reduces Stake
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-walter-public-investments-inc-reduces-stake-2026-11-16/
- Mon 16 Nov | MarketBeat | 92,300 Shares of Meta Platforms, Inc. $META Bought by MKP Capital Management L.L.C.
  https://www.marketbeat.com/instant-alerts/filing-92300-shares-of-meta-platforms-inc-meta-bought-by-mkp-capital-management-llc-2026-11-16/
## TSLA  (8 leads)
- Mon 16 Nov | TipRanks | SpaceX CEO Elon Musk Calls 100% Solar Power “Obvious and Trivial” as Tesla (TSLA) Builds $10 Billion Plant
  https://www.tipranks.com/news/spacex-ceo-elon-musk-calls-100-solar-power-obvious-and-trivial-as-tesla-tsla-builds-10-billion-plant
  (page: did not load (403))
- Mon 16 Nov | Investor's Business Daily | Tesla Sells Cybercabs To The Public. It Might Be Because Of A Bet With A YouTuber.
  https://www.investors.com/news/tesla-cybercab-marquess-brownlee-elon-musk-robotaxi/
  > Tesla (TSLA) opened invite-only orders of the Cybercab for select customers, marking the first time the robotaxi-specific model would be available to the general public. The Cybercab itself will cost $29,990, the company announced on Friday.
- Mon 16 Nov | MarketBeat | Tesla, Inc. $TSLA Stock Acquired by Wellington Grp LLC
  https://www.marketbeat.com/instant-alerts/filing-tesla-inc-tsla-stock-acquired-by-wellington-grp-llc-2026-11-16/
  > $TSLA Stock Acquired by Wellington Grp LLC - Wellington Group increased its Tesla position by 31.3% in the third quarter, adding 3,828 shares to hold 16,069 shares valued at about $5.7 million.
## JPM  (8 leads)
- Mon 16 Nov | The Quantum Insider | JPMorgan Chase Tops The 2026 Finance Quantum Index; HSBC, Wells Fargo Share Second Place
  https://thequantuminsider.com/2026/11/16/jpmorgan-chase-tops-the-2026-finance-quantum-index-hsbc-wells-fargo-share-second-place/
  > - JPMorgan Chase leads all 64 financial institutions in the 2026 Quantum Index, ranking first in workforce, R&D and adoption, followed by HSBC and Wells Fargo in joint second. - The index expanded from 28 to 64 institutions, adding insurers, payment networks, asset managers and central banks, with 17 new entrants reaching the top 25.
- Mon 16 Nov | Investing.com UK | JPMorgan stock price target held at $361 by Truist Securities
  https://uk.investing.com/news/stock-market-news/jpmorgan-stock-price-target-held-at-361-by-truist-securities-93CH-4985112
  (page: did not load (403))
- Mon 16 Nov | blockchain.news | IREN Stock Price Prediction: JPMorgan and Goldman cut targets as the chart stays under pressure
  https://blockchain.news/news/20261116-price-prediction-iren-jpmorgan-and-goldman-cut-targets-as
  > Analyst cuts meet a bruised tape IREN stock remains under pressure even after the company posted a strong operational update for fiscal Q1 2027. 5, IREN reported total quarterly revenue of $228 million, up 66% sequentially, while AI Cloud revenue rose 182% sequentially to $200 million.
## XOM  (8 leads)
- Mon 16 Nov | Seeking Alpha | ExxonMobil launches $3B debt buyback across four bond series
  https://seekingalpha.com/news/4673029-exxonmobil-launches-3b-debt-buyback-across-four-bond-series
  (page: did not load (403))
- Mon 16 Nov | Business Wire | ExxonMobil: Cash tender offers to purchase certain outstanding notes
  https://www.businesswire.com/news/home/20261116008533/en/ExxonMobil-Cash-tender-offers-to-purchase-certain-outstanding-notes
  (page: did not load (403))
- Mon 16 Nov | MarketBeat | ProVise Management Group LLC Makes New $27.28 Million Investment in ExxonMobil Corporation $XOM
  https://www.marketbeat.com/instant-alerts/filing-provise-management-group-llc-makes-new-2728-million-investment-in-exxonmobil-corporation-xom-2026-11-16/
  > ProVise Management Group LLC Makes New $27.28 Million Investment in ExxonMobil Corporation $XOM - ProVise Management Group bought 167,609 ExxonMobil shares in the third quarter, worth approximately $27.28 million. The position represents 1.8% of its portfolio and is its 15th-largest holding.
## AVGO  (8 leads)
- Mon 16 Nov | Yahoo Finance | AMD, Broadcom stocks sink on tighter US chips rules, CoreWeave drops
  https://finance.yahoo.com/markets/stocks/article/nvidia-amd-micron-sink-on-us-chips-restrictions-coreweave-tanks-as-cloud-providers-tank-too-142453519.html
  > Semiconductor stocks, along with other AI infrastructure equities, tanked on Monday as investors weighed Nvidia (NVDA) leadership turmoil and tighter US restrictions on overseas access to advanced artificial intelligence chips. Peers AMD (AMD) and Broadcom (AVGO) dropped 5% and 4%, respectively.
- Mon 16 Nov | Benzinga | What's Going On With Broadcom Stock Monday?
  https://www.benzinga.com/markets/tech/26/11/63290142/whats-going-on-with-broadcom-stock-monday-11
  (page: did not load (403))
- Mon 16 Nov | 24/7 Wall St. | Broadcom Management Says AI Chip Revenue to Double to $115 Billion in 2027, Giving Bulls Plenty to Cheer
  https://247wallst.com/investing/2026/11/16/broadcom-management-says-ai-chip-revenue-to-double-to-115-billion-in-2027-giving-bulls-plenty-to-cheer/
  > Broadcom Management Says AI Chip Revenue to Double to $115 Billion in 2027, Giving Bulls Plenty to Cheer This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Mon 16 Nov | FourWeekMBA | Broadcom Trades at 24.8x Its AI Revenue, Nvidia at 11x
  https://fourweekmba.com/ai-broadcom-trades-at-24-8x-its-ai-revenue-nvidia-at-11x/
  (page: did not load (403))
- Mon 16 Nov | Yahoo! Finance Canada | Broadcom (AVGO) Downgraded As Wall Street Questions Its AI Financing Model
  https://ca.finance.yahoo.com/news/broadcom-avgo-downgraded-wall-street-130730831.html
- Mon 16 Nov | MarketBeat | Broadcom Inc. $AVGO Stock Holdings Lessened by King Luther Capital Management Corp
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-holdings-lessened-by-king-luther-capital-management-corp-2026-11-16/
- Mon 16 Nov | MarketBeat | Broadcom Inc. $AVGO Stock: UNIVEST FINANCIAL Corp Boosts Position
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-stock-univest-financial-corp-boosts-position-2026-11-16/
- Mon 16 Nov | MarketBeat | Broadcom Inc. $AVGO Shares Newly Bought by Turn8 Private Wealth Inc.
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-shares-newly-bought-by-turn8-private-wealth-inc-2026-11-16/
## BRK.B  (8 leads)
- Mon 16 Nov | NewsBytes | Warren Buffett donates over 9M Berkshire Hathaway shares
  https://www.newsbytesapp.com/news/business/over-9m-berkshire-hathaway-shares-donated-by-warren-buffett/story
  (page: did not load (403))
- Mon 16 Nov | SSBCrack | Berkshire Hathaway Sells $426 Million More in Stocks Under Greg Abel as Value Opportunities Remain Scarce
  https://news.ssbcrack.com/berkshire-hathaway-sells-426-million-more-in-stocks-under-greg-abel-as-value-opportunities-remain-scarce/
  > Berkshire Hathaway’s new chief executive, Greg Abel, continued the company’s long-running pattern of selling more stocks than it bought, even as he reshaped the conglomerate’s investment portfolio after taking over from Warren Buffett. In the third quarter, Berkshire purchased $2.366 billion in equity securities and sold $2.792 billion, producing net sales of $426 million.
- Mon 16 Nov | The Edge Malaysia | Warren Buffett donates more Berkshire shares, confidence 'as strong as ever'
  https://theedgemalaysia.com/node/826020
  > (Nov 16): Warren Buffett said on Monday he is donating about US$5.47 billion (RM22.4 billion) of his Berkshire Hathaway shares to four charities led by his adult children, and said his confidence in the conglomerate he built over 60 years remains "as strong as ever."
## WMT  (8 leads)
- Mon 16 Nov | Traders Union | Walmart stock weekly forecast: Buyers sustain control while support holds at $123.7
  https://tradersunion.com/news/stocks/show/4268630-walmart-gains-2-05percent-this-week/
  (page: did not load (403))
- Mon 16 Nov | TipRanks | Walmart Appoints Joseph E. Creed to Board of Directors
  https://www.tipranks.com/news/company-announcements/walmart-appoints-joseph-e-creed-to-board-of-directors
  (page: did not load (403))
- Mon 16 Nov | Investing.com Canada | Walmart adds Caterpillar CEO Joe Creed to board of directors By Investing.com
  https://ca.investing.com/news/stock-market-news/walmart-adds-caterpillar-ceo-joe-creed-to-board-of-directors-93CH-4960841
  (page: did not load (403))
## V  (8 leads)
- Mon 16 Nov | Yahoo Finance | Did You Miss Visa Stock?
  https://finance.yahoo.com/markets/stocks/articles/did-miss-visa-stock-114211594.html
  > For questions about this article or underlying research, email help@trefis.com. Visa (V) stock returned 18.9% over the three months to November 13, 2026, while the S&P 500 lost 2.1%.
- Mon 16 Nov | The Globe and Mail | The Zacks Analyst Blog Highlights Visa, ExxonMobil Holdings and Pfizer
  https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/8850969/the-zacks-analyst-blog-highlights-visa-exxonmobil-holdings-and-pfizer/
  > The Zacks Analyst Blog Highlights Visa, ExxonMobil Holdings and Pfizer Chicago, IL – November 16, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Stocks recently featured in the blog include: Visa Inc. Top Stock Reports for Visa, ExxonMobil & Pfizer
- Mon 16 Nov | MarketBeat | Visa Inc. $V Stock Position Cut by Bessemer Group Inc.
  https://www.marketbeat.com/instant-alerts/filing-visa-inc-v-stock-position-cut-by-bessemer-group-inc-2026-11-16/
  > $V Stock Position Cut by Bessemer Group Inc. - Bessemer Group cut its Visa position by 6% in the third quarter, selling 111,684 shares and retaining 1.75 million shares valued at about $630 million.
## ORCL  (8 leads)
- Mon 16 Nov | Yahoo Finance | New Jersey-based Shore Medical Center and Shore Physicians Group Select Oracle Health's New AI-Powered EHR to Create a More Connected Experience for Patients and Care Teams
  https://finance.yahoo.com/healthcare/articles/jersey-based-shore-medical-center-141200352.html
  > Technology will unify Shore Medical Center and Shore Physicians Group to streamline care, improve communication, and enhance the patient experience 16, 2026 /PRNewswire/ -- Shore Medical Center and Shore Physicians Group (Shore) is expanding its longstanding relationship with Oracle Health.
- Mon 16 Nov | ad-hoc-news.de | Oracle's AI Ambitions Meet a $10 Billion Funding Test as Microsoft Lets a Cloud Deal Lapse
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-s-ai-ambitions-meet-a-10-billion-funding-test-as-microsoft-lets-a-cloud-deal-lapse/70521183
  > Oracle is discovering that building out artificial intelligence infrastructure is a two-front campaign: one fought in the capital markets, the other in the shifting loyalties of its partners.
- Mon 16 Nov | The Motley Fool | Larry Ellison Has Lost $145 Billion in Net Worth Over the Past Year as Oracle Stock Fell 59% From Its Peak. Here's Why Oracle's Heavy Concentration in OpenAI Has Wall Street Nervous.
  https://www.fool.com/investing/2026/11/16/larry-ellison-has-lost-145-billion-in-net-worth-ov/
  > The last year has been brutal for Oracle (ORCL -1.39%) stock investors. The company's share price is down roughly 44% over the stretch and roughly 50% from its high, and you can count founder and CEO Larry Ellison among those impacted by the stock's big sell-offs.
## COST  (8 leads)
- Mon 16 Nov | TIKR.com | “Costco Has Terrible Governance,” Says Lean Startup Author. Its Stock Just Hit a Record
  https://www.tikr.com/blog/costco-has-terrible-governance-says-lean-startup-author-its-stock-just-hit-a-record
  > - Costco stock closed at a record high on Nov. 13 after a $30-a-share special dividend worth about $13.3 billion. - Eric Ries says governance ratings punish companies that resist shareholder demands, Costco included.
- Mon 16 Nov | MarketBeat | Costco Wholesale (NASDAQ:COST) Downgraded by Northcoast Research to "Neutral"
  https://www.marketbeat.com/instant-alerts/analyst-costco-wholesale-nasdaq-cost-downgraded-by-northcoast-research-to-neutral-2026-11-16/
  > Costco Wholesale (NASDAQ:COST) Downgraded by Northcoast Research to "Neutral" - Northcoast Research downgraded Costco from “buy” to “neutral.” Other analysts have also trimmed price targets, though the overall consensus remains “Moderate Buy” with an average target of $1,092.23.
- Mon 16 Nov | Business Insider | I'm a dietitian and mom of 2. These 11 Costco buys help me quickly throw together balanced dinners during the week.
  https://www.businessinsider.com/costco-easy-dinners-for-family-dietitian-meal-ideas-shopping-list-2026-11
  > Our family needs dinners that are fast, healthy, and delicious — a tall order for any weeknight, especially when feeding two working parents and two picky toddlers. As a dietitian, I also aim for our meals to be well-rounded, containing protein, starchy carbohydrates, and vegetables.
## NFLX  (8 leads)
- Mon 16 Nov | Zacks Investment Research | Netflix Lowers 2026 Ad Revenue Forecast: Time to Hold the Stock?
  https://www.zacks.com/stock/news/3030333/netflix-lowers-2026-ad-revenue-forecast-time-to-hold-the-stock
  > We use cookies to understand how you use our site and to improve your experience. This includes personalizing content and advertising. Netflix Lowers 2026 Ad Revenue Forecast: Time to Hold the Stock? Netflix lowers its 2026 ad revenue outlook to $2.7B from $3B amid slower rollout of ad capabilities. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | Blockchain News | Netflix (NFLX) Price Prediction: Weak momentum holds as price tests support after mixed earnings and softer guidance
  https://blockchain.news/news/20261116-price-prediction-price-nflx-weak-momentum-holds-as-tests-support
  > Price action: a bounce, but not a repair Netflix (NFLX) is holding just above the lower end of its recent range at $62.57, up 1.69% on the day, but the broader setup still looks damaged.
- Mon 16 Nov | TIKR.com | Trump Backs a Hollywood Tax Break So Movies “Must Stay in America.” Netflix and Disney Could Gain
  https://www.tikr.com/blog/trump-backs-a-hollywood-tax-break-so-movies-must-stay-in-america-netflix-and-disney-could-gain?
  > - President Trump backed a bipartisan bill that would give US film and TV productions a 20% federal tax credit on labor costs. - A credit would lower what Netflix and Disney pay to film in the US, helping cash flow and margins.
## INTC  (8 leads)
- Mon 16 Nov | MLQ.ai | Dragoneer's 13F: $3 billion in new SK hynix and Intel shares, SpaceX stake trimmed 15%
  https://mlq.ai/news/dragoneers-13f-3-billion-in-new-sk-hynix-and-intel-shares-spacex-stake-trimmed-15/
  (page: did not load (403))
- Mon 16 Nov | 24/7 Wall St. | How Much Could a 62-Year-Old Save Moving $900,000 of Intel Stock Out of a 401(k) With the NUA Rule?
  https://247wallst.com/investing/2026/11/16/how-much-could-a-62-year-old-save-moving-900000-of-intel-stock-out-of-a-401k-with-the-nua-rule/
  > How Much Could a 62-Year-Old Save Moving $900,000 of Intel Stock Out of a 401(k) With the NUA Rule? This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them. Intel (NASDAQ:INTC | INTC Price Prediction) has given long-tenured employees a sharp lesson in timing.
- Mon 16 Nov | Benzinga | Intel Stock Falls as Shareholders Sue Over PC Slump Behind 29% One-Day Drop
  https://www.benzinga.com/trading-ideas/movers/26/11/63290500/intel-stock-falls-as-shareholders-sue-over-pc-slump-behind-29-one-day-drop
  (page: did not load (403))
- Mon 16 Nov | TIKR.com | Intel’s CEO Says AI Is Buying “Almost as Many CPUs as GPUs.” AMD and Arm Gain Too
  https://www.tikr.com/blog/intels-ceo-says-ai-is-buying-almost-as-many-cpus-as-gpus-amd-and-arm-gain-too
  > - Intel CEO Lip-Bu Tan says AI systems have gone from about eight GPUs for every CPU to roughly one for one, and in some cases to more CPUs than GPUs. - AI agents depend on general-purpose processors, so more demand for server CPUs helps Intel, AMD and Arm alike.
- Mon 16 Nov | MarketBeat | Vista Capital Partners Inc. Makes New Investment in Intel Corporation $INTC
  https://www.marketbeat.com/instant-alerts/filing-vista-capital-partners-inc-makes-new-investment-in-intel-corporation-intc-2026-11-16/
- Mon 16 Nov | Yahoo Finance | Shareholders sue Intel after its shares plunge nearly 29%
  https://finance.yahoo.com/markets/stocks/articles/shareholders-sue-intel-shares-plunge-134142086.html
- Mon 16 Nov | TradingKey | Intel Drops Over 5% Pre-Market as Company, CEO and CFO Sued by Shareholders With Weak PC Demand in Focus
  https://www.tradingkey.com/analysis/stocks/us-stocks/262307101-intel-drops-over-5-premarket-company-ceo-cfo-shareholder-class-action-lawsuit-tradingkey
- Mon 16 Nov | Quartz | Intel shareholders sue over alleged hidden PC sales slowdown
  https://qz.com/intel-shareholder-lawsuit-pc-sales-slowdown-stock-111626
## LLY  (8 leads)
- Mon 16 Nov | marketscreener.com | Eli Lilly to spend up to $1.5bn to acquire Calytrix Bio
  https://www.marketscreener.com/news/eli-lilly-to-spend-up-to-1-5bn-to-acquire-calytrix-bio-ce785edfd88af225
  (page: did not load (403))
- Mon 16 Nov | Quartz | Eli Lilly is buying a rare blood cancer biotech for up to $1.5 billion
  https://qz.com/eli-lilly-calytrix-bio-acquisition-blood-cancer-111626
  > The deal covers Calytrix's preclinical antibody for essential thrombocythemia and myelofibrosis, with milestone payments included Under the definitive agreement, Calytrix shareholders could receive up to $1.5 billion, made up of an upfront payment and further payments that depend on clinical and regulatory milestones being met, the company said.
- Mon 16 Nov | BioPharma Dive | Lilly adds to buyout streak with $1.5B purchase of startup Calytrix
  https://www.biopharmadive.com/news/lilly-calytrix-bio-acquire-deal-myelofibrosis-essential-thrombocythemiaenial-/874719/
  (page: did not load (403))
Read 93 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, EMFD, SKPC.
