# Desk brief, Tuesday, November 17, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 19s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-16 (22.91); Treasury yields to 2026-11-16 (10-year 5.12%).
- **valuation**: ok in 24s (GitHub Actions). LLY: $1.36tn, P/E (last 12 months) 44.8, Forecast P/E (fiscal 2026) 40.2 (the four quarters to Sep 2026)
- **movers**: ok in 20s (GitHub Actions). Market values: 18 of 39 updated
- **calendar**: ok in 1s (GitHub Actions). 2027-01-28 V results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 mixed, RSI 54.5
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 51 stocks, k 16.4%, median P/E 10.1; cheapest MASR +69%, PHAR +52%, ABUK +49%; dearest ARAB -62%, MOIN -65%, BTFH -70%
- **views**: ok in 0s (GitHub Actions). 2026-11-05-brent-hormuz: open -> on track
- **results**: ok in 75s (GitHub Actions). 
- **news**: ok in 427s (GitHub Actions). 
- **leads**: ok in 114s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 29 failed, 126 needed a retry (stock_news.py, fetch_movers.py).

## What moved (latest close against the one before)
- EGX30 52,199.80 (+0.02%); EGX70 EWI 18,028.40 (-3.76%); USD/EGP 53.68 (-0.33%); Gold 21K 5,910.00 (-0.76%); Brent 92.44 (-3.55%); S&P 500 7,416.59 (-1.92%); Nasdaq 24,509.76 (-2.49%); Bitcoin 64,604.00 (+0.39%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): EFID +7.4%, INTC -7.0%, ETEL +5.2%, ORCL -5.0%, NVDA -4.1%, MFPC -4.1%, GOOGL -4.1%, AVGO -3.9%, PHDC -3.4%, AMZN -3.3%, CLHO -3.3%, HRHO -3.2%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 81, stretched after a run: above 70.
    - COST: Turning up: above both its 50-day average (14.7% over) and its 200-day (14.0% over), though the 50-day is still below the 200-day; RSI 77, stretched after a run: above 70.
    - INTC: Turning down: below both its 50-day average (41.1% under) and its 200-day (36.5% under), though the 50-day is still above the 200-day; RSI 30, washed out: below 30.
    - NVDA: Turning down: below both its 50-day average (26.8% under) and its 200-day (23.5% under), though the 50-day is still above the 200-day; RSI 23, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- US TU (TELUS) +12.2%; US MOH (Molina Healthcare) +11.3%; US TSN (Tyson Foods) +8.7%; US HUBS (HubSpot) +6.8%; US MOG.B (Moog) +6.7%; US ASTS (AST SpaceMobile) -12.3%; US NTRA (Natera) -9.6%; US TEM (Tempus AI) -9.6%; US TSEM (Tower Semiconductor) -9.2%; US ALAB (Astera Labs) -8.8%

Leads for them (open before using; never guess a reason):
```
EGX: failed (HTTP Error 401: Unauthorized); kept the saved session
EGX week and month: EGX stocks trading at least EGP 1m a day on average (215)
US: 2026-11-16, 841 companies
US week and month: US companies worth $10bn or more (840)
EGX30 heatmap: 2026-11-16, 31 members
US heatmap: 2026-11-16, 100 members
Market values: 18 of 39 updated

# EGX 2026-11-12
## INFI +17.5%  Foodico
- no headlines found
## ATLC +8.7%  AT Lease
- no headlines found
## DTPP +8.0%  Delta for Printing & Packaging
- no headlines found
## ROTO +5.9%  Al Rowad
- Mon 16 Nov | شبكة تواصل الإخبارية | الدارة تنظم الورشة التعريفية الثانية لبرنامج (الأعمال الكاملة للمؤرخين الرواد)
  https://twaslnews1.twaslnews.com/7811776/
- Mon 16 Nov | صحيفة النهار السعودية | دارة الملك عبدالعزيز تنظم الورشة التعريفية الثانية لبرنامج (الأعمال الكاملة للمؤرخين الرواد) عبر الاتصال المرئي
  https://annahar-news.com/news/single/39908
- Mon 16 Nov | المتداول العربي | الولايات المتحدة تختار إنفيديا وأنثروبيك ضمن «الرواد الوطنيين» للذكاء الاصطناعي
  https://news.google.com/rss/articles/CBMingVBVV95cUxPRUE0VVBEX2dlZEhZWWtxZUhRY2FEYkl5dUh4NFd2YzV0NUpVZjFzZGUyWDFFdlozVThfck90Z2xmUVF0ZkVCT25acDZERFA5VG1IcndzOTEyQl9QQnZudVZUN19GSkZLS1RJbXNJUzNmU3VOSjFtVTZyVG1LT1dFbkxHRGIwUmdmMlB
- Sun 15 Nov | شاهد الآن | اتحاد الرواد العرب يوسّع دوره المجتمعي بلجنتين للعمل الخيري وذوي الاحتياجات الخاصة
  https://shahdnow.sa/369889/
## HDBK +5.8%  Housing & Development Bank
- Mon 16 Nov | الرئيس نيوز | بعد رفع الفائدة 1%.. أحدث أسعار عائد شهادات الادخار في البنك الأهلي وبنك مصر والتعمير والإسكان
  https://www.alraeesnews.com/346915
- Mon 16 Nov | الأسبوع | أعلى عائد على شهادات الادخار 2026.. 19% من بنك التعمير والإسكان و18.85% بالأهلي
  https://www.elaosboa.com/3023462/
- Mon 16 Nov | شبكة تواصل الإخبارية | بنك التعمير والإسكان يوظف 40% من ودائعه في منح القروض بنهاية سبتمبر 2026
  https://twaslnews1.twaslnews.com/7778858/
- Mon 16 Nov | بنكي | بنك التعمير والإسكان يتيح تقسيط اشتراك Castello Gym حتى 12 شهرًا دون فوائد أو مصاريف إدارية
  https://www.bankygate.com/202604
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
- Sun 15 Nov | جريدة المال | أرباح جلاكسو سميثكلاين تقفز 314% خلال 9 أشهر
  https://almalnews.com/2147361/أرباح-جلاكسو-سميثكلاين-تقفز-314-خلال-9/
- Sun 15 Nov | Dawaa News MENA | أسهم الأدوية المصرية تصعد بقيادة جلاكسو والنيل وممفيس | 12 نوفمبر 2026
  https://dawaanews.com/egypt-pharma-healthcare-stocks-weekly-12-november-2026/
## COPR -3.3%  Copper For Commercial Investment
- no headlines found

# US 2026-11-16
## TU +12.2%  TELUS
- Tue 17 Nov | iNews Zoombangla | Quebecor proposes cash and stock offer for TELUS at a 60% premium
  https://inews.zoombangla.com/quebecor-cash-stock-offer-telus-60-percent-premium/
  > Quebecor has made a non-binding proposal to the TELUS board of directors to acquire all of TELUS’s shares in a cash and stock transaction.
- Tue 17 Nov | Yahoo Finance | TELUS (TSX:T) Looks Fairly Valued Following Québecor Bid Interest
  https://finance.yahoo.com/markets/stocks/articles/telus-tsx-t-looks-fairly-051242217.html
  > TELUS (TSX:T) moved into the spotlight after confirming an unsolicited, non-binding takeover proposal from Québecor that coincided with a double-digit one day share price jump and raised fresh questions about valuation and control.
- Tue 17 Nov | Yahoo Finance | TELUS (TSX:T) Drops Vancouver AI Data Centre Plans And Bets On Kamloops
  https://finance.yahoo.com/technology/ai/articles/telus-tsx-t-drops-vancouver-031021614.html
  > - TELUS (TSX:T) has withdrawn from two planned AI data centre projects in Vancouver, according to a recent update. - The telecom is refocusing infrastructure plans on expanding its existing facilities in Kamloops to support future AI workloads.
- Tue 17 Nov | Yahoo Finance | TELUS (TSX:T) Stock Trades Below Fair Value On Cash Flow Views
  https://finance.yahoo.com/markets/stocks/articles/telus-tsx-t-stock-trades-020729514.html
  > TELUS has rallied in recent weeks and is now in the spotlight after a C$31b takeover proposal, which puts fresh focus on whether the current share price lines up with what its cash flows can support.
## MOH +11.3%  Molina Healthcare
- Tue 17 Nov | Kalkine Media | Molina Healthcare Director Steven Orlando Announces Intent to Sell 702 Shares
  https://kalkinemedia.com/us/news/announcements/molina-healthcare-director-steven-orlando-announces-intent-to-sell-702-shares
  > On November 16, 2026, Molina Healthcare Inc. Director Steven Orlando submitted a Form 144 filing with the SEC, revealing plans to sell 702 shares of the company's common stock via Merrill Lynch Wealth Management. - Seller and Position: Steven Orlando, Director at Molina Healthcare Inc.
- Tue 17 Nov | GuruFocus | A Look at Molina Healthcare Inc (MOH) After 11.3% Gain -- GF Val
  https://www.gurufocus.com/news/9203126/a-look-at-molina-healthcare-inc-moh-after-113-gain-gf-value-35640-vs-price-23309
  (page: did not load (403))
- Mon 16 Nov | AlphaStreet | Molina Healthcare Jumps 7.5% Amid Sector-Wide Rally
  https://news.alphastreet.com/molina-healthcare-jumps-7-5-amid-sector-wide-rally/amp/
  > AlphaStreet Newsdesk powered by AlphaStreet Intelligence Molina Healthcare soared Monday. Shares of the healthcare plans provider jumped 7.5% to $225.25 on November 16, 2026, riding a broad rally across managed care stocks that sent sector peers sharply higher in heavy trading.
- Mon 16 Nov | Moomoo | Mizuho Securities Maintains Molina Healthcare(MOH.US) With Buy Rating, Maintains Target Price $255
  https://www.moomoo.com/news/post/1004770306/mizuho-securities-maintains-molina-healthcare-mohus-with-buy-rating-maintains
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## TSN +8.7%  Tyson Foods
- Tue 17 Nov | Kalkine Media | Tyson Foods Submits Annual 10-K Report for Fiscal Year Ending October 3, 2026
  https://kalkinemedia.com/us/news/announcements/tyson-foods-submits-annual-10-k-report-for-fiscal-year-ending-october-3-2026
  > has submitted its Annual Report on Form 10-K to the U.S. Securities and Exchange Commission for the fiscal year ending October 3, 2026, detailing share statistics, segment organization, and business operations within its five reportable segments. - Fiscal Year End: The reporting period concluded on October 3, 2026.
- Tue 17 Nov | EBC Financial Group | ​Tyson Foods Stock Jumps 8.7% Despite Just $1 Million in Q4 Operating Profit
  https://www.ebc.com/forex/tyson-foods-stock-q4-2026-earnings-beef-losses-copy
  > Tyson Foods (NYSE: TSN) shares surged 8.72% to $63.95 on November 16, despite fiscal fourth-quarter GAAP operating income falling to just $1 million from $158 million a year earlier.
- Tue 17 Nov | HDFC Sky | US Stocks Today: Tyson Foods Jumps 7.46%, Small Caps Fall
  https://hdfcsky.com/news/tyson-jumps-7-46percent-on-earnings-beat-virtuix-plunges-17percent-microbot-sinks-34percent-as-stocks-react-to-q3-results
  > Tyson Jumps 7.46% on Earnings Beat, Virtuix Plunges 17%, Microbot Sinks 34% as Stocks React to Q3 Results Open Free Demat Account Mumbai, 17 November 2026: U.S. Tyson Foods rallied on an earnings beat, while several small-cap stocks plunged despite operational progress. [Figures on the page: nine months; first half; one quarter. Check which one each figure is.]
- Tue 17 Nov | Investing.com | Tyson Foods earnings beat by $0.01, revenue topped estimates
  https://www.investing.com/news/earnings/tyson-foods-earnings-missed-by-014-revenue-fell-short-of-estimates-5030363
  (page: did not load (403))
## HUBS +6.8%  HubSpot
- Tue 17 Nov | MarketBeat | HubSpot (NYSE:HUBS) Shares Cross Above 200-Day Moving Average - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-hubspot-nyse-hubs-shares-cross-above-200-day-moving-average-should-you-sell-2026-11-17/
  > HubSpot (NYSE:HUBS) Shares Cross Above 200-Day Moving Average - Should You Sell? - HubSpot shares rose above their 200-day moving average of $226.70, reaching an intraday high of $233.88 and last trading at $231.53.
- Tue 17 Nov | Simply Wall St | HubSpot Stock What Changed As Co Founder Returns And New CFO Takes Over
  https://simplywall.st/stocks/us/software/nyse-hubs/hubspot/news/hubspot-stock-what-changed-as-co-founder-returns-and-new-cfo
  > HubSpot announced a major leadership reset, with co founder Brian Halligan returning as CEO and Adobe finance veteran Karen Burgess set to succeed retiring CFO Kate Bueker after a defined transition period. The company is pairing this executive reshuffle with active capital return and detailed revenue and earnings guidance.
- Mon 16 Nov | MLQ.ai | HubSpot co-founder Brian Halligan buys $5 million of stock days after returning as CEO
  https://mlq.ai/news/hubspot-co-founder-brian-halligan-buys-5-million-of-stock-days-after-returning-as-ceo/
  (page: did not load (403))
- Mon 16 Nov | FourWeekMBA | HubSpot CEO Buys $5M of Stock, Will Pay HubSpot $450K
  https://fourweekmba.com/ai-hubspot-ceo-buys-5m-of-stock-will-pay-hubspot-450k/
  (page: did not load (403))
## MOG.B +6.7%  Moog
- Mon 16 Nov | Seeking Alpha | Moog: Still A Buy, But The Easy Money Has Been Made
  https://seekingalpha.com/article/4968583-moog-still-buy-but-easy-money-made
  (page: did not load (403))
- Sun 15 Nov | Simply Wall St | Moog (MOG.A) Sets Earnings Date, Is The Valuation Discount An Opportunity?
  https://simplywall.st/stocks/us/capital-goods/nyse-mog.a/moog/news/moog-moga-sets-earnings-date-is-the-valuation-discount-an-op
  > Moog (MOG.A) is in focus after scheduling its fiscal 2026 fourth quarter and full year earnings release for November 20, 2026, along with a management conference call for investors.
- Sat 14 Nov | Simply Wall St | How ETF Selling Will Impact Moog (MOG.A) Investors
  https://simplywall.st/stocks/us/capital-goods/nyse-mog.a/moog/news/how-etf-selling-will-impact-moog-moga-investors
  > Moog drew attention after heavy ETF trading activity, including sales by the iShares Russell 2000 fund, which adjusted its Moog Class A exposure without fully exiting the position.
## ASTS -12.3%  AST SpaceMobile
- Tue 17 Nov | Kalkine Media | What Is the Rakuten AST Venture With AST SpaceMobile (NASDAQ:ASTS)?
  https://kalkinemedia.com/us/stocks/communication/what-is-the-rakuten-ast-venture-with-ast-spacemobile-nasdaqasts
  > - AST SpaceMobile and Rakuten form Rakuten AST - Venture targets a direct-to-device network in Japan AST SpaceMobile, Inc., (NASDAQ:ASTS) Technology Ast Spacemobile Inc (NASDAQ:ASTS) 32.60 USD -1.900 5.507% Last Updated at: 2026-11-13T21:28:00Z Rakuten Group, Inc.
- Tue 17 Nov | Yahoo Finance | What Is AST SpaceMobile (ASTS) Building With Its $1 Billion Japan Venture?
  https://finance.yahoo.com/markets/stocks/articles/ast-spacemobile-asts-building-1-031119939.html
  > - AST SpaceMobile (NasdaqGS:ASTS) is joining Rakuten in a new Japan-focused satellite joint venture, Rakuten AST, backed by roughly $1b in government funding. - The partnership aims to supply a sovereign direct to device satellite network in Japan to support both commercial connectivity and emergency communications.
- Tue 17 Nov | Yahoo Finance Singapore | AST SpaceMobile, Inc. (ASTS) latest stock news and headlines – Yahoo Finance
  https://sg.finance.yahoo.com/quote/ASTS/news/
  (page: only 29 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | Yahoo Finance | AST SpaceMobile (ASTS) Takes a Beating. Here’s What Happened
  https://finance.yahoo.com/markets/stocks/articles/ast-spacemobile-asts-takes-beating-020349552.html
  > (NASDAQ:ASTS) is one of the 10 Stocks Investors Are Dumping Right Now. AST SpaceMobile slashed its share price by 12.33 percent on Monday—a third straight day—amid lingering investor concerns over its launch delays, while mirroring the broader market's decline. [Figures on the page: one quarter; attributable to shareholders. Check which one each figure is.]
## NTRA -9.6%  Natera
- Mon 16 Nov | GuruFocus | Natera Inc (NTRA) Shares Fall 9.6% -- What GF Score of 77 Tells Investors
  https://www.gurufocus.com/news/9202928/natera-inc-ntra-shares-fall-96-what-gf-score-of-77-tells-investors
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-17 CLHO results (expected)
- 2026-11-17 EFID results (expected)
- 2026-11-17 JUFO results (expected)
- 2026-11-17 NVDA results (expected)
- 2026-11-17 PHDC results (expected)
- 2026-11-18 EAST results (expected)  <- write its preview
- 2026-11-18 EFIH results (expected)  <- write its preview
- 2026-11-18 HRHO results (expected)
- 2026-11-19 MSFT dividend
- 2026-11-24 COST dividend

## Views
- due 2026-11-20: Brent stays below $105 while Iran talks continue (on track)
    2026-11-11-value-basket: on track -> open
    2026-10-30-developers: open -> on track
    2026-11-04-fert-gas: open -> on track
    2026-11-05-brent-hormuz: open -> on track

## Fair value
- Changed since the last run: ORHD +38% -> +37% (high -> medium).
- In the ten cheapest or dearest with no note: MCQE, ADIB, EMFD, SCEM, MTIE, AMOC, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-17. Open each story before using it.
## COMI  (8 leads)
- Mon 16 Nov | بوابة المصرف | “التجاري الدولي” يرتفع وحيدًا بين أسهم البنوك بالبورصة.. وخسائر جماعية للقطاع بختام التعاملات
  https://www.almasraf.news/التجاري-الدولي-يرتفع-وحيدًا-بين-أسهم-2/
  > شهدت أسهم البنوك المدرجة بالبورصة المصرية أداءً متباينًا بختام تعاملات اليوم الإثنين، بعدما ارتفع سهم البنك التجاري الدولي مصر CIB وحيدًا، فيما تراجعت أسهم 11 بنكًا، بينما استقر سهم بنك فيصل الإسلامي المصري المتداول بالدولار.
- Mon 16 Nov | أموال الغد | المصرية للاتصالات والتجاري الدولي وقرة تتصدر الأسهم النشطة بالبورصة بتداولات مليارية
  https://amwalalghad.com/2026/11/16/المصرية-للاتصالات-والتجاري-الدولي-وق/
  > تصدر سهم القاهرة للدواجن قائمة الأسهم المقيدة بالسوق الرئيسي بالبورصة المصرية من حيث قيمة التداول خلال تعاملات الاثنين 16 نوفمبر 2026، بقيمة بلغت 1.789 مليار جنيه، فيما جاء البنك التجاري الدولي – مصر في المركز الثاني بقيمة 1.122 مليار جنيه، تلاه سهم المصرية للاتصالات بقيمة 750.5 مليون جنيه، وفقًا للتقرير اليومي للبورصة المصرية الصادر عن ...
- Mon 16 Nov | جريدة الكنانة نيوز | البورصة المصرية ترتفع في بداية التعاملات بدعم التجاري الدولي وبلتون
  https://elkanananews.com/البورصة-المصرية-ترتفع-في-بداية-التعام/
  > البورصة المصرية ترتفع في بداية التعاملات بدعم التجاري الدولي وبلتون
## TMGH  (8 leads)
- Tue 17 Nov | المصري اليوم | 24 ٪ نموًا فى إيرادات «طلعت مصطفى».. والمبيعات تسجل 290 مليار جنيه
  https://www.almasryalyoum.com/news/details/4412513
  > 24 ٪ نموًا فى إيرادات «طلعت مصطفى».. والمبيعات تسجل 290 مليار جنيه حققت مجموعة طلعت مصطفى القابضة قفزة مالية وتشغيلية بارزة خلال الأشهر التسعة الأولى من عام 2026، مدعومة بكفاءة التنفيذ وتنوع الأنشطة الاستراتيجية، ما يعكس قدرة المجموعة على مواصلة النمو المستدام فى السوق المصرى والأسواق الإقليمية الواعدة. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | ايكونومي بلس | تسليمات مجموعة طلعت مصطفى تقفز 70% في أول 9 أشهر من 2026
  https://economyplusme.com/ar/news/34225
  (page: only 28 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | بوابة الوفد الإلكترونية | أحمد موسى: "طلعت مصطفى خد 10 ملايين متر بالسعودية ومقالوش باعوها"
  https://www.alwafd.news/6003245
  (page: did not load (403))
## ETEL  (8 leads)
- Tue 17 Nov | موقع الحرية الإخباري | خسائر حريق رمسيس بـ 1.48 مليار جنيه وأصول غير مدرجة.. تفاصيل تقرير المركزي للمحاسبات عن «المصرية للاتصالات
  https://alhorianews.com/خسائر-حريق-رمسيس-بـ-1-48-مليار-جنيه-وأصول-غ/
  > كشف تقرير الفحص المحدود الصادر عن الجهاز المركزي للمحاسبات بشأن القوائم المالية الدورية المستقلة والمجمعة للشركة المصرية للاتصالات عن الفترة المنتهية في 30 سبتمبر 2026، والمرسل إلى البورصة المصرية اليوم، عن حزمة من التحفظات والملاحظات الجوهرية، تصدرتها الخسائر الرأسمالية الناتجة عن حريق سنترال رمسيس، إلى جانب أصول ثابتة بمليارات الجنيهات غير مدرجة أو مهلكة دفتريًا. [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Mon 16 Nov | GuruFocus | Telecom Egypt SAE (CAI:ETEL) (Q3 2026) Earnings Call Highlights:
  https://www.gurufocus.com/news/9202179/telecom-egypt-sae-caietel-q3-2026-earnings-call-highlights-revenue-jumps-23-as-data-demand-and-margin-expansion-fuel-strong-cash-generation
  (page: did not load (403))
- Mon 16 Nov | أموال الغد | المصرية للاتصالات والتجاري الدولي وقرة تتصدر الأسهم النشطة بالبورصة بتداولات مليارية
  https://amwalalghad.com/2026/11/16/المصرية-للاتصالات-والتجاري-الدولي-وق/
  > تصدر سهم القاهرة للدواجن قائمة الأسهم المقيدة بالسوق الرئيسي بالبورصة المصرية من حيث قيمة التداول خلال تعاملات الاثنين 16 نوفمبر 2026، بقيمة بلغت 1.789 مليار جنيه، فيما جاء البنك التجاري الدولي – مصر في المركز الثاني بقيمة 1.122 مليار جنيه، تلاه سهم المصرية للاتصالات بقيمة 750.5 مليون جنيه، وفقًا للتقرير اليومي للبورصة المصرية الصادر عن ...
- Mon 16 Nov | جريدة المال | «المصرية للاتصالات» تخفض أرصدة القروض والتسهيلات الائتمانية إلى 56.7 مليار جنيه بنهاية سبتمبر 2026
  https://almalnews.com/2147728/«المصرية-للاتصالات»-تخفض-أرصدة-القروض-والتسهيلات-الائتمانية/
  > كشفت القوائم المالية المستقلة للشركة المصرية للاتصالات عن تراجع إجمالي أرصدة القروض والتسهيلات الائتمانية إلى نحو 56.7 مليار جنيه بنهاية سبتمبر 2026، مقابل 73.77 مليار بنهاية ديسمبر 2025، بانخفاض قدره نحو 17.06 مليار ، وبمعدل تراجع يقترب من 23.1%.
- Mon 16 Nov | https://ekhbary24.com/ | المقاولون العرب يهزم المصرية للاتصالات ويتأهل لدور الـ16 بكأس مصر
  https://ekhbary24.com/article/57272
- Mon 16 Nov | WebWire | Q3 2026 Results: Telecom Egypt Delivers Strong 9M 2026 Results as Strategy Execution Progresses
  https://www.webwire.com/ViewPressRel.asp?aId=364222
- Mon 16 Nov | https://ekhbary24.com/ | شادي حسين يقود هجوم المقاولون العرب أمام المصرية للاتصالات في كأس مصر
  https://ekhbary24.com/article/56873
- Sun 15 Nov | مانكيش نت | المصرية للاتصالات تحقق فوزًا مثيرًا على كهرباء الإسماعيلية
  https://mangish.net/المصرية-للاتصالات-تحقق-فوزًا-مثيرًا-ع/
## PHDC  (8 leads)
- Mon 16 Nov | followict | ياسين منصور: بالم هيلز تضخ 13 مليار جنيه في الإنشاءات وتنهي 2,210 وحدة خلال 9 أشهر
  https://followict.news/ياسين-منصور-بالم-هيلز-تضخ-13-مليار-جنيه-ف/
  > كشفت شركة بالم هيلز للتعمير عن تحقيق أداء تشغيلي ومالي قوي خلال الأشهر التسعة الأولى من عام 2026، مدعومة باستمرار الطلب على مشروعاتها العقارية، وارتفاع معدلات التنفيذ والتسليم، إلى جانب نمو التحصيلات النقدية وتعزيز قدرتها على تمويل خططها الإنشائية، في إطار استراتيجية تستهدف تحقيق النمو مع الحفاظ على مستويات مدروسة من المخاطر المالية. [Figures on the page: unaudited or preliminary; nine months. Check which one each figure is.]
- Mon 16 Nov | followict | تسليمات بالم هيلز الأرشيف
  https://followict.news/tag/تسليمات-بالم-هيلز/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | CNBC عربية | أرباح "بالم هيلز" المصرية ترتفع هامشياً إلى 1.1 مليار جنيه في الربع الثالث
  https://www.cnbcarabia.com/159896/2026/16/11/أرباح-"بالم-هيلز"-المصرية-ترتفع-هامشياً-إلى-1.1-مليار-جنيه-في-الربع-الثالث
  > ارتفعت أرباح شركة بالم هيلز للتعمير هامشياً في الربع الثالث من العام الحالي مسجلة 1.1 مليار جنيه بعد خصم حقوق الأقلية مقارنة مع 1.09 مليار جنيه في الربع المماثل من العام السابق. [Figures on the page: one quarter; attributable to shareholders. Check which one each figure is.]
- Mon 16 Nov | المصدر | بالم هيلز تحقق مبيعات بقيمة 214.1 مليار جنيه خلال 9 أشهر
  https://www.almasdar.com/176122
  > بالم هيلز تحقق مبيعات بقيمة 214.1 مليار جنيه خلال 9 أشهر حققت شركة بالم هيلز للتعمير، مبيعات جديدة بقيمة 214.1 مليار جنيه خلال الأشهر التسعة الأولى من عام 2026، بمعدل نمو 18% على أساس سنوي، في ظل استمرار قوة الطلب على محفظة مشروعات الشركة المتنوعة، ومواصلة استراتيجية النمو المنضبط تحقيق نتائج إيجابية.
- Mon 16 Nov | التعمير | ياسين منصور: 293 مليار جنيه أوراق قبض توفر لبالم هيلز غطاءً نقديًا وتدعم خططها الإنشائية
  https://eltaameer.com/archives/484791
- Mon 16 Nov | التعمير | بالم هيلز تحقق 214.1 مليار جنيه مبيعات خلال 9 أشهر بنمو 18%
  https://eltaameer.com/archives/484787
- Mon 16 Nov | جريدة المال | بالم هيلز للتعمير تحقق مبيعات بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://almalnews.com/2147741/بالم-هيلز-للتعمير-تحقق-مبيعات-بقيمة-214/
- Mon 16 Nov | - سي نيوز | بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://www.cnewsarab.com/بالم-هيلز-للتعمير-تحقق-مبيعات-جديدة-بق/
## SWDY  (8 leads)
- Mon 16 Nov | اخبارك نت | «السويدي للتنمية» تستهدف إنهاء تطوير المرحلة الأولى من مشروعها الصناعي بتنزانيا خلال النصف الأول من 2027 | أموال الغد
  https://akhbarak.net/news/details/49552532/4/السويدي-للتنمية-تستهدف-إنهاء-تطوير-المرحلة-الأولى-من-مشروعها-الصناعي-بتنزانيا-خلال-النصف-الأول-من-2027-أموال-الغد
  > تستهدف شركة السويدي للتنمية الصناعية، التابعة لمجموعة السويدي إليكتريك، جذب استثمارات تقدر بنحو مليار دولار للمرحلة الأولى من مشروع مدينتها الصناعية في تنزانيا، والتي تمتد على مساحة مليون متر مربع، ضمن خطة لتطوير مدينة صناعية متكاملة على مساحة إجمالية تبلغ 2.6 مليون متر مربع.
- Mon 16 Nov | جريدة باور نيوز الاخبارية | السويدي إليكتريك تبحث مع وزير التجارة والصناعة الهندي فرص التعاون في المعدات الكهربائية والعدادات الذكية ومراكز البيانات
  https://powernews.cc/?p=294175
  > التقى المهندس أحمد السويدي، الرئيس التنفيذي والعضو المنتدب لشركة السويدي إليكتريك، والمهندس أحمد فتحي السويدي، الرئيس التنفيذي لشركة السويدي إليكتريك في السعودية وقطر وجنوب آسيا وقطاع إكسسوارات الكابلات، بمعالي السيد بيوش جويال، وزير التجارة والصناعة الهندي، خلال زيارته إلى القاهرة، لبحث فرص تعزيز التعاون الثنائي وتوسيع آفاق الشراكات الاستراتيجية بين الجانبين.
- Mon 16 Nov | scanx.trade | Power Mech Projects wins Rs 492 crore work order from Elsewedy-Sinohydro JV for Rabigh 2 IPP Expansion
  https://scanx.trade/stock-market-news/companies/gokaldas-exports-schedules-investor-meetings-bengaluru-nov-19-20/56383794
  (page: did not load (404))
## ORAS  (4 leads)
- Mon 16 Nov | Energy Global | ENGIE-Aeolus-Orascom Construction consortium achieves financial close
  https://www.energyglobal.com/wind/16112026/engie-aeolus-orascom-construction-consortium-achieves-financial-close/
  > The Shokeir Wind Energy consortium comprising ENGIE (35%), Aeolus SAS (40%), and Orascom Construction (25%) has achieved financial close on the new 900 MW wind farm located near Ras Shokeir in the Gulf of Suez, Egypt. The project will double the consortium’s operational wind power capacity in Egypt to 1.8 GW once fully operational.
- Mon 16 Nov | جريدة باور نيوز الاخبارية | تحالف يضم أوراسكوم كونستراكشون يحقق الإغلاق المالي لمشروع رياح جديد في مصر
  https://news.google.com/rss/articles/CBMiREFVX3lxTE85WlpWNjhMbDk0ZmpjSklWZTJkMjVDUGRaOXFIWV96bWV2Q0RMR2ZvbWREXzFuREw1WmVtOWxOdDQ3R29n?oc=5
  > أعلنت شركة أوراسكوم كونستراكشون أن تحالف «شقير لطاقة الرياح»، الذي يضم شركة إنجي الفرنسية بنسبة 35%، وشركة Aeolus اليابانية بنسبة 40%، وشركة أوراسكوم كونستراكشون بنسبة 25%، قد حقق الإغلاق المالي لمشروع محطة جديدة لطاقة الرياح بقدرة 900 ميغاوات، بالقرب من منطقة رأس شقير على خليج السويس في مصر.
- Sun 15 Nov | Prop News Time | ENGIE, Aeolus and Orascom Construction achieve financial close for 900 MW wind farm in Egypt
  https://propnewstime.com/latestnewsstories/NDAyNzg=/engie-aeolus-and-orascom-construction-achieve-financial-close-for-900-mw-wind-farm-in-egypt
  > The Gulf conflict has disrupted global supply chains, pushed... REITs have changed the way commercial real estate is owned a... A consortium comprising ENGIE, Aeolus and Orascom Construction has achieved financial close for a 900 MW wind farm near Ras Shokeir on Egypt’s Gulf of Suez coast.
## FWRY  (8 leads)
- Mon 16 Nov | EnterpriseAM | GB Corp’s income rises 9.9% in 3Q, Fawry’s climbs 37.5%
  https://enterpriseam.com/egypt/2026/11/17/gb-corps-income-rises-9-9-in-3q-fawrys-climbs-37-5/
  > EGX-listed GB Corp’s net income rose 9.9% y-o-y to EGP 824.5 mn in 3Q 2026, while its revenue increased 23.7% to EGP 26.8 bn, according to the company’s financial statements (pdf). For 9M, net income fell 13.9% y-o-y to EGP 2.09 bn, even as revenue rose 30.9% to EGP 75.3 bn.
- Mon 16 Nov | CNN الاقتصادية | أرباح فوري المصرية تقفز 37% في الربع الثالث بدفعة من المدفوعات الرقمية
  https://cnnbusinessarabic.com/finance-markets/1152629/أرباح-فوري-المصرية-تقفز-37-في-الربع-الثالث-بدفعة-من-المدفوعات-الرقمية
  > أرباح «فوري» تقفز 37.4% إلى 1.1 مليار جنيه خلال الربع الثالث (رويترز) سجلت شركة «فوري» لتكنولوجيا البنوك والمدفوعات الإلكترونية نمواً في أرباحها خلال الربع الثالث من عام 2026، بدعم من ارتفاع الإيرادات وتوسع نشاطها في خدمات المدفوعات الرقمية والحلول المالية، وفقاً للقوائم المالية المجمعة للشركة. [Figures on the page: consolidated; unaudited or preliminary; one quarter. Check which one each figure is.]
- Mon 16 Nov | waya.media | Fawry Allocates USD 1.6M for Technology Investments by End of 2026
  https://waya.media/fawry-allocates-usd-1-6m-for-technology-investments-by-end-of-2026/
  > Fawry is allocating EGP 80 million (approx. USD 1.6M) for investments through the end of 2026. The company also plans to introduce a microinsurance service in 2027. The investment plans reflect Fawry’s continued focus on technology development, with approximately 10% of its revenues directed towards technology investments.
## ABUK  (8 leads)
- Mon 16 Nov | عالم المال | رئيس مجلس الإدارة والعضو المنتدب لشركة أبوقير للأسمدة والصناعات الكيماوية
  https://alamalmal.net/tagnews/261170/رئيس-مجلس-الإدارة-والعضو-المنتدب-لشركة-أبوقير/1
  (page: only 22 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 15 Nov | القاهرة 24 | هيثم شعبان يجتمع مع مسؤولي أبو قير للأسمدة لبحث تدعيم صفوف الفريق في يناير
  https://www.cairo24.com/2529932
  > هيثم شعبان يجتمع مع مسؤولي أبو قير للأسمدة لبحث تدعيم صفوف الفريق في يناير يعقد هيثم شعبان المدير الفني للفريق الأول لكرة القدم بـ نادي أبوقير للأسمدة اجتماعًا خلال الأسبوع الحالي مع مجلس إدارة النادي، لمناقشة عدد من الملفات الخاصة بالفريق الأول، وأبرزها المراكز التي تحتاج إلى تدعيم.
- Sun 15 Nov | عالم الطاقة | أبوقير للأسمدة تعزز ريادتها في الاستدامة.. توقيع اتفاقية مع الهيئة العربية للتصنيع لتنفيذ المرحلة الثانية
  https://www.alamaltaqa.com/52250
  > أبوقير للأسمدة تعزز ريادتها في الاستدامة.. توقيع اتفاقية مع الهيئة العربية للتصنيع لتنفيذ المرحلة الثانية
- Sun 15 Nov | أموال الغد | أبو قير للأسمدة تبدأ صيانة وتحديث مصنع «أبوقير 2» لمدة أسبوعين
  https://amwalalghad.com/2026/11/15/أبو-قير-للأسمدة-تبدأ-صيانة-وتحديث-مصنع/
  > كشفت شركة أبو قير للأسمدة والصناعات الكيماوية، بدء تنفيذ أعمال الصيانة الدورية وإجراء تحديثات لبعض المعدات بمصنع أبوقير (2)، في إطار خطة الشركة لإدارة وتوزيع الأحمال وتعظيم الاستفادة من حصص الغاز الطبيعي الموردة.
- Sun 15 Nov | بوابة بلوم | بعد خفض إمدادات الغاز.. أبوقير للأسمدة تبدأ صيانة أحد مصانعها
  https://bloom-gate.com/أسواق/بعد-خفض-إمدادات-الغاز-أبوقير-للأسمدة-ت/
- Sun 15 Nov | أصول مصر | أبوقير للأسمدة تبدأ صيانة أحد مصانعها لمدة أسبوعين بعد خفض إمدادات الغاز 33%
  https://www.osoulmisrmagazine.com/452617
- Sun 15 Nov | جريدة الملتقى الاقتصادي | «أبوقير للأسمدة» تبدأ صيانة مصنع 2 لمدة أسبوعين بعد توقف الإنتاج بسبب خفض الغاز
  https://www.moltakaaliqtisad.online/أبوقير-للأسمدة-تبدأ-صيانة-مصنع-2-لمدة/
- Sun 15 Nov | ايكونومي بلس | للحد من تأثير خفض إمدادات الغاز 33%.. "أبوقير للأسمدة" تبدأ صيانة أحد مصانعها
  https://economyplusme.com/ar/news/34167
## HRHO  (8 leads)
- Tue 17 Nov | مجلة أرقام | إي اف چي هيرميس المنسق الدولي الأوحد ومدير الطرح الأوحد
  https://arqam.news/610730/
  > أعلنت شركة مصر لتأمينات الحياة اعتزامها طرح 750 مليون سهم من أسهمها العادية في البورصة المصرية، بما يمثل 15% من رأس المال المصدر للشركة، في خطوة تستهدف إتمام أول طرح عام أولي لها، ومن المتوقع أن يمثل أول قيد كبير لشركة تأمين في البورصة المصرية.
- Tue 17 Nov | شبكة تواصل الإخبارية | إي اف چي هيرميس المنسق الدولي الأوحد ومدير الطرح الأوحد لأسهم مصر لتأمينات الحياة في البورصة المصرية
  https://twaslnews1.twaslnews.com/7830862/
  (page: did not load (403))
- Tue 17 Nov | بوابة التكنولوجيا المالية | EFG Hermes Named International Coordinator and Sole Bookrunner as Misr Life Insurance Officially Announces IPO of 15% of Its Shares on the Egyptian Exchange
  https://fintechgate.net/257678
  > EFG Hermes Named International Coordinator and Sole Bookrunner as Misr Life Insurance Officially Announces IPO of 15% of Its Shares on the Egyptian Exchange Misr Life Insurance Company S.A.E.
- Tue 17 Nov | شبكة تواصل الإخبارية | إي إف چي هيرميس المنسق الدولي ومدير الطرح الأوحد لأسهم مصر لتأمينات الحياة في البورصة
  https://twaslnews1.twaslnews.com/7829216/
  (page: did not load (403))
- Tue 17 Nov | البوابة نيوز | إي إف جي هيرميس المنسق الدولي الأوحد.. مصر لتأمينات الحياة تعلن طرح 15% من أسهمها في البورصة
  https://www.albawabhnews.com/5436950
- Tue 17 Nov | Pioneers Misr | إي إف چي هيرميس مستشاراً مالياً لصفقة طرح مصر لتأمينات الحياة في البورصة
  https://pioneersmisr.com/123818/
- Tue 17 Nov | - سي نيوز | إي إف جي هيرميس مديراً لطرح 15% من أسهم مصر لتأمينات الحياة بالبورصة المصرية خلال ديسمبر
  https://www.cnewsarab.com/إي-إف-جي-هيرميس-مديراً-لطرح-15-من-أسهم-مصر/
- Mon 16 Nov | جريدة المال | التابعة لـ «إي إف چي هيرميس».. «مصر للتعليم» تفتح باب التقديم لمدرستها البريطانية الأولى بالإسكندرية
  https://almalnews.com/2147699/التابعة-لـ-«إي-إف-چي-هيرميس»-«مصر/
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
- Sun 15 Nov | جريدة المال | أرباح الإسكندرية لتداول الحاويات ترتفع 15% لتسجل 5.72 مليار جنيه في 9 أشهر
  https://almalnews.com/2147339/أرباح-الإسكندرية-لتداول-الحاويات-ترتفع-15-لتسجل/
  > أظهرت القوائم المالية لشركة الإسكندرية لتداول الحاويات والبضائع عن التسعة أشهر الأولى من العام الجاري، نمو أرباح الشركة على أساس سنوي بنسبة 15%.
## MFPC  (8 leads)
- Mon 16 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | العقارية توقع عقدًا مع شركة موبكو لتنفيذ الحزمة الأولى من مشروع بورتا جدة بقيمة 463.1 مليون ريال
  https://www.argaam.com/ar/article/articledetail/id/1936577
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 16 Nov | Quantum Commodity Intelligence | Egyptian fertiliser producer Mopco sees 9M profits climb
  https://www.qcintel.com/ammonia/article/egyptian-fertiliser-producer-mopco-sees-9m-profits-climb-77634.html
  (page read: it never names the company, so probably not about it: skip)
- Mon 16 Nov | CNBC عربية | بدعم من نمو المبيعات.. أرباح "موبكو" المصرية ترتفع 56% في 9 أشهر
  https://www.cnbcarabia.com/159849/2026/15/11/بدعم-من-نمو-المبيعات..-أرباح-"موبكو"-المصرية-ترتفع-56--في-9-أشهر
  > ارتفعت الأرباح المجمعة لشركة مصر لإنتاج الأسمدة "موبكو" خلال الأشهر التسعة الأولى من العام بنسبة 56% لتصل إلى 12 مليار جنيه بعد خصم الضرائب، بدعم من زيادة المبيعات بنسبة 47% على أساس سنوي مسجلة نحو 27.5 مليار جنيه. [Figures on the page: consolidated; one quarter. Check which one each figure is.]
- Mon 16 Nov | Dealroom | MOPCO lands $165M loan for $265M plant overhaul
  https://app.dealroom.co/news/note/mopco-lands-165m-loan-for-265m-plant-overhaul
  (page: did not load (403))
- Mon 16 Nov | Egypt Oil & Gas | MOPCO Unveils $265Mn Financing Package for Plant Upgrades
  https://egyptoil-gas.com/news/mopco-secures-165-mn-loan-to-modernize-production-facilities/
- Sun 15 Nov | شبكة تواصل الإخبارية | أرباح موبكو ترتفع 56% إلى 12 مليار جنيه خلال 9 أشهر
  https://twaslnews1.twaslnews.com/7753826/
- Sun 15 Nov | جريدة باور نيوز الاخبارية | أرباح موبكو تقفز إلى 12.1 مليار جنيه في 9 أشهر بزيادة قدره نمو 56% مقابل الفترة المماثلة من العام السابق
  https://news.google.com/rss/articles/CBMiREFVX3lxTE9aWFFCY29JYmlqN0xFSkprY3FvRVgyNTFvZHhYMWxRZmx6c3l4X0FtSGc1MTBSRHI1TGk3dTFOYW9BdWFP?oc=5
- Sun 15 Nov | جريدة باور نيوز الاخبارية | موبكو تحصل على تمويل بقيمة 165 مليون دولار لتطوير وتحديث مصانعها
  https://powernews.cc/?p=294102
## EAST  (1 leads)
- Mon 16 Nov | ad-hoc-news.de | Eastern Company stock reports sharp nine-month profit growth
  https://news.google.com/rss/articles/CBMiuwFBVV95cUxQSEZ5S0Z5dkV0N3FraDl6N0w2dXFFMmJQbXpJaG03aHprM3hkZzU4RG1xalMxc0M4czBUUkdxR3pyMU9rcWFwOGc3ZHBPYUVCTEM4Mk5xY29KMzBtVWk3elc0X3U4NDdJQVE1T25aY295cXNvRVNMSDRFYlN5ZW5jc3VkM0szNnAzUmk
  > Eastern Company reported a sharp increase in earnings for the first nine months of 2026, with consolidated net profit reaching about EGP 9 billion, according to Arab Finance. The report was published on November 11, 2026, and said profit increased 39 percent from EGP 6.48 billion in the comparable period. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
## EFIH  (1 leads)
- Arabic search failed: HTTP Error 429: Too Many Requests
- Mon 16 Nov | ad-hoc-news.de | e-finance stock: Nine-month net profit rises 41.7%
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/e-finance-stock-nine-month-net-profit-rises-41-7/70518460
  > e-finance reported a 41.74 percent year-on-year increase in consolidated net profit after tax and non-controlling interests for the nine months ended September 30, according to Arab Finance. The disclosure was published on November 12, 2026, and puts consolidated profit at EGP 2.593 billion, compared with EGP 1.829 billion in the year-earlier period. [Figures on the page: standalone; consolidated; nine months; attributable to shareholders. Check which one each figure is.]
## BQDC  (8 leads)
- Tue 17 Nov | زاد الاردن | بنك القاهرة عمان راعيًا فضيًا لجائزة الحسين لأبحاث السرطان لعام 2026
  https://www.jordanzad.com/index.php?page=article&id=775388
  > زاد الاردن الاخباري -
- Mon 16 Nov | بوابة المصرف | 6,771 جنيهًا في شهر.. تفاصيل عائد 16.25% المعلن لودائع بنك القاهرة
  https://www.almasraf.news/6771-جنيهًا-في-شهر-تفاصيل-عائد-16-25-المعلن-لود/
  > أبرز تحديث لأسعار ودائع بنك القاهرة بالجنيه المصري عائدًا سنويًا يصل إلى 16.25% على الودائع لمدة شهر واحد، بحد أدنى يبلغ 500 ألف جنيه، ما يعادل نحو 6,771 جنيهًا خلال شهر عند صرف العائد في نهاية المدة، وفق حساب تقريبي يفترض تقسيم السنة إلى 12 شهرًا متساويًا.
- Mon 16 Nov | شبابيك | وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
  https://shbabbek.com/show/288015
  > وظائف بنك القاهرة 2026.. الشروط الكاملة ورابط التقديم لوظيفة مراجع أول مخاطر
## EGAL  (2 leads)
- Mon 16 Nov | شبكة تواصل الإخبارية | اليوم.. نهاية حق توزيع 16 جنيهًا لسهم “مصر للألومنيوم”
  https://news.google.com/rss/articles/CBMiU0FVX3lxTE9rS094OGw5ZVI4bDAtMmEzdldnWUkxSEF6NWJ1LW5zTmNNQ2lYT01QcFRNMkxsUVBxQ3BieGdYdkh3dVJaN1htU0syZ3ppa1pGaGhB?oc=5
  (page: did not load (403))
- Mon 16 Nov | مجلة البوصلة الاقتصادية | اليوم.. نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم
  https://alboslanews.com/أسواق-مال/اليوم-نهاية-حق-الحصول-على-التوزيع-النقدي-لـ-مصر-للألومنيوم-430846
  > نهاية حق الحصول على التوزيع النقدي لـ مصر للألومنيوم الإثنين 16 نوفمبر 2026 -10:16 ينتهي مع ختام جلسة اليوم الإثنين حق الحصول على توزيع الكوبون النقدي لشركة مصر للألومنيوم، بواقع 16 جنيه للسهم. على أن يتم صرف التوزيع في 19 نوفمبر 2026، وتتولى التنفيذ شركة مصر للمقاصة والإيداع والقيد المركزي.
## AMOC  (1 leads)
- Sun 15 Nov | ad-hoc-news.de | Alexandria Mineral Oils stock posts 153.7% nine-month profit gain
  https://news.google.com/rss/articles/CBMiwAFBVV95cUxPejNhUWpWVHF6bDFYdmZtcEY4MlFHZjFzU25rNGpnNWtZdkxfZHJlWG1IcGtad2ZtdVhOWFlRYU1VZ2F6dEhnb0t6Q1I4MHRLVFZRMHFOT1dNRjRkODFNZS0xZUg3WGdiRzc2UjB1N2VUZHQ3S3VEaFk5S1NJQW9CWHNUMllTd0lMelh
  > Alexandria Mineral Oils reported a sharp rise in nine-month net profit in a filing published on November 15, 2026. [Figures on the page: standalone; consolidated. Check which one each figure is.]
## EFID  (8 leads)
- Tue 17 Nov | Daily News Egypt | Edita’s Q3 profit jumps 41.5% on record sales
  https://dailynewsegypt.com/2026/11/16/editas-q3-profit-jumps-41-5-on-record-sales/
  > Edita Food Industries (EFID.CA), one of Egypt’s leading packaged snack-food makers, reported a 41.5% year-on-year rise in net profit to EGP 938.1m for the third quarter (Q3) of 2026. Revenues reached EGP 7.3bn, the highest quarterly figure in the company’s history. Q3 revenues rose 32.9% from the same quarter of 2025. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Mon 16 Nov | عالم المال | أخبار البورصة المصرية اليوم.. «إيديتا» تتصدر الرابحين و«كرستمارك» الأكثر تراجعًا
  https://alamalmal.net/article/943439/أخبار-البورصة-المصرية-اليوم-«إيديتا»-تتصدر-الرابحين
  > تباين أداء الأسهم بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الاثنين 16 نوفمبر 2026، حيث تصدر سهم شركة إيديتا للصناعات الغذائية قائمة الأسهم الأكثر ارتفاعًا بنسبة 7.44%، فيما جاء سهم شركة كرستمارك للمقاولات والتطوير العقاري في صدارة الأسهم الأكثر انخفاضًا بنسبة 20%. الأسهم الأكثر ارتفاعًا بالبورصة المصرية
- Mon 16 Nov | شبكة تواصل الإخبارية | “إيديتا” تقرر تخفيض رأسمالها إلى 416.7 مليون جنيه عبر إعدام أسهم خزينة
  https://twaslnews1.twaslnews.com/7792952/
  (page: did not load (403))
- Mon 16 Nov | جريدة المال | «إيديتا للصناعات الغذائية» تقرر تخفيض رأس المال عبر إعدام أسهم خزينة
  https://almalnews.com/2147686/«إيديتا-للصناعات-الغذائية»-تقرر-تخفيض-رأس-المال/
  > وافق مجلس إدارة شركة إيديتا للصناعات الغذائية، على دعوة الجمعية العامة غير العادية للنظر في تخفيض رأسمال الشركة عبر إعدام أسهم الخزينة. [Figures on the page: standalone; consolidated. Check which one each figure is.]
- Mon 16 Nov | شبكة تواصل الإخبارية | أرباح «إيديتا» تقفز 52% خلال أول 9 أشهر من 2026
  https://twaslnews1.twaslnews.com/7788876/
- Mon 16 Nov | أصول مصر | «إيديتا» تحقق أرباحاً بقيمة 938 مليون جنيه خلال الربع الثالث بنمو 41.5%
  https://www.osoulmisrmagazine.com/452724
- Mon 16 Nov | بوابة مولانا | إيديتا تقفز بأرباحها 44.1% في الربع الثالث من 2026
  https://mwlana.com/details/303664/
- Mon 16 Nov | أموال الغد | أرباح إيديتا للصناعات الغذائية تقفز 52% إلى 2.61 مليار جنيه خلال 9 أشهر
  https://amwalalghad.com/2026/11/16/أرباح-إيديتا-للصناعات-الغذائية-تقفز-52-إ/
## AAPL  (7 leads)
- Tue 17 Nov | Benzinga | Apple Names 26-Year Veteran Corey Fugman To Run Apple Pay and Wallet As Jennifer Bailey Exits: Report
  https://www.benzinga.com/markets/tech/26/11/63329966/apple-reportedly-taps-corey-fugman-to-run-apple-pay-and-wallet-jennifer-bailey
  (page: did not load (403))
- Tue 17 Nov | Yahoo Finance | Gene Munster Says Nvidia Could Be the Next Apple if Investors ‘Sleep Well at Night’
  https://finance.yahoo.com/markets/stocks/articles/gene-munster-says-nvidia-could-032355214.html
  > (NASDAQ:NVDA) could earn a higher earnings multiple even if growth slows, investor Gene Munster said Monday, as long as customers return for chip upgrades. Sees Apple Playbook for Nvidia In a post on X, the managing partner at Deepwater Asset Management compared Nvidia with Apple Inc.
- Tue 17 Nov | 9to5Mac | Former Apple chairman Arthur Levinson files to sell $31.8 million in company stock
  https://9to5mac.com/2026/11/16/former-apple-chairman-arthur-levinson-files-to-sell-31-8-million-in-company-stock/
  > Arthur Levinson, who currently serves as Apple’s lead independent director, informed the SEC today of his plans to sell 90,000 shares of Apple stock worth approximately $31.8 million. Here are the details.
## MSFT  (8 leads)
- Tue 17 Nov | Investing.com India | Microsoft Outage Disrupts Services Worldwide
  https://news.google.com/rss/articles/CBMikgFBVV95cUxNT2htY09iSm5HUW9HeklXSklZZ3JobWxxRjVuUTZNTHNVV2R3cTVLYUx6N0FJQkszeWRRSkdoZUo1NG9qZk52cXpxaEtyMXl2RmF4OXBfNXdJcmpvbzdmNkhPd0VtR1p0RDNMcC1kRFhnaV9OQXBWbzBDaFlOYTR4M2hyMV9hTFRZN18
  (page: Google's link could not be resolved to the outlet's page)
- Tue 17 Nov | MLQ.ai | 13F roundup: Gavin Baker's Atreides buys a chip ETF put and Alphabet calls, Maverick and Tudor cut Microsoft and Astera
  https://mlq.ai/news/13f-roundup-gavin-bakers-atreides-buys-a-chip-etf-put-and-alphabet-calls-maverick-and-tudor-cut-microsoft-and-astera/
  (page: did not load (403))
- Tue 17 Nov | Investing.com India | Form 4 Microsoft Corporation: Amy Coleman (EVP, Chief Human Resources Off) For: 16 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-microsoft-corporation-amy-coleman-evp-chief-human-resources-off-for-16-november-93CH-5708614
  (page: did not load (403))
## NVDA  (8 leads)
- Tue 17 Nov | The Motley Fool | This Is What It Would Take for Me to Buy Nvidia Stock
  https://www.fool.com/investing/2026/11/17/this-is-what-it-would-take-for-me-to-buy-nvidia-stock/
  > What happened to Nvidia (NVDA -4.12%) stock this week is an excellent example of a black swan event. Nvidia had been flying high for years as the face of artificial intelligence (AI), and the market didn't see anything like this coming.
- Tue 17 Nov | The Washington Post | Stock market drops amid continued Nvidia fallout
  https://www.washingtonpost.com/business/2026/11/16/stock-market-drops-amid-continued-nvidia-fallout/
  (page: did not load (TimeoutError))
- Tue 17 Nov | Yahoo Finance UK | The Nvidia share price is down 30% and UK investors are buying. I’m not convinced it’s a bargain
  https://uk.finance.yahoo.com/news/nvidia-share-price-down-30-064600224.html
  > The Nvidia (NASDAQ:NVDA) share price has fallen sharply since Jensen Huang resigned last week (12 November), ending a 33-year tenure as CEO. Yet UK investors haven't been deterred, treating the sell-off as a chance to buy.
- Tue 17 Nov | The Block | Cathie Wood's Ark Invest loads up on crypto stocks while selling $85 million in Nvidia
  https://www.theblock.co/news/business/2026-11-17-ark-invest-buys-crypto-stocks-sells-nvidia-442080
  (page: did not load (403))
- Tue 17 Nov | Yahoo Finance | Nvidia faces alarming revenue questions before earnings
  https://finance.yahoo.com/markets/stocks/articles/nvidia-faces-alarming-revenue-questions-050300921.html
- Tue 17 Nov | USA Today | Nvidia set for first earnings call since Jensen Huang's resignation
  https://www.usatoday.com/story/money/2026/11/17/nvidia-earnings-call-how-to-watch/92819260007/
- Tue 17 Nov | The Motley Fool | Jensen Huang Stepped Away From Nvidia, and That Might Not Be the Company's Biggest Problem
  https://www.fool.com/investing/2026/11/16/jensen-huang-stepped-away-from-nvidia-and-that-might-not-even-be-the-company-s-biggest-problem/
- Tue 17 Nov | Yahoo Finance | Nvidia “Could Have Theoretically Lost 30% of Demand” and Still Hit Its Forecast, Says Dan Niles
  https://news.google.com/rss/articles/CBMioAFBVV95cUxQdmdtNFYzdjRzVnF3TWNRa3gxWllsSE5iaXZ1Q08xX3h5UnB3X3Nvc1RycFhiWTlCT3F0QXBmS3prQzN2cXdMcDdyQUgtSjA2MXBkQ2ZTUUxkOFJsek9XQjYzVmJ1akJkVmdZc1JYTkk3MjVubFhNRWtEVkxVTm1HZU53QUdTdkN1amV
## GOOGL  (8 leads)
- Tue 17 Nov | Pluang | Alphabet posts record $127.6B revenue with 25% ...
  https://pluang.com/en/news-feed/alphabet-kasus-pendanaan-adalah-peluang-bull
  (page: did not load (403))
- Tue 17 Nov | Seeking Alpha | Alphabet: The Funding Scare Is The Bull Case
  https://seekingalpha.com/article/4968872-alphabet-stock-funding-scare-bull-case
  (page: did not load (403))
- Tue 17 Nov | Briefs Finance | Alphabet Backs $3B Prepaid Energy Bonds
  https://www.briefs.co/news/alphabet-to-anchor-two-prepaid-energy-bond-deals-totaling-3/
  > Fresh preliminary filings list Alphabet as the funding recipient for two upcoming prepaid energy transactions worth a combined $3 billion. The bonds are planned through the Southeast Energy Authority and handled by Goldman Sachs Group Inc., which the documents describe as a top underwriter in this niche.
- Tue 17 Nov | FXLeaders | Alphabet Stock Extends Decline as $200B Spending and Google Anthropic Investment Raise Concerns
  https://www.fxleaders.com/news/2026/11/16/alphabet-stock-extends-decline-as-200b-spending-and-google-anthropic-investment-raise-concerns/
  > Alphabet Stock Extends Decline as $200B Spending and Google Anthropic Investment Raise Concerns Alphabet shares reversed below $300 and fallen toward $280 despite new Gemini products, strong Google Cloud growth and another $10 billion Anthropic investment, as investors question whether rising infrastructure costs can generate sufficient returns.
- Tue 17 Nov | ad-hoc-news.de | Jefferies stock after company files notes tied to Amazon, Alphabet
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/jefferies-stock-after-company-files-notes-tied-to-amazon-alphabet/70523359
- Tue 17 Nov | Investing.com UK | Form 4 Alphabet Inc Class A: Kavitark Ram Shriram (Director) For: 12 November
  https://news.google.com/rss/articles/CBMizwFBVV95cUxNSW5QcVp5REkyU3NwckNFeUhfbGdBNkRjRGE3NHFoV2RhSWNkazRrWXY3eU5RbTJLTU5lVWhOa21xZWRlY0c2M3RFdmdleEVkRDFReExUUndOUTBMQzhDbEVBSkVmakJZdXdPME5oVWpxeWt6YXYzT190U2RJb1VMSHMtNU5CZXhLeEd
- Mon 16 Nov | Investing.com India | Form 4 Alphabet Inc Class A: John L. Hennessy (Director) For: 12 November By Investing.com
  https://in.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-john-l-hennessy-director-for-12-november-93CH-5708313
- Mon 16 Nov | Investing.com | Alphabet director John L. Hennessy sells $90,000 in class C stock
  https://www.investing.com/news/insider-trading-news/alphabet-director-john-l-hennessy-sells-90000-in-class-c-stock-93CH-5031263
## META  (8 leads)
- Tue 17 Nov | Gotrade | Meta Stock Falls 2.4% as AI Stocks Slide (Nov 16)
  https://www.heygotrade.com/en/news/meta-meta-stock-news-november-17-2026/
  > AI-powered contentSome parts of this article are powered by AI. Meta Platforms (META) fell 2.38% to $626.41 on November 16, 2026, slightly less than the Nasdaq Composite's 2.49% drop. Financial media tied the decline to a sell-off in AI-linked stocks led by Nvidia and named no Meta-specific news.
- Tue 17 Nov | Stocktwits | Meta Platforms Stock Price, News, Analysis and Trading Ideas
  https://stocktwits.com/symbol/META
  > engages in the development of social media applications. It builds technology that helps people connect and share, find communities, and grow businesses. Saverin on February 4, 2004, and is headquartered in Menlo Park, CA.
- Tue 17 Nov | Simply Wall St | Meta Platforms (META) Faces Fresh Questions As Insurers Pile Into AI Debt
  https://simplywall.st/stocks/us/media/nasdaq-meta/meta-platforms/news/meta-platforms-meta-faces-fresh-questions-as-insurers-pile-i
  > Meta Platforms (NasdaqGS:META) is linked to a growing pool of insurer investments in AI data center debt uncovered in a recent investigation. Large life insurers are reported to be buying complex securities tied to Meta backed AI infrastructure where Meta often holds only partial ownership.
- Mon 16 Nov | GuruFocus | Louis Moore Bacon's Top Q3 2026 Move: Meta Platforms Inc at a 4.
  https://news.google.com/rss/articles/CBMiuwFBVV95cUxNM3NCUGtEYTJtaGMybWY4OEpqUm5iRW0xUzhYcnA4Q3pkRVNWN1ZEOG5TcU5PdERiOFB6ZWN3VVNyZVE2THNWXzlKeFJzWGp2M3FNZlltT1hncFJRaUVlclNCeC1NV2pXY1ljSjZqMV8tcjFqQWY4ZWNLb0JVYWRKRVVZV0t6UEpXOW1
  (page: did not load (403))
- Mon 16 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Stock Falls 2.4% - Time to Sell?
  https://news.google.com/rss/articles/CBMitAFBVV95cUxPZTBFcHlIZkRlVXFFelNrbVNIc1ZEWWwyMUNSLXJsVC1qcDI2Qmt6NERxWjU0S2hmOEhMZlprZnpSR0RSY09hVEl1TTFKSHo2Mm9sWEVrYllxZkJXTzdQbzRBTkU0V3lSSzBiVmlqQTQ5c0pZMDFWZ2JfWWFld2xNd2w5WjhmNGoyelJ
- Mon 16 Nov | MLQ.ai | 13F roundup: Tepper adds Micron and Nvidia, Loeb buys Meta, Viking halves Meta and Lone Pine buys Amazon and Intel
  https://mlq.ai/news/13f-roundup-tepper-adds-micron-and-nvidia-loeb-buys-meta-viking-halves-meta-and-lone-pine-buys-amazon-and-intel/
- Mon 16 Nov | Benzinga | Here’s How Much You Would Have Made Owning Meta Platforms Stock In The Last 10 Years
  https://www.benzinga.com/news/26/11/63326103/here-s-how-much-you-would-have-made-owning-meta-platforms-stock-last-10-years
- Mon 16 Nov | Pluang | Italy fines Meta $887M over privacy breach, cha...
  https://news.google.com/rss/articles/CBMimAFBVV95cUxOOEk3OUIyTHJmby1yTExyV3M4dnV4OHZIR2xheWsyMmFiUm9XbGtQT2VXYU1WencwUVVGSU5JSElrRHo1eHd5R3BMSkZIZnRjVkI5WWJxLVVsX19hMXJ6em9GbzhZODk5SktsZmtZUnJ3T3k1Vk93VFRvQTlzZGg1Y0lheFk3cS1naGJ
## TSLA  (8 leads)
- Tue 17 Nov | The Globe and Mail | Elon Musk Just Killed the Cybertruck to Build Cybercabs. Here’s What It Means for Tesla Stock -- and Rivian’s.
  https://www.theglobeandmail.com/investing/markets/stocks/TSLA/pressreleases/8868688/elon-musk-just-killed-the-cybertruck-to-build-cybercabs-heres-what-it-means-for-tesla-stock-and-rivians/
  > - Tesla is ending the Cybertruck in favor of the Cybercab. - Rivian stock may benefit if the Cybertruck is retired. Tesla(NASDAQ:TSLA) is officially shutting down production of the futuristic-looking truck, replacing it with the autonomous Cybercab in the middle of next year.
- Tue 17 Nov | MarketBeat | Tesla (NASDAQ:TSLA) Stock Price Breaks Below 200 Day Moving Average - Here's Why
  https://www.marketbeat.com/instant-alerts/price-tesla-nasdaq-tsla-stock-price-breaks-below-200-day-moving-average-heres-why-2026-11-17/
  > Tesla (NASDAQ:TSLA) Stock Price Breaks Below 200 Day Moving Average - Here's Why - Tesla shares fell below their 200-day moving average, trading as low as $375.63 and last at $379.74, versus the average of $382.79; the stock was down 2.7%.
- Tue 17 Nov | Investing.com | Barclays reiterates Tesla stock rating on robotaxi progress
  https://www.investing.com/news/analyst-ratings/barclays-reiterates-tesla-stock-rating-on-robotaxi-progress-93CH-5031841
  (page: did not load (403))
- Tue 17 Nov | Gotrade | Tesla Stock (TSLA) Falls 2.7% as Tech Stocks Slide (Nov 16)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-17-2026/
  > AI-powered contentSome parts of this article are powered by AI. Shares of Tesla (TSLA) fell 2.69% to $379.74 on November 16, 2026, a move 0.20 percentage points weaker than the Nasdaq Composite. AAP reported a broad sell-off led by AI and chip companies, while TipRanks linked the slip to the Cybercab's $299 monthly autonomy subscription.
- Mon 16 Nov | Yahoo Finance | Your $300,000 in XLY Holds $125,585 in Amazon and Tesla Alone
  https://news.google.com/rss/articles/CBMijwFBVV95cUxPdFhETnduQk5xb0pwYVpkNVlvbThnS3g5c2x0RkdwSG5jc3ZUZXdvQnlwWTlVVkNQYmdXU29tQVpaZ2tMd04taGZVZEQwN19mTjhpR3pwYkdpSXE0MmczT0p5RjNmRmhtTnJwXzVOc2sxVEVpNDNYdmprR01XUUJrM3pnNmFOYjR3Q1F
- Mon 16 Nov | The New York Times | Elon Musk Wants to Merge Tesla and SpaceX. Their Businesses Already Overlap.
  https://news.google.com/rss/articles/CBMie0FVX3lxTE9ELUVFNFBiWjJzc1Nzc1RmbFkzRV9UVEtwN2VQRlBtV1VuVjR1aThINEpLOUhMYXRLRGF0N0lCbDZJWldSbERPYWxSWHFZQlVPZVlHWnpJa09sc01lRFFXR1JBU2ZrY3dFZnpJNFpLYnZRTWJVYUpxZnFnZw?oc=5
- Mon 16 Nov | MarketBeat | Tesla (NASDAQ:TSLA) Stock Falls 2.7% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-tesla-nasdaq-tsla-stock-falls-27-heres-what-happened-2026-11-16/
- Mon 16 Nov | MLQ.ai | Altimeter sells its chip-equipment stocks and Qualcomm, buys a put on a chip ETF and a Tesla stake, 13F shows
  https://mlq.ai/news/altimeter-sells-its-chip-equipment-stocks-and-qualcomm-buys-a-put-on-a-chip-etf-and-a-tesla-stake-13f-shows/
## JPM  (8 leads)
- Tue 17 Nov | Investing.com | JPMorgan downgrades Tyson stock rating to neutral on valuation
  https://www.investing.com/news/analyst-ratings/jpmorgan-downgrades-tyson-stock-rating-to-neutral-on-valuation-93CH-5031819
  (page: did not load (403))
- Tue 17 Nov | www.tokenpost.com | Bank of America Cut JPMorgan Chase Holdings by 29.52% in Q3
  https://www.tokenpost.com/news/investing/59178
  > Bank of America reduced its position in JPMorgan Chase by about 20.57 million shares, or 29.52%, in the third quarter, while Nvidia remained its largest listed holding by market value. The bank held about 200 million Nvidia shares valued at $45.578 billion as of Sept.
- Tue 17 Nov | TipRanks | JPMorgan Chase No Longer Has Notifiable Interest in Hexagon Composites
  https://www.tipranks.com/news/company-announcements/jpmorgan-chase-no-longer-has-notifiable-interest-in-hexagon-composites
  (page: did not load (403))
- Tue 17 Nov | TelegraphHerald.com | Technical issue at JPMorgan Chase triggers online problems for major banks
  https://news.google.com/rss/articles/CBMimAFBVV95cUxQU2c2aTI3aVNxdTBMb0ZrQ3hIN3YteTg4UmFmRVhWd2JUZy1DQ1NOaUFQV0N5WGhhVGpBMWJmOVJYeFBmLVRqaktfUEZob3hBZ2Q5TFp5MmJiSF9IdVVNZUJ1OXdvcFNVb1ZHTVNaTkVyQUR5T0RodlAtbFRVLUYyUGxnMUxRWXAyUGV
  (page: only 69 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | Rockdale Citizen | A technical issue at JPMorgan Chase triggers online banking delays for major US banks
  https://news.google.com/rss/articles/CBMijgJBVV95cUxQOFAxdTZrWVRSU3J4M0RZUlJLNWM2a3pRUnlfQTVpY1ZhUmtJMWktMUpRZXIyWTNDcGI5dWNfQTk3OThpbHZMdDVBWFlSZEVxRW5qUzlPRUhON0VrcHNSMGlvMkNEd2pmZnBwZWZ1SEtiMzhBNmFuVVlwaVJHanB3Y0pSSFo5NTVuWmN
- Tue 17 Nov | Decatur Daily | A technical issue at JPMorgan Chase triggers online banking delays across major US banks
  https://www.decaturdaily.com/business/a-technical-issue-at-jpmorgan-chase-triggers-online-banking-delays-across-major-us-banks/article_9e139ca8-78bd-400d-b8ff-29d38bb5f7da.html
- Tue 17 Nov | KOMO | Tech glitches hit JPMorgan Chase, United after FAA ground stop
  https://komonews.com/news/local/tech-glitches-hit-jpmorgan-chase-united-after-faa-ground-stop-cybersecurity-nationwide-banking-outage-departing-flights
- Tue 17 Nov | www.tokenpost.com | JPMorgan Chase Links Monday Transaction Disruptions to Software Bug
  https://www.tokenpost.com/news/business/59093
## XOM  (8 leads)
- Tue 17 Nov | Club of Mozambique | Mozambique: Chapo meets ExxonMobil and Eni executives to review Rovuma Basin gas projects
  https://clubofmozambique.com/news/mozambique-chapo-meets-exxonmobil-and-eni-executives-to-review-rovuma-basin-gas-projects/
  > During separate meetings at the President’s Office, the two companies presented progress on the strategic restructuring of their stakes in the natural gas projects, as well as their development plans and the expansion of operations in Cabo Delgado province.
- Tue 17 Nov | marketscreener.com | ExxonMobil starts up fifth oil project in Guyana
  https://www.marketscreener.com/news/exxonmobil-starts-up-fifth-oil-project-in-guyana-ce785edfdd8aff25
  (page: did not load (403))
- Tue 17 Nov | Splash247 | ExxonMobil pushes past million-barrel daily output in Guyana
  https://splash247.com/exxonmobil-pushes-past-million-barrel-daily-output-in-guyana/
  > US supermajor ExxonMobil has pushed Guyana’s installed offshore oil production capacity beyond the one-million-barrel-per-day mark after starting up its fifth floating production unit in the country’s prolific Stabroek block. The US energy giant began production at the Uaru development on November 16, lifting total installed capacity across the block to approximately 1.1m barrels per day.
- Tue 17 Nov | Trend News Agency | ExxonMobil launches production at fifth oil development offshore Guyana
  https://www.trend.az/world/us/4247262.html
  > BAKU, Azerbaijan, November 17. ExxonMobil Guyana has commenced production at the Uaru development in the offshore Stabroek block, marking the country's fifth oil development and increasing its installed production capacity to 1.1 million barrels per day, the company said on November 16.
- Tue 17 Nov | Yahoo Finance | ExxonMobil's Uaru Startup Lifts Guyana Oil Capacity to 1.1 Million Bpd
  https://finance.yahoo.com/energy/articles/exxonmobils-uaru-startup-lifts-guyana-064000242.html
- Tue 17 Nov | Upstream Online | Saipem secures approval for ExxonMobil’s Guyana deepwater project
  https://www.upstreamonline.com/field-development/saipem-secures-approval-for-exxonmobil-s-guyana-deepwater-project/2-1-2075057
- Tue 17 Nov | www.marketscreener.com | MODEC : ExxonMobil and MODEC celebrate First Oil milestone of FPSO Errea Wittu
  https://www.marketscreener.com/news/modec-exxonmobil-and-modec-celebrate-first-oil-milestone-of-fpso-errea-wittu-ce785edfde8af120
- Tue 17 Nov | JPT Homepage | ExxonMobil Declares FID on Longtail Deepwater Gas Project Offshore Guyana
  https://jpt.spe.org/exxonmobil-declares-fid-on-longtail-deepwater-gas-project-offshore-guyana
## AVGO  (8 leads)
- Tue 17 Nov | Gotrade | Broadcom Stock (AVGO) Falls 3.9% on Tighter US Chip Rules (Nov 16)
  https://www.heygotrade.com/en/news/broadcom-avgo-stock-news-november-17-2026/
  > AI-powered contentSome parts of this article are powered by AI. Broadcom (AVGO) fell 3.92% to $333.40 on Monday, November 16, 2026, 1.43 percentage points steeper than the Nasdaq Composite.
- Tue 17 Nov | Yahoo Finance | Anthropic IPO Overvalued? Hardly. Valuation Is “About Where Broadcom and AMD Trade,” Says Scott Galloway
  https://finance.yahoo.com/markets/stocks/articles/anthropic-ipo-overvalued-hardly-valuation-013234576.html
  > - At $1.5 trillion, Anthropic's IPO would value the AI lab at about 19x its $81 billion revenue run rate. Scott Galloway says that's about where Broadcom and AMD trade. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Tue 17 Nov | Yahoo Finance | Why Broadcom Stock Got Mashed on Monday
  https://news.google.com/rss/articles/CBMimgFBVV95cUxQNWw0c1BIbVJKeHpucmlwVEVGWENpeDZxOGh6SnpkNHNsVk15S2k0NTZ2UW9YRWJYbF9NTkdpNjdyTk4xMUVVNXZFNUdZYVZxTDJjdm5nV3lOTzlnRTZPMGJIa3F4MlVwcnQtcGFIUTJ4MkxCM0Fab1JzcnQtYmRUbGp0VjJ4dFkyUER
  > Broadcom (NASDAQ:AVGO) is one of the tech hardware manufacturers spearheading the artificial intelligence (AI) revolution, but you wouldn't know that from its stock's performance on Monday.
- Mon 16 Nov | Yahoo Finance | Broadcom Is “the Best Play” on Nvidia’s CEO Exit, One Investor Argues. The Reason Is China
  https://finance.yahoo.com/markets/stocks/articles/broadcom-best-play-nvidia-ceo-231259559.html
  > - Broadcom (AVGO) surged 5.5% on November 12 following NVIDIA (NVDA) CEO Jensen Huang's departure, before retreating to $333.40 on November 16. - Advanced Micro Devices (AMD) also rallied, while Alphabet (GOOG) provides Broadcom with exposure to Google's custom AI chips through a supply agreement extending up to 2031.
- Mon 16 Nov | Kalkine Media | Broadcom (NASDAQ:AVGO) Rides Custom AI Chip Demand. What’s Next?
  https://kalkinemedia.com/us/stocks/technology/broadcom-nasdaqavgo-rides-custom-ai-chip-demand-whats-next
- Mon 16 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Falls 4% After Analyst Downgrade
  https://news.google.com/rss/articles/CBMiugFBVV95cUxOaDh4YjBOT19SWXl5NVR2YmpreHNTQWg2YWVtTzBFc0UwNG5HS00ycG1mdEFHNlR0dEJJT0kyYXhtTW9FLXhzR1NGeTZwN1dXV3VpaTc0bEZoRVRPV3N2bHBJcHhjMWpXSk5rOTk4ZnRLOGR6Y3U5ejJxUFJqYVJISkR0VXZaQXoyTDB
- Mon 16 Nov | TipRanks | Appaloosa exits stakes in AMD, Broadcom, boosts positions in Micron, Nvidia
  https://news.google.com/rss/articles/CBMivwFBVV95cUxQdHRXTjRaUHJXV0hvX2l4YkRleWFxODJicVBzX3RzQmFLOERNODZCZnVPVXprbW1uVnA2LWg5MXBNWDNtRzdHYTdVZXRzRUM0Z2Q5b0xkMTlldzFDWk5jaUZiVkU0WkVWcWl6d2pNaURYM3l6SlhhenU4M1dRMC1uVWd0eE1TSDU1RF9
- Mon 16 Nov | Yahoo Finance | AMD, Broadcom stocks sink on tighter US chip rules, CoreWeave and Nebius shares drop
  https://news.google.com/rss/articles/CBMiygFBVV95cUxOVmRVNUZveFlyMzN1YXlaNndmR0QzaGFwNjR5X1FVS2hXa21zV2VxWVJCQ09KNC1ib2c4QTZ1djNDMlE4Qm42S3U5Zk9YRGZYR3NVV3lZM1hJNVRDRjBsUldMNDRLNWZTRmd4TThDWFRDWGZxT0hUSDM1Rlp3VVZZamNkX2FsdE1YWFN
## BRK.B  (8 leads)
- Tue 17 Nov | Aktualita.co | Warren Buffett Donates US$5.5 Billion, Shares Important Message Amidst New Era for Berkshire Hathaway
  https://aktualita.co/en/economy/warren-buffett-donates-us55-billion-shares-important-message-amidst-new-era-for-berkshire-hathaway
  > OMAHA, Aktualita.co - Warren Buffett is back in the spotlight after announcing a charitable donation worth approximately US$5.5 billion. The 96-year-old legendary investor also shared a message regarding kindness, gratitude, and the importance of sharing wealth amidst major leadership changes at Berkshire Hathaway. [Figures on the page: nine months; one quarter; attributable to shareholders. Check which one each figure is.]
- Tue 17 Nov | citybiz | Berkshire Hathaway Nearly Doubles Lennar Stake as Greg Abel Expands U.S. Housing Investments
  https://www.citybiz.co/article/934405/berkshire-hathaway-nearly-doubles-lennar-stake-as-greg-abel-expands-u-s-housing-investments/
  > Berkshire Hathaway significantly increased its investment in homebuilder Lennar Corporation, nearly doubling its stake during the third quarter of 2026 as the conglomerate expands its exposure to the U.S. housing market under Chief Executive Greg Abel.
- Tue 17 Nov | The Korea Daily | Warren Buffett donation — Another $5.5B Given to Charity
  https://en.koreadaily.com/warren-buffett-donation/
  (page: did not load (URLError))
## WMT  (8 leads)
- Tue 17 Nov | Intellectia AI | Walmart Set to Report Q3 Earnings Amid Growth Expectations
  https://intellectia.ai/news/stock/walmart-set-to-report-q3-earnings-amid-growth-expectations
  (page: did not load (403))
- Tue 17 Nov | Investing.com | Safe haven or bubble? Walmart and Costco now trade at 45x–53x P/E
  https://www.investing.com/news/stock-market-news/safe-haven-or-bubble-walmart-and-costco-now-trade-at-45x53x-pe-5029122
  (page: did not load (403))
- Tue 17 Nov | CryptoRank | Walmart xStock Exchanges WMTX Markets | Buy & Sell & Trade
  https://cryptorank.io/price/walmart-tokenized-stock-xstock/exchanges
  (page: did not load (403))
## V  (8 leads)
- Tue 17 Nov | CryptoRank | Wrapped Visa Tokenized Stock (xStock): Funding, Investors, Team and Key Events
  https://cryptorank.io/price/wrapped-visa-tokenized-stock-xstock
  (page: did not load (403))
- Tue 17 Nov | Seeking Alpha | Visa, Mastercard seek to end 21-year merchant dispute with $38B deal - report (V:NYSE)
  https://seekingalpha.com/news/4673436-visa-mastercard-seek-to-end-21-year-merchant-dispute-with-38b-deal---report
  (page: did not load (403))
- Tue 17 Nov | The Daily Pennsylvanian | Federal judge throws out Trump proposal limiting foreign student visa lengths
  https://www.thedp.com/article/2026/11/penn-international-student-final-rule-visa-enrollment
  > A federal court struck down a Trump administration rule that would have placed significant restrictions on the number of years international students could lawfully study in the United States on Monday.
## ORCL  (8 leads)
- Tue 17 Nov | Startup Fortune | Oracle stock slides again as its debt-funded AI buildout becomes the market's stress test
  https://startupfortune.com/oracle-stock-slides-again-as-its-debt-funded-ai-buildout-becomes-the-markets-stress-test/
  > Oracle has sold stock and borrowed billions to pay for AI data centers, so every wobble in the AI trade hits its shares first. If you own anything tied to AI spending, this is the stock that shows how nervous the market is.
- Mon 16 Nov | TradingView | Apaloosa adds Oracle, exits Advanced Micro, raises stake in NVIDIA, cuts in Alphabet among Q3 moves
  https://www.tradingview.com/news/seekingalpha:c26ae599e094b:0-apaloosa-adds-oracle-exits-advanced-micro-raises-stake-in-nvidia-cuts-in-alphabet-among-q3-moves/
  > Apaloosa adds Oracle, exits Advanced Micro, raises stake in NVIDIA, cuts in Alphabet among Q3 moves Appaloosa took a new position in Oracle ORCL and exited Advanced Micro Devices AMD, while raising stake in NVIDIA NVDA and reducing holdings in Alphabet GOOG GOOGL, according to its latest 13F filing.
- Mon 16 Nov | Seeking Alpha | Appaloosa adds Oracle, exits Advanced Micro, raises stake in NVIDIA, cuts in Alphabet among Q3 moves
  https://seekingalpha.com/news/4673369-appaloosa-adds-oracle-exits-advanced-micro-raises-stake-in-nvidia-cuts-in-alphabet-among-q3-moves
  (page: did not load (403))
- Mon 16 Nov | GuruFocus | Oracle Corp (ORCL) Stock Down 5.0% -- Now Undervalued? GF Score: 89/100
  https://www.gurufocus.com/news/9202777/oracle-corp-orcl-stock-down-50-now-undervalued-gf-score-89100
  (page: did not load (403))
- Mon 16 Nov | CryptoRank | Wrapped Oracle Tokenized stock (xStock): Funding, Investors, Team and Key Events
  https://cryptorank.io/price/wrapped-oracle-tokenized-stock-xstock
- Mon 16 Nov | MarketBeat | Oracle (NYSE:ORCL) Stock Falls 5.1% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-stock-falls-51-heres-why-2026-11-16/
- Mon 16 Nov | Yahoo Finance | Here's Why Oracle (ORCL) Fell More Than Broader Market
  https://finance.yahoo.com/markets/stocks/articles/heres-why-oracle-orcl-fell-214503903.html
- Mon 16 Nov | MarketWatch | Oracle Corp. stock underperforms Monday when compared to competitors
  https://www.marketwatch.com/data-news/oracle-corp-stock-underperforms-monday-when-compared-to-competitors-e90c5b81-1e8402f4183f
## COST  (8 leads)
- Tue 17 Nov | Investing.com | Safe haven or bubble? Walmart and Costco now trade at 45x–53x P/E
  https://www.investing.com/news/stock-market-news/safe-haven-or-bubble-walmart-and-costco-now-trade-at-45x53x-pe-5029122
  (page: did not load (403))
- Tue 17 Nov | Investing.com India | Stifel initiates Costco stock with buy rating on membership growth By Investing.com
  https://in.investing.com/news/stock-market-news/stifel-initiates-costco-stock-with-buy-rating-on-membership-growth-93CH-5708736
  (page: did not load (403))
- Tue 17 Nov | Yahoo Finance | Costco Just Gained 13% in a Month. What Will It Take to Hit $1,200?
  https://finance.yahoo.com/markets/stocks/articles/costco-just-gained-13-month-041257095.html
  > - Costco stock gained 12.6% in the past month to a record close after strong October sales and a $30-a-share special dividend. - Investors now pay about 49x forward earnings, against a five-year average of 43x.
## NFLX  (8 leads)
- Tue 17 Nov | The Mirror | Netflix viewers are stuck to seats for six hours binging 'must-watch' crime drama
  https://www.mirror.co.uk/tv/tv-news/netflix-viewers-stuck-seats-six-37870322
  > Netflix viewers are stuck to seats for six hours binging 'must-watch' crime drama A Netflix crime drama has had viewers stuck to their seats for six hours straight. The show, which can be viewed on Netflix, has been hailed as nothing short of exceptional by fans.
- Tue 17 Nov | Stocktwits | NFLX Stock Edges Higher Overnight: Evercore Swaps Netflix For Spotify On Top Picks List
  https://news.google.com/rss/articles/CBMi5AFBVV95cUxNSWxDeEZpVjZzNWZrTkhrelhnNmVzdmMzSDlDQzM1UGV3VmpqQml5dXhlVXhua0xkU0pFVGJudUh2dGRUaEo1TFBMRE01RDlVY3NCbXVwSWxtcVlxVzl5a3JJVEZoVl9sQTdMU2FERkYxUWdFZExRdVZCaDMzSFZuTlVfWnkxRXIwOG1
  > (NFLX) shares edged marginally higher overnight, reversing a decline of over 2% at close, even as experts took opposing stances on the company. Evercore ISI removed Netflix from its top picks stocks list and replaced it with Spotify Technology (SPOT) as its third-ranked large-cap recommendation, according to a report from Investing.com.
- Tue 17 Nov | Yahoo Finance | Bill Ackman Adds More To Netflix In Q3; Exits Hertz, Cuts Microsoft
  https://finance.yahoo.com/markets/stocks/articles/bill-ackman-adds-more-netflix-000807017.html
  > - The firm reported a new stake of roughly 6.6 million shares in Intercontinental Exchange valued at about $1.01 billion. - Ackman's firm also increased its Netflix holdings to about 15.4 million shares, up from 13.08 million shares in the prior quarter.
- Mon 16 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Shares Down 2.3% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-shares-down-23-heres-why-2026-11-16/
  > Netflix (NASDAQ:NFLX) Shares Down 2.3% - Here's Why - Netflix shares fell 2.3% to $60.75 in Monday mid-day trading, with trading volume 16% below its daily average. - Analysts maintain a Moderate Buy consensus and an average price target of $89.14, though some firms recently lowered their targets.
- Mon 16 Nov | Kalkine Media | What Is Driving Fresh Interest in Netflix (NASDAQ:NFLX) Right Now?
  https://news.google.com/rss/articles/CBMisAFBVV95cUxQcmFHTWt2eUNFc3BxUi1qeUdQdjJJWkg3ZVhSYkNYbDNNTS1XdDhfcTRwcVIzWWYzTFpDUDk0a0hxX0tTWXJQS2VCVG4zeWhDckxZWEtJeG9uU2lueVdjRDBoLWJ1R3hwRmtyTFdiZHlRRkowbVJwX0l0cW9NZmoyZVVhRXRqT2wxT0l
- Mon 16 Nov | Investor's Business Daily | Netflix (NFLX) Stock Quotes, Company News And Chart Analysis
  https://www.investors.com/news/technology/netflix-nflx-stock-quotes-company-news-and-chart-analysis/
- Mon 16 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Reaches New 12-Month Low - Here's Why
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-reaches-new-12-month-low-heres-why-2026-11-16/
- Mon 16 Nov | The Globe and Mail | Netflix Stock Now Trades at a 70% Discount to Its Peak Valuation, and One Number Is to Blame
  https://www.theglobeandmail.com/investing/markets/stocks/NVDA/pressreleases/8857715/netflix-stock-now-trades-at-a-70-discount-to-its-peak-valuation-and-one-number-is-to-blame/
## INTC  (8 leads)
- Tue 17 Nov | Electronics For You BUSINESS | Shareholders Sue Intel After Stock Plunges 29%
  https://www.electronicsforyou.biz/industry-buzz/shareholders-sue-intel-after-stock-plunges-29/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | Tech Times | Intel Shareholders Sue CEO, CFO After 28.6 Percent Stock Crash In One Day—PC Sales Dipping?
  https://www.techtimes.com/articles/330896/20261117/intel-shareholders-sue-ceo-cfo-after-286-percent-stock-crash-one-day-pc-sales-dipping.htm
  > One of America's most storied semiconductor companies, Intel, is now dealing with legal fallout from one of its worst stock-market days in decades. group of shareholders has taken direct aim at the executives who steered Intel through what they are calling a deliberate concealment of bad news. Intel Shareholders Sue CEO, CFO After Stock Crash [Figures on the page: first half; one quarter. Check which one each figure is.]
- Tue 17 Nov | India Today | Explained: What led to Intel's 29% stock plunge and why shareholders are suing
  https://www.indiatoday.in/business/story/explained-what-led-to-intels-29-stock-plunge-and-why-shareholders-are-suing-3040496-2026-11-17
  > Explained: What led to Intel's 29% stock plunge and why shareholders are suing Intel lost nearly $140 billion in market value in a single trading session in October. Now, investors allege that Intel failed to disclose the extent of its PC business troubles even as it raised $23 billion through a share sale.
- Tue 17 Nov | MLQ.ai | Nvidia cut its Intel stake by a quarter and sold more than half its Nokia shares while adding SpaceX, 13F shows
  https://mlq.ai/news/nvidia-cut-its-intel-stake-by-a-quarter-and-sold-more-than-half-its-nokia-shares-while-adding-spacex-13f-shows/
  (page: did not load (403))
- Tue 17 Nov | BigGo Finance | Nvidia's Q3 U.S. Stock Holdings Fall to NT$1.6 Trillion; Intel Stake Cut 25%, SpaceX Becomes Largest Holding
  https://finance.biggo.com/news/b0ec2b1a-da12-4c48-aab2-5cea81be3099
- Tue 17 Nov | Yahoo Finance | SPCX Stock Dethrones Intel As Nvidia’s Biggest Holding — Druckenmiller Buys In And Tepper Ups His Stake Over 1,600%
  https://finance.yahoo.com/markets/stocks/articles/spcx-stock-dethrones-intel-nvidia-034550014.html
- Tue 17 Nov | TradingKey | Intel Tumbles 7% to Retest $50 Level, Risking 60% Plunge If Support Breaks
  https://www.tradingkey.com/analysis/stocks/us-stocks/262308170-stock-intel-intc-price-50-ai-idm-tradingkey
- Tue 17 Nov | FXLeaders | Can $50 Support Hold or Break Down as Intel Gets Sued by Shareholders after 29% Stock Plunge?
  https://www.fxleaders.com/news/2026/11/16/can-support-or-break-down-as-intel-gets-sued-by-shareholders-after-29-stock-plunge/
## LLY  (8 leads)
- Tue 17 Nov | ad-hoc-news.de | Nov. 12 China approval: Eli Lilly and Co. stock slips 1.82% to EUR 1,296.20
  https://www.ad-hoc-news.de/boerse/news/vorboerse/nov-12-china-approval-eli-lilly-and-co-stock-slips-1-82-to-eur-1-296-20/70525136
  > Eli Lilly and Co. stock traded at EUR 1,296.20 on Lang & Schwarz at 07:53 CET on Tuesday, November 17, 2026, 1.82 percent below the Xetra close of Monday, November 16, 2026, at EUR 1,320.20. China approved Eli Lilly's oral GLP-1 medicine orforglipron for weight management on November 12, 2026, according to Pharmaphorum.
- Tue 17 Nov | Coinbase | About Eli Lilly & Co Tokenized Stock (Coinbase)
  https://www.coinbase.com/en-ar/price/eli-lilly--co-base-0xb200000000000000000000f1a0f91e34892e4718
  (page: only 48 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | Kalkine Media | What Obesity Data Is Eli Lilly (NYSE:LLY) Presenting at ObesityWeek?
  https://kalkinemedia.com/us/stocks/healthcare/what-obesity-data-is-eli-lilly-nyselly-presenting-at-obesityweek
  > - Lilly presents new obesity portfolio data at ObesityWeek - Clinical, patient-reported and real-world results shared
Read 81 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, EMFD, SKPC, AMZN.
