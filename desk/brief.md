# Desk brief, Wednesday, November 25, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 26s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-24 (26.36); Treasury yields to 2026-11-24 (10-year 4.91%).
- **valuation**: ok in 22s (GitHub Actions). LLY: $1.33tn, P/E (last 12 months) 44.1, Forecast P/E (fiscal 2026) 39.5 (the four quarters to Sep 2026)
- **movers**: ok in 18s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 47.2
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.3%, median P/E 9.8; cheapest MASR +73%, AMOC +47%, EMFD +42%; dearest ARAB -64%, MOIN -64%, BTFH -69%
- **views**: ok in 0s (GitHub Actions). 2026-11-11-value-basket: on track -> open
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 138s (GitHub Actions). 
- **leads**: ok in 91s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 2 needed a retry.

## What moved (latest close against the one before)
- EGX30 50,885.30 (+0.34%); EGX70 EWI 17,112.80 (+0.09%); USD/EGP 54.23 (-0.40%); Gold 21K 5,680.00 (+1.97%); Brent 91.40 (+2.27%); S&P 500 7,201.09 (-0.50%); Nasdaq 23,733.54 (-1.48%); Bitcoin 59,748.00 (-1.10%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): INTC -8.1%, NVDA -5.9%, SKPC +5.4%, AVGO -4.0%, ORCL -3.7%, LLY +3.2%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - COMI: In a downtrend: below its 50-day average, which is below the 200-day; RSI 49, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - SKPC: In a downtrend: below its 50-day average, which is below the 200-day; RSI 49, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - WMT: Turning up: above both its 50-day average (12.5% over) and its 200-day (11.0% over), though the 50-day is still below the 200-day; RSI 71, stretched after a run: above 70.

## Movers that still need a reason (top five each way, 5% or more)
- EGX GRCA (Grand Investment Capital) +11.7%; EGX UBEE (United Bank) +10.1%; EGX CRST (Creast mark For Contracting) +9.7%; EGX HBCO (Heibco for Commercial Investments & Real Estate Development) +7.3%; EGX GTWL (Goldentex) +7.2%; EGX INEG (Integrated Engineering Group) -6.8%; EGX CPME (Catalyst Partners Middle East) -6.7%; EGX AXPH (Alexandria Company for Pharmaceuticals and Chemical Industries) -5.7%; EGX ELWA (Elwadi for International Investment & Development) -5.2%; US KYMR (Kymera Therapeutics) +15.7%; US DKS (Dick's Sporting Goods) +14.6%; US INSM (Insmed Incorporated) +14.1%; US DLTR (Dollar Tree) +11.2%; US PCVX (Vaxcyte) +11.0%; US ADI (Analog Devices) -17.4%; US HPE (Hewlett Packard Enterprise) -16.3%; US ALAB (Astera Labs) -13.9%; US SITM (SiTime) -13.8%; US MTSI (MACOM Technology Solutions Holdings) -13.4%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-24 (TradingView's closes; Mubasher's list refused), 202 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (207)
US: 2026-11-24, 829 companies
US week and month: US companies worth $10bn or more (828)
EGX30 heatmap: 2026-11-24, 31 members
US heatmap: 2026-11-24, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-24
## GRCA +11.7%  Grand Investment Capital
- no headlines found
## UBEE +10.1%  United Bank
- Wed 25 Nov | Proshare | CardinalStone: United Bank for Africa: Higher Impairments and Taxation Weigh on Earnings
  https://proshare.co/articles/cardinalstone-united-bank-for-africa-higher-impairments-and-taxation-weigh-on-earnings?menu=Market&classification=Read&category=Stock & Analyst Updates
  > United Bank for Africa Plc (NGX: UBA) reported a 25.3% YoY decline in PAT in its unaudited 9M’26 results, following a 4.8x jump in net impairment charges and a higher Effective Tax Rate (ETR). [Figures on the page: standalone; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Wed 25 Nov | Investify | UBL Share Price Today - United Bank Ltd
  https://www.investify.pk/company/UBL/quote
  > United Bank Ltd Share price today About UBL share price United Bank Ltd (UBL) is listed on the Pakistan Stock Exchange in the Commercial Banks sector.
- Tue 24 Nov | Investify | UBL Stock Discussion and Investor Sentiment - United Bank Ltd
  https://www.investify.pk/company/UBL/discussion
  > United Bank Ltd Stock discussion and investor sentiment InvestifyOfficial Investify accountWelcome to the UBL discussion! Share your views on United Bank Ltd: results, dividends, announcements and price moves. United Bank Ltd (UBL) is listed on the Pakistan Stock Exchange in the Commercial Banks sector.
- Mon 23 Nov | Investify | UBL Financial Results & Fundamentals - United Bank Ltd
  https://www.investify.pk/company/UBL/fundamentals
  > United Bank Ltd Financial results & fundamentals Reported earnings per share BASED ON 2026 3Q BASED ON 2025 4Q United Bank Ltd (UBL) is listed on the Pakistan Stock Exchange in the Commercial Banks sector. The available annual EPS for UBL is PKR 51.12 for 2025 FY.
## CRST +9.7%  Creast mark For Contracting
- no headlines found
## HBCO +7.3%  Heibco for Commercial Investments & Real Estate Development
- no headlines found
## GTWL +7.2%  Goldentex
- Tue 24 Nov | اخبارك نت | «الرقابة المالية» توافق على دعوة قدامى مساهمي «جولدن تكس» للاكتتاب في زيادة رأس المال إلى 500 مليون جنيه | أموال الغد
  https://akhbarak.net/news/details/49568207/4/الرقابة-المالية-توافق-على-دعوة-قدامى-مساهمي-جولدن-تكس-للاكتتاب-في-زيادة-رأس-المال-إلى-500-مليون-جنيه-أموال-الغد
  > وافقت الهيئة العامة للرقابة المالية على قيام شركة جولدن تكس للأصواف بنشر دعوة قدامى المساهمين للاكتتاب في أسهم زيادة رأس المال المصدر من 142.83 مليون جنيه إلى 500 مليون جنيه، بزيادة قدرها 357.17 مليون جنيه.
- Tue 24 Nov | شبكة تواصل الإخبارية | جولدن تكس للأصواف ترفع رأسمالها إلى 500 مليون جنيه
  https://twaslnews1.twaslnews.com/8216518/
  (page: did not load (403))
- Tue 24 Nov | جريدة المال | جولدن تكس ترفع رأسمالها إلى 500 مليون جنيه عبر زيادة بقيمة 357.2 مليون
  https://almalnews.com/2149243/جولدن-تكس-ترفع-رأسمالها-إلى-500-مليون/
  > حصلت شركة جولدن تكس للأصواف على عدم ممانعة مبدئية من الهيئة العامة للرقابة المالية لنشر دعوة قدامى المساهمين للاكتتاب في زيادة رأس المال المصدر والمدفوع من 142.8 مليون جنيه إلى 500 مليون جنيه، بزيادة قدرها 357.2 مليون جنيه. [Figures on the page: standalone; unaudited or preliminary. Check which one each figure is.]
- Tue 24 Nov | موقع الحرية الإخباري | الرقابة المالية توافق على نشر دعوة اكتتاب زيادة رأسمال «جولدن تكس للأصواف» لـ 500 مليون جنيه
  https://alhorianews.com/الرقابة-المالية-توافق-على-نشر-دعوة-ا/
  > أعلنت البورصة المصرية، اليوم الثلاثاء 24 نوفمبر 2026، عن ورود بيان من الهيئة العامة لـ الرقابة المالية يتضمن عدم ممانعتها بصفة مبدئية على قيام شركة «جولدن تكس للأصواف» بنشر دعوة قدامى المساهمين للاكتتاب في أسهم زيادة رأس مال الشركة المصدر والمدفوع من 142.83 مليون جنيه إلى 500 مليون جنيه.
## INEG -6.8%  Integrated Engineering Group
- no headlines found
## CPME -6.7%  Catalyst Partners Middle East
- no headlines found
## AXPH -5.7%  Alexandria Company for Pharmaceuticals and Chemical Industries
- no headlines found
## ELWA -5.2%  Elwadi for International Investment & Development
- no headlines found
## OIH -4.9%  Orascom Investment Holding
- no headlines found

# US 2026-11-24
## KYMR +15.7%  Kymera Therapeutics
- Wed 25 Nov | Investing.com Canada | Form 424B5 Kymera Therapeutics Inc For: 25 November By Investing.com
  https://ca.investing.com/news/stock-market-news/form-424b5-kymera-therapeutics-inc-for-25-november-93CH-4980009
  (page: did not load (403))
- Wed 25 Nov | Yahoo Finance | Kymera Therapeutics (KYMR) Gets a Massive 16% Lift From Wall Street
  https://finance.yahoo.com/healthcare/articles/kymera-therapeutics-kymr-gets-massive-020804682.html
  > (NASDAQ:KYMR) is one of the 10 Stocks With Easy Double-Digit Gains.
- Wed 25 Nov | MLQ.ai | Kymera raises about $1.93 billion in an upsized stock sale at $150.37 after its eczema pill data
  https://mlq.ai/news/kymera-raises-about-193-billion-in-an-upsized-stock-sale-at-15037-after-its-eczema-pill-data/
  (page: did not load (403))
- Tue 24 Nov | Stock Titan | Merrill Lynch and BTIG are named in a proposed Kymera Therapeutics (KYMR) stock sale.
  https://www.stocktitan.net/sec-filings/KYMR/144-kymera-therapeutics-inc-sec-filing-747ae74c363c.html
  > Kymera Therapeutics holder proposes $8.62M, $5.12M sales Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
## DKS +14.6%  Dick's Sporting Goods
- Wed 25 Nov | Yahoo Finance | Dick's Sporting Goods Inc (DKS) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P000001PL_AnalystReport_1795550709000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Wed 25 Nov | The Globe and Mail | Dick's Stock Rocks on Tuesday. Here's Why.
  https://www.theglobeandmail.com/investing/markets/stocks/DKS/pressreleases/8989600/dicks-stock-rocks-on-tuesday-heres-why/
  > - Dick's beat on top and bottom lines in this morning's earnings report. - Profit more than doubled -- but analysts see a sharp slowdown in Dick's future. Dick's Sporting Goods (NYSE:DKS). Shares of the sporting goods chain surged 15.3% higher through 11 a.m.
- Tue 24 Nov | GuruFocus | A Look at Dick's Sporting Goods Inc (DKS) After 14.6% Gain -- GF Value $297.35 vs Price $153.17
  https://www.gurufocus.com/news/9218648/a-look-at-dicks-sporting-goods-inc-dks-after-146-gain-gf-value-29735-vs-price-15317
  (page: did not load (403))
- Tue 24 Nov | Pluang | Dick's Sporting Goods stock jumps 14.6% after b...
  https://pluang.com/en/news-feed/dicks-sporting-goods-naikkan-perkiraan-laba-foot-locker-pulih
  (page: did not load (403))
## INSM +14.1%  Insmed Incorporated
- Wed 25 Nov | Seeking Alpha | Insmed Incorporated (INSM) Sanofi - M&A Call - Slideshow
  https://seekingalpha.com/article/4971684-insmed-incorporated-insm-sanofi-m-and-a-call-slideshow
  (page: did not load (403))
- Wed 25 Nov | Benzinga | Sanofi (SNY) Stock Is Trending After Hours on $41 Billion Insmed Acquisition
  https://www.benzinga.com/markets/equities/26/11/63613533/sanofi-shares-after-hours-insmed-acquisition-deal
  (page: did not load (403))
- Tue 24 Nov | TradingView | Insmed Incorporated Stock 12‑Month Price Target Cut to $185.32, Implies 24% Upside
  https://www.tradingview.com/news/tradingview:4f3e8a8d537f7:0-insmed-incorporated-stock-12-month-price-target-cut-to-185-32-implies-24-upside/
  > Insmed Incorporated Stock 12‑Month Price Target Cut to $185.32, Implies 24% Upside Less than 1 min read - According to estimates from 19 analysts, Insmed Incorporated stock's average price target has fallen from $186.3 to $185.32, with forecasts ranging from $158 to $220 per share
- Tue 24 Nov | Quantisnow | INSM: Insmed agrees to be acquired by Sanofi for $175 per share in cash
  https://www.quantisnow.com/insight/sec-form-defa14a-filed-by-insmed-incorporated-6805516
  (page: did not load (403))
## DLTR +11.2%  Dollar Tree
- Wed 25 Nov | Trefis | Why Dollar Tree Stock Jumped Despite A Margin Slip
  https://www.trefis.com/stock/dltr/articles/628749/why-dollar-tree-stock-jumped-despite-a-margin-slip/2026-11-25
  > Why Dollar Tree Stock Jumped Despite A Margin Slip Dollar Tree stock rose 11.2% on Tuesday, Nov 24, to close at $154.65. The S&P 500 fell 0.50% the same day. Comparable store sales, meaning sales at stores open at least a year, rose 4.6%.
- Wed 25 Nov | The Motley Fool | Dollar Tree's Customer Traffic Jumped 3.8% as Comparable Sales Beat Its Outlook. Here's What's Behind the Gains.
  https://www.fool.com/investing/2026/11/25/dollar-tree-s-customer-traffic-jumped-3-8-as-comparable-sales-beat-its-outlook-here-s-what-s-behind-the-gains/
  > By Isac Simon – Updated - Dollar Tree has attracted customers across income profiles as inflation-weary shoppers increasingly seek affordable everyday essentials. Shoppers are looking to squeeze every last bit of value from every dollar spent.
- Wed 25 Nov | JournalArta | Walmart stock gains 2.1% to $132.31 as discount retailers rally after Dollar Tree results
  https://journalarta.com/en/2026/11/25/walmart-stock-gains-2-1-to-132-31-as-discount-retailers-rally-after-dollar-tree-results/
  > Walmart stock gains 2.1% to $132.31 as discount retailers rally after Dollar Tree results Walmart shares closed Tuesday at $132.31, a third straight gain, as discounters rose on Dollar Tree's raised outlook while the S&P 500 slipped.
- Wed 25 Nov | Yahoo Finance | Dollar Tree (DLTR) is On Fire After Hitting This Big Achievement
  https://finance.yahoo.com/markets/stocks/articles/dollar-tree-dltr-fire-hitting-014249646.html
  > (NASDAQ:DLTR) is one of the 10 Stocks With Easy Double-Digit Gains. Dollar Tree soared to a new three-year high on Tuesday after raising its growth outlook for fiscal 2026 and posting a strong performance in the third quarter of the year.
## PCVX +11.0%  Vaxcyte
- Tue 24 Nov | Yahoo! Finance Canada | Vaxcyte, Inc. (PCVX) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/PCVX/
  > NasdaqGS - BOATS Real Time Price  USD       Vaxcyte, Inc. - Previous Close  56.90 - Day's Range  56.00 - 63.62 - 52 Week Range  42.40 - 90.75 - Market Cap (intraday)  10.001B - Beta (5Y Monthly) -- - 1y Target Est  --
- Tue 24 Nov | GuruFocus | Vaxcyte (PCVX) Stock Is Up 10.3% Today as Biotech Stocks Rally
  https://www.gurufocus.com/news/9218362/vaxcyte-pcvx-stock-is-up-103-today-as-biotech-stocks-rally
  (page: did not load (403))
## ADI -17.4%  Analog Devices
- Wed 25 Nov | Trefis | Analog Devices Stock At $313: How Low Can It Go?
  https://www.trefis.com/stock/adi/articles/628707/analog-devices-stock-at-313-how-low-can-it-go/2026-11-25
  > Analog Devices Stock At $313: How Low Can It Go? Today’s big story: Anthropic Below Its IPO Price: Do Giants Come Back? Analog Devices (ADI) fell 17.4% on Tuesday, Nov 24, to $312.95. It was the stock’s worst day since Trefis price data begins in 2003.
- Wed 25 Nov | Yahoo Finance | Analog Devices (ADI) Takes a Major Beating as Bulls Retreat
  https://finance.yahoo.com/markets/stocks/articles/analog-devices-adi-takes-major-053913801.html
  > (NASDAQ:ADI) is one of the 10 Stocks Investors Are Dumping. Analog Devices fell by 17.37 percent on Tuesday to end at $312.95 apiece as investors resorted to profit-taking following the previous day's gains.
- Wed 25 Nov | Startup Fortune | Analog Devices falls 17% after an earnings beat and drags Texas Instruments down
  https://startupfortune.com/analog-devices-falls-17-after-an-earnings-beat-and-drags-texas-instruments-down/
  > Beating the numbers bought Analog Devices nothing on Tuesday. If you own industrial or auto chip stocks, the question is whether the AI sell-off has started to leak into the part of the market that was supposed to be insulated from it.
- Wed 25 Nov | Financial-News.co.uk | Analog Devices posts record results as shares keep sliding
  https://www.financial-news.co.uk/analog-devices-posts-record-results-as-shares-keep-sliding/
  > Analog Devices (NASDAQ: ADI) reported record results for its fiscal fourth quarter and full year on 24 November 2026. Fourth-quarter revenue came in at $4.37bn, taking fiscal 2026 revenue to $15.2bn, up 38% on the year, according to the company’s annual filing with the SEC.
## HPE -16.3%  Hewlett Packard Enterprise
- Wed 25 Nov | Yahoo Finance | Hewlett Packard Enterprise (HPE) Suddenly Loses Its Shine. What Went Wrong?
  https://finance.yahoo.com/markets/stocks/articles/hewlett-packard-enterprise-hpe-suddenly-053159181.html
  > Hewlett Packard Enterprise Company (NYSE:HPE) is one of the 10 Stocks Investors Are Dumping. Hewlett Packard Enterprise dropped its share price by 16.31 percent on Tuesday to end at $40.19 apiece amid a combination of profit-taking and investor concerns over weak earnings.
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-25 CLHO results (expected)
- 2026-11-25 EAST results (expected)  <- write its preview
- 2026-11-25 EFIH results (expected)  <- write its preview
- 2026-11-25 JUFO results (expected)
- 2026-12-02 ALCN results (expected)
- 2026-12-02 AMOC results (expected)
- 2026-12-02 EGAL results (expected)
- 2026-12-02 EMFD results (expected)
- 2026-12-02 NVDA dividend
- 2026-12-02 SKPC results (expected)

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (open)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
    2026-11-11-value-basket: on track -> open

## Fair value
- Changed since the last run: AMOC -8% -> +47% (high -> medium); MFPC +43% -> +40% (medium -> high); MHOT new at -8%; HDBK +4% -> -9% (medium -> low).
- In the ten cheapest or dearest with no note: AMOC, EMFD, MCQE, ADIB, MHOT, MTIE, AMIA, LCSW, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-25. Open each story before using it.
## COMI  (8 leads)
- Wed 25 Nov | موقع الحرية الإخباري | بعائد 19% يصرف شهريًا.. تفاصيل شهادة الادخار الثلاثية الجديدة من البنك التجاري الدولي
  https://alhorianews.com/بعائد-19-يصرف-شهريًا-تفاصيل-شهادة-الادخ/
  > أعلن البنك التجاري الدولي (CIB) عن تحديث سعر العائد على شهادات الادخار الثابتة لمدة 3 سنوات بالعملة المحلية (الجنيه المصري)، ليصل إلى 19% سنويًا بدورية صرف شهرية، جاء ذلك في إطار خطة البنك لتحديث أوعيته الادخارية وتلبية احتياجات العملاء الباحثين عن دخل شهري ثابت.
- Tue 24 Nov | أسواق للمعلومات | CIB يرفع سعر العائد على شهادة الادخار Premium إلى 19%
  https://www.aswaqinformation.com/260015
  > CIB يرفع سعر العائد على شهادة الادخار Premium إلى 19% محمد علاء أسواق للمعلومات رفع البنك التجاري الدولي – مصر (CIB)، سعر العائد على شهادة الادخار Premium الثلاثية ذات العائد الثابت، إلى 19% بدورية صرف شهرية. والحد الأدنى لشراء الشهادة 50 ألف جنيه، مع إمكانية زيادة قيمة الشراء بمضاعفات الألف جنيه.
- Tue 24 Nov | شبكة تواصل الإخبارية | بنك CIB يرفع العائد على الشهادة الثلاثية الثابتة إلى 19% سنوياً
  https://twaslnews1.twaslnews.com/8235189/
  (page: did not load (403))
## TMGH  (3 leads)
- Tue 24 Nov | جريدة البورصة | سهم طلعت مصطفى يرتفع 2.28% خلال تعاملات البورصة اليوم
  https://alborsaanews.com/2026/11/24/2008848
  > سجل سهم مجموعة طلعت مصطفى القابضة أداءً إيجابيًا خلال تعاملات البورصة المصرية اليوم الثلاثاء، بعدما ارتفع بنسبة 2.28% ليصل إلى مستوى 80.80 جنيه، مواصلًا التحرك في المنطقة الخضراء بالتزامن مع عودة الصعود إلى مؤشرات السوق الرئيسية.
- Tue 24 Nov | جريدة المال | سهم طلعت مصطفى يقفز بنسبة 2.28% خلال تعاملات البورصة اليوم
  https://almalnews.com/2149469/سهم-طلعت-مصطفى-يقفز-بنسبة-2-28/
  (same wording as the جريدة البورصة story above: one source, not two)
- Tue 24 Nov | بنكي | بطاقة ماستركارد تيتانيوم TMG — بنك الامارات دبي الوطني مصر
  https://www.bankygate.com/products/cards/42
  > بطاقة ماستركارد تيتانيوم TMG بطاقة ممتازة لمن يتعاملون بانتظام مع مجموعة طلعت مصطفى بفضل مكافآتها السخية، رغم ضرورة الانتباه لارتفاع رسومها وفوائدها عند التأخير في السداد. - الرسوم السنوية 400 ج.م أعلى من متوسط 22 كارت تيتانيوم (375 ج.م) - معدل الفائدة السنوي الفعلي 79.38% أعلى من متوسط 21 كارت تيتانيوم (64.78%)
## PHDC  (2 leads)
- Tue 24 Nov | نيوز رووم | بالم هيلز أمام فرصة صعود 83%.. «الأهلي فاروس» تحدد القيمة العادلة للسهم عند 21.40 جنيه
  https://newsroom.info/488456
  > بالم هيلز أمام فرصة صعود 83%.. «الأهلي فاروس» تحدد القيمة العادلة للسهم عند 21.40 جنيه
- Tue 24 Nov | اليوم السابع | الكبار يبيعون أسهم CIB وبالم هيلز ومستشفى النزهة وشراء في "جهينة"
  https://www.youm7.com/story/2026/11/24/الكبار-يبيعون-أسهم-CIB-وبالم-هيلز-ومستشفى-النزهة-وشراء-في/7630345
  (page: did not load (TimeoutError))
## SWDY  (2 leads)
- Tue 24 Nov | شبكة تواصل الإخبارية | شواحن السيارات الكهربائية في مصر على موعد مع طفرة.. «السويدي» تستهدف إنتاج أكثر من 25 ألف شاحن سنويا
  https://twaslnews1.twaslnews.com/8202507/
  (page: did not load (403))
- Mon 23 Nov | جريدة باور نيوز الاخبارية | «نقل الكهرباء» تُصدر أمر توريد لـ«إيجيتك للكابلات السويدي» لاحلال موصلات الخط الهوائي المزدوج الدائرة بين «بلاط» و«موط» جهد 66 كيلوفولت
  https://powernews.cc/?p=294830
  > أصدرت الشركة المصرية لنقل الكهرباء أمر توريد لشركة «إيجيتك للكابلات (السويدي) لتنفيذ أعمال تصنيع وتوريد ونقل موصلات حرارية بسعة 1200 أمبير، مع ملحقاتها المعدنية وقطع الغيار، ضمن مشروع إحلال موصلات الخط الهوائي المزدوج الدائرة بين «بلاط» و«موط» بجهد 66 كيلوفولت، بطول إجمالي يبلغ 30 كيلومترًا مسارًا.
## ORAS  (8 leads)
- Wed 25 Nov | اليوم السابع | أوراسكوم كونستراكشون تحسم الدمج مع "OCI" وتطرح 97.2 مليون سهم جديد
  https://www.youm7.com/story/2026/11/25/أوراسكوم-كونستراكشون-تحسم-الدمج-مع-OCI-وتطرح-97-2-مليون/7631639
  > أعلنت شركة أوراسكوم كونستراكشون بي. سي، إتمام عملية الاستحواذ على شركة "OCI Rembrandt Holdings B.V" من شركة "OCI N.V"، في خطوة تمثل إنجازًا رئيسيًا ضمن عملية الاندماج التي سبق الإعلان عنها بين الشركتين.
- Wed 25 Nov | الخلاصة نت | أوراسكوم كونستراكشون تنهي الاستحواذ على أو سي آي وتصدر أسهماً جديدة
  https://www.khlaasa.net/1538802
  > أعلنت شركة أوراسكوم كونستراكشون عن إتمام عملية الاستحواذ على شركة أو سي آي، وذلك من خلال شركتها التابعة أو سي آي ريمبرانت هولدينغز، كجزء من عملية الاندماج المعلنة مسبقاً بين الشركتين.
- Wed 25 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي»
  https://cnnbusinessarabic.com/finance-markets/1153374/أوراسكوم-كونستراكشون-تنهي-الاستحواذ-على-أو-سي-آي
  > «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي» تاريخ النشر: قبل 22 دقيقة آخر تعديل: قبل 21 دقيقة 97.2 مليون سهم جديد.. كيف تتغير هيكلية أسهم «أوراسكوم كونستراكشون» بعد الاندماج؟
## FWRY  (2 leads)
- Mon 23 Nov | سودان تربيون | بنك السودان يستعد لإطلاق منصة موحدة للدفع الفوري
  https://sudantribune.net/article/321565
  > الخرطوم 23 نوفمبر 2026- يستعد بنك السودان المركزي لإطلاق النظام القومي للدفع الفوري (NIPS)، في خطوة تستهدف تطوير البنية التحتية للمدفوعات الرقمية في السودان، وتمكين التحويلات والمدفوعات الفورية بين الأفراد والمصارف والجهات الحكومية والمنشآت التجارية، عبر منصة قومية موحدة تعمل على مدار الساعة.
- Mon 23 Nov | العربية | السودان يعلن تفاصيل نظام الدفع الفوري.. تحويلات بدون إنترنت
  https://www.alarabiya.net/amp/aswaq/economy/2026/11/23/السودان-يعلن-تفاصيل-نظام-الدفع-الفوري-تحويلات-بدون-انترنت
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
## HRHO  (8 leads)
- Tue 24 Nov | جريدة المال | إي اف چي هيرميس لترويج وتغطية الاكتتاب
  https://almalnews.com/tag/إي-اف-چي-هيرميس-لترويج-وتغطية-الاكتتاب/1/
  (page: only 31 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 24 Nov | أراجيك | EFG Hermes ONE and Bank NXT Launch Egypt’s First Bank-Brokerage Credit Card
  https://www.arageek.com/en/efg-hermes-one-and-bank-nxt-launch-egypts-first-bank-brokerage-credit-card
  > - Bank NXT and EFG Hermes launched a Visa co-branded credit card in Egypt. - The card is for clients of the EFG Hermes ONE investment app. - Cashback goes straight into users' EFG Hermes ONE wallets to reinvest. - It offers airport lounge access and instalments of up to 60 months.
- Tue 24 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 24 Nov | Sortir à Paris | قفز هيرميس 2027 في القصر الكبير بباريس - المواعيد
  https://www.sortiraparis.com/ar/altarfihi/alriyada-walrafaahiya/articles/47137-mwa-yd-saut-hermes-2027-fy-alqsr-alkbyr-bbarys
  > تعود منافسات سوت هيرميس أيام الجمعة 19 والسبت 20 والأحد 21 مارس 2027 إلى القصر الكبير في باريس. وتجمع هذه المسابقة الدولية لقفز الحواجز من فئة الخمس نجوم (CSI 5*) أبرز فرسان العالم، إلى جانب الفرسان الشباب دون سن الخامسة والعشرين.
- Tue 24 Nov | بوابة المصرف | إي إف چي هيرميس تقود طرح مصر لتأمينات الحياة بالبورصة بقيمة تصل إلى 10.2 مليار جنيه
  https://www.almasraf.news/إي-إف-چي-هيرميس-تقود-طرح-مصر-لتأمينات-ال/
- Tue 24 Nov | بوابة المصرف | 750 مليون سهم.. إي اف چي هيرميس تدير اكتتاب مصر لتأمينات الحياة بالبورصة
  https://www.almasraf.news/750-مليون-سهم-إي-اف-چي-هيرميس-تدير-اكتتاب-م/
- Tue 24 Nov | مجلة أرقام | بإدارة إي اف چي هيرميس.. مصر لتأمينات الحياة تطرح 15% من أسهمها بالبورصة بسعر يصل إلى 13.60 جنيه
  https://arqam.news/612343/
- Mon 23 Nov | The TRADE | People Moves Monday: TD Securities, Verition Fund Management and EFG Holding
  https://www.thetradenews.com/people-moves-monday-td-securities-verition-fund-management-and-efg-holding/
## JUFO  (5 leads)
- Tue 24 Nov | جريدة المال | زيادة جديدة في أسعار ألبان جهينة.. ارتفاع سعر عبوة اللتر إلى 57 جنيهًا للمستهلك
  https://almalnews.com/2149368/زيادة-جديدة-في-أسعار-ألبان-جهينة-ارتفاع/
  > أخطرت شركة جهينة للصناعات الغذائية التجار والموزعين بتطبيق زيادة جديدة على أسعار عدد من منتجات الألبان، اعتبارًا من الأحد المقبل، في خطوة تشمل مجموعة من أصناف اللبن بأحجامها المختلفة، وفقًا لحازم المنوفي، عضو شعبة المواد الغذائية.
- Tue 24 Nov | اليوم السابع | الكبار يبيعون أسهم CIB وبالم هيلز ومستشفى النزهة وشراء في "جهينة"
  https://www.youm7.com/story/2026/11/24/الكبار-يبيعون-أسهم-CIB-وبالم-هيلز-ومستشفى-النزهة-وشراء-في/7630345
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية، خلال جلسة تداول أمس الإثنين، تنفيذ عمليات شراء وبيع على أسهم 28 شركة، تنوعت بين تحركات للداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم، وفقًا لبيانات التداول المعلنة.
- Tue 24 Nov | جريدة المستقبل | اعتبارًا من الأحد المقبل| زيادة جديدة في أسعار ألبان جهينة
  https://www.elmostaqbal.com/879113/اعتبارًا-من-الأحد-المقبل-زيادة-جديدة-ف/
  > أعلنت شركة جهينة عن تطبيق زيادة جديدة في أسعار عدد من منتجات الألبان اعتبارًا من الأحد المقبل. وذلك وفقًا لما أخطرت به التجار والموزعين، بحسب تصريحات حازم المنوفي، عضو شعبة المواد الغذائية. زيادة سعر كرتونة لبن جهينة حيث سجل سعر كرتونة لبن جهينة 1 لتر نحو 650 جنيهًا، بواقع 54.2 جنيه للوحدة.
## MFPC  (1 leads)
- Tue 24 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EFIH  (2 leads)
- Tue 24 Nov | جريدة المطور | البنك الأهلي المصري و«إي نوفيت» التابعة لـ«إي فاينانس» يوقعان بروتوكول تعاون لتعزيز تأمين معاملات الشراء عبر الإنترنت
  https://almotawwer.com/top-article/335346/
  > البنك الأهلي المصري و«إي نوفيت» التابعة لـ«إي فاينانس» يوقعان بروتوكول تعاون لتعزيز تأمين معاملات الشراء عبر الإنترنت محمد الأتربي: حماية بيانات العملاء وتأمين معاملاتهم المالية على رأس أولويات البنك الأهلي المصري
- Tue 24 Nov | Masrawy | بروتوكول بين البنك الأهلي وشركة تابعة لـ"إي فاينانس" لتعزيز تأمين معاملات الشراء عبر الإنترنت
  https://www.masrawy.com/news/news-banking/details/2026/11/24/3083849/بروتوكول-بين-البنك-الأهلي-وشركة-تابعة-لـ-إي-فاينانس-لتعزيز-تأمين-معاملات-الشراء-عبر-الإنترنت
  > أعلن البنك الأهلي المصري توقيع بروتوكول تعاون مع شركة إي نوفيت، التابعة لمجموعة إي فاينانس للاستثمارات المالية والرقمية، بهدف تعزيز منظومة تأمين معاملات الشراء عبر الإنترنت باستخدام البطاقات الصادرة من البنك الأهلي المصري، من خلال إتاحة خدمة الرقم السري المتغير (One Time Password – OTP) 3D-Secure، وذلك في إطار استراتيجية البنك المستمرة لتطوير خدماته المصرفية ...
## EMFD  (1 leads)
- Tue 24 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. أوراسكوم للتنمية وإعمار مصر تتصدران الارتفاعات الثلاثاء
  https://www.osoulmisrmagazine.com/453340
  > الأسهم العقارية بالبورصة المصرية.. أوراسكوم للتنمية وإعمار مصر تتصدران الارتفاعات الثلاثاء سجلت أسهم الشركات العقارية المقيدة بالبورصة المصرية أداءً متباينًا خلال ختام تعاملات جلسة اليوم الثلاثاء، إذ ارتفعت أسعار أسهم 6 شركات، مقابل تراجع أسهم 3 شركات، بينما استقر سهم المطورون العرب القابضة دون تغيير.
## BQDC  (8 leads)
- Wed 25 Nov | مباشر بنوك مصر | بنك القاهرة يطرح شهادة "بريمو" الثابتة بحد أدنى 1000 جنيه
  https://egyptbanks.info/13308/article/بنك-القاهرة-يطرح-شهادة-بريمو-الثابتة-بحد-أدنى-1000-جنيه
  > أعلن بنك القاهرة عن طرح شهادة الادخار "بريمو" ذات العائد السنوي الثابت، والذي يصل لـ 19.75% حسب اختلاف دورية الصرف. ويمكن للبنك إصدار الشهادة للأفراد فقط، ولمدة 3 سنوات، وبحد أدنى 1000 جنيه ومضاعفاتها لإصدار الشهادة، وبدورية صرف يومية أو شهرية أو ربع سنوية أو سنوية.
- Wed 25 Nov | شبكة تواصل الإخبارية | المدعى عليهم: أردنيون.. أقامها: بنك القاهرة عمان (أسماء)
  https://twaslnews1.twaslnews.com/8268444/
  (page: did not load (403))
- Wed 25 Nov | https://www.youlyou.com/ | بعائد يصل إلى 19.75%.. تفاصيل شهادة بريمو الجديدة من بنك القاهرة
  https://www.youlyou.com/102336
  > أعلن بنك القاهرة طرح شهادات الادخار بريمو ذات العائد الثابت لمدة 3 سنوات بالجنيه المصري، بعائد يصل إلى 19.75% سنويًا، مع إتاحة 4 دوريات مختلفة لصرف الأرباح، لتلبية احتياجات العملاء الراغبين في استثمار مدخراتهم والحصول على دخل دوري.
- Tue 24 Nov | مصر الآن | بنك القاهرة يطرح شهادات «بريمو» الثلاثية بعائد ثابت يصل إلى 19.75%.. التفاصيل كاملة
  https://misrelaan.com/article/144198/بنك-القاهرة-يطرح-شهادات-«بريمو»-الثلاثية
  > بنك القاهرة يطرح شهادات «بريمو» الثلاثية بعائد ثابت يصل إلى 19.75%.. أعلن بنك القاهرة طرح شهادات الادخار «بريمو» ذات العائد الثابت لمدة 3 سنوات بالجنيه المصري، بمعدلات عائد تصل إلى 19.75% سنويًا، مع إتاحة 4 دوريات لصرف العائد، لتلبية احتياجات العملاء وتفضيلاتهم الادخارية.
- Tue 24 Nov | فيتو | تفاصيل شهادة البريمو من بنك القاهرة
  https://www.vetogate.com/5777513
- Tue 24 Nov | شبكة تواصل الإخبارية | بنك القاهرة يطرح شهادات ”بريمو” الثلاثية بعائد يصل إلى 19.75% سنويًا
  https://twaslnews1.twaslnews.com/8245420/
- Tue 24 Nov | صراحة نيوز | بنك القاهرة عمان وصيفاً لبطولة البنوك الخامسة لكرة القدم 2026
  https://www.sarahanews.net/1411392-بنك-القاهرة-عمان-وصيفاً-لبطولة-البنوك/
- Tue 24 Nov | الوطن | بعائد 19.75%.. كل ما تريد معرفته عن شهادة بنك القاهرة «بريمو» الثلاثية
  https://www.elwatannews.com/news/details/8403223
## EGAL  (4 leads)
- Wed 25 Nov | جريدة المال | بحوث نعيم توصي بشراء سهم مصر للألومنيوم عند سعر مستهدف 392.7 جنيه
  https://almalnews.com/2149522/بحوث-نعيم-توصي-بشراء-سهم-مصر-للألومنيوم/
  > قالت بحوث “نعيم للوساطة في الأوراق المالية” إن شركة “مصر للألومنيوم” حققت نتائج إيجابية وقوية للغاية خلال الربع الأول من العام المالي 2026/ 2027، حيث قفز صافي الربح بنسبة %104.0 على أساس سنوي ليصل إلى 4.93 مليار جنيه مقارنة، بـ 2.42 مليار في الفترة المقابلة، مدعوماً باتساع حاد في الهوامش التشغيلية والمالية.
- Wed 25 Nov | الأسبوع | بمشاركة 500 قيادة عمالية ونقابية.. مؤتمر عمالي بـ«مصر للألومنيوم» في نجع حمادي لدعم الدولة وتعزيز الإنتاج
  https://www.elaosboa.com/3033313/
  > بمشاركة 500 قيادة عمالية ونقابية.. مؤتمر عمالي بـ«مصر للألومنيوم» في نجع حمادي لدعم الدولة وتعزيز الإنتاج
- Tue 24 Nov | صدى الأمة | مصر للألومنيوم بنجع حمادي تستضيف مؤتمرًا عماليًا لتعزيز الوعي بقضايا الوطن ودعم زيادة الإنتاج
  https://www.sadaelomma.com/2026/11/blog-post_693.html
  (page: did not load (429))
## SKPC  (1 leads)
- Tue 24 Nov | جريدة المال | سيدي كرير للبتروكيماويات تتصدر ارتفاعات أسهم قطاع الموارد الأساسية بالبورصة المصرية خلال تعاملات الثلاثاء
  https://almalnews.com/2149405/سيدي-كرير-للبتروكيماويات-تتصدر-ارتفاعات-أسهم-قطاع/
  > تصدرت شركة سيدي كرير للبتروكيماويات «سيدبك» ارتفاعات أسهم قطاع الموارد الأساسية بالبورصة المصرية خلال تعاملات جلسة الثلاثاء، بعدما صعد سهمها بنسبة 5.36% ليغلق عند 14.94 جنيه، بقيمة تداول بلغت 89.16 مليون جنيه، من خلال تنفيذ 1590 عملية.
## EFID  (8 leads)
- Mon 23 Nov | Investing.com Canada | Edita Food Industries S.A.E (CAI:EFID) Q3 2026 Earnings Call Highlights: Record Revenue of EGP7. ... By GuruFocus
  https://ca.investing.com/news/company-news/edita-food-industries-sae-caiefid-q3-2026-earnings-call-highlights-record-revenue-of-egp7--4976438
  (page: did not load (403))
- Mon 23 Nov | Trendtype | Dislog and Edita end their joint venture in Morocco
  https://trendtype.com/insights/dislog-and-edita-end-their-joint-venture-in-morocco/
  (page: only 55 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | Food Business Middle East & Africa | Edita Food Industries profit jumps 65% in first nine months
  https://www.foodbusinessmea.com/edita-food-industries-profit-jumps-65-in-first-nine-months/
  > Record quarterly sales and higher volumes supported earnings growth, while the Egyptian snack maker continued investing in production capacity and expanding its regional operations. [Figures on the page: nine months; first half; one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 23 Nov | جريدة البورصة | الرقابة المالية تعتمد تخفيض رأسمال "إيديتا" 416.7 مليون جنيه
  https://alborsaanews.com/2026/11/23/2008303
  > قالت الهيئة العامة للرقابة المالية، إنها لا مانع لديها على نشر تقرير الإفصاح لشركة إيديتا للصناعات الغذائية، تمهيداً للسير في إجراءات دعوة الجمعية العامة غير العادية للشركة، للنظر في تخفيض رأس المال المصدر من 418.9 إلى 416.7 مليون جنيه. [Figures on the page: unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Mon 23 Nov | عالم المال | الرقابة المالية توافق على نشر إفصاح «إيديتا» بشأن تخفيض رأس المال
  https://alamalmal.net/article/943955/الرقابة-المالية-توافق-على-نشر-إفصاح-«إيديتا»
- Mon 23 Nov | موقع الحرية الإخباري | بقيمة 2.2 مليون جنيه.. الرقابة المالية توافق لإيديتا على السير في إجراءات تخفيض رأس المال
  https://alhorianews.com/بقيمة-2-2-مليون-جنيه-الرقابة-المالية-توا/
- Mon 23 Nov | أموال الغد | «الرقابة المالية» توافق على نشر إفصاح «إيديتا» لتخفيض رأس المال عبر إعدام أسهم خزينة
  https://amwalalghad.com/2026/11/23/الرقابة-المالية-توافق-على-نشر-إفصاح-4/
- Mon 23 Nov | جريدة الاستثمار العربى | «الرقابة المالية» توافق على تخفيض رأس مال «إيديتا» بنحو 2.2 مليون جنيه
  https://estsmararabe.com/الرقابة-المالية-توافق-على-تخفيض-رأس/
## AAPL  (8 leads)
- Wed 25 Nov | Trefis | Is Micron’s Record Margin Squeezing Apple And HP?
  https://www.trefis.com/stock/mu/articles/628762/is-micron-s-record-margin-squeezing-apple-and-hp/2026-11-25
  > Is Micron’s Record Margin Squeezing Apple And HP? Micron Technology makes the memory chips inside PCs, phones and servers. That margin hit 86.8% in the three months to Sep 3, 2026. It was 44.7% a year earlier, so it rose 42.1 points. It is the highest in our quarterly data back to March 2015.
- Wed 25 Nov | The Globe and Mail | Can Wearables & Mac Revenues Add Fresh Momentum to Apple Stock Ahead?
  https://www.theglobeandmail.com/investing/markets/stocks/AAPL-Q/pressreleases/8985755/can-wearables-mac-revenues-add-fresh-momentum-to-apple-stock-ahead/
  > Can Wearables & Mac Revenues Add Fresh Momentum to Apple Stock Ahead? Apple Inc.AAPL enters the holiday quarter with its Mac business gaining momentum, while its Wearables, Home and Accessories segment is leaning on a refreshed lineup to reverse a slowdown.
- Tue 24 Nov | Benzinga | Congressman Buys Apple Stock Again, How Dividend Reinvestments Add Up - Apple (NASDAQ:AAPL)
  https://www.benzinga.com/news/politics/26/11/63612652/congressman-buys-apple-stock-again-shows-off-power-of-dividend-reinvestments
  (page: did not load (403))
## MSFT  (8 leads)
- Wed 25 Nov | blockchain.news | Microsoft (MSFT) Stock Price Prediction: AI enthusiasm meets a fading short-term trend
  https://blockchain.news/news/20261125-price-prediction-msft-ai-enthusiasm-meets-a-fading-short
  > Price action is softer than the fundamentals Microsoft ended the session at $488.78, near the lower end of its 24-hour range of $502.52 to $487.61. The stock is trading below its 7-day SMA of $494.28, its 20-day SMA of $514.36 and its 50-day SMA of $524.25, which puts the short- to medium-term trend under pressure.
- Wed 25 Nov | Kalkine | Data#3 (ASX:DTL): What Record FY26 Sales Say About Microsoft, Security and Managed Services Demand
  https://kalkine.com.au/news/dividend-stocks/data3-asxdtl-what-record-fy26-sales-say-about-microsoft-security-and-managed-services-demand
  (page: did not load (403))
- Wed 25 Nov | Gotrade | Microsoft Stock (MSFT) Rises 0.7% to $496.13 (Nov 24)
  https://www.heygotrade.com/en/news/microsoft-msft-stock-news-november-25-2026/
  > AI-powered contentSome parts of this article are powered by AI. - Microsoft (MSFT) closed at $496.13 on November 24, 2026, up 0.74%, while the Nasdaq Composite fell 1.48%. - No source reviewed named a Microsoft-specific catalyst, and Yahoo Finance tied the day's tech weakness to a chip-led sell-off and rate-hike expectations.
## NVDA  (8 leads)
- Wed 25 Nov | Trefis | Buy, Sell Or Hold Nvidia Stock After A 31.5% Day?
  https://www.trefis.com/stock/nvda/articles/628686/buy-sell-or-hold-nvidia-stock-after-a-31-5-day/2026-11-25
  > Buy, Sell Or Hold Nvidia Stock After A 31.5% Day? Today’s big story: Anthropic Below Its IPO Price: Do Giants Come Back? Nvidia stock rose 31.5% on Monday, Nov 23, to $165.05. It was its second-biggest one-day gain since 2003. On Friday it had fallen 14.0%. On Tuesday, Nov 24, it fell 5.9% to $155.38.
- Wed 25 Nov | The Washington Post | See all of Trump’s Nvidia stock trades since January
  https://www.washingtonpost.com/politics/2026/11/24/see-all-trumps-nvidia-stock-trades-since-january/
  (page: did not load (TimeoutError))
- Wed 25 Nov | Reuters | COMMENTARY: Icarus stock Nvidia sends chill to US savers
  https://www.reuters.com/commentary/reuters-open-interest/icarus-stock-nvidia-sends-chill-us-savers-2026-11-25/
  (page: did not load (401))
- Wed 25 Nov | Yahoo Finance | Donald Trump Floats Jensen Huang Pardon, US Stake In Nvidia – But NVDA Loses Momentum
  https://finance.yahoo.com/markets/stocks/articles/donald-trump-floats-jensen-huang-052052146.html
  > - While analysts view Huang's return as largely positive for Nvidia and the broader AI trade, some say the AI chipmaker is not out of the woods yet. - Huang will appear before Congress committees for questioning on Dec.
- Wed 25 Nov | The Washington Post | Analysis | Trump’s Nvidia gambit shows the stock market is the economy
  https://www.washingtonpost.com/business/2026/11/24/maybe-market-is-economy-after-all/
- Wed 25 Nov | Yahoo Finance | COHR Stock Swings After Nvidia-Led AI Rally: $15M Insider Buy Draws Attention
  https://finance.yahoo.com/markets/stocks/articles/cohr-stock-swings-nvidia-led-044037567.html
- Wed 25 Nov | The Motley Fool | The Semiconductor ETF Kept Falling After Nvidia Raised Its Forecast. Time to Buy?
  https://www.fool.com/investing/2026/11/24/the-semiconductor-etf-kept-falling-after-nvidia-raised-its-forecast-time-to-buy/
- Wed 25 Nov | Benzinga | Dan Ives Raises Nvidia Price Target to $250 With Jensen Huang Back - NVIDIA (NASDAQ:NVDA)
  https://www.benzinga.com/markets/tech/26/11/63613403/dan-ives-nvidia-price-target-250-base-case-jensen-huang-back-china-loophole
## AMZN  (8 leads)
- Wed 25 Nov | Benzinga | Didn't Get Your Amazon Refund? You Could Get a Share of $309.5 Million, But There's a Catch
  https://www.benzinga.com/news/legal/26/11/63614829/amazon-refund-settlement-deadline
  (page: did not load (403))
- Wed 25 Nov | blockchain.news | Amazon (AMZN) Stock Price Prediction: Pullback tests support as analysts lean higher
  https://blockchain.news/news/20261125-price-prediction-amzn-pullback-tests-support-as-analysts-lean
  > What changed in AMZN shares Amazon (AMZN) is trading at $248.62 after a 3.58% 24-hour drop, with the session range extending from $258.25 down to $248.56. The move leaves AMZN below its 7-day, 20-day, 50-day, 200-day, 12-day EMA and 26-day EMA, which is a clean short-term weakness signal rather than a one-day noise move.
- Wed 25 Nov | Seeking Alpha | Amazon: The AI Boom Is Just Getting Started
  https://seekingalpha.com/article/4971730-amazon-stock-ai-boom-is-just-getting-started
  > - Amazon's AWS revenue surged 39.3% to $45.98 billion, marking six consecutive quarters of acceleration, while backlog reached $578 billion. - AWS operating margins expanded to 38.7%, generating $17.77 billion in operating income and approximately 63% of consolidated profits.
## GOOGL  (8 leads)
- Wed 25 Nov | blockchain.news | Alphabet (GOOGL) Stock Price Prediction: Oversold bounce risk meets a still-bearish trend
  https://blockchain.news/news/20261125-price-prediction-googl-oversold-bounce-risk-meets-a-still
  > What happened in the stock Alphabet (Google) (GOOGL) closed at $273.75, down 4.17% on the latest session, with the day’s range stretching from $286.37 down to $273.56. That leaves GOOGL stock just above immediate support at $269.42 and below the pivot at $277.89, with the short-term trend still under pressure. [Figures on the page: standalone; consolidated; one quarter. Check which one each figure is.]
- Wed 25 Nov | ad-hoc-news.de | Alphabet stock slips 0.82% to EUR 250.98 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/alphabet-stock-slips-0-82-to-eur-250-98-before-xetra/70552386
  > Alphabet's investor-relations calendar lists third-quarter 2026 results announced on October 28. On Xetra, the stock closed at EUR 253.05 on Tuesday, November 24, 2026. - Alphabet's investor-relations page lists third-quarter 2026 results announced on October 28. - The 2026 calendar also includes quarterly earnings releases and 10-Q filings.
- Wed 25 Nov | The Motley Fool | Alphabet Has $251 Billion Invested In 2 of Its Biggest Artificial Intelligence Partners
  https://www.fool.com/investing/2026/11/25/alphabet-has-251-billion-invested-in-2-of-its-biggest-artificial-intelligence-partners/
  > By Adam Levy – - Alphabet invests in start-ups through its venture funds, its Other Bets, and strategic investments. - Alphabet has significant exposure to both of them outside of its equity investments. Alphabet (GOOG -1.05%) (GOOGL -1.08%) has long invested in new technology and start-ups.
## META  (8 leads)
- Wed 25 Nov | Investing.com | Cathie Wood’s ARK sells Meta stock, buys Alphabet and Anthropic
  https://www.investing.com/news/company-news/cathie-woods-ark-sells-meta-stock-buys-alphabet-and-anthropic-93CH-5049488
  (page: did not load (403))
- Wed 25 Nov | BigGo Finance | Cathie Wood's ARK Pours $61.6M Into Anthropic as Shares Trade Below IPO Price, Trims Meta and Palantir
  https://finance.biggo.com/news/49a72169-f227-404b-8d78-92d1be614530
  > Cathie Wood's ARK Pours $61.6M Into Anthropic as Shares Trade Below IPO Price, Trims Meta and Palantir Cathie Wood's ARK Invest bought roughly $61.6 million of Anthropic PBC (NASDAQ:ANT) stock on Tuesday, adding to the Claude developer even as its shares slipped beneath the $83 offer price set in its Nov. 19 initial public offering.
- Wed 25 Nov | bloomingbit | Meta’s Threads Adds Real-Time Crypto, US Stock Quotes in Broader Rivalry With X
  https://en.bloomingbit.io/feed/news/125178
  > - Meta’s Threads said it will introduce a real-time quote feature for cryptocurrencies and US stocks. - Threads said it is rolling out a cashtag feature that lets users check live price data for cryptocurrencies and stocks listed on the NYSE and Nasdaq.
## TSLA  (8 leads)
- Wed 25 Nov | AFR | SpaceX-Tesla: Robyn Denholm tapped to negotiate biggest merger ever
  https://www.afr.com/world/north-america/spacex-tesla-the-directors-negotiating-the-biggest-merger-ever-20261125-p61h5i
  > SpaceX and Tesla have entrusted five directors with the fate of the largest merger in history, with the quintet hashing out the terms of a potential $US3.5 trillion ($5.3 million) combination and racing to complete the deal before the end of the year.
- Wed 25 Nov | Gotrade | Tesla Stock (TSLA) Falls 0.2% to $384.68 (Nov 24)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-25-2026/
  > AI-powered contentSome parts of this article are powered by AI. - Tesla (TSLA) closed at $384.68 on November 24, 2026, down 0.20%, while the Nasdaq Composite fell 1.48%.
- Wed 25 Nov | Gotrade | SpaceX Stock (SPCX) Falls 5.7% on Reports of a Tesla Merger (Nov 24)
  https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-25-2026/
  > AI-powered contentSome parts of this article are powered by AI. - SpaceX (SPCX) fell 5.65% to $125.81 on Tuesday, November 24, 2026, 4.17 percentage points worse than the Nasdaq Composite.
## JPM  (8 leads)
- Wed 25 Nov | MarketBeat | JPMorgan Chase & Co. (NYSE:JPM) Shares Unloaded by Rep. Harriet M. Hageman
  https://www.marketbeat.com/instant-alerts/congress-jpmorgan-chase-co-nyse-jpm-shares-unloaded-by-rep-harriet-m-hageman-2026-11-25/
  > JPMorgan Chase & Co. (NYSE:JPM) Shares Unloaded by Rep. Harriet Hageman disclosed selling $1,001–$15,000 of JPMorgan shares on August 27 from an IRA account; the disclosure was filed November 23.
- Wed 25 Nov | MarketBeat | JPMorgan Chase & Co. (NYSE:JPM) Stock Sale Revealed by Rep. Harriet M. Hageman
  https://www.marketbeat.com/instant-alerts/congress-jpmorgan-chase-co-nyse-jpm-stock-sale-revealed-by-rep-harriet-m-hageman-2026-11-25/
  (same wording as the MarketBeat story above: one source, not two)
- Wed 25 Nov | Kalkine Media | Southwest Gas Initiates $340 Million ATM Equity Offering with JPMorgan and Wells Fargo
  https://kalkinemedia.com/us/news/announcements/southwest-gas-initiates-340-million-atm-equity-offering-with-jpmorgan-and-wells-fargo
  > On November 24, 2026, Southwest Gas Holdings, Inc. disclosed via a Form 8-K filing with the SEC that it has entered into at-the-market (ATM) sales agreements with J.P. The agreements authorize the offer and sale of common stock totaling up to $340,000,000.
## XOM  (8 leads)
- Wed 25 Nov | MarketBeat | ExxonMobil (NYSE:XOM) Stock Sale Revealed by Rep. Harriet M. Hageman
  https://www.marketbeat.com/instant-alerts/congress-exxonmobil-nyse-xom-stock-sale-revealed-by-rep-harriet-m-hageman-2026-11-25/
  > ExxonMobil (NYSE:XOM) Stock Sale Revealed by Rep. Hageman disclosed selling $1,001–$15,000 of ExxonMobil shares on October 14 from an RBC Wealth Management IRA; the sale was reported November 23. - ExxonMobil beat quarterly earnings and revenue expectations, reporting EPS of $4.23 and revenue of $110.5 billion.
- Wed 25 Nov | BBJ - Budapest Business Journal | ExxonMobil Hungary: Connecting Global Expertise With Local Impact
  https://bbj.hu/business/people/interview/exxonmobil-hungary-connecting-global-expertise-with-local-impact/
  > ExxonMobil Hungary’s role increasingly extends beyond traditional support activities to responsibilities with regional and global reach. BBJ: What are the main operational dependencies between Budapest and ExxonMobil’s other locations, and how do you prevent handovers from slowing delivery?
- Tue 24 Nov | Demerara Waves Online News- Guyana | Exxon Mobil hopes international community will tame Venezuela over ICJ ruling
  https://demerarawaves.com/2026/11/24/exxon-mobil-hopes-international-community-will-tame-venezuela-over-icj-ruling/
  > Last Updated on Tuesday, 24 November 2026, 18:28 by .
## AVGO  (8 leads)
- Wed 25 Nov | Blockchain News | Broadcom (AVGO) Stock Price Prediction: Pressure at support after a sharp drawdown, while analysts still see room to recover
  https://blockchain.news/news/20261125-price-prediction-avgo-pressure-at-support-after-a-sharp
  > What changed in the tape Broadcom (AVGO) is under pressure, with the share price at $292.21 after a 6.41% 24-hour decline. That leaves AVGO below its 7-day, 20-day, 50-day and 200-day moving averages, a bearish alignment that confirms the stock is still trading in a downtrend rather than a clean rebound.
- Wed 25 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Sale Reported by Rep. Harriet M. Hageman
  https://www.marketbeat.com/instant-alerts/congress-broadcom-nasdaq-avgo-stock-sale-reported-by-rep-harriet-m-hageman-2026-11-25/
  > Broadcom (NASDAQ:AVGO) Stock Sale Reported by Rep. Harriet Hageman disclosed selling $1,001–$15,000 of Broadcom shares on September 16 from an IRA account; the filing was reported November 23. - Broadcom’s latest quarter beat analyst estimates, reporting EPS of $3.32 versus $3.22 expected and revenue of $29.59 billion, up 85.5% year over year.
- Wed 25 Nov | JournalArta | Broadcom stock slides 4% to $301.08 as chip selloff deepens, pushing it into a bear market
  https://journalarta.com/en/2026/11/25/broadcom-stock-slides-4-to-301-08-as-chip-selloff-deepens-pushing-it-into-a-bear-market/
  > Broadcom stock slides 4% to $301.08 as chip selloff deepens, pushing it into a bear market Broadcom shares closed at $301.08 on Tuesday, down 3.98%, as chip stocks sold off. The stock is now more than 37% below its June high and 3.3% above its November low.
- Wed 25 Nov | FourWeekMBA | Broadcom’s IPO Sold Shares at $15; $1,000 Is Now Worth $201K
  https://fourweekmba.com/ai-broadcoms-ipo-sold-shares-at-15-1000-is-now-worth-201k/
  (page: did not load (403))
- Tue 24 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Price Down 4% - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-stock-price-down-4-should-you-sell-2026-11-24/
- Tue 24 Nov | Yahoo Finance | Broadcom Stock Could Have 70% Upside, Analysts Say. What AVGO’s Valuation Reveals.
  https://finance.yahoo.com/markets/stocks/articles/broadcom-stock-could-70-upside-201017926.html
- Tue 24 Nov | FourWeekMBA | Broadcom Paid VMware in Stock; It’s Worth 5.5x the Cash Now
  https://fourweekmba.com/ai-broadcom-paid-vmware-in-stock-its-worth-5-5x-the-cash-now/
- Tue 24 Nov | Yahoo Finance | Nvidia, AMD, Broadcom lead chip stocks lower as AI trade comes under pressure
  https://finance.yahoo.com/markets/article/nvidia-amd-broadcom-lead-chip-stocks-lower-as-ai-trade-comes-under-pressure-141635463.html
## BRK.B  (8 leads)
- Wed 25 Nov | Coinbase | Berkshire Hathaway Price, BRK.BC Price, Live Charts, and Marketcap - Coinbase Australia
  https://www.coinbase.com/en-au/price/berkshire-hathaway-inc-class-b-base-0xb20000000000000000000024170488e788cbbcb4
  > Berkshire Hathaway is only tradable on decentralized exchanges (DEXs). Class B (Coinbase Tokenized Stock) is an onchain certificate that provides economic exposure to shares of Berkshire Hathaway Inc. Each token initially represents a 1:1 beneficial interest in shares held in a segregated custody account with a regulated broker-dealer and custodian.
- Wed 25 Nov | Barron's | Berkshire’s Third-Quarter Stock Moves Due Today. It Could Have Sold Bank of America.
  https://www.barrons.com/articles/berkshire-hathaway-bank-of-america-stock-806558be
  (page: did not load (401))
- Wed 25 Nov | Business NH Magazine | NH's Top Women-Led Businesses 2026: (#11) Berkshire Hathaway HomeServices Verani Realty
  https://www.businessnhmagazine.com/article/nhs-top-women-led-businesses-2026-11-berkshire-hathaway-homeservices-verani-realty
  > (#11) Inspiring Women-Led Businesses: Berkshire Hathaway HomeServices Verani Realty Margherita Verani’s story of real estate success begins not in Londonderry where her family’s business, Berkshire Hathaway HomeServices Verani Realty, is headquartered, but rather in Italy. Margherita, originally a social worker, joined the business full time in 1979.
## WMT  (8 leads)
- Wed 25 Nov | MarketBeat | Rep. Harriet M. Hageman Sells Shares of Walmart Inc. (NASDAQ:WMT)
  https://www.marketbeat.com/instant-alerts/congress-rep-harriet-m-hageman-sells-shares-of-walmart-inc-nasdaq-wmt-2026-11-25/
  > Hageman Sells Shares of Walmart Inc. Hageman disclosed selling $1,001–$15,000 in Walmart shares on August 27 from an RBC Wealth Management IRA account. - Walmart’s latest quarter beat analyst estimates, with EPS of $0.65 and revenue of $188.84 billion; revenue rose 5.2% year over year.
- Wed 25 Nov | Mashable | Black Friday PS5 and PS5 Pro deals: See the best deals at Amazon, Best Buy, Target, and Walmart
  https://mashable.com/tech/best-black-friday-ps5-deals-2026
  > If you are trying to get your hands on a PlayStation 5 right now, the real win is not a discount — it is simply finding one in stock at standard retail price.
- Wed 25 Nov | Pluang | Walmart adds $7B to Symbotic backlog, boosting automation growth and fiscal 2026 profits.
  https://pluang.com/en/news-feed/symbotic-3-poin-penting-investor-jangka-panjang-kontrak-walmart-diperluas
  (page: did not load (403))
- Wed 25 Nov | JournalArta | Walmart stock gains 2.1% to $132.31 as discount retailers rally after Dollar Tree results
  https://journalarta.com/en/2026/11/25/walmart-stock-gains-2-1-to-132-31-as-discount-retailers-rally-after-dollar-tree-results/
  > Walmart stock gains 2.1% to $132.31 as discount retailers rally after Dollar Tree results Walmart shares closed Tuesday at $132.31, a third straight gain, as discounters rose on Dollar Tree's raised outlook while the S&P 500 slipped.
- Wed 25 Nov | Simply Wall St | Why Did The Walmart (WMT) President Sell Shares?
  https://simplywall.st/stocks/us/consumer-retailing/nasdaq-wmt/walmart/news/why-did-the-walmart-wmt-president-sell-shares
- Wed 25 Nov | Scripps News | Walmart shoppers stock up on water, propane amid recent disruptions
  https://www.scrippsnews.com/us-news/walmart-shoppers-stock-up-on-water-propane-amid-recent-disruptions
- Tue 24 Nov | 아시아경제 | Strategic Price Cuts Amid Inflation... "Walmart Posts Solid Growth Despite Headwinds" [Click e-Stock]
  https://www.asiae.co.kr/en/article/stock-disclosure/2026112416523531423
- Tue 24 Nov | MarketBeat | Walmart (NASDAQ:WMT) Stock Price Up 2.1% Following Analyst Upgrade
  https://www.marketbeat.com/instant-alerts/price-walmart-nasdaq-wmt-stock-price-up-21-following-analyst-upgrade-2026-11-24/
## V  (8 leads)
- Wed 25 Nov | Fintech Singapore | Visa Approves US$50 Million Stock Award to Retain CEO Ryan McInerney
  https://fintechnews.sg/142320/payments/visa-ceo-ryan-mcinerney-stock-award/
  > Visa has approved a performance-based stock option award worth approximately US$50 million for CEO Ryan McInerney covering nearly 379,000 shares. The board’s compensation committee authorised the grant on 18 November 2026, according to a filing with the US Securities and Exchange Commission (SEC).
- Tue 24 Nov | MarketBeat | Visa (NYSE:V) Shares Climb 1.6% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-visa-nyse-v-shares-climb-16-heres-what-happened-2026-11-24/
  > Visa (NYSE:V) Shares Climb 1.6% - Here's What Happened - Visa shares rose 1.6% to $415.92, while trading volume was 17% below its average. - Visa beat quarterly earnings and revenue estimates, with revenue up 13.2% year over year, and raised its quarterly dividend from $0.67 to $0.78 per share.
- Tue 24 Nov | The Globe and Mail | Visa Approves Performance Stock Award for CEO
  https://www.theglobeandmail.com/investing/markets/stocks/V/pressreleases/8992945/visa-approves-performance-stock-award-for-ceo/
  > Visa ( (V) ) has shared an update. Visa Inc.’s Compensation Committee approved on November 18, 2026, a performance stock option for CEO Ryan McInerney covering 378,940 Class A common shares, with an approximately $50 million grant-date value, a 10-year term and an exercise price equal to the stock’s closing price that day.
## ORCL  (8 leads)
- Wed 25 Nov | Blockchain News | Oracle (ORCL) Stock Price Prediction: Momentum stays pressured as ORCL trades below key averages
  https://blockchain.news/news/20261125-price-prediction-orcl-momentum-stays-pressured-as-orcl-trades
  > What the tape is saying Oracle (ORCL) closed its latest 24-hour stretch at $105.56, down 7.51%, after trading in a $114.37 to $105.36 range.
- Wed 25 Nov | Trefis | Oracle Spends $28.5 Billion A Quarter Building. Who Covers The Wait?
  https://www.trefis.com/stock/orcl/articles/628215/oracle-spends-28-5-billion-a-quarter-building-who-covers-the-wait/2026-11-25
  > Oracle Spends $28.5 Billion A Quarter Building. Who Covers The Wait? Oracle‘s stock closed Tuesday 67% below its peak. For Oracle, that gap is the whole story. Today’s big story asks whether Oracle should keep building or take a breather. How Long Is Oracle’s Wait?
- Wed 25 Nov | NewsBytes | Oracle's Larry Ellison loses $11 billion in a day
  https://www.newsbytesapp.com/news/business/oracle-s-larry-ellison-loses-11-billion-in-a-day/story
  (page: did not load (403))
- Wed 25 Nov | MarketBeat | Rep. Harriet M. Hageman Sells Shares of Oracle Corporation (NYSE:ORCL)
  https://www.marketbeat.com/instant-alerts/congress-rep-harriet-m-hageman-sells-shares-of-oracle-corporation-nyse-orcl-2026-11-25/
  > Hageman Sells Shares of Oracle Corporation (NYSE:ORCL) Hageman disclosed selling $1,001–$15,000 of Oracle shares on September 16 from an RBC Wealth Management IRA account; the disclosure was filed November 23. - Oracle reported quarterly earnings of $1.92 per share and revenue of $19.34 billion, beating analyst estimates; revenue rose 29.6% year over year.
- Wed 25 Nov | FinanceFeeds | Oracle Stock $109.50: AI Selloff Undoes a Third of Rebound
  https://financefeeds.com/oracle-orcl-stock-109-wednesday-ai-selloff-undoes-third-of-rebound-bull-119-bear-100/
- Wed 25 Nov | JournalArta | Oracle share price closes at $109.50 after technology selloff
  https://journalarta.com/en/2026/11/25/oracle-shares-slide-to-109-50-as-technology-stocks-fall/
- Wed 25 Nov | Wisevoter | Ellison Loses $10.9 Billion as Oracle Shares Fall
  https://wisevoter.com/world/us/2026/11/25/ellison-loses-10-9-billion-oracle-shares-fall
- Wed 25 Nov | TIKR.com | Not Good: Oracle’s Credit Swaps Blow Out Again a Day After Huang’s Return Lifted Nvidia
  https://www.tikr.com/blog/not-good-oracles-credit-swaps-blow-out-again-a-day-after-huangs-return-lifted-nvidia
## COST  (8 leads)
- Wed 25 Nov | MarketBeat | Costco Wholesale Corporation (NASDAQ:COST) Stock Has Average Target Price of $1,098.88
  https://www.marketbeat.com/instant-alerts/consensus-costco-wholesale-corporation-nasdaq-cost-stock-has-average-target-price-of-109888-2026-11-25/
  > Costco Wholesale Corporation (NASDAQ:COST) Stock Has Average Target Price of $1,098.88 - Analysts remain broadly positive on Costco: 35 brokerages give it a consensus “Moderate Buy” rating, with an average 12-month price target of $1,098.88.
- Wed 25 Nov | The Globe and Mail | Costco Hasn't Split Its Stock Since 2000. Here's Why 2027 Could Be the Year.
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8996896/costco-hasnt-split-its-stock-since-2000-heres-why-2027-could-be-the-year/
  > - Costco's last stock split occurred when shares were at a record high and business performance was strong. - Management has said there's no current plan for a split. - Long-term investors should focus on Costco's high-quality operations rather than split speculation. Missed AI’s "Act 1"? Act 2 Could Be 15x Bigger.
- Wed 25 Nov | Pluang | Costco may consider a stock split in 2027 amid record prices and strong growth.
  https://pluang.com/en/news-feed/alasan-costco-bisa-lakukan-stock-split-2027
  (page: did not load (403))
## NFLX  (8 leads)
- Wed 25 Nov | JournalArta | Netflix stock price rises to $58.87 after Radford Studio deal
  https://journalarta.com/en/2026/11/25/netflix-shares-rise-to-58-87-after-studio-deal-remain-near-yearly-low/
  > Netflix shares rise to $58.87 after studio deal, remain near yearly low Netflix shares rose for a second straight session to $58.87 after the company announced a deal to buy Radford Studio Center, though the stock remained close to its one-year low.
- Wed 25 Nov | Yahoo Finance | What Could Netflix (NFLX) Gain From Owning The Radford Studio Center?
  https://finance.yahoo.com/media-advertising/articles/could-netflix-nflx-gain-owning-042601498.html
  > - Netflix (NasdaqGS:NFLX) is in advanced talks to acquire the Radford Studio Center in Los Angeles, according to recent reports. - The Radford Studio Center is a long established Hollywood production lot that currently hosts multiple television and film projects.
- Wed 25 Nov | Benzinga | Cathie Wood Buys $62M in Anthropic Stock as Shares Slip Below IPO Price; Ark Sells Meta, Netflix and Pala
  https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/11/63613295/cathie-wood-buys-62m-in-anthropic-stock-as-shares-slip-below-ipo-price-ark-sells-meta-netflix-and-palantir
  (page: did not load (403))
## INTC  (8 leads)
- Wed 25 Nov | Blockchain News | Intel (INTC) Stock Price Prediction: Broken momentum meets still-supportive analyst targets after the post-earnings reset
  https://blockchain.news/news/20261125-price-prediction-intc-broken-momentum-meets-still-supportive-analyst
  > What happened and why it matters Intel’s latest move is defined by a clean break lower rather than a slow drift. INTC shares closed the latest 24-hour window at $53.29, down 8.17%, with price trading between $58.09 and $52.60 and volume described as a low-volume pullback at 0.17x of the five-day average.
- Wed 25 Nov | Around Prague | Dell's Weak PC Signal Lands as Intel and Chip Stocks Pull Back
  https://aroundprague.cz/en/news/us/dell-s-weak-pc-signal-lands-as-intel-and-chip-stocks-pull-back
  (page: did not load (403))
- Wed 25 Nov | www.marketscreener.com | Aeeris Limited has Changed its Name to Blue Horizon Intel Ltd
  https://www.marketscreener.com/news/aeeris-limited-has-changed-its-name-to-blue-horizon-intel-ltd-ce7851dbde81f720
  (page: did not load (403))
- Wed 25 Nov | Investing.com Canada | Form 4 Intel Corporation For: 25 November By Investing.com
  https://ca.investing.com/news/stock-market-news/form-4-intel-corporation-for-25-november-93CH-4979949
  (page: did not load (403))
- Wed 25 Nov | Gotrade | Intel Stock (INTC) Falls 8.1% as Chip Stocks Retreat (Nov 24)
  https://www.heygotrade.com/en/news/intel-intc-stock-news-november-25-2026/
- Wed 25 Nov | Simply Wall St | Intel (INTC) Backs New Push To Extend CHIPS Incentives And Counter China
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-intc-backs-new-push-to-extend-chips-incentives-and-cou
- Tue 24 Nov | Yahoo Finance | Why Intel Stock Fell Today
  https://finance.yahoo.com/markets/stocks/articles/why-intel-stock-fell-today-231601168.html
- Tue 24 Nov | FXLeaders | Intel Stock INTC Eyes $85 after Avoiding the AI Crash as $50 Support and First 18A Customer Boosts Recovery Hopes
  https://www.fxleaders.com/news/2026/11/24/intel-stock-intc-eyes-85-after-avoiding-the-ai-crash-as-50-support-and-first-18a-customer-boosts-recovery-hopes/
## LLY  (8 leads)
- Wed 25 Nov | NAI500 | Revenue Performance Stands Out as Eli Lilly’s Third-Quarter Revenue Reaches a Stage Peak
  https://nai500.com/blog/2026/11/revenue-performance-stands-out-as-eli-lillys-third-quarter-revenue-reaches-a-stage-peak/
  > Eli Lilly (LLY) primarily researches, develops, and produces treatments for diabetes, obesity, and cancer for a broad patient population. The company has recently achieved multiple business milestones. On August 28, its product Mounjaro received approval for reducing cardiovascular risk. On November 12, the company began construction of an active pharmaceutical ingredient manufacturing base in Pennsylvania.
- Tue 24 Nov | GuruFocus | Eli Lilly and Co (LLY) Stock Up 3.1% and Still Undervalued -- GF Score: 98/100
  https://www.gurufocus.com/news/9218487/eli-lilly-and-co-lly-stock-up-31-and-still-undervalued-gf-score-98100
  (page: did not load (403))
- Tue 24 Nov | Wisevoter | Eli Lilly Buys LoQus23 for Up to $725 Million
  https://wisevoter.com/world/2026/11/24/eli-lilly-acquires-loqus23-huntingtons-candidate
  > Eli Lilly Buys LoQus23 for Up to $725 Million The Huntington's-focused preclinical biotech will join Lilly's portfolio, with payments tied to development and regulatory milestones. 24, 2026 in Biotech Eli Lilly has agreed to acquire LoQus23 Therapeutics for up to $725 million in cash, including an upfront payment and later milestone payments.
- Tue 24 Nov | BigGo Finance | Moody's Lifts Eli Lilly to Aa2 as Obesity Drug Demand Outpaces Novo Nordisk's Sales Momentum
  https://finance.biggo.com/news/685c9f61-b9d8-4ef7-9746-5eec8fe868f4
  > Moody's Lifts Eli Lilly to Aa2 as Obesity Drug Demand Outpaces Novo Nordisk's Sales Momentum Moody's Ratings raised Eli Lilly and Company's (LLY) senior unsecured notes and issuer ratings to Aa2 from Aa3 on Tuesday, pointing to the earnings power of its metabolic drug franchise.
- Tue 24 Nov | Pluang | Eli Lilly's revenue consistently outpaced Novo Nordisk's over eight quarters, showing steady growth.
  https://pluang.com/en/news-feed/eli-lilly-vs-novo-nordisk-tren-penjualan-glp-1
- Tue 24 Nov | Simply Wall St | Eli Lilly (LLY) Stock May Be 22% Undervalued Following Neuroscience Deal
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-stock-may-be-22-undervalued-following-neurosci
- Tue 24 Nov | Moomoo | Eli Lilly and Co(LLY) Stock Price Today | Quotes & News
  https://www.moomoo.com/stock/LLY-US?chain_id=Name1K9-3FXPhg.1lgbr60&global_content={"promote_id":"","sub_promote_id":64,"subpromote_id":"","f":"www.moomoo.com/community/profile/75934617/post/all"}
- Tue 24 Nov | Investing.com | Eli Lilly earns Moody’s upgrade to Aa2 as obesity drug demand fuels earnings
  https://www.investing.com/news/stock-market-news/eli-lilly-earns-moodys-upgrade-to-aa2-as-obesity-drug-demand-fuels-earnings-5048935
Read 86 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ETEL, CLHO, ALCN, EAST, AMOC.
