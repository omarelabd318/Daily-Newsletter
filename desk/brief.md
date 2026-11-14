# Desk brief, Saturday, November 14, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 349s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-13 (19.3); Treasury yields to 2026-11-13 (10-year 5.15%).
- **valuation**: ok in 22s (GitHub Actions). LLY: $1.36tn, P/E (last 12 months) 44.7, Forecast P/E (fiscal 2026) 40.5 (the four quarters to Sep 2026)
- **movers**: ok in 19s (GitHub Actions). Market values: 18 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 53.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 50 stocks, k 16.5%, median P/E 10.8; cheapest MASR +71%, PHAR +51%, EXPA +49%; dearest ARAB -61%, MOIN -66%, BTFH -68%
- **views**: ok in 0s (GitHub Actions). 2026-11-04-fert-gas: open -> on track
- **results**: ok in 61s (GitHub Actions). 
- **news**: ok in 126s (GitHub Actions). 
- **leads**: ok in 103s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 29 failed, 0 needed a retry (fetch_intraday.py); api.polygon.io: 25 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

## What moved (latest close against the one before)
- EGX30 52,023.37 (-0.91%); EGX70 EWI 18,527.43 (+0.43%); USD/EGP 53.50 (-0.22%); Gold 21K 5,950.00 (-2.70%); Brent 95.90 (+3.39%); S&P 500 7,592.40 (-0.35%); Nasdaq 25,366.09 (-0.39%); Bitcoin 69,007.00 (-6.17%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): AVGO +5.5%, NVDA -4.3%, EAST +4.2%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 80, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (13.4% over) and its 200-day (12.0% over), though the 50-day is still below the 200-day; RSI 74, stretched after a run: above 70.
    - GOOGL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 42, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (23.0% under) and its 200-day (18.7% under), though the 50-day is still above the 200-day; RSI 26, washed out: below 30.
    - ORCL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 48, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).

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
- Fri 13 Nov | صحيفة الحدث | جمعية الرواد الشبابية بجازان تحتفي بتخريج 522شابًا وفتاة ضمن مشروع "مهارات المستقبل"
  https://al-hadath.com/local-news/102684/جمعية-الرواد-الشبابية-بجازان-تحتفي-بتخريج-522شابًا-وفتاة-ضمن-مشروع-مهارات-المستقبل
- Fri 13 Nov | alraynews.net | جمعية الرواد الشبابية بجازان تحتفي بتخريج 522 شابًا وفتاة ضمن مشروع «مهارات المستقبل»
  https://alraynews.net/6762050.htm
- Fri 13 Nov | كود | فاس جمعات أطباء من المغرب والعالم وجراح برازيلي من الرواد فجراحة الأذن بالمنظار
  https://www.goud.ma/فاس-جمعات-أطباء-من-المغرب-والعالم-وجرا-1053891/
- Fri 13 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | التصنيع تعلن موافقة هيئة المنافسة على استحواذ تحويل القابضة على حصصها في الرواد التحويلية الصناعية
  https://www.argaam.com/ar/article/articledetail/id/1919988
## HDBK +5.8%  Housing & Development Bank
- Fri 13 Nov | بنكي | بنك التعمير والإسكان يؤكد أهمية تكامل الرقمنة والتمويل لدعم النمو بمؤتمر «الناس والبنوك»
  https://www.bankygate.com/202507
- Fri 13 Nov | شبكة تواصل الإخبارية | بنك التعمير والإسكان يتيح ربط الشهادات الادخارية أونلاين عبر تطبيق HDB Mobile
  https://twaslnews1.twaslnews.com/7625065/
- Fri 13 Nov | https://ekhbary24.com/ | البنك الأهلي وبنك مصر يرفعان عائد الشهادات إلى 18.85% الأحد
  https://ekhbary24.com/article/51830
- Thu 12 Nov | اتحاد بنوك مصر | بنك التعمير والاسكان يتصدر ارتفاعات أسهم البنوك بالبورصة بنهاية تعاملات اليوم
  https://febanks.com/1357557/
## INEG -6.3%  Integrated Engineering Group
- Wed 11 Nov | معلومات مباشر | تم ايقاف الورقة المالية - EGS3E3B1C014 - المجموعة المتكاملة للأعمال الهندسية لمدة 10 دقائق لتجاوزها نسبة 5%
  https://www.mubasher.info/news/4700438/تم-ايقاف-الورقة-المالية-EGS3E3B1C014-المجموعة-المتكاملة-للأعمال-الهندسية-لمدة-10-دقائق-لتجاوزها-نسبة-5-/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
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
- Fri 13 Nov | Simply Wall St | Nu (NU) Stock Jumps As Q3 Earnings Strengthen Profit Case Amid Credit Risk
  https://simplywall.st/stocks/us/banks/nyse-nu/nu-holdings/news/nu-nu-stock-jumps-as-q3-earnings-strengthen-profit-case-amid
  > Nu Holdings came into this Q3 2026 report with a mixed tape. The stock was down double digits over the past month, yet it ripped 11.8% higher today to close at US$13.22.
- Fri 13 Nov | Yahoo Finance | Nu Holdings (NU) Stock Rallies On Q3 Results As Profit Strength Counters Credit Risk
  https://finance.yahoo.com/markets/stocks/articles/nu-holdings-nu-stock-rallies-231522054.html
  > Nu Holdings came into this Q3 2026 report with a reputation as the high growth Latin American fintech that pairs rapid expansion with rich profitability. The stock had cooled over the past three months, yet today it rose 11.8% as investors reacted to the headline numbers.
- Fri 13 Nov | The Globe and Mail | Stock Market Today, Nov. 13: Nu Holdings Surges on Record Q3 Earnings Beat Driven by Strong Revenue
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8829813/stock-market-today-nov-13-nu-holdings-surges-on-record-q3-earnings-beat-driven-by-strong-revenue/
  > Nu Holdings(NYSE:NU), a Latin American digital bank and consumer finance platform, closed at $13.21, up 11.71%. Premarket earnings beat forecasts and management commentary on Mexico and Colombia kept investors watching growth and efficiency next. Trading volume reached 143.2M shares, coming in about 74% above its three-month average of 82.1M shares.
- Fri 13 Nov | The Motley Fool | Stock Market Today, Nov. 13: Nu Holdings Surges on Record Q3 Earnings Beat Driven by Strong Revenue
  https://www.fool.com/coverage/stock-market-today/2026/11/13/stock-market-today-nov-13-nu-holdings-surges-on-record-q3-earnings-beat-driven-by-strong-revenue/
  > Nu Holdings (NU +11.75%), a Latin American digital bank and consumer finance platform, closed at $13.21, up 11.71%. Premarket earnings beat forecasts and management commentary on Mexico and Colombia kept investors watching growth and efficiency next.
## CBRS +11.2%  Cerebras Systems
- Sat 14 Nov | Simply Wall St | Cerebras Systems (CBRS) Stock Jumps As Q3 Results Fuel Growth Conviction
  https://simplywall.st/stocks/us/semiconductors/nasdaq-cbrs/cerebras-systems/news/cerebras-systems-cbrs-stock-jumps-as-q3-results-fuel-growth/amp
  > Cerebras Systems released its Q3 2026 report and the stock rose 11.2% in the first full trading session to US$108.72. This is a significant move for a business that is still losing money, which indicates that the reaction was driven by belief in the growth story.
- Fri 13 Nov | Simply Wall St | Has Cerebras Systems (CBRS) Fallen Enough To Shrink Its Sales Premium?
  https://simplywall.st/stocks/us/semiconductors/nasdaq-cbrs/cerebras-systems/news/has-cerebras-systems-cbrs-fallen-enough-to-shrink-its-sales
  > Cerebras Systems shares have had a rough spell in 2026, and the slide so far this year raises a simple question for investors who care about valuation. Is the current price tag on Cerebras stock still in line with what the business is generating in sales?
- Fri 13 Nov | MarketBeat | CBRS News Today | Why did Cerebras Systems stock go up today?
  https://www.marketbeat.com/stocks/NASDAQ/CBRS/news/
  (page: did not load (403))
- Fri 13 Nov | Yahoo Finance | Cerebras Systems (CBRS) Stock Jumps As Q3 Results Revive Valuation Debate
  https://finance.yahoo.com/markets/stocks/articles/cerebras-systems-cbrs-stock-jumps-231157278.html
  > Cerebras Systems rose 11.1% to US$108.59 after posting Q3 2026 numbers, a sharp rebound for a stock that fell over the past month and quarter.
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
- Sun 08 Nov | آراب فاينانس | %104 نموًا بأرباح مصر للألومنيوم في ثلاثة أشهر
  https://www.arabfinance.com/ar/news/newdetails/أرباح-مصر-للألومنيوم-في-ثلاثة-أشهر
  > آراب فاينانس: أعلنت شركة مصر للألومنيوم (EGAL)، عن مؤشرات نتائج الاعمال غير مدققة عن الفترة المنتهية فى 30/09/2026، والتي أظهرت تحقيق صافي ربح بلغ 4.928 مليار جنيه مقابل صافي ربح بلغ 2.415 مليار جنيه عن نفس الفترة من العام السابق، بنسبة نمو بلغت 104%، حسبما ذكرت الشركة في بيانها المرسل إلى البورصة المصرية.
- Sun 08 Nov | شبكة تواصل الإخبارية | أرباح مصر للألومنيوم تقفز إلى 4.93 مليار جنيه.. تضاعف الأرباح خلال 3 أشهر
  https://twaslnews1.twaslnews.com/7312425/
- Sun 08 Nov | اخبارك نت | أرباح مصر للألومنيوم تقفز 104% إلى 4.93 مليار جنيه خلال الربع الأول من العام المالي الجاري | أموال الغد
  https://www.akhbarak.net/news/details/49536242/4/أرباح-مصر-للألومنيوم-تقفز-104-إلى-4-93-مليار-جنيه-خلال-الربع-الأول-من-العام-المالي-الجاري-أموال-الغد
  > أظهرت نتائج أعمال شركة مصر للألومنيوم ارتفاع صافي أرباح الشركة خلال الربع الأول من العام المالي 2026/2027 بنسبة 104% على أساس سنوي. أوضحت الشركة، في نتائجها المالية المرسلة إلى بورصة مصر، أنها حققت صافي ربح بعد الضرائب بلغ 4.93 مليار جنيه خلال الفترة من يوليو حتى نهاية سبتمبر 2026، مقابل 2.41 مليار جنيه خلال الفترة المقارنة من العام المالي السابق.
- Sun 08 Nov | جريدة البورصة | "مصر للألومنيوم" تضاعف أرباحها في الربع الأول إلى 4.93 مليار جنيه
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: SWDY, JUFO, EAST, EFIH, EMFD, BQDC.
- Already recorded: COMI, ETEL.

## Coming up (seven days)
- 2026-11-16 CLHO results (expected)
- 2026-11-16 PHDC results (expected)
- 2026-11-16 XOM dividend
- 2026-11-17 EGAL dividend
- 2026-11-17 NVDA results (expected)
- 2026-11-18 EAST results (expected)
- 2026-11-18 EFIH results (expected)
- 2026-11-18 HRHO results (expected)
- 2026-11-19 MSFT dividend

## Views
- due 2026-11-13: Chip stocks stay under pressure into Apple's results (on track)
- due 2026-11-13: Higher rates protect CIB's margins (on track)
- due 2026-11-20: Brent stays below $105 while Iran talks continue (open)
    2026-11-04-fert-gas: open -> on track

## Fair value
- Changed since the last run: MASR +86% -> +71% (medium -> medium); PHDC +32% -> +24% (high -> medium); CSAG +35% -> +23% (low -> medium); ETEL +23% -> +20% (medium -> low); HDBK +2% -> -14% (medium -> low); ABUK +19% -> -33% (high -> low); CANA +0% -> -34% (low -> low); LCSW -46% -> -47% (medium -> low); ARAB new at -61%.
- In the ten cheapest or dearest with no note: MCQE, SCEM, ADIB, CSAG, ARCC, AMOC, MTIE, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-14. Open each story before using it.
## COMI  (8 leads)
- Fri 13 Nov | بنكي | بطاقة CIB noon الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/414
  > - كاش باك 5% - معدل الفائدة السنوي الفعلي 28 عرض ساري على البطاقة تقسيط بدون فوائد 17 · خصومات 12 · 4 بينتهوا خلال أيام - تقسيط بدون فوائد Dream 2000 دريم 2000 - تقسيط المشتريات لمدة 12 شهرًا بدون فوائد Audio Technology شرف دي جي مرتبة بالأقرب انتهاءً · 6 من 28
- Fri 13 Nov | بنكي | بطاقة كاش باك (Cashback) الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/405
  (same wording as the بنكي story above: one source, not two)
- Fri 13 Nov | بنكي | بطاقة Swype 12 — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/416
  (same wording as the بنكي story above: one source, not two)
## TMGH  (3 leads)
- Fri 13 Nov | Billionaires.Africa | Investor Memo: The $200 Billion Question — Hisham Talaat Moustafa's TMG, Egypt's Four New Megaprojects, and Who Will Share the Proceeds
  https://www.billionaires.africa/2026/11/13/investor-memo-the-200-billion-question-hisham-talaat-moustafas-tmg-egypts-four-new-megaprojects-and-who-will-share-the-proceeds/
  > Investor Memo: The $200 Billion Question — Hisham Talaat Moustafa's TMG, Egypt's Four New Megaprojects, and Who Will Share the Proceeds Talaat Moustafa Group has agreed four projects with Egypt's government worth about $200 billion, nearly 60 times its market value.
- Thu 12 Nov | Billionaires.Africa | Egyptian billionaire Hisham Talaat Moustafa's $200 billion TMG deal draws military interest
  https://www.billionaires.africa/2026/11/12/egyptian-billionaire-hisham-talaat-moustafas-200-billion-tmg-deal-draws-military-interest/
  > Egypt's military establishment is pushing for a share of the roughly $200 billion in development projects that Egyptian billionaire Hisham Talaat Moustafa's Talaat Moustafa Group Holding Co. agreed with the government in October, Africa Intelligence reported on Nov. The four projects carry total planned investment of about 11 trillion Egyptian pounds ($199 billion).
- Thu 12 Nov | Africa Intelligence | Egypt • Military seeks a slice of real estate giant TMG's mega-project
  https://www.africaintelligence.com/north-africa/2026/11/12/military-seeks-a-slice-of-real-estate-giant-tmg-s-mega-project,110919102-art
  > Military seeks a slice of real estate giant TMG's mega-project Published on 12.11.2026 at 05:40 GMT The $200bn deal announced in October between Talaat Moustafa Group and the Egyptian government has whetted the military establishment's appetite.
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
## SWDY  (8 leads)
- Thu 12 Nov | خاص عن مصر | إيرادات "السويدي إليكتريك" تقفز إلى 263 مليار جنيه في 9 أشهر والأرباح ترتفع 16%
  https://aboutmsr.com/إيرادات-السويدي-إليكتريك-تقفز-إلى-263-مل/
  > سجلت شركة «السويدي إليكتريك» نموًا في إيراداتها المجمعة بنسبة 31.7% خلال أول تسعة أشهر من عام 2026، لتصل إلى 263.03 مليار جنيه، مقابل 199.7 مليار جنيه خلال الفترة نفسها من العام الماضي، مدعومة بزيادة حجم أعمالها، فيما ارتفع صافي الأرباح بنسبة 16.07% إلى 16.4 مليار جنيه. [Figures on the page: standalone; consolidated; nine months; one quarter. Check which one each figure is.]
- Thu 12 Nov | ايكونومي بلس | أرباح السويدي إليكتريك ترتفع 35% في الربع الثالث إلى 5.4 مليار جنيه
  https://economyplusme.com/ar/news/34144
  > أرباح السويدي إليكتريك ترتفع 35% في الربع الثالث إلى 5.4 مليار جنيه ارتفع صافي ربح شركة السويدي إليكتريك بعد خصم حقوق الأقلية والضرائب خلال الربع الثالث من عام 2026 بنسبة 35.1% على أساس سنوي، ليصل إلى نحو 5.4 مليار جنيه، مقابل 3.98 مليار جنيه خلال الفترة المقارنة من عام 2025. [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Thu 12 Nov | آراب فاينانس | السويدي إليكتريك ترتفع بأرباحها في تسعة أشهر
  https://www.arabfinance.com/ar/news/newdetails/السويدي-إليكتريك-ترتفع-بأرباحها-في-تسعة-أشهر
  (page read: it never names the company, so probably not about it: skip)
## FWRY  (2 leads)
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية
  https://www.fintechgate.net/257376
  > سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية واصل سهم شركة «فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية» تعزيز مكاسبه في البورصة المصرية للأسبوع الثاني على التوالي خلال تعاملات شهر نوفمبر الحالي، مستفيدًا من موجة الصعود التي شهدتها السوق وارتفاع مؤشراتها الرئيسية والثانوية، وسط أداء إيجابي للأسهم القيادية وتحسن شهية المستثمرين للشراء.
- Thu 12 Nov | Alkalima Online | Whish Money تعتمد Featurespace من فيزا لتعزيز قدراتها على التصدي الفوري للاحتيال
  https://www.alkalimaonline.com/news.aspx?id=960765
  > Whish Money تعتمد Featurespace من فيزا لتعزيز قدراتها على التصدي الفوري للاحتيال Thursday, November 12, 2026 في 12 نوفمبر 2026, أعلنت شركة «Whish Money»، الرائدة في مجال التكنولوجيا المالية، عن تعاونها مع فيزا لاعتماد Featurespace المدعوم بالذكاء الاصطناعي للوقاية من الاحتيال، بهدف تعزيز قدراتها على رصد عمليات الاحتيال والخداع عبر قنوات دفع متعددة في لبنان.
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
## HRHO  (7 leads)
- Fri 13 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | Citywire | Standard Bank, EFG Hermes and Bravura among 2026 AGF award winners
  https://citywire.com/za/news/standard-bank-efg-hermes-and-bravura-among-2026-agf-award-winners/a2503332
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «إي إف جي القابضة» يقفز 6.64% ويضيف 2.27 مليار جنيه لقيمته السوقية ببورصة مصر خلال أسبوع
  https://www.fintechgate.net/257381
  > سهم «إي إف جي القابضة» يقفز 6.64% ويضيف 2.27 مليار جنيه لقيمته السوقية ببورصة مصر خلال أسبوع عزز سهم مجموعة «إي إف جي القابضة» مكاسبه في البورصة المصرية خلال تعاملات الأسبوع الماضي، مستفيدًا من تحسن أداء أسهم قطاع الخدمات المالية غير المصرفية، وسط نشاط ملحوظ في التداولات على السهم، بالتزامن مع الارتفاع الجماعي لمؤشرات السوق.
## JUFO  (4 leads)
- Thu 12 Nov | Investing.com | Earnings call transcript: Juhayna posts record Q3 2026 sales as stock slips
  https://www.investing.com/news/transcripts/earnings-call-transcript-juhayna-posts-record-q3-2026-sales-as-stock-slips-93CH-5021816
  (page: did not load (403))
- Thu 12 Nov | Investing.com | جهينة للصناعات الغذائية تسجل مبيعات قياسية في الربع الثالث من 2026 وسط تراجع السهم
  https://sa.investing.com/news/transcripts/article-93CH-3439242
  (page: did not load (403))
- Thu 12 Nov | شبكة تواصل الإخبارية | 2.03 مليار جنيه أرباح جهينة .. ماذا تعني طفرة الأغذية لسياحة الفنادق بمصر؟
  https://twaslnews1.twaslnews.com/7553230/
  (page: did not load (403))
- Thu 12 Nov | معلومات مباشر | العنوان : جهينة للصناعات الغذائية (JUFO.CA) - بيان من الشركةاسم الشركة: جهينة للصناعات الغذائيةكود الترقيم الدولي: EGS30901C010كود رو
  https://www.mubasher.info/news/4701286/العنوان-جهينة-للصناعات-الغذائية-JUFO-CA-بيان-من-الشركةاسم-الشركة-جهينة-للصناعات-الغذائيةكود-الترقيم-الدولي-EGS30901C010كود-رو/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## MFPC  (1 leads)
- Thu 12 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EAST  (7 leads)
- Thu 12 Nov | اخبارك نت | «MSCI» تضم المصرية للاتصالات إلى مؤشرها القياسي وتستبعد الشرقية للدخان في مراجعة نوفمبر | أموال الغد
  https://akhbarak.net/news/details/49543838/4/msci-تضم-المصرية-للاتصالات-إلى-مؤشرها-القياسي-وتستبعد-الشرقية-للدخان-في-مراجعة-نوفمبر-أموال-الغد
  > أعلنت مؤسسة مورجان ستانلي كابيتال إنترناشيونال «MSCI» انضمام سهم الشركة المصرية للاتصالات إلى مؤشر MSCI Egypt، ضمن مؤشرات MSCI العالمية القياسية (Global Standard Indexes)، مقابل استبعاد سهم الشركة الشرقية للدخان، وذلك في إطار نتائج المراجعة الدورية لمؤشرات الأسواق العالمية لشهر نوفمبر 2026.
- Thu 12 Nov | مانكيش نت | ارتفاع أرباح الشرقية للدخان إلى 8.98 مليار جنيه في 9 أشهر
  https://mangish.net/ارتفاع-أرباح-الشرقية-للدخان-إلى-8-98-مليا/
  > أفادت شركة الشرقية – إيسترن كومباني بأنها قد أنجزت أعمالها المجمعة عن التسعة أشهر التي انتهت في 30 سبتمبر 2026، وذلك وفقًا للبيان الذي تم إرساله إلى البورصة المصرية يوم الخميس الموافق 12 نوفمبر 2026. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Thu 12 Nov | الجريدة العقارية | أرباح الشرقية للدخان ترتفع إلى 8.98 مليار جنيه خلال أول 9 أشهر من 2026
  https://www.aleqaria.com.eg/post/details/357800/أرباح-الشرقية-للدخان
  (page: only 67 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 12 Nov | Pioneers Misr | مورجان ستانلي تستبعد سهم «الشرقية للدخان» من مؤشر مصر القياسي وتضيف سهم «المصرية للاتصالات»
  https://pioneersmisr.com/123554/
  > أعلنت مؤسسة مورجان ستانلي كابيتال إنترناشيونال «MSCI» انضمام سهم الشركة المصرية للاتصالات إلى مؤشر «MSCI Egypt» ضمن مؤشرات الأسواق العالمية القياسية، مقابل استبعاد سهم الشركة الشرقية للدخان، وذلك في إطار المراجعة الدورية لمؤشرات الأسواق العالمية لشهر نوفمبر 2026.
- Thu 12 Nov | ايكونومي بلس | بنهاية نوفمبر.. "MSCI" تضم "المصرية للاتصالات" إلى مؤشرها القياسي وتستبعد "الشرقية للدخان"
  https://economyplusme.com/ar/news/34126
- Thu 12 Nov | بوابة بلوم | المصرية للاتصالات تنضم إلى مؤشر MSCI مع استبعاد الشرقية للدخان
  https://bloom-gate.com/أسواق/المصرية-للاتصالات-تنضم-إلى-مؤشر-msci-مع-اس/
- Thu 12 Nov | - سي نيوز | مورغان ستانلي تجري تغييرات على مؤشرات بورصة مصر.. ترقية المصرية للاتصالات وخفض تصنيف إيسترن كومباني
  https://www.cnewsarab.com/tag/مورغان-ستانلي-تجري-تغييرات-على-مؤشرات/
## EFIH  (8 leads)
- Fri 13 Nov | Pioneers Misr | إيرادات إي فاينانس الأرشيف - Pioneers Misr
  https://pioneersmisr.com/tag/إيرادات-إي-فاينانس/
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
  https://www.masrawy.com/news/news_egypt/details/2026/11/13/3078330/خالد-أبو-بكر-يهاجم-تصريحات-حمدين-صباحي-بشأن-بيع-أراضي-مصر-وبنك-القاهرة?amp
  > خالد أبو بكر يهاجم تصريحات حمدين صباحي بشأن بيع أراضي مصر وبنك القاهرة علق المحامي خالد أبو بكر على تصريحات حمدين صباحي بشأن رفض بيع أراضي مصر وبنك القاهرة، مطالبًا إياه بالتركيز على الحديث في تخصصه، والابتعاد عن الشعارات التي وصفها بأنها باتت باهتة.
- Fri 13 Nov | مصر تايمز | خالد أبو بكر يهاجم حمدين صباحي بسبب شعارات "بيع مصر وبنك القاهرة"
  https://www.masrtimes.com/777117
  > خالد أبو بكر يهاجم حمدين صباحي بسبب شعارات "بيع مصر وبنك القاهرة" هاجم الإعلامي والمحامي الدولي خالد أبو بكر، السياسي حمدين صباحي، بعد انتقاداته لتوجهات الدولة الاقتصادية، ورفع شعارات "لا لبيع أرض مصر ولا لبيع بنك القاهرة".
## AMOC  (1 leads)
- Fri 13 Nov | جريدة باور نيوز الاخبارية | غدا.. عمومية “أموك” تبحث تعديل 6 مواد بالنظام الأساسي
  https://powernews.cc/?p=293946
  > دعت شركة الإسكندرية للزيوت المعدنية “أموك”، مساهميها غدا السبت لحضور الجمعية العامة غير العادية للنظر في تعديل 6 مواد بنظامها الأساسي. وستنظر العمومية في تعديل المواد أرقام (7، 21، 28، 46، 56) من النظام الأساسي للشركة. وبدأت شركة الإسكندرية للزيوت المعدنية “أموك”، التشغيل التجريبي لمشروع معالجة الغازات الحامضية.
## SKPC  (2 leads)
- Thu 12 Nov | www.youlyou.com | كيف ساهمت خامات البلاستيك المستوردة في زيادة مبيعات سيدبك إلى 14.7 مليار جنيه؟
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
- Sat 14 Nov | BBN Times | FTSE 100 Today: London Soars 10,902.56 as Aviva and Energy Stocks Shrug Off Nvidia and Microsoft Turmoil
  https://www.bbntimes.com/global-economy/ftse-100-today-london-soars-10-902-56-as-aviva-and-energy-stocks-shrug-off-nvidia-and-microsoft-turmoil
  > FTSE 100 Today: London Soars 10,902.56 as Aviva and Energy Stocks Shrug Off Nvidia and Microsoft Turmoil Britain’s blue-chip index rose 0.4% on Friday, finishing a 2.2% weekly gain as insurers, utilities and oil majors offset another sell-off in US technology stocks and a global Microsoft outage that disrupted UK public services.
- Fri 13 Nov | Stocks Down Under | Microsoft (NASDAQ:MSFT) Stock Falls as Global Outage Hits Outlook, Teams and Copilot
  https://stocksdownunder.com/microsoft-stock-outlook-teams-copilot-outage/
  (page: did not load (403))
- Fri 13 Nov | Bloomberg.com | US Futures Gain With Microsoft Outage, Producer Prices in Focus
  https://www.bloomberg.com/news/articles/2026-11-13/us-futures-gain-with-microsoft-outage-producer-prices-in-focus
  (page: did not load (403))
## NVDA  (8 leads)
- Sat 14 Nov | The New York Times | Despite Nvidia’s Drop, Stocks Push Ahead
  https://www.nytimes.com/2026/11/13/business/nvidia-turmoil-stock-market.html
  (page: did not load (403))
- Sat 14 Nov | Yahoo Finance | Exclusive-Ex-Nvidia CEO misled top lawyer on affair with Chinese businesswoman, sources say
  https://finance.yahoo.com/markets/stocks/articles/exclusive-ex-nvidia-ceo-misled-002638424.html
  > Cherney and Jeffrey Dastin
- Sat 14 Nov | Mashable | Nvidia stock plunges as CEO Jensen Huang resigns: How low it might go
  https://mashable.com/tech/nvidia-stock-plunges-ceo-jensen-huang-resigns-how-low-did-it-go
  > Nvidia CEO Jensen Huang has just resigned from the company he co-founded amid reports of two alleged affairs, including one with a woman that U.S. intelligence believes is a Chinese spy, according to a bombshell New York Times report.
- Fri 13 Nov | Jessica Yellin | Substack | Nvidia: “The Story That Will Swallow All Stories”
  https://newsnotnoisejessicayellin.substack.com/p/nvidia-the-story-that-will-swallow
  (page: did not load (403))
- Fri 13 Nov | Yahoo Finance | Wall Street stocks mostly lower as Nvidia extends slump
  https://finance.yahoo.com/markets/stocks/articles/wall-street-stocks-mostly-lower-230704278.html
- Fri 13 Nov | Barron's | Nvidia Has Real Problems—but Don’t Fall For Fear Mongering
  https://www.barrons.com/articles/nvidia-balance-sheet-math-f210c291
- Fri 13 Nov | Marketplace.org | What will happen at Nvidia's impending earnings call?
  https://www.marketplace.org/story/2026/11/13/nvidias-upcoming-earnings-call-could-spell-trouble
- Fri 13 Nov | CNN | Nvidia’s week of chaos, explained
  https://www.cnn.com/2026/11/13/business/nvidia-jensen-huang-affair-fallout-vis
## AMZN  (8 leads)
- Sat 14 Nov | ad-hoc-news.de | Amazon's Shopping Ambitions Stretch From a Product Database to the Courtroom
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-shopping-ambitions-stretch-from-a-product-database-to-the-courtroom/70507135
  > A federal judge in the United States cleared the way on Wednesday for a group of plaintiffs to proceed collectively in their suit against Amazon Photos, according to Bloomberg Law. The case centers on allegations that the service's facial recognition technology ran afoul of Illinois' biometric privacy statute.
- Fri 13 Nov | Pluang | Amazon launches new Kindle Colorsoft with color display, premium design, and $290+ price tag
  https://pluang.com/en/news-feed/amazon-kindle-colorsoft-peluncuran-produk-baru
  (page: did not load (403))
- Fri 13 Nov | GuruFocus | Fermi Secures 600 MW Power Deal with Amazon (AMZN), Marking Rene
  https://www.gurufocus.com/news/9198708/fermi-secures-600-mw-power-deal-with-amazon-amzn-marking-renewed-partnership
  (page: did not load (403))
## GOOGL  (8 leads)
- Fri 13 Nov | ad-hoc-news.de | Alphabet's AI Spending Spree Faces Its Reckoning as HSBC and JPMorgan Diverge
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/alphabet-s-ai-spending-spree-faces-its-reckoning-as-hsbc-and-jpmorgan-diverge/70507103
  > HSBC analyst Paul Rossington is betting Alphabet shares can recover from their recent slide, publishing a price target of $360 on the stock today. His bullish case rests on the pace of Google Cloud's expansion — provided the company can eventually convert its hefty infrastructure outlays into stronger free cash flow. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Fri 13 Nov | CEOWORLD magazine | Billionaire Larry Page to Sell $148 Million of Alphabet Stock: What the Filing Shows
  https://ceoworld.biz/2026/11/14/billionaire-larry-page-to-sell-148-million-of-alphabet-stock-what-the-filing-shows/
  > Three trusts tied to the Google co-founder have filed to sell about half a million shares. The more consequential seller of Alphabet stock this year is Alphabet. Trusts linked to Larry Page have given notice that they intend to sell about $148.3 million of Alphabet stock. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Fri 13 Nov | Investing.com Australia | David Taylor reports Alphabet stock purchases By Investing.com
  https://au.investing.com/news/stock-market-news/david-taylor-reports-alphabet-stock-purchases-93CH-4770254
  (page: did not load (403))
## META  (8 leads)
- Fri 13 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Stock Jumps 2.9% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-meta-platforms-nasdaq-meta-stock-jumps-29-heres-why-2026-11-13/
  > Meta Platforms (NASDAQ:META) Stock Jumps 2.9% - Here's Why - Meta shares rose 2.9% in Friday’s mid-day trading to $641.69, on volume about 17% below the daily average. - The company’s latest quarterly results beat estimates: earnings were $7.40 per share versus $6.54 expected, while revenue reached $64.6 billion and grew 26.1% year over year.
- Fri 13 Nov | Investing.com | Meta tests prediction-market app for employees, WSJ reports
  https://www.investing.com/news/stock-market-news/meta-tests-predictionmarket-app-for-employees-wsj-reports-5026398
  (page: did not load (403))
- Fri 13 Nov | Investing.com | Meta employees test prediction-market app, WSJ reports By Reuters
  https://www.investing.com/news/stock-market-news/meta-employees-test-predictionmarket-app-wsj-reports-5026444
  (page: did not load (403))
## TSLA  (8 leads)
- Sat 14 Nov | Yahoo Finance | Zero To Sixty: Tesla Winds Down Cybertruck, Pulls Model Y Variant While Rivian, Lucid Chase Volumes
  https://finance.yahoo.com/markets/stocks/articles/zero-sixty-tesla-winds-down-004556808.html
  > - Elon Musk this week noted a larger order backlog than remaining production capacity and said Tesla would produce the Cybertruck until the end of summer 2027.
- Fri 13 Nov | MarketBeat | Tesla (NASDAQ:TSLA) Shares Down 1.8% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-tesla-nasdaq-tsla-shares-down-18-heres-why-2026-11-13/
  > Tesla (NASDAQ:TSLA) Shares Down 1.8% - Here's Why - Tesla shares fell 1.8% Friday to $390.22, with trading volume 36% below the average session volume.
- Fri 13 Nov | Investor's Business Daily | SpaceX, Tesla Merger Puts Musk At Forefront Of 'Revolutionary' Tech, Analyst Says
  https://www.investors.com/news/spacex-tesla-merger-grok-optimus-robotics-engineering-starship-spcx-stock-tsla/
  > The much-touted merger between SpaceX and Tesla seems almost inevitable at this point. Some analysts project the mega-combination could come as early as next month. Copyright ©2026 Investor's Business Daily, LLC.
## JPM  (8 leads)
- Sat 14 Nov | Financial-News.co.uk | JPMorgan Declares Preferred Stock Dividends on Three Series
  https://www.financial-news.co.uk/jpmorgan-declares-preferred-stock-dividends-on-three-series/
  > JPMorgan Chase & Co (NYSE: JPM) declared preferred stock dividends on its Series II, OO and PP shares on 13 November 2026, the bank said. The declaration covers three outstanding series of non-cumulative preferred stock and lands the same day JPMorgan filed a routine insider transaction form unrelated to the payout. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Fri 13 Nov | TipRanks | JPMorgan Chase (JPM) Ramps Up Crypto Investments
  https://www.tipranks.com/news/jpmorgan-chase-jpm-ramps-up-crypto-investments
  (page: did not load (403))
- Fri 13 Nov | StreetInsider | Form 424B2 JPMORGAN CHASE & CO
  https://www.streetinsider.com/SEC+Filings/Form+424B2+JPMORGAN+CHASE+&amp;+CO/27344327.html
  (page: did not load (403))
## XOM  (8 leads)
- Sat 14 Nov | GuruFocus | ExxonMobil Holdings Corp (XOM) Stock Up 0.5% but GF Value Says O
  https://www.gurufocus.com/news/9199273/exxonmobil-holdings-corp-xom-stock-up-05-but-gf-value-says-overvalued-gf-score-70100
  (page: did not load (403))
- Sat 14 Nov | Yahoo Finance | Is ExxonMobil Holdings (XOM) Undervalued After Its $12.5b Guyana Longtail Approval?
  https://finance.yahoo.com/energy/articles/exxonmobil-holdings-xom-undervalued-12-011312124.html
  > ExxonMobil Holdings (XOM) just approved a US$12.5b Longtail development offshore Guyana, targeting non associated gas and condensate. This gives investors a fresh long term project to factor into the stock's risk profile.
- Fri 13 Nov | Oil & Gas Journal | ExxonMobil takes FID for Longtail development offshore Guyana
  https://www.ogj.com/exploration-development/news/55418842/exxonmobil-takes-fid-for-longtail-development-offshore-guyana
  > The development, in the southeastern portion of the block, will target non-associated gas and condensate-rich reservoirs. Subject to future investment decisions, market demand, and development of supporting infrastructure, gas from the project could be transported to shore by pipeline.
## AVGO  (8 leads)
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
  > Nvidia Loses Nearly $1 Trillion in Value After Jensen Huang Resigns; Broadcom Drops 5% - Nvidia shares posted their worst weekly performance this week and erased nearly $1 trillion in market value after former CEO Jensen Huang resigned.
- Fri 13 Nov | Global Banking & Finance Review | Broadcom falls 4.76% in Friday's session
  https://www.globalbankingandfinance.com/broadcom-avgo-falls-2026-11-13/
- Fri 13 Nov | Yahoo Finance Australia | Broadcom Inc. (AVGO) Suffers a Larger Drop Than the General Market: Key Insights
  https://au.finance.yahoo.com/news/broadcom-inc-avgo-suffers-larger-214501014.html
- Fri 13 Nov | Benzinga | Nvidia Loses Its Founder, AMD and Broadcom Take the Crown: This Week on Wall Street
  https://www.benzinga.com/markets/market-summary/26/11/63269563/this-week-on-wall-street-nvidia-huang-amd-broadcom-fed-hike
- Fri 13 Nov | Moomoo | Broadcom Shares Fall After Rothschild & Co Redburn Downgrade
  https://www.moomoo.com/news/post/1004619830/broadcom-shares-fall-after-rothschild-co-redburn-downgrade
## BRK.B  (8 leads)
- Sat 14 Nov | ad-hoc-news.de | Berkshire's Buyback Spree Masks a Thinner Insurance Haul as 13F Deadline Nears
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-s-buyback-spree-masks-a-thinner-insurance-haul-as-13f-deadline-nears/70507780
  > Berkshire Hathaway returned roughly $9.6 billion to shareholders through buybacks in the third quarter of 2026, even as underwriting profit at its insurance and reinsurance operations slid 42.9% to $1.35 billion. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Sat 14 Nov | GuruFocus | Berkshire Hathaway Inc (BRK.B) Stock Up 0.5% but GF Value Says O
  https://www.gurufocus.com/news/9199263/berkshire-hathaway-inc-brkb-stock-up-05-but-gf-value-says-overvalued-gf-score-74100
  (page: did not load (403))
- Sat 14 Nov | ad-hoc-news.de | Berkshire's $352 Billion War Chest Faces Its Toughest Test Yet
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-s-352-billion-war-chest-faces-its-toughest-test-yet/70507119
  > Berkshire Hathaway's cash pile has long been the stuff of investor legend, but the conglomerate's latest quarterly scorecard suggests that financial firepower alone won't be enough to carry the stock. With roughly $352.3 billion in cash, cash equivalents and U.S. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
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
- Fri 13 Nov | MarketBeat | Visa (NYSE:V) Stock Jumps 1.2% - Time to Buy?
  https://www.marketbeat.com/instant-alerts/price-visa-nyse-v-stock-jumps-12-time-to-buy-2026-11-13/
  > Visa (NYSE:V) Stock Jumps 1.2% - Time to Buy? - Visa shares rose 1.2% to about $425.55, though trading volume was 38% below its average. - Visa beat quarterly forecasts, reporting EPS of $3.48 and revenue of $12.14 billion; revenue increased 13.2% year over year.
- Fri 13 Nov | Yahoo Finance | Top Stock Reports for Visa, ExxonMobil & Pfizer
  https://finance.yahoo.com/markets/stocks/articles/top-stock-reports-visa-exxonmobil-201900445.html
  > Friday, November 13, 2026 The Zacks Research Daily presents the best research output of our analyst team. Today's Research Daily features new research reports on 16 major stocks, including Visa Inc. These research reports have been hand-picked from roughly 70 reports published by our analyst team today.
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
- Sat 14 Nov | Pluang | Costco uses AI to auto-reorder drugs, keeping p...
  https://pluang.com/en/news-feed/costco-ai-pemesanan-obat-otomatis-tingkatkan-pertumbuhan-farmasi
  (page: did not load (403))
- Sat 14 Nov | PYMNTS.com | Costco Trusts AI to Reorder Drugs. Most Retailers Won’t
  https://www.pymnts.com/news/retail/2026/costco-trusts-ai-to-reorder-drugs-most-retailers-wont/
  > Costco uses AI to compare drug prices across suppliers and automatically reorder inventory, keeping pharmacy in-stock levels above 98%. Costco is extending AI inventory management to gasoline operations while expanding pharmacy services through prescription pickup lockers, mobile prepayment and GLP-1 programs.
- Fri 13 Nov | Barron's | Costco: An AI Shelter?
  https://www.barrons.com/articles/costco-an-ai-shelter-182f8c30
  (page: did not load (401))
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
- Fri 13 Nov | 24/7 Wall St. | Netflix Split Its Stock 10-for-1 One Year Ago, and $1,000 Invested Right After Is Now Worth $568
  https://247wallst.com/investing/2026/11/13/netflix-split-its-stock-10-for-1-one-year-ago-and-1000-invested-right-after-is-now-worth-568/
  > Netflix Split Its Stock 10-for-1 One Year Ago, and $1,000 Invested Right After Is Now Worth $568 This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Fri 13 Nov | Investing.com South Africa | Why is Netflix stock gaining today? By Investing.com
  https://za.investing.com/news/stock-market-news/why-is-netflix-stock-gaining-today-93CH-4574709
- Fri 13 Nov | ad-hoc-news.de | Netflix stock: NBCUniversal speculation puts M&A in focus
  https://www.ad-hoc-news.de/boerse/news/corporate-news/netflix-stock-nbcuniversal-speculation-puts-m-a-in-focus/70505688
- Fri 13 Nov | StreetInsider | Netflix gains as institutions add shares near 52-week low
  https://www.streetinsider.com/Investing/Netflix+gains+as+institutions+add+shares+near+52-week+low/27340962.html
- Fri 13 Nov | Budapest Reporter | Ottoman Soldiers Spotted on Netflix’s 3 Body Problem Set in Budapest
  https://www.budapestreporter.com/3-body-problem-budapest-stock-exchange-palace/
## INTC  (8 leads)
- Sat 14 Nov | Pluang | Lawsuit filed against Intel over alleged mislea...
  https://pluang.com/en/news-feed/peringatan-penggugat-kelas-intel-dampak-negatif-hasil-q3-2026
  (page: did not load (403))
- Sat 14 Nov | WTVB | Soros Fund ramps up Intel stake to over $340 million in third quarter
  https://wtvbam.com/2026/11/13/soros-fund-ramps-up-intel-stake-to-over-340-million-in-third-quarter/
  > Nov 13 (Reuters) – Soros Fund Management, the family office of billionaire George Soros, significantly raised its stake in Intel in the third quarter, a regulatory filing showed on Friday. Here are more details:
- Fri 13 Nov | Yahoo Finance | Why Intel Stock Slumped Today
  https://finance.yahoo.com/markets/stocks/articles/why-intel-stock-slumped-today-230951500.html
  > It was an explosive week for the semiconductor industry, and Intel (NASDAQ:INTC) is surely glad that it's over. On Friday, the company's stock sank for the second day in a row, dipping by almost 3% on growing concerns that changes at Nvidia (NASDAQ:NVDA) would negatively affect its operations.
- Fri 13 Nov | Finimize | Soros Fund Management Loaded Up On Intel, Filings Show
  https://finimize.com/content/soros-fund-management-loaded-up-on-intel-filings-show
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | Crypto Briefing | Intel stock falls nearly 3% as Nvidia’s leadership shake-up rattles chipmakers
  https://cryptobriefing.com/intel-stock-falls-nvidia-leadership-uncertainty/
- Fri 13 Nov | MarketBeat | Intel (NASDAQ:INTC) Stock Falls 2.5% After Analyst Downgrade
  https://www.marketbeat.com/instant-alerts/price-intel-nasdaq-intc-stock-falls-25-after-analyst-downgrade-2026-11-13/
- Fri 13 Nov | TipRanks | Soros boosts stakes in Intel, Meta, cuts stake in Linde
  https://www.tipranks.com/news/the-fly/soros-boosts-stakes-in-intel-meta-cuts-stake-in-linde-thefly-news?utm_source=edition.cnn.com&utm_medium=referral
- Fri 13 Nov | Crypto Briefing | Soros Fund Management raises stakes in Micron and Intel
  https://cryptobriefing.com/soros-fund-raises-micron-intel-stakes/
## LLY  (8 leads)
- Sat 14 Nov | GuruFocus | A Look at Eli Lilly and Co (LLY) After 1.1% Gain -- GF Value $16
  https://www.gurufocus.com/news/9199259/a-look-at-eli-lilly-and-co-lly-after-11-gain-gf-value-161019-vs-price-144350
  (page: did not load (403))
- Sat 14 Nov | WFMZ.com | Eli Lilly breaks ground on $3.5 billion manufacturing facility in Lehigh County
  https://www.wfmz.com/video/eli-lilly-breaks-ground-on-3-5-billion-manufacturing-facility-in-lehigh-county/video_1c5a9c85-2651-54f5-bfc3-9c37154861d7.html
  (page read: it never names the company, so probably not about it: skip)
- Sat 14 Nov | Trefis | What Is The Market Seeing In Eli Lilly Stock?
  https://www.trefis.com/stock/lly/articles/624864/what-is-the-market-seeing-in-eli-lilly-stock/2026-11-13
  > What Is The Market Seeing In Eli Lilly Stock? For questions about this article or underlying research, email help@trefis.com. Eli Lilly (LLY) stock trades at 46.1 times its earnings over the last twelve months, compared with 21.9 for the S&P 500. So how much growth are buyers paying for at Lilly’s current price?
Read 80 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: PHDC, ORAS, CLHO, ALCN, EGAL.
