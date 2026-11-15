# Desk brief, Sunday, November 15, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 275s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-13 (19.3); Treasury yields to 2026-11-13 (10-year 5.15%).
- **valuation**: ok in 9s (GitHub Actions). LLY: failed ('NoneType' object is not subscriptable); kept the card it had
- **movers**: ok in 19s (GitHub Actions). Market values: 18 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 53.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 50 stocks, k 16.2%, median P/E 10.7; cheapest MASR +71%, PHAR +51%, ABUK +50%; dearest ARAB -62%, MOIN -66%, BTFH -71%
- **views**: ok in 0s (GitHub Actions). 2026-10-30-cib-margins: on track -> right  (Judged on its date: CIB +6.9% against egx30 +4.9% since 2026-10-30.)
- **results**: ok in 61s (GitHub Actions). 
- **news**: ok in 97s (GitHub Actions). 
- **leads**: ok in 99s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py).

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
EGX week and month: EGX stocks trading at least EGP 1m a day on average (213)
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
- Thu 12 Nov | آراب فاينانس | دلتا للطباعة تضاعف أرباحها في تسعة أشهر
  https://www.arabfinance.com/ar/news/newdetails/دلتا-للطباعة-تضاعف-أرباحها-في-تسعة-أشهر
- Thu 12 Nov | أموال الغد | أرباح دلتا للطباعة والتغليف تقفز 137% إلى 147.6 مليون جنيه خلال 9 أشهر
  https://amwalalghad.com/2026/11/12/أرباح-دلتا-للطباعة-والتغليف-تقفز-137-إلى-147/
- Thu 12 Nov | أموال الغد | أرباح دلتا للطباعة والتغليف تقفز 137.1% إلى 147.6 مليون جنيه خلال 9 أشهر
  https://amwalalghad.com/2026/11/12/أرباح-دلتا-للطباعة-والتغليف-تقفز-137-1-إلى-14/
## ROTO +5.9%  Al Rowad
- Sat 14 Nov | Vietnam.vn | يعمل المسؤولون الرواد على تعزيز الأساس من القاعدة الشعبية.
  https://www.vietnam.vn/ar/can-bo-tien-phong-cung-co-suc-manh-tu-co-so
- Sat 14 Nov | الموقف الرياضي | الرواد يحل ضيفاً على الحرية في دوري كرة السلة للسيدات
  https://riadi.alwehda.gov.sy/?p=173605
- Sat 14 Nov | شاهد الآن | جمعية الرواد الشبابية بجازان تحتفي بتخريج (522) شابًا وفتاة
  https://shahdnow.sa/369612/
- Sat 14 Nov | صحيفة الحقيقة الإلكترونية | جمعية الرواد الشبابية بجازان تحتفي بتأهيل 522 شابًا وشابة عبر مشروع "مهارات المستقبل"
  https://alhqyq.com/news/s/28646
## HDBK +5.8%  Housing & Development Bank
- Sun 15 Nov | المصري اليوم | 14.8 مليار جنيه أرباحًا خلال 9 أشهر.. بنك التعمير والإسكان يعزز انطلاقته بقيادة يحيى أبوالفتوح
  https://www.almasryalyoum.com/news/details/4410647
- Sat 14 Nov | جريدة الدستور | سعر الريال السعودي اليوم السبت 14 نوفمبر 2026 في البنك الأهلي وبنك مصر
  https://www.dostor.org/5777067
- Sat 14 Nov | الجريدة العقارية | من المدرجات.. موظفو بنك التعمير والإسكان يدعمون منتخب مصر أمام مالاوي (صور)
  https://www.aleqaria.com.eg/post/details/358053/من-المدرجات..-موظفو-بنك-التعمير-والإسكان-يدعمون-منتخب-مصر-أمام-مالاوي-صور
- Sat 14 Nov | التعمير | بالصور.. موظفو بنك التعمير والإسكان يدعمون منتخب مصر من المدرجات.. «دايمًا في ضهر بلدهم»
  https://eltaameer.com/archives/484389
## INEG -6.3%  Integrated Engineering Group
- no headlines found
## PRCL -6.0%  Sheeni
- no headlines found
## CCRS -5.0%  Gulf Canadian Real Estate Investment
- no headlines found
## BIOC -4.3%  Glaxo Smith Kline
- Sun 15 Nov | Dawaa News MENA | أسهم الأدوية المصرية تصعد بقيادة جلاكسو والنيل وممفيس | 12 نوفمبر 2026
  https://dawaanews.com/egypt-pharma-healthcare-stocks-weekly-12-november-2026/
- Thu 12 Nov | جريدة المال | «جلاكسو سميثكلاين» تدعو جمعيتها غير العادية للانعقاد 6 ديسمبر للنظر في الاندماج مع «أمون للأدوية»
  https://almalnews.com/2146951/«جلاكسو-سميثكلاين»-تدعو-جمعيتها-غير-العادية-للانعقاد/
- Thu 12 Nov | شبكة تواصل الإخبارية | 6 ديسمبر.. عمومية “جلاكسو سميثكلاين” تبحث زيادة رأس المال للاندماج مع “أمون”
  https://twaslnews1.twaslnews.com/7581920/
- Thu 12 Nov | Traders Union | جلاكسو سميثكلاين تدعو عمومية 6 ديسمبر لمناقشة اندماج أمون في مصر
  https://tradersunion.com/ar/news/companies/show/4212568-gsk-amoun-merger-egypt-meeting/
## COPR -3.3%  Copper For Commercial Investment
- no headlines found

# US 2026-11-13
## NU +11.8%  Nu Holdings
- Sun 15 Nov | The Globe and Mail | Nu Holdings: 3 Key Takeaways for Long-Term Investors
  https://www.theglobeandmail.com/investing/markets/stocks/NU/pressreleases/8842160/nu-holdings-3-key-takeaways-for-long-term-investors/
- Sat 14 Nov | The Globe and Mail | Analysts Offer Insights on Financial Companies: Vylor Inc (VYLR) and Nu Holdings (NU)
  https://www.theglobeandmail.com/investing/markets/stocks/NU/pressreleases/8838441/analysts-offer-insights-on-financial-companies-vylor-inc-vylr-and-nu-holdings-nu/
- Sat 14 Nov | Quantisnow | Nu Holdings jumps 12% on record profit and wins back half of a monthlong slide
  https://www.quantisnow.com/articles/nu-holdings-jumps-12-on-record-profit-as-90-day-bad-loans-rise-to-7-3
- Sat 14 Nov | Yahoo Finance | Nu Holdings (NU) is Surging by Double Digits. Here’s What’s Driving the Rally
  https://finance.yahoo.com/markets/stocks/articles/nu-holdings-nu-surging-double-045349151.html
## CBRS +11.2%  Cerebras Systems
- Sat 14 Nov | Moomoo | Cerebras Systems (CBRS) Stock Week Ahead: Options Flow Braces for a 12.4% Swing by Friday
  https://www.moomoo.com/community/feed/cerebras-systems-cbrs-stock-week-ahead-options-flow-braces-for-117615595094037
- Sat 14 Nov | Pluang | Cerebras Systems upgraded to buy as valuation i...
  https://pluang.com/en/news-feed/cerebras-peluang-beli-tepat-waktu-peningkatan-rating
- Sat 14 Nov | MarketBeat | Cerebras Q3 Results: How Much More Proof Does Wall Street Need?
  https://www.marketbeat.com/articles/cerebras-q3-results-how-much-more-proof-does-wall-street-need/
- Sat 14 Nov | Yahoo Finance | Cerebras Systems (CBRS) Rockets Higher as These 2 Catalysts Emerge
  https://finance.yahoo.com/markets/stocks/articles/cerebras-systems-cbrs-rockets-higher-044957586.html
## MOG.B +6.7%  Moog
- Fri 13 Nov | Stock Titan | Moog (MOG) director sells Class A shares in nine trades under a preset trading plan.
  https://www.stocktitan.net/sec-filings/MOG/form-4-moog-inc-insider-trading-activity-19dd5dc1dbe9.html
- Fri 13 Nov | Stock Titan | Moog's 10 a.m. ET results call is set for Nov. 20.
  https://www.stocktitan.net/news/MOG/moog-inc-to-announce-fiscal-2026-year-end-results-on-november-20-3l7xfb692nal.html
- Fri 13 Nov | Yahoo! Finance Canada | Moog Inc. (MOG-A) Stock Forecasts
  https://ca.finance.yahoo.com/research/reports/ARGUS_4143_QuantitativeReport_1794355200000
- Fri 13 Nov | Yahoo Finance | Moog (MOG.A) Earnings Expected to Grow: What to Know Ahead of Q4 Release
  https://finance.yahoo.com/markets/stocks/articles/moog-mog-earnings-expected-grow-140001035.html
## ALNY +5.4%  Alnylam Pharmaceuticals
- Fri 13 Nov | Traders Union | Alnylam Pharmaceuticals shares jump around 5.5% as strong Q3 product revenue drives commercial momentum
  https://tradersunion.com/news/stocks/show/4238510-alnylam-pharmaceuticals-rises-5-40percent-today/
- Fri 13 Nov | Stock Titan | An investment manager reports over 10% of Alnylam (ALNY), with no shared voting power.
  https://www.stocktitan.net/sec-filings/ALNY/schedule-13g-a-alnylam-pharmaceuticals-inc-amended-passive-investment-2b2a0b6dc3f8.html
- Fri 13 Nov | Quiver Quantitative | Why Alnylam Pharmaceuticals (ALNY) Stock Is Up Today | ALNY Stock News
  https://www.quiverquant.com/news/Why+Alnylam+Pharmaceuticals+(ALNY)+Stock+Is+Up+Today
- Fri 13 Nov | Yahoo Finance UK | Alnylam Pharmaceuticals, Inc. (ALNY) stock price, news, quote and history
  https://uk.finance.yahoo.com/quote/ALNY/
## U +5.2%  Unity Software
- Fri 13 Nov | GuruFocus | Unity Software Inc (U) Shares Surge 5.2% -- What GF Score of 68 Tells Investors
  https://www.gurufocus.com/news/9198827/unity-software-inc-u-shares-surge-52-what-gf-score-of-68-tells-investors
- Fri 13 Nov | Investing.com Nigeria | Piper Sandler reiterates Unity Software stock rating at overweight By Investing.com
  https://ng.investing.com/news/stock-market-news/piper-sandler-reiterates-unity-software-stock-rating-at-overweight-93CH-2806488
- Fri 13 Nov | Stock Titan | Convertible notes due in 2027 underpin Sequoia Capital DIV-2022’s Unity Software (U) stake.
  https://www.stocktitan.net/sec-filings/U/schedule-13g-a-unity-software-inc-amended-passive-investment-disclosu-af4c80ad7ab2.html
- Fri 13 Nov | Yahoo Finance | Unity (U) Stock Sees Fair Value Lift After Q3 Spurs Higher Analyst Targets
  https://finance.yahoo.com/markets/stocks/articles/unity-u-stock-sees-fair-200842465.html
## NBIS -9.9%  Nebius Group
- Sun 15 Nov | Kalkine Media | What Is Driving Nebius Group (NASDAQ:NBIS) AI Cloud Expansion?
  https://kalkinemedia.com/us/stocks/communication/what-is-driving-nebius-group-nasdaqnbis-ai-cloud-expansion
- Sat 14 Nov | The Globe and Mail | Innodata vs. Nebius: Which Technology Stock Is a Better Buy for 2027?
  https://www.theglobeandmail.com/investing/markets/stocks/NBIS/pressreleases/8838474/innodata-vs-nebius-which-technology-stock-is-a-better-buy-for-2027/
- Sat 14 Nov | The Motley Fool | Innodata vs. Nebius: Which Technology Stock Is a Better Buy for 2027?
  https://www.fool.com/coverage/better-buy/2026/11/14/innodata-vs-nebius-which-technology-stock-is-a-better-buy-for-2027/
- Sat 14 Nov | Benzinga | Benzinga Bulls and Bears: Nvidia, Rocket Lab, Nebius
  https://www.benzinga.com/markets/market-summary/26/11/63273716/benzinga-bulls-and-bears-nvidia-rocket-lab-nebius
## AMD -8.8%  Advanced Micro Devices
- Sun 15 Nov | Investing.com India | Form 4 Advanced Micro Devices For: 14 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-advanced-micro-devices--for-14-november-93CH-5704969
- Sat 14 Nov | The Globe and Mail | Why Advanced Micro Devices Stock Surged This Week
  https://www.theglobeandmail.com/investing/markets/stocks/AMD/pressreleases/8836877/why-advanced-micro-devices-stock-surged-this-week/
- Sat 14 Nov | The Motley Fool | Why Advanced Micro Devices Stock Surged This Week
  https://www.fool.com/coverage/market-movers/2026/11/14/why-advanced-micro-devices-stock-surged-this-week/
- Sat 14 Nov | MarketBeat | Advanced Micro Devices, Inc. $AMD Stock Position Boosted by Cornerstone Advisors LLC
  https://www.marketbeat.com/instant-alerts/filing-advanced-micro-devices-inc-amd-stock-position-boosted-by-cornerstone-advisors-llc-2026-11-14/
## FN -7.3%  Fabrinet
- Sun 15 Nov | TipRanks | Fabrinet Earnings Call Signals Data Center Growth Surge
  https://www.tipranks.com/news/company-announcements/fabrinet-earnings-call-signals-data-center-growth-surge
```

## Results to record (results_due.py)
## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py
### TMGH
- Sun 15 Nov | جريدة المال | مجموعة طلعت مصطفى تحقق 47.6 مليار جنيه إيرادات و15 مليارًا صافي ربح خلال 9 أشهر
  https://almalnews.com/2147287/مجموعة-طلعت-مصطفى-تحقق-47-6-مليار/
  > أعلنت مجموعة طلعت مصطفى القابضة، تحقيق إيرادات مجمعة بقيمة 47.6 مليار جنيه خلال الأشهر التسعة الأولى من عام 2026، بنمو 24% على أساس سنوي، مدفوعة بكفاءة التنفيذ في قطاع التطوير العقاري والنمو المتواصل في أنشطة الضيافة ومصادر الدخل المتكرر الأخرى التابعة للمجموعة. وارتفع صافي الربح المجمع بعد الضريبة بنسبة 19% على أساس سنوي، ليسجل 15 مليار جنيه، بما يعكس قوة الأداء التشغيلي ومرونة نموذج الأعمال المتنوع للمجموعة. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Sun 15 Nov | أموال الغد | «طلعت مصطفى» تحقق 15 مليار جنيه أرباحا خلال 9 أشهر
  https://amwalalghad.com/2026/11/15/طلعت-مصطفى-تحقق-15-مليار-جنيه-أرباحا-خ/
  > ارتفع صافي الربح المجمع بعد الضرائب لمجموعة طلعت مصطفى القابضة بنسبة 19% خلال التسعة أشهر الأولى من عام 2026، على أساس سنوي، ليصل إلى 15 مليار جنيه، مقارنة بالفترة المقابلة من العام الماضي، فيما سجلت الإيرادات المجمعة نموًا بنسبة 24% لتبلغ 47.6 مليار جنيه. [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | التعمير | مجموعة طلعت مصطفى تحقق 15 مليار جنيه صافي ربح خلال 9 أشهر
  https://eltaameer.com/archives/484428
  > *290.1 مليار جنيه مبيعات متعاقد عليها.. وارتفاع مبيعات الربع الثالث 54.6% إلى 71 مليار جنيه *18.9 مليار جنيه إيرادات متكررة تمثل 40% من إجمالي الإيرادات.. وتسليم 2724 وحدة خلال 9 أشهر [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | بوابة مولانا | طلعت مصطفى تحقق 15 مليار جنيه أرباحًا وترفع الإيرادات
### ALCN
- Wed 11 Nov | جريدة المال | الأهلي فاروس: أرباح تشغيلية استثنائية لـ «النزهة» و«الحاويات» دون فرصة شراء عند التقييمات الحالية
  https://almalnews.com/2146570/الأهلي-فاروس-أرباح-تشغيلية-استثنائية-لـ-«النزهة»/
  > أظهر تقرير صادر عن وحدة بحوث «الأهلي فاروس» أن نتائج أعمال «مستشفى النزهة الدولي» خلال الأشهر التسعة الأولى من عام 2026 جاءت إيجابية على صعيد الإيرادات والأرباح، محققة 434.2 مليون جنيه إيرادات بنمو 10% على أساس سنوي، وصافي ربح بلغ 143.5 مليون جنيه بزيادة 14% على أساس سنوي. [Figures on the page: nine months; first half. Check which one each figure is.]
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: SWDY, JUFO, EAST, EFIH, EMFD, BQDC.
- Already recorded: COMI, ABUK, ETEL, EGAL.

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
- 2026-11-18 HRHO results (expected)  <- write its preview
- 2026-11-19 MSFT dividend

## Views
- judged right with no lesson yet: Higher rates protect CIB's margins  <- write its `lesson`
- due 2026-11-20: Brent stays below $105 while Iran talks continue (open)
    2026-10-30-cib-margins: on track -> right  (Judged on its date: CIB +6.9% against egx30 +4.9% since 2026-10-30.)

## Fair value
- Changed since the last run: ABUK -33% -> +50% (low -> low); EXPA +49% -> +30% (low -> medium); HDBK -14% -> +2% (low -> medium); LCSW -47% -> -50% (low -> medium).
- In the ten cheapest or dearest with no note: MCQE, ADIB, SCEM, CSAG, AMOC, MTIE, AMIA, LCSW, BINV.

## Due today
- Light run (no session since Saturday's desk): carry both sections over, update only news, the week ahead and views due; no movers' reasons; side sessions only if there is work for them.
- Sunday: write the desk's note for two more stocks (18 still without one; next: XOM, MSFT), and read the whole fair-value table for figures that cannot be right.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 3 days, 2026-11-15. Open each story before using it.
## COMI  (8 leads)
- Sun 15 Nov | بنوك اون لاين | عمر الحسيني رئيسًا لقطاع الخدمات المصرفية للمؤسسات بالبنك التجاري الدولي CIB
  https://www.bnokonline.com/28666
  > عمر الحسيني رئيسًا لقطاع الخدمات المصرفية للمؤسسات بالبنك التجاري الدولي CIB تولى عمر الحسيني منصب رئيس قطاع الخدمات المصرفية للمؤسسات بالبنك التجاري الدولي مصر «CIB»، وذلك بعد قيادته لقطاع الخزانة وأسواق المال، في خطوة تعكس اتساع نطاق مسؤولياته داخل البنك، مستندًا إلى خبرة مصرفية تمتد لأكثر من 20 عامًا.
- Sat 14 Nov | شبكة تواصل الإخبارية | الدولار يسجل 53.50 جنيه للبيع بالبنك المركزي.. و53.45 جنيه في CIB والإسكندرية
  https://twaslnews1.twaslnews.com/7660854/
  (page: did not load (403))
- Fri 13 Nov | بنكي | بطاقة CIB noon الائتمانية — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/414
  > - كاش باك 5% - معدل الفائدة السنوي الفعلي 24 عرض ساري على البطاقة تقسيط بدون فوائد 13 · خصومات 12 - تقسيط المشتريات لمدة 12 شهرًا بدون فوائد Audio Technology شرف دي جي - تقسيط بدون فوائد + خصم حتى 25% Bosch بوش - خصم 10% DALYDRESS دالى دريس
## TMGH  (8 leads)
- Sun 15 Nov | جريدة المال | مجموعة طلعت مصطفى تحقق 47.6 مليار جنيه إيرادات و15 مليارًا صافي ربح خلال 9 أشهر
  https://almalnews.com/2147287/مجموعة-طلعت-مصطفى-تحقق-47-6-مليار/
  > أعلنت مجموعة طلعت مصطفى القابضة، تحقيق إيرادات مجمعة بقيمة 47.6 مليار جنيه خلال الأشهر التسعة الأولى من عام 2026، بنمو 24% على أساس سنوي، مدفوعة بكفاءة التنفيذ في قطاع التطوير العقاري والنمو المتواصل في أنشطة الضيافة ومصادر الدخل المتكرر الأخرى التابعة للمجموعة. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Sun 15 Nov | أموال الغد | «طلعت مصطفى» تحقق 15 مليار جنيه أرباحا خلال 9 أشهر
  https://amwalalghad.com/2026/11/15/طلعت-مصطفى-تحقق-15-مليار-جنيه-أرباحا-خ/
  > ارتفع صافي الربح المجمع بعد الضرائب لمجموعة طلعت مصطفى القابضة بنسبة 19% خلال التسعة أشهر الأولى من عام 2026، على أساس سنوي، ليصل إلى 15 مليار جنيه، مقارنة بالفترة المقابلة من العام الماضي، فيما سجلت الإيرادات المجمعة نموًا بنسبة 24% لتبلغ 47.6 مليار جنيه. [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | التعمير | مجموعة طلعت مصطفى تحقق 15 مليار جنيه صافي ربح خلال 9 أشهر
  https://eltaameer.com/archives/484428
  > *290.1 مليار جنيه مبيعات متعاقد عليها.. وارتفاع مبيعات الربع الثالث 54.6% إلى 71 مليار جنيه *18.9 مليار جنيه إيرادات متكررة تمثل 40% من إجمالي الإيرادات.. وتسليم 2724 وحدة خلال 9 أشهر [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | بوابة مولانا | طلعت مصطفى تحقق 15 مليار جنيه أرباحًا وترفع الإيرادات
  https://mwlana.com/details/294208/
  > كشفت القوائم المالية المجمعة لمجموعة طلعت مصطفى القابضة عن تحقيق قفزة قوية في مؤشرات الأداء المالي والتشغيلي خلال الأشهر التسعة الأولى من عام 2026؛ حيث ارتفع صافي الربح المجمع بعد الضريبة بنسبة 19% على أساس سنوي ليصل إلى 15 مليار جنيه، مقارنة بنحو 12.6 مليار جنيه خلال الفترة نفسها من العام الماضي. [Figures on the page: consolidated; unaudited or preliminary; nine months; one quarter. Check which one each figure is.]
- Sun 15 Nov | شبكة تواصل الإخبارية | طلعت مصطفى تُحقق 15 مليار جنيه أرباحًا مجمعة في 9 أشهر بارتفاع 19%
  https://twaslnews1.twaslnews.com/7713410/
- Sun 15 Nov | ايكونومي بلس | أكثر من ألف أجنبي يشترون عقارات من "طلعت مصطفى" بـ31.2 مليار جنيه في 9 أشهر
  https://economyplusme.com/ar/news/34164
- Sun 15 Nov | Pioneers Misr | ارتفاع أرباح مجموعة طلعت مصطفى القابضة 12% خلال الربع الثالث من 2026 لتسجل 5.1 مليار جنيه
  https://pioneersmisr.com/123651/
- Sun 15 Nov | بوابة بلوم | بنمو 12%.. الإيرادات العقارية تدفع أرباح طلعت مصطفى إلى 5.06 مليار جنيه بالربع الثالث
  https://bloom-gate.com/أسواق/بنمو-12-الإيرادات-العقارية-تدفع-أرباح-ط/
## ETEL  (8 leads)
- Sun 15 Nov | CairoScene | Telecom Egypt's Net Profit Rises 44% to EGP 24.4 Billion
  https://cairoscene.com/News/Telecom-Egypt-s-Net-Profit-Rises-44-to-EGP-24-4-Billion
  > Telecom Egypt's Net Profit Rises 44% to EGP 24.4 Billion Telecom Egypt recorded EGP 93.6 billion in revenue during the first nine months of 2026, driven by data services and international calls. Telecom Egypt recorded a 44% year-on-year increase in net profit after tax during the first nine months of 2026, reaching EGP 24.4 billion. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Sat 14 Nov | موقع الصفحة الأولى | "حماية الحقوق" بين 14 مليون عميل واستثمارات بـ260 مليار فى المصرية للاتصالات
  https://www.safha1.com/16697
  > ماذا تفيد توصيات مجلس النواب لمستقبل الإنترنت ؟ "حماية الحقوق" بين 14 مليون عميل واستثمارات بـ260 مليار فى المصرية للاتصالات أوصت لجنة الاتصالات وتكنولوجيا المعلومات بمجلس النواب، بإلزام الشركة المصرية للاتصالات بالتنسيق مع وزارة الاتصالات والجهاز القومي لتنظيم الاتصالات؛
- Sat 14 Nov | اليوم السابع | المصرية للاتصالات تعلن خلو منصب الرئيس التنفيذي للشؤون التجارية للأفراد
  https://www.youm7.com/story/2026/11/14/المصرية-للاتصالات-تعلن-خلو-منصب-الرئيس-التنفيذي-للشؤون-التجارية-للأفراد/7618462
  > أعلنت الشركة المصرية للاتصالات، خلو منصب الرئيس التنفيذي للشؤون التجارية للأفراد اعتبارًا من 12 نوفمبر 2026، وذلك وفقًا لقرارات مجلس إدارة الشركة التي أبلغت بها البورصة المصرية، عقب اجتماع المجلس الذي عقد في 11 نوفمبر الجاري. [Figures on the page: standalone; consolidated; nine months. Check which one each figure is.]
## PHDC  (2 leads)
- Sat 14 Nov | نيوز رووم | محاضر بأول أكتوبر ضد «بالم هيلز» وياسين منصور بسبب نزاع على وحدات «بالم فالي»
  https://newsroom.info/484889
  (page read: it never names the company, so probably not about it: skip)
- Sat 14 Nov | موقع الحرية الإخباري | محاضر ضد «بالم هيلز» وياسين منصور على خلفية بيع وحدات بكمبوند «بالم فالي».. ووزير سابق ضمن أطراف النزاع
  https://alhorianews.com/محاضر-ضد-بالم-هيلز-وياسين-منصور-على-خ/
  > تصاعدت الخلافات بين شركة السعودية للتطوير العمراني وشركة «بالم هيلز» للتعمير بشأن بيع عدد من الوحدات داخل كمبوند «بالم فالي»، لتصل إلى تحرير عدة محاضر ضد الشركة ورئيس مجلس إدارتها ياسين منصور، على خلفية نزاعات تتعلق بعمليات بيع وحدات سكنية لأكثر من طرف، وتضارب المراكز القانونية للمشترين.
## SWDY  (8 leads)
- Sun 15 Nov | BW Businessworld | Piyush Goyal Meets ElSewedy Electric CEO, Explores Investment Opportunities In India
  https://www.businessworld.in/article/piyush-goyal-meets-elsewedy-electric-ceo-explores-investment-opportunities-in-india-633668
  > Commerce and Industry Minister Piyush Goyal met Ahmed ElSewedy, President and CEO of Egyptian multinational ElSewedy Electric, on 14 November to discuss potential investment opportunities in India and strengthen bilateral business ties. The discussions focused on collaboration in key sectors, including electrical equipment, smart meters and data centres, Goyal said in a social media post.
- Sun 15 Nov | MillenniumPost | Goyal meets ElSewedy Electric CEO; discusses investment opportunities in India
  https://www.millenniumpost.in/amp/business/goyal-meets-elsewedy-electric-ceo-discusses-investment-opportunities-in-india-683289
  > Goyal meets ElSewedy Electric CEO; discusses investment opportunities in India Cairo: Commerce and Industry Minister Piyush Goyal met Ahmed ElSewedy, President and CEO of the Egyptian multinational ElSewedy Electric, to discuss potential investment opportunities in India. The meeting was held here on November 14.
- Sun 15 Nov | NewsBytes | Piyush Goyal in Egypt urges ElSewedy Electric invest in India
  https://www.newsbytesapp.com/news/business/piyush-goyal-in-egypt-urges-elsewedy-electric-invest-in-india/tldr
  (page: did not load (403))
## ORAS  (1 leads)
- Sat 14 Nov | www.youlyou.com | تحالف أوراسكوم كونستراكشون يؤمن تمويل محطة رياح في مصر والتشغيل صيف 2028
  https://www.youlyou.com/93991
  > 1- تأمين تمويل محطة رياح جديدة في مصر بقدرة 900 ميجاوات. 2- المشروع ينفذه تحالف ENGIE وAeolus وأوراسكوم للإنشاءات. 3- المحطة تقع بمنطقة رأس شقير على خليج السويس. 4- بدء التشغيل بقدرة 300 ميجاوات في ديسمبر 2027. 5- المحطة توفر الكهرباء لأكثر من 1.4 مليون منزل مصري
## FWRY  (4 leads)
- Sun 15 Nov | بوابة التكنولوجيا المالية | صافي أرباح «فوري» يرتفع 32.2% إلى 2.69 مليار جنيه والإيرادات تسجل 8.35 مليار خلال 9 أشهر
  https://fintechgate.net/257468
  > صافي أرباح «فوري» يرتفع 32.2% إلى 2.69 مليار جنيه والإيرادات تسجل 8.35 مليار خلال 9 أشهر [Figures on the page: consolidated; nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Sat 14 Nov | جريدة المطور | بنك ABC مصر يطلق خصمًا فوريًا 10% على مشتريات أمازون لحاملي بطاقات Visa الائتمانية
  https://almotawwer.com/bankers/334104/
  > في إطار المنافسة المتزايدة بين البنوك العاملة في السوق المصرية على جذب العملاء وتنشيط استخدام البطاقات المصرفية، أعلن بنك ABC مصر عن إطلاق عرض ترويجي جديد يتيح لحاملي بطاقات Visa الائتمانية الحصول على خصم فوري يصل إلى 10% عند التسوق عبر منصة أمازون، في خطوة تستهدف زيادة الاعتماد على المدفوعات الإلكترونية وتوسيع قاعدة استخدام الخدمات ...
- Fri 13 Nov | بوابة التكنولوجيا المالية | سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية
  https://www.fintechgate.net/257376
  > سهم «فوري» يواصل الصعود للأسبوع الثاني ويربح 1.74 مليار جنيه في البورصة المصرية واصل سهم شركة «فوري لتكنولوجيا البنوك والمدفوعات الإلكترونية» تعزيز مكاسبه في البورصة المصرية للأسبوع الثاني على التوالي خلال تعاملات شهر نوفمبر الحالي، مستفيدًا من موجة الصعود التي شهدتها السوق وارتفاع مؤشراتها الرئيسية والثانوية، وسط أداء إيجابي للأسهم القيادية وتحسن شهية المستثمرين للشراء.
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
## HRHO  (4 leads)
- Fri 13 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 13 Nov | www.marketscreener.com | EFG-Hermes Brokerage Boosts Americana Restaurants International's PT, Keeps at Buy
  https://www.marketscreener.com/news/efg-hermes-brokerage-boosts-americana-restaurants-international-s-pt-keeps-at-buy-ce785ed9de8ef227
  (page: did not load (403))
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
- Thu 12 Nov | TradingView | Juhayna Food Industries Q3 2026 Earnings Call Is Live
  https://www.tradingview.com/news/urn:live_audio:quartr.com:798948:0-juhayna-food-industries-q3-2026-earnings-call-is-live/
  > Juhayna Food Industries Q3 2026 Earnings Call Is Live Juhayna Food Industries's quarterly earnings call has just begun.
- Thu 12 Nov | شبكة تواصل الإخبارية | 2.03 مليار جنيه أرباح جهينة .. ماذا تعني طفرة الأغذية لسياحة الفنادق بمصر؟
  https://twaslnews1.twaslnews.com/7553230/
  (page: did not load (403))
## ALCN  (1 leads)
- Sat 14 Nov | الجريدة العقارية | موانئ أبوظبي تستهدف 90% من "الإسكندرية لتداول الحاويات" بسعر أعلى
  https://www.aleqaria.com.eg/post/details/337319/موانئ-أبوظبي-تستهدف-90-من-الإسكندرية-لتداول-الحاويات-بسعر-أعلى
  > رفعت مجموعة موانئ أبوظبي عرضها غير المباشر للاستحواذ على شركة الإسكندرية لتداول الحاويات والبضائع المدرجة في البورصة المصرية، في خطوة تمثل ثاني محاولة للسيطرة على أحد أكبر مشغلي محطات الحاويات في البلاد، حيث تقدمت بعرض شراء إجباري يصل إلى 90% من أسهم الشركة، بزيادة تقارب 20% مقارنة بعرضها السابق.
## MFPC  (1 leads)
- Sat 14 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## EAST  (5 leads)
- Thu 12 Nov | الجريدة العقارية | أرباح الشرقية للدخان ترتفع إلى 8.98 مليار جنيه خلال أول 9 أشهر من 2026
  https://www.aleqaria.com.eg/post/details/357800/أرباح-الشرقية-للدخان
  (page: only 67 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 12 Nov | Pioneers Misr | مورجان ستانلي تستبعد سهم «الشرقية للدخان» من مؤشر مصر القياسي وتضيف سهم «المصرية للاتصالات»
  https://pioneersmisr.com/123554/
  > أعلنت مؤسسة مورجان ستانلي كابيتال إنترناشيونال «MSCI» انضمام سهم الشركة المصرية للاتصالات إلى مؤشر «MSCI Egypt» ضمن مؤشرات الأسواق العالمية القياسية، مقابل استبعاد سهم الشركة الشرقية للدخان، وذلك في إطار المراجعة الدورية لمؤشرات الأسواق العالمية لشهر نوفمبر 2026.
- Thu 12 Nov | أموال الغد | «MSCI» تضم المصرية للاتصالات إلى مؤشرها القياسي وتستبعد الشرقية للدخان في مراجعة نوفمبر
  https://amwalalghad.com/2026/11/12/msci-تضم-المصرية-للاتصالات-إلى-مؤشرها-ا/
  > أعلنت مؤسسة مورجان ستانلي كابيتال إنترناشيونال «MSCI» انضمام سهم الشركة المصرية للاتصالات إلى مؤشر MSCI Egypt، ضمن مؤشرات MSCI العالمية القياسية (Global Standard Indexes)، مقابل استبعاد سهم الشركة الشرقية للدخان، وذلك في إطار نتائج المراجعة الدورية لمؤشرات الأسواق العالمية لشهر نوفمبر 2026.
## EFIH  (8 leads)
- Sat 14 Nov | followict | وزير الاتصالات يشهد توقيع بروتوكول تعاون مشترك مع النيابة العامة ووزارة التضامن الاجتماعي و«أورنچ» و«إي فاينانس»
  https://followict.news/وزير-الاتصالات-يشهد-توقيع-بروتوكول-تع-3/
  > شهد المهندس/ رأفت هندي وزير الاتصالات وتكنولوجيا المعلومات، والمستشار/ محمد شوقي عياد، النائب العام، والدكتورة/ مايا مرسي وزيرة التضامن الاجتماعي احتفالية النيابة العامة تحت عنوان “رحلة النيابة العامة من العدالة الرقمية إلى العدالة الذكية”، والتي عُقدت بمقر مكتب النائب العام.
- Sat 14 Nov | www.youlyou.com | وزير الاتصالات يشهد توقيع بروتوكول تعاون مع النيابة العامة والتضامن وأورانج و إي فاينانس لتطوير الخدمات الرقمية
  https://www.youlyou.com/94422
  > - توقيع بروتوكول تعاون خماسي لتطوير الخدمات الرقمية. - افتتاح مركز بيانات الذكاء الاصطناعي بالنيابة العامة. شهد المهندس رأفت هندي، وزير الاتصالات وتكنولوجيا المعلومات، توقيع بروتوكول تعاون مشترك بين الوزارة والنيابة العامة ووزارة التضامن الاجتماعي، وشركتي «أورانج مصر» و«إي فاينانس»، بهدف تعزيز توظيف التقنيات الحديثة في تطوير الخدمات الحكومية وتيسير وصول المواطنين إليها.
- Sat 14 Nov | جريدة النهار المصرية | بروتوكول تعاون يجمع الاتصالات والنيابة العامة والتضامن و«أورانج» و«إي فاينانس»
  https://www.alnaharegypt.com/1204523
  > خلال احتفالية النيابة العامة وافتتاح مركز بيانات النيابة العامة للذكاء الاصطناعي بروتوكول تعاون يجمع الاتصالات والنيابة العامة والتضامن و«أورانج» و«إي فاينانس»
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
- Sun 15 Nov | صدى البلد | خبير: طرح بنك القاهرة بقيمة 36 مليار جنيه دفعة قوية لبرنامج الطروحات الحكومية
  https://www.elbalad.news/7181046
  > أكد الدكتور حسام عيد، الخبير الاقتصادي ومحلل أسواق المال، أن برنامج الطروحات الحكومية، واختيار بنك القاهرة ليكون أحد أبرز الطروحات المرتقبة، يمثل خطوة إيجابية لدعم سوق المال المصري، خاصة في ظل القيمة المستهدفة للطرح التي تبلغ نحو 36 مليار جنيه، بما يعزز من عمق السوق ويرفع من قدرته على جذب المزيد من الاستثمارات المحلية والأجنبية.
- Sun 15 Nov | شبكة تواصل الإخبارية | المدعى عليهم: أردنيون.. أقامها: بنك القاهرة عمان (أسماء)
  https://twaslnews1.twaslnews.com/7707790/
  (page: did not load (403))
- Sun 15 Nov | المصري اليوم | بنك القاهرة يقفز بأرباحه إلى 13.1 مليار جنيه.. ويقود تحالفًا لتمويل مشروع عقارى بـ 3.2 مليار
  https://www.almasryalyoum.com/news/details/4410650
  > بنك القاهرة يقفز بأرباحه إلى 13.1 مليار جنيه.. ويقود تحالفًا لتمويل مشروع عقارى بـ 3.2 مليار [Figures on the page: consolidated; unaudited or preliminary; nine months. Check which one each figure is.]
## EGAL  (1 leads)
- Sat 14 Nov | https://ekhbary24.com/ | مصر للألومنيوم تحقق 4.93 مليار جنيه أرباحاً في 3 أشهر
  https://ekhbary24.com/article/53511
  > أعلنت شركة مصر للألومنيوم، التابعة للشركة القابضة للصناعات المعدنية، ارتفاع صافي أرباحها بنسبة 104% خلال الربع الأول من العام المالي 2026-2027، لتسجل 4.93 مليار جنيه مقابل 2.41 مليار جنيه في الفترة المماثلة من العام السابق.
## AMOC  (4 leads)
- Sat 14 Nov | المصري اليوم | «أموك» تستعد لمضاعفة الحصيلة الدولارية وتوسعات جديدة لزيادة الإنتاج وتنويع المنتجات
  https://www.almasryalyoum.com/news/details/4410264
  > «أموك» تستعد لمضاعفة الحصيلة الدولارية وتوسعات جديدة لزيادة الإنتاج وتنويع المنتجات عقدت شركة الإسكندرية للزيوت المعدنية «أموك» اجتماع الجمعية العامة غير العادية، اليوم، برئاسة الكيميائي ماجد الكُردي، رئيس مجلس الإدارة والعضو المنتدب، بحضور قيادات الهيئة المصرية العامة للبترول وممثلي المساهمين وأعضاء مجلس الإدارة.
- Sat 14 Nov | عالم الطاقة | أموك تعتمد تعديل بعض مواد النظام الأساسي خلال اجتماع الجمعية العامة غير العادية
  https://www.alamaltaqa.com/52243
  (same wording as the المصري اليوم story above: one source, not two)
- Sat 14 Nov | المستقبل اليوم | أموك تُقر تعديل 5 مواد من نظامها الأساسي وتدرس تنفيذ توسعات إنتاجية
  https://www.elmostqpalelyuom.com/39099
  > أموك تُقر تعديل 5 مواد من نظامها الأساسي وتدرس تنفيذ توسعات إنتاجية أقرت الجمعية العامة غير العادية لشركة الإسكندرية للزيوت المعدنية «أموك»، خلال اجتماعها اليوم السبت 14 نوفمبر 2026، تعديل المواد 7 و21 و28 و46 و56 من النظام الأساسي للشركة.
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
- Sun 15 Nov | KuCoin | Apple stock reaches $360.18, surpassing NVIDIA in market cap by $1.3 trillion
  https://www.kucoin.com/news/flash/apple-stock-hits-360-18-surpasses-nvidia-in-market-cap-by-1-3t
  > stock market opened tonight, Apple's stock price rose 1.49% to $360.18 per share (IT Home note: approximately RMB 2,407 at current exchange rates), reaching a new high, with a total market capitalization of $5.24 trillion (approximately RMB 35.03 trillion at current exchange rates).
- Sat 14 Nov | The Motley Fool | Apple's Market Value Grew From $350 Billion to $4 Trillion During Tim Cook's 15 Years as CEO. Here's What That Growth Curve Means for Apple's Next Chapter Under John Ternus
  https://www.fool.com/investing/2026/11/14/apples-market-value-grew-from-350-billion-to-4-trillion-during-tim-cooks-15-years-as-ceo-heres-what-that-growth-curve-means-for-apples-next-chapter-under-john-ternus/
  > At the end of August, Tim Cook stepped down as CEO of Apple (AAPL +0.39%), ending a highly successful tenure as the head of one of the world's largest companies. Tim Cook led Apple as it revolutionized the tech sector and became the world's first trillion-dollar company.
- Sat 14 Nov | shattered.io | Apple Stock Leads Magnificent Seven With 30.5% Gain
  https://shattered.io/apple-leads-magnificent-seven-30-5-percent-gain-aapl/
  > Apple (NASDAQ: AAPL) is the best-performing Magnificent Seven stock of 2026, according to the performance tables and calculations in coverage from outlets including Foreign Policy Journal and Engadget. One calculation puts the gain at 30.5% through the November 12, 2026 close, with the stock moving from $271.86 on December 31, 2025 to $354.88.
## MSFT  (8 leads)
- Sat 14 Nov | JournalArta | Microsoft Outage Didn’t Lose Your Email, but Firms May Get Credits
  https://journalarta.com/en/2026/11/14/microsoft-outage-didnt-lose-your-email-credits-network-upgrade/
  > Microsoft Outage Didn’t Lose Your Email, but Firms May Get Credits Microsoft says its outage, which began midday Thursday and hit Outlook and other workplace apps worldwide, did not delete email. Messages keep retrying for 48 hours.
- Sat 14 Nov | TradingKey | Why Is Microsoft Stock Surging Today? Azure Growth Hits 43% as MSFT Targets $560 Next
  https://www.tradingkey.com/analysis/stocks/us-stocks/262072017-why-microsoft-stock-surging-azure-ai-growth-msft-560-forecast
  > Why Is Microsoft Stock Surging Today? Azure Growth Hits 43% as MSFT Targets $560 Next Microsoft shares rallied following a strong fiscal fourth-quarter performance, where revenue of $90 billion and adjusted earnings of $4.74 per share surpassed analyst estimates. [Figures on the page: standalone; one quarter. Check which one each figure is.]
- Sat 14 Nov | Yahoo Finance | Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet
  https://finance.yahoo.com/markets/stocks/articles/billionaire-bill-ackman-says-huge-150502419.html
  > Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet The stock market hasn't been as keen on the hyperscalers in 2026 as it was in years past.
## NVDA  (8 leads)
- Sun 15 Nov | Yahoo Finance | Forget Former Nvidia CEO Jensen Huang -- This Is the Real Question Investors Need to Ask About Nvidia Stock
  https://finance.yahoo.com/markets/stocks/articles/forget-former-nvidia-ceo-jensen-073002643.html
  > Forget Former Nvidia CEO Jensen Huang -- This Is the Real Question Investors Need to Ask About Nvidia Stock Jensen Huang, who co-founded Nvidia (NASDAQ:NVDA) over three decades ago at a Denny's restaurant, is officially out as CEO of the artificial intelligence (AI) chip giant.
- Sun 15 Nov | Yahoo Finance | Nvidia's Jensen Huang Is 'Irreplaceable' And Worth $1 Trillion To The Story, Says Dan Ives Amid Support From Elon Musk, Gavin Baker And Others
  https://finance.yahoo.com/technology/ai/articles/nvidias-jensen-huang-irreplaceable-worth-063909067.html
  > Nvidia's Jensen Huang Is 'Irreplaceable' And Worth $1 Trillion To The Story, Says Dan Ives Amid Support From Elon Musk, Gavin Baker And Others - Ives noted that Nvidia faces an unusually significant leadership dependency, describing Huang as potentially the most consequential executive at any company.
- Sun 15 Nov | Yahoo Finance | AMD Has Two Big Catalysts Lined Up For 2027 — And Nvidia Should Be Watching, Says IO Fund
  https://finance.yahoo.com/markets/stocks/articles/amd-two-big-catalysts-lined-055325943.html
  > - IO Fund said AMD's two strategic product launches, which is the company's lineup of Venice server CPUs and Helios MI400-series AI accelerators, are exceeding the chipmaker's initial expectations.
- Sun 15 Nov | Yahoo Finance | Nvidia earnings — along with the baggage — top next week's markets
  https://finance.yahoo.com/markets/stocks/articles/nvidia-earnings-along-baggage-top-053700154.html
  > Time was that earnings reports from chip giant Nvidia provided moments of celebration for the extraordinary success of a U.S. original who led it for 33 years.
- Sun 15 Nov | Yahoo Finance | Michael Burry sees 2 chip winners in Nvidia’s shake-up
  https://finance.yahoo.com/markets/stocks/articles/michael-burry-sees-2-chip-033300677.html
- Sun 15 Nov | Yahoo Finance | Broadcom Jumped as Nvidia Fell. This Is What Has Investors Excited.
  https://finance.yahoo.com/markets/stocks/articles/broadcom-jumped-nvidia-fell-investors-022002767.html
- Sun 15 Nov | Forbes | Investing Expert On Nvidia: ‘People Will Wish They Bought’
  https://www.forbes.com/sites/johnkoetsier/2026/11/14/investing-expert-on-nvidia-people-will-wish-they-bought/
- Sat 14 Nov | The Motley Fool | Nvidia's Ousted CEO Said a 1-Gigawatt Data Center Delay Costs $10 Billion a Quarter. Here's Why That Matters for Power Stocks.
  https://www.fool.com/investing/2026/11/14/nvidias-ousted-ceo-said-a-1-gigawatt-data-center/
## AMZN  (8 leads)
- Sun 15 Nov | TipRanks | Amazon Earnings Call Highlights AI-Led Growth and Margins
  https://www.tipranks.com/news/company-announcements/amazon-earnings-call-highlights-ai-led-growth-and-margins
  (page: did not load (403))
- Sat 14 Nov | Crypto Briefing | Amazon named as Fermi’s 600 MW customer for Project Matador
  https://cryptobriefing.com/amazon-fermi-600-mw-project-matador/
  > The Financial Times identified Amazon as the hyperscaler behind Fermi's $200 million prepayment deal, and the stock jumped Fermi spent Thursday describing its newest customer as an unnamed “investment-grade hyperscaler.” By Friday, the Financial Times had supplied the name: Amazon.
- Sat 14 Nov | Yahoo Finance | Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet
  https://finance.yahoo.com/markets/stocks/articles/billionaire-bill-ackman-says-huge-150502419.html
  > Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet The stock market hasn't been as keen on the hyperscalers in 2026 as it was in years past.
## GOOGL  (8 leads)
- Sat 14 Nov | Yahoo Finance | He Thinks His $200,000 S&P 500 401(k) Spreads His AI Risk. Two Alphabet Share Classes Put $10,380 in One Company. A 20% Drop Could Cost Him $2,076
  https://finance.yahoo.com/markets/stocks/articles/thinks-200-000-p-500-230346273.html
  > - S&P 500 funds list GOOGL and GOOG separately, hiding a combined 5% stake in Alphabet that exposes a $200,000 account to about $10,000 of single-company risk. - Alphabet's third-quarter capital spending jumped 114% to $51 billion, pushing free cash flow negative, so AI-driven swings now matter more to retirement balances.
- Sat 14 Nov | TradingKey | Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?
  https://www.tradingkey.com/analysis/stocks/us-stocks/262008961-alphabet-googl-stock-price-forecast-2026-google-cloud-tradingkey
  > Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short? Alphabet’s Q1 2026 results exceeded expectations with $109.9 billion in revenue (+22% YoY). Google Cloud hit $20.03 billion (+63% YoY) with a record $462 billion backlog, signaling strong demand.
- Sat 14 Nov | Yahoo Finance | Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet
  https://finance.yahoo.com/markets/stocks/articles/billionaire-bill-ackman-says-huge-150502419.html
  > Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet The stock market hasn't been as keen on the hyperscalers in 2026 as it was in years past.
## META  (8 leads)
- Sun 15 Nov | KuCoin | Trade outlook for Meta Platforms, Inc. - Class A Common Stoc
  https://www.kucoin.com/news/insight/META/6af93d0640903b0007ae1c1b
  > Trade outlook for Meta Platforms, Inc. - Class A Common Stock over the next hours #Autochartist #Meta Platforms, Inc.
- Sat 14 Nov | Admirals | Meta Stock After the €805m Italy Fine: What It Means
  https://admiralmarkets.com/education/articles/shares/meta-stock-italy-fine-805-million
  (page: did not load (403))
- Sat 14 Nov | Kalkine Media | Meta (NASDAQ:META) Connects The World: What Comes Next?
  https://kalkinemedia.com/us/stocks/communication/meta-nasdaqmeta-connects-the-world-what-comes-next
  > - The stock moved higher in the latest session. - Favorable ratings dominate coverage. (NASDAQ:META) Communication Services Meta Platforms Inc. (NASDAQ:META) 621.27 USD -7.500 1.193% Last Updated at: 2026-11-12T15:17:00Z operates some of the world's most widely used digital platforms, connecting people through photo sharing, messaging, and other online services.
- Sat 14 Nov | Simply Wall St | Meta Platforms (META) Is Held Liable For Algorithm Driven Harms
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/meta-platforms-meta-is-held-liable-for-algorithm-driven-harm
  > Meta Platforms (NasdaqGS:META) has signed multi year supply deals with Stegra, Sublime Systems, and Nevoya to source green steel, low carbon cement, and electric trucking capacity. The agreements target emissions tied to Meta's data center and office construction, as well as product logistics across its global supply chain.
- Sat 14 Nov | Investing.com Nigeria | Form 4 Meta Platforms Inc For: 14 November By Investing.com
  https://ng.investing.com/news/stock-market-news/form-4-meta-platforms-inc-for-14-november-93CH-2808020
- Sat 14 Nov | Investing.com | Italy fines Meta €805 million over access to Android users’ photos
  https://www.investing.com/news/stock-market-news/italy-fines-meta-805-million-over-access-to-android-users-photos-5027370
- Sat 14 Nov | The Globe and Mail | Billionaire Bill Ackman Says There’s a Huge Disconnect in Wall Street’s Expectations for Amazon, Microsoft, Meta, and Alphabet
  https://www.theglobeandmail.com/investing/markets/stocks/MSFT/pressreleases/8837737/billionaire-bill-ackman-says-theres-a-huge-disconnect-in-wall-streets-expectations-for-amazon-microsoft-meta-and-alphabet/
- Sat 14 Nov | Yahoo Finance | Meta Is Testing a Prediction-Market App With Its Employees
  https://finance.yahoo.com/technology/articles/meta-testing-prediction-market-app-142245481.html
## TSLA  (8 leads)
- Sun 15 Nov | Admirals | Tesla Cybercab at $29,990: Orders, Fees and TSLA Impact
  https://admiralmarkets.com/education/articles/shares/tesla-cybercab-price-orders-tsla
  (page: did not load (403))
- Sat 14 Nov | Yahoo Finance | Elon Musk's Tesla and SpaceX Lost More Than $420 Billion in Combined Market Value in Two Days After Democrats Swept the Midterms, With Investors Fearing New Congressional Probes. Here's Why That Poli
  https://finance.yahoo.com/markets/stocks/articles/elon-musks-tesla-spacex-lost-224802258.html
  > Elon Musk's Tesla and SpaceX Lost More Than $420 Billion in Combined Market Value in Two Days After Democrats Swept the Midterms, With Investors Fearing New Congressional Probes. Here's Why That Political Risk Matters for Shareholders Elon Musk-led publicly traded corporations, Tesla (NASDAQ:TSLA) and Space Exploration Technologies (NASDAQ:SPCX), remain volatile.
- Sat 14 Nov | Yahoo Finance | Tesla opens Cybercab pre-orders ‘for personal use,’ with geo restrictions and a $299 monthly fee
  https://finance.yahoo.com/technology/articles/tesla-opens-cybercab-pre-orders-200444578.html
  > Tesla said on Friday evening that "select customers" now have the opportunity to pre-order the company's autonomous, golden Cybercab "for personal use." More details became clear as those select customers looked at the order page. The estimated delivery date is December 2026.
## JPM  (8 leads)
- Sat 14 Nov | Briefs Finance | JPMorgan Card Chief Allison Beer to Depart
  https://www.briefs.co/news/jpmorgan-s-allison-beer-to-exit-with-successor-for-card-unit/
  > Allison Beer, who joined JPMorgan in 2017, is departing to take a role outside the bank.
- Sat 14 Nov | Bloomberg.com | JPMorgan Loses Card Chief Allison Beer to ‘External Opportunity’
  https://www.bloomberg.com/news/articles/2026-11-14/jpmorgan-loses-card-chief-allison-beer-to-external-opportunity
  (page: did not load (403))
- Sat 14 Nov | Simply Wall St | Raised NII Outlook Might Change The Case For Investing In JPMorgan Chase Stock (JPM)
  https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/raised-nii-outlook-might-change-the-case-for-investing-in-jp
  > JPMorgan Chase has declared dividends on its Series II, OO and PP preferred stock and raised a wide slate of fixed rate bond funding across maturities from 2033 to 2056, including callable and senior unsecured notes priced at 100% of face value.
## XOM  (8 leads)
- Sun 15 Nov | Celebplanes | Exxon Mobil's Gulfstream G650ER N100A lands in Barcelona from Houston in 8 hours 16 minutes
  https://www.celebplanes.com/articles/exxon-mobil-flight-32633
  > Exxon Mobil's Gulfstream G650ER, tail number N100A, landed at Josep Tarradellas Barcelona-El Prat Airport in Spain on Saturday, November 14, 2026, at 22:59 UTC. The aircraft departed George Bush Intercontinental Airport in Houston at 14:43 UTC the same day. The flight took 8 hours and 16 minutes.
- Sun 15 Nov | Kalkine Media | ExxonMobil (NYSE:XOM) Approves Longtail Project. What’s Next?
  https://kalkinemedia.com/us/stocks/energy/exxonmobil-nysexom-approves-longtail-project-whats-next
  > - The Longtail development was approved. - It is the largest phase so far. Few offshore basins have transformed as quickly as the waters of northern South America, and Exxon Mobil Corporation (NYSE:XOM) Energy ExxonMobil Holdings Corporation (NYSE:XOM) 167.93 USD +1.220 0.732% Last Updated at: 2026-11-12T15:38:00Z sits at the center of that growth.
- Sat 14 Nov | Beaumont Enterprise | ExxonMobil Beaumont gives $210,000 to United Way of Beaumont
  https://www.beaumontenterprise.com/news/article/exxonmobile-raises-210-000-united-way-beaumont-22527270.php
  (page: only 35 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## AVGO  (8 leads)
- Sun 15 Nov | Yahoo Finance | Broadcom Jumped as Nvidia Fell. This Is What Has Investors Excited.
  https://finance.yahoo.com/markets/stocks/articles/broadcom-jumped-nvidia-fell-investors-022002767.html
  > Nvidia (NASDAQ:NVDA) has had a rough few days thanks to news breaking about its CEO. However, Broadcom (NASDAQ:AVGO) could be in a strong position to capitalize on it, and the market has already made its opinion known about this potential. Since November began, the S&P 500 is flat.
- Sun 15 Nov | Simply Wall St | Should AI Customer Risk Require Action From Broadcom (AVGO) Investors?
  https://simplywall.st/stocks/us/semiconductors/nasdaq-avgo/broadcom/news/should-ai-customer-risk-require-action-from-broadcom-avgo-in
  > Broadcom is under pressure after concerns resurfaced about its concentration in large AI customers such as OpenAI and Anthropic, including the financing guarantees it provides to support their custom accelerator build outs.
- Sat 14 Nov | The Globe and Mail | Nvidia Fell While AMD and Broadcom Jumped. Here’s What History Says Happens Next to All 3 Stocks.
  https://www.theglobeandmail.com/investing/markets/stocks/AMD/pressreleases/8840702/nvidia-fell-while-amd-and-broadcom-jumped-heres-what-history-says-happens-next-to-all-3-stocks/
  > - Nvidia will likely be fine as a company, even without co-founder Jensen Huang as CEO. - AMD's stock trades at a pricey premium. - Broadcom may be the safest investment of these three chipmakers.
- Sat 14 Nov | BigGo Finance | Nvidia Stock Sinks 11% as Huang Exit Sparks $100B+ Rotation Into AMD, Broadcom and TSMC
  https://finance.biggo.com/news/d48eb2fa-db4e-4958-8f46-ace8b3b1d9ab
  > Nvidia Stock Sinks 11% as Huang Exit Sparks $100B+ Rotation Into AMD, Broadcom and TSMC (NVDA) shares have tumbled about 11% this week after chief executive Jensen Huang resigned Thursday amid reports of two extramarital affairs — one with a woman U.S.
- Sat 14 Nov | TradingView | Notable analyst calls this week: Nvidia, Broadcom and AMD among top picks
  https://www.tradingview.com/news/seekingalpha:ac3c12b71094b:0-notable-analyst-calls-this-week-nvidia-broadcom-and-amd-among-top-picks/
- Sat 14 Nov | Moomoo | Broadcom (AVGO) Stock Week Ahead: Options Flow Braces for a 6.7% Swing by Friday
  https://www.moomoo.com/community/feed/broadcom-avgo-stock-week-ahead-options-flow-braces-for-a-117615225733125
- Sat 14 Nov | Opening Bell Daily | Stock market this week: Broadcom jumps 18.2%
  https://www.openingbelldailynews.com/p/stock-market-this-week-broadcom-18-percent-nov-14-2026
- Sat 14 Nov | Seeking Alpha | Broadcom: Buy AI Growth With A Diversified Company Underneath (NASDAQ:AVGO)
  https://seekingalpha.com/article/4968190-broadcom-buy-ai-growth-with-a-diversified-company-underneath
## BRK.B  (8 leads)
- Sun 15 Nov | Simply Wall St | Why Is Berkshire Hathaway (BRK.A) Issuing $1.1 Billion In Japanese Bonds?
  https://simplywall.st/stocks/us/diversified-financials/nyse-brk.a/berkshire-hathaway/news/why-is-berkshire-hathaway-brka-issuing-11-billion-in-japanes
  > Berkshire Hathaway (NYSE:BRK.A) issued ¥1.1b in yen-denominated bonds in Japan to support its local equity positions. The new bond deal is structured to hedge currency risk tied to Berkshire Hathaway's sizeable portfolio of Japanese stocks.
- Sun 15 Nov | Simply Wall St | Is Berkshire Hathaway (BRK.B) Undervalued Given Its Excess Returns?
  https://simplywall.st/stocks/us/diversified-financials/nyse-brk.b/berkshire-hathaway/news/is-berkshire-hathaway-brkb-undervalued-given-its-excess-retu
  > Berkshire Hathaway has delivered strong share returns in recent years, which puts a spotlight on whether those gains line up with the returns the conglomerate earns on its capital. With the stock now reflecting years of compounding, investors are increasingly asking if the underlying economics of how Berkshire deploys cash still justify today’s price tag.
- Sun 15 Nov | ad-hoc-news.de | Berkshire's Buyback Barometer: Record Relative Strength Meets a Cautious Wall Street Verdict
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-s-buyback-barometer-record-relative-strength-meets-a-cautious-wall-street-verdict/70514623
  > Berkshire Hathaway's stock has just notched its strongest rolling one-month performance against the broader market since February 2010, according to an analysis by Bespoke — a run of relative strength that points to growing investor confidence in Greg Abel's leadership. [Figures on the page: nine months; one quarter. Check which one each figure is.]
## WMT  (8 leads)
- Sat 14 Nov | TradingKey | Walmart Rises Over 10% in Past Month, Nearing 52-Week High: Q3 Earnings May Push Stock to $150
  https://www.tradingkey.com/analysis/stocks/us-stocks/262305681-wmt-walmaert-us-tradingkey
  > Walmart Rises Over 10% in Past Month, Nearing 52-Week High: Q3 Earnings May Push Stock to $150 Walmart shares approach their fiscal 2027 third-quarter earnings report on November 19, following strong second-quarter results driven by e-commerce and profit growth. Technically, the stock is in a short-term pullback phase above key support at $123.46.
- Sat 14 Nov | Yahoo Finance | Walmart just took another step to beat Costco that could backfire
  https://finance.yahoo.com/markets/stocks/articles/walmart-just-took-another-step-143300648.html
  > Walmart and Costco are natural competitors. Both retailers have built their businesses around offering shoppers competitive prices, a wide selection of merchandise, and opportunities to save money. Walmart has increasingly focused on making shopping more convenient, particularly through its growing delivery business.
- Sat 14 Nov | Simply Wall St | Child Labor Settlement Might Change The Case For Investing In Walmart Stock (WMT)
  https://simplywall.st/stocks/us/consumer-retailing/nasdaq-wmt/walmart/news/child-labor-settlement-might-change-the-case-for-investing-i
  > Walmart has agreed to a historic US$7.8 million settlement with Pennsylvania over widespread Child Labor Act violations, along with commitments to tighter monitoring and increased future penalties if new breaches are found.
## V  (8 leads)
- Sat 14 Nov | Stock & Land | Too little, too late: contractors face 22-hour days as visa delays cut staff
  https://www.stockandland.com.au/story/9389896/working-holiday-maker-visa-fix-too-little-too-late-for-some/
  > Subscribe now for unlimited access to all our agricultural news or signup to continue reading The government agreed to speed up the Working Holiday Maker visa process in September after pressure from the National Farmers Federation (NFF) and Victorian Farmers Federation (VFF) to reverse a decision to "go slow" on applications to reduce migration numbers.
- Sat 14 Nov | Yahoo Finance | Card Networks Like Visa and Mastercard Don't Take Credit Losses. American Express Does. Here's Why That Matters for the Stock.
  https://finance.yahoo.com/markets/stocks/articles/card-networks-visa-mastercard-dont-135500020.html
  > Visa and Mastercard enable global commerce to function smoothly, processing trillions of dollars in payment volume on a quarterly basis. But they don't issue cards directly to consumers. So, the leading card networks Visa and Mastercard operate business models that allow them to avoid taking on credit risk and the potential losses this may bring. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Sat 14 Nov | GuruFocus | Is Visa Inc (V) Overvalued After 1.3% Rally? GF Value Says Overv
  https://www.gurufocus.com/news/9199269/is-visa-inc-v-overvalued-after-13-rally-gf-value-says-overvalued
  (page: did not load (403))
## ORCL  (8 leads)
- Sat 14 Nov | Yahoo Finance | Oracle (ORCL): Can Surging Cloud Revenue Outpace Its Financing Burden?
  https://finance.yahoo.com/technology/articles/oracle-orcl-surging-cloud-revenue-192942521.html
  > We just published the list of the 10 AI Infrastructure Stocks to Watch After CoreWeave's Earnings and Oracle Corporation (NYSE:ORCL) ranked 8th on this list. Why Are AI Infrastructure Stocks Under Pressure?
- Sat 14 Nov | The Motley Fool | Could Oracle Hit Its $30 Billion Free Cash Flow Target by Fiscal 2029?
  https://www.fool.com/investing/2026/11/14/could-oracle-hit-its-usd30-billion-free-cash-flow-target-by-fiscal-2029/
  > Oracle (ORCL -1.39%) is attempting to transform extraordinary AI demand into a self-funding growth engine. I examine why its $30 billion fiscal 2029 free cash flow target could dramatically change how investors value the stock, even as a $20 billion financing deal, expensive bonds, and shareholder dilution complicate the picture.
- Sat 14 Nov | TIKR.com | CoreWeave Jumped 20% and Pulled Oracle Higher. Is It Time to Sell, or Load Up?
  https://www.tikr.com/blog/coreweave-jumped-20-and-pulled-oracle-higher-is-it-time-to-sell-or-load-up
  > - Oracle sold $20 billion of stock and bonds days after capping new capital-market funding at that amount through fiscal 2030. - Bloomberg reported that Microsoft is winding down a 2023 deal to rent AI computing from Oracle on older Nvidia chips.
## COST  (8 leads)
- Sat 14 Nov | Investing.com Nigeria | Form 144 COSTCO WHOLESALE CORP /NEW For: 14 November By Investing.com
  https://ng.investing.com/news/stock-market-news/form-144-costco-wholesale-corp-new-for-14-november-93CH-2808114
  (page: did not load (403))
- Sat 14 Nov | Yahoo Finance | Costco solves a problem Sam's Club hasn't figured out yet
  https://finance.yahoo.com/small-business/articles/costco-solves-problem-sams-club-190300162.html
  > Costco has a sort of magic that's not explained simply by the chain's treasure hunt model. Yes, it's fun to shop there with free samples, the cheap food court, and the ever-changing merchandise, but the chain offers members something that's harder to explain.
- Sat 14 Nov | Yahoo Finance | Walmart just took another step to beat Costco that could backfire
  https://finance.yahoo.com/markets/stocks/articles/walmart-just-took-another-step-143300648.html
  > Walmart and Costco are natural competitors. Both retailers have built their businesses around offering shoppers competitive prices, a wide selection of merchandise, and opportunities to save money. Costco, meanwhile, continues to emphasize its in-store experience, giving members reasons to visit and discover products they might not have planned to purchase.
## NFLX  (8 leads)
- Sat 14 Nov | Simply Wall St | Netflix (NFLX) Stock May Be A Bargain Following Channel Store Talk
  https://simplywall.st/stocks/us/media/nasdaq-nflx/netflix/news/netflix-nflx-stock-may-be-a-bargain-following-channel-store/amp
  > Netflix has had a rough stretch in the market, and the drop is forcing investors to ask a simple question: Is the current share price still in line with what the company’s future cash flows can support?
- Sat 14 Nov | Yahoo Finance | Netflix (NFLX) Following Ad Outlook Cuts Still Looks Undervalued To Some Investors
  https://finance.yahoo.com/markets/stocks/articles/netflix-nflx-following-ad-outlook-190805204.html
  > Netflix (NFLX) cut its 2026 ad revenue and free cash flow outlook after delays in rolling out new ad features and partner integrations, putting the streaming group's newer ad-supported model under closer investor scrutiny.
- Sat 14 Nov | Yahoo Finance | Netflix Engagement Growth Is Slowing. Here’s Why I Bought More Anyway.
  https://finance.yahoo.com/markets/stocks/articles/netflix-engagement-growth-slowing-why-180501543.html
  > Netflix (NASDAQ:NFLX) is seeing a decline in the number of hours its members watch. The company's What We Watched report showed a 2% year-over-year increase in total viewing hours in the first half of the year. [Figures on the page: first half; one quarter. Check which one each figure is.]
## INTC  (8 leads)
- Sun 15 Nov | ad-hoc-news.de | Intel's Product Pipeline Faces a Sector-Wide Confidence Test
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/intel-s-product-pipeline-faces-a-sector-wide-confidence-test/70515942
  > Intel shares slipped 2.3% on Friday as unease rippled through the chip sector, with Reuters linking the broader technology weakness to uncertainty surrounding Nvidia following Jensen Huang's departure. Yet the same day brought a concrete product confirmation from Intel — a reminder that company-specific news and sector-wide sentiment are pulling in opposite directions.
- Sun 15 Nov | Seeking Alpha | Intel: Wall Street May Be Underestimating Its Comeback And Nvidia Opportunity (Upgrade)
  https://seekingalpha.com/article/4968345-intel-wall-street-may-be-underestimating-its-comeback-nvidia-opportunity
  (page: did not load (403))
- Sun 15 Nov | Yahoo Finance Singapore | Intel (INTC) Stock Sees Fair Value Falls After Guidance And Operational Issues
  https://sg.finance.yahoo.com/news/intel-intc-stock-sees-fair-031334674.html
  > Intel's latest valuation reset has pulled estimated fair value down from about US$107.21 to about US$90.65, putting fresh focus on how much risk investors are willing to take. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sat 14 Nov | openclassactions.com | Intel Securities Class Action (INTC): Jan. 12 Deadline
  https://openclassactions.com/lawsuits/intel-securities-class-action.php
  > Allegations Only · No Settlement Yet This article describes a class action complaint. Intel has not been found liable, there is no certified class, and [Figures on the page: first half; one quarter. Check which one each figure is.]
- Sat 14 Nov | Yahoo Finance | Why Intel CEO Lip-Bu Tan has 22 meetings a day — and what you can learn from it
  https://finance.yahoo.com/markets/article/why-intel-ceo-lip-bu-tan-has-22-meetings-a-day--and-what-you-can-learn-from-it-210301452.html
- Sat 14 Nov | Kalkine Media | How Is Intel (NASDAQ:INTC) Building Momentum Across Chips?
  https://kalkinemedia.com/us/stocks/technology/how-is-intel-nasdaqintc-building-momentum-across-chips
- Sat 14 Nov | Yahoo Finance | Soros’ Fund Made Intel Its Biggest Stock Bet Right Before It Halved
  https://finance.yahoo.com/markets/stocks/articles/soros-fund-made-intel-biggest-173454289.html
- Sat 14 Nov | TradingKey | Intel Stock Forecast: $20 Billion Offering, AI Growth and Foundry Risks
  https://www.tradingkey.com/analysis/stocks/us-stocks/262103780-intel-stock-forecast-ai-foundry-tradingkey
## LLY  (8 leads)
- Sun 15 Nov | NewsMeter | Eli Lilly eyes $1 billion investment in Hyderabad; CM Revanth woos global pharma investors
  https://newsmeter.in/top-stories/eli-lilly-eyes-1-billion-investment-in-hyderabad-cm-revanth-woos-global-pharma-investors-779351
  > Eli Lilly eyes $1 billion investment in Hyderabad; CM Revanth woos global pharma investors Revanth Reddy said the government was committed to creating an investor-friendly environment and would support entrepreneurs without any discrimination
- Sat 14 Nov | CoinCodex | Eli Lilly Tokenized gStocks (LLYG) Price Prediction 2026, 2027-2030
  https://coincodex.com/crypto/eli-lilly-tokenized-gstocks/price-prediction/
  > | Current Price | $ 1,429.82 | | Price Prediction | $ 1,133.32 (-20.81%) | | Fear & Greed Index | 13 (Extreme Fear) | | 50-Day SMA | - | | 200-Day SMA | - | | 14-Day RSI | (Oversold) | [Figures on the page: unaudited or preliminary; first half. Check which one each figure is.]
- Sat 14 Nov | MarketScale | Lilly breaks ground on $3.5B Pennsylvania injectables plant whose first named drug is still in trials
  https://www.marketscale.com/industries/engineering-and-construction/lilly-breaks-ground-on-35b-pennsylvania-injectables-plant-whose-first-named-drug-is-still-in-trials
  > Lilly breaks ground on $3.5B Pennsylvania injectables plant whose first named drug is still in trials Eli Lilly broke ground on a $3.5 billion injectable medicine and device manufacturing facility in Fogelsville, Pennsylvania, that is expected to be operational by 2031.
Read 105 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO.
