# Desk brief, Thursday, November 19, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 68s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-18 (24.56); Treasury yields to 2026-11-18 (10-year 5.07%).
- **valuation**: ok in 24s (GitHub Actions). LLY: $1.28tn, P/E (last 12 months) 43.3, Forecast P/E (fiscal 2026) 38.7 (the four quarters to Sep 2026)
- **movers**: ok in 7s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-02 XOM results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 turning down, RSI 50.3
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.0%, median P/E 10.2; cheapest MASR +75%, ABUK +48%, PHAR +46%; dearest ARAB -62%, MOIN -65%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 56s (GitHub Actions). 
- **news**: ok in 127s (GitHub Actions). 
- **leads**: ok in 76s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 7 failed, 0 needed a retry (fetch_intraday.py); api.polygon.io: 3 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 1 failed, 8 needed a retry (stock_news.py).

## What moved (latest close against the one before)
- EGX30 51,544.80 (-0.26%); EGX70 EWI 17,564.30 (-0.16%); USD/EGP 53.79 (-0.01%); Gold 21K 5,750.00 (-2.54%); Brent 91.95 (-1.28%); S&P 500 7,323.63 (-0.23%); Nasdaq 24,429.89 (+0.42%); Bitcoin 63,556.00 (-1.45%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): HRHO +5.0%, XOM -4.0%, AMZN +3.8%, AVGO +3.6%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 61, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - COST: In an uptrend: above its 50-day average, which is above the 200-day; RSI 69, neither stretched nor washed out; the 50-day average crossed above the 200-day today.
    - INTC: Turning down: below both its 50-day average (40.7% under) and its 200-day (37.5% under), though the 50-day is still above the 200-day; RSI 29, washed out: below 30; momentum turned up today (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (28.2% under) and its 200-day (25.9% under), though the 50-day is still above the 200-day; RSI 21, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- EGX ZEOT (Extracted Oils & Derivatives) +17.0%; EGX MOSC (Misr Oils & Soap) +12.0%; EGX VERT (Vertika for Industry & Trade) +10.0%; EGX COSG (Cairo Oils & Soap) +9.3%; EGX FIRE (First Investment & Real Estate Development) +8.2%; EGX ADRI (Arab Development & Real Estate Investment) -5.1%; EGX ICFC (International Co. for Fertilizers & Chemicals) -5.0%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-19 (TradingView's closes; Mubasher's list refused), 200 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (212)
US: the market is trading; kept the saved session
US week and month: US companies worth $10bn or more (822)
EGX30 heatmap: 2026-11-19, 31 members
US heatmap: 2026-11-18, 100 members
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

# US 2026-11-18
## OKTA +12.1%  Okta
- Thu 19 Nov | Invezz | Here’s why SentinelOne, Okta, Zscaler, and Crowdstrike stocks rising today
  https://invezz.com/pk/news/2026/11/19/heres-why-sentinelone-okta-zscaler-and-crowdstrike-stocks-rising-today/
- Thu 19 Nov | Investing.com | Why is Okta stock surging today?
  https://www.investing.com/news/stock-market-news/why-is-okta-stock-surging-today-93CH-5038754
- Thu 19 Nov | Trefis | Why Is Okta Stock Going Up?
  https://www.trefis.com/stock/okta/articles/626897/why-is-okta-stock-going-up/2026-11-19
- Thu 19 Nov | Trefis | What Are Okta Investors Betting On?
  https://www.trefis.com/stock/okta/articles/626826/what-are-okta-investors-betting-on/2026-11-19
## SAIL +10.3%  SailPoint
- Thu 19 Nov | Insider Monkey | SailPoint (SAIL) Is Suddenly on Investors’ Radar. Here’s Why
  https://www.insidermonkey.com/news/sailpoint-sail-is-suddenly-on-investors-radar-heres-why-1867280/?amp=1
- Thu 19 Nov | Yahoo Finance | SailPoint (SAIL) Is Suddenly on Investors’ Radar. Here’s Why
  https://finance.yahoo.com/markets/stocks/articles/sailpoint-sail-suddenly-investors-radar-034916685.html
- Wed 18 Nov | Stock Titan | A proposed sale by SailPoint (SAIL) director James Hagan covers 4,205 shares valued at $84,856.90.
  https://www.stocktitan.net/sec-filings/SAIL/144-sail-point-inc-sec-filing-29e9d14cc51f.html
- Wed 18 Nov | marketscreener.com | 1Kosmos Partners With SailPoint Technology Holdings, Inc. To Secure Workforce Onboarding
  https://www.marketscreener.com/news/1kosmos-partners-with-sailpoint-technology-holdings-inc-to-secure-workforce-onboarding-ce785edddd8af020
## PANW +9.9%  Palo Alto Networks
- Thu 19 Nov | Stocks Down Under | Palo Alto Networks (NASDAQ:PANW) Stock Surges After Earnings Beat and $4.5 Billion AI Deal
  https://stocksdownunder.com/palo-alto-networks-stock-surges-earnings-deal/
- Thu 19 Nov | Morningstar | Palo Alto Earnings: Fears Around AI and AI-Assisted Breaches Drives More Dollars to Firm's Top Line
  https://www.morningstar.com/stocks/palo-alto-earnings-fears-around-ai-ai-assisted-breaches-drives-more-dollars-firms-top-line
- Thu 19 Nov | marketscreener.com | Palo Alto's raised sales forecast powers rally in cybersecurity stocks
  https://www.marketscreener.com/news/palo-alto-s-raised-sales-forecast-powers-rally-in-cybersecurity-stocks-ce785ed2dd8dfe25
- Thu 19 Nov | CNBC | Palo Alto stock jumps on earnings beat and company's big bet on securing open-weight models
  https://www.cnbc.com/2026/11/19/palo-alto-networks-earnings-applied-compute.html
## GNRC +9.9%  Generac Holdings
- Thu 19 Nov | 24/7 Wall St. | High End Generators Are Flying Off The Shelves At Costco After A String Of Unusual Tech Outages. Generac Shares Are Up More Than 50% In 2026
  https://247wallst.com/investing/2026/11/19/high-end-generators-are-flying-off-the-shelves-at-costco-after-a-string-of-unusual-tech-outages-generac-shares-are-up-more-than-50-in-2026/
- Thu 19 Nov | Simply Wall St | Generac Stock Gets A Lift From Top Solar Award Recognition
  https://simplywall.st/stocks/us/capital-goods/nyse-gnrc/generac-holdings/news/generac-stock-gets-a-lift-from-top-solar-award-recognition
- Thu 19 Nov | GuruFocus | Generac Holdings Inc (GNRC) Stock Up 9.9% but GF Value Says Over
  https://www.gurufocus.com/news/9208745/generac-holdings-inc-gnrc-stock-up-99-but-gf-value-says-overvalued-gf-score-89100
- Thu 19 Nov | Yahoo! Finance Canada | Generac Holdings Inc. (GNRC) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/GNRC/
## RBRK +9.3%  Rubrik
- Thu 19 Nov | Yahoo Finance | Why Did Rubrik Stock Jump?
  https://finance.yahoo.com/markets/stocks/articles/why-did-rubrik-stock-jump-123719418.html
- Thu 19 Nov | Investing.com | Why is Rubrik stock surging today?
  https://www.investing.com/news/stock-market-news/why-is-rubrik-stock-surging-today-93CH-5038756
- Thu 19 Nov | Yahoo Finance | What Changed For Rubrik Stock, And What Did Not?
  https://finance.yahoo.com/markets/stocks/articles/changed-rubrik-stock-did-not-110438809.html
- Thu 19 Nov | Simply Wall St | Rubrik Stock In Focus After Product Expansion Across Cloud And Cyber Recovery
  https://simplywall.st/stocks/us/software/nyse-rbrk/rubrik/news/rubrik-stock-in-focus-after-product-expansion-across-cloud-a
## HUM -13.0%  Humana
- Thu 19 Nov | Investing.com Australia | Why is Humana stock sliding today? By Investing.com
  https://au.investing.com/news/stock-market-news/why-is-humana-stock-sliding-today-93CH-4780938
- Thu 19 Nov | Yahoo Finance | Why Is Humana Stock Falling?
  https://finance.yahoo.com/markets/stocks/articles/why-humana-stock-falling-124140173.html
- Thu 19 Nov | Yahoo Finance | Should I Buy Humana Stock Now?
  https://finance.yahoo.com/markets/stocks/articles/buy-humana-stock-now-110859807.html
- Thu 19 Nov | MarketBeat | Humana (NYSE:HUM) Stock Price Breaks Below 50-Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-humana-nyse-hum-stock-price-breaks-below-50-day-moving-average-whats-next-2026-11-19/
## UNH -10.2%  UnitedHealth Group Incorporated
- Thu 19 Nov | Yahoo Finance | Managed Care and Pharmacy Benefit Scale Keep UnitedHealth Group (UNH) Attractively Valued
  https://finance.yahoo.com/healthcare/articles/managed-care-pharmacy-benefit-scale-163905858.html
- Thu 19 Nov | Seeking Alpha | UnitedHealth Leads Sector Sell-Off On Medicare Fraud News - Why I Wouldn't Panic (UNH)
  https://seekingalpha.com/article/4970181-unitedhealth-sector-sell-off-on-medicare-news-i-wouldnt-panic
- Wed 18 Nov | Seeking Alpha | UnitedHealth Group retreats 8% amid proposed Medicare fraud rule (UNH:NYSE)
  https://seekingalpha.com/news/4674301-unitedhealth-group-retreats-8-amid-proposed-medicare-fraud-rule
- Wed 18 Nov | Yahoo Finance | George Soros and 26 Other Big Funds Sold UnitedHealth Last Quarter, While 12 Bought. Who’s Right?
  https://finance.yahoo.com/markets/stocks/articles/george-soros-26-other-big-152324175.html
## CBRS -9.6%  Cerebras Systems
- Thu 19 Nov | Trefis | What Explains The Drop In Cerebras Stock?
  https://www.trefis.com/stock/cbrs/articles/626899/what-explains-the-drop-in-cerebras-stock/2026-11-19
- Thu 19 Nov | Stock Titan | After a $77.9M September sale, a Cerebras Systems (CBRS) officer proposes selling more shares.
  https://www.stocktitan.net/sec-filings/CBRS/144-cerebras-systems-inc-sec-filing-7adb8e0b878d.html
- Thu 19 Nov | Stock Titan | An officer received 52,058 Cerebras Systems (CBRS) shares from a stock award and proposes a sale.
  https://www.stocktitan.net/sec-filings/CBRS/144-cerebras-systems-inc-sec-filing-23c182884f19.html
- Wed 18 Nov | MarketBeat | Top Cerebras Systems (CBRS) Competitors 2026
  https://www.marketbeat.com/stocks/NASDAQ/CBRS/competitors-and-alternatives/
## ELV -7.6%  Elevance Health
- Thu 19 Nov | Yahoo Finance | What Argus Sees in Elevance Health (ELV) for 2027
  https://finance.yahoo.com/healthcare/articles/argus-sees-elevance-health-elv-154043331.html
- Thu 19 Nov | ad-hoc-news.de | Elevance Health stock upgraded to Buy by Argus
  https://www.ad-hoc-news.de/boerse/news/corporate-news/elevance-health-stock-upgraded-to-buy-by-argus/70536076
- Thu 19 Nov | kalkine.ca | Why Did Elevance Health (NYSE:ELV) Lose 7.63% After the CMS CRUSH Proposal Targeted Medicare Advantage Insurers?
  https://kalkine.ca/news/healthcare/why-did-elevance-health-nyseelv-lose-763-after-the-cms-crush-proposal-targeted-medicare-advantage-insurers
- Thu 19 Nov | Kalkine | Which of the Five Medicare Advantage Stocks Carries the Largest Exposure to the CMS Audit Rule: Centene (NYSE:CNC), Elevance Health (NYSE:ELV), agilon health (NYSE:AGL), UnitedHealth (NYSE:UNH) or Humana (
  https://kalkine.com.au/news/healthcare/which-of-the-five-medicare-advantage-stocks-carries-the-largest-exposure-to-the-cms-audit-rule-centene-nysecnc-elevance-health-nyseelv-agilon-health-nyseagl-unitedhealth-nyseunh-or-humana-n
## DINO -7.2%  HF Sinclair
- Thu 19 Nov | Investing.com Nigeria | HF Sinclair SVP sells $74,876 in common stock By Investing.com
  https://ng.investing.com/news/stock-market-news/hf-sinclair-svp-sells-74876-in-common-stock-93CH-2817879
- Thu 19 Nov | Stock Titan | After more than 30 years at Shell, Shawn Carsten will become HF Sinclair CFO.
  https://www.stocktitan.net/news/DINO/hf-sinclair-appoints-shawn-j-carsten-as-chief-financial-1zdasbe93mqs.html
- Wed 18 Nov | GuruFocus | HF Sinclair Corp (DINO) Shares Fall 7.2% -- GF Value Says Still Overvalued
  https://www.gurufocus.com/news/9208731/hf-sinclair-corp-dino-shares-fall-72-gf-value-says-still-overvalued
- Wed 18 Nov | MarketBeat | HF Sinclair (NYSE:DINO) SVP Matthew Joyce Sells 810 Shares of Stock
  https://www.marketbeat.com/instant-alerts/insider-hf-sinclair-nyse-dino-svp-matthew-joyce-sells-810-shares-of-stock-2026-11-18/
```

## Results to record (results_due.py)
## Out and not yet recorded: write lastResults, and for an Egyptian stock run set_results.py
### WMT
- WMT: 8-K (results release) filed 2026-11-19: https://www.sec.gov/Archives/edgar/data/104169/000010416926000168/wmt-20261119.htm
    Revenue, quarter to 2026-07-31 (10-Q filed 2026-08-28): $186.10bn; a year earlier $175.75bn (+5.9%)
    Net income, quarter to 2026-07-31 (10-Q filed 2026-08-28): $6.37bn; a year earlier $7.03bn (-9.4%)
    Diluted EPS, quarter to 2026-07-31 (10-Q filed 2026-08-28): $0.80; a year earlier $0.88 (-9.1%)
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: NVDA, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-19 CLHO results (expected)
- 2026-11-19 EAST results (expected)  <- write its preview
- 2026-11-19 EFID results (expected)
- 2026-11-19 EFIH results (expected)  <- write its preview
- 2026-11-19 JUFO results (expected)
- 2026-11-19 MSFT dividend
- 2026-11-19 PHDC results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
- due 2026-11-20: Brent stays below $105 while Iran talks continue (on track)
    Views: nothing to change.

## Fair value
- Changed since the last run: EGAL +42% -> +41% (medium -> high).
- In the ten cheapest or dearest with no note: ADIB, MCQE, CSAG, EMFD, SCEM, AMOC, LCSW, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-19. Open each story before using it.
## COMI  (8 leads)
- Thu 19 Nov | فيتو | عنتر قنديل رئيسًا تنفيذيًا لقطاع الرقمنة والتكنولوجيا بالبنك التجاري الدولي CIB
  https://www.vetogate.com/5774043
  > عنتر قنديل رئيسًا تنفيذيًا لقطاع الرقمنة والتكنولوجيا بالبنك التجاري الدولي CIB في خطوة تعكس توجه البنك التجاري الدولي (CIB) نحو تعزيز التكامل بين التكنولوجيا ووحدات الأعمال الرقمية والبيانات والذكاء الاصطناعي، بما يدعم تنفيذ استراتيجيته ويعزز قدراته التنافسية، تولى عنتر قنديل منصب الرئيس التنفيذي لقطاع الرقمنة والتكنولوجيا بالبنك.
- Thu 19 Nov | شبكة تواصل الإخبارية | أرباح تتجاوز 39 مليار جنيه.. صلابة CIB في قلب المشهد المصرفي
  https://twaslnews1.twaslnews.com/7976737/
  (page: did not load (403))
- Thu 19 Nov | مجلة البوصلة الاقتصادية | تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم
  https://alboslanews.com/أسواق-مال/تراجع-العقود-المستقبلية-لـ-egx30-وطلعت-مصطفى-هامشيًا-وانخفاض-البنك-التجاري-الدولي-بنسب-تتخطى-1-اليوم-431143
  > تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم الخميس 19 نوفمبر 2026 -03:56
## TMGH  (7 leads)
- Thu 19 Nov | مجلة البوصلة الاقتصادية | تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم
  https://alboslanews.com/أسواق-مال/تراجع-العقود-المستقبلية-لـ-egx30-وطلعت-مصطفى-هامشيًا-وانخفاض-البنك-التجاري-الدولي-بنسب-تتخطى-1-اليوم-431143
  > تراجع العقود المستقبلية لـ EGX30 و"طلعت مصطفى" هامشيًا.. وانخفاض البنك التجاري الدولي بنسب تتخطى 1% اليوم الخميس 19 نوفمبر 2026 -03:56
- Wed 18 Nov | شبكة تواصل الإخبارية | 18.8 مليار دولار مستهدفات مبيعات طلعت مصطفى في العراق
  https://twaslnews1.twaslnews.com/7916253/
  (page: did not load (403))
- Wed 18 Nov | https://www.youlyou.com/ | طلعت مصطفى تفتح جبهة استثمارية جديدة في العراق.. مدينة عمرانية بـ43 ألف وحدة ومبيعات مستهدفة 18.8 مليار دولار
  https://www.youlyou.com/97501
  > - مشروع طلعت مصطفى في بغداد يمتد على 12.8 مليون متر مربع ويضم 43 ألف وحدة سكنية. - المبيعات التراكمية المستهدفة تصل إلى 18.8 مليار دولار. - المشروع يستهدف إيرادات سنوية متكررة بقيمة 108 ملايين دولار عند اكتماله.
## ETEL  (8 leads)
- Thu 19 Nov | Masrawy | المصرية للاتصالات يهزم الترسانة في عقر داره ويرتقي بجدول الترتيب
  https://www.masrawy.com/sports/sports_news/details/2026/11/19/3081357/المصرية-للاتصالات-يهزم-الترسانة-في-عقر-داره-ويرتقي-بجدول-الترتيب
  > حقق فريق المصرية للاتصالات (وي) فوزًا مهمًا على حساب منافسه الترسانة بنتيجة 2-1، في المباراة التي جمعت الفريقين اليوم الخميس، ضمن منافسات الجولة الثالثة عشرة من دوري المحترفين المصري.
- Thu 19 Nov | تحيا مصر | تامر المهدي: المصرية للاتصالات تنفذ بنية تكنولوجية متطورة بمشروع نيفيرا
  https://www.tahiamasr.com/1107431
  (page: did not load (403))
- Thu 19 Nov | إقرأ نيوز | المصرية للاتصالات: التكنولوجيا تسهِّل حياة سكان «نيفيرا» وتساعد المستثمرين
  https://www.iqraa.news/236209/المصرية-للاتصالات-التكنولوجيا-تسهِّ/
  > قال المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، إن الشركة ستعمل مع كل مستثمر في مشروع «نيفيرا» منذ مرحلة التصميم لاختيار الحلول التكنولوجية التي تتناسب مع احتياجاته وطبيعة نشاطه.
## PHDC  (2 leads)
- Wed 18 Nov | بروبرتي بلس | شركة بالم هيلز تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال أول 9 أشهر من 2026.. بمعدل نمو 18%
  https://propertypluseg.com/شركة-بالم-هيلز-تحقق-مبيعات-جديدة-بقيمة-2/
  > قال ياسين منصور، رئيس مجلس الإدارة التنفيذي لشركة بالم هيلز: “شهدت الأشهر التسعة الأولى من عام 2026 مجموعة جديدة من النتائج القوية. فقد ظل الطلب قوياً على مستوى محفظتنا المتنوعة، وواصلت استراتيجيتنا للنمو المنضبط تحقيق ثمارها.
- Wed 18 Nov | صدى العرب | بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://www.sada-elarab.com/827417
  > بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18% أعلنت شركة بالم هيلز للتعمير تحقيق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال التسعة أشهر الأولى من عام 2026، بمعدل نمو 18% مقارنة بالفترة نفسها من العام الماضي، مدعومة باستمرار قوة الطلب على مشروعات الشركة وتنوع محفظتها العقارية.
## SWDY  (4 leads)
- Wed 18 Nov | جريدة الملتقى الاقتصادي | السويدي الوطنية تخطط للتوسع في 2027 و2028 وتستهدف زيادة إنتاج أنظمة الري المحوري
  https://www.moltakaaliqtisad.online/السويدي-الوطنية-تخطط-للتوسع-في-2027-و2028-وتس/
  (page: did not load (URLError))
- Wed 18 Nov | جريدة المال | السويدي الوطنية تستهدف زيادة إنتاج أنظمة الري المحوري والتوسع بأسواق إفريقيا والشرق الأوسط خلال 2027-2028
  https://almalnews.com/2148326/السويدي-الوطنية-تستهدف-زيادة-إنتاج-أنظمة-الري/
  > كشفت شركة السويدي الوطنية عن خطة نمو وتوسع خلال عامي 2027 و2028، تستهدف زيادة الطاقة الإنتاجية وتطوير المنتجات والدخول في قطاعات جديدة ذات قيمة مضافة، إلى جانب تعزيز وجودها في أسواق إفريقيا والشرق الأوسط، لتلبية الطلب المتزايد على أنظمة الري المحوري والمنتجات المعدنية المستخدمة في المشروعات الزراعية والصناعية ومشروعات البنية التحتية.
- Wed 18 Nov | جريدة باور نيوز الاخبارية | السويدي الوطنية تكشف خطة 2027–2028 لزيادة الإنتاج والتوسع في أسواق إفريقيا والشرق الأوسط
  https://powernews.cc/?p=294405
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## ORAS  (8 leads)
- Thu 19 Nov | جريدة باور نيوز الاخبارية | أوراسكوم كونستراكشون تضع حجر الأساس لمشروع محطة تحلية مياه بالأردن باستثمارات 6.7 مليار دولار
  https://powernews.cc/?p=294466
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تبدأ تشييد واحدة من أكبر محطات تحلية المياه عالمياً في الأردن
  https://cnnbusinessarabic.com/finance-markets/1152977/أوراسكوم-كونستراكشون-تبدأ-تشييد-واحدة-من-أكبر-محطات-تحلية-المياه-عالميا-في-الأردن
  > «أوراسكوم كونستراكشون» تبدأ تشييد واحدة من أكبر محطات تحلية المياه عالمياً في الأردن تاريخ النشر: قبل 3 ساعات أعلنت شركة «أوراسكوم كونستراكشون» وضع حجر الأساس لمشروع تحلية ونقل المياه من العقبة إلى عمّان في الأردن، وهو مشروع ضخم يتضمن إنشاء واحدة من أكبر محطات تحلية المياه على مستوى العالم.
- Thu 19 Nov | Investing.com UK | Earnings call transcript: Orascom Construction posts strong Q3 2026 growth By Investing.com
  https://uk.investing.com/news/stock-market-news/earnings-call-transcript-orascom-construction-posts-strong-q3-2026-growth-93CH-4993437
  (page: did not load (403))
## FWRY  (4 leads)
- Thu 19 Nov | موقع الحرية الإخباري | عبر 46 منفذًا.. الجيزة تُفعّل سداد مستحقات تقنين أراضي أملاك الدولة من خلال «فوري بلس»
  https://alhorianews.com/عبر-46-منفذًا-الجيزة-تُفعّل-سداد-مستحقا/
  > كشف الدكتور أحمد الأنصاري، محافظ الجيزة، عن تفعيل خدمة السداد الإلكتروني عبر منافذ «فوري بلس» لتحصيل كافة المستحقات المالية المتعلقة بملف تقنين أوضاع أراضي أملاك الدولة، وذلك تنفيذًا لأحكام القانون رقم 168 لسنة 2025 ولائحته التنفيذية، وفي إطار خطة المحافظة لتبسيط الإجراءات وتخفيف الأعباء عن المواطنين. بنود السداد المتاحة دون الذهاب للمقار الحكومية
- Thu 19 Nov | بوابة المصرف | 10 بروتوكولات لتحديث التجارة الخارجية.. فوري وفيزا ومايكروسوفت ضمن الشركاء
  https://www.almasraf.news/10-بروتوكولات-لتحديث-التجارة-الخارجية/
  > وقّع المختبر التنظيمي ومركز الابتكار لتكنولوجيا التجارة (TradeTech Sandbox) 10 بروتوكولات تعاون مع مؤسسات وشركات مصرية ودولية، لتسريع تحديث التجارة الخارجية وتطوير حلول رقمية تستهدف تقليل الوقت والتكلفة المرتبطين بالإجراءات التجارية. وتضم الشراكات شركات متخصصة في التكنولوجيا والاتصالات والمدفوعات والخدمات المالية، من بينها فوري وفيزا ومايكروسوفت. 10 بروتوكولات تجمع شركات التكنولوجيا والمدفوعات لتطوير التجارة
- Thu 19 Nov | آراب فاينانس | فوري وفيزا ومايكروسوفت ضمن 10 جهات تتعاون مع الحكومة لتطوير التجارة الخارجية
  http://www.arabfinance.com/ar/news/newdetails/فوري-وفيزا-ومايكروسوفت
  > آراب فاينانس: تتعاون شركات فوري لتكنولوجيا البنوك والمدفوعات الالكترونية (FWRY) وفيزا ومايكروسوفت واتصالات مصر وإي فاينانس للاستثمارات المالية والرقمية (EFIH) مع وزارة الاستثمار والتجارة الخارجية وعدد من المؤسسات المحلية والدولية، لتطوير حلول تكنولوجية مبتكرة تدعم تحديث منظومة التجارة الخارجية في مصر، وذلك من خلال 10 بروتوكولات تعاون جرى توقيعها ضمن إطلاق المختبر التنظيمي ومركز الابتكار ...
## ABUK  (2 leads)
- Wed 18 Nov | Solarbytes | AOI signs 3 MW solar plant contract with Abu Qir Fertilizers
  https://solarbytes.info/emea-bytes/aoi-signs-3-mw-solar-plant-contract-with-abu-qir-fertilizers-12820027
  > A contract for solar power plants in Alexandria Governorate has been signed by the Arab Organization for Industrialization (AOI), an Egypt-based industrial organisation, with Abu Qir Fertilizers. Under that contract, AOI will supply and install the second phase of the plants, which are to have a total capacity of about 3 MW.
- Wed 18 Nov | ad-hoc-news.de | Abu Qir Fertilizers stock faces gas cost pressure through year-end
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/abu-qir-fertilizers-stock-faces-gas-cost-pressure-through-year-end/70529207
  > Abu Qir Fertilizers faces higher energy costs after Egypt adjusted the price of natural gas supplied to its plants from November 16 through December 31. The company disclosed the measure on Tuesday, November 17, in response to an inquiry from the Egyptian Exchange, according to Ahram Online.
## HRHO  (8 leads)
- Thu 19 Nov | Vietnam.vn | حقيبة هيرميس هي المفضلة لدى ميسي وهالاند.
  https://www.vietnam.vn/ar/chiec-tui-hermes-duoc-long-messi-haaland
  > من ليونيل ميسي وديكلان رايس إلى إيرلينغ هالاند، شوهد العديد من نجوم كرة القدم وهم يحملون حقائب هيرميس الكبيرة، محولين هذه الإكسسوارات الفاخرة إلى جزء لا يتجزأ من أناقتهم خارج الملعب. مع ذلك، فإن العديد من التصاميم التي تحمل اسم "بيركين" هي في الواقع من مجموعة "هوت آ كوروا" (HAC).
- Wed 18 Nov | EnterpriseAM | EFG Holdings and Orascom Construction report their 3Q earnings
  https://enterpriseam.com/egypt/2026/11/19/efg-holdings-and-orascom-construction-report-their-3q-earnings/
  > Our friends at EFG Holding saw their group revenue rise 5% y-o-y to EGP 6.7 bn in 3Q 2026, according to their latest earnings release (pdf). Net income after tax and minority interest fell 15% y-o-y to EGP 720 mn during the quarter. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | EnterpriseAM | "إي إف جي القابضة" وأوراسكوم كونستراكشون تعلنان نتائجهما المالية للربع الثالث
  https://enterpriseam.com/egypt-ar/2026/11/19/إي-إف-جي-القابضة-وأوراسكوم-كونستراكش/
  > ارتفعت إيرادات مجموعة "إي إف جي القابضة" بنسبة 5% على أساس سنوي في الربع الثالث من عام 2026 لتصل إلى 6.7 مليار جنيه، وفقا لبيان نتائج أعمالها (بي دي إف). في المقابل، تراجع صافي أرباح المجموعة بعد خصم الضرائب وحقوق الأقلية بنسبة 15% على أساس سنوي إلى 720 مليون جنيه خلال الربع. [Figures on the page: consolidated; one quarter; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | مجلة أرقام | إي اف چي هيرميس تتم إصدار سندات توريق بقيمة 301 مليون جنيه لصالح «كليڤر»
  https://arqam.news/611208/
  > أعلنت شركة إي اف چي هيرميس، بنك الاستثمار التابع لمجموعة إي اف چي القابضة، إتمام الخدمات الاستشارية لإصدار سندات توريق بقيمة 301 مليون جنيه لصالح شركة كليڤر للتمويل الاستهلاكي (Klivvr)، في أول إصدار توريق للشركة، ضمن برنامجها الأوسع بقيمة إجمالية تبلغ 8 مليارات جنيه.
- Wed 18 Nov | العالم اليوم | كليڤر (Klivvr) تنجح في إتمام أول إصدار لسندات التوريق بقيمة 301 مليون جنيه بالتعاون مع “إي إف چي هيرميس”
  https://alalamelyoum.co/296048/
- Wed 18 Nov | Forbes Middle East | EFG Holding's Q3 Revenue Rises 5% To $124.6M
  https://forbesmiddleeast.com/industry/business/efg-holdings-q3-revenue-grows-5-on-strong-performance-at-hermes-finance
- Wed 18 Nov | Daily News Egypt | EFG Holding third-quarter revenue rises 5% to EGP 6.7bn on growth at EFG Hermes and Valu
  https://dailynewsegypt.com/2026/11/18/efg-holding-third-quarter-revenue-rises-5-to-egp-6-7bn-on-growth-at-efg-hermes-and-valu/
- Wed 18 Nov | Khaleej Times | EFG Holding reports Q3 2026 revenues of EGP 6.7 billion, up 5% Y-o-Y
  https://www.khaleejtimes.com/business/efg-holding-reports-q3-2026-revenues-of-egp-67-billion-up-5-y-o-y
## ALCN  (1 leads)
- Wed 18 Nov | ad-hoc-news.de | Alexandria Container stock posts 16% nine-month profit rise
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/alexandria-container-stock-posts-16-nine-month-profit-rise/70529211
  > Alexandria Container and Cargo Handling reported higher earnings for the nine months ended September 30, 2026, in a filing published by the Egyptian Exchange on November 15. Net income reached EGP 5,722.7 million, compared with EGP 4,951.8 million in the year-earlier period. Revenue increased to EGP 6,772.1 million from EGP 6,340.1 million. [Figures on the page: nine months; one quarter. Check which one each figure is.]
## MFPC  (8 leads)
- Wed 18 Nov | مانكيش نت | موبكو تعلن تعديل مؤقت لأسعار الغاز الطبيعي بنسبة 50%
  https://mangish.net/موبكو-تعلن-تعديل-مؤقت-لأسعار-الغاز-الط/
  > أعلنت شركة مصر لإنتاج الأسمدة «موبكو» أنها قد تلقت إشعارًا رسميًا يُفيد بتعديل أسعار الغاز الطبيعي المستخدم في تشغيل مصانعها، وذلك تنفيذاً لقرار زيادة سعر الغاز المورد لمصانع الأسمدة بنسبة 50% بشكل مؤقت.
- Wed 18 Nov | جريدة آخر الأخبار | موبكو تعلن عن تعديل مؤقت لأسعار الغاز الطبيعي بنسبة 50%
  https://akher.news/1088/موبكو-تعلن-عن-تعديل-مؤقت-لأسعار-الغاز-ا/
  (page: did not load (403))
- Wed 18 Nov | جريدة الدستور | محافظ دمياط يلتقي مجلس إدارة شركة مصر لإنتاج الأسمدة
  https://www.dostor.org/5782339
  (page: did not load (403))
## EFIH  (1 leads)
- Wed 18 Nov | جريدة المال | «الأهلي فاروس» ترفع القيمة العادلة لـ «إي فاينانس» إلى 34.3 جنيه للسهم
  https://almalnews.com/2148141/«الأهلي-فاروس»-ترفع-القيمة-العادلة-لـ-«إي/
  > أصدرت وحدة بحوث «الأهلي فاروس» تقريرًا لشركة «إي فاينانس للاستثمارات المالية والرقمية» رفعت فيه تقديراتها للقيمة العادلة للسهم إلى 34.3 جنيه وفقاً لتقديرات ديسمبر 2026، مع تأكيد توصيتها القوية بشراء السهم الذي يتداول حاليا عند مضاعف ربحية لآخر 12 شهراً يبلغ 26.9 مرة، بقيمة سوقية تصل إلى 86.3 مليار جنيه.
## BQDC  (8 leads)
- Thu 19 Nov | شبابيك | وقف ماكينات atm بنك القاهرة الجمعة.. السبب وموعد عودة الخدمة
  https://shbabbek.com/show/288379
  > وقف ماكينات atm بنك القاهرة الجمعة.. السبب وموعد عودة الخدمة أعلن بنك القاهرة في تنويه رسمي لعملائه عن توقف مؤقت لبعض المعاملات المصرفية، وعلى رأسها ماكينات الصراف الآلي، وذلك فجر غد الجمعة الموافق 20 نوفمبر 2026، لإجراء تحديثات فنية على الأنظمة الإلكترونية للبنك. موعد وقف ماكينات atm بنك القاهرة وعودة الخدمة
- Thu 19 Nov | قناة صدى البلد | بنك القاهرة يعلن توقف بعض الخدمات الإلكترونية لمدة ساعة للصيانة
  https://elbaladtv.net/بنك-القاهرة-يعلن-توقف-بعض-الخدمات-الإل
  > أعلن بنك القاهرة تنفيذ أعمال صيانة دورية على البنية التحتية الداعمة للقنوات الرقمية، يوم الجمعة الموافق 20 نوفمبر 2026، وذلك في إطار حرصه على تعزيز استقرار وكفاءة الخدمات المصرفية المقدمة للعملاء.
- Thu 19 Nov | وطنى | بنك القاهرة: القيام ببعض أعمال الصيانة بخدمات البنك الجمعة20 نوفمبر
  https://www.wataninet.com/2026/11/بنك-القاهرة-القيام-ببعض-أعمال-الصيانة/
  (page: did not load (403))
## SKPC  (2 leads)
- Wed 18 Nov | جريدة باور نيوز الاخبارية | ترقية إسلام زيدان مديرًا عامًا للشئون القانونية بسيدبك مع استمرار ندبه لـ«ووتك»
  https://powernews.cc/?p=294339
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | بترونيوز | بترومنت تجدد عقد الصيانة الشاملة مع سيدبك لتعزيز كفاءة التشغيل واستدامة الأصول
  https://petro-news.com/182015
  (page: did not load (403))
## EFID  (4 leads)
- Thu 19 Nov | Investing.com India | Earnings call transcript: Edita Food posts record Q3 2026 revenue, shares rise By Investing.com
  https://in.investing.com/news/stock-market-news/earnings-call-transcript-edita-food-posts-record-q3-2026-revenue-shares-rise-93CH-5715357
  (page: did not load (403))
- Thu 19 Nov | TradingView | Edita Food Industries Company Q3 2026 Earnings Call Is Live
  https://www.tradingview.com/news/urn:live_audio:quartr.com:800175:0-edita-food-industries-company-q3-2026-earnings-call-is-live/
  > Edita Food Industries Company Q3 2026 Earnings Call Is Live Edita Food Industries Company's quarterly earnings call has just begun.
- Wed 18 Nov | جريدة المال | كريم الشرقاوي: إيديتا تستهدف التوسع في أسواق متعددة وتدرس فرصًا استحواذية لدعم نمو أعمالها
  https://almalnews.com/2148194/كريم-الشرقاوي-إيديتا-تستهدف-التوسع-في-أسواق/
  > قال كريم الشرقاوي، مدير القطاع المالي بمجموعة إيديتا إيجيب، إن المجموعة تستهدف مواصلة التوسع في أسواق متعددة، إلى جانب دراسة فرص الاستحواذ المحتملة، بما يدعم نمو أنشطتها وتعزيز انتشارها الجغرافي خلال الفترة المقبلة.
- Wed 18 Nov | Zawya | Edita’s Q3 profit jumps 41.5% on record sales
  https://www.zawya.com/en/special-coverage/equities/editas-q3-profit-jumps-41.5-on-record-sales-2326603
  > Edita Food Industries (EFID.CA), one of Egypt’s leading packaged snack-food makers, reported a 41.5% year-on-year rise in net profit to EGP 938.1m for the third quarter (Q3) of 2026. Revenues reached EGP 7.3bn, the highest quarterly div in the company’s history. Q3 revenues rose 32.9% from the same quarter of 2025. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## AAPL  (8 leads)
- Thu 19 Nov | Benzinga | Arthur Levinson Sells $32M Of Apple Stock Near 52-Week High
  https://www.benzinga.com/trading-ideas/insider-trades/26/11/63431062/arthur-levinson-sells-32m-of-apple-stock-near-52-week-high
  (page: did not load (403))
- Thu 19 Nov | Yahoo Finance | If Apple Reaches $400, Your $5,000 Investment Would Be Worth This Much
  https://finance.yahoo.com/markets/stocks/articles/apple-reaches-400-5-000-150355893.html
  > - Apple (AAPL) hitting $400 would turn a $5,000 investment into about $5,700, a roughly 14% gain from the latest close. - The model's base case targets $406 within a year, while the bull case reaches $461 and the bear case slips to $342.
- Thu 19 Nov | MarketBeat | Apple's Next Margin Defense Could Be Hiding in Your Wallet
  https://www.marketbeat.com/articles/apples-next-margin-defense-could-be-hiding-in-your-wallet/
  (page: did not load (403))
## MSFT  (8 leads)
- Thu 19 Nov | ad-hoc-news.de | NICE stock: Microsoft integration expands AI agent reach
  https://www.ad-hoc-news.de/boerse/news/corporate-news/nice-stock-microsoft-integration-expands-ai-agent-reach/70537278
  > NiCE expanded its collaboration with Microsoft on November 18, 2026, launching two Cognigy integrations designed to bring AI agents and human employees together in customer-service workflows. The company announced the move in a release carried by the Financial Times.
- Thu 19 Nov | Yahoo Finance | Bill Ackman Says His Microsoft “Sale” Was Really a Swap Into Options
  https://finance.yahoo.com/markets/options/articles/bill-ackman-says-microsoft-sale-162702535.html
  > - Bill Ackman says Pershing Square's Microsoft sale was half a trade: he sold two million shares but bought two million deep-in-the-money options. - Pershing's 13F also shows new stakes in Intercontinental Exchange worth about $1 billion and Alcon worth roughly $954 million.
- Thu 19 Nov | Yahoo Finance | What Makes Microsoft Corporation (MSFT) a Strong Long-Term Bet?
  https://finance.yahoo.com/markets/stocks/articles/makes-microsoft-corporation-msft-strong-162631490.html
  > RiverPark Advisors, an investment advisory firm and sponsor of the RiverPark family of mutual funds, released its "RiverPark Large Growth Fund" Q3 2026 investor letter. The letter can be downloaded here. equity markets rose modestly in the third quarter, with the S&P 500 gaining 2.30% and the Russell 1000 Growth Index increasing 0.92%.
## NVDA  (8 leads)
- Thu 19 Nov | The Motley Fool | Nvidia Stock Could Soar 90% After Jensen Huang's Exit, According to One Wall Street Firm. Is It Time to Buy?
  https://www.fool.com/investing/2026/11/19/nvidia-stock-could-soar-90-after-jensen-huang-s-exit-according-to-one-wall-street-firm-is-it-time-to-buy/
  > By Jonathan Ponciano – - Wedbush raised its Nvidia price target to $293 from $275, nearly double the stock's current price. - Nvidia's revenue rose 103% in its first quarter reported since Jensen Huang resigned, and management raised its outlook for next year.
- Thu 19 Nov | Yahoo Finance | Bill Ackman says Nvidia's board is failing you — and not just because it fired Jensen Huang after one Zoom call, at most
  https://finance.yahoo.com/markets/stocks/articles/bill-ackman-says-nvidias-board-162000364.html
  > Bill Ackman says Nvidia's board is failing you — and not just because it fired Jensen Huang after one Zoom call, at most Billionaire Pershing Square CEO Bill Ackman is joining the growing chorus of Silicon Valley leaders standing in support of disgraced Nvidia (NASDAQ:NVDA) former CEO Jensen Huang.
- Thu 19 Nov | Yahoo Finance | Nvidia, Broadcom, Micron stocks rise leading up to Anthropic's first trade
  https://finance.yahoo.com/markets/article/nvidia-amd-micron-pare-gains-leading-up-to-anthropics-first-trade-155941221.html
  > Chip giant Nvidia (NVDA) gained on Thursday, along with Broadcom (AVGO) and Intel (INTC), as investors prepared for Anthropic to start trading.
- Thu 19 Nov | Barchart.com | Nvidia Could Poach Arm's CEO to Replace Jensen Huang. Here's What That Might Mean for ARM Stock.
  https://www.barchart.com/story/news/8919766/nvidia-could-poach-arm-s-ceo-to-replace-jensen-huang-here-s-what-that-might-mean-for-arm-stock
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Traders Union | Trump disclosure shows Nvidia stock trades amid scrutiny of chip policy ties
  https://tradersunion.com/news/stocks/show/4323685-trump-nvidia-stock-trades-policy/
- Thu 19 Nov | Business Insider | AMD's Lisa Su Speaks Out on Her Cousin Jensen Huang's Nvidia Exit
  https://www.businessinsider.com/amd-lisa-su-jensen-huang-nvidia-resignation-cousin-2026-11
- Thu 19 Nov | Reuters | Trump bought up to $265,000 of Nvidia stock in September, disclosure shows
  https://www.reuters.com/business/trump-bought-up-265000-nvidia-stock-september-disclosure-shows-2026-11-19/
- Thu 19 Nov | Yahoo Finance | Jensen Huang Stepped Away From Nvidia. The Stock Has Crashed. Instead of Rushing to Buy the Dip, Here Are 2 AI Stocks Down More Than 15% to Buy Instead.
  https://finance.yahoo.com/markets/stocks/articles/jensen-huang-stepped-away-nvidia-152702121.html
## AMZN  (8 leads)
- Thu 19 Nov | TipRanks | Amazon Stock (AMZN) Flattens as It Threatens to Leave New York Over Mamdani’s New Delivery Bill
  https://www.tipranks.com/news/amazon-stock-amzn-flattens-as-it-threatens-to-leave-new-york-over-mamdanis-new-delivery-bill
  (page: did not load (403))
- Thu 19 Nov | Yahoo Finance | Instagram creators can now add Amazon affiliate links directly to Reels, posts
  https://finance.yahoo.com/media-advertising/articles/instagram-creators-now-add-amazon-163500147.html
  > This story was originally published on Retail Dive. To receive daily news and insights, subscribe to our free daily Retail Dive newsletter. - Instagram content creators can now promote products via Amazon affiliate links in their feeds and Reels, Instagram and Amazon said in separate posts on Monday.
- Thu 19 Nov | ad-hoc-news.de | Amazon's Ownership Puzzle: A $5 Billion Data-Center Handoff, a 14.7% Anthropic Stake and a Rocket Th
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-ownership-puzzle-a-5-billion-data-center-handoff-a-14-7-anthropic-stake-and-a-rocket-that/70537273
  > Amazon's Monday agreement with Blackstone raises a question bigger than who holds title to a handful of server farms: which pieces of its infrastructure does the company actually need to own?
- Thu 19 Nov | Yahoo Finance | Amazon warns New York labor bill could hike order costs
  https://finance.yahoo.com/economy/policy/articles/amazon-warns-york-labor-bill-154951850.html
  > Amazon warned Thursday that labor protections being considered by the New York City council "could add up to $5 per order," as the retail giant rallied against legislation backed by leftist Mayor Zohran Mamdani.
- Thu 19 Nov | Benzinga | Amazon Stock Moves Higher: What's Going On?
  https://www.benzinga.com/trading-ideas/movers/26/11/63433116/amazon-stock-moves-higher-whats-going-on-3
- Thu 19 Nov | Zacks Investment Research | Can Amazon's Ad Revenue Growth Continue to Underpin the Stock's Value?
  https://www.zacks.com/stock/news/3032569/can-amazons-ad-revenue-growth-continue-to-underpin-the-stocks-value
- Thu 19 Nov | Seeking Alpha | New York City legislation could upend Amazon's delivery model (AMZN:NASDAQ)
  https://seekingalpha.com/news/4674722-new-york-city-legislation-could-upend-amazons-delivery-model
- Thu 19 Nov | Invezz | Anthropic IPO could hand Alphabet and Amazon a windfall, but how long will it last?
  https://invezz.com/news/2026/11/19/anthropic-ipo-could-hand-alphabet-and-amazon-a-windfall-but-how-long-will-it-last/
## GOOGL  (8 leads)
- Thu 19 Nov | Benzinga | What Is Going on With Alphabet Stock on Thursday?
  https://www.benzinga.com/markets/tech/26/11/63440383/what-is-going-on-with-alphabet-stock-on-thursday-2
  (page: did not load (403))
- Thu 19 Nov | Traders Union | Alphabet stock climbs on upward price move as buyers show steady interest
  https://tradersunion.com/news/stocks/show/4323902-alphabet-jumps-2-3percent-to-usd288-95/
  (page: did not load (403))
- Thu 19 Nov | Yahoo Finance | Alphabet (GOOG) Slips as 2026 Capex Outlook Rises
  https://finance.yahoo.com/markets/stocks/articles/alphabet-goog-slips-2026-capex-160741067.html
  > RiverPark Advisors, an investment advisory firm and sponsor of the RiverPark family of mutual funds, released its "RiverPark Large Growth Fund" Q3 2026 investor letter. The letter can be downloaded here. equity markets rose modestly in the third quarter, with the S&P 500 gaining 2.30% and the Russell 1000 Growth Index increasing 0.92%.
## META  (8 leads)
- Thu 19 Nov | Yahoo Finance | Navigating Meta Platforms’ (META) Journey from July Dip to New 52-Week High
  https://finance.yahoo.com/markets/stocks/articles/navigating-meta-platforms-meta-journey-162018276.html
  > RiverPark Advisors, an investment advisory firm and sponsor of the RiverPark family of mutual funds, released its "RiverPark Large Growth Fund" Q3 2026 investor letter. The letter can be downloaded here. equity markets rose modestly in the third quarter, with the S&P 500 gaining 2.30% and the Russell 1000 Growth Index increasing 0.92%.
- Thu 19 Nov | TradingView | Hedge funds take contrasting calls on Meta Platforms
  https://www.tradingview.com/news/seekingalpha:fb6832df3094b:0-hedge-funds-take-contrasting-calls-on-meta-platforms/
  > Hedge funds take contrasting calls on Meta Platforms Hedge funds showed a divided stance on Meta Platforms META in the third quarter, with several high-profile investors aggressively adding to positions even as others pared exposure or exited entirely, according to their recent 13F filings.
- Thu 19 Nov | Benzinga | Meta Short Interest Climbs After Q3 Earnings Report
  https://www.benzinga.com/trading-ideas/short-ideas/26/11/63430497/meta-short-interest-climbs-after-q3-earnings-report
  (page: did not load (403))
## TSLA  (8 leads)
- Thu 19 Nov | Benzinga | Musk Says Tesla-SpaceX Merger Shouldn’t Earn Extra Pay - SpaceX (NASDAQ:SPCX)
  https://www.benzinga.com/markets/prediction-markets/26/11/63440349/tesla-spacex-merger-pay
  (page: did not load (403))
- Thu 19 Nov | ad-hoc-news.de | Tesla stock: Musk signals higher China output
  https://www.ad-hoc-news.de/boerse/news/corporate-news/tesla-stock-musk-signals-higher-china-output/70537137
  > Tesla plans to continue increasing production at its Shanghai plant, according to a Yahoo Finance report published Thursday, November 19, 2026. The report cited a CCTV-affiliated account describing comments by Chief Executive Elon Musk during meetings with officials in Shenzhen.
- Thu 19 Nov | 24/7 Wall St. | Tesla Stock Could Be Worth Much More in 2027. Here’s the Number I’m Watching
  https://247wallst.com/investing/2026/11/19/tesla-stock-could-be-worth-much-more-in-2027-heres-the-number-im-watching/
  > Tesla Stock Could Be Worth Much More in 2027. Here’s the Number I’m Watching Tesla (NASDAQ:TSLA | TSLA Price Prediction) spent 2026 rebuilding its business around autonomy, but the stock has not caught up yet. Shares are down 15.56% year to date at $379.74, and the five-year gain stands at just 4.61%.
## JPM  (8 leads)
- Thu 19 Nov | StreetInsider | Form 424B3 JPMORGAN CHASE & CO
  https://www.streetinsider.com/SEC+Filings/Form+424B3+JPMORGAN+CHASE+&amp;+CO/27375166.html
  (page: did not load (403))
- Thu 19 Nov | Politico | JPMorgan Chase customer emails, names may have been accessed in third-party hack
  https://www.politico.com/news/2026/11/19/jpmorgan-chase-third-party-cyberattack-01175392
  (page: did not load (403))
- Thu 19 Nov | شبكة تواصل الإخبارية | JPMorgan Chase says some customer data may be exposed after its vendors were hit by a cyberattack
  https://twaslnews1.twaslnews.com/7980755/
  (page: did not load (403))
## XOM  (8 leads)
- Thu 19 Nov | Yahoo Finance | Erste Group Upgrades ExxonMobil (XOM). Here’s What Drove It.
  https://finance.yahoo.com/markets/stocks/articles/erste-group-upgrades-exxonmobil-xom-154139627.html
  > We just published a list of the 10 Stocks Analysts Upgraded On Wednesday and ExxonMobil (NYSE:XOM) ranked 8th on this list. Hotter inflation has pushed the Federal Reserve back toward rate increases, and the bond market is repricing around it.
- Thu 19 Nov | Egypt Oil & Gas | Oman Sign $400 Mn Deal with EDO, ExxonMobil for Development of Natural Gas Block
  https://egyptoil-gas.com/news/oman-sign-400-mn-deal-with-edo-exxonmobil-for-development-of-natural-gas-block/
  > The Omani government has signed a concession agreement with Energy Development Oman (EDO) and ExxonMobil to appraise and develop discovered natural gas resources in the Greater Makarem area (Block 20), with initial investments expected to exceed $400 Mn, according to the Omani News Agency (ONA).
- Thu 19 Nov | SaudiGulf Projects | ExxonMobil Enters Oman with $400 Million Block 20 Gas Deal
  https://www.saudigulfprojects.com/2026/11/exxonmobil-energy-oman-400-million-block-20-makarem-gas-concession/
  (page: did not load (403))
- Thu 19 Nov | Arab News | Oman signs $400m gas deal with Energy Oman, ExxonMobil, paving way for multibillion-dollar project
  https://www.arabnews.com/business/oman-signs-400m-gas-deal-with-energy-oman-exxonmobil-paving-way-for-multibillion-dollar-project-3012958
  (page: did not load (403))
- Thu 19 Nov | Egypt Oil & Gas | ExxonMobil Egypt Backs 84 Young Entrepreneurs at INJAZ Al-Arab Competition
  https://egyptoil-gas.com/news/exxonmobil-egypt-backs-84-young-entrepreneurs-at-injaz-al-arab-competition/
- Thu 19 Nov | Industrial Info Resources | ExxonMobil Global Outlook: All Types of Energy Will be Required t...
  https://www.industrialinfo.com/news/article/exxonmobil-global-outlook-all-types-of-energy-will-be-required-to-meet-the-growing-needs--364854
- Thu 19 Nov | TradeWinds News | ExxonMobil’s $30bn Rovuma LNG project for Mozambique advances
  https://www.tradewindsnews.com/gas/exxonmobil-s-30bn-rovuma-lng-project-for-mozambique-advances/2-1-2076760
- Thu 19 Nov | MarketBeat | ExxonMobil (NYSE:XOM) Rating Lowered to "Hold" at Zacks Research
  https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-rating-lowered-to-hold-at-zacks-research-2026-11-19/
## AVGO  (8 leads)
- Thu 19 Nov | Pluang | Broadcom's revenue and AI chip sales soar, but stock remains flat amid downgrade concerns.
  https://pluang.com/en/news-feed/pertumbuhan-chip-ai-broadcom-pendapatan-kas-kuat-meski-downgrade
  (page: did not load (403))
- Thu 19 Nov | TIKR.com | Cathie Wood and 26 Other Big Funds Bought Broadcom Last Quarter. David Tepper and 26 Others Sold. Who’s Right?
  https://www.tikr.com/blog/cathie-wood-and-26-other-big-funds-bought-broadcom-last-quarter-david-tepper-and-26-others-sold-whos-right?
  > - Of the 460 big funds that have filed 13Fs for the quarter ended Sept. 30, 27 bought Broadcom and 27 sold, with Cathie Wood’s ARK Invest among the buyers and David Tepper’s Appaloosa among the sellers.
- Thu 19 Nov | Seeking Alpha | Broadcom Should Lead Investors Out Of This AI Slump (Upgrading To Strong Buy) (AVGO)
  https://seekingalpha.com/article/4970166-broadcom-should-lead-investors-out-of-ai-slump-upgrading-strong-buy
  (page: did not load (403))
- Thu 19 Nov | Yahoo Finance | Nvidia, Broadcom, Micron stocks rise leading up to Anthropic's first trade
  https://finance.yahoo.com/markets/article/nvidia-amd-micron-pare-gains-leading-up-to-anthropics-first-trade-155941221.html
  > Chip giant Nvidia (NVDA) gained on Thursday, along with Broadcom (AVGO) and Intel (INTC), as investors prepared for Anthropic to start trading.
- Thu 19 Nov | BigGo Finance | Broadcom's AI Chip Revenue Jumps 221% as Wall Street Trims Its Price Target
  https://finance.biggo.com/news/c90cf5df-373c-4611-963b-cc1e08399f09
- Thu 19 Nov | 24/7 Wall St. | Broadcom’s $13.67B Quarterly FCF Beats Marvell’s Scaling Story, Plain and Simple
  https://247wallst.com/investing/2026/11/19/broadcoms-13-67b-quarterly-fcf-beats-marvells-scaling-story-plain-and-simple/
- Thu 19 Nov | Crypto Briefing | Broadcom passes Saudi Aramco to become the world’s eighth most valuable company
  https://cryptobriefing.com/broadcom-passes-saudi-aramco-market-value/
- Thu 19 Nov | Traders Union | Broadcom stock recovery holds but faces a stretched setup: weekly analysis
  https://tradersunion.com/news/stocks/show/4322672-broadcom-gains-5-06percent-over-the/
## BRK.B  (8 leads)
- Thu 19 Nov | TheStreet | Berkshire almost doubles stake in tumbling housing stock
  https://www.thestreet.com/investing/stocks/len-lennar-warren-buffet-berkshire-hathaway-almost-doubles-stake
  (page: did not load (403))
- Thu 19 Nov | ad-hoc-news.de | Buffett Shifts $9.23 Billion in Stock to Family Charities as Berkshire's Earnings Momentum Cools
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/buffett-shifts-9-23-billion-in-stock-to-family-charities-as-berkshire-s-earnings-momentum-cools/70536995
  > Warren Buffett will convert 6,150 Berkshire Hathaway Class A shares into roughly 9.23 million Class B shares and hand the entire proceeds to four family foundations, the conglomerate disclosed on Monday. The Susan Thompson Buffett Foundation is set to receive 3.69 million Class B shares, while The Sherwood Foundation, The Howard G.
- Thu 19 Nov | ad-hoc-news.de | Buffett's $9.23 Million Share Gift Lands Alongside a 5.8% Profit Retreat
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/buffett-s-9-23-million-share-gift-lands-alongside-a-5-8-profit-retreat/70536874
  > Warren Buffett set the wheels in motion on Monday to convert 6,150 Berkshire Hathaway A-shares into roughly 9.23 million B-shares, with the proceeds earmarked for four family foundations. The Susan Thompson Buffett Foundation is in line for 3.69 million B-shares, while The Sherwood Foundation, The Howard G.
- Thu 19 Nov | Traders Union | Berkshire Hathaway stock weekly forecast: Holds gains as buyers stay in control
  https://tradersunion.com/news/stocks/show/4321543-berkshire-falls-3-16percent-over-the/
  (page: did not load (403))
- Thu 19 Nov | Yahoo Finance | Apple Became a Top Buffett Holding for a Reason. I'd Buy It With $1,000 Now.
  https://finance.yahoo.com/markets/stocks/articles/apple-became-top-buffett-holding-132200995.html
- Thu 19 Nov | Barchart.com | Forget Apple. Warren Buffett’s Berkshire Is Pouring Nearly $1 Billion Into This Little-Known Tech Stock.
  https://www.barchart.com/story/news/8913811/forget-apple-warren-buffetts-berkshire-is-pouring-nearly-1-billion-into-this-little-known-tech-stock
- Thu 19 Nov | The Motley Fool | Prediction: A Stock Market Crash Is Coming. Here's What Investors Should Do Based on Warren Buffett's Proven Advice.
  https://www.fool.com/investing/2026/11/19/prediction-stock-market-crash-coming-investors-warren-buffetts-proven-advice/
- Thu 19 Nov | ad-hoc-news.de | Berkshire Hathaway stock reshuffles portfolio in Q3 13F
  https://www.ad-hoc-news.de/boerse/news/corporate-news/berkshire-hathaway-stock-reshuffles-portfolio-in-q3-13f/70535595
## WMT  (8 leads)
- Thu 19 Nov | Yahoo Finance | Sky-high diesel prices take a $2 billion bite out of Walmart
  https://finance.yahoo.com/markets/stocks/article/sky-high-diesel-prices-take-a-2-billion-bite-out-of-walmart-163930973.html
  > Diesel price inflation significantly drove up Walmart's (WMT) fuel bill. "Diesel prices overall for us have been about $2 billion of incremental costs for us this year," Walmart (WMT) CFO John David Rainey said on Sozzi Unleashed.
- Thu 19 Nov | Startup Fortune | Walmart shares slip after a third-quarter beat and a higher full-year outlook
  https://startupfortune.com/walmart-shares-slip-after-a-third-quarter-beat-and-a-higher-full-year-outlook/
  > Walmart did what investors asked of it and still lost ground on the day. When a retailer this size gets sold on a clean beat, the market is telling you the bar was set higher than the numbers.
- Thu 19 Nov | Yahoo Finance | What Walmart (WMT) Said on Its Q3 Earnings Call
  https://finance.yahoo.com/markets/stocks/articles/walmart-wmt-said-q3-earnings-161628504.html
  > - Interested in Walmart Inc.? Here are five stocks we like better. - Walmart raised its full-year outlook after stronger-than-expected third-quarter results, now forecasting 4.9%–5.2% sales growth and EPS of $2.84–$2.89. - Digital businesses boosted growth and profitability: global e-commerce sales rose 17%, Walmart U.S.
## V  (8 leads)
- Thu 19 Nov | Türkiye Today | Türkiye asks EU to ease Schengen visa processes at first Ankara talks with Commission
  https://www.turkiyetoday.com/region/turkiye-asks-eu-to-ease-schengen-visa-processes-at-first-ankara-talks-with-commission-3232788
  > Türkiye has asked European Union member states and the European Commission to make Schengen visa procedures easier for its citizens, saying it will keep pursuing practical improvements until visa-free travel becomes a reality, according to diplomatic sources. Foreign Ministry officials made the request on Nov.
- Thu 19 Nov | MarketBeat | Private Advisor Group LLC Purchases 72,752 Shares of Visa Inc. $V
  https://www.marketbeat.com/instant-alerts/filing-private-advisor-group-llc-purchases-72752-shares-of-visa-inc-v-2026-11-19/
  > Private Advisor Group LLC Purchases 72,752 Shares of Visa Inc. - Private Advisor Group increased its Visa stake by 47.3% in the third quarter, buying 72,752 shares to hold 226,497 shares worth about $81.4 million.
- Thu 19 Nov | TradingView | Can Visa Turn AI-Led Commerce Into a New Growth Driver?
  https://www.tradingview.com/news/zacks:9ed88f2fc094b:0-can-visa-turn-ai-led-commerce-into-a-new-growth-driver/
  > Can Visa Turn AI-Led Commerce Into a New Growth Driver? V is expanding its Agentic Ready program to merchants, payment service providers, acquirers and commerce platforms, with more than 140 participants joining at launch. Visa's framework allows participants to test agent authentication, tokenized credentials and fraud controls using existing payment infrastructure.
## ORCL  (8 leads)
- Thu 19 Nov | Substack | AI Patient Zero: Oracle’s Investment Grade Rating Masks Default Risk
  https://roddubitsky.substack.com/p/ai-patient-zero-oracles-investment
  > “History may reveal Oracle as patient zero, should the AI bubble burst.” ---- Rod Dubitsky, December 2025 The above quote is from my December 2025 Oracle article where I argued that Oracle was at risk of becoming the largest fallen angel (investment grade to junk) in history. [Figures on the page: consolidated; first half; one quarter. Check which one each figure is.]
- Thu 19 Nov | ad-hoc-news.de | Oracle stock: Bernstein sees value in worst-case AI scenario
  https://www.ad-hoc-news.de/boerse/news/corporate-news/oracle-stock-bernstein-sees-value-in-worst-case-ai-scenario/70537227
  > In an analysis published Wednesday, November 18, 2026, MarketWatch, citing Dow Jones, reported that Bernstein analyst Mark Moerdler maintained an Outperform rating and a USD 325 price target for Oracle. His analysis adds a severe downside scenario to the debate over the company's artificial-intelligence infrastructure spending.
- Thu 19 Nov | The Globe and Mail | The Zacks Analyst Blog Highlights Oracle, Microsoft, Amazon and Alphabet
  https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/8919443/the-zacks-analyst-blog-highlights-oracle-microsoft-amazon-and-alphabet/
  > The Zacks Analyst Blog Highlights Oracle, Microsoft, Amazon and Alphabet Chicago, IL – November 19, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Stocks recently featured in the blog include: Oracle ORCL, Microsoft MSFT, Amazon AMZN and Alphabet GOOGL. Oracle Stock Plunges -41% YTD Despite Cloud Strength: Hold or Fold?
## COST  (8 leads)
- Thu 19 Nov | Benzinga | Here's How Much $1000 Invested In Costco Wholesale 15 Years Ago Would Be Worth Today
  https://www.benzinga.com/news/26/11/63439208/here-s-how-much-1000-invested-costco-wholesale-15-years-ago-would-be-worth-today
  (page: did not load (403))
- Thu 19 Nov | 24/7 Wall St. | High End Generators Are Flying Off The Shelves At Costco After A String Of Unusual Tech Outages. Generac Shares Are Up More Than 50% In 2026
  https://247wallst.com/investing/2026/11/19/high-end-generators-are-flying-off-the-shelves-at-costco-after-a-string-of-unusual-tech-outages-generac-shares-are-up-more-than-50-in-2026/
  > High End Generators Are Flying Off The Shelves At Costco After A String Of Unusual Tech Outages. Generac Shares Are Up More Than 50% In 2026 Mizuho analyst David Bellinger[1] ran an online availability check of Costco Wholesale (NASDAQ:COST | COST Price Prediction) on Sunday night, Nov.
- Thu 19 Nov | ad-hoc-news.de | Costco Wholesale stock: Mizuho raises target to USD 1,150
  https://www.ad-hoc-news.de/boerse/news/corporate-news/costco-wholesale-stock-mizuho-raises-target-to-usd-1-150/70536811
  > Mizuho raised its price target for Costco Wholesale from USD 1,100 to USD 1,150 on November 17 and retained an Outperform rating, according to Yahoo Finance. Analyst David Bellinger also removed Costco from Mizuho's Top Pick list after the stock's strong run. The target change adds a fresh analyst signal to Costco's current investor narrative.
## NFLX  (8 leads)
- Thu 19 Nov | ad-hoc-news.de | Netflix stock: Games unit cuts add to strategic reset
  https://www.ad-hoc-news.de/boerse/news/corporate-news/netflix-stock-games-unit-cuts-add-to-strategic-reset/70536905
  > Netflix Games cut an undisclosed number of jobs during a restructuring reported on Tuesday, November 17. The development adds another strategic test for the streaming company's gaming ambitions, while Netflix says its wider approach to games remains unchanged.
- Thu 19 Nov | Yahoo Finance | With Netflix Stock Down Nearly 46% In The Last Year, Michael Burry Reveals The Price He’d Think About Buying
  https://finance.yahoo.com/markets/stocks/articles/netflix-stock-down-nearly-46-142545256.html
  > - Michael Burry says he is "more in the high 30s now on NFLX," far below its $60 price after a 46% yearly slide. - Michael Burry would buy Alibaba "in the 60s," well below its $87 close, and he is not buying NVIDIA calls to offset his puts.
- Thu 19 Nov | Yahoo Finance | Netflix Number One Show Returns With $300 Million Costs
  https://finance.yahoo.com/media-advertising/articles/netflix-number-one-show-returns-120035351.html
  > Netflix knows when it has got a hot property on its hands. Many of its most successful shows are renewed within a matter of weeks of their debut.
## INTC  (8 leads)
- Thu 19 Nov | 24/7 Wall St. | Intel’s CEO Says It “Just Signed the First Customer” for 18A
  https://247wallst.com/investing/2026/11/19/intels-ceo-says-it-just-signed-the-first-customer-for-18a/
  > Intel’s CEO Says It “Just Signed the First Customer” for 18A This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Thu 19 Nov | The Motley Fool | Why Intel Stock Is Gaining Today
  https://www.fool.com/investing/2026/11/19/why-intel-stock-is-gaining-today/
  > By Johnny Rice – - Intel CEO Lip-Bu Tan said the company has signed its first outside customer for 18A, its most advanced chipmaking process.
- Thu 19 Nov | Simply Wall St | Intel (INTC) Stock Looks Undervalued With Cash Flow Recovery In View
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-intc-stock-looks-undervalued-with-cash-flow-recovery-i
  > Intel has had a punishing few weeks in the market after a strong run over the past year, which puts a sharper spotlight on whether the current share price lines up with the cash the business is expected to generate.
## LLY  (8 leads)
- Thu 19 Nov | The News International | Canada approves new Eli Lilly GLP-1 pill for weight loss and Type 2 diabetes
  https://www.thenews.com.pk/latest/1424290-canada-approves-new-eli-lilly-glp-1-pill-for-weight-loss-and-type-2-diabetes
  (page: did not load (403))
- Thu 19 Nov | blockchain.news | Eli Lilly (LLY) Stock Price Prediction: Lilly pulls back toward support as analysts stay constructive
  https://blockchain.news/news/20261119-price-prediction-lly-lilly-pulls-back-toward-support-as
  > What the tape is saying Eli Lilly (LLY) is easing off recent highs rather than breaking down outright. The stock is at $1,369.97, down 2.52% over 24 hours, and it has slipped under the 7-day SMA of $1,414.69, the 20-day SMA of $1,407.70 and the 12-day EMA of $1,403.69.
- Thu 19 Nov | The Globe and Mail | Is Immunology Emerging as Eli Lilly's Next Growth Driver?
  https://www.theglobeandmail.com/investing/markets/stocks/NVS/pressreleases/8919218/is-immunology-emerging-as-eli-lillys-next-growth-driver/
  > Is Immunology Emerging as Eli Lilly's Next Growth Driver? Eli Lilly and Company LLY continues to derive a significant portion of its revenues from its blockbuster GLP-1 drugs, Mounjaro and Zepbound. Lilly is investing in immunology through commercial expansion, clinical development and strategic acquisitions to establish additional long-term growth drivers.
- Thu 19 Nov | Yahoo Finance | Eli Lilly Stopped Touting Dose Counts. Should You Worry?
  https://finance.yahoo.com/healthcare/articles/eli-lilly-stopped-touting-dose-150930626.html
  > Today's big story: Could Anthropic Stock Fall 25%? Eli Lilly (LLY) stock trades at 44.7 times earnings, against 21.5 for the S&P 500. On calls in February and August 2025, management emphasized how many doses of its weight-loss and diabetes drugs it could make. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Thu 19 Nov | Cleanroom Technology | Eli Lilly to create 2,000 construction jobs in Pennsylvania with $3.5bn new facility
  https://www.cleanroomtechnology.com/eli-lilly-to-create-2-000-construction-jobs-in
- Thu 19 Nov | Yahoo Finance | Eli Lilly (LLY) Expands Its Oncology Research Platform
  https://finance.yahoo.com/healthcare/articles/eli-lilly-lly-expands-oncology-122029469.html
- Thu 19 Nov | Seeking Alpha | Eli Lilly: Everyone Losing Weight, But Lilly Keeps Gaining (Initiating With A Buy) (LLY)
  https://seekingalpha.com/article/4969989-eli-lilly-everyone-losing-weight-but-lilly-keeps-gaining-initiating-with-a-buy
- Thu 19 Nov | MedWatch | Eli Lilly signs cancer research deal with US biotech Stipple Bio
  https://news.google.com/rss/articles/CBMib0FVX3lxTE02OXN6eWxXNEpYbGdlRnVibEVMMnJpT0xOYzhtZGM1aW1NRlF1bk1IMjZiRHNuR2lmZ1huRGM2clZqbHBFVEpjSkNwelZYTjVScmU5czBfR193VzBMcHBZVlpKVFU0ZHB0dnhPcTVRRQ?oc=5
Read 84 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, JUFO, EAST, EMFD, EGAL, AMOC.
