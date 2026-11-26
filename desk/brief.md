# Desk brief, Thursday, November 26, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 28s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-25 (28.29); Treasury yields to 2026-11-25 (10-year 4.85%).
- **valuation**: ok in 22s (GitHub Actions). LLY: $1.31tn, P/E (last 12 months) 43.6, Forecast P/E (fiscal 2026) 39.0 (the four quarters to Sep 2026)
- **movers**: ok in 17s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-09 ABUK results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 45.1
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.7%, median P/E 9.7; cheapest MASR +74%, ABUK +51%, AMOC +48%; dearest MOIN -65%, LCSW -68%, BTFH -70%
- **views**: ok in 0s (GitHub Actions). 2026-10-30-rotation: open -> on track
- **results**: ok in 85s (GitHub Actions). 
- **news**: ok in 124s (GitHub Actions). 
- **leads**: ok in 101s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 2 failed, 12 needed a retry (results_due.py, stock_news.py).

## What moved (latest close against the one before)
- EGX30 50,538.70 (-0.68%); EGX70 EWI 16,886.70 (-1.32%); USD/EGP 54.76 (+0.98%); Gold 21K 5,635.00 (-0.79%); Brent 94.61 (+3.51%); S&P 500 7,182.78 (-0.25%); Nasdaq 23,585.80 (-0.62%); Bitcoin 60,539.00 (+1.32%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): ORCL -5.1%, NVDA -3.9%, META +3.4%, AMZN -3.1%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - WMT: Turning up: above both its 50-day average (11.7% over) and its 200-day (10.7% over), though the 50-day is still below the 200-day; RSI 70, stretched after a run: above 70; momentum turned up today (MACD crossed its signal line).

## Movers that still need a reason (top five each way, 5% or more)
- EGX SPIN (Alexandria Spinning & Weaving) +8.1%; EGX ZEOT (Extracted Oils & Derivatives) +5.7%; EGX HBCO (Heibco for Commercial Investments & Real Estate Development) +5.5%; EGX CPME (Catalyst Partners Middle East) +5.5%; EGX VERT (Vertika for Industry & Trade) -10.0%; EGX GTWL (Goldentex) -7.4%; EGX ADCI (Arab Pharmaceuticals) -7.3%; EGX CRST (Creast mark For Contracting) -6.3%; EGX ACAP (A Capital Holding) -5.3%; US HPQ (HP) +11.5%; US ASTS (AST SpaceMobile) +10.3%; US QXO (QXO) +8.6%; US CHTR (Charter Communications) +8.4%; US BSP (Bending Spoons S.p.A) +8.0%; US NTNX (Nutanix) -15.2%; US LRCX (Lam Research) -5.7%; US SNDK (Sandisk) -5.6%; US WSO.B (Watsco) -5.4%; US ORCL (Oracle) -5.1%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-25 (TradingView's closes; Mubasher's list refused), 195 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (207)
US: 2026-11-25, 836 companies
US week and month: US companies worth $10bn or more (835)
EGX30 heatmap: 2026-11-25, 31 members
US heatmap: 2026-11-25, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-25
## SPIN +8.1%  Alexandria Spinning & Weaving
- no headlines found
## ZEOT +5.7%  Extracted Oils & Derivatives
- no headlines found
## HBCO +5.5%  Heibco for Commercial Investments & Real Estate Development
- no headlines found
## CPME +5.5%  Catalyst Partners Middle East
- no headlines found
## IBCT +4.5%  International Business Corp. for Trading & Agencies
- no headlines found
## VERT -10.0%  Vertika for Industry & Trade
- no headlines found
## GTWL -7.4%  Goldentex
- Wed 25 Nov | خاص عن مصر | حركة أسهم البورصة المصرية│ "سبينالكس" تتصدر الارتفاعات بـ7%.. و"جولدن تكس" الأكثر تراجعًا
  https://aboutmsr.com/حركة-أسهم-البورصة-المصرية│-سبينالكس/
  > تصدر سهم الإسكندرية للغزل والنسيج «سبينالكس» قائمة الأسهم الأكثر ارتفاعًا بالبورصة المصرية خلال تعاملات جلسة الأربعاء، بعدما صعد بنسبة 7%، فيما تصدر سهم جولدن تكس للأصواف قائمة الأسهم الأكثر تراجعاً بانخفاض 7.37%، وسط موجة هبوط جماعية شهدتها السوق.
- Wed 25 Nov | Pioneers Misr | «بي دي أو كيز» تحدد القيمة العادلة لسهم «جولدن تكس» عند 111.6 جنيه قبل زيادة رأس المال
  https://pioneersmisr.com/124454/
  > قدرت شركة «بي دي أو كيز للاستشارات المالية عن الأوراق المالية» القيمة العادلة لسهم شركة «جولدن تكس للأصواف» عند 111.61 جنيه، بإجمالي قيمة لحقوق المساهمين بلغت 1.594 مليار جنيه (1,594,125 ألف جنيه) موزعة على 14,283,363 سهماً في تاريخ التقييم 30 يونيو 2026، وذلك في إطار إجراءات زيادة رأس المال.
- Wed 25 Nov | اخبارك نت | «جولدن تكس» تعتمد القيمة العادلة لسهمها عند 111.61 جنيه تمهيدًا لزيادة رأس المال إلى 500 مليون جنيه | أموال الغد
  https://www.akhbarak.net/news/details/49570406/4/جولدن-تكس-تعتمد-القيمة-العادلة-لسهمها-عند-111-61-جنيه-تمهيد-ا-لزيادة-رأس-المال-إلى-500-مليون-جنيه-أموال-الغد
  > اعتمد مجلس إدارة شركة «جولدن تكس للأصواف» تقرير القيمة العادلة لسهم الشركة، الصادر عن المستشار المالي المستقل شركة BDO كيز للاستشارات المالية عن الأوراق المالية، والذي حدد القيمة العادلة للسهم عند 111.61 جنيه.
- Wed 25 Nov | شبكة تواصل الإخبارية | «PKF» تحدد القيمة العادلة لسهم جولدن تكس للأصواف عند 111.61 جنيه
  https://twaslnews1.twaslnews.com/8278096/
  (page: did not load (403))
## ADCI -7.3%  Arab Pharmaceuticals
- no headlines found
## CRST -6.3%  Creast mark For Contracting
- no headlines found
## ACAP -5.3%  A Capital Holding
- no headlines found

# US 2026-11-25
## HPQ +11.5%  HP
- Thu 26 Nov | TradingView | HPQ: HP Jumps More Than 11% as Earnings Beat Cuts Through Tech Selloff
  https://www.tradingview.com/news/tradingview:8531331ea094b:0-hpq-hp-jumps-more-than-11-as-earnings-beat-cuts-through-tech-selloff/
  > HPQ: HP Jumps More Than 11% as Earnings Beat Cuts Through Tech Selloff - Earnings beat powers an 11% rally 💻 HP finds bidders as tech falters - HP shares HPQ surged 11.5% Wednesday after reporting fiscal fourth-quarter results late Tuesday.
- Thu 26 Nov | Investing.com | HP stock rating downgraded by HSBC on weak FY27 guidance, tariff concerns
  https://www.investing.com/news/analyst-ratings/hp-stock-rating-downgraded-by-hsbc-on-weak-fy27-guidance-tariff-concerns-93CH-5052123
  (page: did not load (403))
- Thu 26 Nov | Yahoo Finance | HP Inc. (HPQ) Explodes After Delivering This Double Dose of Good News
  https://finance.yahoo.com/markets/stocks/articles/hp-inc-hpq-explodes-delivering-061805487.html
  > (NYSE:HPQ) is one of the 10 Stocks Stealing the Spotlight. bounced back from losses on Wednesday, surging 11.57 percent to close at $31.15 apiece after reporting strong revenues in the fourth quarter of the fiscal period and raising its next quarterly dividend payments.
- Thu 26 Nov | MarketBeat | HP (NYSE:HPQ) Stock Price Crosses Above Fifty Day Moving Average Following Analyst Downgrade
  https://www.marketbeat.com/instant-alerts/price-hp-nyse-hpq-stock-price-crosses-above-fifty-day-moving-average-following-analyst-downgrade-2026-11-25/
  > HP (NYSE:HPQ) Stock Price Crosses Above Fifty Day Moving Average Following Analyst Downgrade - HP shares moved above their 50-day moving average, trading at $31.15.
## ASTS +10.3%  AST SpaceMobile
- Thu 26 Nov | Yahoo Finance | AST SpaceMobile (ASTS) Stages Impressive Comeback From Record Low
  https://finance.yahoo.com/markets/stocks/articles/ast-spacemobile-asts-stages-impressive-060124396.html
  > (NASDAQ:ASTS) is one of the 10 Stocks Stealing the Spotlight. (NASDAQ:ASTS) soared by 10.25 percent on Wednesday to end at $26.02 apiece, as investors resorted to bargain-hunting after its shares fell to a record low in intraday trade.
- Wed 25 Nov | MarketBeat | AST SpaceMobile (NASDAQ:ASTS) Stock Price Up 10.3% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-ast-spacemobile-nasdaq-asts-stock-price-up-103-heres-what-happened-2026-11-25/
  > AST SpaceMobile (NASDAQ:ASTS) Stock Price Up 10.3% - Here's What Happened - AST SpaceMobile shares rose 10.3% to $26.02, with trading volume 55% above its average; the article did not identify a definitive catalyst, and noted the move came amid volatility in space stocks.
- Wed 25 Nov | Around Prague | Why Is AST SpaceMobile Stock Up Today? Shares Jump 12% to $26.44 in a Dip-Buying Rebound
  https://aroundprague.cz/en/news/us/why-is-ast-spacemobile-stock-up-today-shares-jump-12-to-26-44-in-a-dip-buying
  (page: did not load (403))
- Wed 25 Nov | 24/7 Wall St. | AST SpaceMobile Surges 9%, Erasing Early Losses as Space Stocks Diverge; SpaceX Eases, Rocket Lab Holds Steady
  https://247wallst.com/investing/2026/11/25/ast-spacemobile-surges-9-erasing-early-losses-as-space-stocks-diverge-spacex-eases-rocket-lab-holds-steady/
  > AST SpaceMobile Surges 9%, Erasing Early Losses as Space Stocks Diverge; SpaceX Eases, Rocket Lab Holds Steady This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
## QXO +8.6%  QXO
- Thu 26 Nov | Yahoo! Finance Canada | QXO, Inc. (QXO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/QXO/
  > NYSE - Nasdaq Real Time Price  USD       QXO, Inc. - Previous Close  11.02 - Day's Range  10.48 - 12.20 - 52 Week Range  10.04 - 27.61 - Market Cap (intraday)  12.448B - Beta (5Y Monthly) -- - 1y Target Est  --
- Thu 26 Nov | Yahoo Finance | QXO Inc. (QXO) Gets 9% Boost From Wall Street
  https://finance.yahoo.com/markets/stocks/articles/qxo-inc-qxo-gets-9-040757183.html
  > (NYSE:QXO) is one of the 10 Stocks Stealing the Spotlight. QXO saw its share price jump by 8.62 percent on Wednesday to end at $11.97 apiece after earning a bullish rating and a higher price target from BTIG.
- Wed 25 Nov | Quiver Quantitative | QXO gains as investors digest strong Q3 results and fresh analyst support
  https://www.quiverquant.com/news/QXO+gains+as+investors+digest+strong+Q3+results+and+fresh+analyst+support
  > (QXO) is up 8.5% today. Here is some analysis on what might have caused this price movement. Analysis: The most likely driver appears to be a continued positive reaction to QXO’s recent third-quarter results, which showed sharp sales and adjusted EBITDA growth following major acquisitions. QXO, SEC, Google Finance
- Wed 25 Nov | Yahoo Finance | QXO261127C00017000 Interactive Stock Chart | QXO Nov 2026 17.000 call Stock
  https://finance.yahoo.com/chart/QXO261127C00017000
  (page: did not load (404))
## CHTR +8.4%  Charter Communications
- Thu 26 Nov | Simply Wall St | Charter Communications (CHTR) Jumped, What Is Behind The Fresh Attention?
  https://simplywall.st/stocks/us/media/nasdaq-chtr/charter-communications/news/charter-communications-chtr-jumped-what-is-behind-the-fresh
  > Charter Communications (CHTR) moved into the spotlight after its latest quarterly update combined mixed broadband trends with the closing of its Cox Communications deal and a new Internet first cost cutting program.
- Wed 25 Nov | kalkine.com | Charter Communications (NASDAQ:CHTR) Reports Quarterly Results, Franchise Impairment and Operating Model: Stock Sees Heavy Trading Activity
  https://kalkine.com/news/technology/charter-communications-nasdaqchtr-reports-quarterly-results-franchise-impairment-and-operating-model-stock-sees-heavy-trading-activity
  > - Third quarter 2026 revenues were $14,922 million, and net loss attributable to Charter shareholders was $2,397 million. - The quarter included a $6,326 million Impairment of franchises, and the loss was $20.50 per diluted share. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Wed 25 Nov | MarketBeat | Charter Communications (NASDAQ:CHTR) Shares Up 4.1% - Should You Buy?
  https://www.marketbeat.com/instant-alerts/price-charter-communications-nasdaq-chtr-shares-up-41-should-you-buy-2026-11-25/
  > Charter Communications (NASDAQ:CHTR) Shares Up 4.1% - Should You Buy? - Charter shares rose 4.1% to about $141.41, though trading volume was 72% below its daily average.
- Wed 25 Nov | GuruFocus | Charter Communications (CHTR) Stock Is Up 7.4% Today Without Com
  https://www.gurufocus.com/news/9220680/charter-communications-chtr-stock-is-up-74-today-without-company-news
  (page: did not load (403))
## BSP +8.0%  Bending Spoons S.p.A
- Wed 25 Nov | Yahoo Finance UK | Bending Spoons S.p.A. (BSP) stock price, news, quote and history
  https://uk.finance.yahoo.com/quote/BSP/
  > - Previous close  42.86 - Bid 34.00 x 100 - Ask 51.26 x 200 - Day's range  39.95 - 46.42 - 52-week range  30.11 - 59.50 - Market cap (intra-day)  30.4B - Beta (5Y monthly) -- - PE ratio (TTM)  107.65 - EPS (TTM)  0.43
- Tue 24 Nov | MarketBeat | Stock Traders Purchase High Volume of Bending Spoons Call Options (NASDAQ:BSP)
  https://www.marketbeat.com/instant-alerts/options-stock-traders-purchase-high-volume-of-bending-spoons-call-options-nasdaq-bsp-2026-11-24/
  > Stock Traders Purchase High Volume of Bending Spoons Call Options (NASDAQ:BSP) - Traders bought 19,658 Bending Spoons call options on Tuesday, 607% above the typical volume of 2,779 contracts. - Bending Spoons shares fell $4.76 to $42.51 in Tuesday trading.
- Tue 24 Nov | GuruFocus | Bending Spoons (BSP) Stock Is Down 12.2% Today Without Company N
  https://www.gurufocus.com/news/9217706/bending-spoons-bsp-stock-is-down-122-today-without-company-news
  (page: did not load (403))
- Mon 23 Nov | MarketBeat | Wells Fargo & Company Forecasts Strong Price Appreciation for Bending Spoons (NASDAQ:BSP) Stock
  https://www.marketbeat.com/instant-alerts/analyst-wells-fargo-company-forecasts-strong-price-appreciation-for-bending-spoons-nasdaq-bsp-stock-2026-11-23/
  > Wells Fargo & Company Forecasts Strong Price Appreciation for Bending Spoons (NASDAQ:BSP) Stock - Wells Fargo raised its price target on Bending Spoons from $48 to $52 and maintained an “overweight” rating, implying about 9.1% upside from the stock’s current price.
## NTNX -15.2%  Nutanix
- Thu 26 Nov | FourWeekMBA | Nutanix’s IPO Sold Shares at $16; $1,000 Is Now Worth $2,890
  https://fourweekmba.com/ai-nutanixs-ipo-sold-shares-at-16-1000-is-now-worth-2890/
  (page: did not load (403))
- Thu 26 Nov | Yahoo Finance | Nutanix, Inc. (NTNX) Stock Forecasts
  https://finance.yahoo.com/research/reports/ARGUS_6741_QuantitativeReport_1795564800000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 26 Nov | TipRanks | Nutanix Earnings Call Signals Strong Growth Despite Transition
  https://www.tipranks.com/news/company-announcements/nutanix-earnings-call-signals-strong-growth-despite-transition
  (page: did not load (403))
- Thu 26 Nov | MEXC | Why Is Nutanix (NTNX) Stock Down 15% Today? CEO Exit and Slower Bookings Overshadow Earnings
  https://www.mexc.com/crypto-pulse/article/why-is-nutanix-ntnx-stock-down-15-today-ceo-exit-and-slower-bookings-overshadow-earnings-194549
  (page: did not load (403))
## LRCX -5.7%  Lam Research
- Thu 26 Nov | Seeking Alpha | Lam Research: Equipment Demand Is Surging, But The Stock Is Down 52% (NASDAQ:LRCX)
  https://seekingalpha.com/article/4972157-lam-research-stock-equipment-demand-surging-but-stock-down-52-percent
  (page: did not load (403))
- Thu 26 Nov | Pluang | Lam Research upgraded to Buy as valuation impro...
  https://pluang.com/en/news-feed/lam-research-harga-tertekan-cerita-upgrade-beli
  (page: did not load (403))
- Thu 26 Nov | Seeking Alpha | Lam Research: The Price Has Caught Down The Story
  https://seekingalpha.com/article/4972115-lam-research-the-price-has-caught-down-the-story-upgrade-buy
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-26 CLHO results (expected)
- 2026-11-26 EAST results (expected)  <- write its preview
- 2026-11-26 EFIH results (expected)  <- write its preview
- 2026-11-26 JUFO results (expected)
- 2026-12-02 ALCN results (expected)
- 2026-12-02 AMOC results (expected)
- 2026-12-02 EGAL results (expected)
- 2026-12-02 EMFD results (expected)
- 2026-12-02 NVDA dividend
- 2026-12-02 SKPC results (expected)

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (on track)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
    2026-11-11-value-basket: open -> on track
    2026-10-30-rotation: open -> on track

## Fair value
- Changed since the last run: ABUK +37% -> +51% (medium -> medium); PHAR +31% -> +20% (low -> low); SCEM +21% -> +19% (medium -> high); CSAG +22% -> +10% (medium -> medium); CLHO -34% -> -48% (low -> low); LCSW -48% -> -68% (medium -> low). Dropped out: EFIH.
- In the ten cheapest or dearest with no note: AMOC, EMFD, MCQE, ADIB, PRDC, MHOT, MTIE, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-26. Open each story before using it.
## COMI  (8 leads)
- Thu 26 Nov | شبكة تواصل الإخبارية | «التجاري الدولي» يستحوذ على 39.1% من أرباح البنوك المدرجة بنهاية سبتمبر
  https://twaslnews1.twaslnews.com/8323230/
  (page: did not load (403))
- Wed 25 Nov | بوابة المصرف | قطاع البنوك بالبورصة يتراجع 0.1% في ختام تعاملات.. «التجاري الدولي» يرتفع و«فيصل» يتصدّر الصعود
  https://www.almasraf.news/قطاع-البنوك-بالبورصة-يتراجع-0-1-في-ختام-ت/
  > أنهت أسهم قطاع البنوك المدرجة بالبورصة المصرية تعاملات جلسة اليوم الأربعاء 25 نوفمبر 2026 على أداء متباين مائل للتراجع، وسط ضغوط بيعية طالت غالبية الأسهم المصرفية، في مقابل ارتفاعات محدودة لعدد من الأسهم.
- Wed 25 Nov | شبكة تواصل الإخبارية | البنك التجاري الدولي CIB يطرح حساب التوفير اليومي Premium بالدولار
  https://twaslnews1.twaslnews.com/8285064/
  (page: did not load (403))
## TMGH  (3 leads)
- Thu 26 Nov | ad-hoc-news.de | Talaat Moustafa Group stock: 9M revenue rises 24% to EGP 47.6bn
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/talaat-moustafa-group-stock-9m-revenue-rises-24-to-egp-47-6bn/70555421
  > Talaat Moustafa Group reported stronger results for the first nine months of 2026 in an earnings release dated November 12. TMG Holding's earnings release showed higher revenue and net profit, supported by real estate deliveries, hospitality and recurring-income activities. Consolidated revenue rose 24.1% year over year to EGP 47.5532 billion in the nine-month period. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Tue 24 Nov | جريدة البورصة | سهم طلعت مصطفى يرتفع 2.28% خلال تعاملات البورصة اليوم
  https://alborsaanews.com/2026/11/24/2008848
  > سجل سهم مجموعة طلعت مصطفى القابضة أداءً إيجابيًا خلال تعاملات البورصة المصرية اليوم الثلاثاء، بعدما ارتفع بنسبة 2.28% ليصل إلى مستوى 80.80 جنيه، مواصلًا التحرك في المنطقة الخضراء بالتزامن مع عودة الصعود إلى مؤشرات السوق الرئيسية.
- Tue 24 Nov | جريدة المال | سهم طلعت مصطفى يقفز بنسبة 2.28% خلال تعاملات البورصة اليوم
  https://almalnews.com/2149469/سهم-طلعت-مصطفى-يقفز-بنسبة-2-28/
  (same wording as the جريدة البورصة story above: one source, not two)
## ETEL  (8 leads)
- Thu 26 Nov | جريدة المال | المصرية للاتصالات تتوقع تسجيل مركز نقدي صافٍ خلال 3 - 5 سنوات
  https://almalnews.com/2149753/المصرية-للاتصالات-تتوقع-تسجيل-مركز-نقدي-صافٍ/
  (page: only 65 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Wed 25 Nov | شبكة تواصل الإخبارية | قفزة قياسية.. أرباح المصرية للاتصالات WE تصعد لـ 24.4 مليار جنيه
  https://twaslnews1.twaslnews.com/8307208/
  (page: did not load (403))
- Wed 25 Nov | بوابة الغد | «أهل مصر» تعلن استعداد فرقها الطبية لبدء التشخيص عن بُعد لمرضى الحروق بالتعاون مع «الصحة» و«المصرية للاتصالات»
  https://elghad.news/313142/
  > أعلنت الدكتورة هبة السويدي المدير التنفيذي ورئيس مجلس أمناء مؤسسة ومستشفى أهل مصر لعلاج الحروق، الانتهاء من تدريب وتأهيل الفرق الطبية والتمريضية وفق أعلى معايير الرعاية، والاستعداد الكامل لاستقبال أول حالة ضمن منظومة التشخيص عن بُعد الجديدة، تمهيداً لتعميم التجربة وتحسين جودة الرعاية المقدمة لمرضى الحروق.
## PHDC  (3 leads)
- Wed 25 Nov | Billionaires.Africa | Egyptian billionaire Yasseen Mansour's Palm Hills posts $63 million nine-month profit
  https://www.billionaires.africa/2026/11/25/egyptian-billionaire-yasseen-mansours-palm-hills-posts-63-million-nine-month-profit/
  > Palm Hills Developments SAE, the Cairo-based property developer chaired by Egyptian billionaire Yasseen Mansour, posted a net profit of 3.374 billion Egyptian pounds ($62.8 million) for the first nine months of 2026, as higher sales lifted revenue but squeezed margins. [Figures on the page: nine months; first half; attributable to shareholders. Check which one each figure is.]
- Tue 24 Nov | نيوز رووم | بالم هيلز أمام فرصة صعود 83%.. «الأهلي فاروس» تحدد القيمة العادلة للسهم عند 21.40 جنيه
  https://newsroom.info/488456
  > بالم هيلز أمام فرصة صعود 83%.. «الأهلي فاروس» تحدد القيمة العادلة للسهم عند 21.40 جنيه
- Tue 24 Nov | اليوم السابع | الكبار يبيعون أسهم CIB وبالم هيلز ومستشفى النزهة وشراء في "جهينة"
  https://www.youm7.com/story/2026/11/24/الكبار-يبيعون-أسهم-CIB-وبالم-هيلز-ومستشفى-النزهة-وشراء-في/7630345
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية، خلال جلسة تداول أمس الإثنين، تنفيذ عمليات شراء وبيع على أسهم 28 شركة، تنوعت بين تحركات للداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم، وفقًا لبيانات التداول المعلنة.
## SWDY  (4 leads)
- Wed 25 Nov | FLAIR MAGAZINE | Alstom’s Chief Procurement Officer Meets Elsewedy Electric’s President to Explore Ways to Strengthen Industrial Cooperation and Expand Across Regional Markets
  https://flair-magazine.com/2026/11/25/alstoms-chief-procurement-officer-meets-elsewedy-electrics-president-to-explore-ways-to-strengthen-industrial-cooperation-and-expand-across-regional-markets/
  > Alstom’s Chief Procurement Officer, Nathalie Saint Martin, met today with Ahmed Elsewedy, President and CEO of Elsewedy Electric, to review the collaboration between the two companies and discuss its future potential.
- Wed 25 Nov | بوابة الغد | فرصة عمل وتأهيل كابلات السكك الحديدية.. أبرز ملفات لقاء قيادتي «ألستوم» و«السويدي إليكتريك»
  https://elghad.news/313133/
  > بحثت ناتالي سان مارتن رئيس قطاع المشتريات العالمية بشركة «ألستوم» الفرنسية، مع المهندس أحمد السويدي، الرئيس التنفيذي والعضو المنتدب لشركة «السويدي إليكتريك»، سبل تعميق التعاون الصناعي القائم بين الجانبين، واستعراض آفاق توسيع الشراكة في مصر والأسواق الإقليمية خلال المرحلة المقبلة.
- Wed 25 Nov | Billionaires.Africa | Egyptian tycoon Ahmed El Sewedy's Elsewedy to build 90MW Angola solar plant
  https://www.billionaires.africa/2026/11/25/egyptian-tycoon-ahmed-el-sewedys-elsewedy-to-build-90mw-angola-solar-plant/
  > Elsewedy Electric SAE, the Egyptian cable and power group run by tycoon Ahmed El Sewedy, is building a 90-megawatt solar plant with 25 megawatts of battery storage in Angola's oil-producing Cabinda province, a project due to be finished in June 2029.
- Wed 25 Nov | جريدة المال | ألستوم والسويدي إليكتريك تبحثان توسيع شراكتهما الصناعية
  https://almalnews.com/2149637/ألستوم-والسويدي-إليكتريك-تبحثان-توسيع-شراكتهما-الصناعية/
  > بحثت ناتالي سان مارتن، رئيس قطاع المشتريات العالمية بشركة ألستوم، مع المهندس أحمد السويدي، الرئيس التنفيذي والعضو المنتدب لشركة السويدي إليكتريك، سبل تعزيز التعاون القائم بين الشركتين، واستكشاف آفاق توسيعه خلال المرحلة المقبلة، في إطار شراكة تستهدف دعم التصنيع المحلي وتطوير سلاسل التوريد وتوسيع نطاق المشاركة في المشروعات الصناعية ومشروعات البنية التحتية بالمنطقة.
## ORAS  (8 leads)
- Thu 26 Nov | The Globe and Mail | OCI Completes Sale to Orascom Construction
  https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/9014280/oci-completes-sale-to-orascom-construction/
  > ( (NL:OCI) ) has issued an announcement. OCI Global completed the sale and transfer of its shares in OCI Rembrandt Holdings B.V. to Orascom Construction, receiving 97,201,359 newly issued Orascom Construction shares.
- Thu 26 Nov | EnterpriseAM | أوراسكوم كونستراكشون تتم اندماجها مع "أو سي آي" مقابل 47% من أسهمها
  https://enterpriseam.com/egypt-ar/issues/أوراسكوم-كونستراكشون-تتم-اندماجها-مع/
  (page read: it never names the company, so probably not about it: skip)
- Wed 25 Nov | بوابة بلوم | باستثمارات 6.7 مليار دولار.. أوراسكوم كونستراكشون تضع حجر أساس مشروع تحلية مياه في الأردن
  https://bloom-gate.com/أسواق/باستثمارات-6-7-مليار-دولار-أوراسكوم-كون-2/
  > باستثمارات 6.7 مليار دولار.. أوراسكوم كونستراكشون تضع حجر أساس مشروع تحلية مياه في الأردن أعلنت شركة «أوراسكوم كونستراكشون» وضع حجر الأساس لمشروع تحلية ونقل المياه من مدينة العقبة إلى العاصمة الأردنية عمان، بمشاركة الشركة ضمن تحالفين يتوليان تنفيذ أعمال التصميم والتوريد والإنشاء، في إطار اتفاقية تمتد لمدة 30 عامًا، وباستثمارات تتجاوز 6.7 مليار دولار.
- Wed 25 Nov | Masrawy | أوراسكوم كونستراكشون تعلن إتمام الاستحواذ على شركة تابعة لـ"أو سي آي"
  https://www.masrawy.com/news/news_economy/details/2026/11/25/3084271/أوراسكوم-كونستراكشون-تعلن-إتمام-الاستحواذ-على-شركة-تابعة-لـ-أو-سي-آي-?amp
  > أوراسكوم كونستراكشون تعلن إتمام الاستحواذ على شركة تابعة لـ"أو سي آي" أعلنت شركة أوراسكوم كونستراكشون المدرجة في سوق أبوظبي للأوراق المالية والبورصة المصرية إتمام عملية الاستحواذ على شركة OCI Rembrandt Holdings B.V من شركة"OCI N.V"، وذلك في إطار تنفيذ عملية الاندماج التي سبق الإعلان عنها بين الشركتين، وفقًا لبيان مرسل للبورصة المصرية.
- Wed 25 Nov | جريدة الاستثمار العربى | «أوراسكوم كونستراكشون» تتم الاندماج مع «OCI» وتصدر 97.2 مليون سهم جديد
  https://estsmararabe.com/أوراسكوم-كونستراكشون-تتم-الاندماج/
- Wed 25 Nov | www.marketscreener.com | Orascom Construction PLC completed the acquisition of OCI N.V..
  https://www.marketscreener.com/news/orascom-construction-plc-completed-the-acquisition-of-oci-n-v--ce7851dbd08af223
- Wed 25 Nov | جريدة البورصة | "أوراسكوم كونستراكشون" تنتهي من الإندماج مع "OCI N.V"
  https://alborsaanews.com/2026/11/25/2008956
- Wed 25 Nov | جريدة حابي | أوراسكوم كونستراكشون تعلن إتمام عملية الاندماج مع شركة OCI N.V
  https://hapijournal.com/2026/11/25/أوراسكوم-كونستراكشون-تعلن-إتمام-عملي/
## FWRY  (2 leads)
- Wed 25 Nov | بوابة التكنولوجيا المالية | «اكويتي» و«بوتيم» تتيحان تمويل حسابات التداول والاستثمار عبر خدمة الدفع الفوري «آني» في الإمارات
  https://www.fintechgate.net/258546
  > «اكويتي» و«بوتيم» تتيحان تمويل حسابات التداول والاستثمار عبر خدمة الدفع الفوري «آني» في الإمارات
- Tue 24 Nov | المشهد السوداني | تحويلات في ثوانٍ دون إنترنت.. كل ما تريد معرفته عن نظام الدفع الفوري بالسودان
  https://almashhadalsudani.com/economic-news/sudan-banks-news/180876/
  (page: did not load (403))
## ABUK  (3 leads)
- Tue 24 Nov | جريدة المستقبل | زد يرفع رصيده إلى 12 نقطة بعد التعادل مع أبوقير للأسمدة
  https://www.elmostaqbal.com/879294/زد-يرفع-رصيده-إلى-12-نقطة-بعد-التعادل-مع-أ/
  > انتهت مواجهة زد إف سي وأبوقير للأسمدة بنتيجة التعادل السلبي دون أهداف، في اللقاء الذي جمع الفريقين مساء اليوم الثلاثاء ضمن منافسات الجولة التاسعة من الدوري المصري الممتاز، دوري أورا 2026-2027 لكرة القدم ليكتفي كل طرف بالحصول على نقطة واحدة دون أن ينجح أي منهما في هز الشباك.
- Tue 24 Nov | مصر تايمز | جهاز المنتخب الوطني يتابع مباراتي زد وأبوقير للأسمدة وسموحة والبنك الأهلي
  https://www.masrtimes.com/781372
  > جهاز المنتخب الوطني يتابع مباراتي زد وأبوقير للأسمدة وسموحة والبنك الأهلي حرص الجهاز الفني للمنتخب الوطني الأول لكرة القدم، بقيادة علي ماهر، على متابعة عدد من مباريات اليوم، للوقوف على مستوى اللاعبين ومتابعة العناصر المرشحة للانضمام إلى صفوف المنتخب خلال الفترة المقبلة.
- Tue 24 Nov | الاتحاد المصري لكرة القدم | علي ماهر يتابع مواجهة زد وأبوقير للأسمدة بمقصورة إستاد القاهرة
  https://efa.com.eg/ar/الأخبار/علي-ماهر-يتابع-مواجهة-زد-وأبوقير-للأسمدة-بمقصورة-إستاد-القاهرة/
  (page: did not load (403))
## HRHO  (6 leads)
- Wed 25 Nov | Briefs Finance | EFG Hermes Launches GCC Debt Advisory as IPO Pipeline Thins
  https://www.briefs.co/news/efg-hermes-launches-gcc-debt-advisory-as-ipo-pipeline-thins/
  > - EFG Hermes has set up a debt advisory team across the Gulf Cooperation Council, extending its debt effort beyond Egypt. - The shift comes as Middle East IPO activity slowed before the conflict and then suffered further from the Iran war. Why EFG is moving into debt
- Wed 25 Nov | Bloomberg | Mideast IPO Slump Prompts EFG to Branch Out Into Debt Advisory
  https://www.bloomberg.com/news/articles/2026-11-25/mideast-ipo-slump-prompts-efg-to-branch-out-into-debt-advisory
  (page: did not load (403))
- Tue 24 Nov | جريدة المال | إي اف چي هيرميس لترويج وتغطية الاكتتاب
  https://almalnews.com/tag/إي-اف-چي-هيرميس-لترويج-وتغطية-الاكتتاب/1/
  (page: only 31 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## JUFO  (4 leads)
- Wed 25 Nov | almotawwer.com | Juhayna and Raie Misr Launch “100 Days of Health with Juhayna” Initiative to Serve Over 30,000 Patients in Upper Egypt
  https://almotawwer.com/english/335449/
  > Juhayna and Raie Misr Launch “100 Days of Health with Juhayna” Initiative to Serve Over 30,000 Patients in Upper Egypt
- Wed 25 Nov | مجلة البوصلة الاقتصادية | زيادة أسعار ألبان جهينة تصل إلى 17%.. اعتبارًا من 28 نوفمبر الجاري
  https://alboslanews.com/زراعة/زيادة-أسعار-ألبان-جهينة-تصل-إلى-17-اعتبارًا-من-28-نوفمبر-الجاري-431467
  > زيادة أسعار ألبان جهينة تصل إلى 17%.. اعتبارًا من 28 نوفمبر الجاري الأربعاء 25 نوفمبر 2026 -11:15 أعلن حازم المنوفي، عضو شعبة المواد الغذائية، عن زيادة جديدة في أسعار عدد من منتجات ألبان جهينة، اعتبارًا من يوم السبت 28 نوفمبر 2026، تشمل عدة أصناف وأحجام مختلفة، من بينها الألبان كاملة الدسم وخالية اللاكتوز ومنتجات الهوريكا.
- Wed 25 Nov | بوابة الوفد الإلكترونية | رفع تراكمات القمامة من كوم الجرون ونجع الضبع بمدينة جهينة
  https://www.alwafd.news/6009525
  (page: did not load (403))
## EFIH  (3 leads)
- Wed 25 Nov | بوابة التكنولوجيا المالية | الحكومة المصرية تستهدف توظيف قدرات «إي فاينانس» و«إي تاكس» للتوسع في تطبيقات الذكاء الاصطناعي وتطوير الخدمات الحكومية
  https://fintechgate.net/258472
  > «كجوك»: الذكاء الاصطناعي محور رئيسي في خطة التحول الرقمي وتسجيل نحو 4 ملايين عقار إلكترونيًا الحكومة المصرية تستهدف توظيف قدرات «إي فاينانس» و«إي تاكس» للتوسع في تطبيقات الذكاء الاصطناعي وتطوير الخدمات الحكومية
- Tue 24 Nov | جريدة المطور | البنك الأهلي المصري و«إي نوفيت» التابعة لـ«إي فاينانس» يوقعان بروتوكول تعاون لتعزيز تأمين معاملات الشراء عبر الإنترنت
  https://almotawwer.com/top-article/335346/
  > البنك الأهلي المصري و«إي نوفيت» التابعة لـ«إي فاينانس» يوقعان بروتوكول تعاون لتعزيز تأمين معاملات الشراء عبر الإنترنت محمد الأتربي: حماية بيانات العملاء وتأمين معاملاتهم المالية على رأس أولويات البنك الأهلي المصري
- Tue 24 Nov | Masrawy | بروتوكول بين البنك الأهلي وشركة تابعة لـ"إي فاينانس" لتعزيز تأمين معاملات الشراء عبر الإنترنت
  https://www.masrawy.com/news/news-banking/details/2026/11/24/3083849/بروتوكول-بين-البنك-الأهلي-وشركة-تابعة-لـ-إي-فاينانس-لتعزيز-تأمين-معاملات-الشراء-عبر-الإنترنت
  > أعلن البنك الأهلي المصري توقيع بروتوكول تعاون مع شركة إي نوفيت، التابعة لمجموعة إي فاينانس للاستثمارات المالية والرقمية، بهدف تعزيز منظومة تأمين معاملات الشراء عبر الإنترنت باستخدام البطاقات الصادرة من البنك الأهلي المصري، من خلال إتاحة خدمة الرقم السري المتغير (One Time Password – OTP) 3D-Secure، وذلك في إطار استراتيجية البنك المستمرة لتطوير خدماته المصرفية ...
## BQDC  (8 leads)
- Wed 25 Nov | شبكة تواصل الإخبارية | بنك القاهرة يتيح تقسيط مشتريات 2B على 18 شهرًا بدون فوائد أو مصاريف إدارية أو مقدم
  https://twaslnews1.twaslnews.com/8297795/
  (page: did not load (403))
- Wed 25 Nov | الأسبوع | بنك القاهرة يطرح شهادة «بريمو» بعائد ثابت يصل إلى 19.75% لمدة 3 سنوات
  https://www.elaosboa.com/3033919/
  > بنك القاهرة يطرح شهادة «بريمو» بعائد ثابت يصل إلى 19.75% لمدة 3 سنوات يقدم بنك القاهرة شهادة الادخار «بريمو» ذات العائد الثابت لمدة 3 سنوات بالجنيه المصري، بعوائد سنوية تصل إلى 19.75% مع إتاحة 4 دوريات مختلفة لصرف العائد، بما يوفر للعملاء خيارات ادخارية متنوعة تتناسب مع احتياجاتهم المالية.
- Wed 25 Nov | تليجراف مصر | شهادات بريمو من بنك القاهرة.. كيف تحصل على عائد يتجاوز 118 ألف جنيه؟
  https://www.egypttelegraph.com/article/299143/شهادات-بريمو-من-بنك-القاهرة-كيف-تحصل
  > أعلن بنك القاهرة طرح شهادات الادخار "بريمو" ذات العائد الثابت لمدة 3 سنوات بالجنيه المصري، بمعدلات عائد تصل إلى 19.75% سنويًا، مع إتاحة 4 دوريات لصرف العائد، تشمل الصرف اليومي والشهري والربع سنوي والسنوي.
## EGAL  (7 leads)
- Wed 25 Nov | شبكة تواصل الإخبارية | مصر للألومنيوم وفتنس برايم في المقدمة.. إنذارات وتنبيهات من البورصة لـ11 شركة
  https://twaslnews1.twaslnews.com/8293095/
  (page: did not load (403))
- Wed 25 Nov | إقرأ نيوز | بينها مصر للألومنيوم.. لجنة القيد بالبورصة توجه إنذارات وتنبيهات لـ11 شركة لمخالفة قواعد القيد
  https://www.iqraa.news/266594/بينها-مصر-للألومنيوم-لجنة-القيد-بالبو/
  > لجنة القيد بالبورصة توجه إنذارات وتنبيهات لـ11 شركة لمخالفة قواعد القيد. قررت لجنة القيد بالبورصة المصرية، خلال جلستها المنعقدة بتاريخ 24 نوفمبر 2026، توجيه إنذارات وتنبيهات إلى 11 شركة مقيدة، لمراعاة أحكام قواعد قيد وشطب الأوراق المالية والإجراءات التنفيذية، وذلك وفقًا للضوابط المنظمة لعمل الشركات المقيدة. إنذار وتنبيه 11 شركة بالبورصة المصرية
- Wed 25 Nov | اليوم السابع | إنذار لـ"مصر للألومنيوم" و"فتنس برايم".. تحركات لجنة القيد في البورصة
  https://www.youm7.com/story/2026/11/25/إنذار-لـ-مصر-للألومنيوم-و-فتنس-برايم-تحركات-لجنة-القيد/7632303
  > قررت لجنة القيد بالبورصة المصرية، خلال جلستها المنعقدة أمس الثلاثاء، توجيه تنبيهات وإنذارات لعدد من الشركات المقيدة بالبورصة، بشأن ضرورة مراعاة أحكام قواعد قيد وشطب الأوراق المالية والإجراءات التنفيذية، وذلك في إطار متابعة التزام الشركات بالقواعد المنظمة للقيد والإفصاح.
## SKPC  (1 leads)
- Tue 24 Nov | جريدة المال | سيدي كرير للبتروكيماويات تتصدر ارتفاعات أسهم قطاع الموارد الأساسية بالبورصة المصرية خلال تعاملات الثلاثاء
  https://almalnews.com/2149405/سيدي-كرير-للبتروكيماويات-تتصدر-ارتفاعات-أسهم-قطاع/
  > تصدرت شركة سيدي كرير للبتروكيماويات «سيدبك» ارتفاعات أسهم قطاع الموارد الأساسية بالبورصة المصرية خلال تعاملات جلسة الثلاثاء، بعدما صعد سهمها بنسبة 5.36% ليغلق عند 14.94 جنيه، بقيمة تداول بلغت 89.16 مليون جنيه، من خلال تنفيذ 1590 عملية.
## EFID  (7 leads)
- Thu 26 Nov | Pioneers Misr | إيديتا تضخ 25 مليون دولار في توسعاتها بالعراق خلال عامين.. وتستهدف مضاعفة الطاقة الإنتاجية
  https://pioneersmisr.com/124478/
  > تعتزم شركة إيديتا للصناعات الغذائية ضخ استثمارات جديدة بقيمة 25 مليون دولار في السوق العراقية على مدار العامين المقبلين، في إطار خطتها لتعزيز تواجدها الإقليمي والتوسع في الأسواق الخارجية، مستهدفة مضاعفة طاقتها الإنتاجية بالعراق من خلال استكمال تشغيل خطوط إنتاج جديدة وتدشين مصنع جديد. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Thu 26 Nov | https://www.youlyou.com/ | إيديتا تدعو لجمعية غير عادية لمناقشة تخفيض رأس المال وإعدام أسهم خزينة
  https://www.youlyou.com/103278
  > دعت شركة إيديتا للصناعات الغذائية مساهميها لحضور اجتماع الجمعية العامة غير العادية المقرر عقده يوم 27 ديسمبر 2026، لمناقشة تخفيض رأس المال المصدر والمدفوع للشركة بنحو 2.2 مليون جنيه، عبر إعدام أسهم الخزينة التي تمتلكها.
- Thu 26 Nov | Milling Middle East & Africa | Edita Food Industries achieves record quarterly revenue in Q3 2026 as net profit rises 41.5%
  https://millingmea.com/edita-food-industries-achieves-record-quarterly-revenue-in-q3-2026-as-net-profit-rises-41-5/
  > The company’s consolidated revenues surged by 32.9% year-on-year to reach EGP 7.3 billion (US$133.31M), driven by robust consumer demand, strategic portfolio optimization, and enhanced pricing strategies across its core product segments. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## AAPL  (8 leads)
- Thu 26 Nov | Mitrade | Apple Stock Defies AI Selloff: Is It the Market's Safe Haven?
  https://www.mitrade.com/au/insights/stock-analysis/us-stocks/beincrypto-AAPL-202611261037
  > Apple Stock Defies AI Selloff: Is It the Market's Safe Haven? Apple (AAPL) stock has gained 30.61% in 2026 while Nvidia (NVDA) has lost 21.35%, according to TradingView data. Apple’s climb has not been without its volatility. Shares slid 7.5% between Oct. 3, which suggests holders swapped AI spending risk for valuation risk.
- Thu 26 Nov | Yahoo Finance | Michael Burry Says He’s Shorting The Market’s ‘Generals’ As Apple Flashes A Warning Last Seen In 2002
  https://finance.yahoo.com/markets/stocks/articles/michael-burry-says-shorting-market-034440109.html
  > - He named Apple as a possible target and separately disclosed a bet against private equity. - Burry bought Nvidia calls before Monday's rally, exited his semiconductor ETF puts and later sold his remaining Nasdaq 100 puts. - He also attributed Wednesday's Nasdaq 100 bounce to buyers returning near 25,000.
- Wed 25 Nov | Yahoo Finance | Tech Stock Sell-Off: Here's Why Apple Has Been Immune
  https://finance.yahoo.com/markets/stocks/articles/tech-stock-sell-off-heres-202002463.html
  > Artificial intelligence (AI) stocks have taken a beating in November. The tech-heavy Nasdaq-100 index is down 15% this month on fears that AI spending has gotten out of hand. Smartphone maker Apple (NASDAQ:AAPL) is bucking the trend.
## MSFT  (8 leads)
- Thu 26 Nov | Simply Wall St | Microsoft (MSFT) Stock Could Be 36% Below Fair Value After Global Outage
  https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-stock-could-be-36-below-fair-value-after-glob
  > Microsoft stock has slipped from recent highs yet still trades at a level that assumes a powerful cash engine, which raises a simple question for you as an investor.
- Thu 26 Nov | BigGo Finance | Nvidia Slips Below Microsoft as Valuation Retreats From $5.77 Trillion Peak
  https://finance.biggo.com/news/471f64ed-2335-4e57-a95e-9445bf9beb91
  (page: did not load (URLError))
- Thu 26 Nov | Yahoo Finance | Nvidia’s Market Cap Falls Below Microsoft’s: Analyst Flags Five Overhangs For NVDA Stock
  https://finance.yahoo.com/markets/stocks/articles/nvidia-market-cap-falls-below-023942800.html
  > - At the market close, Nvidia's market cap slid to $3.61 trillion, below Microsoft's $3.64 trillion. - Nvidia's fundamental picture hasn't changed, investor Gary Black said.
## NVDA  (8 leads)
- Thu 26 Nov | Benzinga | Top Analyst Flags 5 Major Risks for NVDA Stock, Says Nvidia Could Stay in ‘Penalty Box’ for 1-2 Quarters
  https://www.benzinga.com/markets/equities/26/11/63660421/top-analyst-flags-5-major-risks-for-nvda-stock-says-nvidia-penalty-box
  (page: did not load (403))
- Thu 26 Nov | The Motley Fool | Prediction: This Is What Nvidia Stock Will Be Worth by 2028
  https://www.fool.com/investing/2026/11/26/prediction-this-is-what-nvidia-stock-will-be-worth-by-2028/
  > Nvidia (NVDA -3.91%) stock has gotten slammed over the past few weeks. It all started with co-founder and former CEO Jensen Huang resigning from his position. While he's back in the CEO role, news of investigations into Nvidia's export controls are also weighing down the stock.
- Thu 26 Nov | Yahoo Finance | MU, SNDK, SKHY Jump As Nvidia Tests Kioxia Memory Fix — Analyst Presses Memory Giants For ‘Massive’ Buybacks
  https://finance.yahoo.com/markets/stocks/articles/mu-sndk-skhy-jump-nvidia-063051265.html
  > - The Nvidia Way author Tae Kim urged memory chipmakers to back their long-term forecasts with "massive stock buybacks." - Micron can begin using its $35.16 billion buyback authorization on Dec. 9 under its U.S. - SanDisk spent $5 billion on buybacks in its latest quarter.
- Thu 26 Nov | Yahoo Finance | Kioxia jumps 14% after Nvidia collaboration as chip stocks rebound
  https://finance.yahoo.com/markets/stocks/articles/kioxia-jumps-14-nvidia-collaboration-062844097.html
  > Investing.com -- Kioxia Holdings shares surged on Thursday, extending a sharp rebound in Japanese semiconductor stocks after the memory chipmaker announced a collaboration with Nvidia to expand effective GPU memory capacity using its solid-state drives. Kioxia rose as much as 14.5% to 7,895 yen, outperforming the Nikkei 225, which gained 1.3% to close at 57,745.27.
- Thu 26 Nov | qz.com | Nvidia stock ends Nov. 23 about 31% below its record close
  https://qz.com/nvidia-stock-31-percent-below-record-close-112426
- Thu 26 Nov | Facebook | “This is INSANE,” said an account on X, which, according to its bio, is run by a stock and options trader. The post claimed that someone had bought $3.4 million worth of Nvidia options on Friday, which re
  https://www.facebook.com/nytimes/posts/this-is-insane-said-an-account-on-x-which-according-to-its-bio-is-run-by-a-stock/1561930049122786/
- Thu 26 Nov | investingLive | My Nvidia stock analysis shows bulls are better than what most seem to think
  https://investinglive.com/stocks/my-nvidia-stock-analysis-shows-bulls-are-better-than-what-most-seem-to-think/
- Thu 26 Nov | The Globe and Mail | Is Nvidia Stock a Buy After Dell's Record AI Backlog?
  https://www.theglobeandmail.com/investing/markets/stocks/DELL/pressreleases/9013547/is-nvidia-stock-a-buy-after-dells-record-ai-backlog/
## AMZN  (8 leads)
- Thu 26 Nov | Trefis | Does Black Friday Ever Move Amazon Stock?
  https://www.trefis.com/stock/amzn/articles/629188/does-black-friday-ever-move-amazon-stock/2026-11-26
  > Does Black Friday Ever Move Amazon Stock? Black Friday is tomorrow. The short answer is that Amazon stock has rarely cared. We did it for every year from 2000 to 2025. The stock rose in 14 of those 26 years and fell in 12. Its median move was 0.03%, close to nothing. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Thu 26 Nov | Benzinga | TruGolf Holdings Shares Surge 18.94% After Hours - Amazon.com (NASDAQ:AMZN), IBM (NYSE:IBM)
  https://www.benzinga.com/markets/equities/26/11/63660267/trugolf-holdings-shares-after-hours-leadership-shakeup
  (page: did not load (403))
- Thu 26 Nov | Gotrade | Meta Stock Rises 3.4% on Reports of Amazon Muse Talks (Nov 25)
  https://www.heygotrade.com/en/news/meta-meta-stock-news-november-26-2026/
  > AI-powered contentSome parts of this article are powered by AI. - Meta Platforms (META) closed at $609.89 on November 25, 2026, a change of +$20.07 (+3.40%), while QQQ (Nasdaq-100 ETF) fell 0.65%.
- Thu 26 Nov | CNBC | K-beauty stocks rally as Korean brands top Amazon bestseller lists globally ahead of Black Friday
  https://www.cnbc.com/2026/11/26/k-beauty-firms-amazon-sales-black-friday.html
  > South Korean beauty stocks jumped Thursday as the country's skincare brands dominated Amazon's bestseller rankings ahead of Black Friday. Shares of K-beauty giant APR climbed 3.77%, while cosmetic contracts manufacturers Kolmar Korea and Cosmax gained 5.46% and 2.91%, respectively.
- Thu 26 Nov | TIKR.com | Bill Gurley: Investors Weren’t “Scrambling to Actually Own Anthropic.” That’s a Problem for Amazon and Alphabet
  https://www.tikr.com/blog/bill-gurley-investors-werent-scrambling-to-actually-own-anthropic-thats-a-problem-for-amazon-and-alphabet
- Wed 25 Nov | Traders Union | AI infrastructure outlay concerns put Amazon under pressure amid negative technology sector flow
  https://tradersunion.com/news/stocks/show/4422025-amazon-falls-on-ai-spending/
- Wed 25 Nov | MarketBeat | Amazon.com (NASDAQ:AMZN) Shares Down 3.1% on Insider Selling
  https://www.marketbeat.com/instant-alerts/price-amazoncom-nasdaq-amzn-shares-down-31-on-insider-selling-2026-11-25/
- Wed 25 Nov | Seeking Alpha | Amazon: Lower Downside Risk, But Not Immune To AI-Trade Related Risks (NASDAQ:AMZN)
  https://seekingalpha.com/article/4972044-amazon-lower-downside-risk-but-not-immune-to-ai-trade-related-risks
## GOOGL  (8 leads)
- Thu 26 Nov | JournalArta | Alphabet stock drops to $273.10 as AI rout widens gap with S&P 500
  https://journalarta.com/en/2026/11/26/alphabet-stock-drops-to-273-10-as-ai-rout-widens-gap-with-sp-500/
  > Alphabet stock drops to $273.10 as AI rout widens gap with S&P 500 Alphabet shares fell 2.13% to $273.10 on Wednesday, extending a two-day slide and leaving the stock 32.17% below its May peak. Alphabet shares fell more than 2% on Wednesday as a selloff in artificial intelligence stocks entered a second day.
- Thu 26 Nov | Pluang | Anthropic's $81B IPO boosts Alphabet's stake to $149B, strengthening AI and cloud ties.
  https://pluang.com/en/news-feed/ipo-anthropic-menguntungkan-investor-alphabet
  (page: did not load (403))
- Thu 26 Nov | Yahoo Finance | 2 Ways Anthropic's IPO Pays Off for Alphabet Investors
  https://finance.yahoo.com/technology/ai/articles/2-ways-anthropics-ipo-pays-052002893.html
  > Anthropic (NASDAQ:ANT) recently completed the largest initial public offering (IPO) in history, raising $81.3 billion -- beating the previous record set by SpaceX by $6.3 billion in June. Many investors were no doubt pleased with Anthropic's public debut, but individual retail investors aren't the only ones to benefit.
- Thu 26 Nov | The Economic Times | Why is Alphabet stock sliding? Key factors behind the sell-off
  https://m.economictimes.com/markets/us-stocks/news/why-is-alphabet-stock-sliding-key-factors-behind-the-sell-off/alphabet-shares-tumble/slideshow/136178516.cms
  > Why is Alphabet stock sliding? Key factors behind the sell-off Alphabet shares come under heavy selling pressure on Wednesday, November 25, falling more than 5% during the session as investors reassess the technology giant's growth outlook.
- Thu 26 Nov | The Globe and Mail | Is Google Services Still the Prime Earnings Engine for Alphabet Stock?
  https://www.theglobeandmail.com/investing/markets/stocks/AMZN-Q/pressreleases/9004978/is-google-services-still-the-prime-earnings-engine-for-alphabet-stock/
- Thu 26 Nov | ad-hoc-news.de | Alphabet's Borrowing Costs Draw Scrutiny as Malaysian Suit and EU AdSense Appeal Add to the Load
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/alphabet-s-borrowing-costs-draw-scrutiny-as-malaysian-suit-and-eu-adsense-appeal-add-to-the-load/70555486
- Thu 26 Nov | The National Law Review | Kaplan Fox Encourages Investors of Alphabet Inc. (NASDAQ: GOOGL
  https://natlawreview.com/press-releases/kaplan-fox-encourages-investors-alphabet-inc-nasdaq-googl-goog-contact-1
- Wed 25 Nov | MarketWatch | Alphabet Inc. Cl C stock underperforms Wednesday when compared to competitors
  https://www.marketwatch.com/data-news/alphabet-inc-cl-c-stock-underperforms-wednesday-when-compared-to-competitors-5d6b057a-e82f2c8af3e3?mod=goog_fin_scmw
## META  (8 leads)
- Thu 26 Nov | MarketBeat | Meta Platforms, Inc. (NASDAQ:META) Stock Has Average Target Price of $826.41
  https://www.marketbeat.com/instant-alerts/consensus-meta-platforms-inc-nasdaq-meta-stock-has-average-target-price-of-82641-2026-11-26/
  > (NASDAQ:META) Stock Has Average Target Price of $826.41 - Analyst sentiment is broadly positive: Meta has a “Moderate Buy” consensus among 56 analysts, with an average 12-month price target of $826.41. Recent target changes were mixed, including JPMorgan cutting its target to $775 and President Capital raising its target to $897.
- Thu 26 Nov | Simply Wall St | How Investors May Respond To Meta Stock Muse UK Launch
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/how-investors-may-respond-to-meta-stock-muse-uk-launch
  > - JD Sports Fashion plc recently announced a partnership with Meta Platforms to plug its UK customers into Muse, Meta’s AI personal agent, enabling product discovery, comparison and purchases inside the assistant alongside other shopping and travel connectors.
- Thu 26 Nov | Yahoo! Finance Canada | META Nov 2026 490.000 put (META261125P00490000) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/META261125P00490000/
  (page: did not load (404))
- Thu 26 Nov | Gotrade | Meta Stock Rises 3.4% on Reports of Amazon Muse Talks (Nov 25)
  https://www.heygotrade.com/en/news/meta-meta-stock-news-november-26-2026/
  > AI-powered contentSome parts of this article are powered by AI. - Meta Platforms (META) closed at $609.89 on November 25, 2026, a change of +$20.07 (+3.40%), while QQQ (Nasdaq-100 ETF) fell 0.65%.
- Thu 26 Nov | TradingView | Price to earnings forward of Meta Platforms Inc Units Thailand Depositery Receipts Repr 0.01 Sh – SET:META01
  https://www.tradingview.com/symbols/SET-META01/financials-statistics-and-ratios/price-earnings-fwd/
- Thu 26 Nov | BigGo Finance | Meta Shares Buck Trend to Close Up 3.4% on Report of Restarted Muse Shopping Talks With Amazon
  https://finance.biggo.com/news/77d3b159-67e6-4aa2-b0fa-f527177e250f
- Thu 26 Nov | Benzinga | PANW, META, AMZN, LI, SPCX: 5 Trending Stocks Today - SpaceX (NASDAQ:SPCX)
  https://www.benzinga.com/markets/equities/26/11/63659140/palo-alto-networks-meta-platforms-amazon-li-auto-and-spacex-why-these-5-stocks-are-on-investors-radar-today
- Thu 26 Nov | Investing.com UK | Form 4 Meta Platforms Inc: Javier Olivan (COO) For: 23 November
  https://uk.investing.com/news/stock-market-news/form-4-meta-platforms-inc-javier-olivan-coo-for-23-november-93CH-5005043
## TSLA  (8 leads)
- Thu 26 Nov | ad-hoc-news.de | Tesla stock gains 5.49% to EUR 350.00 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/tesla-stock-gains-5-49-to-eur-350-00-before-xetra/70556658
  > Tesla stock traded at EUR 350.00 on Lang & Schwarz at 08:29 CET on Thursday, November 26, 2026, 5.49 percent above the Xetra close of Wednesday, November 25, 2026. The move came as investors assessed a delayed European regulatory decision on Tesla's assisted-driving technology.
- Thu 26 Nov | JournalArta | Tesla Stock Price Today
  https://journalarta.com/en/2026/11/26/tesla-stock-falls-in-bear-market-territory-as-sp-500-slips/
  > Tesla stock falls in bear-market territory as S&P 500 slips Tesla shares closed at $380.14 on Wednesday, logging their steepest daily drop since Nov. 20 and remaining more than 22% below their one-year peak. Tesla shares fell on Wednesday, logging their steepest daily drop since Nov. 20 as the S&P 500 edged lower.
- Thu 26 Nov | Gotrade | Tesla Stock (TSLA) Falls 1.2% on EU Self-Driving Vote Delay (Nov 25)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-26-2026/
  > AI-powered contentSome parts of this article are powered by AI. - Tesla (TSLA) closed at $380.14 on November 25, 2026, down 1.18%, after trading as low as $357.64 in the session.
## JPM  (8 leads)
- Thu 26 Nov | TradingView | REG - JPMorgan Emerging MD - Dividend Declaration
  https://www.tradingview.com/news/reuters.com,2026-11-26:newsml_RSZ7107Ea:0-reg-jpmorgan-emerging-md-dividend-declaration/
  > REG - JPMorgan Emerging MD - Dividend Declaration LONDON STOCK EXCHANGE ANNOUNCEMENT JPMORGAN EMERGING MARKETS DIVIDEND INCOME PLC Legal Entity Identifier: 549300OPJXU72JMCYU09 As announced in the Company's financial results for the year ended 31st July 2026, the Board recognises the importance of regular and attractive dividends to shareholders.
- Thu 26 Nov | Investing.com | Vertex stock rating reiterated by JPMorgan after povetacicept PDUFA delay
  https://www.investing.com/news/analyst-ratings/vertex-stock-rating-reiterated-by-jpmorgan-after-povetacicept-pdufa-delay-93CH-5052108
  (page: did not load (403))
- Thu 26 Nov | Investing.com | Adecoagro stock rating upgraded by JPMorgan on Carapo mill acquisition
  https://www.investing.com/news/analyst-ratings/adecoagro-stock-rating-upgraded-by-jpmorgan-on-carapo-mill-acquisition-93CH-5052109
  (page: did not load (403))
## XOM  (8 leads)
- Thu 26 Nov | Ocean Energy Resources | ExxonMobil intends to drill further north in Stabroek Block
  https://ocean-energyresources.com/2026/11/26/exxonmobil-intends-to-drill-further-north-in-stabroek-block/
  > ExxonMobil is looking to start exploring the northern part of the block as early as 2027. This depends on the International Court of Justice (ICJ) ruling in Guyana’s favour in its territorial dispute with Venezuela.
- Thu 26 Nov | Splash247 | ExxonMobil eyes $2bn savings from repeat FPSO design in Guyana
  https://splash247.com/exxonmobil-eyes-2bn-savings-from-repeat-fpso-design-in-guyana/
  > US energy major ExxonMobil is looking to cut development costs by up to $2bn offshore Guyana by replicating the design of its recently sanctioned Longtail FPSO for another project. ExxonMobil Guyana president Alistair Routledge said the company was looking to leverage engineering, procurement, and fabrication work undertaken for Longtail in the proposed Haimara development.
- Thu 26 Nov | SOMO - The Centre for Research on Multinational Corporations | From false promises to legal pressure: ExxonMobil’s fight against EU carbon capture rules
  https://www.somo.nl/from-false-promises-to-legal-pressure-exxonmobils-fight-against-eu-carbon-capture-rules/
  > From false promises to legal pressure: ExxonMobil’s fight against EU carbon capture rules COP31 ended without a final decision, but its proposed text reveals a growing paradox in international climate policy. [Figures on the page: standalone; one quarter; attributable to shareholders. Check which one each figure is.]
## AVGO  (8 leads)
- Thu 26 Nov | JournalArta | Broadcom (AVGO) Stock Price Today
  https://journalarta.com/en/2026/11/26/broadcom-shares-slip-to-300-86-as-bear-market-slump-deepens/
  > Broadcom shares slip to $300.86 as bear-market slump deepens Broadcom shares closed at $300.86 on Wednesday, down 15.02% over five sessions and 37.53% below their June peak. Broadcom shares slipped 0.07% to close at $300.86 on Wednesday, extending a slide that leaves the chipmaker deep in bear-market territory. [Figures on the page: unaudited or preliminary; first half. Check which one each figure is.]
- Thu 26 Nov | Seeking Alpha | Broadcom: Why The Market Is Wrong To Sell (NASDAQ:AVGO)
  https://seekingalpha.com/article/4972153-broadcom-why-the-market-is-wrong-to-sell
  > Since my last article on Broadcom Inc. (AVGO), the company’s share price has dropped 20%. Despite this, Broadcom remains a Quality Growth stock, and I'm reiterating my Buy rating, even though one of my arguments from
- Thu 26 Nov | ad-hoc-news.de | Broadcom's Google Order Trim Takes the Shine Off a Bruising Week
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/broadcom-s-google-order-trim-takes-the-shine-off-a-bruising-week/70556310
  > Broadcom shareholders have had little to celebrate over the past seven days.
## BRK.B  (8 leads)
- Thu 26 Nov | Simply Wall St | Berkshire Hathaway And 2 Insurance Stocks Built For Higher US Interest Rates
  https://simplywall.st/stocks/us/diversified-financials/nyse-brk.a/berkshire-hathaway/news/berkshire-hathaway-and-2-insurance-stocks-built-for-higher-u
  > With the market almost pricing in back to back Fed hikes and inflation readings still running hotter than the 2% target, higher borrowing costs are no longer a distant threat but a present filter on which stocks feel comfortable to hold.
- Thu 26 Nov | ad-hoc-news.de | Berkshire Builds 4% Stake in Italy's Bending Spoons While Oregon Court Widens PacifiCorp Wildfire Re
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-builds-4-stake-in-italy-s-bending-spoons-while-oregon-court-widens-pacificorp-wildfire/70555588
  > Berkshire Hathaway disclosed a fresh 4% holding in Italian app developer Bending Spoons on November 16, a filing that also revealed a broader reshuffling of the conglomerate's equity book and coincided with a legal development for its utility arm.
- Thu 26 Nov | Pluang | Investors shift from high-risk AI power stocks to safer, diversified Berkshire Hathaway amid market caution.
  https://pluang.com/en/news-feed/berkshire-tertinggi-ai-energi-bergerak-ke-investasi-konservatif
  (page: did not load (403))
## WMT  (8 leads)
- Thu 26 Nov | JournalArta | Walmart Stock Slips to $131.94 as Tariff Risks Test Rally
  https://journalarta.com/en/2026/11/26/walmart-shares-slip-as-tariff-threats-test-monthly-rally/
  > Walmart shares slip as tariff threats test monthly rally Walmart stock closed at $131.94 on Wednesday, slipping 0.28% after new tariff proposals tempered a month-long rally that has left shares near their annual high. Walmart shares slipped on Wednesday as sweeping new U.S.
- Wed 25 Nov | Investing.com Canada | Form 4 Walmart Inc: Dwayne M. Milum (SVP & Controller) For: 23 November
  https://ca.investing.com/news/stock-market-news/form-4-walmart-inc-dwayne-m-milum-svp--controller-for-23-november-93CH-4981638
  (page: did not load (403))
- Wed 25 Nov | Investing.com | Walmart controller sells nearly $1M in company stock
  https://www.investing.com/news/insider-trading-news/walmart-controller-sells-nearly-1m-in-company-stock-93CH-5051556
  (page: did not load (403))
## V  (8 leads)
- Thu 26 Nov | Kalkine Media | Visa's Rajat Taneja Disposes of 1,712 Shares at $409 Each on November 24, 2026
  https://kalkinemedia.com/us/news/announcements/visas-rajat-taneja-disposes-of-1712-shares-at-409-each-on-november-24-2026
  > On November 25, 2026, Rajat Taneja, Visa Inc.'s President of Technology, submitted a beneficial ownership change statement revealing the sale of 1,712 shares of Visa Class A Common Stock on November 24, 2026. - Reporting individual: Rajat Taneja, President, Technology at Visa Inc.
- Wed 25 Nov | MarketBeat | Visa (NYSE:V) Stock Price Up 2% - Still a Buy?
  https://www.marketbeat.com/instant-alerts/price-visa-nyse-v-stock-price-up-2-still-a-buy-2026-11-25/
  > Visa (NYSE:V) Stock Price Up 2% - Still a Buy? - Visa shares rose 2% to $424.96, with trading volume 12% below its average. - Analyst sentiment is broadly positive: Visa has a consensus “Buy” rating and a $444.60 price target; Wedbush initiated coverage with an “Outperform” rating and a $487 target.
- Wed 25 Nov | MarketWatch | Visa Inc. Cl A stock outperforms competitors on strong trading day
  https://www.marketwatch.com/data-news/visa-inc-cl-a-stock-outperforms-competitors-on-strong-trading-day-3c8cce2b-cbb92e8f4a76?mod=goog_fin_scmw
  (page: did not load (401))
## ORCL  (8 leads)
- Thu 26 Nov | Wisevoter | Oracle Shareholders Approve $884.1M Executive Pay
  https://wisevoter.com/world/us/2026/11/26/oracle-shareholders-approve-884-million-executive-pay
  > Oracle Shareholders Approve $884.1M Executive Pay An advisory vote on named executive officer compensation passed with 63.7% support, aided by votes from chairman Larry Ellison. 26, 2026 in Public Companies Oracle shareholders approved an advisory vote covering $884.1 million in compensation for the company's named executive officers.
- Thu 26 Nov | ad-hoc-news.de | Oracle's Credit Insurance Hits a Record 356 Basis Points as Wall Street Recomputes the AI Payback Cl
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-s-credit-insurance-hits-a-record-356-basis-points-as-wall-street-recomputes-the-ai-payback/70555715
  > Oracle shares slid 5.2% on Tradegate, with the pressure tracing back to the credit market rather than the equity tape. Premiums on five-year credit default swaps for Oracle and other AI-linked companies have climbed to record levels, according to Reuters, with Oracle's spread sitting at 356 basis points.
- Thu 26 Nov | Kotak Neo | Nvidia, Micron and Oracle Shares Fall as AI Sell-Off Continues; Key Reasons Behind the Decline
  https://www.kotakneo.com/news/global-markets/nvidia-micron-oracle-shares-fall-as-ai-selloff-deepens-on-rising-infrastructure-costs-and-debt-concerns/
  > Nvidia, Micron and Oracle Shares Fall as AI Sell-Off Continues; Key Reasons Behind the Decline The Philadelphia Semiconductor Index touched a seven-month low on Wednesday before recovering some of its losses.
- Thu 26 Nov | BeInCrypto | Is Oracle the First AI Casualty as It Sheds 70% of Its Value?
  https://beincrypto.com/oracle-stock-falls-70-ai-debt/
  (page: did not load (403))
- Wed 25 Nov | GuruFocus | Oracle (ORCL) Stock: A Hidden Value Trap? Unpacking the Risks an
  https://www.gurufocus.com/news/9220970/oracle-orcl-stock-a-hidden-value-trap-unpacking-the-risks-and-rewards
- Wed 25 Nov | BigGo Finance | Oracle Shares Sink as Credit Insurance Costs Hit 360 Basis Points on AI Spending Fears
  https://finance.biggo.com/news/d53acd4e-f12e-440e-aa33-7c326ba80fc7
- Wed 25 Nov | MarketBeat | Oracle (NYSE:ORCL) Stock Falls 5.1% - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-falls-51-should-you-sell-2026-11-25/
- Wed 25 Nov | MarketWatch | Oracle, CoreWeave and other tech stocks bounce back after selloff
  https://www.marketwatch.com/story/oracles-stock-sinks-toward-a-3-year-low-as-the-ai-trade-continues-to-unravel-d4698d77
## COST  (8 leads)
- Thu 26 Nov | ad-hoc-news.de | Costco Wholesale stock at EUR 992.85, down 0.32% before trading
  https://www.ad-hoc-news.de/boerse/news/vorboerse/costco-wholesale-stock-at-eur-992-85-down-0-32-before-trading/70556742
  > Costco Wholesale operates membership warehouses and e-commerce sites serving high-volume retail demand. On Xetra, the stock closed at EUR 996.00 on Wednesday, November 25, 2026. Costco stock slips before trading - Costco Wholesale operates membership warehouses and e-commerce sites. - The broader US market context is represented by the S&P 500.
- Thu 26 Nov | JournalArta | Costco shares edge down to $1,086.81 in third straight loss
  https://journalarta.com/en/2026/11/26/costco-shares-edge-down-to-1086-81-as-three-day-slide-continues/
  > Costco shares edge down to $1,086.81 as three-day slide continues Costco Wholesale shares slipped 0.45% to $1,086.81 on Wednesday for a third straight daily decline, while remaining 10.59% higher over the past month. Costco Wholesale shares edged down on Wednesday as the stock extended its losing streak to three sessions.
- Wed 25 Nov | Traders Union | Costco stock edges lower as inflation adds risk to interest rate outlook
  https://tradersunion.com/news/stocks/show/4421749-costco-edges-down-as-inflation/
  (page: did not load (403))
## NFLX  (8 leads)
- Thu 26 Nov | Investing.com | Cathie Wood’s ARK adds to Anthropics stock, trims Netflix
  https://www.investing.com/news/company-news/cathie-woods-ark-adds-to-anthropics-stock-trims-netflix-93CH-5051847
  (page: did not load (403))
- Wed 25 Nov | JournalArta | Netflix Stock Price Today
  https://journalarta.com/en/2026/11/26/netflix-edges-up-to-59-31-on-380-million-studio-deal/
  > Netflix edges up to $59.31 on $380 million studio deal Netflix shares edged up 0.74% to $59.31 in afternoon trading Wednesday following a $380 million deal for Radford Studio Center, extending a three-day rebound from last week's one-year low.
- Wed 25 Nov | 24/7 Wall St. | Netflix Has 2 Growth Engines That Could Drive Its Stock Higher in 2027
  https://247wallst.com/investing/2026/11/25/netflix-has-2-growth-engines-that-could-drive-its-stock-higher-in-2027/
  > Netflix Has 2 Growth Engines That Could Drive Its Stock Higher in 2027 This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them. Netflix (NASDAQ:NFLX | NFLX Price Prediction) now reaches an audience approaching one billion people.
## INTC  (8 leads)
- Thu 26 Nov | MarketBeat | Intel (NASDAQ:INTC) Stock Sale Disclosed by Rep. Kevin Hern
  https://www.marketbeat.com/instant-alerts/congress-intel-nasdaq-intc-stock-sale-disclosed-by-rep-kevin-hern-2026-11-26/
  > Intel (NASDAQ:INTC) Stock Sale Disclosed by Rep. Kevin Hern disclosed selling $15,001–$50,000 of Intel shares on November 9 from his Hern Family Foundation account; the filing was made public November 24. - Intel’s latest quarter beat earnings-per-share expectations, reporting $0.52 versus a $0.41 estimate, while revenue of $16.51 billion came in slightly below forecasts.
- Wed 25 Nov | BeInCrypto | Dell Stock Joins Nvidia, AMD, and Intel Selloff Despite Record Demand
  https://beincrypto.com/dell-stock-falls-ai-selloff-record-backlog/
  (page: did not load (403))
- Wed 25 Nov | FXLeaders | Intel Aims for Strong Rebound as INTC Stock Buyers Defend $50 Support Convincingly after Nvidia Selloff
  https://www.fxleaders.com/news/2026/11/25/intel-aims-for-strong-rebound-as-intc-stock-buyers-defend-50-support-convincingly-after-nvidia-selloff/
  > Intel Aims for Strong Rebound as INTC Stock Buyers Defend $50 Support Convincingly after Nvidia Selloff Intel shares are attempting a rebound after repeatedly holding the $50 level, with confirmation of the first external customer for its advanced 18A manufacturing process providing fresh optimism despite weak guidance, legal challenges and Nvidia reducing its stake.
## LLY  (8 leads)
- Thu 26 Nov | JournalArta | Eli Lilly (LLY) Stock: $1,392.22, Down 1.09% Nov 25
  https://journalarta.com/en/2026/11/26/eli-lilly-lly-stock-falls-1-09-up-8-1-in-a-month/
  > Eli Lilly (LLY) Stock Falls 1.09%: Up 8.1% in a Month Technical analysis of LLY stock on November 25, 2026: price 1,392.22 USD, trend sideways, RSI 56.1, support 1,347.11, resistance 1,443.50. NYSE data on Wednesday, November 25, 2026, showed Eli Lilly sliding 1.09% to $1,392.22. The stock closed below its previous $1,407.59 finish.
- Thu 26 Nov | ad-hoc-news.de | Eli Lilly Balances Label Warning Pressure With Ratings Upgrade and a Burst of Deal Activity
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/eli-lilly-balances-label-warning-pressure-with-ratings-upgrade-and-a-burst-of-deal-activity/70556309
  > Eli Lilly is preparing to add warnings about a rare condition that can cause loss of vision to the labels of its GLP-1 medicines, according to The Straits Times, with the US Food and Drug Administration requesting the notices for the products of both Lilly and Novo Nordisk.
- Wed 25 Nov | Simply Wall St | What Eli Lilly Stock Data Means For Shareholders
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/what-eli-lilly-stock-data-means-for-shareholders
  > - Eli Lilly is set to showcase new data across its breast cancer portfolio at the San Antonio Breast Cancer Symposium, including late breaking Phase 3 EMBER-3 results for Inluriyo and biomarker findings for Verzenio, as well as updated data on investigational PI3Ka inhibitor tersolisib.
Read 89 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, ALCN, MFPC, EAST, EMFD, AMOC.
