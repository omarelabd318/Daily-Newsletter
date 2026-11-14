# Desk brief, Saturday, November 14, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 293s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-13 (19.3); Treasury yields to 2026-11-13 (10-year 5.15%).
- **valuation**: ok in 23s (GitHub Actions). LLY: $1.36tn, P/E (last 12 months) 45.2, Forecast P/E (fiscal 2026) 40.5 (the four quarters to Sep 2026)
- **movers**: ok in 20s (GitHub Actions). Market values: 18 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 53.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 50 stocks, k 16.5%, median P/E 10.8; cheapest MASR +71%, PHAR +51%, EXPA +49%; dearest ARAB -61%, MOIN -66%, BTFH -68%
- **views**: ok in 0s (GitHub Actions). 2026-10-31-chips: on track -> right  (Judged on its date: Nvidia at 162.85 from 204.64 (-20.4%).)
- **results**: ok in 60s (GitHub Actions). 
- **news**: ok in 134s (GitHub Actions). 
- **leads**: ok in 107s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

## What moved (latest close against the one before)
- EGX30 52,023.37 (-0.91%); EGX70 EWI 18,527.43 (+0.43%); USD/EGP 53.50 (-0.22%); Gold 21K 5,970.00 (+0.34%); Brent 95.84 (-0.06%); S&P 500 7,561.67 (-0.40%); Nasdaq 25,136.27 (-0.91%); Bitcoin 67,137.00 (-2.71%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): AVGO -4.8%, EAST +4.2%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 81, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (14.4% over) and its 200-day (13.4% over), though the 50-day is still below the 200-day; RSI 76, stretched after a run: above 70.
    - NVDA: Turning down: below both its 50-day average (24.1% under) and its 200-day (20.2% under), though the 50-day is still above the 200-day; RSI 25, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- EGX INEG (Integrated Engineering Group) -6.3%; US NU (Nu Holdings) +11.8%; US CBRS (Cerebras Systems) +11.2%; US MOG.B (Moog) +6.7%; US ALNY (Alnylam Pharmaceuticals) +5.4%; US U (Unity Software) +5.2%; US NBIS (Nebius Group) -9.9%; US AMD (Advanced Micro Devices) -8.8%; US FN (Fabrinet) -7.3%; US DELL (Dell Technologies) -7.2%; US TSEM (Tower Semiconductor) -6.9%

Leads for them (open before using; never guess a reason):
```
EGX: failed (HTTP Error 401: Unauthorized); kept the saved session
EGX week and month: EGX stocks trading at least EGP 1m a day on average (210)
US: 2026-11-13, 847 companies
US week and month: US companies worth $10bn or more (846)
EGX30 heatmap: 2026-11-12, 31 members
US heatmap: 2026-11-13, 100 members
Market values: 18 of 39 updated

# EGX 2026-11-12
## INFI +17.5%  Foodico
- Thu 12 Nov | عالم المال | أخبار البورصة المصرية اليوم.. «فوديكو» تتصدر الرابحين و«العامة للصيني» الأكثر تراجعًا
  https://alamalmal.net/article/943162/أخبار-البورصة-المصرية-اليوم-«فوديكو»-تتصدر-الرابحين
- Thu 12 Nov | Traders Union | البورصة المصرية تشهد صعود فوديكو 17.52% وتراجع الخزف والصيني 6%
  https://tradersunion.com/ar/news/stocks/show/4216492-egypt-stock-vodico-ceramics-move/
- Thu 12 Nov | معلومات مباشر | تم ايقاف الورقة المالية - EGS01041C010 - الاسماعيلية الوطنية للصناعات الغذائية (فوديكو) لمدة 10 دقائق لتجاوزها نسبة 10 %
  https://www.mubasher.info/news/4701441/تم-ايقاف-الورقة-المالية-EGS01041C010-الاسماعيلية-الوطنية-للصناعات-الغذائية-فوديكو-لمدة-10-دقائق-لتجاوزها-نسبة-10-/
## ATLC +8.7%  AT Lease
- no headlines found
## DTPP +8.0%  Delta for Printing & Packaging
- Thu 12 Nov | شبكة تواصل الإخبارية | “دلتا للطباعة” تضاعف أرباحها إلى 147.6 مليون جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7575434/
- Thu 12 Nov | أموال الغد | أرباح دلتا للطباعة والتغليف تقفز 137% إلى 147.6 مليون جنيه خلال 9 أشهر
  https://amwalalghad.com/2026/11/12/أرباح-دلتا-للطباعة-والتغليف-تقفز-137-إلى-147/
- Thu 12 Nov | أموال الغد | أرباح دلتا للطباعة والتغليف تقفز 137.1% إلى 147.6 مليون جنيه خلال 9 أشهر
  https://amwalalghad.com/2026/11/12/أرباح-دلتا-للطباعة-والتغليف-تقفز-137-1-إلى-14/
- Thu 12 Nov | جريدة المال | أرباح دلتا للطباعة والتغليف تقفز 137.1% إلى 147.6 مليون جنيه خلال 9 أشهر
  https://almalnews.com/2146793/أرباح-دلتا-للطباعة-والتغليف-تقفز-137-1/
## ROTO +5.9%  Al Rowad
- Sat 14 Nov | صحيفة الحقيقة الإلكترونية | جمعية الرواد الشبابية بجازان تحتفي بتأهيل 522 شابًا وشابة عبر مشروع "مهارات المستقبل"
  https://alhqyq.com/news/s/28646
- Sat 14 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | التصنيع تكمل بيع حصصها في الرواد التحويلية بقيمة 684 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1933098
- Fri 13 Nov | صحيفة الحدث | جمعية الرواد الشبابية بجازان تحتفي بتخريج 522شابًا وفتاة ضمن مشروع "مهارات المستقبل"
  https://al-hadath.com/local-news/102684/جمعية-الرواد-الشبابية-بجازان-تحتفي-بتخريج-522شابًا-وفتاة-ضمن-مشروع-مهارات-المستقبل
- Fri 13 Nov | alraynews.net | جمعية الرواد الشبابية بجازان تحتفي بتخريج 522 شابًا وفتاة ضمن مشروع «مهارات المستقبل»
  https://alraynews.net/6762050.htm
## HDBK +5.8%  Housing & Development Bank
- Sat 14 Nov | https://www.youlyou.com/ | كم يبلغ عائد المليون جنيه في حساب توفير EDGE من بنك التعمير والإسكان؟
  https://www.youlyou.com/93803
- Fri 13 Nov | بنكي | بنك التعمير والإسكان يؤكد أهمية تكامل الرقمنة والتمويل لدعم النمو بمؤتمر «الناس والبنوك»
  https://www.bankygate.com/202507
- Fri 13 Nov | شبكة تواصل الإخبارية | بنك التعمير والإسكان يتيح ربط الشهادات الادخارية أونلاين عبر تطبيق HDB Mobile
  https://twaslnews1.twaslnews.com/7625065/
- Fri 13 Nov | https://ekhbary24.com/ | البنك الأهلي وبنك مصر يرفعان عائد الشهادات إلى 18.85% الأحد
  https://ekhbary24.com/article/51830
## INEG -6.3%  Integrated Engineering Group
- no headlines found
## PRCL -6.0%  Sheeni
- no headlines found
## CCRS -5.0%  Gulf Canadian Real Estate Investment
- no headlines found
## BIOC -4.3%  Glaxo Smith Kline
- Thu 12 Nov | جريدة المال | «جلاكسو سميثكلاين» تدعو جمعيتها غير العادية للانعقاد 6 ديسمبر للنظر في الاندماج مع «أمون للأدوية»
  https://almalnews.com/2146951/«جلاكسو-سميثكلاين»-تدعو-جمعيتها-غير-العادية-للانعقاد/
- Thu 12 Nov | شبكة تواصل الإخبارية | 6 ديسمبر.. عمومية “جلاكسو سميثكلاين” تبحث زيادة رأس المال للاندماج مع “أمون”
  https://twaslnews1.twaslnews.com/7581920/
- Thu 12 Nov | Traders Union | جلاكسو سميثكلاين تدعو عمومية 6 ديسمبر لمناقشة اندماج أمون في مصر
  https://tradersunion.com/ar/news/companies/show/4212568-gsk-amoun-merger-egypt-meeting/
- Thu 12 Nov | معلومات مباشر | 6 ديسمبر.. عمومية جلاكسو سميثكلاين تناقش الاندماج مع أمون
  https://www.mubasher.info/news/4701529/6-ديسمبر-عمومية-جلاكسو-سميثكلاين-تناقش-الاندماج-مع-أمون/
## COPR -3.3%  Copper For Commercial Investment
- no headlines found

# US 2026-11-13
## NU +11.8%  Nu Holdings
- Sat 14 Nov | Yahoo Finance | Nu Holdings (NU) is Surging by Double Digits. Here’s What’s Driving the Rally
  https://finance.yahoo.com/markets/stocks/articles/nu-holdings-nu-surging-double-045349151.html
  > (NYSE:NU) is one of the 10 Stocks Defying Tech Market Turmoil. Nu Holdings grew its share price by 11.75 percent on Friday to close at $13.22 apiece after reporting strong earnings performance in the third quarter of the year, thanks to solid net interest income across its global businesses.
- Sat 14 Nov | qz.com | Nu Holdings posts $1.09 billion quarterly profit, shares rise
  https://qz.com/nu-holdings-third-quarter-net-income-efficiency-outlook-111326
  > Nubank parent Nu Holdings reported third-quarter net income of $1.09 billion on Nov. 12, a 31% increase from a year earlier on a currency-neutral basis and in line with analyst estimates, according to Reuters.
- Fri 13 Nov | Simply Wall St | Nu (NU) Stock Jumps As Q3 Earnings Strengthen Profit Case Amid Credit Risk
  https://simplywall.st/stocks/us/banks/nyse-nu/nu-holdings/news/nu-nu-stock-jumps-as-q3-earnings-strengthen-profit-case-amid
  > Nu Holdings came into this Q3 2026 report with a mixed tape. The stock was down double digits over the past month, yet it ripped 11.8% higher today to close at US$13.22.
- Fri 13 Nov | Yahoo Finance | Stock Market Today, Nov. 13: Nu Holdings Surges on Record Q3 Earnings Beat Driven by Strong Revenue
  https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nov-13-221302620.html
  > Nu Holdings (NYSE:NU), a Latin American digital bank and consumer finance platform, closed at $13.21, up 11.71%. Premarket earnings beat forecasts and management commentary on Mexico and Colombia kept investors watching growth and efficiency next.
## CBRS +11.2%  Cerebras Systems
- Sat 14 Nov | Yahoo Finance | Cerebras Systems (CBRS) Rockets Higher as These 2 Catalysts Emerge
  https://finance.yahoo.com/markets/stocks/articles/cerebras-systems-cbrs-rockets-higher-044957586.html
  > (NASDAQ:CBRS) is one of the 10 Stocks Defying Tech Market Turmoil. Cerebras Systems saw its share prices jump by 11.22 percent on Friday to finish at $108.72 apiece, as investor sentiment was bolstered by its higher growth outlook for full-year 2026 and a record-breaking revenue from cloud and other services.
- Sat 14 Nov | Investing.com Nigeria | Craig-Hallum cuts Cerebras Systems stock price target on lower market multiples
  https://ng.investing.com/news/stock-market-news/craighallum-cuts-cerebras-systems-stock-price-target-on-lower-market-multiples-93CH-2806775
  (page: did not load (403))
- Sat 14 Nov | Simply Wall St | Cerebras Systems (CBRS) Stock Jumps As Q3 Results Fuel Growth Conviction
  https://simplywall.st/stocks/us/semiconductors/nasdaq-cbrs/cerebras-systems/news/cerebras-systems-cbrs-stock-jumps-as-q3-results-fuel-growth/amp
  > Cerebras Systems released its Q3 2026 report and the stock rose 11.2% in the first full trading session to US$108.72. This is a significant move for a business that is still losing money, which indicates that the reaction was driven by belief in the growth story.
- Fri 13 Nov | Simply Wall St | Has Cerebras Systems (CBRS) Fallen Enough To Shrink Its Sales Premium?
  https://simplywall.st/stocks/us/semiconductors/nasdaq-cbrs/cerebras-systems/news/has-cerebras-systems-cbrs-fallen-enough-to-shrink-its-sales
  > Cerebras Systems shares have had a rough spell in 2026, and the slide so far this year raises a simple question for investors who care about valuation. Is the current price tag on Cerebras stock still in line with what the business is generating in sales?
## MOG.B +6.7%  Moog
- Fri 13 Nov | Stock Titan | Moog (MOG) director sells Class A shares in nine trades under a preset trading plan.
  https://www.stocktitan.net/sec-filings/MOG/form-4-moog-inc-insider-trading-activity-19dd5dc1dbe9.html
  > Moog director John Scannell sells 3,000 shares Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Fri 13 Nov | scanx.trade | Moog Inc. to release Q4FY26 results on November 20, 2026
  https://scanx.trade/stock-market-news/companies/moog-inc-release-q4fy26-results-november-20-2026/56140752
  > to release Q4FY26 results on November 20, 2026 will release fiscal 2026 fourth quarter and full year financial results on November 20, 2026 - CEO Pat Roche and CFO Jennifer Walter will host a conference call at 10:00 am ET
- Fri 13 Nov | Stock Titan | Moog's 10 a.m. ET results call is set for Nov. 20.
  https://www.stocktitan.net/news/MOG/moog-inc-to-announce-fiscal-2026-year-end-results-on-november-20-3l7xfb692nal.html
  > to Announce Fiscal 2026 Year-End Results on November 20, 2026 Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Fri 13 Nov | Yahoo Finance | Moog (MOG.A) Earnings Expected to Grow: What to Know Ahead of Q4 Release
  https://finance.yahoo.com/markets/stocks/articles/moog-mog-earnings-expected-grow-140001035.html
  > Moog (MOG.A) is expected to deliver a year-over-year increase in earnings on higher revenues when it reports results for the quarter ended September 2026.
## ALNY +5.4%  Alnylam Pharmaceuticals
- Fri 13 Nov | Stock Titan | One investor reports owning 10.9 million shares of Alnylam (ALNY).
  https://www.stocktitan.net/sec-filings/ALNY/schedule-13g-a-alnylam-pharmaceuticals-inc-amended-passive-investment-8183041103fc.html
  (page: did not load (429))
- Fri 13 Nov | Traders Union | Alnylam Pharmaceuticals shares jump around 5.5% as strong Q3 product revenue drives commercial momentum
  https://tradersunion.com/news/stocks/show/4238510-alnylam-pharmaceuticals-rises-5-40percent-today/
  (page: did not load (403))
- Fri 13 Nov | Stock Titan | An investment manager reports over 10% of Alnylam (ALNY), with no shared voting power.
  https://www.stocktitan.net/sec-filings/ALNY/schedule-13g-a-alnylam-pharmaceuticals-inc-amended-passive-investment-2b2a0b6dc3f8.html
  (page: did not load (429))
- Fri 13 Nov | Quiver Quantitative | Why Alnylam Pharmaceuticals (ALNY) Stock Is Up Today | ALNY Stock News
  https://www.quiverquant.com/news/Why+Alnylam+Pharmaceuticals+(ALNY)+Stock+Is+Up+Today
  > Alnylam Pharmaceuticals (ALNY) is up 6.9% today. Here is some analysis on what might have caused this price movement.
## U +5.2%  Unity Software
- Fri 13 Nov | GuruFocus | Unity Software Inc (U) Shares Surge 5.2% -- What GF Score of 68 Tells Investors
  https://www.gurufocus.com/news/9198827/unity-software-inc-u-shares-surge-52-what-gf-score-of-68-tells-investors
  (page: did not load (403))
- Fri 13 Nov | Stock Titan | Convertible notes due in 2027 underpin Sequoia Capital DIV-2022’s Unity Software (U) stake.
  https://www.stocktitan.net/sec-filings/U/schedule-13g-a-unity-software-inc-amended-passive-investment-disclosu-af4c80ad7ab2.html
  > Unity Software: Sequoia Capital DIV-2022 has 0.3% stake Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale. (U) reports that Sequoia Capital DIV-2022, L.P.
- Fri 13 Nov | Yahoo Finance | Unity (U) Stock Sees Fair Value Lift After Q3 Spurs Higher Analyst Targets
  https://finance.yahoo.com/markets/stocks/articles/unity-u-stock-sees-fair-200842465.html
  > Unity Software is back in focus as analysts lift their modeled fair value from US$50.41 to US$61.29, a sizable reset to where they think the stock could reasonably trade.
- Fri 13 Nov | Investing.com Nigeria | BTIG reiterates Buy on Unity Software stock, keeps $60 target By Investing.com
  https://ng.investing.com/news/stock-market-news/btig-reiterates-buy-on-unity-software-stock-keeps-60-target-93CH-2805834
  (page: did not load (403))
## NBIS -9.9%  Nebius Group
```

## Results to record (results_due.py)
## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py
### BRK.B
- BRK.B: 8-K (results release) filed 2026-11-09: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452530/brka-20261107.htm
- BRK.B: 10-Q filed 2026-11-09: https://www.sec.gov/Archives/edgar/data/1067983/000119312526452412/brka-20260930.htm
    Revenue, quarter to 2026-09-30 (10-Q filed 2026-11-09): $74.32bn; a year earlier $63.75bn (+16.6%)
    Net income, quarter to 2026-09-30 (10-Q filed 2026-11-09): $22.11bn; a year earlier $30.80bn (-28.2%)
### ABUK
- Wed 11 Nov | ad-hoc-news.de | Abu Qir Fertilizers stock: nine-month net profit jumps 103%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/abu-qir-fertilizers-stock-nine-month-net-profit-jumps-103/70489206
  > Abu Qir Fertilizers reported a sharp increase in nine-month profitability on October 29, 2026, when it released unaudited financial indicators for the period ended September 30. Abu Qir Fertilizers reported net profit after tax of EGP 12.97 billion, up 103 percent from EGP 6.40 billion in the comparable period of 2025. Revenue reached EGP 31.49 billion, compared with EGP 16.58 billion a year earlier, an increase of 90 percent.
### ALCN
- Wed 11 Nov | جريدة المال | الأهلي فاروس: أرباح تشغيلية استثنائية لـ «النزهة» و«الحاويات» دون فرصة شراء عند التقييمات الحالية
  https://almalnews.com/2146570/الأهلي-فاروس-أرباح-تشغيلية-استثنائية-لـ-«النزهة»/
  > أظهر تقرير صادر عن وحدة بحوث «الأهلي فاروس» أن نتائج أعمال «مستشفى النزهة الدولي» خلال الأشهر التسعة الأولى من عام 2026 جاءت إيجابية على صعيد الإيرادات والأرباح، محققة 434.2 مليون جنيه إيرادات بنمو 10% على أساس سنوي، وصافي ربح بلغ 143.5 مليون جنيه بزيادة 14% على أساس سنوي. [Figures on the page: nine months; first half. Check which one each figure is.]
### EGAL
- Sat 14 Nov | ekhbary24.com | مصر للألومنيوم تحقق 4.93 مليار جنيه أرباحاً في 3 أشهر
  https://ekhbary24.com/article/53511
  > أعلنت شركة مصر للألومنيوم، التابعة للشركة القابضة للصناعات المعدنية، ارتفاع صافي أرباحها بنسبة 104% خلال الربع الأول من العام المالي 2026-2027، لتسجل 4.93 مليار جنيه مقابل 2.41 مليار جنيه في الفترة المماثلة من العام السابق. بلغت إيرادات الشركة خلال الفترة من يوليو إلى سبتمبر 2026 نحو 12.05 مليار جنيه، مقارنة بـ 11.33 مليار جنيه في الربع المقابل من العام المالي الماضي، محققة نمواً بنسبة 6.35%.
- Sun 08 Nov | آراب فاينانس | %104 نموًا بأرباح مصر للألومنيوم في ثلاثة أشهر
  https://www.arabfinance.com/ar/news/newdetails/أرباح-مصر-للألومنيوم-في-ثلاثة-أشهر
  > آراب فاينانس: أعلنت شركة مصر للألومنيوم (EGAL)، عن مؤشرات نتائج الاعمال غير مدققة عن الفترة المنتهية فى 30/09/2026، والتي أظهرت تحقيق صافي ربح بلغ 4.928 مليار جنيه مقابل صافي ربح بلغ 2.415 مليار جنيه عن نفس الفترة من العام السابق، بنسبة نمو بلغت 104%، حسبما ذكرت الشركة في بيانها المرسل إلى البورصة المصرية.
- Sun 08 Nov | شبكة تواصل الإخبارية | أرباح مصر للألومنيوم تقفز إلى 4.93 مليار جنيه.. تضاعف الأرباح خلال 3 أشهر
  https://twaslnews1.twaslnews.com/7312425/
- Sun 08 Nov | جريدة البورصة | "مصر للألومنيوم" تضاعف أرباحها في الربع الأول إلى 4.93 مليار جنيه
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: SWDY, JUFO, EAST, EFIH, EMFD, BQDC.
- Already recorded: COMI, ETEL.

## Coming up (seven days)
- 2026-11-16 CLHO results (expected)
- 2026-11-16 EFID results (expected)
- 2026-11-16 JUFO results (expected)
- 2026-11-16 PHDC results (expected)
- 2026-11-16 XOM dividend
- 2026-11-17 EGAL dividend
- 2026-11-17 NVDA results (expected)
- 2026-11-18 EAST results (expected)
- 2026-11-18 EFIH results (expected)
- 2026-11-18 HRHO results (expected)
- 2026-11-19 MSFT dividend

## Views
- judged right with no lesson yet: Chip stocks stay under pressure into Apple's results  <- write its `lesson`
- due 2026-11-13: Higher rates protect CIB's margins (on track)
- due 2026-11-20: Brent stays below $105 while Iran talks continue (open)
    2026-10-31-chips: on track -> right  (Judged on its date: Nvidia at 162.85 from 204.64 (-20.4%).)

## Fair value
- Changed since the last run: nothing by 10 points or more.
- In the ten cheapest or dearest with no note: MCQE, SCEM, ADIB, CSAG, ARCC, AMOC, MTIE, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-14. Open each story before using it.
## COMI  (8 leads)
- Sat 14 Nov | متن نيوز | الدولار يسجل 53.50 جنيه للبيع بالبنك المركزي.. و53.45 جنيه في CIB والإسكندرية
  https://www.matnnews.com/312923
  > الدولار يسجل 53.50 جنيه للبيع بالبنك المركزي.. و53.45 جنيه في CIB والإسكندرية حافظ سعر الدولار الأمريكي أمام الجنيه المصري اليوم السبت 14 نوفمبر 2026 على مستوياته المسجلة في البنوك، بالتزامن مع استمرار العطلة الأسبوعية وتوقف التعاملات المصرفية، وسط استقرار أسعار الشراء والبيع في عدد من البنوك العاملة بالسوق المحلية.
- Fri 13 Nov | بنكي | بطاقة CIB noon الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/414
  > - كاش باك 5% - معدل الفائدة السنوي الفعلي 28 عرض ساري على البطاقة تقسيط بدون فوائد 17 · خصومات 12 · 4 بينتهوا خلال أيام - تقسيط بدون فوائد Dream 2000 دريم 2000 - تقسيط المشتريات لمدة 12 شهرًا بدون فوائد Audio Technology شرف دي جي مرتبة بالأقرب انتهاءً · 6 من 28
- Fri 13 Nov | بنكي | بطاقة كاش باك (Cashback) الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/405
  (same wording as the بنكي story above: one source, not two)
## TMGH  (2 leads)
- Fri 13 Nov | Billionaires.Africa | Investor Memo: The $200 Billion Question — Hisham Talaat Moustafa's TMG, Egypt's Four New Megaprojects, and Who Will Share the Proceeds
  https://www.billionaires.africa/2026/11/13/investor-memo-the-200-billion-question-hisham-talaat-moustafas-tmg-egypts-four-new-megaprojects-and-who-will-share-the-proceeds/
  > Investor Memo: The $200 Billion Question — Hisham Talaat Moustafa's TMG, Egypt's Four New Megaprojects, and Who Will Share the Proceeds Talaat Moustafa Group has agreed four projects with Egypt's government worth about $200 billion, nearly 60 times its market value.
- Thu 12 Nov | Billionaires.Africa | Egyptian billionaire Hisham Talaat Moustafa's $200 billion TMG deal draws military interest
  https://www.billionaires.africa/2026/11/12/egyptian-billionaire-hisham-talaat-moustafas-200-billion-tmg-deal-draws-military-interest/
  > Egypt's military establishment is pushing for a share of the roughly $200 billion in development projects that Egyptian billionaire Hisham Talaat Moustafa's Talaat Moustafa Group Holding Co. agreed with the government in October, Africa Intelligence reported on Nov. The four projects carry total planned investment of about 11 trillion Egyptian pounds ($199 billion).
## ETEL  (8 leads)
- Fri 13 Nov | الهيئة العامة للاستعلامات | Telecom Egypt climbs to MSCI Global Standard category
  https://sis.gov.eg/en/media-center/news/telecom-egypt-climbs-to-msci-global-standard-category/
  (page: did not load (URLError))
- Fri 13 Nov | موقع الموقع | المصرية للاتصالات تنضم إلى مؤشر MSCI Egypt القياسي بعد ترقيتها من فئة الشركات الصغيرة
  https://almawq3.com/المصرية-للاتصالات-تنضم-إلى-مؤشر-msci-egypt-الق/
  > كتب – أحمد عادل حققت الشركة المصرية للاتصالات خطوة جديدة في مسار تعزيز حضورها بأسواق المال الدولية، بعدما أعلنت نتائج المراجعة الدورية لمؤشرات مورجان ستانلي كابيتال إنترناشيونال (MSCI) لشهر نوفمبر 2026، انضمام الشركة إلى مؤشر MSCI Egypt ضمن فئة الشركات القياسية (Global Standard)، عقب ترقيتها من فئة الشركات الصغيرة (Small Cap).
- Fri 13 Nov | TechAfrica News | Telecom Egypt Revenue Rises 19% to EGP 93.6 Billion in 9M 2026
  https://techafricanews.com/2026/11/13/telecom-egypt-revenue-rises-19-percent-egp-93-6-billion-9m-2026/
  > Telecom Egypt Revenue Rises 19% to EGP 93.6 Billion in 9M 2026 The company said its priorities remain focused on disciplined investment and capital allocation, stronger cash flows and delivering long-term value to shareholders.
## SWDY  (7 leads)
- Thu 12 Nov | خاص عن مصر | إيرادات "السويدي إليكتريك" تقفز إلى 263 مليار جنيه في 9 أشهر والأرباح ترتفع 16%
  https://aboutmsr.com/إيرادات-السويدي-إليكتريك-تقفز-إلى-263-مل/
  > سجلت شركة «السويدي إليكتريك» نموًا في إيراداتها المجمعة بنسبة 31.7% خلال أول تسعة أشهر من عام 2026، لتصل إلى 263.03 مليار جنيه، مقابل 199.7 مليار جنيه خلال الفترة نفسها من العام الماضي، مدعومة بزيادة حجم أعمالها، فيما ارتفع صافي الأرباح بنسبة 16.07% إلى 16.4 مليار جنيه. [Figures on the page: standalone; consolidated; nine months; one quarter. Check which one each figure is.]
- Thu 12 Nov | جريدة باور نيوز الاخبارية | أرباح السويدي إليكتريك تقفز إلى 16.4 مليار جنيه في 9 أشهر بزيادة قدرها 16% عن نفس الفترة من العام السابق
  https://powernews.cc/?p=293886
  > أظهرت القوائم المالية المجمعة لشركة السويدي إليكتريك عن التسعة أشهر الأولى من العام الجاري؛ نمو أرباح الشركة بنسبة 16% على أساس سنوي. [Figures on the page: standalone; consolidated; nine months. Check which one each figure is.]
- Thu 12 Nov | ايكونومي بلس | أرباح السويدي إليكتريك ترتفع 35% في الربع الثالث إلى 5.4 مليار جنيه
  https://economyplusme.com/ar/news/34144
  > أرباح السويدي إليكتريك ترتفع 35% في الربع الثالث إلى 5.4 مليار جنيه ارتفع صافي ربح شركة السويدي إليكتريك بعد خصم حقوق الأقلية والضرائب خلال الربع الثالث من عام 2026 بنسبة 35.1% على أساس سنوي، ليصل إلى نحو 5.4 مليار جنيه، مقابل 3.98 مليار جنيه خلال الفترة المقارنة من عام 2025. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
## ORAS  (1 leads)
- Sat 14 Nov | www.youlyou.com | تحالف أوراسكوم كونستراكشون يؤمن تمويل محطة رياح في مصر والتشغيل صيف 2028
  https://www.youlyou.com/93991
  > 1- تأمين تمويل محطة رياح جديدة في مصر بقدرة 900 ميجاوات. 2- المشروع ينفذه تحالف ENGIE وAeolus وأوراسكوم للإنشاءات. 3- المحطة تقع بمنطقة رأس شقير على خليج السويس. 4- بدء التشغيل بقدرة 300 ميجاوات في ديسمبر 2027. 5- المحطة توفر الكهرباء لأكثر من 1.4 مليون منزل مصري
## FWRY  (2 leads)
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية
  https://www.fintechgate.net/257376
  > سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية واصل سهم شركة «فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية» تعزيز مكاسبه في البورصة المصرية للأسبوع الثاني على التوالي خلال تعاملات شهر نوفمبر الحالي، مستفيدًا من موجة الصعود التي شهدتها السوق وارتفاع مؤشراتها الرئيسية والثانوية، وسط أداء إيجابي للأسهم القيادية وتحسن شهية المستثمرين للشراء.
- Thu 12 Nov | مجلة أرقام | Whish Moneyتعتمد Featurespaceمن فيزا لتعزيز قدراتها على التصدي الفوري للاحتيال وحماية عملائها
  https://arqam.news/609751/
  (page read: it never names the company, so probably not about it: skip)
## ABUK  (8 leads)
- Fri 13 Nov | Sada Elbalad English | Abu Qir Fertilizers Signs EGP 76.17M Deal for 3 MW of Solar Power
  https://see.news/abu-qir-fertilizers-signs-egp-7617m-deal-for-3-mw-of-solar-power
  > Abu Qir Fertilizers and Chemical Industries has signed a EGP 76.17 million contract with the Arab Organization for Industrialization (AOI) to implement the second phase of its solar power project in Alexandria, adding around 3 megawatts of renewable energy capacity as the company seeks to reduce its reliance on electricity from the national grid.
- Thu 12 Nov | البوابة نيوز | باستثمارات 76.17 مليون جنيه.. العربية للتصنيع توقع عقدًا لتنفيذ محطات طاقة شمسية لشركة أبوقير للأسمدة
  https://www.albawabhnews.com/5435257
  (page: did not load (403))
- Thu 12 Nov | ايكونومي بلس | "العربية للتصنيع" توقع عقدا لتنفيذ محطات شمسية لـ"أبوقير للأسمدة" باستثمارات 76.2 مليون جنيه
  https://economyplusme.com/ar/news/34138
  > "العربية للتصنيع" توقع عقدا لتنفيذ محطات شمسية لـ"أبوقير للأسمدة" باستثمارات 76.2 مليون جنيه وقعت الهيئة العربية للتصنيع عقداً لتوريد وتركيب محطات طاقة شمسية لشركة أبوقير للأسمدة والصناعات الكيماوية بمحافظة الإسكندرية، بقدرة إجمالية تبلغ نحو 3 ميجاوات، وتكلفة استثمارية تقدر بنحو 76.2 مليون جنيه.
## HRHO  (5 leads)
- Fri 13 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «إي إف جي القابضة» يقفز 6.64% ويضيف 2.27 مليار جنيه لقيمته السوقية ببورصة مصر خلال أسبوع
  https://www.fintechgate.net/257381
  > سهم «إي إف جي القابضة» يقفز 6.64% ويضيف 2.27 مليار جنيه لقيمته السوقية ببورصة مصر خلال أسبوع عزز سهم مجموعة «إي إف جي القابضة» مكاسبه في البورصة المصرية خلال تعاملات الأسبوع الماضي، مستفيدًا من تحسن أداء أسهم قطاع الخدمات المالية غير المصرفية، وسط نشاط ملحوظ في التداولات على السهم، بالتزامن مع الارتفاع الجماعي لمؤشرات السوق.
- Thu 12 Nov | بوابة الجمهورية | إي اف چي هيرميس تقدم الخدمات الاستشارية في الطرح العام الأولي لشركة دي أي بي هولدينغ بقيمة 1.94 مليار درهم بسوق دبي المالي
  https://www.gomhuriaonline.com/5042171
  > إي اف چي هيرميس تقدم الخدمات الاستشارية في الطرح العام الأولي لشركة دي أي بي هولدينغ بقيمة 1.94 مليار درهم بسوق دبي المالي
## JUFO  (2 leads)
- Thu 12 Nov | Investing.com | Earnings call transcript: Juhayna posts record Q3 2026 sales as stock slips
  https://www.investing.com/news/transcripts/earnings-call-transcript-juhayna-posts-record-q3-2026-sales-as-stock-slips-93CH-5021816
  (page: did not load (403))
- Thu 12 Nov | Investing.com | جهينة للصناعات الغذائية تسجل مبيعات قياسية في الربع الثالث من 2026 وسط تراجع السهم
  https://sa.investing.com/news/transcripts/article-93CH-3439242
  (page: did not load (403))
## MFPC  (1 leads)
- Thu 12 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EAST  (3 leads)
- Thu 12 Nov | اخبارك نت | «MSCI» تضم المصرية للاتصالات إلى مؤشرها القياسي وتستبعد الشرقية للدخان في مراجعة نوفمبر | أموال الغد
  https://akhbarak.net/news/details/49543838/4/msci-تضم-المصرية-للاتصالات-إلى-مؤشرها-القياسي-وتستبعد-الشرقية-للدخان-في-مراجعة-نوفمبر-أموال-الغد
  > أعلنت مؤسسة مورجان ستانلي كابيتال إنترناشيونال «MSCI» انضمام سهم الشركة المصرية للاتصالات إلى مؤشر MSCI Egypt، ضمن مؤشرات MSCI العالمية القياسية (Global Standard Indexes)، مقابل استبعاد سهم الشركة الشرقية للدخان، وذلك في إطار نتائج المراجعة الدورية لمؤشرات الأسواق العالمية لشهر نوفمبر 2026.
- Thu 12 Nov | مانكيش نت | ارتفاع أرباح الشرقية للدخان إلى 8.98 مليار جنيه في 9 أشهر
  https://mangish.net/ارتفاع-أرباح-الشرقية-للدخان-إلى-8-98-مليا/
  > أفادت شركة الشرقية – إيسترن كومباني بأنها قد أنجزت أعمالها المجمعة عن التسعة أشهر التي انتهت في 30 سبتمبر 2026، وذلك وفقًا للبيان الذي تم إرساله إلى البورصة المصرية يوم الخميس الموافق 12 نوفمبر 2026. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Thu 12 Nov | الجريدة العقارية | أرباح الشرقية للدخان ترتفع إلى 8.98 مليار جنيه خلال أول 9 أشهر من 2026
  https://www.aleqaria.com.eg/post/details/357800/أرباح-الشرقية-للدخان
  (page: only 67 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EFIH  (8 leads)
- Fri 13 Nov | Pioneers Misr | أرباح إي فاينانس 2026 الأرشيف - Pioneers Misr
  https://pioneersmisr.com/tag/أرباح-إي-فاينانس-2026/
  (page: only 36 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «إي فاينانس» يربح 5.1 مليار جنيه خلال أسبوع ويواصل صعوده ببورصة مصر
  https://www.fintechgate.net/257374
  > سهم «إي فاينانس» يربح 5.1 مليار جنيه خلال أسبوع ويواصل صعوده ببورصة مصر [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Fri 13 Nov | Elsiyasa | إي فاينانس المصرية تستعد لدخول لبنان لتطوير أنظمة المدفوعات الحكومية
  https://elsiyasa.com/article/436408
  > تعتزم مجموعة «إي فاينانس» المصرية دخول السوق اللبنانية خلال عام 2027، ضمن خطتها للتوسع خارج مصر، عبر تصدير أنظمتها الرقمية المتخصصة في إدارة المدفوعات وتحصيل الإيرادات الحكومية.
## EMFD  (8 leads)
- Thu 12 Nov | almotawwer.com | Rowad Modern Engineering Secures the Largest Construction Package Ever Awarded by Emaar Misr in Egypt
  https://almotawwer.com/companies-and-investments/333996/
  > Rowad Modern Engineering Secures the Largest Construction Package Ever Awarded by Emaar Misr in Egypt Cairo, Egypt – [12/11/2026] — Rowad Modern Engineering has secured the largest construction package Emaar Misr has awarded in Egypt to date for Marassi Red Sea, its landmark coastal development in Abo Soma, Hurghada.
- Thu 12 Nov | almotawwer.com | رواد الهندسة الحديثة تنفذ 667 فيلا وتاون هاوس بمشروع مراسي البحر الأحمر بالتعاون مع إعمار مصر
  https://almotawwer.com/companies-and-investments/333990/
  > تواصل شركات المقاولات تعزيز حصتها في مشروعات التطوير العقاري والسياحي الكبرى، مع اتجاه المطورين إلى إسناد حزم إنشائية متكاملة لشركات تمتلك خبرات تنفيذية في المشروعات السكنية والبنية التحتية، وهو ما يعكس اتساع نطاق الأعمال المرتبطة بالتوسعات العمرانية والسياحية على ساحل البحر الأحمر.
- Thu 12 Nov | https://www.youlyou.com/ | العبار يجمع 19 مليار جنيه من إعمار مصر في 9 شهور.. والأرباح تقفز 129%
  https://www.youlyou.com/93304
  > 1- إعمار مصر تسجل إيرادات بقيمة 18.97 مليار جنيه خلال 9 أشهر من 2026. 2- الإيرادات ترتفع 27.1% مقارنة بالفترة نفسها من 2025. 3- صافي ارباح إعمار مصر يقفز 128.8% إلى 9.82 مليار جنيه. 4- الإيرادات التمويلية ترتفع إلى 5.6 مليار جنيه مقابل 1.99 مليار جنيه.
## BQDC  (8 leads)
- Fri 13 Nov | عالم المال | بالأرقام.. أعلى شهادات الادخار في بنك القاهرة 2026
  https://alamalmal.net/article/943209/بالأرقام-أعلى-شهادات-الادخار-في-بنك-القاهرة
  > تتصدر شهادات الادخار في بنك القاهرة 2026 اهتمامات المواطنين الباحثين عن أوعية ادخارية تحقق عائدًا تنافسيًا على مدخراتهم، خاصة مع تنوع المنتجات التي يقدمها البنك بين الشهادات ثابتة العائد ومتغيرة العائد، واختلاف دوريات صرف الأرباح بين اليومية والشهرية والربع سنوية والسنوية. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Fri 13 Nov | Masrawy | خالد أبو بكر يهاجم تصريحات حمدين صباحي بشأن بيع أراضي مصر وبنك القاهرة
  https://www.masrawy.com/news/news_egypt/details/2026/11/13/3078330/خالد-أبو-بكر-يهاجم-تصريحات-حمدين-صباحي-بشأن-بيع-أراضي-مصر-وبنك-القاهرة
  > علق المحامي خالد أبو بكر على تصريحات حمدين صباحي بشأن رفض بيع أراضي مصر وبنك القاهرة، مطالبًا إياه بالتركيز على الحديث في تخصصه، والابتعاد عن الشعارات التي وصفها بأنها باتت باهتة.
- Fri 13 Nov | مصر تايمز | خالد أبو بكر يهاجم حمدين صباحي بسبب شعارات "بيع مصر وبنك القاهرة"
  https://www.masrtimes.com/777117
  > خالد أبو بكر يهاجم حمدين صباحي بسبب شعارات "بيع مصر وبنك القاهرة" هاجم الإعلامي والمحامي الدولي خالد أبو بكر، السياسي حمدين صباحي، بعد انتقاداته لتوجهات الدولة الاقتصادية، ورفع شعارات "لا لبيع أرض مصر ولا لبيع بنك القاهرة".
## EGAL  (1 leads)
- Sat 14 Nov | ekhbary24.com | مصر للألومنيوم تحقق 4.93 مليار جنيه أرباحاً في 3 أشهر
  https://ekhbary24.com/article/53511
  > أعلنت شركة مصر للألومنيوم، التابعة للشركة القابضة للصناعات المعدنية، ارتفاع صافي أرباحها بنسبة 104% خلال الربع الأول من العام المالي 2026-2027، لتسجل 4.93 مليار جنيه مقابل 2.41 مليار جنيه في الفترة المماثلة من العام السابق.
## AMOC  (1 leads)
- Fri 13 Nov | جريدة باور نيوز الاخبارية | غدا.. عمومية “أموك” تبحث تعديل 6 مواد بالنظام الأساسي
  https://powernews.cc/?p=293946
  > دعت شركة الإسكندرية للزيوت المعدنية “أموك”، مساهميها غدا السبت لحضور الجمعية العامة غير العادية للنظر في تعديل 6 مواد بنظامها الأساسي. وستنظر العمومية في تعديل المواد أرقام (7، 21، 28، 46، 56) من النظام الأساسي للشركة. وبدأت شركة الإسكندرية للزيوت المعدنية “أموك”، التشغيل التجريبي لمشروع معالجة الغازات الحامضية.
## SKPC  (2 leads)
- Thu 12 Nov | https://www.youlyou.com/ | كيف ساهمت خامات البلاستيك المستوردة في زيادة مبيعات سيدبك إلى 14.7 مليار جنيه؟
  https://www.youlyou.com/93318
  > 1- أرباح سيدبك تسجل 1.496 مليار جنيه خلال 9 أشهر من 2026. 2- إيرادات الشركة ترتفع 34.8% إلى 14.713 مليار جنيه. 3- مجمل الربح ينمو 16.4% ليسجل 2.355 مليار جنيه. 4- مبيعات خامات البلاستيك المستوردة تسجل 1.899 مليار جنيه. 5- نصيب السهم من الأرباح يتراجع إلى 1.07 جنيه مقابل 1.47 جنيه
- Thu 12 Nov | بترونيوز | بترومنت تجدد عقد الصيانة الشاملة مع سيدبك لتعزيز كفاءة التشغيل واستدامة الأصول
  https://petro-news.com/182015
  (page: did not load (403))
## EFID  (1 leads)
- Fri 13 Nov | TradingView | Edita Food Industries SAE Financial Disclosures & Filings
  https://www.tradingview.com/symbols/EGX-EFID/documents/
  (page: only 50 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## AAPL  (8 leads)
- Sat 14 Nov | Yahoo Finance | Is Apple Stock a Buy Right Now?
  https://finance.yahoo.com/markets/stocks/articles/apple-stock-buy-now-002700097.html
  > In a market ripe with opportunities after seeing so many growth stocks implode this earnings season, Apple (NASDAQ: AAPL) is thriving. The consumer tech giant hit another all-time high on Thursday.
- Fri 13 Nov | USA Today | Apple stock stands out as Big Tech tumbles. Here's what's working
  https://www.usatoday.com/story/money/money-management/investing/2026/11/13/apple-stock-big-tech-market/92708432007/
  (page: did not load (402))
- Fri 13 Nov | The Apple Post | Analyst raises Apple stock target to $425 on iPhone Duo hopes
  https://www.theapplepost.com/2026/11/13/74235/analyst-raises-apple-stock-target-to-425-on-iphone-duo-hopes/
  > Apple shares have received one of Wall Street’s most optimistic new forecasts after China Renaissance raised its price target for the company to $425, betting that iPhone Duo could encourage a major wave of iPhone upgrades.
## MSFT  (8 leads)
- Sat 14 Nov | TradingView | Key facts: Microsoft $45.2B Q1 capex; service outage hits shares
  https://www.tradingview.com/news/tradingview:0a643077ed284:0-key-facts-microsoft-45-2b-q1-capex-service-outage-hits-shares/
  > Key facts: Microsoft $45.2B Q1 capex; service outage hits shares Vortex Media1 min read - Microsoft (MSFT) spent $45.2 billion on capital projects in fiscal Q1 2027 and expects about $170 billion in 2026. Spending may top $50 billion in December as data-center capacity expands.
- Sat 14 Nov | BBN Times | FTSE 100 Today: London Soars 10,902.56 as Aviva and Energy Stocks Shrug Off Nvidia and Microsoft Turmoil
  https://www.bbntimes.com/global-economy/ftse-100-today-london-soars-10-902-56-as-aviva-and-energy-stocks-shrug-off-nvidia-and-microsoft-turmoil
  > FTSE 100 Today: London Soars 10,902.56 as Aviva and Energy Stocks Shrug Off Nvidia and Microsoft Turmoil Britain’s blue-chip index rose 0.4% on Friday, finishing a 2.2% weekly gain as insurers, utilities and oil majors offset another sell-off in US technology stocks and a global Microsoft outage that disrupted UK public services.
- Fri 13 Nov | Yahoo Finance | Microsoft 365 Outage: CIOs Should Verify Recovery Across Workflows and Security Controls, Says Infotech
  https://finance.yahoo.com/technology/articles/microsoft-365-outage-cios-verify-220300737.html
  > The Microsoft 365 outage has shown how email dependencies can interrupt business processes even when other functions remain available. Infotech's research note, Microsoft 365 Outage: Immediate Actions for CIOs, covers recovery validation, potential security coverage gaps, and continuity measures for prolonged cloud outages.
## NVDA  (8 leads)
- Sat 14 Nov | Yahoo Finance | Jensen Huang Misled Nvidia Leadership, Lawyer On Affair With Alleged Chinese Spy: Report
  https://finance.yahoo.com/markets/stocks/articles/jensen-huang-misled-nvidia-leadership-092558570.html
  > - In October, Huang sent two separate messages to Nvidia General Counsel Tim Teter and Chief Marketing Officer Alison Wagonfeld, describing the interactions as standard dealings with customers.
- Sat 14 Nov | The Motley Fool | Should You Really Buy Nvidia Stock After CEO Jensen Huang's Exit? Wall Street Has a Clear Answer for Investors.
  https://www.fool.com/investing/2026/11/14/buy-nvidia-stock-ceo-jensen-huang-exit-wall-street-answer/
  > Nvidia (NVDA -2.01%) has dominated the headlines in recent days. CEO Jensen Huang resigned from his position after revelations of extramarital affairs, including a relationship with a businesswoman that U.S. Nvidia's board of directors launched an investigation into the potential national security implications of the news, and Huang officially resigned on Thursday, Oct.
- Sat 14 Nov | WSJ | Nvidia’s Meteoric Rise, in One Chart
  https://www.wsj.com/tech/nvidias-meteoric-rise-in-one-chart-2f47d54e
  (page: did not load (401))
- Sat 14 Nov | Morningstar | Investor Focus: Nvidia CEO Crisis, Anthropic IPO Valuation, and Undervalued UK Stocks After Earnings
  https://global.morningstar.com/en-gb/columns/investor-focus-nvidia-ceo-crisis-anthropic-ipo-valuation-undervalued-uk-stocks-after-earnings
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 14 Nov | 富途牛牛 | With a NVIDIA stock holding worth $135 billion, will Jensen Huang sell off to cash out?
  https://news.futunn.com/en/post/1004523351/with-a-nvidia-stock-holding-worth-135-billion-will-jensen
- Sat 14 Nov | Yahoo Finance | Is Nvidia Worth This Much Less Without Jensen Huang?
  https://finance.yahoo.com/markets/stocks/articles/nvidia-worth-much-less-without-064902824.html
- Sat 14 Nov | Yahoo | Fact Check: Trump DID 'Dump' Up To $1 Million In Nvidia Stock -- But Also Bought Up To $1.6 Million
  https://www.yahoo.com/news/politics/articles/fact-check-trump-did-dump-054604090.html
- Sat 14 Nov | Yahoo Finance | Elon Musk, Tom Lee, Shopify CEO Sign ‘Stand With Jensen’ Petition To Reinstate Him As Nvidia CEO
  https://finance.yahoo.com/markets/stocks/articles/elon-musk-tom-lee-shopify-042453542.html
## AMZN  (8 leads)
- Sat 14 Nov | TIKR.com | Jim Cramer: Amazon Has What “May Soon Be a $50 Billion Semiconductor Business”
  https://www.tikr.com/blog/jim-cramer-amazon-has-what-may-soon-be-a-50-billion-semiconductor-business?
  > - A day after Jensen Huang resigned as Nvidia’s CEO, Jim Cramer said Amazon has what “may soon be a $50 billion semiconductor business.” - Andy Jassy gave that number in April: chips running above $20 billion a year would bring in about $50 billion priced like a standalone chipmaker. [Figures on the page: standalone; one quarter. Check which one each figure is.]
- Sat 14 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: Busey Bank Cuts Holdings
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-busey-bank-cuts-holdings-2026-11-14/
  > $AMZN Stock: Busey Bank Cuts Holdings - Busey Bank reduced its Amazon stake by 1.4% in the third quarter, selling 8,185 shares. It retained 579,451 shares worth about $144.4 million, making Amazon its fifth-largest holding.
- Sat 14 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: Asset Management One Co. Ltd. Trims Stake
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-asset-management-one-co-ltd-trims-stake-2026-11-14/
  > $AMZN Stock: Asset Management One Co. - Asset Management One Co. trimmed its Amazon stake by 0.7%, selling 34,327 shares in the third quarter; it still held about 4.63 million shares valued at $1.15 billion. - Analysts gave Amazon a “Moderate Buy” consensus rating, with an average price target of $321.74.
## GOOGL  (8 leads)
- Sat 14 Nov | Investing.com India | Form 4 Alphabet Inc Class A For: 14 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-14-november-93CH-5704653
  (page: did not load (403))
- Sat 14 Nov | CEOWORLD magazine | Billionaire Larry Page to Sell $148 Million of Alphabet Stock: What the Filing Shows
  https://ceoworld.biz/2026/11/14/billionaire-larry-page-to-sell-148-million-of-alphabet-stock-what-the-filing-shows/
  > Three trusts tied to the Google co-founder have filed to sell about half a million shares. The more consequential seller of Alphabet stock this year is Alphabet. Trusts linked to Larry Page have given notice that they intend to sell about $148.3 million of Alphabet stock. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Fri 13 Nov | ad-hoc-news.de | Alphabet's AI Spending Spree Faces Its Reckoning as HSBC and JPMorgan Diverge
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/alphabet-s-ai-spending-spree-faces-its-reckoning-as-hsbc-and-jpmorgan-diverge/70507103
  > HSBC analyst Paul Rossington is betting Alphabet shares can recover from their recent slide, publishing a price target of $360 on the stock today. His bullish case rests on the pace of Google Cloud's expansion — provided the company can eventually convert its hefty infrastructure outlays into stronger free cash flow. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
## META  (8 leads)
- Sat 14 Nov | MarketBeat | Meta Platforms, Inc. $META Shares Newly Purchased by Accuvest Global Advisors
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-shares-newly-purchased-by-accuvest-global-advisors-2026-11-14/
  > $META Shares Newly Purchased by Accuvest Global Advisors - Accuvest Global Advisors initiated a Meta stake in the third quarter, buying 4,660 shares worth about $3.38 million; the position represents 2.5% of its portfolio. - Other major investors also increased or initiated holdings, and institutional investors collectively own about 79.9% of Meta’s shares.
- Sat 14 Nov | GuruFocus | Meta Platforms Inc (META) Stock Up 2.9% and Still Undervalued -- GF Score: 99/100
  https://www.gurufocus.com/news/9199257/meta-platforms-inc-meta-stock-up-29-and-still-undervalued-gf-score-99100
  (page: did not load (403))
- Fri 13 Nov | Yahoo! Finance Canada | META Nov 2026 635.000 put (META261113P00635000) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/META261113P00635000/
  (page: did not load (404))
- Fri 13 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Stock Jumps 2.9% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-stock-jumps-29-heres-why-2026-11-13/
  > Meta Platforms (NASDAQ:META) Stock Jumps 2.9% - Here's Why - Meta shares rose 2.9% in Friday’s mid-day trading to $641.69, on volume about 17% below the daily average. - The company’s latest quarterly results beat estimates: earnings were $7.40 per share versus $6.54 expected, while revenue reached $64.6 billion and grew 26.1% year over year.
- Fri 13 Nov | Investing.com | Meta employees test prediction-market app, WSJ reports By Reuters
  https://www.investing.com/news/stock-market-news/meta-employees-test-predictionmarket-app-wsj-reports-5026444
- Fri 13 Nov | Investing.com | Meta tests prediction-market app for employees, WSJ reports
  https://www.investing.com/news/stock-market-news/meta-tests-predictionmarket-app-for-employees-wsj-reports-5026398
- Fri 13 Nov | Investing.com Nigeria | Meta tests prediction-market app for employees, WSJ reports By Investing.com
  https://ng.investing.com/news/stock-market-news/meta-tests-predictionmarket-app-for-employees-wsj-reports-2807129
- Fri 13 Nov | BNN Bloomberg | Jason Del Vicario’s Past Picks: Meta Platforms, Christian Dior & Oddity Tech
  https://www.bnnbloomberg.ca/video/shows/market-call/2026/11/13/jason-del-vicarios-past-picks-meta-platforms-christian-dior-oddity-tech/
## TSLA  (8 leads)
- Sat 14 Nov | MarketBeat | Tesla, Inc. $TSLA Stock Position Lowered by Diversified Trust Co
  https://www.marketbeat.com/instant-alerts/filing-tesla-inc-tsla-stock-position-lowered-by-diversified-trust-co-2026-11-14/
  > $TSLA Stock Position Lowered by Diversified Trust Co - Diversified Trust Co. cut its Tesla stake by 10.1% in the third quarter, selling 4,312 shares and ending with 38,220 shares valued at about $13.56 million.
- Sat 14 Nov | MarketBeat | 6,729 Shares of Tesla, Inc. $TSLA Acquired by Bernicke Wealth Management Ltd.
  https://www.marketbeat.com/instant-alerts/filing-6729-shares-of-tesla-inc-tsla-acquired-by-bernicke-wealth-management-ltd-2026-11-14/
  > 6,729 Shares of Tesla, Inc. $TSLA Acquired by Bernicke Wealth Management Ltd. - Bernicke Wealth Management acquired 6,729 Tesla shares in the third quarter, valued at about $2.39 million. Tesla represents 0.3% of the firm’s portfolio and is its 28th-largest holding.
- Sat 14 Nov | Stocktwits | Tesla Cybercab Now Available For Purchase For Select Customers — But There’s A Catch
  https://stocktwits.com/news-articles/markets/equity/tesla-cybercab-purchase-select-customers-but-catch/cNb26QDR9Qf
  > (TSLA) has begun inviting select customers to purchase its fully autonomous Cybercab, marking a new step in Elon Musk's long-promised robotaxi ambitions. However, owning the futuristic, two-seater vehicle comes with some significant limitations, including a mandatory monthly software subscription and restrictions on where it can operate.
## JPM  (8 leads)
- Sat 14 Nov | GuruFocus | JPMorgan Chase & Co (JPM) Stock Up 1.0% but GF Value Says Overvalued -- GF Score: 85/100
  https://www.gurufocus.com/news/9199268/jpmorgan-chase-co-jpm-stock-up-10-but-gf-value-says-overvalued-gf-score-85100
  (page: did not load (403))
- Sat 14 Nov | Yahoo Finance | JPMorgan Chase (JPM) Sees 40% Jump In Asia Pacific Alternative Asset Allocations
  https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-jpm-sees-40-042637965.html
  > - JPMorgan Chase (NYSE:JPM) reports a sharp rise in ultra-wealthy client demand for alternative investments tied to infrastructure themes. - The bank highlights a tilt toward assets linked to AI data centers, power grid upgrades, electrification and energy security projects.
- Sat 14 Nov | Financial-News.co.uk | JPMorgan Declares Preferred Stock Dividends on Three Series
  https://www.financial-news.co.uk/jpmorgan-declares-preferred-stock-dividends-on-three-series/
  > JPMorgan Chase & Co (NYSE: JPM) declared preferred stock dividends on its Series II, OO and PP shares on 13 November 2026, the bank said. The declaration covers three outstanding series of non-cumulative preferred stock and lands the same day JPMorgan filed a routine insider transaction form unrelated to the payout. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
## XOM  (8 leads)
- Sat 14 Nov | MarketBeat | ExxonMobil Corporation (NYSE:XOM) Stock Now Rated "Hold" by Sell-Side Brokerages
  https://www.marketbeat.com/instant-alerts/consensus-exxonmobil-corporation-nyse-xom-stock-now-rated-hold-by-sell-side-brokerages-2026-11-14/
  > ExxonMobil Corporation (NYSE:XOM) Stock Now Rated "Hold" by Sell-Side Brokerages - Analysts rate ExxonMobil “Hold” overall: Of 27 brokerages, 14 recommend holding, 12 recommend buying or strong buying, and one recommends selling. Their average 12-month price target is $170.79.
- Sat 14 Nov | Simply Wall St | Why Is ExxonMobil (XOM) Backing A $12.5 Billion Guyana Gas Project?
  https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/why-is-exxonmobil-xom-backing-a-125-billion-guyana-gas-proje
  > ExxonMobil Holdings (NYSE:XOM) approved a US$12.5b Longtail development offshore Guyana on 13 November 2026. Longtail is the eighth large scale project on the Stabroek block and is described by the company as its largest phase so far. We have also spotted 1 major warning sign worth knowing about at ExxonMobil Holdings.
- Sat 14 Nov | MarketBeat | ExxonMobil Corporation $XOM Stake Lowered by Aberdeen Group plc
  https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stake-lowered-by-aberdeen-group-plc-2026-11-14/
  > ExxonMobil Corporation $XOM Stake Lowered by Aberdeen Group plc - Aberdeen Group cut its ExxonMobil stake by 27.9% in the third quarter, selling 526,239 shares and ending the period with 1,359,956 shares valued at about $221.3 million. - Analyst opinion is mixed: MarketBeat reports a consensus Hold rating and an average price target of $170.79.
## AVGO  (8 leads)
- Sat 14 Nov | MarketBeat | Rep. David Taylor Buys Shares of Broadcom Inc. (NASDAQ:AVGO)
  https://www.marketbeat.com/instant-alerts/congress-rep-david-taylor-buys-shares-of-broadcom-inc-nasdaq-avgo-2026-11-14/
  > David Taylor Buys Shares of Broadcom Inc. David Taylor disclosed buying $1,001–$15,000 of Broadcom shares on November 5 in a joint brokerage account held by the David Taylor Trust. - Broadcom shares were reported down 4.8%; its latest quarterly results beat analyst expectations, with revenue up 85.5% year over year.
- Sat 14 Nov | 재경일보 | Nvidia shock spreads: AMD plunges 8.75%, Broadcom slides 4.76% : Finance : JKN
  https://news.jkn.co.kr/editions/english/post/1092735
  (page read: it never names the company, so probably not about it: skip)
- Sat 14 Nov | 재경일보 | AMD and Broadcom shares tumble a day after rallying on Jensen Huang resignation; semiconductor firms saw rebound effects as Nvidia fallout continues
  https://news.jkn.co.kr/editions/english/post/1092519
  > Expectations for delayed technology development and customer diversification The backdrop for the stock price surge was the expectation that NVIDIA's technology development direction and pace could be affected by the CEO change. Broadcom is expanding its custom AI accelerators and data center networking solutions.
- Sat 14 Nov | Seeking Alpha | Broadcom: Nvidia Has A Problem, And That Creates An Opportunity (NASDAQ:AVGO)
  https://seekingalpha.com/article/4968075-broadcom-nvidia-has-a-problem-and-that-creates-an-opportunity
  (page: did not load (403))
- Fri 13 Nov | bloomingbit | Nvidia Loses Nearly $1 Trillion in Value After Jensen Huang Resigns; Broadcom Drops 5%
  https://en.bloomingbit.io/feed/news/124412
- Fri 13 Nov | TIKR.com | Broadcom Sinks 7% as Rothschild Redburn Downgrade Slashes Target to $398: “Unlikely to Occur Quickly”
  https://www.tikr.com/blog/broadcom-sinks-7-as-rothschild-redburn-downgrade-slashes-target-to-398-unlikely-to-occur-quickly
- Fri 13 Nov | Global Banking & Finance Review | Broadcom falls 4.76% in Friday's session
  https://www.globalbankingandfinance.com/broadcom-avgo-falls-2026-11-13/
- Fri 13 Nov | Yahoo Finance Australia | Broadcom Inc. (AVGO) Suffers a Larger Drop Than the General Market: Key Insights
  https://au.finance.yahoo.com/news/broadcom-inc-avgo-suffers-larger-214501014.html
## BRK.B  (8 leads)
- Sat 14 Nov | CoinCodex | Berkshire Hathaway Tokenized gStocks Price: Live BRKBG/USD Rate, Market Cap & BRKBG Price Chart
  https://coincodex.com/crypto/berkshire-hathaway-gstocks/
  > | Exchange | Price | Volume | Price/Volume |  | Action | | Gate | $ 591.88$ 27,550 |  | $ 591.88 | $ 27,550 | Trade Now | | Berkshire Hathaway Tokenized gStocks Price | $ 591.89 | | 24H Volume | $ 27,574 | | Dominance | 0.00% |
- Sat 14 Nov | CoinCodex | Berkshire Hathaway Tokenized gStocks (BRKBG) Price Prediction 2026, 2027-2030
  https://coincodex.com/crypto/berkshire-hathaway-gstocks/price-prediction/
  > Berkshire Hathaway Tokenized gStocks (BRKBG) Price Prediction 2026, 2027-2030 Explore short and medium-term Berkshire Hathaway Tokenized gStocks price prediction analysis and check long-term Berkshire Hathaway Tokenized gStocks forecasts for 2026, 2030, and beyond. [4ms] Starting data fetch for slug=berkshire-hathaway-gstocks [33ms] fetchAsset(berkshire-hathaway-gstocks) completed in 29ms [36ms] Starting combineLatest for berkshire-hathaway-gstocks
- Sat 14 Nov | GuruFocus | Berkshire Hathaway Inc (BRK.B) Stock Up 0.5% but GF Value Says Overvalued -- GF Score: 74/100
  https://www.gurufocus.com/news/9199263/berkshire-hathaway-inc-brkb-stock-up-05-but-gf-value-says-overvalued-gf-score-74100
  (page: did not load (403))
## WMT  (8 leads)
- Fri 13 Nov | Yahoo Finance | How Digital Expansion At Walmart (WMT) Has Changed Its Investment Story
  https://finance.yahoo.com/markets/stocks/articles/digital-expansion-walmart-wmt-changed-231951520.html
  > - Walmart recently agreed to a record US$7.8 million settlement with Pennsylvania authorities over Child Labor Act violations and is rolling out new energy, AI shopping, and drone delivery initiatives while preparing to report third quarter earnings on 19 November 2026.
- Fri 13 Nov | Yahoo Finance | Walmart, Target, and Nvidia Headline a Pivotal Week for Q3 Earnings
  https://finance.yahoo.com/markets/stocks/articles/walmart-target-nvidia-headline-pivotal-230000146.html
  > Walmart WMT shares have seen a modest bid in recent weeks, likely reflecting the company's defensive attributes as the more glamorous AI trade has lost some of its earlier luster. Despite recent struggles, Walmart shares outperformed peers like Target TGT and even Amazon AMZN over the last five years, up more than +175% vs.
- Fri 13 Nov | MarketBeat | Walmart (NASDAQ:WMT) Shares Up 1.5% on Analyst Upgrade
  https://www.marketbeat.com/instant-alerts/price-walmart-nasdaq-wmt-shares-up-15-on-analyst-upgrade-2026-11-13/
  > Walmart (NASDAQ:WMT) Shares Up 1.5% on Analyst Upgrade - Walmart shares rose 1.5% after Wells Fargo raised its price target from $120 to $135 and maintained an overweight rating. - Analyst sentiment is broadly positive: the stock has a consensus “Buy” rating and an average price target of $131.90, with JPMorgan’s target at $145.
## V  (8 leads)
- Sat 14 Nov | GuruFocus | Is Visa Inc (V) Overvalued After 1.3% Rally? GF Value Says Overv
  https://www.gurufocus.com/news/9199269/is-visa-inc-v-overvalued-after-13-rally-gf-value-says-overvalued
  (page: did not load (403))
- Sat 14 Nov | Yahoo! Finance Canada | Visa (V) Stock Gets Fair Value Bump As Analysts Lift Targets On New Growth Areas
  https://ca.finance.yahoo.com/news/visa-v-stock-gets-fair-070814550.html
  > Visa's analyst narrative has shifted, with price targets now clustering in the US$480 to US$500 range, compared with a fair value estimate that has moved from US$437.06 to US$449.06.
- Sat 14 Nov | MarketBeat | Visa (NYSE:V) Shares Sold Off by Rep. David Taylor
  https://www.marketbeat.com/instant-alerts/congress-visa-nyse-v-shares-sold-off-by-rep-david-taylor-2026-11-14/
  > Visa (NYSE:V) Shares Sold Off by Rep. David Taylor disclosed selling $1,001–$15,000 of Visa shares on November 3 from a joint brokerage account. - Visa’s latest quarterly results topped expectations: EPS was $3.48 versus $3.44 forecast, while revenue rose 13.2% year over year to $12.14 billion.
## ORCL  (8 leads)
- Fri 13 Nov | Simply Wall St | Oracle (ORCL) Expanded Its Federal Health Network With Two Major U.S. Departments
  https://simplywall.st/stocks/us/software/nyse-orcl/oracle/news/oracle-orcl-expanded-its-federal-health-network-with-two-maj
  > Oracle (NYSE: ORCL) expanded its federal footprint as the U.S. Department of Veterans Affairs joined the Oracle Health Information Network under TEFCA. Department of War implemented Oracle's Health Information Network to support secure nationwide health data exchange across its care systems.
- Fri 13 Nov | MarketBeat | Oracle (NYSE:ORCL) Shares Down 1.4% - Time to Sell?
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-down-14-time-to-sell-2026-11-13/
  > Oracle (NYSE:ORCL) Shares Down 1.4% - Time to Sell? - Oracle shares fell 1.4% to $125.31, with trading volume 27% below its average. - Oracle’s latest quarter beat earnings and revenue estimates, with revenue up 29.6% year over year. Analysts maintain a consensus “Moderate Buy” rating and a $249.27 average price target.
- Fri 13 Nov | Yahoo Finance | Why Stephens Upgraded Oracle (ORCL)
  https://finance.yahoo.com/markets/stocks/articles/why-stephens-upgraded-oracle-orcl-213119416.html
  > We just published a list of the 10 Stocks With Insane Upside According to Reddit and Oracle (NYSE:ORCL) ranked 10th on this list. US stocks edged lower Thursday, snapping a rebound that had lifted the S&P 500 1.3% a day earlier.
## COST  (8 leads)
- Sat 14 Nov | Yahoo Finance | ‘They’re Getting Insider Information From Costco Employees’: Inside the Pokemon Card Line Where Resellers Buy Executive Memberships
  https://finance.yahoo.com/markets/stocks/articles/getting-insider-information-costco-employees-090729688.html
  > - Christa DiBiase says resellers at one COST warehouse buy Executive memberships to chase Pokemon cards, though she did not verify the claim of employee tips. - Membership upgrades fuel COST's profit engine: Executive members grew 9% to 42 million, and fee income rose 7% to about $2 billion.
- Sat 14 Nov | Simply Wall St | What Costco Wholesale Doubters Overlooked
  https://simplywall.st/stocks/us/consumer-retailing/nasdaq-cost/costco-wholesale/news/what-costco-wholesale-doubters-overlooked
  > If Costco Wholesale sat on your watchlist rather than in your portfolio this year, the gap between watching and owning may feel uncomfortably real. Holding Costco Wholesale from the start of the year would have returned 30.2%, including dividends.
- Sat 14 Nov | Pluang | Costco uses AI to auto-reorder drugs, keeping p...
  https://pluang.com/en/news-feed/costco-ai-pemesanan-obat-otomatis-tingkatkan-pertumbuhan-farmasi
  (page: did not load (403))
## NFLX  (8 leads)
- Fri 13 Nov | Digital Spy | Beloved Netflix hit shares major new-season update which breaks record for the streamer
  https://www.digitalspy.com/tv/a74427151/netflix-virgin-river-new-season-update-record/
  > One of Netflix’s most successful shows has reached a landmark for the very first time. The giant streaming platform is home to popular programmes such as Stranger Things, Squid Game and Money Heist.
- Fri 13 Nov | Radio & Television Business Report | ‘GTN’ or Netflix Stock: What’s The Better Value Option?
  https://rbr.com/gtn-or-netflix-stock-whats-the-better-value-option/
  (page: only 47 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | Foreign Policy Journal | Netflix (NASDAQ: NFLX) Stock Trades At A Decade-Low Valuation As Its Advertising Business Holds The Key To A Potential Rebound
  https://www.foreignpolicyjournal.com/2026/11/13/netflix-nasdaq-nflx-stock-trades-at-a-decade-low-valuation-as-its-advertising-business-holds-the-key-to-a-potential-rebound/
  > Netflix (NASDAQ: NFLX) is trading at just 17.6 times its trailing twelve-month earnings, a steep discount to the S&P 500’s multiple of 21.9 times. That gap is not trivial: at the close of September, Netflix’s price-to-earnings ratio of 19.5 was lower than at every quarter-end since late 2016 except one.
## INTC  (8 leads)
- Sat 14 Nov | MarketBeat | Bernicke Wealth Management Ltd. Makes New Investment in Intel Corporation $INTC
  https://www.marketbeat.com/instant-alerts/filing-bernicke-wealth-management-ltd-makes-new-investment-in-intel-corporation-intc-2026-11-14/
  > Bernicke Wealth Management Ltd. Makes New Investment in Intel Corporation $INTC - Bernicke Wealth Management opened a new Intel position in the third quarter, buying 10,574 shares worth about $1.27 million. Institutional investors and hedge funds collectively own 64.53% of Intel’s stock.
- Sat 14 Nov | MarketBeat | Intel Corporation $INTC Position Raised by Aberdeen Group plc
  https://www.marketbeat.com/instant-alerts/filing-intel-corporation-intc-position-raised-by-aberdeen-group-plc-2026-11-14/
  > Intel Corporation $INTC Position Raised by Aberdeen Group plc - Aberdeen Group increased its Intel stake by 34.7% in the third quarter, adding 1.23 million shares to hold about 4.76 million shares valued at $572.6 million.
- Sat 14 Nov | Finimize | Soros Fund Management Loaded Up On Intel, Filings Show
  https://finimize.com/content/soros-fund-management-loaded-up-on-intel-filings-show
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sat 14 Nov | Investing.com | Soros Fund ramps up Intel stake to over $340 million in third quarter By Reuters
  https://www.investing.com/news/stock-market-news/soros-fund-ramps-up-intel-stake-to-over-340-million-in-third-quarter-5026774
  (page: did not load (403))
- Sat 14 Nov | BigGo Finance | Soros Fund's Q3 Holdings Shake-Up: Intel Stake Surges More Than 27-Fold, New SK Hynix Position, Nvidia Trimmed
  https://finance.biggo.com/news/8ea2085b-1a4d-4780-b2ac-0b90110bc1ef
- Sat 14 Nov | Pluang | Lawsuit filed against Intel over alleged mislea...
  https://pluang.com/en/news-feed/peringatan-penggugat-kelas-intel-dampak-negatif-hasil-q3-2026
- Fri 13 Nov | Reuters | Soros Fund ramps up Intel stake to over $340 million in third quarter
  https://www.reuters.com/legal/legalindustry/soros-fund-ramps-up-intel-stake-over-340-million-third-quarter-2026-11-13/
- Fri 13 Nov | Yahoo Finance | Why Intel Stock Slumped Today
  https://finance.yahoo.com/markets/stocks/articles/why-intel-stock-slumped-today-230951500.html
## LLY  (8 leads)
- Sat 14 Nov | TIKR.com | Trump Touts Lilly’s “$3.5 Billion” Obesity Drug Plant, Its 10th New U.S. Site Since 2020
  https://www.tikr.com/blog/trump-touts-lillys-3-5-billion-obesity-drug-plant-its-10th-new-u-s-site-since-2020?
  > - Eli Lilly broke ground on Nov. 12 on a $3.5 billion plant for injectable obesity drugs, and President Trump shared the news. - The plant won’t run until 2031, so Lilly is paying now for sales years away. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sat 14 Nov | Simply Wall St | Eli Lilly (LLY) Faces New Vision Loss Lawsuits As Pipeline Milestones Keep Coming
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-faces-new-vision-loss-lawsuits-as-pipeline-mil
  > Eli Lilly (NYSE:LLY) faces new lawsuits alleging its GLP-1 drug Mounjaro causes irreversible vision loss linked to NAION. Regulators in several countries issued safety updates on GLP-1 eye risks while US product labels for Mounjaro remain unchanged. Lilly expanded its obesity and neuroscience pipeline work through fresh collaboration milestones with Fauna Bio and VectorY.
- Sat 14 Nov | KuCoin | Eli Lilly CEO Doubts AI Can Cure Cancer Within 10 Years
  https://www.kucoin.com/news/flash/eli-lilly-ceo-doubts-ai-can-cure-cancer-within-10-years
  > IT Home, November 14: On November 12, Dave Ricks, Chairman and CEO of Eli Lilly, posted a tweet on X responding to Dario Amodei, CEO of Anthropic, who predicted that AI would cure diseases like cancer in less than ten years. Ricks called the vision "appealing" but unlikely to be realized.
Read 88 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: PHDC, CLHO, ALCN.
