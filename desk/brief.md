# Desk brief, Thursday, November 19, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 65s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-18 (24.56); Treasury yields to 2026-11-18 (10-year 5.07%).
- **valuation**: ok in 23s (GitHub Actions). LLY: $1.33tn, P/E (last 12 months) 43.3, Forecast P/E (fiscal 2026) 38.7 (the four quarters to Sep 2026)
- **movers**: ok in 21s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-02 XOM results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 turning down, RSI 50.3
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.0%, median P/E 10.1; cheapest MASR +74%, ABUK +49%, PHAR +48%; dearest ARAB -61%, MOIN -64%, BTFH -68%
- **views**: ok in 0s (GitHub Actions). Views: nothing to change.
- **results**: ok in 53s (GitHub Actions). 
- **news**: ok in 151s (GitHub Actions). 
- **leads**: ok in 71s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 1 failed, 22 needed a retry (stock_news.py).

## What moved (latest close against the one before)
- EGX30 51,544.80 (-0.26%); EGX70 EWI 17,564.30 (-0.16%); USD/EGP 53.79 (-0.01%); Gold 21K 5,750.00 (-2.54%); Brent 91.95 (-1.28%); S&P 500 7,323.63 (-0.23%); Nasdaq 24,429.89 (+0.42%); Bitcoin 63,556.00 (-1.45%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): HRHO +5.0%, XOM -4.0%, AMZN +3.8%, AVGO +3.6%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - B: In an uptrend: above its 50-day average, which is above the 200-day; RSI 61, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - COST: In an uptrend: above its 50-day average, which is above the 200-day; RSI 69, neither stretched nor washed out; the 50-day average crossed above the 200-day today.
    - INTC: Turning down: below both its 50-day average (40.7% under) and its 200-day (37.5% under), though the 50-day is still above the 200-day; RSI 29, washed out: below 30; momentum turned up today (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (28.2% under) and its 200-day (25.9% under), though the 50-day is still above the 200-day; RSI 21, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- EGX MENA (Mena Touristic Investment) +14.4%; EGX INEG (Integrated Engineering Group) +9.9%; EGX ADRI (Arab Development & Real Estate Investment) +7.1%; EGX KWIN (El Kahera El Watania Investment) +6.1%; EGX HBCO (Heibco for Commercial Investments & Real Estate Development) +5.9%; EGX AMES (Alexandria New Medical Center) -10.2%; EGX UNIT (United Housing Construction SA) -6.7%; US OKTA (Okta) +12.1%; US SAIL (SailPoint) +10.3%; US PANW (Palo Alto Networks) +9.9%; US GNRC (Generac Holdings) +9.9%; US RBRK (Rubrik) +9.3%; US HUM (Humana) -13.0%; US UNH (UnitedHealth Group Incorporated) -10.2%; US CBRS (Cerebras Systems) -9.6%; US ELV (Elevance Health) -7.6%; US DINO (HF Sinclair) -7.2%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-18 (TradingView's closes; Mubasher's list refused), 195 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (212)
US: 2026-11-18, 822 companies
US week and month: US companies worth $10bn or more (820)
EGX30 heatmap: 2026-11-18, 31 members
US heatmap: 2026-11-18, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-18
## MENA +14.4%  Mena Touristic Investment
- no headlines found
## INEG +9.9%  Integrated Engineering Group
- no headlines found
## ADRI +7.1%  Arab Development & Real Estate Investment
- no headlines found
## KWIN +6.1%  El Kahera El Watania Investment
- no headlines found
## HBCO +5.9%  Heibco for Commercial Investments & Real Estate Development
- no headlines found
## AMES -10.2%  Alexandria New Medical Center
- no headlines found
## UNIT -6.7%  United Housing Construction SA
- no headlines found
## AMII -4.5%  Arabian Metal Industries and Industrial Investments
- no headlines found
## FTNS -3.9%  Fitness Prime
- no headlines found
## GPIM -3.7%  GPI For Urban Growth
- no headlines found

# US 2026-11-18
## OKTA +12.1%  Okta
- Thu 19 Nov | Insider Monkey | Okta (OKTA) Is Turning Heads. Here’s What’s Happening
  https://www.insidermonkey.com/news/okta-okta-is-turning-heads-heres-whats-happening-1867284/
- Thu 19 Nov | Yahoo Finance | Okta (OKTA) Is Turning Heads. Here’s What’s Happening
  https://finance.yahoo.com/markets/stocks/articles/okta-okta-turning-heads-happening-035406782.html
  > (NASDAQ:OKTA) is one of the 10 Stocks Investors Are Rushing to Buy. Okta bounced back 12.07 percent on Wednesday to finish at $195.61 apiece, as investors gobbled up shares in cybersecurity stocks, helped by Palo Alto Networks' strong earnings performance.
- Wed 18 Nov | Global Banking & Finance Review | Okta rises 12.11% in Wednesday's session
  https://www.globalbankingandfinance.com/okta-okta-rises-2026-11-18/
- Wed 18 Nov | Benzinga | Okta Stock Rallies Amid Concerns Over Digital Infrastructure Vulnerability
  https://www.benzinga.com/trading-ideas/movers/26/11/63407584/okta-stock-rallies-amid-concerns-over-digital-infrastructure-vulnerability
  (page: did not load (403))
## SAIL +10.3%  SailPoint
- Thu 19 Nov | Insider Monkey | SailPoint (SAIL) Is Suddenly on Investors’ Radar. Here’s Why
  https://www.insidermonkey.com/news/sailpoint-sail-is-suddenly-on-investors-radar-heres-why-1867280/?amp=1
- Thu 19 Nov | Yahoo Finance | SailPoint (SAIL) Is Suddenly on Investors’ Radar. Here’s Why
  https://finance.yahoo.com/markets/stocks/articles/sailpoint-sail-suddenly-investors-radar-034916685.html
  > (NASDAQ:SAIL) is one of the 10 Stocks Investors Are Rushing to Buy.
- Wed 18 Nov | marketscreener.com | 1Kosmos Partners With SailPoint Technology Holdings, Inc. To Secure Workforce Onboarding
  https://www.marketscreener.com/news/1kosmos-partners-with-sailpoint-technology-holdings-inc-to-secure-workforce-onboarding-ce785edddd8af020
  (page: did not load (403))
- Wed 18 Nov | Yahoo Finance | 1Kosmos Partners with SailPoint to Secure Workforce Onboarding
  https://finance.yahoo.com/technology/ai/articles/1kosmos-partners-sailpoint-secure-workforce-140400081.html
  > Integration helps reduce hiring fraud, service desk attacks and password reset abuse by verifying identity before provisioning is approved
## PANW +9.9%  Palo Alto Networks
- Thu 19 Nov | KuCoin | Palo Alto Networks to Acquire Applied Compute for $4.5 Billion to Enhance AI Infrastructure
  https://www.kucoin.com/news/flash/palo-alto-networks-to-acquire-applied-compute-for-4-5-billion-to-boost-ai-infrastructure
  > - Palo Alto Networks has agreed to acquire Applied Compute. - Palo Alto's quarterly revenue increased 39% to $3.44 billion. - This transaction will enable Palo Alto Networks to integrate cybersecurity with AI model development, deployment, and infrastructure services.
- Thu 19 Nov | Benzinga | Palo Alto Sees Rising Cyber Budgets Amid AI Threats As Firms Tap ‘Emergency Funds’; CEO Nikesh Arora Says
  https://www.benzinga.com/markets/earnings/26/11/63418481/palo-alto-sees-rising-cyber-budgets-amid-ai-threats-as-firms-tap-emergency-funds-ceo-nikesh-arora-says-applied-compute-bet-could-dwarf-cybersecurity-business
  (page: did not load (403))
- Thu 19 Nov | Investing.com | RBC Capital reiterates Palo Alto Networks stock rating at Outperform
  https://www.investing.com/news/analyst-ratings/rbc-capital-reiterates-palo-alto-networks-stock-rating-at-outperform-93CH-5037891
  (page: did not load (403))
- Thu 19 Nov | TradingKey | Palo Alto Surges 9% on Earnings, $4.5 Billion Applied Compute Deal as Stock Eyes $400 Mark
  https://www.tradingkey.com/analysis/stocks/us-stocks/262312539-palo-alto-surges-earnings-4-5b-applied-compute-test-400-panw-tradingkey
  > Palo Alto Surges 9% on Earnings, $4.5 Billion Applied Compute Deal as Stock Eyes $400 Mark Palo Alto Networks reported strong quarterly results, with revenue up 39% year over year to $3.44 billion and adjusted EPS of $1.05, driven by surging cybersecurity demand and platform consolidation.
## GNRC +9.9%  Generac Holdings
- Thu 19 Nov | Simply Wall St | Generac Stock Gets A Lift From Top Solar Award Recognition
  https://simplywall.st/stocks/us/capital-goods/nyse-gnrc/generac-holdings/news/generac-stock-gets-a-lift-from-top-solar-award-recognition
  > Generac Holdings reported that its PWRmicro microinverter was selected as a Best in Show winner in the residential category of the 2026 Solar Power World Top Products Awards, recognizing the product’s fit with larger, higher output solar panels.
- Thu 19 Nov | GuruFocus | Generac Holdings Inc (GNRC) Stock Up 9.9% but GF Value Says Over
  https://www.gurufocus.com/news/9208745/generac-holdings-inc-gnrc-stock-up-99-but-gf-value-says-overvalued-gf-score-89100
  (page: did not load (403))
- Wed 18 Nov | MarketWatch | Generac Holdings Inc. stock outperforms competitors on strong trading day
  https://www.marketwatch.com/data-news/generac-holdings-inc-stock-outperforms-competitors-on-strong-trading-day-a6c7a8ca-95a47fdc016b
  (page: did not load (401))
- Wed 18 Nov | Yahoo! Finance Canada | Generac Holdings Inc. (GNRC) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/GNRC/
  > designs, manufactures, and distributes energy technology products and solutions worldwide.
## RBRK +9.3%  Rubrik
- Thu 19 Nov | Simply Wall St | Rubrik Stock In Focus After Product Expansion Across Cloud And Cyber Recovery
  https://simplywall.st/stocks/us/software/nyse-rbrk/rubrik/news/rubrik-stock-in-focus-after-product-expansion-across-cloud-a
  > Rubrik has rolled out a cluster of new cyber and data resilience products across Microsoft 365, Azure Cosmos DB, Google BigQuery, AWS workloads, DevOps platforms, and on-premise NAS. All of these are centered on its Rubrik Security Cloud platform with capabilities such as immutable backups, configuration rollback, and application-consistent recovery.
- Wed 18 Nov | Quiver Quantitative | Rubrik stock jumps as new Microsoft-focused launches add to cloud security momentum
  https://www.quiverquant.com/news/Rubrik+stock+jumps+as+new+Microsoft-focused+launches+add+to+cloud+security+momentum
  > (RBRK) is up 9.3% today. Here is some analysis on what might have caused this price movement. Analysis: The move appears tied to a fresh set of product announcements centered on Microsoft environments, which likely reinforced investor confidence in Rubrik’s platform expansion and cyber-recovery story.
- Wed 18 Nov | TradingView | Rubrik shares skyrocket, what you need to know
  https://www.tradingview.com/news/stockstory:1a1bd03e3094b:0-rubrik-shares-skyrocket-what-you-need-to-know/
  > Rubrik shares skyrocket, what you need to know Shares of data security software company Rubrik RBRK jumped 6.3% in the morning session after the company announced Configuration Resilience for Microsoft 365 and protection for Microsoft Azure Cosmos DB at Microsoft Ignite.
- Wed 18 Nov | MarketBeat | Rubrik (NYSE:RBRK) Shares Up 6.8% on Analyst Upgrade
  https://www.marketbeat.com/instant-alerts/price-rubrik-nyse-rbrk-shares-up-68-on-analyst-upgrade-2026-11-18/
  > Rubrik (NYSE:RBRK) Shares Up 6.8% on Analyst Upgrade - Rubrik shares rose 6.8% after Cantor Fitzgerald raised its price target from $120 to $125 and maintained an Overweight rating; the stock closed at $107.49.
## HUM -13.0%  Humana
- Thu 19 Nov | Benzinga | Humana (HUM) Stock Trending After Hours as CMS Proposes $90B Medicare Anti-Fraud Rule
  https://www.benzinga.com/markets/equities/26/11/63417422/humana-shares-slip-after-hours-cms-fraud-rule
  (page: did not load (403))
- Thu 19 Nov | TradingView | Humana (HUM) Stock Trending After Hours as CMS Proposes $90B Medicare Anti-Fraud Rule
  https://www.tradingview.com/news/benzinga:9bdf40bc6094b:0-humana-hum-stock-trending-after-hours-as-cms-proposes-90b-medicare-anti-fraud-rule/
  > Humana (HUM) Stock Trending After Hours as CMS Proposes $90B Medicare Anti-Fraud Rule HUM shares are trending on Wednesday night. Shares of the Kentucky-based health insurer slipped 0.46% to $384.00 in after-hours trading. In the regular session, HUM closed at $385.78, down 12.98%, according to Benzinga Pro data.
- Wed 18 Nov | Beinsure | Healthcare stocks (UnitedHealth, Humana, CVS, Cigna) fall on new Medicare rules
  https://beinsure.com/news/healthcare-stocks-fall-as-medicare-rules-trigger-a-selloff/
  > US healthcare insurance stocks extended their losses on November after the Centers for Medicare & Medicaid Services (CMS) proposed stricter oversight of federal healthcare programs, raising concerns about retrospective payment recoveries and future profitability. UnitedHealth Group (NYSE: UNH) and Humana (NYSE: HUM) led the decline.
- Wed 18 Nov | AlphaStreet | Humana Drops 6.4% Amid Sector-Wide Selling
  https://news.alphastreet.com/humana-drops-6-4-amid-sector-wide-selling/
  > AlphaStreet Newsdesk powered by AlphaStreet Intelligence shares tumbled 6.4% on Wednesday to $415.14, caught in a broad sector-wide selloff that dragged down managed care and health insurance stocks across the board.
## UNH -10.2%  UnitedHealth Group Incorporated
- Thu 19 Nov | Kalkine Media | Is UnitedHealth (NYSE:UNH) Executing a Multiyear Plan?
  https://kalkinemedia.com/us/stocks/healthcare/is-unitedhealth-nyseunh-executing-a-multiyear-plan
  > - A refreshed finance team described a staged path to restore the group's standing after a bruising stretch - The plan carried a familiar tension for a company working to steady itself after a difficult run.
- Wed 18 Nov | Yahoo! Finance Canada | What Could UnitedHealth Group (UNH) Face From New CMS Audits And Breakup Pressure?
  https://ca.finance.yahoo.com/news/could-unitedhealth-group-unh-face-210951670.html
  > - UnitedHealth Group (NYSE: UNH) faces a new CMS proposal to tighten Medicare and Medicaid anti-fraud audits and oversight. - The draft CMS rule would expand data reviews of managed care plans, potentially increasing compliance and documentation requirements for UnitedHealth.
- Wed 18 Nov | Quantisnow | UnitedHealth, Humana and Elevance fall sharply after Medicare audit proposal
  https://www.quantisnow.com/articles/cms-audit-proposal-drives-humana-unitedhealth-and-elevance-lower-as-s-p-500-edges-up
  (page: did not load (403))
- Wed 18 Nov | Seeking Alpha | UnitedHealth Group retreats 8% amid proposed Medicare fraud rule (UNH:NYSE)
  https://seekingalpha.com/news/4674301-unitedhealth-group-retreats-8-amid-proposed-medicare-fraud-rule
  > UnitedHealth Group (UNH) shares shed just over 8% on Wednesday, falling alongside the overall managed care sector after news broke earlier this week of a proposed rule that raised regulatory concerns for managed-care companies. The health-benefits provider was down $32.79 at $356.89 in midday
## CBRS -9.6%  Cerebras Systems
- Thu 19 Nov | Stock Titan | After a $77.9M September sale, a Cerebras Systems (CBRS) officer proposes selling more shares.
  https://www.stocktitan.net/sec-filings/CBRS/144-cerebras-systems-inc-sec-filing-7adb8e0b878d.html
  > Cerebras Systems' Mallick proposes $1.77M share sale Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Thu 19 Nov | Stock Titan | An officer received 52,058 Cerebras Systems (CBRS) shares from a stock award and proposes a sale.
  https://www.stocktitan.net/sec-filings/CBRS/144-cerebras-systems-inc-sec-filing-23c182884f19.html
  > Cerebras Systems officer proposes $2.93M share sale Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Wed 18 Nov | MarketBeat | Top Cerebras Systems (CBRS) Competitors 2026
  https://www.marketbeat.com/stocks/NASDAQ/CBRS/competitors-and-alternatives/
  (page: did not load (403))
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: NVDA, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-19 CLHO results (expected)
- 2026-11-19 EAST results (expected)  <- write its preview
- 2026-11-19 EFID results (expected)
- 2026-11-19 EFIH results (expected)  <- write its preview
- 2026-11-19 HRHO results (expected)
- 2026-11-19 JUFO results (expected)
- 2026-11-19 MSFT dividend
- 2026-11-19 PHDC results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
- due 2026-11-20: Brent stays below $105 while Iran talks continue (on track)
    Views: nothing to change.

## Fair value
- Changed since the last run: CSAG +22% -> +35% (medium -> medium); LCSW -44% -> -41% (low -> medium); TALM new at -44%.
- In the ten cheapest or dearest with no note: MCQE, ADIB, CSAG, EMFD, SCEM, AMOC, LCSW, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-19. Open each story before using it.
## COMI  (8 leads)
- Wed 18 Nov | https://www.youlyou.com/ | 10 شركات تقود أرباح البورصة المصرية في 9 أشهر.. التجاري الدولي في الصدارة وأبو قير الأسرع نموا والمصرية للاتصالات تسجل 24.4 مليار جنيه
  https://www.youlyou.com/97542
  > كشفت نتائج أعمال الشركات المقيدة بالبورصة المصرية عن تفاوت واضح في خريطة الربحية خلال التسعة أشهر الأولى من عام 2026، مع تصدر القطاع المصرفي قائمة الشركات الأعلى تحقيقًا لصافي الأرباح، بالتوازي مع حضور قوي لقطاعات الاتصالات والأسمدة والصناعات الكهربائية والعقارات. [Figures on the page: standalone; consolidated; unaudited or preliminary; nine months. Check which one each figure is.]
- Wed 18 Nov | بنكي | بقيمة 366.06 مليون جنيه.. البنك التجاري الدولي CIB يواصل الهيمنة على تداولات القطاع بنسبة 61.6% بنهاية جلسة الأربعاء
  https://www.bankygate.com/202762
  > واصل سهم البنك التجاري الدولي – مصر CIB تصدره لقائمة الأسهم الأكثر نشاطًا بقطاع البنوك المقيدة بالبورصة المصرية بنهاية تعاملات جلسة الأربعاء 18 نوفمبر 2026، بعدما استحوذ على 61.6% من إجمالي قيمة تداولات القطاع، في تأكيد جديد على مكانته كأكبر الأسهم المصرفية جذبًا للسيولة داخل السوق.
- Wed 18 Nov | عالم المال | تباين أداء أسهم البنوك بالبورصة.. التجاري الدولي يتصدر التداولات بـ366 مليون جنيه
  https://alamalmal.net/article/943631/تباين-أداء-أسهم-البنوك-بالبورصة-التجاري-الدولي
  > شهد قطاع البنوك بالبورصة المصرية أداءً متبايناً بختام تعاملات جلسة اليوم، مع ميل أغلب الأسهم إلى التراجع، وسط اختلاف تحركات الأسهم بين الارتفاع والانخفاض، فيما تصدر البنك التجاري الدولي قائمة الأسهم الأعلى تداولاً من حيث القيمة.
## TMGH  (8 leads)
- Wed 18 Nov | شبكة تواصل الإخبارية | 18.8 مليار دولار مستهدفات مبيعات طلعت مصطفى في العراق
  https://twaslnews1.twaslnews.com/7916253/
  (page: did not load (403))
- Wed 18 Nov | https://www.youlyou.com/ | طلعت مصطفى تفتح جبهة استثمارية جديدة في العراق.. مدينة عمرانية بـ43 ألف وحدة ومبيعات مستهدفة 18.8 مليار دولار
  https://www.youlyou.com/97501
  > - مشروع طلعت مصطفى في بغداد يمتد على 12.8 مليون متر مربع ويضم 43 ألف وحدة سكنية. - المبيعات التراكمية المستهدفة تصل إلى 18.8 مليار دولار. - المشروع يستهدف إيرادات سنوية متكررة بقيمة 108 ملايين دولار عند اكتماله.
- Wed 18 Nov | صحيفة اخبارنا | استثمارات طلعت مصطفى القابضة في العراق تستهدف مدينة ببغداد تضم 43 ألف وحدة
  https://www.akhbrna.ae/economy/astthmarat-tlat-mstfa-alqabda-fy/
  > تبحث مجموعة طلعت مصطفى القابضة توسيع استثماراتها في العراق عبر مشروع عمراني متكامل جنوب غرب بغداد، بعد حصول شركتها التابعة «طلعت مصطفى بغداد» على إجازة استثمار لتطوير المشروع الذي يخطط لأن يضم نحو 43 ألف وحدة سكنية.
## ETEL  (8 leads)
- Thu 19 Nov | تحيا مصر | تامر المهدي: المصرية للاتصالات تنفذ بنية تكنولوجية متطورة بمشروع نيفيرا
  https://www.tahiamasr.com/1107431
  (page: did not load (403))
- Thu 19 Nov | إقرأ نيوز | المصرية للاتصالات: التكنولوجيا تسهِّل حياة سكان «نيفيرا» وتساعد المستثمرين
  https://www.iqraa.news/236209/المصرية-للاتصالات-التكنولوجيا-تسهِّ/
  > قال المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، إن الشركة ستعمل مع كل مستثمر في مشروع «نيفيرا» منذ مرحلة التصميم لاختيار الحلول التكنولوجية التي تتناسب مع احتياجاته وطبيعة نشاطه.
- Thu 19 Nov | إقرأ نيوز | المصرية للاتصالات تبني شبكة ألياف ضوئية تغطي «نيفيرا» بالكامل
  https://www.iqraa.news/236197/المصرية-للاتصالات-تبني-شبكة-ألياف-ضوئ/
  > قال المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، إن الشركة تشارك في مشروع «نيفيرا» بصفتها شريك الاتصالات والتكنولوجيا، وستتولى بناء شبكة ألياف ضوئية تغطي كامل مساحة المدينة، التي تبلغ نحو 36 مليون متر.
## PHDC  (4 leads)
- Wed 18 Nov | بروبرتي بلس | شركة بالم هيلز تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال أول 9 أشهر من 2026.. بمعدل نمو 18%
  https://propertypluseg.com/شركة-بالم-هيلز-تحقق-مبيعات-جديدة-بقيمة-2/
  > قال ياسين منصور، رئيس مجلس الإدارة التنفيذي لشركة بالم هيلز: “شهدت الأشهر التسعة الأولى من عام 2026 مجموعة جديدة من النتائج القوية. فقد ظل الطلب قوياً على مستوى محفظتنا المتنوعة، وواصلت استراتيجيتنا للنمو المنضبط تحقيق ثمارها.
- Wed 18 Nov | صدى العرب | بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://www.sada-elarab.com/827417
  > بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18% أعلنت شركة بالم هيلز للتعمير تحقيق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال التسعة أشهر الأولى من عام 2026، بمعدل نمو 18% مقارنة بالفترة نفسها من العام الماضي، مدعومة باستمرار قوة الطلب على مشروعات الشركة وتنوع محفظتها العقارية.
- Tue 17 Nov | أصول مصر | «بالم هيلز للتعمير» تحقق مبيعات قياسية بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  https://www.osoulmisrmagazine.com/452821
  > «بالم هيلز للتعمير» تحقق مبيعات قياسية بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
## SWDY  (6 leads)
- Thu 19 Nov | أسواق للمعلومات | السويدي الوطنية تستعرض خطة 2027–2028 لزيادة الإنتاج والتوسع في إفريقيا والشرق الأوسط
  https://www.aswaqinformation.com/259688
  > السويدي الوطنية تستعرض خطة 2027–2028 لزيادة الإنتاج والتوسع في إفريقيا والشرق الأوسط إيمان سعيد أسواق للمعلومات
- Wed 18 Nov | جريدة الملتقى الاقتصادي | السويدي الوطنية تخطط للتوسع في 2027 و2028 وتستهدف زيادة إنتاج أنظمة الري المحوري
  https://www.moltakaaliqtisad.online/السويدي-الوطنية-تخطط-للتوسع-في-2027-و2028-وتس/
  > كشفت شركة السويدي الوطنية عن خطة للتوسع والنمو خلال عامي 2027 و2028، تستهدف زيادة الطاقة الإنتاجية وتطوير المنتجات ودخول قطاعات جديدة ذات قيمة مضافة، إلى جانب تعزيز وجودها في أسواق إفريقيا والشرق الأوسط، لمواكبة الطلب المتزايد على أنظمة الري المحوري والمنتجات المعدنية المستخدمة في المشروعات الزراعية والصناعية والبنية التحتية.
- Wed 18 Nov | جريدة المال | السويدي الوطنية تستهدف زيادة إنتاج أنظمة الري المحوري والتوسع بأسواق إفريقيا والشرق الأوسط خلال 2027-2028
  https://almalnews.com/2148326/السويدي-الوطنية-تستهدف-زيادة-إنتاج-أنظمة-الري/
  (same wording as the جريدة الملتقى الاقتصادي story above: one source, not two)
## ORAS  (8 leads)
- Thu 19 Nov | Construction Business News Middle East | Orascom Construction Backlog Climbs To US$11.6 Billion As Nine-Month Profit Nearly Doubles
  https://www.cbnme.com/news/orascom-construction-backlog-climbs-to-us11-6-billion-as-nine-month-profit-nearly-doubles/
  > Orascom Construction has reported a 95.9 per cent rise in net profit for the first nine months of 2026, with revenue up 39.5 per cent and new awards of US$7.1 billion [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | EnterpriseAM | Orascom Construction’s net income doubles in 3Q
  https://enterpriseam.com/uae/2026/11/19/orascom-constructions-net-income-doubles-in-3q/
  > Orascom Construction’s net income attributable to shareholders rose 103% y-o-y to USD 102.7 mn in 3Q 2026, while its revenue climbed 22.5% to USD 1.8 bn, according to the company’s latest earnings release (pdf). Meanwhile, EBITDA increased 56.1% y-o-y to USD 132.1 mn, widening the EBITDA margin to 7.3% from 5.7%. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | EnterpriseAM | EFG Holdings and Orascom Construction report their 3Q earnings
  https://enterpriseam.com/egypt/2026/11/19/efg-holdings-and-orascom-construction-report-their-3q-earnings/
  > Our friends at EFG Holding saw their group revenue rise 5% y-o-y to EGP 6.7 bn in 3Q 2026, according to their latest earnings release (pdf). Net income after tax and minority interest fell 15% y-o-y to EGP 720 mn during the quarter. [Figures on the page: consolidated; nine months; attributable to shareholders. Check which one each figure is.]
## FWRY  (4 leads)
- Wed 18 Nov | أراجيك - Arageek | Fawry تخصص 80 مليون جنيه لاستثمارات التكنولوجيا والأمن السيبراني في الصدارة
  https://www.arageek.com/fawry-تخصص-80-مليون-جنيه-لاستثمارات-التكنولو
  > Fawry تخصص 80 مليون جنيه لاستثمارات التكنولوجيا والأمن السيبراني في الصدارة تخطط شركة التكنولوجيا المالية المصرية Fawry لتخصيص 80 مليون جنيه، أي ما يعادل نحو 1.6 مليون دولار، لاستثمارات التكنولوجيا بحلول نهاية عام 2026، مع إعطاء الأولوية للأمن السيبراني وتطوير بنيتها التحتية الرقمية.
- Tue 17 Nov | CairoScene | Fawry Allocates $1.6 Million for Cybersecurity Investments
  https://cairoscene.com/Business/Fawry-Allocates-1-6-Million-for-Cybersecurity-Investments
  > Fawry Allocates $1.6 Million for Cybersecurity Investments The fintech company is directing LE 80 million towards technology upgrades by the end of 2026. Egyptian fintech company Fawry plans to allocate LE 80 million (approximately $1.6 million) towards technology investments by the end of 2026, prioritising cybersecurity and improvements to its digital infrastructure.
- Tue 17 Nov | كندا نيوز 24 | نظام دفع فوري جديد في كندا.. كيف سيؤثر على الرواتب والتحويلات والشيكات المصرفية؟
  https://canadanews24.ca/نظام-دفع-فوري-جديد-في-كندا-كيف-سيؤثر-عل/
  > أطلقت كندا نظاماً جديداً للمدفوعات الفورية يُعرف باسم Real-Time Rail (RTR)، يتيح تحويل الأموال وتسويتها خلال ثوانٍ بدلاً من أيام، في خطوة تهدف إلى تسريع المعاملات المالية وتسهيل وصول الأفراد والشركات إلى أموالهم. وبهذا الإطلاق، أصبحت كندا آخر دولة ضمن مجموعة السبع (G7) تنشئ شبكة للمدفوعات الفورية.
## ABUK  (8 leads)
- Wed 18 Nov | Solarbytes | AOI signs 3 MW solar plant contract with Abu Qir Fertilizers
  https://solarbytes.info/emea-bytes/aoi-signs-3-mw-solar-plant-contract-with-abu-qir-fertilizers-12820027
  > A contract for solar power plants in Alexandria Governorate has been signed by the Arab Organization for Industrialization (AOI), an Egypt-based industrial organisation, with Abu Qir Fertilizers. Under that contract, AOI will supply and install the second phase of the plants, which are to have a total capacity of about 3 MW.
- Wed 18 Nov | ad-hoc-news.de | Abu Qir Fertilizers stock faces gas cost pressure through year-end
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/abu-qir-fertilizers-stock-faces-gas-cost-pressure-through-year-end/70529207
  > Abu Qir Fertilizers faces higher energy costs after Egypt adjusted the price of natural gas supplied to its plants from November 16 through December 31. The company disclosed the measure on Tuesday, November 17, in response to an inquiry from the Egyptian Exchange, according to Ahram Online.
- Tue 17 Nov | المصري اليوم | بعد أنباء زيادة الغاز بـ50%.. أول تعليق من «أبو قير للأسمدة» بشأن إنتاجها
  https://www.almasryalyoum.com/news/details/4412838
  > بعد أنباء زيادة الغاز بـ50%.. أول تعليق من «أبو قير للأسمدة» بشأن إنتاجها أعلنت شركة أبوقير للأسمدة والصناعات الكيماوية، تلقيها إخطارًا بتعديل سعر الغاز الطبيعي المورد لمصانعها، اعتبارًا من 16 نوفمبر الجاري، وحتى 31 ديسمبر المقبل، وذلك تعليقا على أنباء زيادة سعر الغاز لمصانع الأسمدة بنسبة 50%.
## HRHO  (8 leads)
- Thu 19 Nov | Vietnam.vn | حقيبة هيرميس هي المفضلة لدى ميسي وهالاند.
  https://www.vietnam.vn/ar/chiec-tui-hermes-duoc-long-messi-haaland
  > من ليونيل ميسي وديكلان رايس إلى إيرلينغ هالاند، شوهد العديد من نجوم كرة القدم وهم يحملون حقائب هيرميس الكبيرة، محولين هذه الإكسسوارات الفاخرة إلى جزء لا يتجزأ من أناقتهم خارج الملعب. مع ذلك، فإن العديد من التصاميم التي تحمل اسم "بيركين" هي في الواقع من مجموعة "هوت آ كوروا" (HAC).
- Wed 18 Nov | EnterpriseAM | "إي إف جي القابضة" وأوراسكوم كونستراكشون تعلنان نتائجهما المالية للربع الثالث
  https://enterpriseam.com/egypt-ar/2026/11/19/إي-إف-جي-القابضة-وأوراسكوم-كونستراكش/
  > ارتفعت إيرادات مجموعة "إي إف جي القابضة" بنسبة 5% على أساس سنوي في الربع الثالث من عام 2026 لتصل إلى 6.7 مليار جنيه، وفقا لبيان نتائج أعمالها (بي دي إف). في المقابل، تراجع صافي أرباح المجموعة بعد خصم الضرائب وحقوق الأقلية بنسبة 15% على أساس سنوي إلى 720 مليون جنيه خلال الربع. [Figures on the page: consolidated; one quarter; attributable to shareholders. Check which one each figure is.]
- Wed 18 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | إعمار العقارية تعيّن هيرميس الإمارات مديراً رئيسياً مشاركاً إضافياً لعرض الاستحواذ على إعمار للتطوير
  https://www.argaam.com/ar/article/articledetail/id/1953618
  (page read: it never names the company, so probably not about it: skip)
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
## EFIH  (2 leads)
- Wed 18 Nov | جريدة المال | «الأهلي فاروس» ترفع القيمة العادلة لـ «إي فاينانس» إلى 34.3 جنيه للسهم
  https://almalnews.com/2148141/«الأهلي-فاروس»-ترفع-القيمة-العادلة-لـ-«إي/
  > أصدرت وحدة بحوث «الأهلي فاروس» تقريرًا لشركة «إي فاينانس للاستثمارات المالية والرقمية» رفعت فيه تقديراتها للقيمة العادلة للسهم إلى 34.3 جنيه وفقاً لتقديرات ديسمبر 2026، مع تأكيد توصيتها القوية بشراء السهم الذي يتداول حاليا عند مضاعف ربحية لآخر 12 شهراً يبلغ 26.9 مرة، بقيمة سوقية تصل إلى 86.3 مليار جنيه.
- Tue 17 Nov | موقع الموقع | وزيرة التضامن تقود خطة تطوير الخدمات الرقمية ببنك ناصر بالتعاون مع «إي فاينانس»
  https://almawq3.com/وزيرة-التضامن-تقود-خطة-تطوير-الخدمات-ا/
  > وقع بنك ناصر الاجتماعي، برئاسة الدكتورة مايا مرسي، وزيرة التضامن الاجتماعي ورئيسة مجلس إدارة البنك، بروتوكول تعاون مع شركة «e Novate» المتخصصة في تشغيل وإدارة الحلول الذكية للمدفوعات الرقمية، وإحدى الشركات التابعة لشركة «إي فاينانس للاستثمارات المالية والرقمية»، وذلك في إطار خطة البنك لتطوير خدماته المالية والمصرفية، وتعزيز كفاءة منظومة المدفوعات الرقمية، ومواكبة التحول التكنولوجي ...
## BQDC  (8 leads)
- Thu 19 Nov | وطنا نيوز | بنك القاهرة عمان راعيًا فضيًا لجائزة الحسين لأبحاث السرطان للعام 2026
  https://watananews.com/572714/
  > وطنا اليوم: قدم بنك القاهرة عمان رعايته الفضية لجائزة الحسين لأبحاث السرطان لعام 2026، تأكيدًا على التزامه بدعم البحث العلمي وتطوير أبحاث السرطان، وتشجيع الابتكار في هذا المجال على مستوى الأردن والوطن العربي.
- Wed 18 Nov | العراب نيوز | بنك القاهرة عمان راعيًا فضيًا لجائزة الحسين لأبحاث السرطان لعام 2026
  https://alarrabnews.com/article/166465
  > تأكيدًا على التزامه بدعم البحث العلمي وتعزيز الجهود الرامية إلى مكافحة مرض السرطان، قدّم بنك القاهرة عمان رعايته الفضية لجائزة الحسين لأبحاث السرطان لعام 2026، في إطار حرصه على دعم المبادرات العلمية والصحية الرائدة، والمساهمة في تطوير الأبحاث الطبية وتشجيع الابتكار العلمي بما يسهم في تحسين فرص الوقاية من السرطان وتشخيصه وعلاجه على مستوى الأردن ...
- Wed 18 Nov | بنكي | بنك القاهرة يرفع الفائدة على حساب توفير ثروة لتصل لـ 16.75% سنوياً
  https://www.bankygate.com/202778
  > رفع بنك القاهرة أسعار الفائدة على حساب توفير ثروة لتصل إلى 16.75% سنويًا، مع صرف العائد بدورية شهرية، وذلك وفقًا لشرائح رصيد الحساب، في خطوة تعزز العوائد المقدمة للعملاء. ويبدأ احتساب العائد من رصيد 100 ألف جنيه، بينما يبلغ الحد الأدنى لفتح الحساب 50 ألف جنيه. حساب توفير ثروة من بنك القاهرة
## SKPC  (2 leads)
- Wed 18 Nov | جريدة باور نيوز الاخبارية | ترقية إسلام زيدان مديرًا عامًا للشئون القانونية بسيدبك مع استمرار ندبه لـ«ووتك»
  https://powernews.cc/?p=294339
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 17 Nov | بترونيوز | بترومنت تجدد عقد الصيانة الشاملة مع سيدبك لتعزيز كفاءة التشغيل واستدامة الأصول
  https://petro-news.com/182015
  (page: did not load (403))
## EFID  (4 leads)
- Wed 18 Nov | جريدة المال | كريم الشرقاوي: إيديتا تستهدف التوسع في أسواق متعددة وتدرس فرصًا استحواذية لدعم نمو أعمالها
  https://almalnews.com/2148194/كريم-الشرقاوي-إيديتا-تستهدف-التوسع-في-أسواق/
  > قال كريم الشرقاوي، مدير القطاع المالي بمجموعة إيديتا إيجيب، إن المجموعة تستهدف مواصلة التوسع في أسواق متعددة، إلى جانب دراسة فرص الاستحواذ المحتملة، بما يدعم نمو أنشطتها وتعزيز انتشارها الجغرافي خلال الفترة المقبلة.
- Wed 18 Nov | Zawya | Edita’s Q3 profit jumps 41.5% on record sales
  https://www.zawya.com/en/special-coverage/equities/editas-q3-profit-jumps-41.5-on-record-sales-2326603
  > Edita Food Industries (EFID.CA), one of Egypt’s leading packaged snack-food makers, reported a 41.5% year-on-year rise in net profit to EGP 938.1m for the third quarter (Q3) of 2026. Revenues reached EGP 7.3bn, the highest quarterly div in the company’s history. Q3 revenues rose 32.9% from the same quarter of 2025. [Figures on the page: consolidated; nine months; one quarter. Check which one each figure is.]
- Tue 17 Nov | Billionaires.Africa | Egyptian tycoon Hani Berzi's Edita posts 65% jump in nine-month profit
  https://www.billionaires.africa/2026/11/17/egyptian-tycoon-hani-berzis-edita-posts-65-jump-in-nine-month-profit/
  > Edita Food Industries SAE, the Egyptian snack maker founded and controlled by Hani Berzi, said profit for the first nine months of 2026 rose about 65% as record sales volumes lifted earnings despite pressure on margins in the third quarter. [Figures on the page: nine months; first half; one quarter; attributable to shareholders. Check which one each figure is.]
- Tue 17 Nov | CNN الاقتصادية | إيديتا لـCNN الاقتصادية: نتوقع مبيعات بـ27 مليار جنيه.. ونغيّر شبكة التوزيع في المغرب
  https://cnnbusinessarabic.com/finance-markets/1152802/إيديتا-لcnn-الاقتصادية-نتوقع-مبيعات-ب27-مليار-جنيه-ونغير-شبكة-التوزيع-في-المغرب
  > تتوقع شركة إيديتا للصناعات الغذائية أن تبلغ مبيعاتها نحو 27 مليار جنيه، وربما أكثر، خلال عام 2026، متجاوزة مستهدفها المعلن البالغ 26 مليار جنيه، مع زيادة الكميات المبيعة وطرح منتجات بأحجام وأسعار مختلفة.
## AAPL  (8 leads)
- Wed 18 Nov | Yahoo! Finance Canada | Apple Inc. (AAPL) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/AAPL/
  > designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories.
- Wed 18 Nov | Investor's Business Daily | Apple Stock Polishes Breakout As Nvidia-Led AI Boom Gets Wake-Up Call
  https://www.investors.com/research/ibd-stock-analysis/apple-stock-outshines-ai-peers-nvidia-meta/
  > Turmoil among market indexes and artificial intelligence leaders like Nvidia (NVDA) and Meta Platforms (META) has dragged down Investor's Business Daily's recommended market exposure level to the lowest-possible range of 0% - 20%. Yet in that environment, shares of Apple (AAPL) stock remain impressively strong.
- Wed 18 Nov | Barchart.com | Apple Stock Shows Strength Now, and a Key Catalyst Is Brewing in June 2027
  https://www.barchart.com/story/news/8900400/apple-stock-shows-strength-now-and-a-key-catalyst-is-brewing-in-june-2027
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
## MSFT  (8 leads)
- Thu 19 Nov | Benzinga | John Moolenaar Calls Out Microsoft for ‘Playing Both Sides’ of US-China AI Race
  https://www.benzinga.com/markets/tech/26/11/63418560/microsoft-bytedance-national-security
  (page: did not load (403))
- Thu 19 Nov | marketscreener.com | Microsoft Corporation : Gets a Buy rating from Jefferies
  https://www.marketscreener.com/news/microsoft-corporation-gets-a-buy-rating-from-jefferies-ce785eddd18ffe26
  (page: did not load (403))
- Thu 19 Nov | marketscreener.com | Microsoft Corporation : JP Morgan keeps its Buy rating
  https://www.marketscreener.com/news/microsoft-corporation-jp-morgan-keeps-its-buy-rating-ce785eddd18cf225
  (page: did not load (403))
## NVDA  (8 leads)
- Thu 19 Nov | Benzinga | Trump Reportedly Traded Over $97 Million Worth of Nvidia Stock in 2 Years — Elizabeth Warren Wants Congre
  https://www.benzinga.com/news/politics/26/11/63376420/trump-reportedly-traded-over-97-million-worth-of-nvidia-stock-in-2-years-elizabeth-warren-wants-congress-to-force-him-to-divest
  (page: did not load (403))
- Thu 19 Nov | Trefis | Your Nvidia Weight Sets How Much A Fall Hurts
  https://www.trefis.com/stock/nvda/articles/626647/your-nvidia-weight-sets-how-much-a-fall-hurts/2026-11-19
  > Your Nvidia Weight Sets How Much A Fall Hurts Nvidia closed at $150.96 on Wednesday, Nov 18. That is 36.9% below its record close of $239.24 on Oct 6. Wednesday’s 2.9% drop came the day after Nvidia’s third-quarter report. Revenue rose 103% from a year earlier, to $115.8 billion.
- Thu 19 Nov | Morningstar | Nvidia’s Crisis Has Boosted Competing Stocks
  https://global.morningstar.com/en-nd/stocks/nvidias-crisis-has-boosted-competing-stocks
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Yahoo Finance | Anthropic's record IPO lands as Nvidia suffers its worst run since 2008
  https://finance.yahoo.com/markets/stocks/articles/anthropics-record-ipo-lands-nvidia-053102964.html
  > For years, Jensen Huang and Dario Amodei could hardly agree on anything. The Nvidia founder once said he disagreed "with almost everything" the Anthropic chief executive says. [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Thu 19 Nov | Yahoo Finance | Why Did Cathie Wood Sell Nvidia Before Earnings and Buy Crypto Stocks?
  https://finance.yahoo.com/markets/crypto/articles/why-did-cathie-wood-sell-050000758.html
- Thu 19 Nov | WRAL | Invested in Nvidia? Here's how financial planners say you should handle your portfolio
  https://www.wral.com/consumer/5onyourside/financial-advice-nvidia-money-invest-retire-banking-november-2026/
- Thu 19 Nov | The Motley Fool | 4 Things the Headlines Missed in Nvidia's First Post-Jensen Earnings Report
  https://www.fool.com/investing/2026/11/18/4-things-the-headlines-missed-in-nvidia-s-first-post-jensen-earnings-report/
- Thu 19 Nov | Yahoo Finance | Dan Ives Says Nvidia’s AI Dominance Can Survive Without Jensen Huang: ‘Two, Three Years Ahead’ Of Rivals
  https://finance.yahoo.com/technology/ai/articles/dan-ives-says-nvidia-ai-033956725.html
## AMZN  (8 leads)
- Thu 19 Nov | Stocktwits | ASTS Stock Jumps Overnight Despite New Shares For Engines And Spectrum — Bulls Cheer ULA’s Amazon Launch Clue
  https://stocktwits.com/news-articles/markets/equity/asts-new-shares-engines-spectrum-bulls-ula-amazon-launch-clue/cNbLyqER9iS
  > Shares of AST SpaceMobile (ASTS) rebounded nearly 3% overnight heading into Thursday despite new shares for rocket engines and spectrum rights, as retail bulls saw an encouraging sign for its next Blue Origin flight in the probe of a failed Amazon satellite launch.
- Thu 19 Nov | TipRanks | Amazon’s Anthropic Stake Is Worth $159 Billion – What It Means for AMZN Stock
  https://www.tipranks.com/news/amazons-anthropic-stake-is-worth-159-billion-what-it-means-for-amzn-stock
  (page: did not load (403))
- Thu 19 Nov | 24/7 Wall St. | Amazon's $18 Billion Anthropic Bet Is Worth $159 Billion at the IPO Price. Here's What That Is Per Amazon Share
  https://247wallst.com/investing/2026/11/18/amazons-18-billion-anthropic-bet-is-worth-159-billion-at-the-ipo-price-heres-what-that-is-per-amazon-share/
  > Amazon’s $18 Billion Anthropic Bet Is Worth $159 Billion at the IPO Price. Here’s What That Is Per Amazon Share [Figures on the page: nine months; one quarter. Check which one each figure is.]
- Thu 19 Nov | Benzinga | ANT, UNH, CRWD, TTWO, AMZN: 5 Trending Stocks Today - Amazon.com (NASDAQ:AMZN)
  https://www.benzinga.com/markets/equities/26/11/63416815/anthropic-unitedhealth-group-crowdstrike-take-two-interactive-and-amazon-why-these-5-stocks-are-on-investors-radars-today
  (page: did not load (403))
- Wed 18 Nov | Forbes | Google And Amazon Will Own More Anthropic Stock Than All Cofounders Combined
  https://www.forbes.com/sites/richardnieva/2026/11/18/google-and-amazon-will-own-more-anthropic-stock-than-all-cofounders-combined/
- Wed 18 Nov | Cryptonews.net | XRP Price Targets as XRP Chart Resembles Amazon Before Its Historic Breakout
  https://cryptonews.net/news/analytics/33772149/
- Wed 18 Nov | Yahoo! Finance Canada | Amazon.com, Inc. (AMZN) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/AMZN/
- Wed 18 Nov | MarketBeat | Amazon.com (NASDAQ:AMZN) Stock Jumps 3.8% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-amazoncom-nasdaq-amzn-stock-jumps-38-heres-why-2026-11-18/
## GOOGL  (8 leads)
- Thu 19 Nov | Investing.com UK | Form 4 Alphabet Inc Class A For: 19 November By Investing.com
  https://uk.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-19-november-93CH-4992400
  (page: did not load (403))
- Thu 19 Nov | FXLeaders | Alphabet Stock Rebounds From Support as Anthropic Stake Pre IPO and Nvidia Earnings Lift GOOG
  https://www.fxleaders.com/news/2026/11/18/alphabet-stock-rebounds-from-support-as-anthropic-stake-pre-ipo-and-nvidia-earnings-lift-goog/
  > Alphabet Stock Rebounds From Support as Anthropic Stake Pre IPO and Nvidia Earnings Lift GOOG Alphabet (GOOGL) shares have rebounded from the $280 support zone after falling below $300, as stronger Nvidia results improve sentiment across the technology sector.
- Thu 19 Nov | Gotrade | Google Stock (GOOGL) Rises 0.8% to $282.44 (Nov 18)
  https://www.heygotrade.com/en/news/google-googl-stock-news-november-19-2026/
  > AI-powered contentSome parts of this article are powered by AI. Alphabet (GOOGL) closed at $282.44 on November 18, 2026, up 0.80%, while the Nasdaq Composite gained 0.42%. None of the reports reviewed named a company-specific cause; on the same day, Anthropic priced its IPO at $83 per share, according to CNBC.
## META  (8 leads)
- Thu 19 Nov | Seeking Alpha | Meta: Buy The AI Payoff Before The Capex Fear Fades
  https://seekingalpha.com/article/4969963-meta-buy-the-ai-payoff-before-the-capex-fear-fades
  > - Meta Platforms is a Buy: AI-driven ad pricing supports a $712–$782 base case, despite spending and funding risks. - Q3 revenue grew 26% as ad prices rose 14% and impressions increased 10%, showing advertisers are paying more for performance.
- Thu 19 Nov | Kalkine Media | What Does a Bigger AI Spending Plan Mean for Meta (NASDAQ:META)?
  https://kalkinemedia.com/us/stocks/communication/what-does-a-bigger-ai-spending-plan-mean-for-meta-nasdaqmeta
  > - Meta Platforms drew fresh attention as the company signaled a notably larger artificial-intelligence spending plan for the year ahead. - The advertising engine across its family of apps remains the financial foundation funding the heavy build-out. Meta Platforms (NASDAQ:META) Communication Services Meta Platforms Inc.
- Thu 19 Nov | finance.biggo.com | Meta Shelves Class C Stock Issuance to Preserve Zuckerberg's Control as Shareholder Lawsuit Looms
  https://finance.biggo.com/news/0739ef36-a9fa-4aa4-a0c4-85d5c940e6b0
  > Meta Shelves Class C Stock Issuance to Preserve Zuckerberg's Control as Shareholder Lawsuit Looms [Figures on the page: consolidated; attributable to shareholders. Check which one each figure is.]
## TSLA  (8 leads)
- Thu 19 Nov | BigGo Finance | Musk Says Tesla and SpaceX Are 'Probably Better Together' but Rejects Merger-Linked Pay
  https://finance.biggo.com/news/c0f91318-21a4-45b1-81a7-d3d14f0fbacb
  > Musk Says Tesla and SpaceX Are 'Probably Better Together' but Rejects Merger-Linked Pay Elon Musk told a New York audience this week that Tesla and SpaceX would likely be worth more as one company, while insisting a combination should not by itself hand him the performance-based stock awards tied to Tesla's operating results.
- Wed 18 Nov | TIKR.com | Waymo Ordered Off California Freeways for an “Imminent Hazard to Public Safety.” Tesla Has More at Stake
  https://www.tikr.com/blog/waymo-ordered-off-california-freeways-for-an-imminent-hazard-to-public-safety-tesla-has-more-at-stake?
  > - California’s DMV ordered Alphabet’s Waymo off the state’s freeways, calling its driverless freeway operations “an imminent hazard to public safety.” - Tesla has far more at stake: it trades at about 178x forward earnings, compared with about 20x for Alphabet.
- Wed 18 Nov | Stocktwits | Elon Musk Says Tesla And SpaceX Could Be ‘Better Together’ – But There’s A Catch To His TSLA Pay
  https://stocktwits.com/news-articles/markets/equity/tesla-spacex-better-together-musk-performance-tsla-pay/cNbLsa5R9iJ
  > Elon Musk said on Wednesday that Tesla (TSLA) and SpaceX (SPCX) would probably be better together, but that closing a merger shouldn’t be enough to earn him the stock awards Tesla tied to its performance. Both stocks rose for a second straight session on Wednesday, with TSLA gaining 1 % and SPCX climbing 1.3%.
## JPM  (8 leads)
- Thu 19 Nov | Investing.com Canada | JPMorgan upgrades DBS Group stock rating on valuation, raises PT By Investing.com
  https://ca.investing.com/news/stock-market-news/jpmorgan-upgrades-dbs-group-stock-rating-on-valuation-raises-pt-93CH-4968651
  (page: did not load (403))
- Thu 19 Nov | Simply Wall St | Why Is JPMorgan Chase (JPM) Naming Bregje De Best As Its Next CFO?
  https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/why-is-jpmorgan-chase-jpm-naming-bregje-de-best-as-its-next
  > JPMorgan Chase (NYSE:JPM) said Bregje de Best will succeed Jeremy Barnum as Chief Financial Officer after the first quarter of 2027. De Best currently serves in senior finance leadership at JPMorgan Chase and will work alongside Barnum during a multi year transition period.
- Thu 19 Nov | Investing.com India | JPMorgan cuts CRH stock price target on weaker outlook By Investing.com
  https://in.investing.com/news/stock-market-news/jpmorgan-cuts-crh-stock-price-target-on-weaker-outlook-93CH-5714206
  (page: did not load (403))
## XOM  (8 leads)
- Thu 19 Nov | Kalkine Media | Why ExxonMobil (NYSE:XOM) Faced Market Pressure?
  https://kalkinemedia.com/us/stocks/energy/why-exxonmobil-nysexom-faced-market-pressure
  > - ExxonMobil experienced market pressure despite positive operational developments and stronger quarterly financial performance. - New production from Guyana strengthens the company's energy operations and production pipeline.
- Thu 19 Nov | GuruFocus | ExxonMobil (XOM) Advances Venezuela Oil Exploration Amid $100B U
  https://www.gurufocus.com/news/9209418/exxonmobil-xom-advances-venezuela-oil-exploration-amid-100b-us-energy-deal
  (page: did not load (403))
- Thu 19 Nov | Kalkine | WTI Crude Near US$83: What Matters for ExxonMobil and Canadian Natural?
  https://kalkine.com.au/news/energy/wti-crude-near-us83-what-matters-for-exxonmobil-and-canadian-natural
  (page: did not load (403))
- Thu 19 Nov | Construction Review | Rovuma LNG Project: Mozambique Approves ExxonMobil’s Amended $30B Development Plan
  https://constructionreviewonline.com/rovuma-lng-project-mozambique-approves-exxonmobils-amended-30b-development-plan/
  > Mozambique’s Council of Ministers approved ExxonMobil’s amended development plan for the Rovuma LNG project. This approval cleared a regulatory hurdle before a final investment decision (FID) that the company expects by the end of the year.
- Thu 19 Nov | Admirals | Exxon Mobil Stock: Business, News and Key Risks
  https://admiralmarkets.com/education/articles/shares/exxon-mobil-stock
- Thu 19 Nov | Traders Union | What's behind Exxon Mobil's latest stock pullback?
  https://tradersunion.com/news/stocks/show/4313146-exxon-mobil-slides-3-66percent-today/
- Thu 19 Nov | iMarine | SBM Offshore Secures Contracts from ExxonMobil Guyana for Longtail FPSO
  https://www.imarinenews.com/41053.html
- Thu 19 Nov | Cyprus Shipping News | ExxonMobil starts production at Uaru, raising Guyana’s installed capacity to 1.1 million barrels per day
  https://cyprusshippingnews.com/2026/11/19/exxonmobil-starts-production-at-uaru-raising-guyanas-installed-capacity-to-1-1-million-barrels-per-day/
## AVGO  (8 leads)
- Thu 19 Nov | Seeking Alpha | Broadcom: Scale-Up And Scale-Out Ethernet Networking Remains Underappreciated By Market
  https://seekingalpha.com/article/4969949-broadcom-scale-up-and-scale-out-ethernet-networking-remains-underappreciated-by-market
  (page: only 33 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Kalkine Media | Broadcom (NASDAQ:AVGO) Rises As AI Chip Demand Builds
  https://kalkinemedia.com/us/stocks/technology/broadcom-nasdaqavgo-rises-as-ai-chip-demand-builds
  > - Broadcom advanced as enthusiasm across the artificial intelligence sector strengthened. - Management anticipates substantial expansion in AI-chip demand. Broadcom benefits from renewed enthusiasm surrounding artificial intelligence infrastructure, with customized semiconductor demand supporting its business activity while customer concentration and competitive pressures remain important considerations.
- Thu 19 Nov | Kalkine Media | Is Broadcom (NASDAQ:AVGO) Extending Its Climb?
  https://kalkinemedia.com/us/stocks/technical-analysis/is-broadcom-nasdaqavgo-extending-its-climb
  > - Broadcom (NASDAQ:AVGO) Technology Broadcom Inc (NASDAQ:AVGO) 353.97 USD +12.370 3.621% Last Updated at: 2026-11-18T21:00:00Z has stretched its uptrend as demand for custom artificial-intelligence silicon stays brisk. - Networking hardware and custom accelerators for large computing operators sit behind the chart story.
- Thu 19 Nov | 재경일보 | Nvidia stock plunges 30% in a month; AMD and Broadcom trend upward : Finance : JKN
  https://news.jkn.co.kr/editions/english/post/1106235
  > Nvidia shares fell for the fifth consecutive trading day on the 18th (local time), even after reporting earnings and future guidance that beat market expectations. Amid growing management uncertainty following the resignation of its CEO, AMD and Broadcom rose as they emerged as alternative stocks.
- Thu 19 Nov | The Globe and Mail | Thinking About Buying Anthropic’s IPO on Nov. 19? Here’s an AI Stock I’d Consider First (Hint: It’s Not Nvidia or Broadcom).
  https://www.theglobeandmail.com/investing/markets/stocks/ASML/pressreleases/8906785/thinking-about-buying-anthropics-ipo-on-nov-19-heres-an-ai-stock-id-consider-first-hint-its-not-nvidia-or-broadcom/
- Wed 18 Nov | Global Banking & Finance Review | Broadcom rises 3.83% in Wednesday's session
  https://www.globalbankingandfinance.com/broadcom-avgo-rises-2026-11-18/
- Wed 18 Nov | TIKR.com | Up 50% in Last 12 Months, Can Broadcom Stock Keep Climbing in 2026?
  https://www.tikr.com/blog/up-50-in-last-12-months-can-broadcom-nasdaq-avgo-stock-keep-climbing-in-2026
- Wed 18 Nov | TipRanks | Broadcom price target lowered to $460 from $540 at Goldman Sachs
  https://www.tipranks.com/news/the-fly/broadcom-price-target-lowered-to-460-from-540-at-goldman-sachs-thefly-news
## BRK.B  (8 leads)
- Thu 19 Nov | JournalArta | Berkshire’s Kraft Heinz Stake Falls From $30 Billion to $8 Billion
  https://journalarta.com/en/2026/11/19/berkshire-kraft-heinz-stake-value-declines/
  > Berkshire’s Kraft Heinz Stake Falls From $30 Billion to $8 Billion Berkshire Hathaway remained Kraft Heinz’s largest shareholder through September, even after filing paperwork to enable a sale. The stake’s market value has fallen from nearly $30 billion in early 2017 to roughly $8 billion at early-November prices.
- Thu 19 Nov | JournalArta | Berkshire Hathaway (BRK-B) Stock: $574.62, Down 2.07% Nov 18
  https://journalarta.com/2026/11/19/berkshire-hathaway-stock-update-slides-2-07-down-2-3-in-five-sessions/
  > Berkshire Hathaway Stock Update: Slides 2.07%, Down 2.3% in Five Sessions Technical analysis of Berkshire Hathaway stock on November 18, 2026: price 574.62 USD, trend uptrend, RSI 60.8, support 540.34, resistance 592.94.
- Thu 19 Nov | Yahoo Finance | Berkshire’s stake in this stock was worth $30B. Now it’s $8B
  https://finance.yahoo.com/markets/stocks/articles/berkshire-stake-stock-worth-30b-050300544.html
  > Heinz ketchup and Kraft Mac & Cheese are pantry staples across America, and Berkshire Hathaway still owns more of the company behind them than anyone else. In January, a regulatory filing cleared the way for Berkshire to sell almost its entire stake in Kraft Heinz (KHC). Through September, Berkshire held on anyway.
- Thu 19 Nov | The Motley Fool Australia | 3 Berkshire 13F moves you may have missed while watching Anthropic and Nvidia
  https://www.fool.com.au/2026/11/19/3-berkshire-13f-moves-you-may-have-missed-while-watching-anthropic-and-nvidia/
  > While Wall Street was glued to Nvidia Corp (NASDAQ: NVDA) and Anthropic this week, investors may have overlooked the latest 13F quarterly filings. Every quarter, institutional managers overseeing at least US$100 million have to pull back the curtain and show the SEC what they've been buying and selling.
- Thu 19 Nov | Yahoo Finance | Warren Buffett Gives $5.4 Billion in Berkshire Shares to 4 Family Foundations— See Which One Gets the Most: ‘Be a Benefactor for Someone Else’
  https://finance.yahoo.com/markets/stocks/articles/warren-buffett-gives-5-4-023005052.html
- Thu 19 Nov | Yahoo Finance | Warren Buffett Expects Berkshire Hathaway (BRKA, BRKB) Stock to Drop About 50% Again Someday. Here's What He Says to Do Then.
  https://finance.yahoo.com/markets/stocks/articles/warren-buffett-expects-berkshire-hathaway-012500364.html
- Thu 19 Nov | Barchart.com | Berkshire Might Give Up on This High-Yielding Dividend Stock. You Maybe Should Too.
  https://www.barchart.com/story/news/8907215/berkshire-might-give-up-on-this-high-yielding-dividend-stock-you-maybe-should-too
- Thu 19 Nov | TIKR.com | The 5 Best Stocks in Berkshire Hathaway’s Portfolio
  https://www.tikr.com/blog/the-5-best-stocks-in-berkshire-hathaways-portfolio
## WMT  (8 leads)
- Thu 19 Nov | JournalArta | Walmart (WMT) Stock: $127.36, Down 0.13% Nov 18
  https://journalarta.com/en/2026/11/19/walmart-wmt-stock-on-wednesday-falls-0-13-up-1-3-in-five-sessions/
  > Walmart (WMT) Stock on Wednesday: Falls 0.13%, Up 1.3% in Five Sessions Technical analysis of WMT stock on November 18, 2026: price 127.36 USD, trend uptrend, RSI 64.1, support 118.77, resistance 129.17.
- Thu 19 Nov | Gotrade | Gotrade Daily: Anthropic Debut and Walmart Results Tonight
  https://www.heygotrade.com/en/news/anthropic-debut-and-walmart-results-tonight/
  > Anthropic starts trading on Nasdaq tonight after the largest IPO on record. Before the open, Walmart reports third-quarter results. Anthropic priced its IPO at $83 a share, above its $70 to $78 range, and raised $81.3 billion, according to CNBC. At that price, the company is worth about $1.5 trillion on a fully diluted basis.
- Thu 19 Nov | The Shortcut | Matt Swider | PS5 Pro is in stock at Walmart, but Black Friday is when you’re likely going to be able to buy it
  https://www.theshortcut.com/p/ps5-pro-is-in-stock-at-walmart-but
  > - 🚨 The Walmart PS5 Pro restock is currently happening through its online store - 🙅♂️ But no one could buySony’s most powerful PlayStation 5 video game console - ⏰ This means Walmart is likely saving inventory for next week, Black Friday
## V  (8 leads)
- Thu 19 Nov | The Daily Pennsylvanian | Federal judge throws out Trump rule limiting foreign student visa lengths
  https://www.thedp.com/article/2026/11/penn-international-student-final-rule-visa-enrollment
  > On Monday, a federal court struck down a Trump administration rule that would have placed significant restrictions on the number of years international students could lawfully study in the United States.
- Thu 19 Nov | Yahoo! Finance Canada | Visa Inc. (V.SN) Seasonal Returns Chart - Yahoo Finance
  https://ca.finance.yahoo.com/quote/V.SN/seasonality/
  (page: did not load (404))
- Wed 18 Nov | Blockchain News | Visa (V) Stock Price Prediction: Visa holds a constructive pullback as analysts stay broadly positive
  https://blockchain.news/news/20261118-price-prediction-v-visa-holds-a-constructive-pullback-as
  > What happened and why it matters Visa (V) is coming off a modest pullback, with the stock at $416.71 after falling 1.89% on the day. That leaves V shares below the 7-day and 20-day moving averages near $422.20 and $422.19, but still above the 50-day average at $403.34.
## ORCL  (8 leads)
- Thu 19 Nov | ad-hoc-news.de | Oracle stock: EUR 106.34, up 2.09% before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/oracle-stock-eur-106-34-up-2-09-before-xetra/70534462
  > Oracle stock traded at EUR 106.34 on Lang & Schwarz at 08:28 CET on Thursday, November 19, 2026, 2.09 percent above the Xetra close of Wednesday, November 18, 2026. Oracle provides database technology, cloud infrastructure and enterprise applications to businesses worldwide. Next Catalyst for Oracle
- Thu 19 Nov | Kalkine Media | Is Oracle (NYSE:ORCL) Seeing Steady Cloud Demand?
  https://kalkinemedia.com/us/stocks/technology/is-oracle-nyseorcl-seeing-steady-cloud-demand
  > - Oracle (NYSE:ORCL) Technology Oracle Corporation (NYSE:ORCL) 113.89 USD 0.000 0.000% Last Updated at: 2026-11-18T21:04:00Z stays in focus as its cloud-infrastructure backlog swells on brisk demand.
- Thu 19 Nov | 24/7 Wall St. | Oracle Falls to a Fresh One-Year Low of $113.89
  https://247wallst.com/cards/oracle-orcl-enriched-price-move-01m7rgxw3hmfctc8ae7kd5fd34
  > Oracle Falls to a Fresh One-Year Low of $113.89 As seen on the 24/7 Wall St. homepage on November 18, 2026. Oracle's close at a fresh one-year low of $113.89 puts it below its July 24 trough, a level buyers have not had to defend in a year.
## COST  (8 leads)
- Thu 19 Nov | South Florida Reporter | Costco Sees Surge in Panic-Buying Amid Tech Outages
  https://southfloridareporter.com/costco-sees-surge-in-panic-buying-amid-tech-outages/
  > Anxious consumers are flocking to Costco Wholesale Corp. to stock up on emergency supplies following a string of high-profile technology failures. According to the report COSTCO SHOPPERS ARE PANIC-BUYING DUE TO OUTAGES, ANALYSTS SAY from Bloomberg, shoppers are rapidly clearing shelves of survival essentials.
- Thu 19 Nov | Breitbart News | Tech Outages Spark Panic Buying, Costco Reaps the Rewards
  https://www.breitbart.com/pre-viral/2026/11/18/tech-outages-spark-panic-buying-costco-reaps-the-rewards/
  > Recent nationwide tech outages have triggered panic buying, driving up Costco’s sales as anxious shoppers stock up on essential supplies. In the final week of October, Costco’s U.S.
- Thu 19 Nov | New York Post | Panic at the Costco? Let’s not fall for doomer freak-outs — again
  https://nypost.com/2026/11/18/opinion/dont-fall-for-doomer-freak-outs-again/
  (page read: it never names the company, so probably not about it: skip)
## NFLX  (8 leads)
- Thu 19 Nov | Startup Fortune | Netflix trades near 16 times earnings after a 50% slide from its peak
  https://startupfortune.com/netflix-trades-near-16-times-earnings-after-a-50-slide-from-its-peak/
  > Netflix once sold at a premium because investors believed it could grow faster than anything else in media. At current levels, the market now prices it like a mature company, and the next two earnings reports will show whether that's fair.
- Wed 18 Nov | 24/7 Wall St. | Josh Brown Says Netflix Trades at 16 Times Next Year's Earnings After a 50% Drop. Is It a Buy?
  https://247wallst.com/investing/2026/11/18/josh-brown-says-netflix-trades-at-16-times-next-years-earnings-after-a-50-drop-is-it-a-buy/
  > Josh Brown Says Netflix Trades at 16 Times Next Year’s Earnings After a 50% Drop. Is It a Buy? Netflix (NASDAQ:NFLX | NFLX Price Prediction) has fallen sharply in 2026, and one of its best-known fans says the price now reflects much of the damage.
- Wed 18 Nov | TradingView | Rep. Byron Donalds Sells Netflix Stock for Loss: Here’s What He’s Buying Instead
  https://www.tradingview.com/news/benzinga:b7db4e1aa094b:0-rep-byron-donalds-sells-netflix-stock-for-loss-here-s-what-he-s-buying-instead/
  > Byron Donalds Sells Netflix Stock for Loss: Here’s What He’s Buying Instead Byron Donalds (R-Fla.) is one of the many members of Congress who have their stock trades regularly tracked by the public.
## INTC  (8 leads)
- Thu 19 Nov | Yahoo Finance Singapore | Intel Stock And The Chipmaking Picks Investors May Be Missing
  https://sg.finance.yahoo.com/news/intel-stock-chipmaking-picks-investors-051326573.html
  > Intel's push to win outside customers for its 18A-P chipmaking technology has turned a bruising share price slide into a live test of whether onshoring and advanced fabrication infrastructure can justify fresh attention. This shift in momentum creates a window in which investors risk being late rather than early.
- Thu 19 Nov | BigGo Finance | Intel's Foundry Business Scores Double Win: First External Customer Signs for 18A-P, Microsoft Adopts EMIB Packaging
  https://finance.biggo.com/news/64aa001b-0d0f-4c38-972d-93476238b1c3
  > Intel's Foundry Business Scores Double Win: First External Customer Signs for 18A-P, Microsoft Adopts EMIB Packaging Intel's foundry transformation has reached a key milestone. CEO Lip-Bu Tan announced Wednesday at the TomorrowX Summit in Austin, Texas, that the company has signed its first external customer for its 18A-series process.
- Thu 19 Nov | CNBC | Intel signs first external customer for advanced 18A chips
  https://www.cnbc.com/2026/11/18/intel-first-18a-foundry-customer.html
  > Intel CEO Lip-Bu Tan said on Wednesday that the company has signed the first outside customer for its 18A chips. "Resilient supply on the foundry is very important," Tan said at the TomorrowX Summit in Austin, Texas.
## LLY  (8 leads)
- Thu 19 Nov | Kalkine Media | How Does ObesityWeek Data Showcase the Eli Lilly (NYSE:LLY) Push?
  https://kalkinemedia.com/us/stocks/healthcare/how-does-obesityweek-data-showcase-the-eli-lilly-nyselly-push
  > - Eli Lilly lined up a broad ObesityWeek slate framed around moving obesity care beyond the scale - The data spanned an injectable mainstay, a watched oral medicine and earlier-stage metabolic compounds
- Wed 18 Nov | Simply Wall St | What Eli Lilly Buyers Were Betting On
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/what-eli-lilly-buyers-were-betting-on
  > If you only glanced at Eli Lilly’s headlines this year, the focus was on soaring GLP-1 revenues, fresh acquisitions across vaccines, oncology, and neuroscience, and raised guidance for 2026. Holding Eli Lilly over the past year would have returned 32.5%, including dividends.
- Wed 18 Nov | cwibc.co.id | Lilly Faces Potential Bidding Contest for Rhythm Pharmaceuticals
  https://cwibc.co.id/en/lilly-rhythm-pharmaceuticals-bidding-contest
  > Lilly Faces Potential Bidding Contest for Rhythm Pharmaceuticals A potential acquisition contest involving Eli Lilly and AstraZeneca is drawing attention to the biotechnology sector, as both pharmaceutical companies are linked to possible offers for Rhythm Pharmaceuticals, a Boston-based manufacturer of treatments for rare metabolic disorders. [Figures on the page: standalone; one quarter. Check which one each figure is.]
- Wed 18 Nov | Global Banking & Finance Review | Eli Lilly and Co falls 2.39% in Wednesday's session
  https://www.globalbankingandfinance.com/eli-lilly-and-co-lly-falls-2026-11-18/
  (page read: it never names the company, so probably not about it: skip)
- Wed 18 Nov | cwibc.co.id | Eli Lilly Raises Revenue Forecast on Strong Drug Demand
  https://cwibc.co.id/en/eli-lilly-revenue-forecast-drug-demand
- Wed 18 Nov | MarketWatch | Eli Lilly & Co. stock underperforms Wednesday when compared to competitors
  https://www.marketwatch.com/data-news/eli-lilly-co-stock-underperforms-wednesday-when-compared-to-competitors-1aa666c6-db25a8cd6cc6?mod=goog_fin_scmw
- Wed 18 Nov | GuruFocus | Health Canada Approves Eli Lilly's Mounjaro for Cardiovascular R
  https://www.gurufocus.com/news/9208381/health-canada-approves-eli-lillys-mounjaro-for-cardiovascular-risk-reduction-in-type-2-diabetes-lly
- Wed 18 Nov | Global News | Health Canada approves new Eli Lilly GLP-1 pill for weight loss
  https://globalnews.ca/news/12156896/health-canada-approves-eli-lilly-glp1/
Read 99 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, JUFO, EAST, EMFD, EGAL, AMOC.
