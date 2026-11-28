# Desk brief, Saturday, November 28, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 29s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-27 (23.81); Treasury yields to 2026-11-27 (10-year 4.94%).
- **valuation**: ok in 23s (GitHub Actions). LLY: $1.31tn, P/E (last 12 months) 43.6, Forecast P/E (fiscal 2026) 39.0 (the four quarters to Sep 2026)
- **movers**: ok in 18s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-10 LLY results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 down, RSI 43.8
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 51 stocks, k 16.4%, median P/E 9.7; cheapest AMOC +101%, MASR +74%, ORWE +64%; dearest MOIN -66%, BTFH -71%, LCSW -71%
- **views**: ok in 0s (GitHub Actions). 2026-10-30-rotation: on track -> right  (Judged on its date: Walmart and JPMorgan +1.9% on average against Alphabet and Amazon +0.6% since 2026-10-30.)
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 103s (GitHub Actions). 
- **leads**: ok in 80s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

## What moved (latest close against the one before)
- EGX30 50,311.80 (+0.00%); EGX70 EWI 16,886.20 (-0.00%); USD/EGP 54.82 (-0.16%); Gold 21K 5,820.00 (+3.01%); Brent 95.44 (-1.17%); S&P 500 7,297.49 (+1.60%); Nasdaq 24,129.50 (+2.31%); Bitcoin 59,574.00 (-3.27%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): INTC +5.4%, TSLA +5.2%, AMZN +4.0%, AVGO +3.8%, ORAS +3.5%, ORCL +3.1%, META +3.1%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - PHDC: In a downtrend: below its 50-day average, which is below the 200-day; RSI 42, neither stretched nor washed out; the 50-day average crossed below the 200-day today.
    - AAPL: In an uptrend: above its 50-day average, which is above the 200-day; RSI 60, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - INTC: In a downtrend: below its 50-day average, which is below the 200-day; RSI 40, neither stretched nor washed out; the 50-day average crossed below the 200-day today.
    - META: No clear trend: 6.3% below its 50-day average and 0.3% above the 200-day; RSI 50, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - NFLX: In a downtrend: below its 50-day average, which is below the 200-day; RSI 45, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - NVDA: In a downtrend: below its 50-day average, which is below the 200-day; RSI 38, neither stretched nor washed out; the 50-day average crossed below the 200-day today.
    - TSLA: Turning up: above both its 50-day average (5.9% over) and its 200-day (5.0% over), though the 50-day is still below the 200-day; RSI 56, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - WMT: Turning up: above both its 50-day average (12.2% over) and its 200-day (11.7% over), though the 50-day is still below the 200-day; RSI 72, stretched after a run: above 70; momentum turned up 1 sessions ago (MACD crossed its signal line).

## Movers that still need a reason (top five each way, 5% or more)
- US XP (XP) +18.1%; US SNDK (Sandisk) +16.0%; US COHR (Coherent) +14.1%; US ANT (Anthropic, PBC) +11.0%; US ALAB (Astera Labs) +8.7%; US WSO.B (Watsco) -5.4%; US VRTX (Vertex Pharmaceuticals Incorporated) -5.2%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-26 (TradingView's closes; Mubasher's list refused), 192 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (204)
US: 2026-11-27, 840 companies
US week and month: US companies worth $10bn or more (840)
EGX30 heatmap: 2026-11-26, 31 members
US heatmap: 2026-11-27, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-26
## ACAP +12.9%  A Capital Holding
- no headlines found
## VERT +6.9%  Vertika for Industry & Trade
- no headlines found
## LUTS +6.5%  Lotus For Agricultural Investments And Development
- no headlines found
## MAAL +5.6%  Marseilla Al Masreia Al Khalegeya for Holding Investment
- no headlines found
## RAYA +5.2%  Raya Holding for Financial Investments
- no headlines found
## MPCI -6.2%  Memphis Pharmaceutical & Chemical Industries
- no headlines found
## CRST -6.1%  Creast mark For Contracting
- no headlines found
## ZEOT -4.1%  Extracted Oils & Derivatives
- no headlines found
## GTWL -3.3%  Goldentex
- Wed 25 Nov | خاص عن مصر | حركة أسهم البورصة المصرية│ "سبينالكس" تتصدر الارتفاعات بـ7%.. و"جولدن تكس" الأكثر تراجعًا
  https://aboutmsr.com/حركة-أسهم-البورصة-المصرية│-سبينالكس/
- Wed 25 Nov | Pioneers Misr | «بي دي أو كيز» تحدد القيمة العادلة لسهم «جولدن تكس» عند 111.6 جنيه قبل زيادة رأس المال
  https://pioneersmisr.com/124454/
- Wed 25 Nov | شبكة تواصل الإخبارية | «PKF» تحدد القيمة العادلة لسهم جولدن تكس للأصواف عند 111.61 جنيه
  https://twaslnews1.twaslnews.com/8278096/
## KABO -3.2%  El Nasr Clothing & Textiles
- no headlines found

# US 2026-11-27
## XP +18.1%  XP
- Sat 28 Nov | Yahoo Finance | XP Inc. (XP) Goes on a Monster Rally. Here’s What You Need to Know
  https://finance.yahoo.com/markets/stocks/articles/xp-inc-xp-goes-monster-060509360.html
  > (NASDAQ:XP) is one of the 10 Stocks Outshining Wall Street's Biggest Winners. soared by 18.07 percent on Friday to end at $16.99 apiece, mimicking the jump in Brazilian stocks, thanks to a banking executive's appointment as the country's next Finance chief.
- Sat 28 Nov | Yahoo Finance | XP (XP) Stock Still Looks Undervalued Despite A 33% Five Year Fall
  https://finance.yahoo.com/markets/stocks/articles/xp-xp-stock-still-looks-011038040.html
  > has delivered a sharp 29.4% gain over the past week after a mixed multi year share price record, which puts fresh focus on whether that rebound lines up with the returns it earns on its capital.
- Sat 28 Nov | GuruFocus | Is It Too Late to Buy XP Inc (XP) After 18.1% Rally? GF Value Says Undervalued
  https://www.gurufocus.com/news/9229175/is-it-too-late-to-buy-xp-inc-xp-after-181-rally-gf-value-says-undervalued
  (page: did not load (403))
- Fri 27 Nov | Business Upturn | US Stock Movers: GUNN, XP, VERA Lead Gains; VRTX, RHI Slide on Friday
  https://businessupturn.com/usa/money/us-markets/us-stock-movers-gunn-xp-vera-lead-gains-vrtx-rhi-slide-on-friday/
  > US equities closed out Friday's session with a clutch of sharp movers on either side of the ledger, as markets wrapped up trading on 27 November 2026. (GUNN) topped the gainers board, surging 23.88% to close at $6.38, while Brazilian financial platform XP Inc. (XP) jumped 18.07% to $16.99.
## SNDK +16.0%  Sandisk
- Sat 28 Nov | FinanceFeeds | Sandisk Stock $85.36: SNDK Week Ahead After a 16% Rebound
  https://financefeeds.com/sandisk-sndk-stock-85-saturday-week-ahead-after-16-percent-rebound-bull-94-bear-73/
  > - Friday close: $85.36, up 15.96 percent from Wednesday’s $73.61 (Yahoo Finance; The Motley Fool). - Friday range: $77.10-$85.44 (Yahoo Finance). - Split: Sandisk’s 8-for-1 split took effect after the 19 November close.
- Sat 28 Nov | Simply Wall St | Sandisk (SNDK) Stock Could Trade Below Fair Value Despite Its 206% Run
  https://simplywall.st/stocks/us/tech/nasdaq-sndk/sandisk/news/sandisk-sndk-stock-could-trade-below-fair-value-despite-its
  > Sandisk has swung from a sharp retreat in recent weeks to a stock that is still up very strongly over the past year. This puts a spotlight on whether its current valuation can be explained by its earnings power.
- Sat 28 Nov | The Financial Express | AI stocks bounce back: Nvidia, Micron and Sandisk lead stock market rebound
  https://www.financialexpress.com/market/global-markets/ai-stocks-bounce-back-nvidia-micron-and-sandisk-lead-stock-market-rebound/4395797/
  (page: did not load (403))
- Fri 27 Nov | Pluang | Sandisk shares jump nearly 16% as NAND memory d...
  https://pluang.com/en/news-feed/sandisk-melesat-pemulihan-saham-memory-dari-penjualan-ai-27-nov-2026
  (page: did not load (403))
## COHR +14.1%  Coherent
- Sat 28 Nov | Yahoo Finance | Coherent Corp. (COHR) Pulls Off a Jaw-Dropping Comeback
  https://finance.yahoo.com/markets/stocks/articles/coherent-corp-cohr-pulls-off-062107786.html
  > (NYSE:COHR) is one of the 10 Stocks Outshining Wall Street's Biggest Winners. [Figures on the page: one quarter; attributable to shareholders. Check which one each figure is.]
- Fri 27 Nov | GuruFocus | Coherent Corp (COHR) Stock Up 14.1% but GF Value Says Overvalued -- GF Score: 79/100
  https://www.gurufocus.com/news/9229038/coherent-corp-cohr-stock-up-141-but-gf-value-says-overvalued-gf-score-79100
  (page: did not load (403))
- Fri 27 Nov | GuruFocus | Coherent (COHR) Stock: Significantly Overvalued Despite Strong D
  https://www.gurufocus.com/news/9228930/coherent-cohr-stock-significantly-overvalued-despite-strong-daily-surge
  (page: did not load (403))
- Fri 27 Nov | 24/7 Wall St. | Coherent Jumps 12% as Optical Stocks Rebound From Wednesday's AI Selloff; Applied Optoelectronics and Lumentum Rise 7%
  https://247wallst.com/investing/2026/11/27/coherent-jumps-12-as-optical-stocks-rebound-from-wednesdays-ai-selloff-applied-optoelectronics-and-lumentum-rise-7/
  > Coherent Jumps 12% as Optical Stocks Rebound From Wednesday’s AI Selloff; Applied Optoelectronics and Lumentum Rise 7% This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them. [Figures on the page: first half; one quarter. Check which one each figure is.]
## ANT +11.0%  Anthropic, PBC
- Fri 27 Nov | FinancialContent | Anthropic, PBC - Class A Common Stock (Nasdaq:ANT) Stock Quote
  https://markets.financialcontent.com/stocks/quote?Symbol=NQ:ANT
  > | Volume | 143,747,654 | | Open | 84.99 | | Bid (Size) | 91.40 (200) | | Ask (Size) | 91.41 (500) | Close | 82.79 | | Today's Range | 84.51 - 93.39 | | 52wk Range | 73.85 - 115.10 | 20.2% below 52-week high
- Fri 27 Nov | Yahoo Finance | Anthropic, PBC (ANT) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P00035T2Z_AnalystReport_1795778438000/
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | Yahoo Finance Singapore | Anthropic, PBC (1ANT.MU) stock price, news, quote and history
  https://sg.finance.yahoo.com/quote/1ANT.MU/
  (page: did not load (404))
- Thu 26 Nov | Kalkine | Anthropic, PBC Class A Common Stock (NASDAQ: ANT) Share Price, ANT Stock News, ANT Share Price & Updates
  https://kalkine.com.au/company/nasdaq-ant/
  (page: did not load (403))
## ALAB +8.7%  Astera Labs
- Sat 28 Nov | MarketBeat | 1,242,311 Astera Labs, Inc. $ALAB Shares Acquired by Atreides Management LP
  https://www.marketbeat.com/instant-alerts/filing-1242311-astera-labs-inc-alab-shares-acquired-by-atreides-management-lp-2026-11-28/
  > 1,242,311 Astera Labs, Inc. $ALAB Shares Acquired by Atreides Management LP - Atreides Management more than doubled its Astera Labs stake in the third quarter, adding 1.24 million shares to reach 2.46 million shares, valued at about $875 million in its latest filing.
- Fri 27 Nov | MarketBeat | Astera Labs (NASDAQ:ALAB) Shares Climb 7.6% - Still a Buy?
  https://www.marketbeat.com/instant-alerts/price-astera-labs-nasdaq-alab-shares-climb-76-still-a-buy-2026-11-27/
  > Astera Labs (NASDAQ:ALAB) Shares Climb 7.6% - Still a Buy? - Astera Labs shares rose 7.6% to $204.84 in Friday midday trading, though trading volume was 36% below its daily average.
- Fri 27 Nov | Simply Wall St | What Astera Labs Holders Bought Into
  https://simplywall.st/stocks/us/semiconductors/nasdaq-alab/astera-labs/news/what-astera-labs-holders-bought-into
  > If Astera Labs sat on your watchlist instead of in your portfolio, the outcome may feel like a missed shot rather than just an interesting chart. For Astera Labs shareholders, the return over the past year was 20.8%, including dividends.
- Fri 27 Nov | Seeking Alpha | Astera Labs climbs 9% amid broad rally in technology shares (ALAB:NASDAQ)
  https://seekingalpha.com/news/4677097-astera-labs-climbs-9-percent-amid-broad-rally-in-technology-shares
  (page: did not load (403))
## WSO.B -5.4%  Watsco
- Fri 27 Nov | شبكة تواصل الإخبارية | Why Is Watsco (WSO) up 6.7% since last earnings report? | FXStreet
  https://twaslnews1.twaslnews.com/8378001/
  (page: did not load (403))
- Thu 26 Nov | TIKR.com | A $1,200,000 Portfolio in Watsco, Truist and Eversource Pays $51,753 a Year in Dividends. Here’s What Happens if One Cuts
  https://www.tikr.com/blog/a-1200000-portfolio-in-watsco-truist-and-eversource-pays-53196-a-year-in-dividends-heres-what-happens-if-one-cuts
  > - A $1,200,000 portfolio split evenly across Watsco, Truist Financial and Eversource Energy pays about $51,800 a year in dividends at today’s prices, or about $4,310 a month.
- Thu 26 Nov | Yahoo! Finance Canada | Watsco, Inc. (WSO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/WSO/
  (page: did not load (404))
- Thu 26 Nov | Yahoo Finance | Watsco, Inc. (WSO) Stock Forecasts
  https://finance.yahoo.com/research/reports/ARGUS_4353_QuantitativeReport_1795564800000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## VRTX -5.2%  Vertex Pharmaceuticals Incorporated
- Fri 27 Nov | Blockonomi | Vertex Pharma (VRTX) Stock: Falls 5% as FDA Delays Kidney Drug Approval Decision
  https://blockonomi.com/vertex-pharma-vrtx-stock-falls-5-as-fda-delays-kidney-drug-approval-decision/
  > - Vertex Pharma stock drops 5.24% to $534.57 following the FDA’s review extension. - FDA extends the povetacicept approval decision deadline to February 28, 2027. - Vertex faces mounting competition from Otsuka and Vera in kidney disease treatment.
- Fri 27 Nov | Kalkine Media | Vertex Pharmaceuticals Director Alan Garber to Sell 1,291 Shares After Option Exercise
  https://kalkinemedia.com/us/news/announcements/vertex-pharmaceuticals-director-alan-garber-to-sell-1291-shares-after-option-exercise
  (page: did not load (404))
- Fri 27 Nov | Benzinga | Vertex Faces FDA Delay for Povetacicept, Analyst Sees Likely Approval
  https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/11/63674157/vertex-faces-fda-delay-for-povetacicept-analyst-sees-likely-approval
  (page: did not load (403))
- Fri 27 Nov | Seeking Alpha | Vertex falls on “disappointing” FDA delay on kidney drug review; Vera rises
  https://seekingalpha.com/news/4677048-vertex-stock-falls-fda-delays-drug-review
  (page: did not load (403))
## FRHC -3.7%  Freedom Holding
- Sat 28 Nov | GuruFocus | Is Freedom Holding Corp (FRHC) a Bargain After 3.7% Drop? GF Val
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-12-02 ALCN results (expected)
- 2026-12-02 EGAL results (expected)
- 2026-12-02 EMFD results (expected)
- 2026-12-02 NVDA dividend
- 2026-12-02 SKPC results (expected)

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- judged right with no lesson yet: Developers lag while rates stay high  <- write its `lesson`
- judged right with no lesson yet: Money rotates from AI spenders to steady earners  <- write its `lesson`
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
    2026-10-30-developers: on track -> right  (Judged on its date: Talaat Moustafa and Palm Hills -1.0% on average against the EGX30 +1.4% since 2026-10-30.)
    2026-10-30-rotation: on track -> right  (Judged on its date: Walmart and JPMorgan +1.9% on average against Alphabet and Amazon +0.6% since 2026-10-30.)

## Fair value
- Changed since the last run: AMOC +49% -> +101% (medium -> low); ORWE +43% -> +64% (medium -> medium). Dropped out: MHOT.
- Figures to check before trusting (a P/E under 3 or upside above 80%): AMOC (P/E 4.5, +101%).
- In the ten cheapest or dearest with no note: ORWE, EMFD, MCQE, ADIB, PHAR, MTIE, RAYA, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-28. Open each story before using it.
## COMI  (5 leads)
- Sat 28 Nov | بنكي | الوديعة السنوية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/deposits/192
  > من 16% إلى 17% - عايز دخل شهري - 5,000 ج.م فأكثر16.25% - 5,000 ج.م فأكثر16.5% - 5,000 ج.م فأكثر16.75% - 5,000 ج.م فأكثر17% - 5,000 ج.م فأكثر16% وديعة السنة هي الأكثر جاذبية في هذا الجدول، خاصة مع وصول العائد إلى 17% لفئة Private وصرفه شهريًا.
- Fri 27 Nov | بوابة المصرف | القاهرة ينتزع عرش النمو في الاستثمارات المالية.. والتجاري الدولي يتصدر الحجم
  https://www.almasraf.news/القاهرة-ينتزع-عرش-النمو-في-الاستثمارا/
  > في سباق مصرفي تجاوزت فيه المحافظ الاستثمارية حاجز التريليوني جنيه، أعادت البنوك المدرجة بالبورصة المصرية رسم خريطة المنافسة في الاستثمارات المالية خلال الأشهر التسعة الأولى من 2026، بعدما أضافت 340.83 مليار جنيه إلى محافظها، وسط صعود بنك القاهرة إلى قمة معدلات النمو، واحتفاظ البنك التجاري الدولي بأكبر محفظة استثمارية بين البنوك محل المقارنة.
- Fri 27 Nov | مجلة البوصلة الاقتصادية | "جهينة" تؤمن قرض بـ 1.73 مليار جنيه من "البنك التجاري الدولي" لرفع إنتاجية تابعة لها
  https://www.alboslanews.com/أسواق-مال/جهينة-تؤمن-قرض-بـ-173-مليار-جنيه-من-البنك-التجاري-الدولي-لرفع-إنتاجية-تابعة-لها-430448
  > "جهينة" تؤمن قرض بـ 1.73 مليار جنيه من "البنك التجاري الدولي" لرفع إنتاجية تابعة لها الثلاثاء 10 نوفمبر 2026 -03:46 أعلنت شركة جهينة للصناعات الغذائية، أن إحدى شركاتها التابعة "شركة إنماء للثروة الحبوانية"، قامت بتوقيع اتفاقية تمويل بقيمة 1.73 مليار جنيه، مع البنك التجاري الدولي – مصر "سي أي بي". [Figures on the page: standalone; consolidated; first half. Check which one each figure is.]
## TMGH  (8 leads)
- Fri 27 Nov | خاص عن مصر | لينك آند كو 08 تجمع بين الفخامة والتكنولوجيا في تعاون عز العرب وطلعت مصطفى.. ما المواصفات؟
  https://aboutmsr.com/لينك-آند-كو-08-تجمع-بين-الفخامة-والتكنول/
  > أعلنت مجموعة عز العرب للسيارات توقيع شراكة استراتيجية مع مجموعة طلعت مصطفى القابضة، لتقديم سيارة Lynk & Co 08 لمشتري وحدات المرحلة الثانية بمشروعي The Spine وSharm Bay. وتعتمد السيارة المقدمة ضمن الاتفاق على منظومة الدفع الهجين القابل للشحن الخارجي، التي تجمع بين تكنولوجيا المحركات الكهربائية ومحرك الاحتراق الداخلي. لينك آند كو 08..
- Fri 27 Nov | أهل مصر | عز العرب وطلعت مصطفى
  https://ahlmasrnews.com/tags/1464536/عز-العرب-وطلعت-مصطف
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | https://www.youlyou.com/ | «طلعت مصطفى» تعزز مفهوم الحياة المتكاملة في «مدينة نور» بافتتاح «بيت الجملة»
  https://www.youlyou.com/104344
  > تواصل مجموعة طلعت مصطفى ترسيخ مفهوم المدن العمرانية المتكاملة، عبر تطوير منظومة الخدمات والمرافق داخل مدينة نور بشرق القاهرة، بما يضمن توفير مقومات الحياة اليومية للسكان دون الحاجة إلى مغادرة المدينة لتلبية احتياجاتهم الأساسية، في توجه يتجاوز المفهوم التقليدي للتطوير العقاري من بناء الوحدات السكنية إلى إنشاء مجتمعات متكاملة تنبض بالحياة.
## ETEL  (8 leads)
- Sat 28 Nov | Submarine Networks | Telecom Egypt Advances Egypt’s Eastern Digital Corridor with Sharm El Sheikh–Taba Subsea Cable
  https://www.submarinenetworks.com/en/systems/asia-europe-africa/sharm-el-sheikh–taba/telecom-egypt-advances-sharm-ei-sheikh-taba-subsea-cable
  > Technical & Architectural Specifications | Parameter | Sharm El Sheikh–Taba Cable Specification | | Route & Length | Spans approximately 200 km along the eastern coastline of the Sinai Peninsula in the Gulf of Aqaba, linking Sharm El Sheikh (at the southern tip of Sinai) directly to Taba (near the Jordanian border).
- Thu 26 Nov | برلمانى | وزير الاتصالات يطلق مبادرة لمضاعفة تبرعات المواطنين بالتعاون مع شركات المحمول الأربعة.. جنيه المواطن قصاد جنيه من الشركة.. والمصرية للاتصالات تساهم فى توفير الأدوية والأجهزة والمستلزمات اللازمة للمستشفيات
  https://www.parlmany.com/News/2/621705/وزير-الاتصالات-يطلق-مبادرة-لمضاعفة-تبرعات-المواطنين-بالتعاون-مع-شركات
  > تنفيذا لتوجيهات فخامة الرئيس عبد الفتاح السيسى بتقديم الدعم اللازم للمتضررين من حادث حريق الوراق، كلف المهندس رأفت هندي وزير الاتصالات وتكنولوجيا المعلومات الجهاز القومي لتنظيم الاتصالات بإطلاق مبادرة لمضاعفة تبرعات المواطنين بالتعاون مع شركات المحمول الاربعة.
- Thu 26 Nov | اخبارك نت | المصرية للاتصالات تنعى ضحايا حادث الوراق وتضاعف تبرعات WE Pay لدعم المصابين | أموال الغد
  https://www.akhbarak.net/news/details/49572829/4/المصرية-للاتصالات-تنعى-ضحايا-حادث-الوراق-وتضاعف-تبرعات-we-pay-لدعم-المصابين-أموال-الغد
  > أعلنت الشركة المصرية للاتصالات عن مضاعفة قيمة تبرعات عملائها من خلال محفظة WE Pay، لصالح الهلال الأحمر المصري ومستشفى أهل مصر ومستشفى الناس، دعمًا للجهود الإنسانية والطبية التي تقدمها هذه المؤسسات للمصابين بحادث الطريق الدائري.
- Thu 26 Nov | مجلة أرقام | المصرية للاتصالات تضاعف تبرعات عملائها عبر WE Pay لدعم ضحايا ومصابي حريق الوراق
  https://arqam.news/612974/
  > أعلنت الشركة المصرية للاتصالات مضاعفة قيمة تبرعات عملائها من خلال محفظة WE Pay، لصالح ضحايا ومصابي حادث الطريق الدائري بمنطقة الوراق، في إطار التزامها بمسؤوليتها المجتمعية وحرصها على دعم المتضررين من الحادث. وأعربت الشركة عن خالص حزنها وأسفها لضحايا الحادث، مقدمة التعازي وصادق المواساة إلى أسرهم، ومتمنية الشفاء العاجل للمصابين.
- Thu 26 Nov | followict | «المصرية للاتصالات» تضاعف تبرعات عملاء «WE PAY» لدعم مصابي حادث دائري الوراق
  https://followict.news/المصرية-للاتصالات-تضاعف-تبرعات-عمل/
- Thu 26 Nov | جريدة المال | «المصرية للاتصالات» تتحمل تكاليف الأدوية والمستلزمات الطبية لمصابي حادث الوراق
  https://almalnews.com/2149907/«المصرية-للاتصالات»-تتحمل-تكاليف-الأدوية-والمستلزمات-الطبية/
- Thu 26 Nov | جريدة الدستور | لضحايا حادث الوراق.. مضاعفة قيمة التبرعات من خلال محفظة WE Pay
  https://www.dostor.org/5792288
- Thu 26 Nov | موقع الموقع | المصرية للاتصالات تضاعف تبرعات عملائها عبر WE Pay لدعم مصابي حادث الوراق
  https://almawq3.com/المصرية-للاتصالات-تضاعف-تبرعات-عملائ/
## PHDC  (8 leads)
- Fri 27 Nov | اوان مصر | ضبط عامل تشطيبات سرق مجوهرات وأموالًا من فيلا بالم هيلز في 6 أكتوبر
  https://www.awanmasr.com/ضبط-عامل-تشطيبات-سرق-مجوهرات-وأموالًا/
  (page read: it never names the company, so probably not about it: skip)
- Thu 26 Nov | خاص عن مصر | "بالم هيلز" تتعثر في مشروع أبوظبي.. وياسين منصور يبحث عن أرض بديلة في الإمارات
  https://aboutmsr.com/بالم-هيلز-تتعثر-في-مشروع-أبوظبي-وياسي/
  > تعثر مشروع شركة بالم هيلز للتعمير في أبوظبي، بعد انتهاء المهلة المحددة لاستيفاء الشروط المسبقة لعقد المساطحة المبرم مع شركة «ويف سيفين للاستثمار المحدودة»، المالكة لقطعة الأرض المخصصة للمشروع، ما أدى إلى عدم استمرار سريان الاتفاق، ودفع الشركة إلى بحث الخطوات التالية مع شريكتها الإماراتية. [Figures on the page: standalone; consolidated; nine months. Check which one each figure is.]
- Thu 26 Nov | صحيفة اخبارنا | بالم هيلز: عقد مشروع أبوظبي لم يعد ساريا لعدم توصيل المرافق
  https://www.akhbrna.ae/economy/balm-hylz-aqd-mshrwa-abwzby/
  > أعلنت شركة بالم هيلز للتعمير أن عقد المساطحة الخاص بمشروعها في إمارة أبوظبي لم يعد ساريا، بعد انقضاء الموعد النهائي المحدد لاستيفاء الشروط المسبقة الواردة فيه.
## SWDY  (2 leads)
- Thu 26 Nov | جريدة باور نيوز الاخبارية | السويدي للمرافق توقع مذكرة تفاهم مع شنايدر إلكتريك لتعزيز التعاون في كفاءة الطاقة وتطوير الشبكات والتحول الرقمي
  https://powernews.cc/?p=295127
  > في خطوة جديدة لتعزيز الشراكات الاستراتيجية في قطاع الطاقة، وقّعت شركة السويدي للمرافق مذكرة تفاهم مع شركة شنايدر إلكتريك، لاستكشاف فرص التعاون المشترك في عدد من المجالات الحيوية، تشمل كفاءة الطاقة، ورفع موثوقية الشبكات الكهربائية، وإدارة الأصول، والتحول الرقمي.
- Thu 26 Nov | بوابة التكنولوجيا المالية | «شنايدر إلكتريك» و«السويدي» توقعان اتفاقية شراكة لتطوير البنية التحتية وتسريع التحول الرقمي
  https://fintechgate.net/258588
  > تعزيز كفاءة وموثوقية حلول الطاقة «شنايدر إلكتريك» و«السويدي» توقعان اتفاقية شراكة لتطوير البنية التحتية وتسريع التحول الرقمي وقعت شركة شنايدر إلكتريك وشركة السويدي للمرافق (Elsewedy Utilities) اتفاقية شراكة، لإرساء إطار للتعاون طويل الأجل بين الشركتين، يشمل جميع مراحل دورة حياة البنية التحتية.
## ORAS  (3 leads)
- Fri 27 Nov | PropNewsTime | Orascom Construction completes OCI combination, issues 97,201,359 new shares
  https://propnewstime.com/latestnewsstories/NDEwNjk=/orascom-construction-completes-oci-combination-issues-97-201-359-new-shares
  > The Gulf conflict has disrupted global supply chains, pushed... REITs have changed the way commercial real estate is owned a... Orascom Construction PLC has completed its acquisition of OCI Rembrandt Holdings B.V. As consideration, Orascom Construction issued and allotted 97,201,359 new shares to OCI, lifting its issued share capital from 110,243,935 to 207,445,294 shares.
- Thu 26 Nov | EnterpriseAM | Orascom Construction closes OCI deal as NMDC Energy pushes into deepwater fabrication
  https://enterpriseam.com/menaplus/2026/11/27/orascom-construction-closes-oci-deal-as-nmdc-energy-pushes-into-deepwater-fabrication/
  > M&A WATCH- Nassef Sawiris’ two listed companies are back under the same roof: ADX- and EGX-listed Orascom Construction closed its acquisition of OCI Rembrandt Holdings from Dutch-listed OCI Global on Wednesday, according to statements (here, pdf and here, pdf).
- Thu 26 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي»
  https://cnnbusinessarabic.com/finance-markets/1153374/أوراسكوم-كونستراكشون-تنهي-الاستحواذ-على-أو-سي-آي
  > «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي» تاريخ النشر: 25 نوفمبر 2026 آخر تعديل: 25 نوفمبر 2026 97.2 مليون سهم جديد.. كيف تتغير هيكلية أسهم «أوراسكوم كونستراكشون» بعد الاندماج؟
## FWRY  (2 leads)
- Thu 26 Nov | الشرق بلومبرغ | تجارة أفريقيا البينية تنتعش والمدفوعات الرقمية الفورية تتضاعف 3 مرات
  https://asharqbusiness.com/banks/158062/تجارة-أفريقيا-البينية-تنتعش-والمدفوعات-الرقمية-تتضاعف-3-مرات/
  > ارتفعت قيمة التجارة البينية بين دول أفريقيا بنحو 6% العام الماضي لتبلغ 213.8 مليار دولار، لكنها لم تشكل سوى 14.6% من إجمالي تجارة القارة، في ظل التحديات التي تعترض التكامل الاقتصادي الإقليمي، وفقاً لدراسة.
- Thu 26 Nov | شبكة تواصل الإخبارية | تجارة أفريقيا البينية ترتفع 6% إلى 213.8 مليار دولار.. والمدفوعات الفورية تتضاعف 3 مرات
  https://twaslnews1.twaslnews.com/8349675/
  (page: did not load (403))
## HRHO  (3 leads)
- Sat 28 Nov | - سي نيوز | «إي إف جي هيرميس» تقود طرح مصر لتأمينات الحياة بقيمة 9.6 مليار جنيه في البورصة
  https://www.cnewsarab.com/إي-إف-جي-هيرميس-تقود-طرح-مصر-لتأمينات/
  > تولت شركة إي إف جي هيرميس لترويج وتغطية الاكتتاب دور المنسق الدولي الأوحد ومدير الطرح الأوحد للطرح العام الأولي لشركة مصر لتأمينات الحياة في البورصة المصرية، والذي تبلغ قيمته الإجمالية 9.6 مليار جنيه، بسعر نهائي 12.80 جنيه للسهم.
- Sat 28 Nov | التعمير | مصر لتأمينات الحياة تحدد 12.80 جنيه سعراً نهائياً للسهم في البورصة.. و«إي إف جي هيرميس» تتولى إدارة الطرح
  https://eltaameer.com/archives/487174
  > أعلنت شركة مصر لتأمينات الحياة، إحدى كبرى شركات تأمينات الحياة في السوق المصرية، عن تحديد السعر النهائي لطرح أسهمها في البورصة المصرية عند 12.80 جنيه للسهم العادي، وذلك عقب الانتهاء بنجاح من عملية بناء سجل الأوامر للطرح الخاص، في خطوة تمهد لبدء تداول أسهم الشركة بالبورصة.
- Thu 26 Nov | الشرق بلومبرغ | "إي إف جي هيرميس" تتوسع في استشارات الديون مع تباطؤ الاكتتابات
  https://asharqbusiness.com/amp/financing-and-investment/157880/ركود-الاكتتابات-بالشرق-الأوسط-يدفع-efg-نحو-استشارات-الديون/
  > يدفع تباطؤ سوق طروحات الأسهم الجديدة في الشرق الأوسط، التي كانت يوماً مزدهرة، حتى أحد أبرز مستشاري الاكتتابات العامة الأولية في المنطقة إلى التوسع نحو مجالات أخرى.
## JUFO  (2 leads)
- Sat 28 Nov | صدى البلد | مصرع طفل غرقًا في جهينة.. ونقل جثمانه للمستشفى المركزي
  https://www.elbalad.news/7197145
  > لقي طفل في العقد الأول من العمر، مصرعه، في حادث مأساوي بدائرة مركز جهينة جنوب محافظة سوهاج؛ إثر تعرضه لحادث غرق، وتم نقل جثمانه إلى مستشفى جهينة المركزي، فيما باشرت الأجهزة الأمنية التحقيق في ملابسات الواقعة.
- Fri 27 Nov | مجلة البوصلة الاقتصادية | "جهينة" تؤمن قرض بـ 1.73 مليار جنيه من "البنك التجاري الدولي" لرفع إنتاجية تابعة لها
  https://www.alboslanews.com/أسواق-مال/جهينة-تؤمن-قرض-بـ-173-مليار-جنيه-من-البنك-التجاري-الدولي-لرفع-إنتاجية-تابعة-لها-430448
  > "جهينة" تؤمن قرض بـ 1.73 مليار جنيه من "البنك التجاري الدولي" لرفع إنتاجية تابعة لها الثلاثاء 10 نوفمبر 2026 -03:46 أعلنت شركة جهينة للصناعات الغذائية، أن إحدى شركاتها التابعة "شركة إنماء للثروة الحبوانية"، قامت بتوقيع اتفاقية تمويل بقيمة 1.73 مليار جنيه، مع البنك التجاري الدولي – مصر "سي أي بي". [Figures on the page: standalone; consolidated; first half. Check which one each figure is.]
## MFPC  (1 leads)
- Fri 27 Nov | الجمهور الإخباري | موبكو دمياط.. قلعة الأسمدة المصرية تدعم الزراعة والتصدير وتنافس الأسواق العالمية بقوة
  https://www.algomhor.com/518551
  > قلعة الأسمدة المصرية تدعم الزراعة والتصدير وتنافس الأسواق العالمية بقوة تواصل صناعة الأسمدة المصرية ترسيخ مكانتها باعتبارها إحدى أهم الصناعات الاستراتيجية الداعمة للأمن الغذائي والصادرات، ويأتي مجمع شركة مصر لإنتاج الأسمدة «موبكو» بمحافظة دمياط في مقدمة القلاع الصناعية التي تعكس قدرة مصر على تحويل مواردها الطبيعية إلى منتجات ذات قيمة مضافة مرتفعة.
## EFIH  (1 leads)
- Thu 26 Nov | أهل مصر | إي فاينانس تنعي ضحايا حادث الدائري ـ الوراق
  https://ahlmasrnews.com/news/technology/13507424/إي-فاينانس-تنعي-ضحايا-حادث-الدائري-ـ-الوراق
  > نعت مجموعة إي فاينانس للاستثمارات المالية والرقمية ضحايا حادث الدائري ـ الوراق الأليم بكل مشاعر الحزن والأسى. وتتقدم مجموعة إي فاينانس برئاسة إبراهيم سرحان رئيس مجلس الإدارة بخالص التعازي والمواساة لأسر الضحايا، داعين الله أن يتغمدهم بواسع رحمته، وأن يمنّ على المصابين بالشفاء العاجل.
## EMFD  (1 leads)
- Thu 26 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. مدينة مصر وإعمار مصر تتصدران الارتفاعات الخميس
  https://www.osoulmisrmagazine.com/453519
  > الأسهم العقارية بالبورصة المصرية.. مدينة مصر وإعمار مصر تتصدران الارتفاعات الخميس سجلت أسهم الشركات العقارية المقيدة بالبورصة المصرية أداءً إيجابيًا خلال ختام تعاملات جلسة اليوم الخميس، إذ ارتفعت أسعار أسهم 5 شركات، مقابل تراجع سهمين، بينما استقرت 3 أسهم دون تغيير.
## BQDC  (8 leads)
- Fri 27 Nov | موقع في الجامعة | حقوق جامعة العاصمة تنظم دورة مجانية حول العمل المصرفي بمشاركة خبراء من بنك القاهرة
  https://filgamaa.com/حقوق-جامعة-العاصمة-تنظم-دورة-مجانية-حو/
  > نظم مركز الاستشارات القانونية والتدريب المهني بكلية الحقوق جامعة العاصمة دورة تدريبية متخصصة حول «العمل المصرفي»، بمشاركة خبراء من القطاع البنكي، وذلك تحت رعاية الدكتور السيد قنديل رئيس الجامعة، والدكتورة أمل لطفي عميد كلية الحقوق.
- Fri 27 Nov | بنكي | بنك القاهرة يتيح تمويل عضوية الأندية حتى 500 ألف جنيه وسداد حتى 7 سنوات
  https://www.bankygate.com/203230
  > يتيح بنك القاهرة برنامج تمويل عضوية الأندية، لمساعدة العملاء على سداد قيمة الاشتراك في عدد من الأندية الرياضية، من خلال قرض تصل قيمته إلى 500 ألف جنيه، وفترة سداد تمتد إلى 84 شهرًا، مع سعر فائدة يبدأ من 29% متناقصة سنويًا.
- Fri 27 Nov | فيتو | تعرف على الحد الأقصى لسداد قرض المعاشات في بنك القاهرة
  https://www.vetogate.com/5779173
  > تعرف على الحد الأقصى لسداد قرض المعاشات في بنك القاهرة يبحث الكثير من عملاء بنك القاهرة عن الحد الأقصى لمدة سداد قرض المعاشات في الفروع. وأوضح مسؤولو بنك القاهرة أن الحد الأقصى لمدة القرض: 10 سنوات (120 شهرًا) يقدم بنك القاهرة خدمات مصرفية عديدة ومتنوعة لعملائه ومنها قرض المعاش.
## EGAL  (1 leads)
- Thu 26 Nov | جريدة باور نيوز الاخبارية | وفد رفيع المستوى من الاتحاد العام لنقابات عمال مصر في زيارة ميدانية لشركة مصر للألومنيوم بنجع حمادي
  https://powernews.cc/?p=295167
  > في إطار تعزيز التواصل بين القيادات النقابية والعاملين، ودعم الحوار الاجتماعي داخل المؤسسات الصناعية الوطنية، استقبلت شركة مصر للألومنيوم بنجع حمادي وفدًا رفيع المستوى من الاتحاد العام لنقابات عمال مصر، وذلك خلال مشاركتهم في اللقاء التثقيفي الذي عُقد بمحافظة قنا.
## EFID  (2 leads)
- Thu 26 Nov | أصول مصر | إيديتا تضخ 25 مليون دولار في العراق لإنشاء مصنع جديد
  https://www.osoulmisrmagazine.com/453511
  > إيديتا تضخ 25 مليون دولار في العراق لإنشاء مصنع جديد تعتزم شركة إيديتا للصناعات الغذائية ضخ استثمارات بقيمة 25 مليون دولار في السوق العراقية، بالتعاون مع مؤسسة التمويل الدولية (IFC)، لإنشاء مصنع جديد وتشغيل خطوط إنتاج إضافية، بما يرفع طاقتها الإنتاجية في العراق إلى أكثر من مثلي مستواها الحالي خلال العامين المقبلين.
- Thu 26 Nov | جريدة حابي | إيديتا تستثمر 25 مليون دولار لمضاعفة طاقتها الإنتاجية في العراق بالشراكة مع IFC
  https://hapijournal.com/2026/11/26/إيديتا-تستثمر-25-مليون-دولار-لمضاعفة-طاق/
  > رنا ممدوح _ أعلنت شركة إيديتا للصناعات الغذائية ومؤسسة التمويل الدولية (IFC)، عن استثمار بقيمة 25 مليون دولار للتوسع في تصنيع الأغذية محليًا في العراق، وتوفير فرص عمل، وتعزيز سلاسل التوريد المحلية. استكمال تشغيل خطوط إنتاج جديدة ومصنع جديد في العراق خلال العامين المقبلين
## AAPL  (8 leads)
- Sat 28 Nov | MarketBeat | Apple Inc. $AAPL Stock Holdings Reduced by AIA Group Ltd
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-stock-holdings-reduced-by-aia-group-ltd-2026-11-28/
  > $AAPL Stock Holdings Reduced by AIA Group Ltd - AIA Group cut its Apple stake by 7.9% in the third quarter, selling 34,414 shares and retaining 402,495 shares valued at about $134 million.
- Sat 28 Nov | Yahoo Finance | Apple Is Beating the Rest of the "Magnificent Seven" in 2026. Can It Do It Again in 2027?
  https://finance.yahoo.com/markets/stocks/articles/apple-beating-rest-magnificent-seven-011910841.html
  > Apple (NASDAQ:AAPL) is the best-performing "Magnificent Seven" stock of 2026, up nearly 32% year to date. It got there by largely sitting out the data center spending race. The question for 2027 is whether that edge is priced in. Missed Nvidia in 2009?
- Fri 27 Nov | Yahoo! Finance Canada | Apple Inc. (AAPL) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/AAPL/
  > designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories.
## MSFT  (8 leads)
- Sat 28 Nov | www.tokenpost.com | Microsoft Shares Hold Near $496 Pivot as Technical Pullback Persists
  https://www.tokenpost.com/news/investing/64072
  > Microsoft (MSFT) shares were quoted at $495.99 in a Nov. 28 market snapshot, down 0.80% and below the $496.13 pivot as solid quarterly growth contrasted with a technically weak short-term setup. The stock’s 24-hour range was $489.63 to $502.78.
- Sat 28 Nov | Blockchain News | Microsoft (MSFT) Stock Price Prediction: AI-strength narrative meets a technically fragile pullback
  https://blockchain.news/news/20261128-price-prediction-msft-ai-strength-narrative-meets-a-technically
  > What drove the setup Microsoft’s latest reported quarter, released on October 28, 2026, gives the stock a fundamentally solid backdrop even as price action softens. Revenue rose to $92.3 billion, up 19% year over year, operating income increased 21%, and diluted EPS came in at $4.92 on a GAAP basis, up 32%.
- Fri 27 Nov | JournalArta | Microsoft (MSFT) Stock Edges Up to $492.85 in Afternoon Trading
  https://journalarta.com/en/2026/11/28/microsoft-stock-edges-up-as-reliability-push-follows-outage/
  > Microsoft stock edges up as reliability push follows outage Microsoft shares edged up 0.60% to $492.85 in Friday afternoon trading, trailing the broader market as management launched an internal push to speed up outage recovery. [Figures on the page: unaudited or preliminary; first half. Check which one each figure is.]
## NVDA  (8 leads)
- Sat 28 Nov | 24/7 Wall St. | 'He Doesn't Have Integrity': Suze Orman Says Jensen Huang Should 'Never, Ever, Ever Come Back' but Won't Sell a Single Nvidia Share
  https://247wallst.com/personal-finance/2026/11/28/he-doesnt-have-integrity-suze-orman-says-jensen-huang-should-never-ever-ever-come-back-but-wont-sell-a-single-nvidia-share/
  > ‘He Doesn’t Have Integrity’: Suze Orman Says Jensen Huang Should ‘Never, Ever, Ever Come Back’ but Won’t Sell a Single Nvidia Share This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Sat 28 Nov | Fortune | Trump says he talked Nvidia’s board into reinstating Jensen Huang. It’s not the first company he’s stepped into
  https://fortune.com/2026/11/28/trump-jensen-huang-nvidia-intervention/
  > In a tumultuous three weeks, Jensen Huang stepped down as Nvidia’s CEO following revelations of his affairs with a suspected Chinese spy and at least one Nvidia employee. At the time, the company’s board chair said it did not intend to reinstate him, and Huang remained without an employer for 11 days.
- Sat 28 Nov | Oninvest | "Sex, Lies, and Nvidia," Show Business on the Stock Market, "Dove" Lands at the ECB
  https://en.oninvest.com/article/sex-lies-and-nvidia-show-business-on-the-stock-market-dove-lands-at-the-ecb
  > "Sex, Lies, and Nvidia," Show Business on the Stock Market, "Dove" Lands at the ECB The scandal surrounding Jensen Huang suddenly put stock market reports on par with the "celebrity gossip" section.
## AMZN  (8 leads)
- Sat 28 Nov | Finimize | Amazon Jumps As Autos Heads To The UK In 2027
  https://finimize.com/content/amazon-jumps-as-autos-heads-to-the-uk-in-2027
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | TIKR.com | Amazon Hits Its Lowest P/E Ever. Jim Cramer Predicts It Will “Prove to Be the Winner”
  https://www.tikr.com/blog/amazon-hits-its-lowest-p-e-ever-jim-cramer-predicts-it-will-prove-to-be-the-winner?ref=tikrblog
  > - Amazon’s forward P/E has fallen to about 24x, near its lowest in a decade, even as analysts expect its normalized EPS to nearly double from 2025 to 2028. - Voters are turning against new data centers, which makes the capacity AWS already owns worth more. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Fri 27 Nov | GuruFocus | Amazon.com Inc (AMZN) Stock Up 4.0% and Still Undervalued -- GF Score: 94/100
  https://www.gurufocus.com/news/9228891/amazoncom-inc-amzn-stock-up-40-and-still-undervalued-gf-score-94100
  (page: did not load (403))
- Fri 27 Nov | Yahoo Finance | What Amazon.com (AMZN)'s UK Car Marketplace Launch Means For Shareholders
  https://finance.yahoo.com/markets/stocks/articles/amazon-com-amzn-uk-car-221235075.html
  > - Amazon.com is expanding its Amazon Autos online car marketplace to the UK in early 2027, while Amazon Web Services continues to post revenue growth and remains a major contributor to group operating income.
- Fri 27 Nov | MarketBeat | Amazon.com (NASDAQ:AMZN) Stock Jumps 4.2% - Should You Buy?
  https://www.marketbeat.com/instant-alerts/price-amazoncom-nasdaq-amzn-stock-jumps-42-should-you-buy-2026-11-27/
- Fri 27 Nov | Yahoo Finance | Can Record Black Friday Spending Lift Amazon Stock?
  https://finance.yahoo.com/markets/stocks/articles/record-black-friday-spending-lift-203500466.html
- Fri 27 Nov | Yahoo Finance | Amazon Stocks Climb 2.96% as Thanksgiving Online Spending Hits $7.1 Billion
  https://finance.yahoo.com/markets/stocks/articles/amazon-stocks-climb-2-96-190908869.html
- Fri 27 Nov | Wisevoter | Amazon, Meta Discuss Restoring Muse Store Access
  https://wisevoter.com/world/us/2026/11/27/amazon-meta-discuss-restoring-muse-store-access
## GOOGL  (8 leads)
- Sat 28 Nov | FinanceFeeds | GOOG Stock $272.44: Week Ahead After Alphabet’s 52-Week Low
  https://financefeeds.com/alphabet-goog-stock-272-saturday-week-ahead-after-52-week-low-bull-290-bear-260/
  > - Friday close: GOOG $272.44 (Google Finance; Fidelity); GOOGL $274.96, up $1.86 (Yahoo Finance; Finviz). - Friday range: $268.20-$277.30 for GOOG (StockAnalysis). - 52-week low: GOOG touched $260.69 on Wednesday 25 November (CNBC) and closed that day at $270.98, down 2.02 percent; GOOGL’s low was $262.73 (EBC).
- Sat 28 Nov | JournalArta | GOOGL Stock Price Today: Alphabet Closes at $274.96
  https://journalarta.com/en/2026/11/28/alphabet-shares-edge-up-as-bear-market-pressures-linger/
  > Alphabet shares edge up as bear-market pressures linger Alphabet shares edged up 0.68% to $274.96 on Friday, trailing the S&P 500's 1.60% rally as investors weighed heavy AI spending and cash-flow pressures. Alphabet shares edged up on Friday as investors weighed a modest bounce against heavy AI spending pressures.
- Sat 28 Nov | Investing.com Nigeria | Form 4 Alphabet Inc Class A For: 27 November By Investing.com
  https://ng.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-27-november-93CH-2831958
  (page: did not load (403))
## META  (8 leads)
- Sat 28 Nov | Simply Wall St | Meta Platforms (META) Faces Australia Monitoring Law And Fresh EU AI Probes
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/meta-platforms-meta-faces-australia-monitoring-law-and-fresh
  > - Meta Platforms (NasdaqGS:META) faces new regulatory pressure after Australia passed its Digital Duty of Care law in late November 2026. - The Australian regime introduces direct monitoring requirements and heavy fines for content moderation failures targeting Meta and other large platforms.
- Sat 28 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Share Price Breaks Above Two Hundred Day Moving Average - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-share-price-breaks-above-two-hundred-day-moving-average-time-to-sell-2026-11-28/
  > Meta Platforms (NASDAQ:META) Share Price Breaks Above Two Hundred Day Moving Average - Time to Sell? - Meta shares moved above their 200-day moving average, trading as high as $636.62 and last at $629.24, compared with a 200-day average of $627.95.
- Sat 28 Nov | Blockchain News | Meta Platforms (META) Stock Price Prediction: Shares Hold Above Key Support as Analysts Split Over AI Spend
  https://blockchain.news/news/20261128-price-prediction-meta-shares-hold-above-key-support-as
  > Meta Platforms (META) is trying to stabilize after a sharp pullback from its recent highs, with the shares at $627.65 and still above the 200-day average of $625.34, but below the 50-day average at $643.61. That keeps the tape constructive enough to avoid outright trend damage, yet not strong enough to call the rebound confirmed.
- Sat 28 Nov | JournalArta | Meta Stock Price Jumps 3.13% to $628.96 on Two-Day Rally
  https://journalarta.com/en/2026/11/28/meta-shares-jump-to-628-96-as-weekly-gain-tops-5/
  > Meta shares jump to $628.96 as weekly gain tops 5% Meta Platforms shares jumped 3.13% to close at $628.96 on Friday, outpacing the S&P 500 as investors weighed AI shopping growth against regulatory risks.
- Sat 28 Nov | Seeking Alpha | Meta Platforms: Looking Beyond Capex, At Efficiency Gains For 2027 (Upgrade)
  https://seekingalpha.com/article/4972688-meta-platforms-looking-beyond-capex-at-efficiency-gains-for-2027-rating-upgrade
- Fri 27 Nov | Yahoo Finance | Meta’s (META) Muse Could Unlock a New Revenue Stream
  https://finance.yahoo.com/technology/ai/articles/meta-meta-muse-could-unlock-232353308.html
- Fri 27 Nov | GuruFocus | Meta Platforms Inc (META) Shares Surge 3.1% -- What GF Score of 99 Tells Investors
  https://www.gurufocus.com/news/9228898/meta-platforms-inc-meta-shares-surge-31-what-gf-score-of-99-tells-investors
- Fri 27 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Stock Price Up 3.2% - Time to Buy?
  https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-stock-price-up-32-time-to-buy-2026-11-27/
## TSLA  (8 leads)
- Sat 28 Nov | MarketBeat | Tesla, Inc. $TSLA Stock Purchased by Aventura Private Wealth LLC
  https://www.marketbeat.com/instant-alerts/filing-tesla-inc-tsla-stock-purchased-by-aventura-private-wealth-llc-2026-11-28/
  > $TSLA Stock Purchased by Aventura Private Wealth LLC - Aventura Private Wealth increased its Tesla stake by 26.1% in the third quarter, adding 1,354 shares to hold 6,548 shares valued at about $2.32 million. - Other institutional investors also reported purchases, and hedge funds and other institutions collectively own 66.2% of Tesla’s stock.
- Sat 28 Nov | FXLeaders | SpaceX Below $135 IPO Price as All-Stock Tesla Merger Talks Advance Ahead of December 3 Meeting
  https://www.fxleaders.com/news/2026/11/28/spacex-below-135-ipo-price-as-all-stock-tesla-merger-talks-advance-ahead-of-december-3-meeting/
  > SpaceX Below $135 IPO Price as All-Stock Tesla Merger Talks Advance Ahead of December 3 Meeting SpaceX is below its June 2026 initial public offering price of $135 as special board committees from SpaceX and Tesla actively negotiate a potential all-stock merger
- Sat 28 Nov | Yahoo Finance | Tesla Stock And Other Tariff Protected Manufacturers Investors Are Watching
  https://finance.yahoo.com/markets/stocks/articles/tesla-stock-other-tariff-protected-051504941.html
  > Tariffs are back in the headlines, and this round of U.S. moves on Chinese imports is reshaping where factories, profits and risks sit. This article reveals 3 stocks tied to these tariff shocks and explains how the news touches each one.
- Sat 28 Nov | Yahoo Finance | Zero To Sixty: Tesla Cybercab Fleet Tops 1,000 In Texas, Lucid Starts Fully Driverless Tests And Chinese EV Maker Posts Stronger Margins
  https://finance.yahoo.com/markets/stocks/articles/zero-sixty-tesla-cybercab-fleet-001227502.html
  > - Texas Department of Motor Vehicles data now lists 1,107 Cybercabs, bringing the state's total robotaxi vehicles to 1,841. - Nuro, Lucid and Uber began fully driverless public-road testing of Lucid Gravity robotaxis in Palo Alto, Mountain View, Los Altos and Sunnyvale this week.
- Fri 27 Nov | TheStreet | Elon Musk’s SpaceX-Tesla merger push just got a new twist
  https://www.thestreet.com/technology/elon-musks-spacex-tesla-merger-push-just-got-a-new-twist
- Fri 27 Nov | RS Web Solutions | Tesla Stock: Is Buying Before December a Smart Move?
  https://www.rswebsols.com/news/is-it-a-good-idea-to-purchase-tesla-stock-before-december/
- Fri 27 Nov | Yahoo Finance | TSLA Stock Clocks Best Week In 18 Months: Tesla Reportedly Eyes Buying German Toolmaker Amid Cybercab, Optimus Scaling Plans
  https://finance.yahoo.com/markets/stocks/articles/tsla-stock-clocks-best-week-195554419.html
- Fri 27 Nov | FinanceBuzz | Tesla Stock Rallies Despite Lingering Concerns for Investors
  https://financebuzz.com/news/tesla-stock-spacex-merger-speculation
## JPM  (8 leads)
- Sat 28 Nov | teiss | News - Hacker group leaks personal data of JPMorgan’s richest clients
  https://www.teiss.co.uk/news/hacker-group-leaks-personal-data-of-jpmorgans-richest-clients-18506
  > Following JPMorgan Chase’s refusal to pay the ransom, the hacking group n0n has released a database containing sensitive personal information belonging to the bank’s most high-profile clients. Earlier this month, a threat actor operating under the alias “n0n hacking group” claimed to have infiltrated JPMorgan Chase’s internal network and exfiltrated confidential corporate information.
- Fri 27 Nov | Quantisnow | JPM: SEC Form FWP filed by JP Morgan Chase & Co.
  https://www.quantisnow.com/insight/sec-form-fwp-filed-by-jp-morgan-chase-co-6808581
  (page: did not load (403))
- Fri 27 Nov | Yahoo Finance | JPMorgan Chase & Co. (JPM) Outpaces Stock Market Gains: What You Should Know
  https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-co-jpm-outpaces-214502182.html
  > JPMorgan Chase & Co. (JPM) ended the recent trading session at $322.96, demonstrating a +1.96% change from the preceding day's closing price. This change outpaced the S&P 500's 1.6% gain on the day. Meanwhile, the Dow gained 1.18%, and the Nasdaq, a tech-heavy index, added 2.31%.
## XOM  (8 leads)
- Sat 28 Nov | MarketBeat | ExxonMobil (NYSE:XOM) Downgraded by Wall Street Zen to "Hold"
  https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-downgraded-by-wall-street-zen-to-hold-2026-11-28/
  > ExxonMobil (NYSE:XOM) Downgraded by Wall Street Zen to "Hold" - Wall Street Zen downgraded ExxonMobil from “buy” to “hold.” MarketBeat’s analyst consensus is also “hold,” with a $170.79 average price target; ratings include 13 buys, 15 holds and one sell.
- Sat 28 Nov | The Nation Newspaper | SNEPCo, ExxonMobil, Chevron, others for PNC Forum
  https://thenationonlineng.net/snepco-exxonmobil-chevron-others-for-pnc-forum/
  (page: did not load (403))
- Sat 28 Nov | TradingView | Cash flow from financing activities of Exxonmobil Holdings Corporation – BCS:XOM1
  https://www.tradingview.com/symbols/BCS-XOM1/financials-cash-flow/cash-f-financing-activities/
  (page: only 10 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## AVGO  (8 leads)
- Sat 28 Nov | Barchart.com | How Is Broadcom’s Stock Performance Compared to Other Semiconductor Stocks?
  https://www.barchart.com/story/news/9041654/how-is-broadcoms-stock-performance-compared-to-other-semiconductor-stocks
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 28 Nov | MarketBeat | Broadcom Inc. $AVGO Holdings Decreased by Bamco Inc. NY
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-holdings-decreased-by-bamco-inc-ny-2026-11-28/
  > $AVGO Holdings Decreased by Bamco Inc. NY reduced its Broadcom stake by 10.1% in the third quarter, selling 51,940 shares. It retained 462,596 shares valued at approximately $162.5 million.
- Sat 28 Nov | FourWeekMBA | Avago Paid $11.15 a Share for LSI; Broadcom Is Now 44.7x
  https://fourweekmba.com/ai-avago-paid-11-15-a-share-for-lsi-broadcom-is-now-44-7x/
  (page: did not load (403))
- Fri 27 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Jumps 3.6% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-stock-jumps-36-heres-what-happened-2026-11-27/
  > Broadcom (NASDAQ:AVGO) Stock Jumps 3.6% - Here's What Happened - Broadcom shares rose 3.6% to about $311.72 as semiconductor stocks rallied in a post-holiday rebound; trading volume was 33% below its daily average. - Analyst views were mixed, but the consensus remained “Moderate Buy” with an average price target of $525.19.
- Fri 27 Nov | JournalArta | Broadcom (AVGO) Stock Price Today
  https://journalarta.com/en/2026/11/28/broadcom-stock-closes-at-312-34-as-anthropic-rallies-yet-weekly-loss-nears-10/
- Fri 27 Nov | MarketWatch | Broadcom Inc. stock outperforms competitors on strong trading day
  https://www.marketwatch.com/data-news/broadcom-inc-stock-outperforms-competitors-on-strong-trading-day-bbbe48c9-afdf8eb29fe5?mod=mw_quote_news
- Fri 27 Nov | FXLeaders | Broadcom Challenges Nvidia Dominance as AVGO Stock Rebounds Off Support while VMware Expansion and Custom Chips Drive Growth
  https://www.fxleaders.com/news/2026/11/27/broadcom-challenges-nvidia-dominance-as-avgo-stock-rebounds-off-support-while-vmware-expansion-and-custom-chips-drive-growth/
- Fri 27 Nov | Yahoo Finance | What Broadcom Stock's Google Chip Order Cut Means For Shareholders
  https://finance.yahoo.com/markets/stocks/articles/broadcom-stocks-google-chip-order-201047235.html
## BRK.B  (8 leads)
- Sat 28 Nov | Pluang | Berkshire Hathaway trades at a premium, seen as justified amid AI-driven market shifts and strong cash reserves.
  https://pluang.com/en/news-feed/berkshire-hathaway-premium-dibangun-untuk-stres-kredit-ai
  (page: did not load (403))
- Sat 28 Nov | Seeking Alpha | Berkshire Hathaway: A Premium Built For The AI Credit Stress (NYSE:BRK.B)
  https://seekingalpha.com/article/4972708-berkshire-hathaway-a-premium-built-for-the-ai-credit-stress
  (page: did not load (403))
- Sat 28 Nov | ad-hoc-news.de | Berkshire Trims Bank of America, Builds Lennar Stake as Argus Flags Stretched Valuation
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-trims-bank-of-america-builds-lennar-stake-as-argus-flags-stretched-valuation/70563992
  > Berkshire Hathaway disclosed a fresh round of portfolio adjustments on November 16, revealing larger positions in homebuilder Lennar and a reduced stake in Bank of America in its mandatory quarterly filing. [Figures on the page: standalone; one quarter. Check which one each figure is.]
## WMT  (8 leads)
- Sat 28 Nov | Mashable | Black Friday PS5 and PS5 Pro deals: Check inventory at Amazon, Walmart, Target, and Best Buy
  https://mashable.com/tech/black-friday-best-ps5-deals-2026
  > If you are trying to get your hands on a PlayStation 5 right now, the real win is not a discount — it is simply finding one in stock at standard retail price.
- Sat 28 Nov | JournalArta | Walmart Stock Closes at $133.13 After 9.80% One-Month Gain
  https://journalarta.com/en/2026/11/28/walmart-shares-edge-up-to-133-13-as-black-friday-online-sales-climb/
  > Walmart shares edge up to $133.13 as Black Friday online sales climb Walmart shares closed at $133.13 on Friday, up 0.90% on light volume, leaving the stock 0.80% below its yearly high and 15.28 percentage points ahead of the S&P 500 over the past month. Walmart shares edged up on Friday as U.S.
- Sat 28 Nov | Yahoo Finance | Walmart bets shoppers won't notice its holiday price increases
  https://finance.yahoo.com/markets/stocks/articles/walmart-bets-shoppers-wont-notice-001700015.html
  > Walmart has quietly cut back on its rollbacks, the company's name for price cuts, as it heads into the holiday season. It's a change the company made after greatly increasing its discounts to help struggling consumers. "In the summer… we had just over 11,000 rollbacks in Walmart U.S.
## V  (8 leads)
- Sat 28 Nov | CEOWORLD magazine | Norwegian-American Billionaire Andreas Halvorsen's Viking Global Buys Mastercard, Sells 32.6 Percent of Its Visa
  https://ceoworld.biz/2026/11/28/norwegian-american-billionaire-andreas-halvorsens-viking-global-buys-mastercard-sells-32-6-percent-of-its-visa/
  > Andreas Halvorsen’s firm sold about a third of its Visa shares and still ended the quarter with more of its reported portfolio in card networks, a trade that points at next year’s bank contract renewals.
- Sat 28 Nov | Yahoo! Finance Canada | Visa Inc. (V) Options Chain - Yahoo Finance
  https://ca.finance.yahoo.com/quote/V/options/?date=1798675200&straddle=false&type=all
  > NYSE - Nasdaq Real Time Price  USD       Visa Inc. Options data delayed by 15 minutes.
- Fri 27 Nov | MarketBeat | Visa (NYSE:V) Shares Up 1.4% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-visa-nyse-v-shares-up-14-heres-why-2026-11-27/
  > Visa (NYSE:V) Shares Up 1.4% - Here's Why - Visa shares rose 1.4% to about $430.49, while trading volume was 51% below its average. - Analyst sentiment remains positive: Wedbush initiated coverage with an Outperform rating and a $487 target, and the consensus rating is Buy with an average target of $444.60.
## ORCL  (8 leads)
- Sat 28 Nov | FourWeekMBA | Oracle Paid $11.25 a Share for Retek; Its Stock Is Now 8.7x
  https://fourweekmba.com/ai-oracle-paid-11-25-a-share-for-retek-its-stock-is-now-8-7x/
  (page: did not load (403))
- Sat 28 Nov | ad-hoc-news.de | Oracle Has the OpenAI Cheque Covered — Now Comes the Hard Part
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/oracle-has-the-openai-cheque-covered-now-comes-the-hard-part/70563700
  > Oracle's stock slipped below its $116 issue price on November 20, caught in a broad selloff across AI and software names, Reuters reported. The shares added 1.2% on Tradegate yesterday, yet they have shed 22% over the past 30 days.
- Fri 27 Nov | GuruFocus | Oracle Corp (ORCL) Stock Up 3.1% and Still Undervalued -- GF Score: 89/100
  https://www.gurufocus.com/news/9228907/oracle-corp-orcl-stock-up-31-and-still-undervalued-gf-score-89100
  (page: did not load (403))
- Fri 27 Nov | MarketBeat | Oracle (NYSE:ORCL) Stock Jumps 3.5% - Still a Buy?
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-jumps-35-still-a-buy-2026-11-27/
  > Oracle (NYSE:ORCL) Stock Jumps 3.5% - Still a Buy? - Oracle shares rose 3.5% to about $107.55 in Friday trading, while volume was 49% below its average. - Analyst sentiment is broadly positive: the consensus rating is “Moderate Buy,” with an average price target of $249.27, though ratings range from buy to sell.
- Fri 27 Nov | Yahoo Finance | Oracle is Living on a Prayer and It’s Not Even Halfway There
  https://finance.yahoo.com/markets/stocks/articles/oracle-living-prayer-not-even-211217776.html
- Fri 27 Nov | JournalArta | Oracle Stock Price Today: ORCL Jumps 3.13% to $107.13
  https://journalarta.com/en/2026/11/28/oracle-stock-rebounds-above-107-as-tech-shares-rally/
- Fri 27 Nov | TradingKey | Oracle Corp Stock (ORCL) Moved Up by 3.16% on Nov 27: What Signal Does It Send?
  https://www.tradingkey.com/news/market-movers/262325731-market-movers-orcl-20261127
- Fri 27 Nov | Pluang | Oracle stock seen worth $133 even with zero AI revenue; investor buys at $104 expecting 28% upside.
  https://pluang.com/en/news-feed/oracle-saham-nilai-133-beli-di-104-ai-nol-pendapatan
## COST  (8 leads)
- Sat 28 Nov | ChartMill | Costco Wholesale (NASDAQ:COST): A Quality Investing Case Study
  https://www.chartmill.com/news/COST/Chartmill-59262-Costco-Wholesale-NASDAQCOST-A-Quality-Investing-Case-Study
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 28 Nov | Yahoo Finance | Black Friday Push Could Be A Big Moment For Costco Stock (COST)
  https://finance.yahoo.com/markets/stocks/articles/black-friday-push-could-big-001331089.html
  > - Costco Wholesale has been in focus after a holiday period that combined wider Black Friday discounts, strong online promotion, and extended delivery and marketplace partnerships with platforms like DoorDash and Uber Eats.
- Fri 27 Nov | TIKR.com | 12 Big Funds Bought Costco Wholesale Last Quarter, While 7 Sold. Who’s Right?
  https://www.tikr.com/blog/12-big-funds-bought-costco-wholesale-last-quarter-while-7-sold-whos-right
  > - Of 460 big funds that have filed 13Fs for the quarter ended Sept. 30, 12 bought Costco Wholesale and 7 sold, and the sellers moved far more money. - Costco is up 19% from its Sept. 30 close, and at 48x forward earnings it trades well above its five-year average of 43x.
## NFLX  (8 leads)
- Sat 28 Nov | Demokratis.co.id | Netflix Shares The Hunting Wives Kiss Clip on Thanksgiving
  https://demokratis.co.id/en/netflix-hunting-wives-thanksgiving-clip
  > Netflix Shares The Hunting Wives Kiss Clip on Thanksgiving A Thanksgiving social media post from Netflix featuring an intimate scene between Brittany Snow and Malin Akerman in The Hunting Wives drew reactions from broadcaster Piers Morgan and Donald Trump Jr. criticized Netflix's decision to share the scene during the holiday.
- Sat 28 Nov | JournalArta | Netflix Stock Down 36.64% This Year as Disney Licenses Titles
  https://journalarta.com/en/2026/11/28/netflix-stock-disney-deal-engagement-guidance/
  > Netflix Stock Down 36.64% This Year as Disney Licenses Titles Netflix shares are down 36.64% this year after a collapsed acquisition and a cut to the company’s advertising revenue outlook. A Disney licensing deal brings more titles to Netflix, but Wells Fargo has warned that weak viewing engagement could lead members to cancel.
- Fri 27 Nov | Wisevoter | Netflix Shares First Look at Watcher Season 2
  https://wisevoter.com/world/us/ny/new-york-city/2026/11/27/naomi-watts-filming-watcher-season-2-nyc
  > Netflix Shares First Look at Watcher Season 2 Naomi Watts is filming new scenes on the streets of New York City as production on the second season of The Watcher gets underway. 27, 2026 in Television
- Fri 27 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Stock Jumps 2% - Time to Buy?
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-stock-jumps-2-time-to-buy-2026-11-27/
  > Netflix (NASDAQ:NFLX) Stock Jumps 2% - Time to Buy? - Netflix shares rose 2% to $60.63 in Friday trading, while volume was 49% below its average. - Analysts maintain a “Moderate Buy” consensus, with an average price target of $89.14; views range from Buy and Strong Buy ratings to 17 Holds and two Sells.
- Fri 27 Nov | Yahoo Finance | Netflix (NFLX) Beats Stock Market Upswing: What Investors Need to Know
  https://finance.yahoo.com/markets/stocks/articles/netflix-nflx-beats-stock-market-214502710.html
- Fri 27 Nov | Pluang | Netflix plans ad expansion and aims to grow ope...
  https://pluang.com/en/news-feed/ini-yang-bakal-membuktikan-saya-salah-tentang-saham-netflix
- Fri 27 Nov | Breitbart News | Netflix Celebrates Thanksgiving by Sharing Adulterous Lesbian Sex Scene from ‘The Hunting Wives’: ‘No Wonder Your Stock Is in the Toilet’
  https://www.breitbart.com/entertainment/2026/11/27/netflix-celebrates-thanksgiving-by-sharing-adulterous-lesbian-sex-scene-from-the-hunting-wives-no-wonder-your-stock-is-in-the-toilet/
- Fri 27 Nov | Pluang | Netflix churn improves despite price hikes; Ama...
  https://pluang.com/en/news-feed/3-saham-terbaik-untuk-dibeli-di-desember-dan-disimpan-hingga-2027
## INTC  (8 leads)
- Sat 28 Nov | Investing.com Canada | Arista Networks, Intel among market cap stock movers on Friday By Investing.com
  https://ca.investing.com/news/stock-market-news/arista-networks-intel-among-market-cap-stock-movers-on-friday-93CH-4983650
  (page: did not load (403))
- Fri 27 Nov | GuruFocus | Intel Corp (INTC) Shares Surge 5.4% -- What GF Score of 70 Tells Investors
  https://www.gurufocus.com/news/9228908/intel-corp-intc-shares-surge-54-what-gf-score-of-70-tells-investors
  (page: did not load (403))
- Fri 27 Nov | Pluang | Intel shares jump 5.38% amid chip sector reboun...
  https://pluang.com/en/news-feed/saham-chip-menguat-berkat-antusiasme-ai-nov-27-2026
  (page: did not load (403))
- Fri 27 Nov | MarketBeat | Intel (NASDAQ:INTC) Shares Climb 4.9% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-intel-nasdaq-intc-shares-climb-49-heres-why-2026-11-27/
  > Intel (NASDAQ:INTC) Shares Climb 4.9% - Here's Why - Intel shares rose 4.9% as chip stocks broadly rebounded, with investors buying after recent weakness. - Investors are also watching Microsoft’s plans to use Intel Foundry’s EMIB packaging for Azure silicon and multi-year Xeon supply arrangements, as well as Intel’s recent data-center growth.
- Fri 27 Nov | www.tokenpost.com | Intel Leads Chip Stock Rebound After Foundry Business Updates
  https://www.tokenpost.com/news/investing/63894
- Fri 27 Nov | Crypto Briefing | Intel leads chip stock rebound as AI enthusiasm returns
  https://cryptobriefing.com/intel-leads-chip-stock-rebound-ai/
- Fri 27 Nov | Kalkine Media | Can Intel (NASDAQ:INTC) Turn Attention Into Lasting Growth?
  https://kalkinemedia.com/us/stocks/technology/can-intel-nasdaqintc-turn-attention-into-lasting-growth
- Fri 27 Nov | GuruFocus | Intel Stocks Climb 2.86% as Court Filings Detail Washington's 10% Stake Push
  https://www.gurufocus.com/news/9228786/intel-stocks-climb-286-as-court-filings-detail-washingtons-10-stake-push
## LLY  (8 leads)
- Sat 28 Nov | Barchart.com | Eli Lilly and Company Stock: Is LLY Outperforming the Healthcare Sector?
  https://www.barchart.com/story/news/9041294/eli-lilly-and-company-stock-is-lly-outperforming-the-healthcare-sector
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 28 Nov | Pluang | Eli Lilly leads in GLP-1 weight-loss drugs but faces high stock valuation and patent risks.
  https://pluang.com/en/news-feed/analisis-saham-eli-lilly-pertumbuhan-dan-risiko-obat-glp-1
  (page: did not load (403))
- Fri 27 Nov | ad-hoc-news.de | Moody's Hands Eli Lilly a Two-Notch Credit Boost as Buyouts and Label Changes Reshape the Story
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/moody-s-hands-eli-lilly-a-two-notch-credit-boost-as-buyouts-and-label-changes-reshape-the-story/70563145
  > Eli Lilly's balance sheet earned a fresh vote of confidence this week, with Moody's Ratings lifting the drugmaker's issuer rating to Aa2 from Aa3 on Tuesday.
Read 85 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ABUK, CLHO, ALCN, EAST, AMOC, SKPC.
