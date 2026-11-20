# Desk brief, Friday, November 20, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 286s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-19 (28.44); Treasury yields to 2026-11-19 (10-year 5.04%).
- **valuation**: ok in 25s (GitHub Actions). LLY: $1.27tn, P/E (last 12 months) 42.3, Forecast P/E (fiscal 2026) 37.9 (the four quarters to Sep 2026)
- **movers**: ok in 23s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-03 TSLA results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 48 series; EGX30 turning down, RSI 49.7
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 53 stocks, k 16.3%, median P/E 10.0; cheapest MASR +74%, PHAR +46%, ABUK +43%; dearest ARAB -62%, MOIN -66%, BTFH -67%
- **views**: ok in 0s (GitHub Actions). 2026-11-11-value-basket: open -> on track
- **results**: ok in 54s (GitHub Actions). 
- **news**: ok in 131s (GitHub Actions). 
- **leads**: ok in 100s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 3 needed a retry.

## What moved (latest close against the one before)
- EGX30 51,458.00 (-0.17%); EGX70 EWI 17,505.80 (-0.33%); USD/EGP 53.88 (+0.16%); Gold 21K 5,675.00 (-1.30%); Brent 91.98 (+0.03%); S&P 500 7,175.83 (-2.02%); Nasdaq 23,879.20 (-2.25%); Bitcoin 61,523.00 (-3.20%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): AMZN -3.9%, ETEL -3.5%, GOOGL -3.5%, NVDA -3.3%, META -3.3%, V -3.1%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - AAPL: In an uptrend: above its 50-day average, which is above the 200-day; RSI 53, neither stretched nor washed out; momentum turned down today (MACD crossed its signal line).
    - NVDA: Turning down: below both its 50-day average (30.1% under) and its 200-day (28.3% under), though the 50-day is still above the 200-day; RSI 20, washed out: below 30.

## Movers that still need a reason (top five each way, 5% or more)
- EGX ZEOT (Extracted Oils & Derivatives) +17.0%; EGX MOSC (Misr Oils & Soap) +12.0%; EGX VERT (Vertika for Industry & Trade) +10.0%; EGX COSG (Cairo Oils & Soap) +9.3%; EGX FIRE (First Investment & Real Estate Development) +8.2%; EGX ADRI (Arab Development & Real Estate Investment) -5.1%; EGX ICFC (International Co. for Fertilizers & Chemicals) -5.0%; US INSM (Insmed Incorporated) +20.6%; US TU (TELUS) +13.4%; US PANW (Palo Alto Networks) +6.4%; US OKTA (Okta) +5.7%; US NTSK (Netskope) +5.5%; US WSM (Williams-Sonoma) -15.2%; US ZM (Zoom Communications) -9.6%; US NBIS (Nebius Group) -9.4%; US PS (Pershing Square) -9.3%; US TWLO (Twilio) -8.8%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-19 (TradingView's closes; Mubasher's list refused), 200 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (212)
US: 2026-11-19, 818 companies
US week and month: US companies worth $10bn or more (816)
EGX30 heatmap: 2026-11-19, 31 members
US heatmap: 2026-11-19, 100 members
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

# US 2026-11-19
## INSM +20.6%  Insmed Incorporated
- Fri 20 Nov | Yahoo Finance | Insmed (INSM) is Attracting Investor Attention — Here’s Why
  https://finance.yahoo.com/markets/stocks/articles/insmed-insm-attracting-investor-attention-053143346.html
  > (NASDAQ:INSM) is one of the 10 Stocks Posting Monster Gains Amid Market Downfall. Shares of Insmed Inc.
- Thu 19 Nov | Proactive financial news | Market movers: Anthropic, AMD, Cohere, Insmed...
  https://www.proactiveinvestors.com/companies/news/1102147/market-movers-anthropic-amd-cohere-insmed-1102147.html
  > Market movers: Anthropic, AMD, Cohere, Insmed... Published: 14:20 19 Nov 2026 EST At about 12:10 pm ET, AMD was trading at $483.59, down $46.55, or 8.78%, from its previous close of $530.14.
- Thu 19 Nov | Seeking Alpha | Insmed may be worth $170 to $210 a share in takeover, analyst
  https://seekingalpha.com/news/4674846-insmed-may-be-worth-170-to-210-a-share-in-takeover-analyst
  (page: did not load (403))
- Thu 19 Nov | BigGo Finance | Sanofi Weighs Takeover of Insmed; INSM Stock Surges 21% in Biggest Day Since August
  https://finance.biggo.com/news/d4ee5a26-ece1-4718-8346-08a3b962ecec
  (page: did not load (URLError))
## TU +13.4%  TELUS
- Thu 19 Nov | MarketWatch | TELUS Corp. stock rises Thursday, outperforms market
  https://www.marketwatch.com/data-news/telus-corp-stock-rises-thursday-outperforms-market-4af274b7-8c05ef0b2f4b?mod=mw_quote_news
  (page: did not load (401))
- Thu 19 Nov | Kalkine Media | Why Did TELUS (TSX:T) Emerge Among Advancing Canadian Stocks?
  https://kalkinemedia.com/ca/stocks/communication/why-did-telus-tsxt-emerge-among-advancing-canadian-stocks
  > - TELUS advanced during a session in which the Toronto market closed substantially lower. - Telecom and a long dividend record can attract during resource. TELUS came into focus. TELUS advanced during the session even as the Toronto market closed substantially lower.
- Thu 19 Nov | Rich Picks Daily | Quebecor (TSX: QBR.B) proposes TELUS combination valued at $19.45 a sh…
  https://richtv.io/news/quebecor-tsx-qbrb-proposes-telus-combination-valued-at-1945-a-share
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Traders Union | Quebecor takeover bid fuels TELUS stock upward price move
  https://tradersunion.com/news/stocks/show/4324612-telus-jumps-9-98percent-on-takeover/
  (page: did not load (403))
## PANW +6.4%  Palo Alto Networks
- Fri 20 Nov | MarketBeat | 148,433 Shares in Palo Alto Networks, Inc. $PANW Purchased by Advisors Asset Management Inc.
  https://www.marketbeat.com/instant-alerts/filing-148433-shares-in-palo-alto-networks-inc-panw-purchased-by-advisors-asset-management-inc-2026-11-20/
  > 148,433 Shares in Palo Alto Networks, Inc. $PANW Purchased by Advisors Asset Management Inc. - Advisors Asset Management opened a substantial position in Palo Alto Networks, buying 148,433 shares worth about $59.0 million in the third quarter. Institutional investors and hedge funds collectively own 79.82% of the company’s stock.
- Fri 20 Nov | Yahoo Finance | Palo Alto (PANW) Is Turning Heads Again. Here’s Why
  https://finance.yahoo.com/markets/stocks/articles/palo-alto-panw-turning-heads-022336090.html
  > Palo Alto Networks Inc. (NASDAW:PANW) is one of the 10 Stocks Posting Monster Gains Amid Market Downfall.
- Thu 19 Nov | Simply Wall St | Palo Alto Networks (PANW) Stock Rallies After Q1 Earnings Revive Profit Story
  https://simplywall.st/stocks/us/software/nasdaq-panw/palo-alto-networks/news/palo-alto-networks-panw-stock-rallies-after-q1-earnings-revi
  > Palo Alto Networks just put Q1 2027 on the board with a sharp rebound in profitability, and traders wasted no time. The stock jumped 6.4% on Thursday to about US$361 after the release, a strong move for a large cybersecurity player.
- Thu 19 Nov | Yahoo Finance | Palo Alto Networks (PANW) Stock Jumps As Q1 Results Boost ARR Confidence
  https://finance.yahoo.com/markets/stocks/articles/palo-alto-networks-panw-stock-231511575.html
  > Palo Alto Networks stock jumped 6.4% to about US$361 after the Q1 FY27 release, a sharp move for a large cybersecurity company that already trades on rich expectations. The quarter just reported delivered a clear headline.
## OKTA +5.7%  Okta
- Fri 20 Nov | MarketBeat | Okta (NASDAQ:OKTA) Stock Crosses Above 50-Day Moving Average - What's Next?
  https://www.marketbeat.com/instant-alerts/price-okta-nasdaq-okta-stock-crosses-above-50-day-moving-average-whats-next-2026-11-20/
  > Okta (NASDAQ:OKTA) Stock Crosses Above 50-Day Moving Average - What's Next? - Okta shares rose 5.7% and moved above their 50-day moving average of $199.56, reaching an intraday high of $214.89 before last trading at $206.85.
- Fri 20 Nov | MarketBeat | Okta, Inc. (OKTA) - What Are Researchers Saying About This Stock?
  https://www.marketbeat.com/instant-alerts/consensus-okta-inc-okta-what-are-researchers-saying-about-this-stock-2026-11-20/
  > (OKTA) - What Are Researchers Saying About This Stock? - Analysts are broadly positive: Forty-three analysts rate Okta a “Moderate Buy,” with 31 buy and two strong-buy ratings; the average 12-month price target is $203.67.
- Fri 20 Nov | GuruFocus | COFG Advisors, LLC's Okta Inc(OKTA) Holding History
  https://www.gurufocus.com/guru-portfolio/COFG Advisors, LLC/OKTA
  (page: did not load (403))
- Thu 19 Nov | Global Banking & Finance Review | Okta rises 5.75% in Thursday's session
  https://www.globalbankingandfinance.com/okta-okta-rises-2026-11-19/
## NTSK +5.5%  Netskope
- Thu 19 Nov | Yahoo! Finance Canada | Netskope, Inc. (NTSK) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/NTSK/
  > NasdaqGS - Nasdaq Real Time Price  USD       Netskope, Inc. - Previous Close  23.50 - Day's Range  24.25 - 26.45 - 52 Week Range  7.66 - 26.71 - Market Cap (intraday)  10.133B - Beta (5Y Monthly) -- - 1y Target Est  --
- Thu 19 Nov | kalkine.ca | Why Did Netskope (NASDAQ:NTSK) Rise About 10% Following a Cloud Security Rival's Solid Quarter?
  https://kalkine.ca/news/technology/why-did-netskope-nasdaqntsk-rise-about-10-following-a-cloud-security-rivals-solid-quarter
  (page: did not load (403))
- Thu 19 Nov | Trefis | Why Did Netskope Stock Move?
  https://www.trefis.com/stock/ntsk/articles/626890/why-did-netskope-stock-move/2026-11-19
  > Why Did Netskope Stock Move? Today’s big story: Could Anthropic Stock Fall 25%? Shares of Netskope (NTSK) rose 12.7% on Wednesday, November 18, 2026, while the S&P 500 slipped 0.2%. Of the 28 other systems software companies worth $2 billion or more, 23 rose.
- Thu 19 Nov | Trefis | Could You Have Spotted Netskope Stock’s Doubling Early?
  https://www.trefis.com/stock/ntsk/articles/626953/could-you-have-spotted-netskope-stocks-doubling-early/2026-11-19
  > Could You Have Spotted Netskope Stock’s Doubling Early? Today’s big story: Could Anthropic Stock Fall 25%? Netskope (NTSK) stock turned $10,000 into about $20,000 between May 20 and November 18, 2026, while the S&P 500 slipped 0.9%. [Figures on the page: first half; one quarter. Check which one each figure is.]
## WSM -15.2%  Williams-Sonoma
- Fri 20 Nov | MarketBeat | Advisors Asset Management Inc. Acquires 152,248 Shares of Williams-Sonoma, Inc. $WSM
  https://www.marketbeat.com/instant-alerts/filing-advisors-asset-management-inc-acquires-152248-shares-of-williams-sonoma-inc-wsm-2026-11-20/
  > Advisors Asset Management Inc. Acquires 152,248 Shares of Williams-Sonoma, Inc. - Advisors Asset Management opened a new Williams-Sonoma position, buying 152,248 shares worth about $34.7 million, or roughly 0.13% of the company.
- Fri 20 Nov | Yahoo! Finance Canada | Williams-Sonoma, Inc. (WSM) Stock Forecasts
  https://ca.finance.yahoo.com/research/reports/MS_0P000005YF_AnalystReport_1795136071000
  (page: only 4 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 20 Nov | TIKR.com | Williams-Sonoma Sinks 14% as Q3 Falls Just Short of Estimates and Full-Year Outlook Stays Put
  https://www.tikr.com/blog/williams-sonoma-sinks-14-as-q3-falls-just-short-of-estimates-and-full-year-outlook-stays-put
  > - Williams-Sonoma fell 14% after its third-quarter results came in just below estimates and it only reiterated its fiscal 2026 outlook. - Excluding a one-time tariff refund, gross margin barely moved as higher oil prices raised supply-chain costs.
- Thu 19 Nov | Yahoo Finance | How to Earn $500 a Month From Williams-Sonoma Stock Ahead of Q3 Earnings
  https://finance.yahoo.com/markets/stocks/articles/earn-500-month-williams-sonoma-223005409.html
  > Benzinga and Yahoo Finance LLC may earn commission or revenue on some items through the links below. will release its third-quarter earnings report before the opening bell on Thursday, Nov.
## ZM -9.6%  Zoom Communications
- Fri 20 Nov | MarketBeat | Zoom Communications (NASDAQ:ZM) Stock Price Crosses Below 200-Day Moving Average Following Analyst Downgrade
  https://www.marketbeat.com/instant-alerts/price-zoom-communications-nasdaq-zm-stock-price-crosses-below-200-day-moving-average-following-analyst-downgrade-2026-11-19/
  > Zoom Communications (NASDAQ:ZM) Stock Price Crosses Below 200-Day Moving Average Following Analyst Downgrade - Zoom shares fell below their 200-day moving average of $92.26, touching $83.50 and last trading at $83.82, after BTIG lowered its price target from $125 to $115 while maintaining a Buy rating.
- Thu 19 Nov | MarketWatch | Zoom Communications Inc. stock falls Thursday, underperforms market
  https://www.marketwatch.com/data-news/zoom-communications-inc-stock-falls-thursday-underperforms-market-4367aaab-49bc3d2d0934?mod=goog_fin_scmw
  (page: did not load (401))
- Thu 19 Nov | Stock Titan | Zoom (ZM) president reports four stock grant holdings, the largest tied to 107,638 Class A shares.
  https://www.stocktitan.net/sec-filings/ZM/form-3-zoom-communications-inc-initial-statement-of-beneficial-owners-680c7dca94e3.html
  > Zoom: Graeme Lambourne Geddes reports 4 stock grants Sentiment and the balance of points Rhea-AI Sentiment reads the wording of the document, how positive or negative its language is on a 1 to 5 scale.
- Thu 19 Nov | MarketBeat | Zoom Communications (NASDAQ:ZM) Stock Price Down 7.1% After Analyst Downgrade
  https://www.marketbeat.com/instant-alerts/price-zoom-communications-nasdaq-zm-stock-price-down-71-after-analyst-downgrade-2026-11-19/
  > Zoom Communications (NASDAQ:ZM) Stock Price Down 7.1% After Analyst Downgrade - Zoom shares fell 7.1% after BTIG cut its price target from $125 to $115, while maintaining a Buy rating; the stock traded near $86.
## NBIS -9.4%  Nebius Group
- Fri 20 Nov | Blockchain News | Nebius Group (NBIS) Stock Price Prediction: Breakdown tests support after Reuters flagged a 2026 revenue reset
  https://blockchain.news/news/20261120-price-prediction-nbis-breakdown-tests-support-after-reuters-flagged
  > Revenue guidance hit the tape first Nebius Group (NBIS) is trading on a very different setup after Reuters reported on November 12, 2026 that the company reduced its 2026 revenue forecast because of delays at third-party capacity additions.
- Fri 20 Nov | TradingView | Nebius Group N.V. Stock 12‑Month Price Target Cut to $239.52, Implies 147% Upside
  https://www.tradingview.com/news/tradingview:821aa87ee1102:0-nebius-group-n-v-stock-12-month-price-target-cut-to-239-52-implies-147-upside/
  > Stock 12‑Month Price Target Cut to $239.52, Implies 147% Upside Less than 1 min read - According to estimates from 21 analysts, Nebius Group N.V. stock's average price target has fallen from $241.18 to $239.52, with forecasts ranging from $84 to $395 per share
- Thu 19 Nov | Global Banking & Finance Review | Nebius Group falls 8.24% in Thursday's session
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
- 2026-11-20 CLHO results (expected)
- 2026-11-20 EAST results (expected)  <- write its preview
- 2026-11-20 EFID results (expected)
- 2026-11-20 EFIH results (expected)  <- write its preview
- 2026-11-20 JUFO results (expected)
- 2026-11-20 PHDC results (expected)
- 2026-11-24 COST dividend

## Views
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (open)
- due 2026-11-26: The pound stays firmer than EGP 56 per dollar into the IMF review (on track)
- due 2026-11-20: Brent stays below $105 while Iran talks continue (on track)
    2026-11-11-value-basket: open -> on track

## Fair value
- Changed since the last run: ABUK +48% -> +43% (low -> medium); ETEL +10% -> +20% (medium -> medium).
- In the ten cheapest or dearest with no note: ADIB, MCQE, CSAG, EMFD, MTIE, AMOC, LCSW, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-20. Open each story before using it.
## COMI  (8 leads)
- Fri 20 Nov | فيتو | شروط إصدار دفاتر الشيكات على الحساب الجاري في بنك CIB
  https://www.vetogate.com/5774285
  > شروط إصدار دفاتر الشيكات على الحساب الجاري في بنك CIB يبحث العديد من عملاء البنك التجاري الدولي CIB عن شروط إصدار دفاتر شيكات من الحساب الجاري. وقال مسؤلو البنك: إن هناك إمكانية استخراج دفتر شيكات بشرط وجود حد أدنى 25 ألف جنيه مصري في الحساب الجاري.
- Thu 19 Nov | بنكي | شهادة 3 سنوات عائد متغير — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cds/21
  > شهادة 3 سنوات عائد متغير شهادة متغيرة العائد تقدم حاليًا 20.25% عند صرف العائد يوميًا و20.50% عند صرفه شهريًا، مع حد أدنى منخفض يبدأ من 1,000 جنيه وإمكانية الاقتراض بضمانها حتى 95% من قيمتها. - 20.25% – 20.5% - يومي 20.25% · شهري 20.5% | 180 | 2.5% | السنة الأولى (بعد ٦ شهور) |
- Thu 19 Nov | بنكي | بطاقة Swype 12 — البنك التجاري الدولي-CIB
  https://www.bankygate.com/products/cards/416
  > تعد بطاقة Swype 12 خيارًا مناسبًا للعملاء الذين يرغبون في تقسيط المشتريات على فترة قصيرة نسبيًا مع الاستفادة من عدم وجود رسوم إصدار أو تجديد. - معدل الفائدة السنوي الفعلي 24 عرض ساري على البطاقة تقسيط بدون فوائد 13 · خصومات 12 · 11 بينتهوا خلال أيام
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
  https://www.masrawy.com/sports/sports_news/details/2026/11/19/3081357/المصرية-للاتصالات-يهزم-الترسانة-في-عقر-داره-ويرتقي-بجدول-الترتيب?utm_source=article-share&utm_medium=social
  > حقق فريق المصرية للاتصالات (وي) فوزًا مهمًا على حساب منافسه الترسانة بنتيجة 2-1، في المباراة التي جمعت الفريقين اليوم الخميس، ضمن منافسات الجولة الثالثة عشرة من دوري المحترفين المصري.
- Thu 19 Nov | تحيا مصر | تامر المهدي: المصرية للاتصالات تنفذ بنية تكنولوجية متطورة بمشروع نيفيرا
  https://www.tahiamasr.com/1107431
  (page: did not load (403))
- Thu 19 Nov | إقرأ نيوز | المصرية للاتصالات: التكنولوجيا تسهِّل حياة سكان «نيفيرا» وتساعد المستثمرين
  https://www.iqraa.news/236209/المصرية-للاتصالات-التكنولوجيا-تسهِّ/
  > قال المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، إن الشركة ستعمل مع كل مستثمر في مشروع «نيفيرا» منذ مرحلة التصميم لاختيار الحلول التكنولوجية التي تتناسب مع احتياجاته وطبيعة نشاطه.
- Thu 19 Nov | إقرأ نيوز | المصرية للاتصالات تبني شبكة ألياف ضوئية تغطي «نيفيرا» بالكامل
  https://www.iqraa.news/236197/المصرية-للاتصالات-تبني-شبكة-ألياف-ضوئ/
  > قال المهندس تامر المهدي، العضو المنتدب والرئيس التنفيذي للشركة المصرية للاتصالات، إن الشركة تشارك في مشروع «نيفيرا» بصفتها شريك الاتصالات والتكنولوجيا، وستتولى بناء شبكة ألياف ضوئية تغطي كامل مساحة المدينة، التي تبلغ نحو 36 مليون متر.
- Wed 18 Nov | بوابة الشروق | المصرية للاتصالات: إنشاء شبكة ألياف ضوئية تغطي مدينة نيفيرا بالكامل
  https://www.shorouknews.com/mobile/news/view.aspx?cdate=19112026&id=b037cb4f-1983-46a6-9efa-223e76833e8e
- Wed 18 Nov | مجلة أرقام | المصرية للاتصالات شريك التكنولوجيا لمشروع «نيفيرا»
  https://arqam.news/611222/
- Wed 18 Nov | اليوم السابع | المصرية للاتصالات: نعمل مع مستثمري نيفيرا لتقديم حلول تكنولوجية متكاملة
  https://m.youm7.com/amp/2026/11/18/المصرية-للاتصالات-نعمل-مع-مستثمري-نيفيرا-لتقديم-حلول-تكنولوجية-متكاملة/7624142
- Wed 18 Nov | مجلة البوصلة الاقتصادية | المصرية للاتصالات شريك التكنولوجيا لمشروع «نيفيرا».. شبكة ألياف ضوئية وحلول المدن الذكية
  https://alboslanews.com/اتصالات-وتكنولوجيا/المصرية-للاتصالات-شريك-التكنولوجيا-لمشروع-نيفيرا-شبكة-ألياف-ضوئية-وحلول-المدن-الذكية-431092
## PHDC  (3 leads)
- Thu 19 Nov | Masrawy | من فيلا بالم هيلز إلى عصابة الشرطة المزيفة ضربتان أمنيتان بأكتوبر
  https://www.masrawy.com/news/news_cases/details/2026/11/19/3081493/من-فيلا-بالم-هيلز-إلى-عصابة-الشرطة-المزيفة-ضربتان-أمنيتان-بأكتوبر?amp
  > من فيلا بالم هيلز إلى عصابة الشرطة المزيفة ضربتان أمنيتان بأكتوبر تسلل في الظلام من فيلا تحت الإنشاء، وكمين مفاجئ بـ30 ألف جنيه قدام نادي الصيد، خيطان لوقعتين مختلفتين في قسم أول أكتوبر، لكن كاميرات المراقبة والتحريات جمعتهم في نقطة واحدة: سقوط المتهمين. قفزة داخل بالم هيلز
- Wed 18 Nov | بروبرتي بلس | شركة بالم هيلز تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال أول 9 أشهر من 2026.. بمعدل نمو 18%
  https://propertypluseg.com/شركة-بالم-هيلز-تحقق-مبيعات-جديدة-بقيمة-2/
  > قال ياسين منصور، رئيس مجلس الإدارة التنفيذي لشركة بالم هيلز: “شهدت الأشهر التسعة الأولى من عام 2026 مجموعة جديدة من النتائج القوية. فقد ظل الطلب قوياً على مستوى محفظتنا المتنوعة، وواصلت استراتيجيتنا للنمو المنضبط تحقيق ثمارها.
- Wed 18 Nov | صدى العرب | بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18%
  http://www.sada-elarab.com/827417
  > بالم هيلز للتعمير تحقق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال 9 أشهر بنمو 18% أعلنت شركة بالم هيلز للتعمير تحقيق مبيعات جديدة بقيمة 214.1 مليار جنيه خلال التسعة أشهر الأولى من عام 2026، بمعدل نمو 18% مقارنة بالفترة نفسها من العام الماضي، مدعومة باستمرار قوة الطلب على مشروعات الشركة وتنوع محفظتها العقارية.
## SWDY  (5 leads)
- Thu 19 Nov | INSITE OOH Media Platform | Elsewedy Industrial Development Reveals Egypt’s Industrial Cities Map in D/OOH Campaign
  https://insiteooh.com/public/article/14776-elsewedy-industrial-development-reveals-egypts-industrial-cities-map-in-dooh-campaign
  > Elsewedy Industrial Development Reveals Egypt’s Industrial Cities Map in D/OOH Campaign Elsewedy Industrial Development is turning anticipation into an invitation to explore its industrial destinations.
- Wed 18 Nov | جريدة الملتقى الاقتصادي | السويدي الوطنية تخطط للتوسع في 2027 و2028 وتستهدف زيادة إنتاج أنظمة الري المحوري
  https://www.moltakaaliqtisad.online/السويدي-الوطنية-تخطط-للتوسع-في-2027-و2028-وتس/
  > كشفت شركة السويدي الوطنية عن خطة للتوسع والنمو خلال عامي 2027 و2028، تستهدف زيادة الطاقة الإنتاجية وتطوير المنتجات ودخول قطاعات جديدة ذات قيمة مضافة، إلى جانب تعزيز وجودها في أسواق إفريقيا والشرق الأوسط، لمواكبة الطلب المتزايد على أنظمة الري المحوري والمنتجات المعدنية المستخدمة في المشروعات الزراعية والصناعية والبنية التحتية.
- Wed 18 Nov | جريدة المال | السويدي الوطنية تستهدف زيادة إنتاج أنظمة الري المحوري والتوسع بأسواق إفريقيا والشرق الأوسط خلال 2027-2028
  https://almalnews.com/2148326/السويدي-الوطنية-تستهدف-زيادة-إنتاج-أنظمة-الري/
  (same wording as the جريدة الملتقى الاقتصادي story above: one source, not two)
## ORAS  (8 leads)
- Thu 19 Nov | ارقام : اخبار ومعلومات سوق الأسهم السعودي - تاسي | مجلس أوراسكوم كونستراكشون يقر زيادة رأس المال بـ 88.2% لصالح شركة OCI N.V
  https://www.argaam.com/ar/article/articledetail/id/1950993
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Water Tech Online | Orascom Construction breaks ground on Jordan desalination and conveyance project
  https://www.watertechonline.com/news-reports/news/55420378/orascom-construction-breaks-ground-on-jordan-desalination-and-conveyance-project
  (page: only 62 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | جريدة باور نيوز الاخبارية | أوراسكوم كونستراكشون تضع حجر الأساس لمشروع محطة تحلية مياه بالأردن باستثمارات 6.7 مليار دولار
  https://powernews.cc/?p=294466
  > أعلنت شركة أوراسكوم كونستراكشون وضع حجر الأساس لمشروع إنشاء محطة تحلية مياه في الأردن، باستثمارات تتجاوز 6.7 مليار دولار، في أحد أكبر مشروعات تحلية ونقل المياه بالمنطقة.
## FWRY  (6 leads)
- Thu 19 Nov | السودان اليوم | نقلة جديدة في المعاملات المالية.. السودان يتجه نحو الدفع الفوري
  https://alsudantoday.com/business/economic-news/568347
  (page: did not load (403))
- Thu 19 Nov | موقع الحرية الإخباري | عبر 46 منفذًا.. الجيزة تُفعّل سداد مستحقات تقنين أراضي أملاك الدولة من خلال «فوري بلس»
  https://alhorianews.com/عبر-46-منفذًا-الجيزة-تُفعّل-سداد-مستحقا/
  > كشف الدكتور أحمد الأنصاري، محافظ الجيزة، عن تفعيل خدمة السداد الإلكتروني عبر منافذ «فوري بلس» لتحصيل كافة المستحقات المالية المتعلقة بملف تقنين أوضاع أراضي أملاك الدولة، وذلك تنفيذًا لأحكام القانون رقم 168 لسنة 2025 ولائحته التنفيذية، وفي إطار خطة المحافظة لتبسيط الإجراءات وتخفيف الأعباء عن المواطنين. بنود السداد المتاحة دون الذهاب للمقار الحكومية
- Thu 19 Nov | بوابة المصرف | 10 بروتوكولات لتحديث التجارة الخارجية.. فوري وفيزا ومايكروسوفت ضمن الشركاء
  https://www.almasraf.news/10-بروتوكولات-لتحديث-التجارة-الخارجية/
  > وقّع المختبر التنظيمي ومركز الابتكار لتكنولوجيا التجارة (TradeTech Sandbox) 10 بروتوكولات تعاون مع مؤسسات وشركات مصرية ودولية، لتسريع تحديث التجارة الخارجية وتطوير حلول رقمية تستهدف تقليل الوقت والتكلفة المرتبطين بالإجراءات التجارية. وتضم الشراكات شركات متخصصة في التكنولوجيا والاتصالات والمدفوعات والخدمات المالية، من بينها فوري وفيزا ومايكروسوفت. 10 بروتوكولات تجمع شركات التكنولوجيا والمدفوعات لتطوير التجارة
- Thu 19 Nov | آراب فاينانس | فوري وفيزا ومايكروسوفت ضمن 10 جهات تتعاون مع الحكومة لتطوير التجارة الخارجية
  http://www.arabfinance.com/ar/news/newdetails/فوري-وفيزا-ومايكروسوفت
  > آراب فاينانس: تتعاون شركات فوري لتكنولوجيا البنوك والمدفوعات الالكترونية (FWRY) وفيزا ومايكروسوفت واتصالات مصر وإي فاينانس للاستثمارات المالية والرقمية (EFIH) مع وزارة الاستثمار والتجارة الخارجية وعدد من المؤسسات المحلية والدولية، لتطوير حلول تكنولوجية مبتكرة تدعم تحديث منظومة التجارة الخارجية في مصر، وذلك من خلال 10 بروتوكولات تعاون جرى توقيعها ضمن إطلاق المختبر التنظيمي ومركز الابتكار ...
- Thu 19 Nov | شبكة تواصل الإخبارية | «اتصالات» و«فوري» و«فيزا» ضمن 10 جهات تشارك في مختبر تكنولوجيا التجارة
  https://twaslnews1.twaslnews.com/7954189/
- Wed 18 Nov | أراجيك - Arageek | Fawry تخصص 80 مليون جنيه لاستثمارات التكنولوجيا والأمن السيبراني في الصدارة
  https://www.arageek.com/fawry-تخصص-80-مليون-جنيه-لاستثمارات-التكنولو
## ABUK  (1 leads)
- Thu 19 Nov | لحظات نيوز | العربية للتصنيع توقع اتفاقا لبناء محطات طاقة شمسية لشركة أبوقير للأسمدة
  https://nl7za.com/economy/العربية-للتصنيع-توقع-اتفاقا-لبناء-محطات-طاقة-شمسية
  > وقعت الهيئة العربية للتصنيع عقدا استراتيجيا موسعا مع شركة أبوقير للأسمدة والصناعات الكيماوية لتنفيذ منظومة متكاملة من محطات توليد الطاقة الكهربائية النظيفة باستخدام الخلايا الشمسية بقدرات تشغيلية عالية، ويهدف المشروع الصناعي الضخم إلى تزويد المجمعات الإنتاجية للشركة بالطاقة المتجددة وخفض تكاليف التشغيل وترشيد استهلاك الوقود التقليدي بما يتوافق مع المعايير البيئية العالمية والتنمية المستدامة للدولة ...
## HRHO  (8 leads)
- Fri 20 Nov | Africa Business Communities | Emirates NBD Egypt and EFG Hermes expand investment partnership
  https://africabusinesscommunities.com/finance/emirates-nbd-egypt-and-efg-hermes-expand-investment-partnership/
  (page: did not load (403))
- Thu 19 Nov | Vietnam.vn | حقيبة هيرميس هي المفضلة لدى ميسي وهالاند.
  https://www.vietnam.vn/ar/chiec-tui-hermes-duoc-long-messi-haaland
  > من ليونيل ميسي وديكلان رايس إلى إيرلينغ هالاند، شوهد العديد من نجوم كرة القدم وهم يحملون حقائب هيرميس الكبيرة، محولين هذه الإكسسوارات الفاخرة إلى جزء لا يتجزأ من أناقتهم خارج الملعب. مع ذلك، فإن العديد من التصاميم التي تحمل اسم "بيركين" هي في الواقع من مجموعة "هوت آ كوروا" (HAC).
- Wed 18 Nov | EnterpriseAM | "إي إف جي القابضة" وأوراسكوم كونستراكشون تعلنان نتائجهما المالية للربع الثالث
  https://enterpriseam.com/egypt-ar/2026/11/19/إي-إف-جي-القابضة-وأوراسكوم-كونستراكش/
  > ارتفعت إيرادات مجموعة "إي إف جي القابضة" بنسبة 5% على أساس سنوي في الربع الثالث من عام 2026 لتصل إلى 6.7 مليار جنيه، وفقا لبيان نتائج أعمالها (بي دي إف). في المقابل، تراجع صافي أرباح المجموعة بعد خصم الضرائب وحقوق الأقلية بنسبة 15% على أساس سنوي إلى 720 مليون جنيه خلال الربع. [Figures on the page: consolidated; one quarter; attributable to shareholders. Check which one each figure is.]
## JUFO  (1 leads)
- Thu 19 Nov | مستقبل وطن نيوز | «كُحل الجبل» يوثق بطولة أبناء جهينة في مواجهة الحملة الفرنسية بالمهرجان القومي للمسرح المدرسي
  https://www.mwatan.news/1040342
  (page: did not load (403))
## MFPC  (8 leads)
- Wed 18 Nov | مانكيش نت | موبكو تعلن تعديل مؤقت لأسعار الغاز الطبيعي بنسبة 50%
  https://mangish.net/موبكو-تعلن-تعديل-مؤقت-لأسعار-الغاز-الط/
  > أعلنت شركة مصر لإنتاج الأسمدة «موبكو» أنها قد تلقت إشعارًا رسميًا يُفيد بتعديل أسعار الغاز الطبيعي المستخدم في تشغيل مصانعها، وذلك تنفيذاً لقرار زيادة سعر الغاز المورد لمصانع الأسمدة بنسبة 50% بشكل مؤقت.
- Wed 18 Nov | جريدة آخر الأخبار | موبكو تعلن عن تعديل مؤقت لأسعار الغاز الطبيعي بنسبة 50%
  https://akher.news/1088/موبكو-تعلن-عن-تعديل-مؤقت-لأسعار-الغاز-ا/
  (page: did not load (403))
- Wed 18 Nov | الجريدة العقارية | بنسبة 50% بشكل مؤقت.. «موبكو» تعلن تعديل أسعار الغاز الطبيعي المستخدم في تشغيل مصانعها
  https://www.aleqaria.com.eg/post/details/358630/بنسبة-50-بشكل-مؤقت..-«موبكو»-تعلن-تعديل-أسعار-الغاز-الطبيعي-المستخدم-في-تشغيل-مصانعها
  > أعلنت شركة مصر لإنتاج الأسمدة «موبكو» تلقيها إخطارًا رسميًا بشأن تعديل أسعار الغاز الطبيعي المستخدم في تشغيل مصانعها، وذلك تنفيذًا لقرار زيادة سعر الغاز المورد لمصانع الأسمدة بنسبة 50% بشكل مؤقت.
## EFIH  (1 leads)
- Wed 18 Nov | جريدة المال | «الأهلي فاروس» ترفع القيمة العادلة لـ «إي فاينانس» إلى 34.3 جنيه للسهم
  https://almalnews.com/2148141/«الأهلي-فاروس»-ترفع-القيمة-العادلة-لـ-«إي/
  > أصدرت وحدة بحوث «الأهلي فاروس» تقريرًا لشركة «إي فاينانس للاستثمارات المالية والرقمية» رفعت فيه تقديراتها للقيمة العادلة للسهم إلى 34.3 جنيه وفقاً لتقديرات ديسمبر 2026، مع تأكيد توصيتها القوية بشراء السهم الذي يتداول حاليا عند مضاعف ربحية لآخر 12 شهراً يبلغ 26.9 مرة، بقيمة سوقية تصل إلى 86.3 مليار جنيه.
## EMFD  (1 leads)
- Thu 19 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس
  https://www.osoulmisrmagazine.com/452994
  > الأسهم العقارية بالبورصة المصرية.. «إعمار مصر» يتصدر الارتفاعات الخميس تباين أداء أسهم الشركات العقارية المقيدة بالبورصة المصرية خلال ختام تعاملات جلسة اليوم الخميس، إذ ارتفعت أسعار أسهم 4 شركات، مقابل تراجع أسهم 4 شركات، بينما استقر سهما مصر الجديدة للإسكان والتعمير والمطورون العرب القابضة دون تغيير.
## BQDC  (8 leads)
- Thu 19 Nov | الأسبوع | لمدة ساعة.. توقف مؤقت لماكينات الصراف الآلي والإنترنت البنكي ببنك القاهرة اليوم
  https://www.elaosboa.com/3027772/
  > توقف مؤقت لماكينات الصراف الآلي والإنترنت البنكي ببنك القاهرة اليوم أعلن بنك القاهرة عن تنفيذ أعمال صيانة وتحديث على البنية التحتية الداعمة لقنواته الرقمية، اليوم الجمعة 20 نوفمبر 2026، وذلك في إطار خطته المستمرة لتعزيز كفاءة واستقرار الخدمات المصرفية المقدمة لعملائه.
- Thu 19 Nov | شبكة تواصل الإخبارية | بعائد يصل إلى 16.75% يُصرف شهريًا.. تعرف على مزايا حساب التوفير «ثروة» من بنك القاهرة
  https://twaslnews1.twaslnews.com/7991966/
  (page: did not load (403))
- Thu 19 Nov | مستقبل وطن نيوز | بنك القاهرة يعلن عن إجراء تحديثات على الأنظمة التشغيلية وتوقا مؤقت لبعض الخدمات البنكية والإلكترونية
  https://www.mwatan.news/1040317
  (page: did not load (403))
## SKPC  (1 leads)
- Wed 18 Nov | جريدة باور نيوز الاخبارية | ترقية إسلام زيدان مديرًا عامًا للشئون القانونية بسيدبك مع استمرار ندبه لـ«ووتك»
  https://powernews.cc/?p=294339
  > أصدر المهندس كريم بدوي، وزير البترول والثروة المعدنية، حركة ترقيات وندب جديدة شملت ترقية إسلام صالح زكي زيدان، بشركة سيدي كرير للبتروكيماويات «سيدبك»، إلى وظيفة مدير عام بالإدارة العامة للشئون القانونية بالشركة، مع استمرار ندبه للقيام بأعمال وظيفة مدير عام الشئون القانونية بشركة تكنولوجيا الأخشاب «ووتك».
## EFID  (4 leads)
- Thu 19 Nov | Investing.com | إيديتا للصناعات الغذائية تسجل أعلى إيرادات فصلية في تاريخها وترتفع أسهمها
  https://sa.investing.com/news/transcripts/article-93CH-3447984
  (page: did not load (403))
- Thu 19 Nov | Investing.com UK | Earnings call transcript: Edita Food posts record Q3 2026 revenue, shares rise
  https://uk.investing.com/news/stock-market-news/earnings-call-transcript-edita-food-posts-record-q3-2026-revenue-shares-rise-93CH-4993449
  (page: did not load (403))
- Thu 19 Nov | TradingView | Edita Food Industries Company Q3 2026 Earnings Call Is Live
  https://www.tradingview.com/news/urn:live_audio:quartr.com:800175:0-edita-food-industries-company-q3-2026-earnings-call-is-live/
  > Edita Food Industries Company Q3 2026 Earnings Call Is Live Edita Food Industries Company's quarterly earnings call has just begun.
- Wed 18 Nov | جريدة المال | كريم الشرقاوي: إيديتا تستهدف التوسع في أسواق متعددة وتدرس فرصًا استحواذية لدعم نمو أعمالها
  https://almalnews.com/2148194/كريم-الشرقاوي-إيديتا-تستهدف-التوسع-في-أسواق/
  > قال كريم الشرقاوي، مدير القطاع المالي بمجموعة إيديتا إيجيب، إن المجموعة تستهدف مواصلة التوسع في أسواق متعددة، إلى جانب دراسة فرص الاستحواذ المحتملة، بما يدعم نمو أنشطتها وتعزيز انتشارها الجغرافي خلال الفترة المقبلة.
## AAPL  (7 leads)
- Fri 20 Nov | The Motley Fool | Warren Buffett’s Successor Just Bought $10 Billion of This AI Stock, and It’s Not Apple
  https://www.fool.com/investing/2026/11/20/warren-buffetts-successor-just-bought-10-billion-of-this-ai-stock-and-its-not-apple/
  > By Thomas Niel – - Greg Abel has made some major deals since taking charge at Berkshire Hathaway, but his largest thus far is his increased investment in Alphabet. - Berkshire purchased $10 billion in newly issued shares of Alphabet as part of a $90 billion private placement. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Fri 20 Nov | MarketBeat | Apple Inc. $AAPL Stock: AMI Investment Management Inc. Boosts Position
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-stock-ami-investment-management-inc-boosts-position-2026-11-20/
  > $AAPL Stock: AMI Investment Management Inc. - AMI Investment Management increased its Apple stake by 21.1% in the third quarter, adding 1,893 shares to reach 10,858 shares valued at $3.616 million. - Apple reported quarterly earnings of $2.10 per share, above the $1.99 consensus estimate, while revenue rose 11.7% year over year to $114.48 billion.
- Fri 20 Nov | marketscreener.com | Apple Inc. : UBS gives a Neutral rating
  https://www.marketscreener.com/news/apple-inc-ubs-gives-a-neutral-rating-ce785ed2d089f426
  (page: did not load (403))
## MSFT  (8 leads)
- Fri 20 Nov | Trefis | What Could Stall Microsoft Stock’s Run?
  https://www.trefis.com/stock/msft/articles/627236/what-could-stall-microsoft-stocks-run/2026-11-20
  > What Could Stall Microsoft Stock’s Run? Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? Microsoft (MSFT) stock returned 19.4% over the six months to November 19, 2026, while the S&P 500 lost 3.1%. The shares still closed 10.2% below their November 4 high. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Fri 20 Nov | Trefis | $1 Million In Microsoft 10 Years Ago: Worth It?
  https://www.trefis.com/stock/msft/articles/627168/1-million-in-microsoft-10-years-ago-worth-it/2026-11-20
  > $1 Million In Microsoft 10 Years Ago: Worth It? Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? $1 million put into Microsoft at the Friday, Nov 18, 2016 close was worth about $9.25 million at Thursday’s close. On price alone, the stake came to $8,256,835.
- Fri 20 Nov | Investing.com | Nestle teams up with Microsoft and Boston Dynamics to expand AI use
  https://www.investing.com/news/stock-market-news/nestle-teams-up-with-microsoft-and-boston-dynamics-to-expand-ai-use-93CH-5040930
  (page: did not load (403))
## NVDA  (8 leads)
- Fri 20 Nov | The New York Times | Stocks Often Prosper After an Abrupt C.E.O. Exit. Is Nvidia Different?
  https://www.nytimes.com/2026/11/20/business/nvidia-ceo-stock-succession-jensen-huang.html
  (page: did not load (403))
- Fri 20 Nov | Yahoo Finance | Nvidia Has Lost More Than the Market Value of 495 S&P 500 Companies in 6 Weeks -- and Its Downtrend May Be Just Beginning
  https://finance.yahoo.com/markets/stocks/articles/nvidia-lost-more-market-value-092601792.html
  > Nvidia Has Lost More Than the Market Value of 495 S&P 500 Companies in 6 Weeks -- and Its Downtrend May Be Just Beginning 6, Nvidia (NASDAQ:NVDA) peaked at an intraday high of $243.37 per share, reaching a valuation of $5.78 trillion. 6 intraday peak and the Nov.
- Fri 20 Nov | Trefis | Is Nvidia’s $81 Billion Receivables Pile A Risk?
  https://www.trefis.com/stock/nvda/articles/627205/is-nvidia-s-81-billion-receivables-pile-a-risk/2026-11-20
  > Is Nvidia’s $81 Billion Receivables Pile A Risk? Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? Most talk about Nvidia stock centers on two events. Nvidia also stopped shipping its licensed Hopper chips to China, a line worth $2.4 billion last quarter. It is the money customers owe Nvidia, called receivables. [Figures on the page: nine months; first half. Check which one each figure is.]
- Fri 20 Nov | Trefis | Should You Sell Nvidia Stock For A Tax Loss?
  https://www.trefis.com/stock/nvda/articles/627207/should-you-sell-nvidia-stock-for-a-tax-loss/2026-11-20
  > Should You Sell Nvidia Stock For A Tax Loss? Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? Nvidia announced on Nov 12 that Jensen Huang resigned as chief executive. If you bought Nvidia at any close in the past year, you hold a loss.
- Fri 20 Nov | Yahoo Finance | ‘Dean Of Valuation’ Says Nvidia Is 30% Below Fair Value, Waits For $140 — Calls Jensen Huang ‘Great CEO, But Human’
  https://finance.yahoo.com/markets/stocks/articles/dean-valuation-says-nvidia-30-085810133.html
- Fri 20 Nov | Trefis | Amazon, Nvidia Fell As Anthropic Gained $185 Billion
  https://www.trefis.com/stock/amzn/articles/627187/amazon-nvidia-fell-as-anthropic-gained-185-billion/2026-11-20
- Fri 20 Nov | Trefis | Why Did Nvidia Stock Fall 39%?
  https://www.trefis.com/stock/nvda/articles/626526/why-did-nvidia-stock-fall-39/2026-11-20
- Fri 20 Nov | Trefis | Cisco Fell 89%. Is Nvidia Stock Next?
  https://www.trefis.com/stock/nvda/articles/626552/cisco-fell-89-is-nvidia-stock-next/2026-11-20
## AMZN  (8 leads)
- Fri 20 Nov | Pluang | Amazon outperforms Alphabet in 2026 amid AI-dri...
  https://pluang.com/en/news-feed/amazon-vs-alphabet-saham-cloud-computing-pilihan-lebih-baik
  (page: did not load (403))
- Fri 20 Nov | Benzinga | NYC Mayor Zohran Mamdani Hits Back at Amazon Over $5 Order Warning - Amazon.com (NASDAQ:AMZN)
  https://www.benzinga.com/markets/tech/26/11/63465083/zohran-mamdani-amazon-new-york-city-delivery-legislation-jeff-bezos-greed
  (page: did not load (403))
- Fri 20 Nov | www.tokenpost.com | Amazon Shares Fell 6.32% to $255.92 After Quarterly Results
  https://www.tokenpost.com/news/investing/61908
  > Amazon shares closed at $255.92 on Nov. 19, 2026, down 6.32% over the preceding 24 hours, after quarterly results missed estimates and left the stock just below its 50-day moving average and near its 200-day average. Amazon reported earnings of $1.89 per share, compared with estimates of about $1.96 to $1.97.
- Fri 20 Nov | Gotrade | Amazon Stock (AMZN) Falls 3.9% After Anthropic IPO Debut (Nov 19)
  https://www.heygotrade.com/en/news/amazon-amzn-stock-news-november-20-2026/
  > AI-powered contentSome parts of this article are powered by AI. Amazon (AMZN) fell 3.87% to $257.37 on November 19, 2026, finishing just $0.62 above its day low. Yahoo Finance linked the market's slide to Anthropic's first day of trading, and Amazon holds 14.6% of Anthropic, according to GuruFocus.
- Fri 20 Nov | Yahoo Finance | Pixalate Launches 4D Invalid Traffic (IVT) Blocking on Amazon Web Services (AWS) RTB Fabric; Industry’s First Infrastructure-, Seller-, Publisher-, & Device-Level Pre-Bid Blocking Modules for Program
  https://finance.yahoo.com/media-advertising/articles/pixalate-launches-4d-invalid-traffic-034000682.html
- Fri 20 Nov | Yahoo Finance | Pixalate Launches OpenEPG DB™ on Amazon Web Services (AWS) RTB Fabric; Industry’s First Show-, Genre-, and Content Rating-Level Enrichment Module for Programmatic CTV, Including Live Sports
  https://finance.yahoo.com/media-advertising/articles/pixalate-launches-openepg-db-amazon-035000473.html
- Fri 20 Nov | Stocktwits | ANT Stock Has Nearly 60% Upside Potential? Wall Street Sees An Amazon-Google Scale Opportunity In Anthropic
  https://stocktwits.com/news-articles/markets/equity/how-high-can-ant-stock-go-wall-street-valuation-analyst-amazon-google-scale-opportunity/cNbSG4tR90C
- Fri 20 Nov | TIKR.com | Prediction: Anthropic Faces a “SpaceX-Like 20 to 30 Percent Decline,” per Paul Kedrosky. That’s a Risk for Amazon
  https://www.tikr.com/blog/prediction-anthropic-faces-a-spacex-like-20-to-30-percent-decline-per-paul-kedrosky-thats-a-risk-for-amazon
## GOOGL  (8 leads)
- Fri 20 Nov | Pluang | Amazon outperforms Alphabet in 2026 amid AI-dri...
  https://pluang.com/en/news-feed/amazon-vs-alphabet-saham-cloud-computing-pilihan-lebih-baik
  (page: did not load (403))
- Fri 20 Nov | FXLeaders | Alphabet Stock Risks Breakdown Below $270 Support as Anthropic Deal, Gemini Expansion and Rising Costs Weigh on GOOG
  https://www.fxleaders.com/news/2026/11/19/alphabet-stock-risks-breakdown-below-270-support-as-anthropic-deal-gemini-expansion-and-rising-costs-weigh-on-goog/
  > Alphabet Stock Risks Breakdown Below $270 Support as Anthropic Deal, Gemini Expansion and Rising Costs Weigh on GOOG
- Fri 20 Nov | CryptoRank | Wrapped Alphabet Tokenized stock (xStock): Funding, Investors, Team and Key Events
  https://cryptorank.io/price/wrapped-alphabet-tokenized-stock-xstock
  (page: did not load (403))
- Fri 20 Nov | Nacionale | Can Google sell its Anthropic stake? Only in small slices for now, and its shares carry no vote
  https://www.nacionale.com/en/articles/can-google-sell-anthropic-stake-lockup-no-vote-alphabet-what-happens-next
  (page: did not load (403))
- Fri 20 Nov | Nacionale | Why did Alphabet stock fall on Anthropic's IPO day? Google's big stake was mostly priced in
  https://www.nacionale.com/en/articles/why-did-alphabet-stock-fall-anthropic-ipo-google-stake-worth-november-19
- Thu 19 Nov | CNBC | Cramer: My favorite chartist sees two major signs of a rally brewing in Alphabet stock
  https://www.cnbc.com/2026/11/19/alphabet-stock-larry-williams-rally-signals.html
- Thu 19 Nov | Global Banking & Finance Review | Alphabet Inc Class C falls 2.93% in Thursday's session
  https://www.globalbankingandfinance.com/alphabet-inc-class-c-goog-falls-2026-11-19/
- Thu 19 Nov | The National Law Review | Kaplan Fox Encourages Alphabet Inc. (NASDAQ: GOOGL, GOOG) Investo
  https://natlawreview.com/press-releases/kaplan-fox-encourages-alphabet-inc-nasdaq-googl-goog-investors-contact-1
## META  (8 leads)
- Fri 20 Nov | MarketBeat | Meta Platforms, Inc. $META Stock Position Lessened by Cypress Funds LLC
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-position-lessened-by-cypress-funds-llc-2026-11-20/
  > $META Stock Position Lessened by Cypress Funds LLC - Cypress Funds cut its Meta stake by 4.8% in the third quarter, selling 1,497 shares; it retained 29,823 shares valued at about $21.6 million, representing 7.1% of its portfolio.
- Fri 20 Nov | MarketBeat | Meta Platforms, Inc. $META Stake Lowered by Farley Capital L.P.
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stake-lowered-by-farley-capital-lp-2026-11-20/
  > $META Stake Lowered by Farley Capital L.P. - Farley Capital cut its Meta stake by 20% in the third quarter, selling 1,950 shares; it held 7,803 shares valued at $5.66 million at quarter-end.
- Fri 20 Nov | marketscreener.com | Meta Platforms Insider Sold Shares Worth $5,720,398, According to a Recent SEC Filing
  https://www.marketscreener.com/news/meta-platforms-insider-sold-shares-worth-5-720-398-according-to-a-recent-sec-filing-ce785ed2d08df127
  (page: did not load (403))
- Fri 20 Nov | Kalkine Media | Why Is Meta Platforms (NASDAQ:META) Scaling Up Its AI Spending Plan?
  https://kalkinemedia.com/us/stocks/communication/why-is-meta-platforms-nasdaqmeta-scaling-up-its-ai-spending-plan
  > - Meta Platforms drew fresh attention as the company signaled a notably larger artificial-intelligence spending plan for the year ahead. - The advertising engine across its family of apps remains the financial foundation funding the heavy build-out. Meta Platforms (NASDAQ:META) Communication Services Meta Platforms Inc.
- Fri 20 Nov | Investing.com | Exclusive-Taiwan tells Meta thousands of China-linked accounts seek to influence elections By Reuters
  https://www.investing.com/news/stock-market-news/exclusivetaiwan-tells-meta-thousands-of-chinalinked-accounts-seek-to-influence-elections-5040684
- Fri 20 Nov | MarketBeat | Meta Platforms (NASDAQ:META) Insider Sells $974,375.00 in Stock
  https://www.marketbeat.com/instant-alerts/insider-meta-platforms-nasdaq-meta-insider-sells-97437500-in-stock-2026-11-19/
- Fri 20 Nov | MarketBeat | Meta Platforms (NASDAQ:META) CTO Sells $4,904,375.00 in Stock
  https://www.marketbeat.com/instant-alerts/insider-meta-platforms-nasdaq-meta-cto-sells-490437500-in-stock-2026-11-19/
- Fri 20 Nov | MarketBeat | Insider Selling: Meta Platforms (NASDAQ:META) CFO Sells $5,720,371.80 in Stock
  https://www.marketbeat.com/instant-alerts/insider-insider-selling-meta-platforms-nasdaq-meta-cfo-sells-572037180-in-stock-2026-11-19/
## TSLA  (8 leads)
- Fri 20 Nov | Pluang | SpaceX-Tesla merger faces tough shareholder vot...
  https://pluang.com/en/news-feed/tantangan-voting-dan-hambatan-regulasi-merger-spacex-tesla
  (page: did not load (403))
- Fri 20 Nov | Yahoo Finance | A SpaceX-Tesla Merger Needs "Yes" From 50% of All Tesla Shares, Not Just Votes Cast. Here's Why That Math Is Harder Than Wall Street Thinks.
  https://finance.yahoo.com/markets/stocks/articles/spacex-tesla-merger-needs-yes-100400761.html
  > A SpaceX-Tesla Merger Needs "Yes" From 50% of All Tesla Shares, Not Just Votes Cast. Here's Why That Math Is Harder Than Wall Street Thinks. Space Exploration Technologies (NASDAQ: SPCX), better known as SpaceX, has been a publicly traded company for less than six months.
- Fri 20 Nov | TipRanks | Tesla upgraded to Hold from Reduce at HSBC
  https://www.tipranks.com/news/the-fly/tesla-upgraded-to-hold-from-reduce-at-hsbc-thefly-news?utm_source=edition.cnn.com&utm_medium=referral
  (page: did not load (403))
- Fri 20 Nov | Benzinga | Gary Black Warns SpaceX-Tesla Merger Could Wipe Out 24% Premium in Weeks: 'Massive Dilution' Could Crush
  https://www.benzinga.com/markets/tech/26/11/63464835/gary-black-warns-spacex-tesla-merger-could-wipe-out-24-premium-in-weeks-massive-dilution-could-crush-shares
  (page: did not load (403))
- Fri 20 Nov | MarketBeat | 2,533 Shares of Tesla, Inc. $TSLA Bought by Beta Wealth Group Inc.
  https://www.marketbeat.com/instant-alerts/filing-2533-shares-of-tesla-inc-tsla-bought-by-beta-wealth-group-inc-2026-11-20/
- Fri 20 Nov | Investing.com | HSBC upgrades Tesla stock rating on acquisition potential, raises price target to $359
  https://www.investing.com/news/analyst-ratings/hsbc-upgrades-tesla-stock-rating-on-acquisition-potential-raises-price-target-to-359-93CH-5040834
- Fri 20 Nov | TradingView | Tesla, Inc. Stock 12‑Month Price Target Raised to $429.16, Implies 15% Upside
  https://www.tradingview.com/news/tradingview:d103d26de535c:0-tesla-inc-stock-12-month-price-target-raised-to-429-16-implies-15-upside/
- Fri 20 Nov | Yahoo Finance | Could Tesla Become The Next Lumentum? Gary Black Warns A SpaceX Stock Deal Could Send TSLA Down 25%
  https://finance.yahoo.com/markets/stocks/articles/could-tesla-become-next-lumentum-061559366.html
## JPM  (8 leads)
- Fri 20 Nov | Hackread | JPMorgan Chase, Visa and Mastercard confirm vendor incidents after n0n leak claims
  https://hackread.com/jpmorgan-chase-visa-mastercard-vendor-incidents-n0n-leak/
  > Press play to start listening JPMorgan Chase, Visa and Mastercard acknowledged cyber incidents involving third-party service providers on Thursday, November 19, after the extortion group n0n posted files it claimed contained records linked to the three companies.
- Fri 20 Nov | FinanceFeeds | Hackers Leak Customer Data Linked to Visa, Mastercard and JPMorgan Chase Following Third-Party Cyberattacks
  https://financefeeds.com/hackers-leak-customer-data-linked-to-visa-mastercard-and-jpmorgan-chase-following-third-party-cyberattacks/
  > Hackers have published personal information associated with thousands of Visa, Mastercard and JPMorgan Chase customers following cyberattacks targeting external service providers, raising concerns about the security of customer data held by financial institutions’ technology partners.
- Fri 20 Nov | TradingView | REG - Ashtead Tech Hldgs JPMorgan Chase & Co - Holding(s) in Company
  https://www.tradingview.com/news/reuters.com,2026-11-20:newsml_RST0494Ea:0-reg-ashtead-tech-hldgs-jpmorgan-chase-co-holding-s-in-company/
  > REG - Ashtead Tech Hldgs JPMorgan Chase & Co - Holding(s) in Company TR-1: Standard form for notification of major holdings JPMorgan Chase & Co.
## XOM  (8 leads)
- Fri 20 Nov | News Room Guyana | PM Phillips renews support to ExxonMobil Guyana Futsal tournament in Linden
  https://newsroom.gy/2026/11/20/pm-phillips-renews-support-to-exxonmobil-guyana-futsal-tournament-in-linden/
  > PM Phillips renews support to ExxonMobil Guyana Futsal tournament in Linden The organisers of the ExxonMobil Guyana Futsal Tournament 2026 are pleased to acknowledge the continued support and sponsorship of Prime Minister Brigadier (Ret’d) Mark Phillips to the annual competition in Linden.
- Fri 20 Nov | Splash247 | ExxonMobil hands TechnipFMC fresh Guyana subsea work
  https://splash247.com/exxonmobil-hands-technipfmc-fresh-guyana-subsea-work/
  > Offshore engineering company TechnipFMC has secured two contracts from ExxonMobil for subsea equipment on the $12.5bn Longtail gas-condensate development in Guyana’s Stabroek block. The first award covers project management, engineering and manufacturing of the project’s subsea production systems, including Subsea 2.0 trees, manifolds and associated controls.
- Fri 20 Nov | Guyana Chronicle | PM Phillips commits to 2026 Exxonmobil Guyana Futsal Tournament
  https://guyanachronicle.com/2026/11/20/pm-phillips-commits-to-2026-exxonmobil-guyana-futsal-tournament/
  (page: did not load (307))
## AVGO  (8 leads)
- Fri 20 Nov | MarketBeat | Broadcom Inc. $AVGO Shares Newly Purchased by Edgestream Partners L.P.
  https://www.marketbeat.com/instant-alerts/filing-broadcom-inc-avgo-shares-newly-purchased-by-edgestream-partners-lp-2026-11-20/
  > $AVGO Shares Newly Purchased by Edgestream Partners L.P. - Edgestream Partners initiated a Broadcom position in the third quarter, buying 10,312 shares valued at approximately $3.62 million. - Several other institutional investors also increased their holdings; hedge funds and other institutions collectively own 76.43% of Broadcom shares.
- Fri 20 Nov | www.tokenpost.com | Broadcom Shares Fall 5.76% as Broker Targets Move Lower
  https://www.tokenpost.com/news/investing/61906
  > Broadcom (AVGO) shares fell 5.76% to $341.68 Thursday as recent broker actions lowered price targets, while two firms retained Buy ratings and another downgraded the stock to Neutral. The close was below Broadcom’s seven-day average of $344.51 and its 200-day average of $376.87, but above its 50-day average of $339.43.
- Fri 20 Nov | MarketBeat | 147,956 Shares of Broadcom Inc. $AVGO Acquired by Advisors Asset Management Inc.
  https://www.marketbeat.com/instant-alerts/filing-147956-shares-of-broadcom-inc-avgo-acquired-by-advisors-asset-management-inc-2026-11-20/
  > 147,956 Shares of Broadcom Inc. $AVGO Acquired by Advisors Asset Management Inc. - Advisors Asset Management acquired 147,956 Broadcom shares in the third quarter, valued at approximately $52 million. - Other institutional investors also increased or added to positions; hedge funds and other institutions own 76.43% of Broadcom’s stock.
- Fri 20 Nov | ad-hoc-news.de | Broadcom stock joins Anthropic deal; EUR 307.40, down 6.09%
  https://www.ad-hoc-news.de/boerse/news/vorboerse/broadcom-stock-joins-anthropic-deal-eur-307-40-down-6-09/70539073
  > Broadcom stock traded at EUR 307.40 on Lang & Schwarz at 08:31 CET on Friday, November 20, 2026, 6.09 percent below the Xetra close of Thursday, November 19, 2026. Broadcom deepens Anthropic ties Broadcom agreed on November 19 to buy about USD 1 billion of Anthropic shares in a planned USD 26 billion private placement.
- Fri 20 Nov | Yahoo Finance | Is Broadcom (AVGO) Stock Stretched Or Still Reasonable On Cash Flow?
  https://finance.yahoo.com/markets/stocks/articles/broadcom-avgo-stock-stretched-still-031317832.html
- Thu 19 Nov | Pluang | Broadcom expects AI chip revenue to hit $230B b...
  https://pluang.com/en/news-feed/pertumbuhan-chip-ai-broadcom-2027-peluang
- Thu 19 Nov | Kalkine Media | Broadcom (NASDAQ:AVGO) Faces AI Growth Questions After Stock Decline
  https://kalkinemedia.com/us/stocks/technology/broadcom-nasdaqavgo-faces-ai-growth-questions-after-stock-decline
- Thu 19 Nov | MarketBeat | Broadcom (NASDAQ:AVGO) Stock Price Down 2.1% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-broadcom-nasdaq-avgo-stock-price-down-21-heres-why-2026-11-19/
## BRK.B  (8 leads)
- Fri 20 Nov | The Motley Fool | Warren Buffett's Successor, Greg Abel, Has 31% of Berkshire Hathaway's $363 Billion Portfolio Invested in 3 Game-Changing AI Stocks
  https://www.fool.com/investing/2026/11/20/warren-buffett-successor-greg-abel-31-berkshire-hathaway-363-billion-portfolio-in-3-ai-stocks/
  > By Sean Williams – - Berkshire’s longtime CEO, Warren Buffett, retired at the end of 2025, passing the baton and oversight of his company’s investment portfolio to Greg Abel. - Abel has completely overhauled Berkshire’s $363 billion portfolio, with a never-before-seen focus on artificial intelligence (AI)-driven tech stocks.
- Fri 20 Nov | شبكة تواصل الإخبارية | Warren Buffett’s Successor Just Bought $10 Billion of This AI Stock, and It’s Not Apple
  https://twaslnews1.twaslnews.com/8014141/
  (page: did not load (403))
- Fri 20 Nov | ad-hoc-news.de | Berkshire Prices a Five-Part Yen Bond as Portfolio Shifts Face an Earnings Test
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/berkshire-prices-a-five-part-yen-bond-as-portfolio-shifts-face-an-earnings-test/70539208
  > Berkshire Hathaway has wrapped a ¥182.3 billion senior note sale, splitting the debt across five maturities that stretch from 2029 all the way to 2056 — a financing package that lands just as investors are weighing whether the conglomerate's reshuffled equity book can offset a softer operating picture. [Figures on the page: standalone; one quarter; attributable to shareholders. Check which one each figure is.]
## WMT  (8 leads)
- Fri 20 Nov | Fox Business | Walmart shoppers stock up on water, propane after US tech outages
  https://www.foxbusiness.com/video/6408641245112
  (page: only 56 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 20 Nov | Trefis | Own Walmart? Its Cash Lags Its Price
  https://www.trefis.com/stock/wmt/articles/627188/own-walmart-its-cash-lags-its-price/2026-11-20
  > Its Cash Lags Its Price Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? Walmart (WMT) did better than expected on Thursday, and its stock still fell. Revenue for the quarter to October grew 4.5% in constant currency.
- Fri 20 Nov | Gotrade | Walmart Stock (WMT) Falls 1.0% After Q3 Earnings (Nov 19)
  https://www.heygotrade.com/en/news/walmart-wmt-stock-news-november-20-2026/
  > AI-powered contentSome parts of this article are powered by AI. Walmart (WMT) fell 1.04% to $126.04 on November 19, 2026, after reporting fiscal third-quarter results and raising its full-year outlook. The decline was milder than the Nasdaq Composite, which fell 2.25% in the same session.
## V  (8 leads)
- Fri 20 Nov | MarketBeat | 292,753 Shares of Visa Inc. $V Purchased by Advisors Asset Management Inc.
  https://www.marketbeat.com/instant-alerts/filing-292753-shares-of-visa-inc-v-purchased-by-advisors-asset-management-inc-2026-11-20/
  > 292,753 Shares of Visa Inc. $V Purchased by Advisors Asset Management Inc. - Advisors Asset Management acquired 292,753 Visa shares in the third quarter, worth about $105.2 million; Visa became 0.9% of its portfolio and its ninth-largest holding. - Analysts’ consensus rating was Buy, with an average price target of $443.35.
- Fri 20 Nov | JournalArta | Visa Stock Slides 3.12% (November 19, 2026): Down 4.3% in Five Sessions
  https://journalarta.com/en/2026/11/20/visa-stock-slides-3-12-november-19-2026-down-4-3-in-five-sessions/
  > Visa Stock Slides 3.12% (November 19, 2026): Down 4.3% in Five Sessions Technical analysis of Visa stock on November 19, 2026: price 402.25 USD, trend sideways, RSI 43.9, support 400.60, resistance 436.57.
- Fri 20 Nov | The Malaysian Reserve | JPMorgan, Visa, Mastercard warn of cyberattack that hit outside vendor
  https://themalaysianreserve.com/2026/11/20/jpmorgan-visa-mastercard-warn-of-cyberattack-that-hit-outside-vendor/
  (page: did not load (403))
- Fri 20 Nov | The Globe and Mail | Can Visa Turn AI-Led Commerce Into a New Growth Driver?
  https://www.theglobeandmail.com/investing/markets/stocks/MA-N/pressreleases/8919216/can-visa-turn-ai-led-commerce-into-a-new-growth-driver/
  > Can Visa Turn AI-Led Commerce Into a New Growth Driver? V is expanding its Agentic Ready program to merchants, payment service providers, acquirers and commerce platforms, with more than 140 participants joining at launch. Visa's framework allows participants to test agent authentication, tokenized credentials and fraud controls using existing payment infrastructure.
- Thu 19 Nov | Kalkine Media | Visa (NYSE:V) Faces Pressure Despite Strong Business Activity
  https://kalkinemedia.com/us/stocks/financial/visa-nysev-faces-pressure-despite-strong-business-activity
- Thu 19 Nov | MarketBeat | Visa (NYSE:V) Shares Down 3.1% - Here's Why
  https://www.marketbeat.com/instant-alerts/price-visa-nyse-v-shares-down-31-heres-why-2026-11-19/
- Thu 19 Nov | Yahoo Finance | JPMorgan, Visa, and Mastercard disclose cyberattack on third-party vendors
  https://finance.yahoo.com/markets/article/jpmorgan-visa-and-mastercard-disclose-cyberattack-on-third-party-vendors-190314490.html
- Thu 19 Nov | Traders Union | Visa stock extends downward price move as seller pressure outweighs oversold signals
  https://tradersunion.com/news/stocks/show/4325480-visa-drops-3-12percent-to-usd402-25/
## ORCL  (8 leads)
- Fri 20 Nov | Pluang | Oracle shares drop 65% from record as revenue g...
  https://pluang.com/en/news-feed/harga-saham-oracle-terendah-april-2024-beli-sekarang
  (page: did not load (403))
- Fri 20 Nov | The Motley Fool | Oracle Stock Just Closed at Its Lowest Price Since April 2024. Is It a Buy Now?
  https://www.fool.com/investing/2026/11/20/oracle-stock-just-closed-at-its-lowest-price-since-april-2024-is-it-a-buy-now/
  > By Daniel Sparks – - Oracle stock finished Nov. 18 at $113.89, around 65% below its September 2025 record. - Oracle expects revenue to rise 30% to 34% in its fiscal second quarter, which ends this month. - Management's guidance has adjusted earnings per share rising a slower 21% to 25%, excluding a one-time gain.
- Fri 20 Nov | ad-hoc-news.de | Oracle stock: Analyst sees AI downside; shares fall 6.01% to EUR 98.11
  https://www.ad-hoc-news.de/boerse/news/vorboerse/oracle-stock-analyst-sees-ai-downside-shares-fall-6-01-to-eur-98-11/70539140
  > Oracle provides database technology, cloud infrastructure and enterprise applications to businesses worldwide. On Xetra, the stock closed at EUR 104.38 on Thursday, November 19, 2026. Oracle faces AI investment scrutiny Bernstein maintained its Outperform rating and a 325 US-dollar price target despite outlining a severe downside scenario for Oracle's AI data-center business.
- Fri 20 Nov | FXLeaders | Oracle Stock ORCL Faces $100 Breakdown Risk as the Data-Centre Costs and Debt Mount
  https://www.fxleaders.com/news/2026/11/19/oracle-stock-orcl-faces-100-breakdown-risk-as-the-data-centre-costs-and-debt-mount/
  > Oracle Stock ORCL Faces $100 Breakdown Risk as the Data-Centre Costs and Debt Mount Oracle stock ORCL is approaching critical support near $110 as demands for financial guarantees, Democratic midterm victories, rising infrastructure costs and a $20 billion funding package intensify concerns about its debt burden and ambitious cloud expansion.
- Fri 20 Nov | Yahoo Finance | Oracle (ORCL) Stock May Be 39% Undervalued As Nashville Buildout Starts
  https://finance.yahoo.com/markets/stocks/articles/oracle-orcl-stock-may-39-002103750.html
- Fri 20 Nov | Kalkine Media | Why Is Oracle (NYSE:ORCL) Facing Pressure Amid Rising AI Infrastructure Costs?
  https://kalkinemedia.com/us/stocks/technology/why-is-oracle-nyseorcl-facing-pressure-amid-rising-ai-infrastructure-costs
- Thu 19 Nov | EnergyNow.com | Gas Pipeline for Proposed Oracle Data Center Delayed to 2027
  https://energynow.com/2026/08/gas-pipeline-for-proposed-oracle-data-center-delayed-to-2027/
- Thu 19 Nov | MarketBeat | Oracle (NYSE:ORCL) Shares Down 3.1% - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-oracle-nyse-orcl-shares-down-31-should-you-sell-2026-11-19/
## COST  (8 leads)
- Fri 20 Nov | MarketBeat | 229,666 Shares in Costco Wholesale Corporation $COST Acquired by Advisors Asset Management Inc.
  https://www.marketbeat.com/instant-alerts/filing-229666-shares-in-costco-wholesale-corporation-cost-acquired-by-advisors-asset-management-inc-2026-11-20/
  > 229,666 Shares in Costco Wholesale Corporation $COST Acquired by Advisors Asset Management Inc. - Advisors Asset Management initiated a major Costco position, buying 229,666 shares worth about $209.1 million in the third quarter. Costco became its second-largest holding, representing roughly 1.8% of its portfolio.
- Fri 20 Nov | MarketBeat | Costco Wholesale (NASDAQ:COST) Stock Sale Reported by Rep. Michael A. Rulli
  https://www.marketbeat.com/instant-alerts/congress-costco-wholesale-nasdaq-cost-stock-sale-reported-by-rep-michael-a-rulli-2026-11-20/
  > Costco Wholesale (NASDAQ:COST) Stock Sale Reported by Rep. Rulli reported selling $1,001–$15,000 of Costco shares on Nov. 12 from his Merrill Lynch Simple Managed Account. - Costco’s latest quarter beat estimates, with EPS of $6.75 versus $6.54 expected and revenue of $95.72 billion; revenue rose 11.1% year over year.
- Fri 20 Nov | Simply Wall St | Costco (COST) Saw Emergency Supply Sales Surge After Tech Outages
  https://simplywall.st/stocks/us/consumer-retailing/nasdaq-cost/costco-wholesale/news/costco-cost-saw-emergency-supply-sales-surge-after-tech-outa
  > Costco Wholesale (NasdaqGS:COST) reported a surge in emergency preparedness product sales after recent large scale technology outages at major firms. The retailer saw heightened demand for generators, bulk pantry staples and related items as shoppers reacted to the infrastructure disruptions.
## NFLX  (8 leads)
- Fri 20 Nov | Kalkine Media | Will the Holiday NFL Stream Boost the Netflix (NASDAQ:NFLX) Ad Tier?
  https://kalkinemedia.com/us/stocks/communication/will-the-holiday-nfl-stream-boost-the-netflix-nasdaqnflx-ad-tier
  > - A marquee holiday live NFL stream puts the advertising push to the test - The advertising-supported tier keeps scaling as a fresh revenue stream
- Fri 20 Nov | Foreign Policy Journal | Netflix (NASDAQ: NFLX) Stock Price Trades At Half Its Historical Multiple As January Guidance Looms Large
  https://www.foreignpolicyjournal.com/2026/11/19/netflix-nasdaq-nflx-stock-price-trades-at-half-its-historical-multiple-as-january-guidance-looms-large/
  > Wall Street’s consensus price target for Netflix (NASDAQ: NFLX) sits more than 40% above its recent close, a gap that reflects deep disagreement about where the streaming giant is headed.
- Fri 20 Nov | River Country News Channel Nebraska | Nebraska man shares experience on Netflix's 'The New Stanford Prison Experiment'
  https://rivercountry.newschannelnebraska.com/story/370530021/nebraska-man-shares-experience-on-netflixs-the-new-stanford-prison-experiment
  (page: only 39 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 19 Nov | Kalkine Media | Netflix (NASDAQ:NFLX) Faces A Major Test As Streaming Evolves
  https://kalkinemedia.com/us/stocks/communication/netflix-nasdaqnflx-faces-a-major-test-as-streaming-evolves
  > - Netflix strengthens its entertainment strategy through advertising and original programming. - Live sports could broaden audience engagement and content offerings. Netflix is broadening its entertainment business through advertising, original programming, mobile games, and live sports as competition reshapes the global streaming industry.
- Thu 19 Nov | Simply Wall St | Netflix (NFLX) Gets A Backing Boost As AI Cuts Streaming Production Compute 30%
  https://simplywall.st/stocks/us/media/nasdaq-nflx/netflix/news/netflix-nflx-gets-a-backing-boost-as-ai-cuts-streaming-produ/amp
- Thu 19 Nov | Global Banking & Finance Review | Netflix falls 2.32% in Thursday's session
  https://www.globalbankingandfinance.com/netflix-nflx-falls-2026-11-19/
- Thu 19 Nov | MarketBeat | Netflix (NASDAQ:NFLX) Stock Price Down 2.3% - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-netflix-nasdaq-nflx-stock-price-down-23-should-you-sell-2026-11-19/
- Thu 19 Nov | TIKR.com | Josh Brown: Netflix Can Clear Wall Street’s 10.6% Growth Bar “Standing on Their Head”
  https://www.tikr.com/blog/josh-brown-netflix-can-clear-wall-streets-10-6-growth-bar-standing-on-their-head?
## INTC  (8 leads)
- Fri 20 Nov | FXLeaders | INTC Stock Rebound Is Underway as Intel Signs First External Customer for Advanced 18A Chips
  https://www.fxleaders.com/news/2026/11/19/intc-stock-rebound-is-underway-as-intel-signs-first-external-customer-for-advanced-18a-chips/
  > INTC Stock Rebound Is Underway as Intel Signs First External Customer for Advanced 18A Chips
- Fri 20 Nov | Barron's | Nvidia, Intel, Salesforce, SpaceX, Anthropic, Sandisk, Home Depot, and More That Explain Today’s Market
  https://www.barrons.com/articles/stock-movers-5503b6f4
  (page: did not load (401))
- Fri 20 Nov | JournalArta | Nvidia and Intel Shares Fall After Earnings and Outlook
  https://journalarta.com/en/2026/11/20/nvidia-intel-shares-fall-earnings-outlook-investor/
  > Nvidia and Intel Shares Fall After Earnings and Outlook Nvidia shares fell after a strong quarterly report, while Intel’s weak outlook has weighed on its stock. An investor known as The Curious Analyst rates Nvidia a Strong Buy and Intel a Hold, citing different prospects for profitability and growth.
## LLY  (8 leads)
- Fri 20 Nov | Kalkine Media | What Did ObesityWeek Data Reveal for Eli Lilly (NYSE:LLY) Investors?
  https://kalkinemedia.com/us/stocks/healthcare/what-did-obesityweek-data-reveal-for-eli-lilly-nyselly-investors
  > - Eli Lilly lined up a broad ObesityWeek slate framed around moving obesity care beyond the scale - The data spanned an injectable mainstay, a watched oral medicine and earlier-stage metabolic compounds
- Fri 20 Nov | Trefis | What Does Eli Lilly Offer That Merck Does Not?
  https://www.trefis.com/stock/mrk/articles/627182/what-does-eli-lilly-offer-that-merck-does-not/2026-11-20
  > What Does Eli Lilly Offer That Merck Does Not? Today’s big story: Will 2027 Be A 2022 Repeat For Stocks? Merck (MRK) and Eli Lilly (LLY) are both owned for a few best-selling medicines. Merck’s KEYTRUDA cancer drugs sold $8.6 billion in the third quarter of 2026.
- Fri 20 Nov | Fierce Healthcare | Florida court tosses Tampa General Hospital's suit against Eli Lilly over 340B discounts
  https://www.fiercehealthcare.com/providers/tampa-general-hospital-sues-eli-lilly-over-pulled-340b-discounts
  > 19 at 1 p.m. A Florida federal court has tossed Tampa General Hospital's lawsuit against Eli Lilly over the 340B drug discount program. If Tampa General Hospital wants to file an amended complaint, it must do so within 30 days.
- Fri 20 Nov | Telehealth.org | Eli Lilly 340B Lawsuit: Hospitals Sue Over Patient Data Demands
  https://telehealth.org/news/eli-lilly-340b-lawsuit-massachusetts-hospitals-sue-over-data-demands-privacy-concerns/
  > Eli Lilly 340B Lawsuit: Key Takeaways for Clinicians - Five Massachusetts hospitals are suing Eli Lilly over requirements to share detailed prescription and claims data to retain federal 340B drug discounts.
- Fri 20 Nov | Simply Wall St | What Do Eli Lilly (LLY) Vendor Hack And Canada Approval Mean Now?
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/what-do-eli-lilly-lly-vendor-hack-and-canada-approval-mean-n/amp
- Thu 19 Nov | JournalArta | Eli Lilly GLP-1 Pill Foundayo Wins Canadian Approval
  https://journalarta.com/en/2026/11/20/eli-lilly-glp-1-pill-foundayo-canada-approval/
- Thu 19 Nov | Global Banking & Finance Review | Eli Lilly and Co falls 2.27% in Thursday's session
  https://www.globalbankingandfinance.com/eli-lilly-and-co-lly-falls-2026-11-19/
- Thu 19 Nov | Modern Healthcare | Judge tosses Tampa General’s 340B suit against Eli Lilly
  https://www.modernhealthcare.com/politics-regulation/mh-tampa-general-340b-lawsuit-lilly-dismissed/
Read 86 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: CLHO, ALCN, EAST, EGAL, AMOC.
