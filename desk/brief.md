# Desk brief, Tuesday, November 24, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 29s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-23 (26.62); Treasury yields to 2026-11-23 (10-year 4.92%).
- **valuation**: ok in 22s (GitHub Actions). LLY: $1.27tn, P/E (last 12 months) 42.7, Forecast P/E (fiscal 2026) 38.3 (the four quarters to Sep 2026)
- **movers**: ok in 19s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-04 AMZN results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 46.0
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.1%, median P/E 9.8; cheapest MASR +76%, ORHD +44%, MFPC +43%; dearest ARAB -62%, MOIN -64%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). 2026-10-30-rotation: on track -> open
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 131s (GitHub Actions). 
- **leads**: ok in 80s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 2 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 7 needed a retry.

## What moved (latest close against the one before)
- EGX30 50,712.00 (+1.44%); EGX70 EWI 17,098.20 (+3.41%); USD/EGP 54.44 (-0.11%); Gold 21K 5,680.00 (+1.97%); Brent 89.37 (-3.46%); S&P 500 7,237.17 (+4.73%); Nasdaq 24,089.56 (+6.51%); Bitcoin 60,414.00 (-1.69%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): NVDA +31.5%, INTC +16.3%, ORCL +12.3%, TSLA +11.5%, META +6.6%, GOOGL +6.3%, PHDC +4.7%, AMZN +3.5%, AVGO +3.0%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - CLHO: In a downtrend: below its 50-day average, which is below the 200-day; RSI 49, neither stretched nor washed out; the 50-day average crossed below the 200-day today.
    - EAST: No clear trend: 6.3% above its 50-day average and 8.6% below the 200-day; RSI 53, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - EMFD: No clear trend: 5.8% below its 50-day average and 7.2% above the 200-day; RSI 42, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - SKPC: In a downtrend: below its 50-day average, which is below the 200-day; RSI 36, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - SWDY: In an uptrend: above its 50-day average, which is above the 200-day; RSI 51, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - TMGH: In a downtrend: below its 50-day average, which is below the 200-day; RSI 38, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - AVGO: In a downtrend: below its 50-day average, which is below the 200-day; RSI 44, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - COST: In an uptrend: above its 50-day average, which is above the 200-day; RSI 68, neither stretched nor washed out; the 50-day average crossed above the 200-day 3 sessions ago; momentum turned down today (MACD crossed its signal line).
    - GOOGL: In a downtrend: below its 50-day average, which is below the 200-day; RSI 41, neither stretched nor washed out; momentum turned up today (MACD crossed its signal line).

## Movers that still need a reason (top five each way, 5% or more)
- EGX COPR (Cooper for Commercial Investment & Real Estate Development) +13.3%; EGX DTPP (Delta for Printing & Packaging) +12.2%; EGX OIH (Orascom Investment Holding) +10.8%; EGX ICFC (International Co. for Fertilizers & Chemicals) +9.9%; EGX GRCA (Grand Investment Capital) +9.4%; EGX CRST (Creast mark For Contracting) -8.3%; US NVDA (NVIDIA) +31.5%; US KYMR (Kymera Therapeutics) +30.4%; US ALAB (Astera Labs) +23.2%; US CRDO (Credo Technology Group Holding) +22.6%; US CRWV (CoreWeave) +22.3%; US CRWD (CrowdStrike Holdings) -8.9%; US WSO.B (Watsco) -5.4%; US TU (TELUS) -5.1%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-23 (TradingView's closes; Mubasher's list refused), 198 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (211)
US: 2026-11-23, 821 companies
US week and month: US companies worth $10bn or more (820)
EGX30 heatmap: 2026-11-23, 31 members
US heatmap: 2026-11-23, 100 members
Market values: 39 of 39 updated

# EGX 2026-11-23
## COPR +13.3%  Cooper for Commercial Investment & Real Estate Development
- no headlines found
## DTPP +12.2%  Delta for Printing & Packaging
- no headlines found
## OIH +10.8%  Orascom Investment Holding
- no headlines found
## ICFC +9.9%  International Co. for Fertilizers & Chemicals
- no headlines found
## GRCA +9.4%  Grand Investment Capital
- no headlines found
## CRST -8.3%  Creast mark For Contracting
- no headlines found
## RKAZ -4.5%  REKAZ Financial Holding
- no headlines found
## ELWA -1.7%  Elwadi for International Investment & Development
- no headlines found
## MOIL -1.3%  Maridive & Oil Services
- no headlines found
## CPCI -1.3%  Kahira Pharmaceuticals & Chemical Industries
- no headlines found

# US 2026-11-23
## NVDA +31.5%  NVIDIA
- Tue 24 Nov | Yahoo! Finance Canada | NVIDIA Corporation (NVDA) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/NVDA/
  > - Previous Close  125.53 - Bid 164.00 x 100 - Ask 164.71 x 100 - Day's Range  156.93 - 171.50 - 52 Week Range  124.50 - 243.37 - Market Cap (intraday)  3.985T - Beta (5Y Monthly) 2.25 - PE Ratio (TTM)  17.73 - EPS (TTM)  9.31
- Mon 23 Nov | Yahoo Finance UK | NVIDIA Corporation (NVDA) stock price, news, quote and history
  https://uk.finance.yahoo.com/quote/NVDA/
  > - Previous close  125.53 - Bid 164.00 x 100 - Ask 164.71 x 100 - Day's range  156.93 - 171.50 - 52-week range  124.50 - 243.37 - Market cap (intra-day)  3.985T - Beta (5Y monthly) 2.25 - PE ratio (TTM)  17.73 - EPS (TTM)  9.31
- Mon 23 Nov | Benzinga | Nvidia Stock Soars as Jensen Huang Returns as CEO - NVIDIA (NASDAQ:NVDA)
  https://www.benzinga.com/trading-ideas/movers/26/11/63526761/nvidia-stock-soars-as-jensen-huang-returns-as-ceo
  (page: did not load (403))
## KYMR +30.4%  Kymera Therapeutics
- Tue 24 Nov | Yahoo Finance | Is Kymera Therapeutics (KYMR) Pricey After Strong KT 621 Phase 2b Eczema Data?
  https://finance.yahoo.com/healthcare/articles/kymera-therapeutics-kymr-pricey-strong-071321861.html
  > Kymera Therapeutics (KYMR) shares have moved higher after 16-week Phase 2b BROADEN2 data for eczema drug KT-621 met all primary and secondary endpoints, showing rapid, placebo-adjusted symptom improvement.
- Tue 24 Nov | BeInCrypto | What Is Kymera and Why Did an Eczema Pill Outperform All AI Stocks on Monday?
  https://beincrypto.com/what-is-kymera-eczema-pill-stock/
  (page: did not load (403))
- Tue 24 Nov | Yahoo Finance | Kymera Therapeutics (KYMR) Bounces Back Big After a Painful Losing Streak
  https://finance.yahoo.com/healthcare/articles/kymera-therapeutics-kymr-bounces-back-044318739.html
  > (NASDAQ:KYMR) is one of the 10 Stocks With Eye-Popping Gains. Kymera Therapeutics snapped a five-day losing streak on Monday, surging 30.40 percent to finish at $150.37 apiece after its treatment candidate successfully showed a whopping 72 percent improvement in eczema patients during the mid-stage clinical trial.
- Tue 24 Nov | Yahoo Finance | Kymera Therapeutics Stock Gets A Lift From Eczema Trial Success
  https://finance.yahoo.com/healthcare/articles/kymera-therapeutics-stock-gets-lift-042552072.html
  > - Kymera Therapeutics reported that KT-621 met all primary and secondary endpoints in the 16 week BROADEN2 Phase 2b atopic dermatitis trial, with oral dosing producing statistically significant improvements versus placebo and efficacy described as comparable to leading biologics.
## ALAB +23.2%  Astera Labs
- Tue 24 Nov | Insider Monkey | Astera Labs (ALAB) Shares Are on Fire. What’s Behind the Surge?
  https://www.insidermonkey.com/news/astera-labs-alab-shares-are-on-fire-whats-behind-the-surge-1869158/
- Tue 24 Nov | GuruFocus | Astera Labs Inc (ALAB) Shares Surge 23.2% -- What GF Score of 27 Tells Investors
  https://www.gurufocus.com/news/9216057/astera-labs-inc-alab-shares-surge-232-what-gf-score-of-27-tells-investors
  (page: did not load (403))
- Mon 23 Nov | MarketBeat | Astera Labs (NASDAQ:ALAB) Shares Climb 23.2% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-astera-labs-nasdaq-alab-shares-climb-232-heres-why-2026-11-23/
  > Astera Labs (NASDAQ:ALAB) Shares Climb 23.2% - Here's Why - Astera Labs shares surged 23.2% to $222.12 in Monday trading, with volume 63% above its average.
- Mon 23 Nov | Traders Union | Astera Labs shares show technical rebound signals after steep correction
  https://tradersunion.com/news/stocks/show/4382179-astera-labs-shares-rebound-signals/
  (page: did not load (403))
## CRDO +22.6%  Credo Technology Group Holding
- Tue 24 Nov | Yahoo Finance | Credo Technology (CRDO) Just Made a Stunning Comeback
  https://finance.yahoo.com/markets/stocks/articles/credo-technology-crdo-just-made-031759842.html
  > Credo Technology Group Holding Ltd. (NASDAQ:CRDO) is one of the 10 Stocks With Eye-Popping Gains.
- Tue 24 Nov | Insider Monkey | Credo Technology (CRDO) Just Made a Stunning Comeback
  https://www.insidermonkey.com/news/credo-technology-crdo-just-made-a-stunning-comeback-1869155/
- Tue 24 Nov | GuruFocus | A Look at Credo Technology Group Holding Ltd (CRDO) After 22.6% Gain -- GF Value $294.08 vs Price $122.46
  https://www.gurufocus.com/news/9216148/a-look-at-credo-technology-group-holding-ltd-crdo-after-226-gain-gf-value-29408-vs-price-12246
  (page: did not load (403))
- Mon 23 Nov | Seeking Alpha | Tech rebound sends Credo Technology higher by 24% (CRDO:NASDAQ)
  https://seekingalpha.com/news/4675619-tech-rebound-sends-credo-technology-higher-by-24
  (page: did not load (403))
## CRWV +22.3%  CoreWeave
- Tue 24 Nov | Simply Wall St | Why Is CoreWeave (CRWV) In Focus After The AI Infrastructure Rally?
  https://simplywall.st/stocks/us/software/nasdaq-crwv/coreweave/news/why-is-coreweave-crwv-in-focus-after-the-ai-infrastructure-r
  > - CoreWeave (NasdaqGS:CRWV) moved into the spotlight after Nvidia CEO Jensen Huang unexpectedly returned with a renewed AI infrastructure push. - Huang’s comeback, announced globally in November 2026, triggered a sharp rally across AI hardware, cloud platforms and related infrastructure providers.
- Tue 24 Nov | Yahoo Finance | CoreWeave Inc. (CRWV) Just Turned the Tables. What Changed?
  https://finance.yahoo.com/markets/stocks/articles/coreweave-inc-crwv-just-turned-031501579.html
  > (NASDAQ:CRWV) is one of the 10 Stocks With Eye-Popping Gains. CoreWeave bounced back after seven straight days of weakness on Monday, soaring 22.32 percent to end at $48.33 apiece, mimicking the sharp rally on Wall Street supported by analysts' bullish rating for the stock.
- Mon 23 Nov | MarketBeat | CoreWeave (NASDAQ:CRWV) Shares Climb 22.3% - What's Next?
  https://www.marketbeat.com/instant-alerts/price-coreweave-nasdaq-crwv-shares-climb-223-whats-next-2026-11-23/
  > CoreWeave (NASDAQ:CRWV) Shares Climb 22.3% - What's Next? - CoreWeave shares surged 22.3% to $48.33 on unusually heavy trading volume, which was 172% above the average session volume.
- Mon 23 Nov | Crypto Briefing | CoreWeave surges 22% as Nvidia reinstates Jensen Huang as CEO
  https://cryptobriefing.com/coreweave-surges-22-as-nvidia-reinstates-jensen-huang-as-ceo/
  > CoreWeave shares surged by 22% after Nvidia reinstated Jensen Huang as its CEO, restoring investor confidence in AI-related stocks. Nvidia’s board made the unanimous decision to bring Huang back less than two weeks after his resignation, following discussions that satisfied the board about his leadership capabilities.
## CRWD -8.9%  CrowdStrike Holdings
- Tue 24 Nov | JournalArta | CrowdStrike (CRWD) Stock: $208.97, Down 8.92% Nov 23
  https://journalarta.com/en/2026/11/24/crowdstrike-crwd-stock-tumbles-8-92-on-monday-down-20-2-in-a-month/
  > CrowdStrike (CRWD) Stock Tumbles 8.92% on Monday, Down 20.2% in a Month Technical analysis of CRWD stock on November 23, 2026: price 208.97 USD, trend downtrend, RSI 38.1, support 208.97, resistance 268.02.
- Tue 24 Nov | The Motley Fool | CrowdStrike Holdings • Robinhood Token - CRWD - Stock Price & News
  https://www.fool.com/quote/crypto/crwd/
  > CrowdStrike Holdings • Robinhood Token(CRYPTO) CRWD CrowdStrike Holdings • Robinhood Token at a Glance
- Tue 24 Nov | Yahoo Finance | CrowdStrike Holdings, Inc. (CRWD) Stock Forecasts
  https://finance.yahoo.com/research/reports/MS_0P0001HOOZ_AnalystReport_1795489087000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 24 Nov | Kalkine Media | CrowdStrike Announces $43.9 Billion All-Stock Acquisition of Zscaler
  https://kalkinemedia.com/us/news/announcements/crowdstrike-announces-439-billion-all-stock-acquisition-of-zscaler
  > On November 23, 2026, CrowdStrike Holdings, Inc. submitted a Form 425 filing revealing its plan to acquire Zscaler, Inc., a leader in zero-trust network security, through an all-stock deal valued at roughly $43.9 billion, based on CrowdStrike's closing share price as of November 20, 2026.
## WSO.B -5.4%  Watsco
- Sat 21 Nov | Yahoo! Finance Canada | Watsco, Inc. (WSO) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/WSO/
  > - Previous Close  292.00 - Day's Range  292.18 - 299.90 - 52 Week Range  277.34 - 459.00 - Market Cap (intraday)  12.247B - Beta (5Y Monthly) 1.03 - PE Ratio (TTM)  25.78 - EPS (TTM)  11.49 - Earnings Date Oct 27, 2026 - Forward Dividend & Yield 13.20 (4.46%)
## TU -5.1%  TELUS
- Tue 24 Nov | Simply Wall St | TELUS (TSX:T) Stock Looks About Right As Rebound Follows 29% Slide
  https://simplywall.st/stocks/ca/telecom/tsx-t/telus-shares/news/telus-tsxt-stock-looks-about-right-as-rebound-follows-29-sli
  > TELUS has bounced sharply in recent weeks after a long stretch of weaker returns, which puts a spotlight on whether the current share price is sensible when judged against its sales base.
- Mon 23 Nov | MarketWatch | TELUS Corp. stock falls Monday, underperforms market
  https://www.marketwatch.com/data-news/telus-corp-stock-falls-monday-underperforms-market-810ace6a-3aef979f27b5?mod=mw_quote_news
  (page: did not load (401))
- Mon 23 Nov | kalkine.ca | Why TELUS Corporation (TSX:T) Is Trending on the S&P/TSX Composite Index: Large Cap Value Stock in Focus on 23 November 2026
  https://kalkine.ca/news/technology/why-telus-corporation-tsxt-is-trending-on-the-sptsx-composite-index-large-cap-value-stock-in-focus-on-23-november-2026
  (page: did not load (403))
- Mon 23 Nov | Kalkine Media | TELUS (TSX:T): How Is Its Special Committee Reviewing Quebecor's Proposal?
  https://kalkinemedia.com/ca/stocks/communication/telus-tsxt-how-is-its-special-committee-reviewing-quebecors-proposal
  > - TELUS stated that it calculated the value of that increase based on Qubecor's closing share price. - The Special Committee is made up of independent board members and is chaired by John Manley, who also chairs the TELUS Board.
## IP -4.5%  International Paper
- Tue 24 Nov | Yahoo Finance UK | International Paper Company (IP) stock price, news, quote and history
  https://uk.finance.yahoo.com/quote/IP/
- Mon 23 Nov | MarketWatch | International Paper Co. stock underperforms Monday when compared to competitors
  https://www.marketwatch.com/data-news/international-paper-co-stock-underperforms-monday-when-compared-to-competitors-ff1c7759-40faff60a9d8?mod=goog_fin_scmw
- Mon 23 Nov | Investing.com South Africa | International Paper board approves EMEA packaging business separation By Investing.com
  https://za.investing.com/news/stock-market-news/international-paper-board-approves-emea-packaging-business-separation-93CH-4592019
- Mon 23 Nov | Packaging Insights | Breaking news: International Paper approves DS Smith spin-off with London listing set for December 7
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: WMT, COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-24 CLHO results (expected)
- 2026-11-24 COST dividend
- 2026-11-24 EAST results (expected)  <- write its preview
- 2026-11-24 EFIH results (expected)  <- write its preview
- 2026-11-24 JUFO results (expected)
- 2026-11-24 PHDC results (expected)

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (open)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
    2026-10-30-rotation: on track -> open

## Fair value
- Changed since the last run: MFPC +47% -> +43% (high -> medium); PHAR +52% -> +32% (low -> low); AMOC -8% -> -8% (medium -> high); LCSW -45% -> -45% (low -> medium).
- In the ten cheapest or dearest with no note: MCQE, EMFD, ADIB, MTIE, AMOC, AMIA, LCSW, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-24. Open each story before using it.
## COMI  (8 leads)
- Tue 24 Nov | بنكي | CIB كينيا يحصد المركز الرابع ضمن الفئة الرابعة
  https://www.bankygate.com/203039
  > حقق فريق البنك التجاري الدولي – كينيا (CIB Kenya) المركز الرابع ضمن الفئة الثالثة (Tier III) في بطولة الألعاب الرياضية بين البنوك، التي تنظمها جمعية المصرفيين الكينية. وحل الفريق في المركز الـ22 في الترتيب العام من بين 40 بنكًا مشاركًا، في أول ظهور له بالبطولة.
- Tue 24 Nov | شبكة تواصل الإخبارية | الدولار يستقر أمام الجنيه.. تعرف على أسعاره في البنك الأهلي وبنك مصر وCIB
  https://twaslnews1.twaslnews.com/8210905/
  (page: did not load (403))
- Tue 24 Nov | الحق والضلال | البنك التجاري الدولي CIB يرفع عائد الشهادة الثلاثية لـ19% سنويًا بصرف شهري
  https://www.christian-dogma.com/2306125
  > شهادة Premium تبدأ من 50 ألف جنيه مع استرداد مشروط البنك التجاري الدولي CIB يرفع عائد الشهادة الثلاثية لـ19% سنويًا بصرف شهري بدأ البنك التجاري الدولي CIB تطبيق زيادة جديدة على عائد شهادة الادخار الثلاثية الثابتة Premium، اعتبارًا من الإثنين 23 نوفمبر 2026، لترتفع الفائدة السنوية من 18% إلى 19%، مع استمرار صرف الأرباح شهريًا.
## TMGH  (2 leads)
- Sun 22 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | صندوق الاستثمارات يوقع مذكرة تفاهم مع مجموعة طلعت مصطفى لتعزيز فرص التعاون
  https://www.argaam.com/ar/article/articledetail/id/1910794
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | Mubasher | مع تهاوي بورصة مصر.. كيف جاء أداء "التجاري الدولي" و"طلعت مصطفى"؟
  https://www.mubasher.info/news/21588660/مع-تهاوي-بورصة-مصر-كيف-جاء-أداء-التجاري-الدولي-و-طلعت-مصطفى
  > القاهرة - مباشر: قاد سهم التجاري الدولي هبوط المؤشر الرئيسي للبورصة "EGX30 دون 50000 نقطة، مع تراجعه في ختام اليوم نحو 2%. وفي ختام البوم انخفض سهم التجاري الدولي عند مستوى 125 جنيه مستقطبا تداولات قيمتها 267.2 مليون جنيه، فيما هبط كل من القلعة وطلعت مصطفى 4% و4.3% على التوالي.
## ETEL  (1 leads)
- Sun 22 Nov | Mubasher | 6 أسهم ترتفع وتخالف الاتجاه الهابط لبورصة مصر.. منها المصرية للاتصالات
  https://www.mubasher.info/news/21588645/6-أسهم-ترتفع-وتخالف-الاتجاه-الهابط-لبورصة-مصر-منها-المصرية-للاتصالات
  > القاهرة - مباشر: رغم الهبوط الجماعي لمؤشرات بورصة مصر بالتعاملات المتأخرة، تمكنت 6 أسهم من الارتفاع مخالفة الاتجاه الهابط للسوق اليوم الأحد. وبحلول الساعة 1:50 مساء، تمكنت 6 أسهم من الارتفاع منها سهم المصرية للاتصالات، مقابل هبوط 205 أسهم، فيما استقر 12 سهماً.
## PHDC  (1 leads)
- Sun 22 Nov | اليوم السابع | خريطة تحركات الكبار بالبورصة.. مشتريات في فوري ومصر الجديدة وتخارجات من بالم هيلز
  https://www.youm7.com/story/2026/11/22/خريطة-تحركات-الكبار-بالبورصة-مشتريات-في-فوري-ومصر-الجديدة-وتخارجات/7627730
  > شهدت تعاملات الداخليين والمساهمين الرئيسيين والمجموعات المرتبطة بهم بالبورصة المصرية خلال جلسة تداول يوم الخميس الماضي، تنفيذ عدد من عمليات الشراء والبيع على أسهم الشركات المقيدة، تصدرتها عمليات الشراء على سهم شركة نهر الخير للتنمية والاستثمار الزراعي والخدمات البيئية، إلى جانب تداولات على أسهم مينا للاستثمار السياحي والعقاري، وفوري لتكنولوجيا البنوك والمدفوعات الإلكترونية، وبالم هيلز ...
## SWDY  (8 leads)
- Tue 24 Nov | شبكة تواصل الإخبارية | شواحن السيارات الكهربائية في مصر على موعد مع طفرة.. «السويدي» تستهدف إنتاج أكثر من 25 ألف شاحن سنويا
  https://twaslnews1.twaslnews.com/8202507/
  (page: did not load (403))
- Mon 23 Nov | سولارابيك | باستطاعة 90 ميجاواط.. السويدي إليكتريك تنفّذ مشروعا للطاقة الشمسية في أنجولا
  https://solarabic.com/أخبار-الطاقة-المتجددة/2026/11/باستطاعة-90-ميجاواط-السويدي-إليكتريك-ت/
  > سولارابيك- دبي، الإمارات العربية المتحدة – 23 نوفمبر 2026: بدأت شركة السويدي إليكتريك لنقل وتوزيع الطاقة T&D تنفيذ مشروع كابيندا للطاقة الشمسية الكهروضوئية في أنجولا، بعد وضع حجر الأساس للمشروع بالتعاون مع شركة PRODEL-EP، الجهة المالكة، في خطوة تستهدف تعزيز إمدادات الكهرباء وتوسيع الاعتماد على مصادر الطاقة المتجددة في البلاد.
- Sun 22 Nov | almotawwer.com | السويدي إليكتريك تنفذ محطة طاقة شمسية بقدرة 90 ميجاوات في أنجولا لخدمة 30 ألف أسرة
  https://almotawwer.com/companies-and-investments/335050/
  > تواصل الشركات المصرية توسيع حضورها في سوق مشروعات الطاقة والبنية التحتية بالقارة الإفريقية، مستفيدة من خبراتها الهندسية وقدراتها التنفيذية في اقتناص مشروعات خارج السوق المحلية، بالتزامن مع توجه عدد من الدول الإفريقية إلى زيادة الاعتماد على مصادر الطاقة المتجددة وتطوير شبكات الكهرباء.
- Sun 22 Nov | خاص عن مصر | "السويدي إليكتريك" تعتزم رفع إنتاجها من شواحن السيارات الكهربائية بمصر لأكثر من 25 ألف سنويًا
  https://aboutmsr.com/السويدي-إليكتريك-تعتزم-رفع-إنتاجها-م/
  > تستهدف مجموعة السويدي إليكتريك زيادة الطاقة الإنتاجية لمصنعها المتخصص في تصنيع شواحن السيارات الكهربائية بمدينة العاشر من رمضان، لتتجاوز 25 ألف شاحن سنوياً، في خطوة تستهدف مواكبة نمو سوق التنقل الكهربائي في مصر، وتعزيز التصنيع المحلي لمكونات البنية التحتية اللازمة لتشغيل السيارات الكهربائية.
- Sun 22 Nov | شبكة تواصل الإخبارية | السويدي إليكتريك تضع حجر الأساس لمشروع كابيندا للطاقة الشمسية في أنجولا لخدمة 30 ألف أسرة
  https://twaslnews1.twaslnews.com/8125658/
- Sun 22 Nov | أموال الغد | «السويدي إليكتريك» تنتج 25 ألف شاحن سيارات كهربائية سنويًا بمصنع العاشر من رمضان
  https://amwalalghad.com/2026/11/22/السويدي-إليكتريك-تنتج-25-ألف-شاحن-سيار/
- Sun 22 Nov | شبكة تواصل الإخبارية | «السويدي إليكتريك» تقود تنفيذ مشروع متكامل للطاقة الشمسية وتخزين البطاريات في أنجولا
  https://twaslnews1.twaslnews.com/8121942/
- Sun 22 Nov | جريدة المال | السويدي إليكتريك تضع حجر أساس محطة شمسية بقدرة 90 ميجاوات بأنجولا لخدمة 30 ألف أسرة
  https://almalnews.com/2148863/السويدي-إليكتريك-تضع-حجر-أساس-محطة-شمسية/
## ORAS  (6 leads)
- Sun 22 Nov | https://www.youlyou.com/ | البورصة تفحص مستندات زيادة رأسمال أوراسكوم كونستراكشون إلى 207.4 مليون دولار
  https://www.youlyou.com/100438
  > تقدمت شركة أوراسكوم كونستراكشون بي إل سي بمستندات قيد أسهم زيادة رأس المال المصدر والمدفوع إلى البورصة المصرية، ليرتفع رأس المال من 110.24 مليون دولار إلى 207.44 مليون دولار، بزيادة قدرها 97.2 مليون دولار. [Figures on the page: consolidated; nine months. Check which one each figure is.]
- Sun 22 Nov | شبكة تواصل الإخبارية | «أوراسكوم كونستراكشون» تتقدم بمستندات زيادة رأس المال لـ207.4 مليون دولار
  https://twaslnews1.twaslnews.com/8126107/
  (page: did not load (403))
- Sun 22 Nov | جريدة المال | «أوراسكوم كونستراكشون» تقدم مستندات قيد زيادة رأسمالها لمبادلة أسهم «OCI N.V»
  https://almalnews.com/2148879/«أوراسكوم-كونستراكشون»-تقدم-مستندات-قيد-زيادة-رأسمالها/
  > أعلنت إدارة البورصة المصرية تقدم شركة أوراسكوم كونستراكشون بي إل سي بمستندات قيد أسهم زيادة رأس المال من 110.24 مليون دولار إلى 207.45 مليون دولار، بزيادة قدرها 97.20 مليون دولار.
## FWRY  (5 leads)
- Mon 23 Nov | سودان تربيون | بنك السودان يستعد لإطلاق منصة موحدة للدفع الفوري
  https://sudantribune.net/article/321565
  > الخرطوم 23 نوفمبر 2026- يستعد بنك السودان المركزي لإطلاق النظام القومي للدفع الفوري (NIPS)، في خطوة تستهدف تطوير البنية التحتية للمدفوعات الرقمية في السودان، وتمكين التحويلات والمدفوعات الفورية بين الأفراد والمصارف والجهات الحكومية والمنشآت التجارية، عبر منصة قومية موحدة تعمل على مدار الساعة.
- Mon 23 Nov | العربية | السودان يعلن تفاصيل نظام الدفع الفوري.. تحويلات بدون إنترنت
  https://www.alarabiya.net/amp/aswaq/economy/2026/11/23/السودان-يعلن-تفاصيل-نظام-الدفع-الفوري-تحويلات-بدون-انترنت
  (page: did not load (403))
- Sun 22 Nov | موقع القيادي | قصة نجاح فوري.. من دفع الفواتير إلى أرباح 2.9 مليار جنيه
  https://www.alqiyady.com/قصة-نجاح-فوري-من-دفع-الفواتير-إلى-أرباح-29-مليار-جنيه-897363.html
  > جميع الحقوق محفوظة  2026 © القيادي، احدى شركات بدأت فوري عام 2008 بفكرة بسيطة لتسهيل دفع الفواتير في بلد يعتمد على النقد، ثم تحولت إلى أول شركة ناشئة مصرية تتجاوز قيمتها مليار دولار، وتخدم اليوم أكثر من 54 مليون مستخدم. [Figures on the page: first half; one quarter. Check which one each figure is.]
## ABUK  (1 leads)
- Sun 22 Nov | www.marketscreener.com | Abu Qir Fertilizers & Chemical Industries Company (S.A.E) Reports Earnings Results for the Third Quarter and Nine Months Ended September 30, 2026
  https://www.marketscreener.com/news/abu-qir-fertilizers-chemical-industries-company-s-a-e-reports-earnings-results-for-the-third-qua-ce785ed3d088f024
  (page: did not load (403))
## HRHO  (8 leads)
- Tue 24 Nov | البوابة نيوز | "إي إف چي هيرميس" مدير الطرح الأوحد.. مصر لتأمينات الحياة تعلن عن النطاق السعري الاسترشادي للطرح في البورصة
  https://www.albawabhnews.com/5439811
  (page: did not load (403))
- Tue 24 Nov | مجلة أرقام | بإدارة إي اف چي هيرميس.. مصر لتأمينات الحياة تطرح 15% من أسهمها بالبورصة بسعر يصل إلى 13.60 جنيه
  https://arqam.news/612343/
  (page read: it never names the company, so probably not about it: skip)
- Mon 23 Nov | The TRADE | People Moves Monday: TD Securities, Verition Fund Management and EFG Holding
  https://www.thetradenews.com/people-moves-monday-td-securities-verition-fund-management-and-efg-holding/
  > Vinisha Minocha has joined TD Securities in New York as a director in electronic trading. She joins from Liquidnet, where she served as head of algos coverage for the US for more than eight years.
## CLHO  (1 leads)
- Mon 23 Nov | ad-hoc-news.de | Cleopatra Hospitals stock flags delay in financial statements
  https://www.ad-hoc-news.de/boerse/news/nebenwerte/cleopatra-hospitals-stock-flags-delay-in-financial-statements/70544940
  > Cleopatra Hospital Company said on November 18, 2026, that it would submit its financial statements for the period ended September 30, 2026 later than scheduled. The disclosure was carried by Sigma Capital, citing a release from the Egyptian Exchange.
## JUFO  (5 leads)
- Tue 24 Nov | جريدة المستقبل | اعتبارًا من الأحد المقبل| زيادة جديدة في أسعار ألبان جهينة
  https://www.elmostaqbal.com/879113/اعتبارًا-من-الأحد-المقبل-زيادة-جديدة-ف/
  > أعلنت شركة جهينة عن تطبيق زيادة جديدة في أسعار عدد من منتجات الألبان اعتبارًا من الأحد المقبل. وذلك وفقًا لما أخطرت به التجار والموزعين، بحسب تصريحات حازم المنوفي، عضو شعبة المواد الغذائية. زيادة سعر كرتونة لبن جهينة حيث سجل سعر كرتونة لبن جهينة 1 لتر نحو 650 جنيهًا، بواقع 54.2 جنيه للوحدة.
- Mon 23 Nov | المصري اليوم | شعبة المواد الغذائية: زيادة جديدة في أسعار ألبان جهينة اعتبارًا من الأحد المقبل
  https://www.almasryalyoum.com/news/details/4418551
  > شعبة المواد الغذائية: زيادة جديدة في أسعار ألبان جهينة اعتبارًا من الأحد المقبل أكد حازم المنوفي، عضو شعبة المواد الغذائية، أن شركة جهينة أخطرت التجار والموزعين بزيادة جديدة في أسعار منتجات الألبان، على أن يتم تطبيقها اعتبارًا من الأحد المقبل.
- Mon 23 Nov | الاقتصادي نيوز | Juhayna and Raie Misr Launch “100 Days of Health with Juhayna” Initiative to Serve Over 30,000 Patients in Upper Egypt
  https://eleqtisadenews.com/en/juhayna-and-raie-misr-launch-100-days-of-health-with-juhayna-initiative-to-serve-over-30000-patients-in-upper-egypt/
  > Juhayna Food Industries signed a cooperation protocol with Raie Misr Foundation for Development to launch the “100 Days of Health with Juhayna” initiative, aiming to provide free healthcare services to more than 30,000 patients from families most in need in Upper Egypt.
## MFPC  (3 leads)
- Sun 22 Nov | ايكونومي بلس | "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو"
  https://economyplusme.com/ar/news/34326
  > "سي آي كابيتال" ترفع السعر المستهدف لسهمي "أبوقير" و"موبكو" أبقت شركة "سي آي كابيتال" على توصيتها المحايدة لسهمي "أبو قير للأسمدة" و"مصر لإنتاج الأسمدة – موبكو"، مع رفع السعر المستهدف للسهمين، في ظل تذبذب أسعار اليوريا والتوترات الجيوسياسية المرتبطة بمضيق هرمز.
- Sun 22 Nov | بوابة الزهراء | سي آي كابيتال ترفع السعر المستهدف لسهمي أبوقير وموبكو في السوق المالية
  https://zahraa.mr/1348/سي-آي-كابيتال-ترفع-السعر-المستهدف-لسهم/
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Sun 22 Nov | جريدة آخر الأخبار | سي آي كابيتال تعدل السعر المستهدف لسهمي أبوقير وموبكو
  https://akher.news/1204/سي-آي-كابيتال-تعدل-السعر-المستهدف-لسهم/
  (page read: it never names the company, so probably not about it: skip)
## BQDC  (8 leads)
- Tue 24 Nov | TLB News | بنك القاهرة عمان وصيفاً لبطولة البنوك الخامسة لكرة القدم 2026
  https://www.talabanews.net/ar/بنك-القاهرة-عمان-وصيفاً-لبطولة-البنوك-الخامسة-لكرة-القدم-2026
  > عمّان – تُوّج فريق بنك القاهرة عمان لكرة القدم بالمركز الثاني في بطولة البنوك الخامسة لعام 2026، عقب المباراة النهائية التي جمعته بفريق بنك الإسكان على ملاعب توينز الرياضية، تحت رعاية محافظ البنك المركزي الأردني الدكتور عادل شركس.
- Tue 24 Nov | الجمهور الإخباري | بنك القاهرة: هذا آخر موعد يحق للمساهمين الراغبين في البيع إيداع أوامرهم
  https://www.algomhor.com/517187
  > بنك القاهرة: هذا آخر موعد يحق للمساهمين الراغبين في البيع إيداع أوامرهم كشف بنك القاهرة عن آخر موعد يحق فيه للمساهمين الراغبين في البيع إيداع أوامرهم لدى نظام الحساب المفتوح بالبورصة المصرية يوم الثلاثاء الموافق 1 ديسمبر 2026.
- Tue 24 Nov | مباشر بنوك مصر | بدءًا من 1 ديسمبر.. بنك القاهرة يرفع الفائدة على حساب "ميجا توفير" لحد أقصى 18.75%
  https://egyptbanks.info/13276/article/بدءًا-من-1-ديسمبر-بنك-القاهرة-يرفع-الفائدة-على-حساب-ميجا-توفير-لحد-أقصى-18-75-
  > أعلن بنك القاهرة عن رفع الفائدة على حساب "ميجا توفير" بدءًا من 1 ديسمبر، ليكون الحد الأقصى للعائد السنوي 18.75% بدلًا من 18.5% بحسب الرصيد، وباختلاف دورية الصرف. ويقوم البنك بفتح الحساب للأفراد فقط، وبالجنيه المصري فقط، وبحد أدنى 5000 جنيه لفتح الحساب، وحد أدنى 100 ألف جنيه لاحتساب العائد.
- Mon 23 Nov | المصري اليوم | «700 ألف مستثمر جديد في أقل من عام».. رئيس البورصة يكشف 600 مليون دولار تدفقات أجنبية من طرح بنك القاهرة
  https://www.almasryalyoum.com/news/details/4418321
  > «700 ألف مستثمر جديد في أقل من عام».. رئيس البورصة يكشف 600 مليون دولار تدفقات أجنبية من طرح بنك القاهرة
- Mon 23 Nov | شبكة تواصل الإخبارية | 13.11 مليار جنيه صافي أرباح بنك القاهرة المجمعة خلال أول 9 أشهر
  https://twaslnews1.twaslnews.com/8183933/
- Mon 23 Nov | شبكة تواصل الإخبارية | بنك القاهرة يحدد 1 ديسمبر آخر موعد لتقديم أوامر بيع أسهم الطرح العام
  https://twaslnews1.twaslnews.com/8181648/
- Mon 23 Nov | شبكة تواصل الإخبارية | شهادات بنك القاهرة 2026.. عائد يصل إلى 20.5% على شهادات بريمو
  https://twaslnews1.twaslnews.com/8180807/
- Mon 23 Nov | مجلة البوصلة الاقتصادية | 1 ديسمبر.. نهاية حق البيع في أسهم بنك القاهرة وفق آلية استقرار سعر السهم
  https://alboslanews.com/بنوك-و-تأمين/1-ديسمبر-نهاية-حق-البيع-في-أسهم-بنك-القاهرة-وفق-آلية-استقرار-سعر-السهم-431365
## EGAL  (1 leads)
- Sun 22 Nov | دار المعارف | طلائع مركز شباب قنا في ضيافة شركة مصر للألومنيوم
  https://daralmaref.com/News/2611455.aspx
  (page: did not load (403))
## EFID  (8 leads)
- Mon 23 Nov | GuruFocus | Edita Food Industries S.A.E (CAI:EFID) Q3 2026 Earnings Call Hig
  https://www.gurufocus.com/news/9215370/edita-food-industries-sae-caiefid-q3-2026-earnings-call-highlights-record-revenue-of-egp73-billion-and-415-profit-growth
  (page: did not load (403))
- Mon 23 Nov | Trendtype | Dislog and Edita end their joint venture in Morocco
  https://trendtype.com/insights/dislog-and-edita-end-their-joint-venture-in-morocco/
  (page: only 55 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | Food Business Middle East & Africa | Edita Food Industries profit jumps 65% in first nine months
  https://www.foodbusinessmea.com/edita-food-industries-profit-jumps-65-in-first-nine-months/
  > Record quarterly sales and higher volumes supported earnings growth, while the Egyptian snack maker continued investing in production capacity and expanding its regional operations. [Figures on the page: nine months; first half; one quarter; attributable to shareholders. Check which one each figure is.]
## AAPL  (6 leads)
- Mon 23 Nov | MacRumors | A Decade Later, Apple Remains Berkshire's Biggest Stock Bet
  https://www.macrumors.com/2026/11/23/apple-remains-berkshires-biggest-stock-bet/
  (page: only 63 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Mon 23 Nov | Yahoo Finance | Apple Hit an All-Time High While AI Stocks Sold Off. Here’s the Big Tech Stock I’d Buy.
  https://finance.yahoo.com/markets/stocks/articles/apple-hit-time-high-while-163202566.html
  > It has been a wild few weeks on Wall Street for big tech. Many of the leading stocks in the sector are down significantly from their all-time highs -- but not Apple (NASDAQ:AAPL).
- Mon 23 Nov | Traders Union | Apple stock forecast: Bearish momentum persists as sellers remain in control
  https://tradersunion.com/news/stocks/show/4373992-apple-drops-1-43percent-today-to/
  (page: did not load (403))
## MSFT  (8 leads)
- Tue 24 Nov | BW People | Microsoft Revises Azure Pay Structure, Rewards Top Performers With More Stock
  https://www.bwpeople.in/article/microsoft-revises-azure-pay-structure-rewards-top-performers-with-more-stock-634948
  > Microsoft is making compensation in its Azure cloud computing division more closely linked to employee performance, offering additional stock awards to top performers while introducing greater scrutiny of employees whose results fall below expectations. The changes were outlined in an internal memo circulated by Arun Ulagaratchagan, executive vice-president of Microsoft's Azure division.
- Tue 24 Nov | Business Today | NVIDIA pips Microsoft, Google in market cap after Jensen Huang's return as CEO
  https://www.businesstoday.in/markets/stocks/story/nvidia-pips-microsoft-google-in-market-cap-after-jensen-huangs-return-as-ceo-569198-2026-11-24
  > NVIDIA on Tuesday surpassed Microsoft and Google to emerge as world's second largest company by market capitalisation. Nvidia stock surged over 30% after its board announced Jensen Huang's immediate reinstatement as CEO and director. NVIDIA's market cap surged to $3.98 trillion followed by Microsoft $3.66 trillion and Alphabet Inc.
- Tue 24 Nov | Yahoo Finance | Microsoft CEO Satya Nadella Offered 60,000 Employees Buyouts So Everyone 'Felt Like They Had Agency' — Yet Insists Software Engineering Is 'Very Much Alive'
  https://finance.yahoo.com/technology/ai/articles/microsoft-ceo-satya-nadella-offered-023006172.html
  > Benzinga and Yahoo Finance LLC may earn commission or revenue on some items through the links below. Nobody enjoys being shown the door, so Microsoft Corp. Microsoft CEO Satya Nadella says the company's buyout offer to roughly 60,000 employees was about choice, as AI changes what a workday looks like inside the tech giant.
## NVDA  (8 leads)
- Tue 24 Nov | i24NEWS | Trump held at least $12 million in Nvidia stock while pressing for Jensen Huang's return - report
  https://www.i24news.tv/en/news/international/americas/artc-trump-held-at-least-12-million-in-nvidia-stock-while-pressing-for-jensen-huang-s-return-report
  > Trump held at least $12 million in Nvidia stock while pressing for Jensen Huang's return - report The White House insists Trump's accounts are independently managed, and neither Donald Trump nor his family can "direct, influence, or provide input" on the portfolio
- Tue 24 Nov | The Washington Post | Nvidia reinstates Jensen Huang after Trump speaks ‘directly’ to board
  https://www.washingtonpost.com/technology/2026/11/23/nvidia-board-reinstates-jensen-huang-after-us-government-input/
  (page: did not load (TimeoutError))
- Tue 24 Nov | The Dispatch | Jensen Huang’s Return Will Cost Nvidia
  https://thedispatch.com/article/jensen-huang-nvidia-reinstatement-business/
  > When Nvidia’s board announced that Jensen Huang would return as CEO less than two weeks after he left amid revelations about his extramarital affair with an alleged Chinese spy, the stock market rejoiced.
- Tue 24 Nov | Yahoo Finance | Nvidia Stock Just Had Its Best Day in Over a Decade. I'd Still Buy It Now.
  https://finance.yahoo.com/markets/stocks/articles/nvidia-stock-just-had-best-060302537.html
  > Nvidia (NASDAQ:NVDA) said on Monday, Nov. 23, that it had brought back Jensen Huang as president and CEO, effective immediately. As I write, the stock's up about 34% for the day, at roughly $168. It'd also add about $1 trillion to Nvidia's market value in one session. Missed Nvidia in 2009?
- Tue 24 Nov | The Washington Post | Markets soar as Huang returns as Nvidia CEO
  https://www.washingtonpost.com/business/2026/11/23/markets-soar-huang-returns-nvidia-ceo/
- Tue 24 Nov | The New York Times | Stocks Surge After Jensen Huang Is Reinstated as Nvidia CEO
  https://www.nytimes.com/2026/11/22/business/nvidia-stock-huang-ai-sp500-markets.html
- Tue 24 Nov | The Conversation | Trump had 4 reasons to ‘convince’ Nvidia to rehire Jensen Huang. Here’s why it matters globally
  https://theconversation.com/trump-had-4-reasons-to-convince-nvidia-to-rehire-jensen-huang-heres-why-it-matters-globally-297377
- Tue 24 Nov | ABC News - Breaking News, Latest News and Videos | Trump owned at least $12 million in Nvidia stock at the end of last year
  https://abcnews.com/US/trump-owned-12-million-nvidia-stock-end-year/story?id=138393684
## AMZN  (8 leads)
- Tue 24 Nov | TradingKey | Amazon Plans to Acquire Decart for About $7.5 Billion, Threatening Nvidia Data Center AI Chips
  https://www.tradingkey.com/analysis/stocks/us-stocks/262319616-stock-amazon-decart-nvidia-data-ai-chips-tradingkey
  > Amazon Plans to Acquire Decart for About $7.5 Billion, Threatening Nvidia Data Center AI Chips Amazon has agreed to acquire Israel’s Decart for approximately $7.5 billion, absorbing its core optimization software and R&D team to strengthen its Trainium computing power.
- Tue 24 Nov | blockchain.news | Amazon (AMZN) Stock Price Prediction: Price stabilizes near pivot as volume and derivatives diverge
  https://blockchain.news/news/20261124-price-prediction-price-amzn-stabilizes-near-pivot-as-volume-and
  > Price action is holding near a key pivot Amazon (AMZN) is trading at $257.73, slightly above the $257.34 pivot, after moving within a 24-hour range of $251.63 to $262.66. The stock’s 7-day moving average at $257.55 sits just below the current price, while the 20-day average at $261.49 remains overhead.
- Tue 24 Nov | Seeking Alpha | FAA probes Amazon delivery drone crash in Michigan near Detroit (AMZN:NASDAQ)
  https://seekingalpha.com/news/4675956-faa-probes-amazon-delivery-drone-crash-in-michigan-near-detroit
  (page: did not load (403))
- Tue 24 Nov | ad-hoc-news.de | Amazon's $7.5 Billion Decart Deal Caps a Week of Legal, Regulatory and Analyst News
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/amazon-s-7-5-billion-decart-deal-caps-a-week-of-legal-regulatory-and-analyst-news/70548086
  > Amazon shares climbed 3.9% in the prior session, with Reuters linking the advance to a broad recovery across AI-related equities. The buying followed Nvidia's decision to reinstate Jensen Huang as chief executive, a move that lifted sentiment across the sector and carried Amazon 5.1% higher on the day.
- Tue 24 Nov | Trefis | Is Amazon’s Profit Riskier Than It Looks?
  https://www.trefis.com/stock/amzn/articles/627559/is-amazon-s-profit-riskier-than-it-looks/2026-11-23
- Tue 24 Nov | TIKR.com | Stanley Druckenmiller and 45 Other Big Funds Bought Amazon Last Quarter. Dan Loeb and 25 Others Sold. Who’s Right?
  https://www.tikr.com/blog/stanley-druckenmiller-and-45-other-big-funds-bought-amazon-last-quarter-dan-loeb-and-25-others-sold-whos-right
- Mon 23 Nov | MarketBeat | Amazon.com (NASDAQ:AMZN) Stock Jumps 3.5% After Analyst Upgrade
  https://www.marketbeat.com/instant-alerts/price-amazoncom-nasdaq-amzn-stock-jumps-35-after-analyst-upgrade-2026-11-23/
- Mon 23 Nov | MarketWatch | Amazon may have just found a ‘cheap’ way to get a lot more out of its chips
  https://www.marketwatch.com/story/amazon-may-have-just-found-a-cheap-way-to-get-a-lot-more-out-of-its-chips-bd822bd5
## GOOGL  (8 leads)
- Tue 24 Nov | ad-hoc-news.de | Alphabet stock gains 1.11% to EUR 262.13 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/alphabet-stock-gains-1-11-to-eur-262-13-before-xetra/70548751
  > Alphabet is the parent company of Google LLC. On Xetra, the stock closed at EUR 259.25 on Monday, November 23, 2026. Alphabet financing reaches settlement date - Alphabet priced CAD 6 billion of senior notes in four tranches on November 19, according to Reuters. - The notes are scheduled to settle on Tuesday, November 24.
- Tue 24 Nov | blockchain.news | Alphabet (GOOGL) Stock Price Prediction: Alphabet tests its near-term pivot as bullish analyst targets meet mixed technicals
  https://blockchain.news/news/20261124-price-prediction-googl-alphabet-tests-its-near-term-pivot
  > Alphabet (Google) (GOOGL) closed at $285.95, up 3.28% on the day, after trading between $275.89 and $287.43. That puts the stock almost exactly on top of its 20-day moving average at $285.69, which matters because the bounce is coming from a short-term area where trend direction can either stabilize or roll over.
- Tue 24 Nov | Kalkine Media | Alphabet Director K. Ram Shriram Transfers 19,730 Shares Each of Class A and Class C Stock via Trust Gifts
  https://kalkinemedia.com/us/news/announcements/alphabet-director-k-ram-shriram-transfers-19730-shares-each-of-class-a-and-class-c-stock-via-trust-gifts
  > On November 23, 2026, Alphabet Inc. Ram Shriram submitted a Form 4 revealing gift transactions dated November 20, 2026, involving 19,730 shares each of Class A Common Stock and Class C Capital Stock transferred among irrevocable trusts at no cost per share. Ram Shriram, Director at Alphabet Inc.
- Tue 24 Nov | Investing.com India | Form 4 Alphabet Inc Class A: Kavitark Ram Shriram (Director) For: 23 November
  https://in.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-kavitark-ram-shriram-director-for-23-november-93CH-5722334
  (page: did not load (403))
- Tue 24 Nov | ACCESS Newswire | Levi & Korsinsky Reminds Alphabet Inc. Investors of The Pending Class Action Lawsuit With a Lead Plaintiff Deadline of December 1, 2026 - GOOGL
  https://www.accessnewswire.com/newsroom/en/business-and-professional-services/levi-and-korsinsky-reminds-alphabet-inc.-investors-of-the-pendin-1256419
- Tue 24 Nov | TIKR.com | Alphabet Soars 6% as Jensen Huang’s Return to Nvidia Reignites AI Stocks
  https://www.tikr.com/blog/alphabet-soars-6-as-jensen-huangs-return-to-nvidia-reignites-ai-stocks
- Mon 23 Nov | TIKR.com | Steve Eisman Said AI Was “No Longer One Trade.” Huang Is Back, but Alphabet and CoreWeave Still Show the Split
  https://www.tikr.com/blog/big-shorts-steve-eisman-without-nvidia-ai-is-no-longer-one-trade-alphabet-and-coreweave-show-the-split
- Mon 23 Nov | Investing.com Canada | Form 4 Alphabet Inc Class A For: 23 November By Investing.com
  https://ca.investing.com/news/stock-market-news/form-4-alphabet-inc-class-a-for-23-november-93CH-4976856
## META  (8 leads)
- Tue 24 Nov | The Economic Times | Meta pauses Class C share issuance amid shareholder lawsuit
  http://economictimes.indiatimes.com/tech/technology/meta-pauses-class-c-share-issuance-amid-shareholder-lawsuit/articleshow/136123722.cms
  > Meta Platforms said on Monday it will not issue its planned Class C shares while it faces shareholder litigation challenging the company's proposed recapitalisation, delaying a share sale program intended to help fund its artificial intelligence investments.
- Tue 24 Nov | Blockchain News | Meta Platforms (META) Stock Price Prediction: Bulls Lean on AI Momentum, but the Chart Still Needs Confirmation
  https://blockchain.news/news/20261124-price-prediction-meta-bulls-lean-on-ai-momentum-but
  > What changed for META Meta Platforms (META) is trying to stabilize after a sharp pullback, with the stock at $602.96 and up 3.91% over the latest 24-hour window.
- Tue 24 Nov | Kalkine India | Meta pauses Class C issuance amid shareholder litigation
  https://www.kalkine.co.in/article/technology/meta-platforms-nasdaq-meta-pauses-class-c-share-issuance-during-shareholder-litigation
  > - Meta Platforms Inc. (NASDAQ: META) agreed not to issue Class C shares during specified phases of shareholder litigation. - The consolidated proceedings are scheduled for trial in April 2027 under the disclosed timetable. (NASDAQ: META) has agreed to pause the issuance of proposed Class C shares while shareholder litigation progresses.
- Tue 24 Nov | ad-hoc-news.de | Meta Platforms stock: Class C shares paused, EUR 552.60, up 1.34%
  https://www.ad-hoc-news.de/boerse/news/vorboerse/meta-platforms-stock-class-c-shares-paused-eur-552-60-up-1-34/70548604
  > Meta Platforms said on Monday, November 23, that it will not issue its planned Class C shares while shareholder litigation over the proposed recapitalization proceeds in Delaware. The delay also affects a planned 60 billion US dollar at-the-market share sale intended to help fund artificial-intelligence investments.
- Tue 24 Nov | Investing.com UK | Form 144 Meta Platforms For: 24 November By Investing.com
  https://uk.investing.com/news/stock-market-news/form-144-meta-platforms-for-24-november-93CH-5000727
- Tue 24 Nov | TradingView | AMD Stock Dips Overnight After Nvidia-Triggered Rally: AMD Registers 337M Shares For Resale Tied To OpenAI, Meta Warrants
  https://www.tradingview.com/news/stocktwits:95c3158a0094b:0-amd-stock-dips-overnight-after-nvidia-triggered-rally-amd-registers-337m-shares-for-resale-tied-to-openai-meta-warrants/
- Tue 24 Nov | BigGo Finance | Meta Halts Class C Share Sale as Delaware Suit Delays $60B AI Funding Vehicle
  https://finance.biggo.com/news/c0ec3c83-343f-4e5e-9ce9-b6f8a7193c85
- Tue 24 Nov | TipRanks | Meta’s $60 Billion AI Funding Plan Hits a Roadblock — What It Means for Investors
  https://www.tipranks.com/news/metas-60-billion-ai-funding-plan-hits-a-roadblock-what-it-means-for-investors
## TSLA  (8 leads)
- Tue 24 Nov | Stocktwits | Tesla And SpaceX Reportedly Name 5 Directors To Lead Merger Discussions — Investor Says Talks Are Moving At ‘Warp Speed’
  https://stocktwits.com/news-articles/markets/equity/tesla-spacex-5-directors-lead-merger-discussions-investor-talks-warp-speed/cNbsbrxR9ke
  > Tesla and SpaceX have reportedly moved from exploring a merger to putting a price on a potential share swap, with five directors leading negotiations that investor Larry Goldberg says are moving at “warp speed” toward a decision on what Tesla holders could get.
- Tue 24 Nov | Morningstar | What Happens If Tesla and SpaceX Merge?
  https://global.morningstar.com/en-gb/stocks/what-happens-if-tesla-spacex-merge
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Tue 24 Nov | Startup Fortune | Tesla jumps 11.5% on FSD v15, a release most owners can't use yet
  https://startupfortune.com/tesla-jumps-115-on-fsd-v15-a-release-most-owners-cant-use-yet/
  (page: did not load (404))
- Tue 24 Nov | Pluang | Tesla's revenue shrinks as spending on robotaxis and AI rises; big gains expected only late 2027.
  https://pluang.com/en/news-feed/prediksi-saham-tesla-tertinggal-pasar-2027
  (page: did not load (403))
- Tue 24 Nov | marketscreener.com | SpaceX and Tesla entrusts five directors for merger talks, FT reports
  https://www.marketscreener.com/news/spacex-and-tesla-entrusts-five-directors-for-merger-talks-ft-reports-ce7851dad189f326
- Tue 24 Nov | Financial Times | SpaceX-Tesla: the directors negotiating the biggest merger ever
  https://www.ft.com/content/2585e45e-9133-4215-a2d8-e1275e1033b9?syn-25a6b1a6=1
- Tue 24 Nov | Gotrade | Tesla Stock (TSLA) Rises 11.5% on Reports of a SpaceX Merger (Nov 23)
  https://www.heygotrade.com/en/news/tesla-tsla-stock-news-november-24-2026/
- Tue 24 Nov | Investor's Business Daily | Dow Jones Futures: Tech Stocks, Nvidia Snap Back On Jensen Huang's Return; Elon Musk-Led SpaceX, Tesla Rally
  https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-sp500-nasdaq-nvidia-jensen-huang-elon-musk-spacex-tesla/
## JPM  (8 leads)
- Tue 24 Nov | TradingView | REG - Future PLC JPMorgan Chase & Co - Holding(s) in Company
  https://www.tradingview.com/news/reuters.com,2026-11-24:newsml_RSX4220Ea:0-reg-future-plc-jpmorgan-chase-co-holding-s-in-company/
  > REG - Future PLC JPMorgan Chase & Co - Holding(s) in Company TR-1: Standard form for notification of major holdings JPMorgan Chase & Co.
- Tue 24 Nov | Avi-Go | Four Jets Attributed to JPMorgan Chase Logged 116 Flights Year to Date, With Estimated 2,259 t of CO₂
  https://avi-go.com/news/articles/2d0a6f342ca0faa8e1f4e161405f33cc
  > Four Jets Attributed to JPMorgan Chase Logged 116 Flights Year to Date, With Estimated 2,259 t of CO₂ Why It MattersTracker-based corporate flight and emissions tallies show how public ADS-B data is used to put a figure on corporate aviation's carbon footprint, within the limits of attribution that can change.
- Tue 24 Nov | Yahoo Finance UK | JPMorgan Chase Financial Company LLC Point to Point Worst Of Buffer Note AAJBJXX (AAJBJXX)
  https://uk.finance.yahoo.com/quote/AAJBJXX/profile/
  (page: did not load (404))
## XOM  (8 leads)
- Mon 23 Nov | MarketBeat | ExxonMobil (NYSE:XOM) Stock Price Down 1.8% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-stock-price-down-18-heres-why-2026-11-23/
  > ExxonMobil (NYSE:XOM) Stock Price Down 1.8% - Here's Why - ExxonMobil shares fell 1.8% to $157.18, on trading volume 16% below its average. - Analyst views remain mixed: 12 rate the stock a Buy, 15 a Hold, and one a Sell; the consensus price target is $170.79.
- Mon 23 Nov | EnterpriseAM | Oman signs a gas concession with ExxonMobil that could feed a new 6-9 mtpa LNG plant at Duqm
  https://enterpriseam.com/infrastructure/2026/11/24/oman-signs-a-gas-concession-with-exxonmobil-that-could-feed-a-new-6-9-mtpa-lng-plant-at-duqm/
  > Oman’s new gas concession with ExxonMobil could feed an LNG plant at Duqm. The Energy Ministry signed a concession agreement last week with state-owned Energy Oman and ExxonMobil to develop gas at Greater Makarem (Block 20), Oman News Agency reports.
- Mon 23 Nov | MarketWatch | ExxonMobil Holdings Corp. stock underperforms Monday when compared to competitors
  https://www.marketwatch.com/data-news/exxonmobil-holdings-corp-stock-underperforms-monday-when-compared-to-competitors-fa2c479a-a1aaf06aa864?mod=mw_quote_news
  (page: did not load (401))
## AVGO  (8 leads)
- Tue 24 Nov | Pluang | Tech stocks Micron, Nvidia, and Broadcom offer strong growth potential amid AI chip demand and market dips.
  https://pluang.com/en/news-feed/black-friday-saham-teknologi-ai-yang-bagus-dibeli
  (page: did not load (403))
- Tue 24 Nov | Blockchain News | Broadcom (AVGO) Stock Price Prediction: Broadcom loses short-term momentum as analysts stay constructive
  https://blockchain.news/news/20261124-price-prediction-avgo-broadcom-loses-short-term-momentum-as
  > Price action: a pullback inside a larger reset Broadcom (AVGO) closed the latest session at $312.42, with a 24-hour range of $325.90 to $304.34 and trading volume of $78.6 million on Binance Futures.
- Tue 24 Nov | ad-hoc-news.de | Broadcom's Split Verdict: Wall Street Trims Targets While Bernstein Backs the AI Franchise
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/broadcom-s-split-verdict-wall-street-trims-targets-while-bernstein-backs-the-ai-franchise/70548081
  > Bernstein Research has doubled down on Broadcom as its top pick among US chipmakers, arguing that the recent pullback across AI-linked equities has gone too far given these companies' exposure to cloud data-center spending. Analyst Mark Newman's team reiterated an "Outperform" rating and a $575 price target on the stock.
- Mon 23 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Shares Up 3% - Should You Buy?
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-shares-up-3-should-you-buy-2026-11-23/
  > Broadcom (NASDAQ:AVGO) Shares Up 3% - Should You Buy? - Broadcom shares rose 3% to $313.55 in heavy trading, with volume about 60% above its average; a broader semiconductor rally and optimism about AI spending supported the move.
- Mon 23 Nov | MarketWatch | Broadcom Inc. stock rises Monday, still underperforms market
  https://www.marketwatch.com/data-news/broadcom-inc-stock-rises-monday-still-underperforms-market-bcd38cd0-8a220e9b613c?mod=mw_quote_news
- Mon 23 Nov | TradingKey | Broadcom Inc Stock (AVGO) Closed Up by 3.00% on Nov 23: Drivers Behind the Movement
  https://www.tradingkey.com/news/market-movers/262318798-market-movers-avgo-20261123
- Mon 23 Nov | FinanceFeeds | Broadcom Stock Rebounds 1.8% After 12% Drop on TPU Cut
  https://financefeeds.com/broadcom-avgo-stock-rebounds-2-as-nvidia-rally-eases-google-tpu-selloff/
- Mon 23 Nov | Yahoo Finance | Why Did Broadcom Stock Drop On Friday?
  https://finance.yahoo.com/markets/stocks/articles/why-did-broadcom-stock-drop-190504586.html
## BRK.B  (8 leads)
- Tue 24 Nov | The Mac Observer | Berkshire Hathaway Keeps a Quarter of Its Investments in Apple
  https://www.macobserver.com/news/berkshire-hathaway-keeps-a-quarter-of-its-investments-in-apple/
  > Financial giant Berkshire Hathaway has hit pause on selling its Apple shares, even while actively reshuffling the rest of its major stock holdings. Under new CEO Greg Abel, the firm kept its entire stake intact through the first three quarters of 2026.
- Tue 24 Nov | AOL.com | If a Stock Market Crash Is Coming, Warren Buffett Says This Is the Best Move Investors Should Make
  https://www.aol.com/articles/stock-market-crash-coming-warren-012002000.html
  > - Euphoria for artificial intelligence (AI) stocks has pushed stock market valuations to historically elevated levels. - History shows that major indexes always recover from stock market crashes. - Warren Buffett's investment strategy emphasizes patience, diversification, and staying invested through volatility.
- Mon 23 Nov | BigGo Finance | Berkshire Stock Outpaces Tech as AI Sell-Off Spurs Safe-Haven Bets
  https://finance.biggo.com/news/eb2e17e5-0cac-4888-8db8-ffd467f8f900
  > Berkshire Stock Outpaces Tech as AI Sell-Off Spurs Safe-Haven Bets Berkshire Hathaway (BRKB) has turned into one of the more quietly watched names on Wall Street as a technology-led slump pushes investors toward defensive corners of the market. [Figures on the page: first half; one quarter. Check which one each figure is.]
## WMT  (8 leads)
- Tue 24 Nov | Scripps News | Walmart shoppers stock up on water, propane amid recent disruptions
  https://www.scrippsnews.com/us-news/walmart-shoppers-stock-up-on-water-propane-amid-recent-disruptions
  > With a growing number of technology outages and disruptions making headlines, some Americans are apparently getting ready for the unexpected. Walmart says shoppers have been stocking up on things like bottled water, propane and camping gear. - Water: one gallon per person, per day (3-day supply for evacuation, 2-week supply for home)
- Tue 24 Nov | TIKR.com | Target Has “Out-Comped Walmart Three Quarters in a Row.” Walmart Still Trades at More Than 2x Its Multiple
  https://www.tikr.com/blog/target-has-out-comped-walmart-three-quarters-in-a-row-walmart-still-trades-at-more-than-2x-its-multiple
  > - Target’s comparable sales rose 5.6% last quarter on 5.0% more traffic, while Walmart’s U.S. comps rose 2.9% and its in-store sales fell again. - Walmart still trades at 41x forward earnings, more than twice Target’s 17x, while Costco trades at 48x and Kroger at 13x.
- Mon 23 Nov | Around Prague | What Stores Are Open on Thanksgiving 2026? Walmart, Target, Costco and Black Friday Hours
  https://aroundprague.cz/en/news/us/what-stores-are-open-on-thanksgiving-2026-walmart-target-costco-and-black
  (page: did not load (403))
## V  (8 leads)
- Tue 24 Nov | Investing.com | Visa president of technology sells $1.62 million in stock
  https://www.investing.com/news/insider-trading-news/visa-president-of-technology-sells-162-million-in-stock-93CH-5047063
  (page: did not load (403))
- Tue 24 Nov | Investing.com UK | Form 4 Visa Inc: Chris Suh (CFO) For: 19 November By Investing.com
  https://uk.investing.com/news/stock-market-news/form-4-visa-inc-chris-suh-cfo-for-19-november-93CH-5000715
  (page: did not load (403))
- Tue 24 Nov | GuruFocus | Visa (V) Grants $50 Million Performance Stock Option to CEO Ryan McInerney
  https://www.gurufocus.com/news/9216176/visa-v-grants-50-million-performance-stock-option-to-ceo-ryan-mcinerney
  (page: did not load (403))
## ORCL  (8 leads)
- Tue 24 Nov | Blockchain News | Oracle (ORCL) Stock Price Prediction: Rebound Attempt Faces Heavy Overhead Supply
  https://blockchain.news/news/20261124-price-prediction-orcl-rebound-attempt-faces-heavy-overhead-supply
  > What the tape is saying Oracle (ORCL) is priced at $114.21, up 8.21% on the day, after trading between $104.89 and $118.82. That puts the stock back above its 7-day SMA of $109.41 and just above its 12-day EMA of $113.66, but still below the 20-day SMA at $116.54 and the 50-day SMA at $126.08.
- Tue 24 Nov | Simply Wall St | Nvidia Rally Puts Oracle And Palantir Stock Back In Focus
  https://simplywall.st/stocks/cn/semiconductors/shse-688041/hygon-information-technology-shares/news/nvidia-rally-puts-oracle-and-palantir-stock-back-in-focus
  > A single management change at Nvidia has just swung nearly US$1 trillion of market value and reignited belief in AI as a story investors care about again. Relief rallies like this can reset sentiment and reorder which companies investors gravitate toward and which get left behind.
- Tue 24 Nov | The Times of India | Larry Ellison loses $10 billion-plus; knocked out of the world's 10-richest men list after Oracle stock f
  https://timesofindia.indiatimes.com/technology/tech-news/larry-ellison-loses-10-billion-plus-knocked-out-of-the-worlds-10-richest-men-list-after-oracle-stock-falls-to-2-year-low-heres-what-triggered-massive-wipe-out/articleshow/
  > Oracle co-founder Larry Ellison has suffered a wealth wipeout of nearly $11 billion after a sharp decline in Oracle’s share price sent his net worth tumbling and pushed him out of the worlds top 10 richest people, according to a report by Fortune citing Bloomberg data.
- Mon 23 Nov | GuruFocus | Oracle Corp (ORCL) Shares Surge 12.3% -- What GF Score of 88 Tel
  https://www.gurufocus.com/news/9215826/oracle-corp-orcl-shares-surge-123-what-gf-score-of-88-tells-investors
  (page: did not load (403))
- Mon 23 Nov | MarketBeat | Oracle (NYSE:ORCL) Shares Up 12.6% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-up-126-heres-what-happened-2026-11-23/
- Mon 23 Nov | 재경일보 | Oracle Shares Jump 12.3% as Tech Stocks Rally on Nvidia Leadership News and Contract Funding
  https://news.jkn.co.kr/editions/english/post/1117602
- Mon 23 Nov | MarketWatch | Oracle and CoreWeave stocks stage big gains as investors bet the AI cash will keep flowing
  https://www.marketwatch.com/story/oracle-and-coreweave-stocks-stage-big-gains-as-investors-bet-the-ai-cash-will-keep-flowing-eeb1aa85
- Mon 23 Nov | Investing.com Australia | Why is Oracle stock surging today? By Investing.com
  https://au.investing.com/news/stock-market-news/why-is-oracle-stock-surging-today-93CH-4790802
## COST  (8 leads)
- Tue 24 Nov | Yahoo Finance | Costco Wholesale (COST) Could Be 27% Overvalued After Its $30 Special Dividend
  https://finance.yahoo.com/markets/stocks/articles/costco-wholesale-cost-could-27-043132200.html
  > Costco Wholesale (COST) has put cash returns in the spotlight after its board declared a special cash dividend of US$30 per share, a US$13.3b payout scheduled for early December. The special dividend lands on a stock that has already had a strong run.
- Tue 24 Nov | Tasting Table | Other Than Food Court Hot Dog Combos And Free Samples, Costco Shoppers Love Having Less Of This In The Aisles
  https://www.tastingtable.com/2319798/costco-shoppers-aisles-choices/
  > Other Than Food Court Hot Dog Combos And Free Samples, Costco Shoppers Love Having Less Of This In The Aisles In an era of online shopping where a seemingly endless variety of products are at our fingertips, the idea that any business would actually benefit from a limited selection seems counter intuitive.
- Mon 23 Nov | Benzinga | If You Invested $1000 In Costco Wholesale Stock 15 Years Ago, You Would Have This Much Today
  https://www.benzinga.com/news/26/11/63567080/if-you-invested-1000-costco-wholesale-stock-15-years-ago-you-would-have-much-today
  (page: did not load (403))
## NFLX  (8 leads)
- Mon 23 Nov | Yahoo Finance | Netflix Cuts About 1,000 Jobs and Its Content Chief. YouTube Already Has Twice Its TV Share
  https://finance.yahoo.com/media-advertising/articles/netflix-cuts-1-000-jobs-233146304.html
  > - Netflix fired its chief content officer and about 1,000 employees in October as its growth slows. - YouTube took 15.8% of US TV time in August, more than twice Netflix's 7.7%, with Disney's and Amazon's streaming apps well behind.
- Mon 23 Nov | Yahoo Finance | How Investors May Respond To Netflix (NFLX) Big Investors Split
  https://finance.yahoo.com/markets/stocks/articles/investors-may-respond-netflix-nflx-232426716.html
  > - Netflix faces renewed scrutiny as high-profile investors Bill Ackman and Michael Burry take opposing valuation stances while the business manages slowing revenue growth, softer advertising expectations and potential live sports content costs.
- Mon 23 Nov | Benzinga | Here’s How Much You Would Have Made Owning Netflix Stock In The Last 10 Years
  https://www.benzinga.com/news/26/11/63566520/here-s-how-much-you-would-have-made-owning-netflix-stock-last-10-years
  (page: did not load (403))
- Mon 23 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Shares Climb 2.4% - Here's What Happened
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-shares-climb-24-heres-what-happened-2026-11-23/
  > Netflix (NASDAQ:NFLX) Shares Climb 2.4% - Here's What Happened - Netflix shares rose 2.4% to $58.10, with trading volume 11% above its daily average.
- Mon 23 Nov | Simply Wall St | Netflix (NFLX) Falls 38% This Year, Is It Now A Bargain?
  https://simplywall.st/stocks/us/media/nasdaq-nflx/netflix/news/netflix-nflx-falls-38-this-year-is-it-now-a-bargain
- Mon 23 Nov | Yahoo Finance | Bill Ackman Likes Netflix Under $60. Michael Burry Is Waiting for the High $30s. Who’s Right?
  https://finance.yahoo.com/markets/stocks/articles/bill-ackman-likes-netflix-under-192858588.html
- Mon 23 Nov | Foreign Policy Journal | Nvidia (NASDAQ: NVDA), Netflix (NASDAQ: NFLX), and Oracle (NYSE: ORCL) Shed Billions As Leadership Chaos, Debt, And Slowing Growth Converge
  https://www.foreignpolicyjournal.com/2026/11/23/nvidia-nasdaq-nvda-netflix-nasdaq-nflx-and-oracle-nyse-orcl-shed-billions-as-leadership-chaos-debt-and-slowing-growth-converge/
- Mon 23 Nov | SuaraGarut.ID | Netflix Shares Hit Yearly Low as Michael Burry Targets $30s
  https://suaragarut.id/en/netflix-shares-michael-burry-valuation
## INTC  (8 leads)
- Tue 24 Nov | blockchain.news | Intel (INTC) Stock Price Prediction: Q3 execution improves, but the chart still needs confirmation
  https://blockchain.news/news/20261124-price-prediction-intc-q3-execution-improves-but-the-chart
  > Q3 growth gave the stock something to work with Intel’s latest reported catalyst is the third quarter of 2026. The company said revenue rose to $16.5 billion, up 21% year over year, with EPS of $0.60 and non-GAAP EPS of $0.52.
- Tue 24 Nov | Simply Wall St | Intel (INTC) Shares Jumped, What Is Behind The Latest Move?
  https://simplywall.st/stocks/us/semiconductors/nasdaq-intc/intel/news/intel-intc-shares-jumped-what-is-behind-the-latest-move
  > Intel (INTC) is back in focus after two related wins in AI infrastructure. The stock is reacting to a new external 18A-P foundry customer and a long-term Microsoft Azure agreement involving Xeon and EMIB packaging.
- Tue 24 Nov | Willamette Week | Lawsuit Adds Insult to Injury for Struggling Intel
  https://www.wweek.com/news/2026/11/23/lawsuit-adds-insult-to-injury-for-struggling-intel/
  > Intel’s rough year continues with a possible securities class action lawsuit over the company’s falling stock. This year, the tech giant—Oregon’s largest for-profit employer—has contended with a global slowdown in personal computer sales and a resulting buildup of inventory.
- Mon 23 Nov | GuruFocus | Intel Corp (INTC) Stock Up 16.3% but GF Value Says Overvalued -- GF Score: 68/100
  https://www.gurufocus.com/news/9215828/intel-corp-intc-stock-up-163-but-gf-value-says-overvalued-gf-score-68100
  (page: did not load (403))
- Mon 23 Nov | MarketBeat | Intel (NASDAQ:INTC) Shares Climb 16.3% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-intel-nasdaq-intc-shares-climb-163-heres-why-2026-11-23/
- Mon 23 Nov | Quantisnow | Intel's 16% jump mostly tracked the chip rebound
  https://www.quantisnow.com/articles/intel-16-1-percent-jump-nov-23-tracked-chip-sector-no-intel-specific-news
- Mon 23 Nov | Kalshi News | Perps roundup: Jensen Huang's return lifts Dell, SK Hynix, Micron, and Intel
  https://news.kalshi.com/p/perps-roundup-jensen-huang-return-fuels-market-recovery
- Mon 23 Nov | Yahoo Finance | Intel Corporation to Participate in Upcoming Investor Conferences
  https://finance.yahoo.com/technology/articles/intel-corporation-participate-upcoming-investor-213000154.html
## LLY  (8 leads)
- Tue 24 Nov | 재경일보 | Eli Lilly Targets Oncology After Obesity Success with 8 Pipeline Candidates Launching Within 5 Years
  https://news.jkn.co.kr/editions/english/post/1119140
  > Eli Lilly and Company, the U.S. pharmaceutical firm that has grown through its obesity treatments, is securing eight oncology drugs that could launch within the next five years, making the cancer business a new pillar of growth.
- Tue 24 Nov | TradingView | Biotech Loses Ground In November’s Market Slide — These 5 Stocks Bucked The Selloff As Lilly, AbbVie And Amgen Fell
  https://www.tradingview.com/news/stocktwits:095f578cb094b:0-biotech-loses-ground-in-november-s-market-slide-these-5-stocks-bucked-the-selloff-as-lilly-abbvie-and-amgen-fell/
  > Biotech Loses Ground In November’s Market Slide — These 5 Stocks Bucked The Selloff As Lilly, AbbVie And Amgen Fell - VCEL led the five stocks with a 47% November gain after stronger knee implant and burn-care sales prompted it to raise its annual revenue forecast. - IRWD climbed 41% as U.S. [Figures on the page: unaudited or preliminary; nine months; first half; one quarter. Check which one each figure is.]
- Tue 24 Nov | Kalkine | Loftus Peak Global Disruption Hedged Active ETF Discloses October 2026 Portfolio with Eli Lilly at 8.34%
  https://kalkine.com.au/news/announcements/loftus-peak-global-disruption-hedged-active-etf-discloses-october-2026-portfolio-with-eli-lilly-at-834
  (page: did not load (403))
Read 75 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ALCN, EAST, EFIH, EMFD, AMOC, SKPC.
