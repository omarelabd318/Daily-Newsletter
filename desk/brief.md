# Desk brief, Friday, November 27, 2026

Built by run_data.py. Work for the run, not for publication.

## Steps
- **intraday**: ok in 286s (GitHub Actions). GLOBAL week and month: hourly from TradingView, brent, gold_usd, dxy, btc
- **rates**: ok in 1s (GitHub Actions). Rates: VIX to 2026-11-25 (28.29); Treasury yields to 2026-11-25 (10-year 4.85%).
- **valuation**: ok in 25s (GitHub Actions). LLY: $1.32tn, P/E (last 12 months) 43.6, Forecast P/E (fiscal 2026) 39.0 (the four quarters to Sep 2026)
- **movers**: ok in 9s (GitHub Actions). Market values: 39 of 39 updated
- **calendar**: ok in 0s (GitHub Actions). 2027-02-10 LLY results  2026-12-31
- **indicators**: ok in 0s (GitHub Actions). indicators: 49 series; EGX30 turning down, RSI 43.8
- **fairvalue**: ok in 1s (GitHub Actions). fair value: 52 stocks, k 16.4%, median P/E 9.7; cheapest MASR +75%, ABUK +54%, AMOC +49%; dearest MOIN -66%, LCSW -68%, BTFH -69%
- **views**: ok in 0s (GitHub Actions). 2026-11-05-pound-firm: on track -> wrong  (Judged on its date: USD/EGP at 54.91 from 54.77 (+0.3%).)
- **results**: ok in 52s (GitHub Actions). 
- **news**: ok in 129s (GitHub Actions). 
- **leads**: ok in 82s (GitHub Actions). 
- **sources**: english.mubasher.info: 4 failed, 0 needed a retry (fetch_movers.py); query2.finance.yahoo.com: 4 failed, 0 needed a retry (fetch_intraday.py); data.sec.gov: 7 failed, 0 needed a retry (results_due.py); news.google.com: 0 failed, 9 needed a retry.

## What moved (latest close against the one before)
- EGX30 50,311.78 (-0.45%); EGX70 EWI 16,886.20 (-0.00%); USD/EGP 54.91 (+0.27%); Gold 21K 5,650.00 (+0.27%); Brent 96.57 (+2.07%); S&P 500 7,182.78 (-0.25%); Nasdaq 23,585.80 (-0.62%); Bitcoin 61,587.00 (+1.73%)
- Desk stocks that moved 3% or more (each needs its leads opened and a stock line in the research log): ORCL -5.1%, NVDA -3.9%, ORAS +3.5%, META +3.4%, AMZN -3.1%.
- Trend and momentum worth a mention (description only, never a reason on its own):
    - PHDC: In a downtrend: below its 50-day average, which is below the 200-day; RSI 42, neither stretched nor washed out; the 50-day average crossed below the 200-day today.
    - WMT: Turning up: above both its 50-day average (11.7% over) and its 200-day (10.7% over), though the 50-day is still below the 200-day; RSI 70, stretched after a run: above 70; momentum turned up today (MACD crossed its signal line).

## Movers that still need a reason (top five each way, 5% or more)
- EGX ACAP (A Capital Holding) +12.9%; EGX VERT (Vertika for Industry & Trade) +6.9%; EGX LUTS (Lotus For Agricultural Investments And Development) +6.5%; EGX MAAL (Marseilla Al Masreia Al Khalegeya for Holding Investment) +5.6%; EGX RAYA (Raya Holding for Financial Investments) +5.2%; EGX MPCI (Memphis Pharmaceutical & Chemical Industries) -6.2%; EGX CRST (Creast mark For Contracting) -6.1%; US HPQ (HP) +11.5%; US ASTS (AST SpaceMobile) +10.3%; US QXO (QXO) +8.6%; US CHTR (Charter Communications) +8.4%; US BSP (Bending Spoons S.p.A) +8.0%; US NTNX (Nutanix) -15.2%; US LRCX (Lam Research) -5.7%; US SNDK (Sandisk) -5.6%; US WSO.B (Watsco) -5.4%; US ORCL (Oracle) -5.1%

Leads for them (open before using; never guess a reason):
```
EGX: Mubasher's list failed (HTTP Error 401: Unauthorized); reading the session from TradingView
EGX: 2026-11-26 (TradingView's closes; Mubasher's list refused), 192 stocks
EGX week and month: EGX stocks trading at least EGP 1m a day on average (204)
US: 2026-11-26, 836 companies
US week and month: US companies worth $10bn or more (835)
EGX30 heatmap: 2026-11-26, 31 members
US heatmap: 2026-11-26, 100 members
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
- Wed 25 Nov | Menafn | 3 ديسمبر.. نهاية حق الاكتتاب في مضاعفة رأسمال جولدن تكس إلى نصف مليار جنيه
  https://menafn.com/arabic/1112019797/3-ديسمبر-نهاية-حق-الاكتتاب-في-مضاعفة-رأسمال-جولدن-تكس-إلى-نصف-مليار-جنيه
## KABO -3.2%  El Nasr Clothing & Textiles
- no headlines found

# US 2026-11-26
## HPQ +11.5%  HP
- Thu 26 Nov | Yahoo Finance | HP Stock Just Had Its Best Day Since May and Blew Past Wall Street’s Price Target
  https://finance.yahoo.com/markets/stocks/articles/hp-stock-just-had-best-200217012.html
  > - HP (HPQ) jumped 11% to $31 after guidance edged past consensus, the S&P 500's biggest gain, even as the index fell. - Goldman Sachs, Barclays and BofA raised targets but kept sell ratings, all below the close, while Bernstein called the beat "low-quality" over tariff refunds.
- Thu 26 Nov | 24/7 Wall St. | HP Stock Just Had Its Best Day Since May and Blew Past Wall Street’s Price Target
  https://247wallst.com/investing/2026/11/26/hp-stock-just-had-its-best-day-since-may-and-blew-past-wall-streets-price-target/
  > HP Stock Just Had Its Best Day Since May and Blew Past Wall Street’s Price Target This post may contain links from our sponsors and affiliates, and Flywheel Publishing may receive compensation for actions taken through them.
- Thu 26 Nov | TradingNEWS | HPQ Stock Price Forecast — HP Inc. (HPQ) ($31.15) $34 Upside Target on $16B Revenue Beat
  https://www.tradingnews.com/news/hp-inc-stock-forecast-hpq-jumps-1149-to-3115-on-earnings-beat-34-usd-target-in-sight
  > closes at $31.15, up 11.49%, after Q4 revenue of $16.0 billion beats the $15.3 billion consensus. - Memory and storage now make up 40% of HP's PC bill of materials, pushing PC margins down to 3.0% from 5.8%. [Figures on the page: first half; one quarter. Check which one each figure is.]
- Thu 26 Nov | StockStory | Stocks making big moves yesterday: Nutanix, Whirlpool, HP, Workday, and Autodesk
  https://stockstory.org/us/stocks/nasdaq/ntnx/news/why-it-moves-summary/stocks-making-big-moves-yesterday-nutanix-whirlpool-hp-workday-and-autodesk
  > Check out the companies making headlines yesterday: Nutanix: Hybrid multicloud computing company Nutanix (NASDAQ:NTNX) fell by 11.9% on Wednesday after the company reconfirmed in-line full-year revenue guidance alongside its fiscal first-quarter results and announced that CEO Rajiv Ramaswami will step down.
## ASTS +10.3%  AST SpaceMobile
- Fri 27 Nov | MarketBeat | 121,746 Shares in AST SpaceMobile, Inc. $ASTS Acquired by Entropy Technologies LP
  https://www.marketbeat.com/instant-alerts/filing-121746-shares-in-ast-spacemobile-inc-asts-acquired-by-entropy-technologies-lp-2026-11-27/
  > 121,746 Shares in AST SpaceMobile, Inc. $ASTS Acquired by Entropy Technologies LP - Entropy Technologies LP initiated a position in AST SpaceMobile, buying 121,746 shares worth approximately $7.17 million in the third quarter. Institutional investors collectively own 60.95% of the company.
- Fri 27 Nov | www.tokenpost.com | AST SpaceMobile Shares Rise 2.06% as Launch Delays Pressure Rebound
  https://www.tokenpost.com/news/investing/63386
  > AST SpaceMobile shares rose 2.06% over 24 hours to $27.21 as of 3:43 a.m. ET (08:43 UTC) Nov. 27, but thin volume and pressure below longer-term moving averages left the rebound unconfirmed. AST SpaceMobile (ASTS) traded between $26.60 and $28.11 during the observation window.
- Fri 27 Nov | Blockchain News | AST SpaceMobile (ASTS) Stock Price Prediction: Launch delays meet a fragile rebound setup
  https://blockchain.news/news/20261127-price-prediction-asts-launch-delays-meet-a-fragile-rebound
  > AST SpaceMobile (ASTS) is trying to hold a rebound after a weak stretch, but the setup is still fragile. The shares were at $27.21, up 2.06% over 24 hours, with the session range between $28.11 and $26.60.
- Fri 27 Nov | Investing.com | AST Spacemobile stock rating cut by Berenberg on launch delays, price target slashed to $30
  https://www.investing.com/news/analyst-ratings/ast-spacemobile-stock-rating-cut-by-berenberg-on-launch-delays-price-target-slashed-to-30-93CH-5053017
  (page: did not load (403))
## QXO +8.6%  QXO
- Thu 26 Nov | MarketBeat | QXO (NYSE:QXO) Shares Break Above Fifty Day Moving Average - Should You Sell?
  https://www.marketbeat.com/instant-alerts/price-qxo-nyse-qxo-shares-break-above-fifty-day-moving-average-should-you-sell-2026-11-26/
  > QXO (NYSE:QXO) Shares Break Above Fifty Day Moving Average - Should You Sell? - QXO shares moved above their 50-day moving average, trading as high as $12.21 and last at $11.965, compared with a 50-day average of $11.57. The stock remains below its 200-day average of $16.31.
- Thu 26 Nov | Yahoo Finance | QXO Inc. (QXO) Gets 9% Boost From Wall Street
  https://finance.yahoo.com/markets/stocks/articles/qxo-inc-qxo-gets-9-040757183.html
  > (NYSE:QXO) is one of the 10 Stocks Stealing the Spotlight. QXO saw its share price jump by 8.62 percent on Wednesday to end at $11.97 apiece after earning a bullish rating and a higher price target from BTIG.
- Wed 25 Nov | Yahoo Finance | QXO261127C00006000 Interactive Stock Chart | QXO Nov 2026 6.000 call Stock
  https://finance.yahoo.com/chart/QXO261127C00006000
  (page: did not load (404))
- Wed 25 Nov | Quiver Quantitative | QXO gains as investors digest strong Q3 results and fresh analyst support
  https://www.quiverquant.com/news/QXO+gains+as+investors+digest+strong+Q3+results+and+fresh+analyst+support
  > (QXO) is up 8.5% today. Here is some analysis on what might have caused this price movement. Analysis: The most likely driver appears to be a continued positive reaction to QXO’s recent third-quarter results, which showed sharp sales and adjusted EBITDA growth following major acquisitions. QXO, SEC, Google Finance
## CHTR +8.4%  Charter Communications
- Fri 27 Nov | MarketBeat | First Trust Advisors LP Purchases 453,797 Shares of Charter Communications, Inc. $CHTR
  https://www.marketbeat.com/instant-alerts/filing-first-trust-advisors-lp-purchases-453797-shares-of-charter-communications-inc-chtr-2026-11-27/
  > First Trust Advisors LP Purchases 453,797 Shares of Charter Communications, Inc. - First Trust Advisors increased its Charter Communications stake by 463.5% in the third quarter, buying 453,797 shares to hold 551,702 shares valued at about $61.2 million.
- Fri 27 Nov | cwibc.co.id | Charter Targets 2 Billion Dollars in Annual Cost Cuts
  https://cwibc.co.id/en/charter-two-billion-cost-cuts
  > Charter Targets 2 Billion Dollars in Annual Cost Cuts Charter Communications is pursuing a major operational restructuring following its combination with Cox Communications, targeting $2 billion in annualized expense reductions over 18 months.
- Thu 26 Nov | Kalkine Media | Could Charter Communications (NASDAQ:CHTR) Win More Spectrum Customers?
  https://kalkinemedia.com/us/stocks/communication/could-charter-communications-nasdaqchtr-win-more-spectrum-customers
  > - Charter set out a detailed calendar for the promotion. - Spectrum services reach numerous homes and businesses across multiple states. - Charter Communications, Inc. Charter Communications (NASDAQ:CHTR) Communication Services Charter Communications Inc (NASDAQ:CHTR) 147.23 USD +11.360 8.361% Last Updated at: 2026-11-25T21:00:00Z disclosed earlier this month, from its Stamford.
- Thu 26 Nov | Yahoo Finance | Why Charter Communications Stock Is Back In Focus After $2 Billion Cost Saving Plan
  https://finance.yahoo.com/markets/stocks/articles/why-charter-communications-stock-back-191436804.html
  > - Charter Communications recently reported third quarter 2026 revenue of US$14.922b alongside a shareholder loss of US$2.397b that was mainly driven by a US$6.326b non cash franchise impairment, while also outlining an Internet first operating model and integration progress following the Cox Communications acquisition.
## BSP +8.0%  Bending Spoons S.p.A
- Wed 25 Nov | MarketBeat | Top Bending Spoons (BSP) Competitors 2026
  https://www.marketbeat.com/stocks/NASDAQ/BSP/competitors-and-alternatives/
  (page: did not load (403))
- Wed 25 Nov | Yahoo! Finance Canada | Bending Spoons S.p.A. (BSP) Stock Price, News, Quote & History
  https://ca.finance.yahoo.com/quote/BSP/
  > - Previous Close  42.86 - Bid 34.00 x 100 - Ask 51.26 x 200 - Day's Range  39.95 - 46.42 - 52 Week Range  30.11 - 59.50 - Market Cap (intraday)  30.4B - Beta (5Y Monthly) -- - PE Ratio (TTM)  107.65 - EPS (TTM)  0.43
- Tue 24 Nov | MarketBeat | Stock Traders Purchase High Volume of Bending Spoons Call Options (NASDAQ:BSP)
  https://www.marketbeat.com/instant-alerts/options-stock-traders-purchase-high-volume-of-bending-spoons-call-options-nasdaq-bsp-2026-11-24/
  > Stock Traders Purchase High Volume of Bending Spoons Call Options (NASDAQ:BSP) - Traders bought 19,658 Bending Spoons call options on Tuesday, 607% above the typical volume of 2,779 contracts. - Bending Spoons shares fell $4.76 to $42.51 in Tuesday trading.
- Tue 24 Nov | GuruFocus | Bending Spoons (BSP) Stock Is Down 12.2% Today Without Company N
  https://www.gurufocus.com/news/9217706/bending-spoons-bsp-stock-is-down-122-today-without-company-news
  (page: did not load (403))
## NTNX -15.2%  Nutanix
- Fri 27 Nov | Simply Wall St | Nutanix (NTNX) Stock May Be 48% Undervalued Following CEO Succession Plan
  https://simplywall.st/stocks/us/software/nasdaq-ntnx/nutanix/news/nutanix-ntnx-stock-may-be-48-undervalued-following-ceo-succe
  > Nutanix has seen its share price swing sharply in recent months, which puts a spotlight on a simple question for investors who care about fundamentals: Are the cash flows that Nutanix can generate over time enough to support where the stock trades today?
- Thu 26 Nov | TradingNEWS | Nutanix Price Forecast — NTNX ($46.30) $54.59 Upside Target on CEO Exit Selloff
  https://www.tradingnews.com/news/nutanix-sinks-15-to-46-30-on-ceo-exit-despite-32-1-margin-beat-54-59-usd-gap-fill-in-view
  > - Nutanix fell 15.2% to $46.30 Wednesday on 13.6 million shares, five times its 2.72 million average. - Q1 revenue rose 15% to $772.4 million with a record 32.1% non-GAAP operating margin. - CEO Rajiv Ramaswami will step down by April 30, 2027, with no successor yet named.
- Thu 26 Nov | StockStory | Stocks making big moves yesterday: Nutanix, Whirlpool, HP, Workday, and Autodesk
  https://stockstory.org/us/stocks/nasdaq/ntnx/news/why-it-moves-summary/stocks-making-big-moves-yesterday-nutanix-whirlpool-hp-workday-and-autodesk
  > Check out the companies making headlines yesterday: Nutanix: Hybrid multicloud computing company Nutanix (NASDAQ:NTNX) fell by 11.9% on Wednesday after the company reconfirmed in-line full-year revenue guidance alongside its fiscal first-quarter results and announced that CEO Rajiv Ramaswami will step down. Is now the time to buy Nutanix?
- Thu 26 Nov | GuruFocus | Nutanix (NTNX) Stock: A Hidden Value Trap? Unpacking the Risks and Rewards
  https://www.gurufocus.com/news/9227812/nutanix-ntnx-stock-a-hidden-value-trap-unpacking-the-risks-and-rewards
  (page: did not load (403))
## LRCX -5.7%  Lam Research
- Fri 27 Nov | blockchain.news | Lam Research (LRCX) Stock Price Prediction: Rebound Attempt Faces Overhead Resistance After a Deep Pullback
  https://blockchain.news/news/20261127-price-prediction-lrcx-rebound-attempt-faces-overhead-resistance-after
  > What changed in the stock Lam Research (LRCX) is trying to stabilize after a sharp drawdown, with the shares last priced at $196.71, up 4.80% over 24 hours.
- Fri 27 Nov | Pluang | Lam Research sees 54% revenue jump, buy rating reiterated despite 50% stock drop
  https://pluang.com/en/news-feed/lam-research-deal-black-friday-terbaik-rating-beli-pertumbuhan-pendapatan
  (page: did not load (403))
- Thu 26 Nov | Yahoo Finance | Is Lam Research Corporation (LRCX) Oversold as Strong AI Demand Supports Recovery?
  https://finance.yahoo.com/markets/stocks/articles/lam-research-corporation-lrcx-oversold-194754377.html
  > We just published our list, 10 Most Oversold Semiconductor Stocks to Buy for 2027, and Lam Research Corporation ranked 6th on this list. The semiconductor sector has experienced heightened volatility in 2026, with several stocks retreating significantly from their 52-week highs.
- Thu 26 Nov | Kalkine Media | How Is Lam Research (NASDAQ:LRCX) Supporting the Next Generation of AI Talent?
  https://kalkinemedia.com/us/stocks/technology/how-is-lam-research-nasdaqlrcx-supporting-the-next-generation-of-ai-talent
  > - Lam Research and LEGO Education disclosed a multiyear partnership earlier this month following a ceremony at LEGO Group headquarters in Billund, Denmark. - The Lam Foundation is contributing a substantial sum several years to support hands-on STEM kits and resources that build computer science and AI literacy.
```

## Results to record (results_due.py)
- No new results waiting: every desk stock that reported in the period is recorded.
- lastResults written but set_results.py not run, so the P/E is still on the old quarter: TMGH, PHDC, SWDY, FWRY, HRHO, JUFO, ALCN, MFPC, EAST, EFIH, AMOC, EFID.
- Already recorded: COMI, ABUK, ETEL, ORAS, EMFD, BQDC, EGAL.

## Coming up (seven days)
- 2026-11-27 CLHO results (expected)
- 2026-11-27 EAST results (expected)  <- write its preview
- 2026-11-27 EFIH results (expected)  <- write its preview
- 2026-11-27 JUFO results (expected)
- 2026-12-02 ALCN results (expected)
- 2026-12-02 AMOC results (expected)
- 2026-12-02 EGAL results (expected)
- 2026-12-02 EMFD results (expected)
- 2026-12-02 NVDA dividend
- 2026-12-02 SKPC results (expected)

## Views
- due 2026-11-30: Telecom Egypt holds its ground into MSCI's November 30 inclusion (on track)
- due 2026-11-27: Developers lag while rates stay high (on track)
- due 2026-11-27: Money rotates from AI spenders to steady earners (on track)
- due 2026-11-30: Gas rationing keeps fertilizer stocks under pressure through November (on track)
- judged wrong with no lesson yet: The pound stays firmer than EGP 56 per dollar into the IMF review  <- write its `lesson`
    2026-11-05-pound-firm: on track -> wrong  (Judged on its date: USD/EGP at 54.91 from 54.77 (+0.3%).)

## Fair value
- Changed since the last run: ORWE +24% -> +43% (medium -> medium); SCEM +19% -> +23% (high -> medium); PHAR +20% -> -9% (low -> medium); RAYA +6% -> -16% (medium -> medium).
- In the ten cheapest or dearest with no note: AMOC, ORWE, EMFD, MCQE, ADIB, MHOT, MTIE, RAYA, AMIA, BINV.

## Due today
- Nothing beyond the daily steps.

## News leads by stock (stock_news.py; all leads for stocks that moved 2% or more, three for the rest)
News leads for the last 2 days, 2026-11-27. Open each story before using it.
## COMI  (6 leads)
- Fri 27 Nov | لحظات نيوز | اليورو صباح الجمعة: أبوظبي الإسلامي يبيع بـ60.3406 والتجاري الدولي بـ60.2802
  https://nl7za.com/economy/اليورو-صباح-الجمعة-أبوظبي-الإسلامي-يبيع-بـ60-3406-والتجاري-الدولي-بـ60-2802
  > اليورو يقف في ساحة الستين جنيهًا هذا الصباح، لكن الفروق بين البنوك لا تزال تتيح فرصة للمقارنة. أعلى سعر شراء يقدمه مصرف أبوظبي الإسلامي، 60.1046 جنيه، وهو أيضًا الأعلى بيعًا عند 60.3406. وفي المرتبة التالية بنك فيصل الإسلامي بـ60.06 للشراء و60.29 للبيع.
- Thu 26 Nov | شبكة تواصل الإخبارية | البنك التجاري الدولي CIB يتيح حساب MyCIB Minor للأطفال من سن 7 سنوات.. المزايا والشروط
  https://twaslnews1.twaslnews.com/8330264/
  (page: did not load (403))
- Thu 26 Nov | شبكة تواصل الإخبارية | «التجاري الدولي» يستحوذ على 39.1% من أرباح البنوك المدرجة بنهاية سبتمبر
  https://twaslnews1.twaslnews.com/8323230/
  (page: did not load (403))
## TMGH  (8 leads)
- Thu 26 Nov | كايرو لايف | بعد تأجيله بسبب حادث الوراق.. مجموعة طلعت مصطفى توضح مصير تذاكر حفل تامر حسني | بث مباشر
  https://www.cairolive24.com/2219918
  > بعد تأجيله بسبب حادث الوراق.. مجموعة طلعت مصطفى توضح مصير تذاكر حفل تامر حسني | بث مباشر
- Thu 26 Nov | https://www.youlyou.com/ | 30 مليون جنيه من هشام طلعت مصطفى وأحمد عز وياسين منصور لدعم ضحايا حريق الوراق
  https://www.youlyou.com/103490
  > 1- مجلس الوزراء يتلقى تبرعات بقيمة 30 مليون جنيه من 3 رجال أعمال لدعم ضحايا حريق الوراق. 2- هشام طلعت مصطفى يتبرع بـ10 ملايين جنيه لمساندة أسر ضحايا ومصابي الحادث. 3- أحمد عز يقدم 10 ملايين جنيه لدعم المتضررين من حريق الطريق الدائري. 4- ياسين منصور يتبرع بـ10 ملايين جنيه لأسر الضحايا والمصابين.
- Thu 26 Nov | برلمانى | 55 مليون جنيه من هشام طلعت مصطفى وأبو هشيمة والدجوى ومنصور وعز ومحمد لطفى.. مجلس الوزراء يتلقى تبرعات من ممثلي مجتمع الأعمال لمساندة أسر ضحايا حادث الوراق.. ومدبولى يوجه وزارة التضامن بتسليم التبرعات لأصحا
  https://www.parlmany.com/News/2/621686/55-مليون-جنيه-من-هشام-طلعت-مصطفى-وأبو-هشيمة-والدجوى
  > صرح المستشار محمد عادل، المتحدث الرسمي باسم رئاسة مجلس الوزراء، بأن مجلس الوزراء تلقي عدة مُبادرات من جانب ممثلي مجتمع الأعمال في إطار التدخل السريع لمُساندة جهود الدولة الداعمة للمُضارين من حادث الحريق أعلى الطريق الدائري بالوراق.
## ETEL  (8 leads)
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
  > أعلنت الشركة المصرية للاتصالات، عن مضاعفة قيمة تبرعات عملائها عبر محفظة «WE PAY» الإلكترونية لصالح الهلال الأحمر المصري ومستشفى أهل مصر ومستشفى الناس، دعمًا لمصابي حادث دائري الوراق.
- Thu 26 Nov | جريدة المال | «المصرية للاتصالات» تتحمل تكاليف الأدوية والمستلزمات الطبية لمصابي حادث الوراق
  https://almalnews.com/2149907/«المصرية-للاتصالات»-تتحمل-تكاليف-الأدوية-والمستلزمات-الطبية/
- Thu 26 Nov | جريدة الدستور | لضحايا حادث الوراق.. مضاعفة قيمة التبرعات من خلال محفظة WE Pay
  https://www.dostor.org/5792288
- Thu 26 Nov | موقع الموقع | المصرية للاتصالات تضاعف تبرعات عملائها عبر WE Pay لدعم مصابي حادث الوراق
  https://almawq3.com/المصرية-للاتصالات-تضاعف-تبرعات-عملائ/
- Thu 26 Nov | الاستاد الرياضي | المصرية للاتصالات توفر الأدوية والأجهزة الضرورية للمستشفيات بعد حادث الدائري
  https://www.alestad.com/169817/المصرية-للاتصالات-توفر-الأدوية-والأج/
## PHDC  (8 leads)
- Fri 27 Nov | اوان مصر | ضبط عامل تشطيبات سرق مجوهرات وأموالًا من فيلا بالم هيلز في 6 أكتوبر
  https://www.awanmasr.com/ضبط-عامل-تشطيبات-سرق-مجوهرات-وأموالًا/
  (page read: it never names the company, so probably not about it: skip)
- Thu 26 Nov | خاص عن مصر | "بالم هيلز" تتعثر في مشروع أبوظبي.. وياسين منصور يبحث عن أرض بديلة في الإمارات
  https://aboutmsr.com/بالم-هيلز-تتعثر-في-مشروع-أبوظبي-وياسي/
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 26 Nov | صحيفة اخبارنا | بالم هيلز: عقد مشروع أبوظبي لم يعد ساريا لعدم توصيل المرافق
  https://www.akhbrna.ae/economy/balm-hylz-aqd-mshrwa-abwzby/
  > أعلنت شركة بالم هيلز للتعمير أن عقد المساطحة الخاص بمشروعها في إمارة أبوظبي لم يعد ساريا، بعد انقضاء الموعد النهائي المحدد لاستيفاء الشروط المسبقة الواردة فيه.
## SWDY  (5 leads)
- Thu 26 Nov | جريدة باور نيوز الاخبارية | السويدي للمرافق توقع مذكرة تفاهم مع شنايدر إلكتريك لتعزيز التعاون في كفاءة الطاقة وتطوير الشبكات والتحول الرقمي
  https://powernews.cc/?p=295127
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Thu 26 Nov | بوابة التكنولوجيا المالية | «شنايدر إلكتريك» و«السويدي» توقعان اتفاقية شراكة لتطوير البنية التحتية وتسريع التحول الرقمي
  https://fintechgate.net/258588
  > تعزيز كفاءة وموثوقية حلول الطاقة «شنايدر إلكتريك» و«السويدي» توقعان اتفاقية شراكة لتطوير البنية التحتية وتسريع التحول الرقمي وقعت شركة شنايدر إلكتريك وشركة السويدي للمرافق (Elsewedy Utilities) اتفاقية شراكة، لإرساء إطار للتعاون طويل الأجل بين الشركتين، يشمل جميع مراحل دورة حياة البنية التحتية.
- Wed 25 Nov | FLAIR MAGAZINE | Alstom’s Chief Procurement Officer Meets Elsewedy Electric’s President to Explore Ways to Strengthen Industrial Cooperation and Expand Across Regional Markets
  https://flair-magazine.com/2026/11/25/alstoms-chief-procurement-officer-meets-elsewedy-electrics-president-to-explore-ways-to-strengthen-industrial-cooperation-and-expand-across-regional-markets/
  > Alstom’s Chief Procurement Officer, Nathalie Saint Martin, met today with Ahmed Elsewedy, President and CEO of Elsewedy Electric, to review the collaboration between the two companies and discuss its future potential.
## ORAS  (8 leads)
- Fri 27 Nov | Prop News Time | Orascom Construction completes OCI combination, issues 97,201,359 new shares
  https://propnewstime.com/latestnewsstories/NDEwNjk=/orascom-construction-completes-oci-combination-issues-97-201-359-new-shares
  > The Gulf conflict has disrupted global supply chains, pushed... REITs have changed the way commercial real estate is owned a... Orascom Construction PLC has completed its acquisition of OCI Rembrandt Holdings B.V. As consideration, Orascom Construction issued and allotted 97,201,359 new shares to OCI, lifting its issued share capital from 110,243,935 to 207,445,294 shares.
- Thu 26 Nov | EnterpriseAM | Orascom Construction closes OCI deal as NMDC Energy pushes into deepwater fabrication
  https://enterpriseam.com/menaplus/2026/11/27/orascom-construction-closes-oci-deal-as-nmdc-energy-pushes-into-deepwater-fabrication/
  > M&A WATCH- Nassef Sawiris’ two listed companies are back under the same roof: ADX- and EGX-listed Orascom Construction closed its acquisition of OCI Rembrandt Holdings from Dutch-listed OCI Global on Wednesday, according to statements (here, pdf and here, pdf).
- Thu 26 Nov | CNN الاقتصادية | «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي»
  https://cnnbusinessarabic.com/finance-markets/1153374/أوراسكوم-كونستراكشون-تنهي-الاستحواذ-على-أو-سي-آي
  > «أوراسكوم كونستراكشون» تنهي الاستحواذ على «أو سي آي» تاريخ النشر: قبل يومين 97.2 مليون سهم جديد.. كيف تتغير هيكلية أسهم «أوراسكوم كونستراكشون» بعد الاندماج؟ أكملت شركة «أوراسكوم كونستراكشون» عملية الاستحواذ على شركة «أو سي آي» من خلال شركتها «أو سي آي ريمبرانت هولدينغز»، وذلك في إطار عملية الاندماج التي سبق الإعلان عنها بين الشركتين.
- Thu 26 Nov | العربية | "أوراسكوم كونستراكشون" تتم عملية الاندماج مع "OCI" الهولندية
  https://www.alarabiya.net/aswaq/companies/2026/11/25/اوراسكوم-كونستراكشون-تتم-عملية-الاندماج-مع-oci-الهولندية-
  (page: did not load (403))
- Thu 26 Nov | The Globe and Mail | OCI Completes Sale to Orascom Construction
  https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/9014280/oci-completes-sale-to-orascom-construction/
- Thu 26 Nov | EnterpriseAM | أوراسكوم كونستراكشون تتم اندماجها مع "أو سي آي" مقابل 47% من أسهمها
  https://enterpriseam.com/egypt-ar/?post_type=issue&p=492471
- Wed 25 Nov | بوابة بلوم | باستثمارات 6.7 مليار دولار.. أوراسكوم كونستراكشون تضع حجر أساس مشروع تحلية مياه في الأردن
  https://bloom-gate.com/عقارات/باستثمارات-6-7-مليار-دولار-أوراسكوم-كون-2/
- Wed 25 Nov | Masrawy | أوراسكوم كونستراكشون تعلن إتمام الاستحواذ على شركة تابعة لـ"أو سي آي"
  https://www.masrawy.com/news/news_economy/details/2026/11/25/3084271/أوراسكوم-كونستراكشون-تعلن-إتمام-الاستحواذ-على-شركة-تابعة-لـ-أو-سي-آي-?amp
## FWRY  (3 leads)
- Thu 26 Nov | شبكة تواصل الإخبارية | تجارة أفريقيا البينية ترتفع 6% إلى 213.8 مليار دولار.. والمدفوعات الفورية تتضاعف 3 مرات
  https://twaslnews1.twaslnews.com/8349675/
  (page: did not load (403))
- Thu 26 Nov | الشرق بلومبرغ | تجارة أفريقيا البينية تنتعش والمدفوعات الرقمية الفورية تتضاعف 3 مرات
  https://asharqbusiness.com/amp/banks/158062/تجارة-أفريقيا-البينية-تنتعش-والمدفوعات-الرقمية-تتضاعف-3-مرات/
  > ارتفعت قيمة التجارة البينية بين دول أفريقيا بنحو 6% العام الماضي لتبلغ 213.8 مليار دولار، لكنها لم تشكل سوى 14.6% من إجمالي تجارة القارة، في ظل التحديات التي تعترض التكامل الاقتصادي الإقليمي، وفقاً لدراسة.
- Wed 25 Nov | بوابة التكنولوجيا المالية | «اكويتي» و«بوتيم» تتيحان تمويل حسابات التداول والاستثمار عبر خدمة الدفع الفوري «آني» في الإمارات
  https://www.fintechgate.net/258546
  > «اكويتي» و«بوتيم» تتيحان تمويل حسابات التداول والاستثمار عبر خدمة الدفع الفوري «آني» في الإمارات
## HRHO  (2 leads)
- Thu 26 Nov | الشرق بلومبرغ | "إي إف جي هيرميس" تتوسع في استشارات الديون مع تباطؤ الاكتتابات
  https://asharqbusiness.com/amp/financing-and-investment/157880/ركود-الاكتتابات-بالشرق-الأوسط-يدفع-efg-نحو-استشارات-الديون/
  > يدفع تباطؤ سوق طروحات الأسهم الجديدة في الشرق الأوسط، التي كانت يوماً مزدهرة، حتى أحد أبرز مستشاري الاكتتابات العامة الأولية في المنطقة إلى التوسع نحو مجالات أخرى.
- Wed 25 Nov | Bloomberg | Mideast IPO Slump Prompts EFG to Branch Out Into Debt Advisory
  https://www.bloomberg.com/news/articles/2026-11-25/mideast-ipo-slump-prompts-efg-to-branch-out-into-debt-advisory
  (page: did not load (403))
## EFIH  (2 leads)
- Thu 26 Nov | أهل مصر | إي فاينانس تنعي ضحايا حادث الدائري ـ الوراق
  https://ahlmasrnews.com/news/technology/13507424/إي-فاينانس-تنعي-ضحايا-حادث-الدائري-ـ-الوراق
  > نعت مجموعة إي فاينانس للاستثمارات المالية والرقمية ضحايا حادث الدائري ـ الوراق الأليم بكل مشاعر الحزن والأسى. وتتقدم مجموعة إي فاينانس برئاسة إبراهيم سرحان رئيس مجلس الإدارة بخالص التعازي والمواساة لأسر الضحايا، داعين الله أن يتغمدهم بواسع رحمته، وأن يمنّ على المصابين بالشفاء العاجل.
- Wed 25 Nov | بوابة التكنولوجيا المالية | الحكومة المصرية تستهدف توظيف قدرات «إي فاينانس» و«إي تاكس» للتوسع في تطبيقات الذكاء الاصطناعي وتطوير الخدمات الحكومية
  https://fintechgate.net/258472
  > «كجوك»: الذكاء الاصطناعي محور رئيسي في خطة التحول الرقمي وتسجيل نحو 4 ملايين عقار إلكترونيًا الحكومة المصرية تستهدف توظيف قدرات «إي فاينانس» و«إي تاكس» للتوسع في تطبيقات الذكاء الاصطناعي وتطوير الخدمات الحكومية
## EMFD  (1 leads)
- Thu 26 Nov | أصول مصر | الأسهم العقارية بالبورصة المصرية.. مدينة مصر وإعمار مصر تتصدران الارتفاعات الخميس
  https://www.osoulmisrmagazine.com/453519
  > الأسهم العقارية بالبورصة المصرية.. مدينة مصر وإعمار مصر تتصدران الارتفاعات الخميس سجلت أسهم الشركات العقارية المقيدة بالبورصة المصرية أداءً إيجابيًا خلال ختام تعاملات جلسة اليوم الخميس، إذ ارتفعت أسعار أسهم 5 شركات، مقابل تراجع سهمين، بينما استقرت 3 أسهم دون تغيير.
## BQDC  (8 leads)
- Fri 27 Nov | الجمهور الإخباري | بنك القاهرة يطلق شركاء SME+ لتقديم عروض حصرية للمشروعات الصغيرة والمتوسطة
  https://www.algomhor.com/518801
  > بنك القاهرة يطلق شركاء SME+ لتقديم عروض حصرية للمشروعات الصغيرة والمتوسطة أعلن بنك القاهرة عن إطلاق شبكة شركاء SME+، وذلك خلال حفل توقيع اتفاقيات تعاون مع عدد من مقدمي الخدمات، في خطوة استراتيجية جديدة تستهدف تعزيز منظومة الخدمات غير المالية وتوسيع نطاق القيمة المضافة المقدمة لعملائه من أصحاب المشروعات الصغيرة والمتوسطة.
- Thu 26 Nov | بوابة بلوم | شروط قرض السيارة من بنك القاهرة حتى 6 ملايين جنيه
  https://bloom-gate.com/أسواق/شروط-قرض-السيارة-من-بنك-القاهرة-حتى-6-مل-3/
  > شروط قرض السيارة من بنك القاهرة حتى 6 ملايين جنيه يقدم بنك القاهرة قرض السيارة الجديدة بتمويل يصل إلى 100% من قيمة السيارة، وبحد أقصى 6 ملايين جنيه، مع فترة سداد تمتد إلى 8 سنوات، وسعر فائدة متناقص يبلغ 26%.
- Thu 26 Nov | elnabaa elwatany newspaper | «بنك القاهرة» يطلق منظومة «SME+».. مزايا حصرية وخدمات متخصصة تفتح آفاقا جديدة
  https://www.elnabaa.net/1205445
  > «بنك القاهرة» يطلق منظومة «SME+».. مزايا حصرية وخدمات متخصصة تفتح آفاقا جديدة
## EGAL  (4 leads)
- Thu 26 Nov | جريدة باور نيوز الاخبارية | وفد رفيع المستوى من الاتحاد العام لنقابات عمال مصر في زيارة ميدانية لشركة مصر للألومنيوم بنجع حمادي
  https://powernews.cc/?p=295167
  (page: only 8 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Wed 25 Nov | شبكة تواصل الإخبارية | مصر للألومنيوم وفتنس برايم في المقدمة.. إنذارات وتنبيهات من البورصة لـ11 شركة
  https://twaslnews1.twaslnews.com/8293095/
  (page: did not load (403))
- Wed 25 Nov | إقرأ نيوز | بينها مصر للألومنيوم.. لجنة القيد بالبورصة توجه إنذارات وتنبيهات لـ11 شركة لمخالفة قواعد القيد
  https://www.iqraa.news/266594/بينها-مصر-للألومنيوم-لجنة-القيد-بالبو/
  > لجنة القيد بالبورصة توجه إنذارات وتنبيهات لـ11 شركة لمخالفة قواعد القيد. قررت لجنة القيد بالبورصة المصرية، خلال جلستها المنعقدة بتاريخ 24 نوفمبر 2026، توجيه إنذارات وتنبيهات إلى 11 شركة مقيدة، لمراعاة أحكام قواعد قيد وشطب الأوراق المالية والإجراءات التنفيذية، وذلك وفقًا للضوابط المنظمة لعمل الشركات المقيدة. إنذار وتنبيه 11 شركة بالبورصة المصرية
## EFID  (8 leads)
- Thu 26 Nov | أصول مصر | إيديتا تضخ 25 مليون دولار في العراق لإنشاء مصنع جديد
  https://www.osoulmisrmagazine.com/453511
  > إيديتا تضخ 25 مليون دولار في العراق لإنشاء مصنع جديد تعتزم شركة إيديتا للصناعات الغذائية ضخ استثمارات بقيمة 25 مليون دولار في السوق العراقية، بالتعاون مع مؤسسة التمويل الدولية (IFC)، لإنشاء مصنع جديد وتشغيل خطوط إنتاج إضافية، بما يرفع طاقتها الإنتاجية في العراق إلى أكثر من مثلي مستواها الحالي خلال العامين المقبلين.
- Thu 26 Nov | شبكة تواصل الإخبارية | «إيديتا» تحصل على 25 مليون دولار قرض من «التمويل الدولية» للتوسع في العراق
  https://twaslnews1.twaslnews.com/8334684/
  (page: did not load (403))
- Thu 26 Nov | جريدة حابي | إيديتا تستثمر 25 مليون دولار لمضاعفة طاقتها الإنتاجية في العراق بالشراكة مع IFC
  https://hapijournal.com/2026/11/26/إيديتا-تستثمر-25-مليون-دولار-لمضاعفة-طاق/
  > رنا ممدوح _ أعلنت شركة إيديتا للصناعات الغذائية ومؤسسة التمويل الدولية (IFC)، عن استثمار بقيمة 25 مليون دولار للتوسع في تصنيع الأغذية محليًا في العراق، وتوفير فرص عمل، وتعزيز سلاسل التوريد المحلية. استكمال تشغيل خطوط إنتاج جديدة ومصنع جديد في العراق خلال العامين المقبلين
- Thu 26 Nov | Dealroom | Edita takes $25M IFC loan to double Iraq food output
  https://app.dealroom.co/news/note/edita-takes-25m-ifc-loan-to-double-iraq-food-output
  (page: did not load (403))
- Thu 26 Nov | Milling Middle East & Africa | Edita, IFC partner in US$25M investment to expand food manufacturing in Iraq
  https://millingmea.com/edita-ifc-partner-in-us25m-investment-to-expand-food-manufacturing-in-iraq/
- Thu 26 Nov | موقع الحرية الإخباري | عمومية «إيديتا» غير العادية تبحث تخفيض رأس المال في 27 ديسمبر
  https://alhorianews.com/عمومية-إيديتا-غير-العادية-تبحث-تخفي/
- Thu 26 Nov | Pioneers Misr | إيديتا تضخ 25 مليون دولار في توسعاتها بالعراق خلال عامين.. وتستهدف مضاعفة الطاقة الإنتاجية
  https://pioneersmisr.com/124478/
- Thu 26 Nov | https://www.youlyou.com/ | إيديتا تدعو لجمعية غير عادية لمناقشة تخفيض رأس المال وإعدام أسهم خزينة
  https://www.youlyou.com/103278
## AAPL  (8 leads)
- Fri 27 Nov | MarketBeat | Apple Inc. $AAPL Stock: Legacy Wealth Management LLC MS Decreases Holdings
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-stock-legacy-wealth-management-llc-ms-decreases-holdings-2026-11-27/
  > $AAPL Stock: Legacy Wealth Management LLC MS Decreases Holdings - Legacy Wealth Management LLC MS cut its Apple stake by 39.8% in the third quarter, selling 43,713 shares and ending the period with 66,083 shares valued at about $22.0 million. Apple remained its third-largest portfolio holding, and institutional investors owned 67.73% of the stock.
- Fri 27 Nov | Benzinga | Telegram Slams Apple, Google Over 30% App Store Fees: ‘Still Beg You to Pay for Cloud Storage on a $1,200 Phone’
  https://www.benzinga.com/markets/tech/26/11/63666322/telegram-apple-google-app-store
  (page: did not load (403))
- Fri 27 Nov | MarketBeat | Apple Inc. $AAPL Shares Newly Purchased by First Nebraska Trust Co
  https://www.marketbeat.com/instant-alerts/filing-apple-inc-aapl-shares-newly-purchased-by-first-nebraska-trust-co-2026-11-27/
  > $AAPL Shares Newly Purchased by First Nebraska Trust Co - First Nebraska Trust Co. bought 275,814 Apple shares in the third quarter, worth about $91.8 million. Apple now represents 7.6% of the trust’s portfolio and is its second-largest holding.
## MSFT  (8 leads)
- Fri 27 Nov | Kalkine Media | Has Bytes Technology (LSE:BYIT) Turned the Corner Now Microsoft's Incentive Changes Have Annualised?
  https://kalkinemedia.com/uk/stocks/technology/has-bytes-technology-lsebyit-turned-the-corner-now-microsofts-incentive-changes-have-annualised
  > - Bytes Technology grew revenue, gross earnings and operating earnings in its interim period. - Chief executive Sam Mudd credited last year's strategic changes for the improvement.
- Fri 27 Nov | Yahoo Finance | Is Microsoft (MSFT) Fully Valued Following Its Atos Sovereign Cloud Deal?
  https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-fully-valued-following-090939545.html
  > Microsoft (MSFT) is back in focus after extending its collaboration with Atos to build sovereign cloud and AI environments for European public sector and regulated clients, raising fresh questions about how this partnership fits into the recent pullback in the stock.
- Fri 27 Nov | Blockchain News | Microsoft (MSFT) Stock Price Prediction: Profit growth meets a soft tape at a key pivot
  https://blockchain.news/news/20261127-price-prediction-msft-profit-growth-meets-a-soft-tape
  > Earnings momentum is intact, but price action has cooled Microsoft’s latest reported quarter, for the period ended September 30, 2026, showed revenue of $92.3 billion, up 19% year over year, operating income of $45.9 billion, up 21%, and non-GAAP diluted EPS of $4.89, up 18%.
## NVDA  (8 leads)
- Fri 27 Nov | Investing.com | Why is NVIDIA stock rallying today?
  https://www.investing.com/news/stock-market-news/why-is-nvidia-stock-rallying-today-93CH-5053241
  (page: did not load (403))
- Fri 27 Nov | The Motley Fool | Nvidia Forecast $130 Billion in Revenue and Added $150 Billion to Its Buyback. Should You Buy the Stock?
  https://www.fool.com/investing/2026/11/27/nvidia-forecast-usd130-billion-in-revenue-and-added-usd150-billion-to-its-buyback-should-you-buy-the-stock/
  > Nvidia (NVDA -3.91%) has a handful of problems right now. Although its chief executive officer, Jensen Huang, is back in his former position, there are still questions about his activities and whether any of Nvidia's technology or products made their way into China's hands unlawfully.
- Fri 27 Nov | SFGATE | Edsource: California Teacher Pension Fund Vulnerable To Stock Markets Nvidia-Fueled Ai Turmoil
  https://www.sfgate.com/news/bayarea/article/edsource-california-teacher-pension-fund-22552007.php
  (page: only 35 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | Seeking Alpha | Nvidia: Sell The Rallies, The Parabolic Gains Are Gone
  https://seekingalpha.com/article/4972476-nvidia-sell-the-rallies-the-parabolic-gains-are-gone
  (page: did not load (403))
- Fri 27 Nov | shattered.io | Eugene Files KRW 50B Tesla-NVIDIA ELS Terms
  https://shattered.io/eugene-investment-series-607-els-tesla-nvidia-krw-50-billion-nov-27/
- Fri 27 Nov | Trefis | How Much Of Big Tech’s AI Spending Reaches Nvidia? About 25 Cents, Not 52
  https://www.trefis.com/stock/nvda/articles/628220/how-much-of-big-tech-s-ai-spending-reaches-nvidia-about-25-cents-not-52/2026-11-27
- Fri 27 Nov | Yahoo Finance | Nvidia, AI Fears Jolt Markets: Market Snapshot
  https://finance.yahoo.com/video/nvidia-ai-fears-jolt-markets-082748065.html
- Fri 27 Nov | TradingView | NVDA: Nvidia Stock Tops $155 as Bargain Hunters Pile In Despite Export Concerns
  https://www.tradingview.com/news/tradingview:88142b4f2094b:0-nvda-nvidia-stock-tops-155-as-bargain-hunters-pile-in-despite-export-concerns/
## AMZN  (8 leads)
- Fri 27 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: Hoertkorn Richard Charles Increases Position
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-hoertkorn-richard-charles-increases-position-2026-11-27/
  > $AMZN Stock: Hoertkorn Richard Charles Increases Position - Hoertkorn Richard Charles increased its Amazon stake by 110.9% in the third quarter, buying 3,590 shares to hold 6,827 shares valued at about $1.7 million. - Analyst sentiment is broadly positive: MarketBeat reports a “Moderate Buy” consensus and an average price target of $320.73.
- Fri 27 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock: Bryn Mawr Trust Advisors LLC Grows Holdings
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-bryn-mawr-trust-advisors-llc-grows-holdings-2026-11-27/
  > $AMZN Stock: Bryn Mawr Trust Advisors LLC Grows Holdings - Bryn Mawr Trust Advisors increased its Amazon stake 29.8% in the third quarter, adding 34,067 shares to reach 148,234 shares valued at about $36.9 million. - Institutional investors and hedge funds own 72.2% of Amazon shares.
- Fri 27 Nov | MarketBeat | Amazon.com, Inc. $AMZN Stock Purchased by Brighton Jones LLC
  https://www.marketbeat.com/instant-alerts/filing-amazoncom-inc-amzn-stock-purchased-by-brighton-jones-llc-2026-11-27/
  > $AMZN Stock Purchased by Brighton Jones LLC - Brighton Jones increased its Amazon stake by 0.5% in the third quarter, adding 21,049 shares to hold about 4.06 million shares worth $1.01 billion. Amazon represents 17.6% of the firm’s portfolio and is its largest holding.
- Fri 27 Nov | Blockchain News | Amazon (AMZN) Stock Price Prediction: Analysts stay constructive as price action tests support after AI-spend pressure
  https://blockchain.news/news/20261127-price-prediction-price-amzn-analysts-stay-constructive-as-action-tests
  > Price action is stabilizing, but the burden of proof is still on buyers Amazon (AMZN) is trading at $252.00, with the session’s 24-hour range spanning $245.93 to $252.12. That leaves the stock back above the $250.02 pivot point, but still capped by nearby resistance at $254.10 and stronger resistance at $256.21.
- Fri 27 Nov | JournalArta | Amazon stock slides 3.12% to $244.43 in tech pullback
  https://journalarta.com/en/2026/11/27/amazon-shares-slide-3-12-as-five-day-selloff-deepens-correction/
- Fri 27 Nov | Yahoo Finance | Amazon Lost 40 Satellites on a Boeing-Lockheed Rocket in November. SpaceX Is the Only Company That Can Fix Amazon’s Problem. Is the Stock a Buy Near $130?
  https://finance.yahoo.com/markets/stocks/articles/amazon-lost-40-satellites-boeing-035302826.html
- Fri 27 Nov | Yahoo Finance | Can Amazon (AMZN) Turn Its AWS Growth Outlook Into Cash?
  https://finance.yahoo.com/markets/stocks/articles/amazon-amzn-turn-aws-growth-035240906.html
- Thu 26 Nov | TIKR.com | Stanley Druckenmiller, Bill Ackman and 7 Other Famous Investors Own Amazon. Here’s Who Bought and Sold Recently
  https://www.tikr.com/blog/stanley-druckenmiller-bill-ackman-and-7-other-famous-investors-own-amazon-heres-who-bought-and-sold-recently
## GOOGL  (8 leads)
- Fri 27 Nov | Wisevoter | Alphabet Stock Slides Amid AI Spending Concerns
  https://wisevoter.com/world/us/2026/11/27/alphabet-stock-decline-ai-spending-cash-flow
  > Alphabet Stock Slides Amid AI Spending Concerns Shares have fallen 33.2% from their 52-week high as investors weigh heavy AI infrastructure costs against weaker free cash flow. 27, 2026 in Public Companies Alphabet's stock has declined 21.3% over the past three months, with its market capitalization near $3.4 trillion.
- Fri 27 Nov | Barchart.com | How Is Alphabet’s Stock Performance Compared to Other Mega-Caps?
  https://www.barchart.com/story/news/9028542/how-is-alphabets-stock-performance-compared-to-other-mega-caps
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | ad-hoc-news.de | Alphabet stock gains 1.75% to EUR 255.23 before Xetra
  https://www.ad-hoc-news.de/boerse/news/vorboerse/alphabet-stock-gains-1-75-to-eur-255-23-before-xetra/70561278
  > Alphabet is the parent company of Google, with operations spanning search, cloud and advertising. On Xetra, the stock closed at EUR 250.85 on Thursday, November 26, 2026. Alphabet's Business Remains Broad
- Fri 27 Nov | Blockchain News | Alphabet (GOOGL) Stock Price Prediction: Oversold rebound faces resistance after Q3 margin-heavy AI spend
  https://blockchain.news/news/20261127-price-prediction-googl-oversold-rebound-faces-resistance-after-q3
  > What the tape is saying now GOOGL shares are trying to stabilize after a sharp pullback from higher levels, with the current price at $280.48 versus a 20-day SMA of $284.42 and a 50-day SMA of $304.98.
- Fri 27 Nov | TradingView | Price to cash flow ratio of Alphabet Inc. Class A – GPW:GOGL_C
  https://www.tradingview.com/symbols/GPW-GOGL_C/financials-statistics-and-ratios/price-cash-flow/
- Fri 27 Nov | TradingView | Debt to equity ratio of Alphabet Inc. Class A – GPW:GOGL_C
  https://www.tradingview.com/symbols/GPW-GOGL_C/financials-statistics-and-ratios/debt-to-equity/
- Fri 27 Nov | TradingView | Operating cash flow per share of Alphabet Inc. Class A – GPW:GOGL_C
  https://www.tradingview.com/symbols/GPW-GOGL_C/financials-statistics-and-ratios/operating-cash-flow-per-share/
- Fri 27 Nov | FourWeekMBA | Google Paid $23 a Share for Mandiant; Alphabet Is Up 146.3%
  https://fourweekmba.com/ai-google-paid-23-a-share-for-mandiant-alphabet-is-up-146-3/
## META  (8 leads)
- Fri 27 Nov | MarketBeat | Meta Platforms, Inc. $META Stock: Dodge & Cox Increases Stake
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-dodge-cox-increases-stake-2026-11-27/
  > $META Stock: Dodge & Cox Increases Stake - Dodge & Cox increased its Meta stake by 1.7% in the third quarter, adding 108,162 shares to reach 6.6 million shares, worth about $4.78 billion. Meta represents 2.6% of the fund’s portfolio and is its sixth-largest holding.
- Fri 27 Nov | MarketBeat | Meta Platforms, Inc. $META Stock Acquired by Empirical Finance LLC
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-acquired-by-empirical-finance-llc-2026-11-27/
  > $META Stock Acquired by Empirical Finance LLC - Empirical Finance increased its Meta stake by 2.2% in the third quarter, adding 1,712 shares to hold 78,732 shares worth about $57.1 million. Meta is 2.3% of the firm’s portfolio and its seventh-largest position.
- Fri 27 Nov | MarketBeat | Meta Platforms, Inc. $META Stock Acquired by Douglass Winthrop Advisors LLC
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-acquired-by-douglass-winthrop-advisors-llc-2026-11-27/
  > $META Stock Acquired by Douglass Winthrop Advisors LLC - Douglass Winthrop Advisors increased its Meta stake by 1,051.8% in the third quarter, adding 131,205 shares to hold 143,679 shares valued at about $104.2 million.
- Fri 27 Nov | MarketBeat | Meta Platforms, Inc. $META Stock: Flputnam Investment Management Co. Grows Stake
  https://www.marketbeat.com/instant-alerts/filing-meta-platforms-inc-meta-stock-flputnam-investment-management-co-grows-stake-2026-11-27/
  > $META Stock: Flputnam Investment Management Co. - Flputnam Investment Management increased its Meta stake by 55.4% in the third quarter, to 119,393 shares valued at about $86.6 million. Institutional investors own 79.91% of the company’s stock.
- Fri 27 Nov | MarketBeat | Cornermen Financial LLC Acquires New Holdings in Meta Platforms, Inc. $META
  https://www.marketbeat.com/instant-alerts/filing-cornermen-financial-llc-acquires-new-holdings-in-meta-platforms-inc-meta-2026-11-27/
- Fri 27 Nov | MarketBeat | 29,328 Meta Platforms, Inc. $META Shares Purchased by Empowered Funds LLC
  https://www.marketbeat.com/instant-alerts/filing-29328-meta-platforms-inc-meta-shares-purchased-by-empowered-funds-llc-2026-11-27/
- Fri 27 Nov | AOL.com | Michael Burry Shares Stark Warning About AI Boom, as Nvidia, Oracle and Meta Face Surging Debt Insurance Costs
  https://www.aol.com/articles/michael-burry-shares-stark-warning-083128000.html
- Fri 27 Nov | Kalkine India | Meta Platforms Balance Sheet: Cash, Debt and Equity Explained
  https://www.kalkine.co.in/article/technology/meta-platforms-inc-nasdaq-meta-debt-of-usd-11209b-and-cash-of-usd-8305b-define-the-latest-balance-sheet
## TSLA  (8 leads)
- Fri 27 Nov | MarketBeat | Tesla, Inc. $TSLA Stock: CSM Advisors LLC Cuts Holdings
  https://www.marketbeat.com/instant-alerts/filing-tesla-inc-tsla-stock-csm-advisors-llc-cuts-holdings-2026-11-27/
  > $TSLA Stock: CSM Advisors LLC Cuts Holdings - CSM Advisors cut its Tesla stake by 4.3% in the third quarter, selling 3,801 shares and ending the period with 85,510 shares worth about $30.3 million. Hedge funds and other institutions collectively owned 66.2% of Tesla stock.
- Fri 27 Nov | Blockonomi | Tesla Shares Regain Key Levels but Can TSLA Break the $400 Barrier?
  https://blockonomi.com/tesla-shares-regain-key-levels-but-can-tsla-break-the-400-barrier/
  > - Tesla shares climbed 1.77% to $389.81, surpassing four major moving averages during early market trading. - Trading volume reached only 18% of its five-day average, indicating limited participation in Tesla’s recovery. - Technical indicators placed immediate TSLA resistance at $393.96, while stronger support stood near $377.15. [Figures on the page: unaudited or preliminary; one quarter. Check which one each figure is.]
- Fri 27 Nov | TradingKey | Tesla Volatility Intensifies as Breakout Above $415 May Trigger Trend Reversal
  https://www.tradingkey.com/analysis/stocks/us-stocks/262324974-tesla-swings-widen-breakout-above-415-could-trigger-trend-reversal-tradingkey
  > Tesla Volatility Intensifies as Breakout Above $415 May Trigger Trend Reversal Tesla shares are consolidating near $380 amid high volatility, supported by strong buying near $360. A primary catalyst is speculation surrounding a potential all-stock merger with SpaceX, which could create a $3.5 trillion enterprise combining AI, robotics, EVs, and aerospace.
## JPM  (8 leads)
- Fri 27 Nov | Benzinga | JPMorgan Reportedly Spots Bitcoin ‘Capitulation’ Signal in Michael Saylor’s Strategy as MSTR Stock Hits 52-Week Low
  https://www.benzinga.com/crypto/cryptocurrency/26/11/63666295/strategy-mstr-bitcoin-capitualtion-jpmorgan-analysts
  (page: did not load (403))
- Fri 27 Nov | TheStreet | JPMorgan Chase launches 2-week mortgage rate sale
  https://www.thestreet.com/real-estate/jpmorgan-chase-launches-2-week-mortgage-rate-sale
  (page: did not load (403))
- Fri 27 Nov | ad-hoc-news.de | Allianz stock: JPMorgan lifts target to EUR 475
  https://www.ad-hoc-news.de/boerse/news/corporate-news/allianz-stock-jpmorgan-lifts-target-to-eur-475/70561565
  > JPMorgan raised its price target for Allianz on November 27, 2026, while retaining a Neutral rating, according to MarketScreener with dpa-AFX Analyser. Analyst Farooq Hanif lifted the target from EUR 460 to EUR 475.
## XOM  (8 leads)
- Fri 27 Nov | Trend News Agency | Azerbaijan ratifies Middle Kura oil and gas agreement with ExxonMobil
  https://www.trend.az/azerbaijan/4251325.html
  > BAKU, Azerbaijan, November 27. ExxonMobil Exploration Production Azerbaijan Limited will explore for oil and gas in Azerbaijan's Middle Kura contract area following Parliament's ratification of the agreement on exploration, development, and production sharing, Trend's correspondent reports.
- Fri 27 Nov | Investing.com South Africa | Form 4 ExxonMobil Holdings Corporation: Staale Gjervik (Executive Officer) For: 23 November By Investing.com
  https://za.investing.com/news/stock-market-news/form-4-exxonmobil-holdings-corporation-staale-gjervik-executive-officer-for-23-november-93CH-4598439
  (page: did not load (403))
- Fri 27 Nov | Guyana Chronicle | Ann’s Grove bid to bring home ExxonMobil Under-18 boys’ title
  https://guyanachronicle.com/2026/11/27/anns-grove-bid-to-bring-home-exxonmobil-under-18-boys-title/
  (page: did not load (307))
## AVGO  (8 leads)
- Fri 27 Nov | Investing.com | Why is Broadcom stock rallying today?
  https://www.investing.com/news/stock-market-news/why-is-broadcom-stock-rallying-today-93CH-5053249
  (page: did not load (403))
- Fri 27 Nov | Blockchain News | Broadcom (AVGO) Stock Price Prediction: Broadcom stabilizes above short-term support after a sharp November reset
  https://blockchain.news/news/20261127-price-prediction-avgo-broadcom-stabilizes-above-short-term-support
  > Price action: rebound, but not a clean reversal Broadcom (AVGO) traded at $312.78, up 2.96% over the latest 24-hour window, with a range of $302.22 to $316.60.
- Fri 27 Nov | ad-hoc-news.de | Broadcom stock at EUR 285.35, up 4.16% before Xetra opens
  https://www.ad-hoc-news.de/boerse/news/vorboerse/broadcom-stock-at-eur-285-35-up-4-16-before-xetra-opens/70561232
  > Broadcom is scheduled to release fiscal 2026 fourth-quarter and full-year results on Wednesday, December 9. On Xetra, the stock closed at EUR 273.95 on Thursday, November 26, 2026. Broadcom stock before the market opens
## BRK.B  (8 leads)
- Fri 27 Nov | ad-hoc-news.de | Argus Steps Back as Berkshire Prices Five Yen Tranches and Oregon Justices Reopen PacifiCorp Review
  https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/argus-steps-back-as-berkshire-prices-five-yen-tranches-and-oregon-justices-reopen-pacificorp-review/70561573
  > Berkshire Hathaway picked up a rare bit of negative analyst attention this week, with Argus Research cutting the conglomerate to Hold from Buy on 20 November. The stated reason was valuation rather than any fresh concern about the business: the shares, in Argus's view, had simply run past its price target.
- Fri 27 Nov | blockchain.news | Berkshire Hathaway (BRKB) Stock Price Prediction: Berkshire Hathaway holds above near-term support as analysts diverge on valuation
  https://blockchain.news/news/20261127-price-prediction-brkb-berkshire-hathaway-holds-above-near-term
  > Price action is holding, but not convincingly breaking out Berkshire Hathaway (BRKB) last traded at $581.32, down 0.23% on the day, with the 24-hour range compressed between $583.08 and $580.27. That puts the stock almost exactly on top of the $581.56 pivot, with immediate support at $580.03 and stronger support at $578.75.
- Fri 27 Nov | Yahoo Finance | Berkshire Cut Chevron By About a Third This Year and Kept Occidental. What Does That Say About Oil Prices?
  https://finance.yahoo.com/energy/articles/berkshire-cut-chevron-third-kept-085000850.html
  > Berkshire Hathaway (NYSE: BRKA) (NYSE: BRKB) has trimmed its stake in Chevron (NYSE: CVX) by roughly a third this year while keeping its investment in Occidental Petroleum (NYSE: OXY). As of its latest regulatory filing on Nov. 16, it showed both positions unchanged.
## WMT  (8 leads)
- Fri 27 Nov | www.tokenpost.com | Walmart Shares Test Resistance After Q3 Beat and Outlook Increase
  https://www.tokenpost.com/news/investing/63396
  > Walmart shares were testing nearby resistance early Nov. 27 after the retailer exceeded fiscal third-quarter earnings expectations, raised its fiscal 2027 outlook and received several higher analyst price targets. The shares traded at $131.74 at 3:56 a.m. ET (08:56 UTC), just below the upper Bollinger Band at $132.47 and above the $131.67 pivot.
- Fri 27 Nov | blockchain.news | Walmart (WMT) Stock Price Prediction: Bulls Test Resistance After Strong Q3 and Broker Upgrades
  https://blockchain.news/news/20261127-price-prediction-wmt-bulls-test-resistance-after-strong-q3
  > Q3 beat and guidance lift keep WMT in focus Walmart’s latest catalyst is fundamentally solid: the company reported better-than-expected third-quarter fiscal 2027 results and raised full-year guidance again.
- Fri 27 Nov | Trefis | Walmart Is Priced Almost Like 1999. Holders Then Waited 12 Years
  https://www.trefis.com/stock/wmt/articles/629160/walmart-is-priced-almost-like-1999-holders-then-waited-12-years/2026-11-27
  > Is Walmart Stock Priced Like 1999 Again? Today’s big story: Chip Stocks Jumped 15% In A Day. Walmart‘s stock rose 26% this fall. That added $215 billion to its value, the most among the fall’s 10 biggest percentage gainers. But investors now pay $50 for each $1 of Walmart’s yearly profit.
## V  (8 leads)
- Fri 27 Nov | NRI Affairs | Underpayment checks: 7 critical steps for visa holders
  https://www.nriaffairs.com/underpayment-checks-australia-workers/
  > Checked 27 November 2026. The amount reaching a bank account does not tell the whole pay story. A visa holder’s concern about immigration consequences adds another question, but it does not erase workplace entitlements.
- Fri 27 Nov | Blockchain News | Visa (V) Stock Price Prediction: Visa holds above short-term averages as analyst targets stay constructive
  https://blockchain.news/news/20261127-price-prediction-v-visa-holds-above-short-term-averages
  > Price action and what changed Visa (V) was last quoted at $425.90, up 0.38% on the day, with a 24-hour range of $427.05 to $421.95 and relatively light volume of $393,660 on Binance futures terms.
- Fri 27 Nov | Firstpost | Why is IBM ending US visa and green card sponsorship for most consulting jobs?
  https://www.firstpost.com/tech/ibm-ending-us-visa-and-green-card-sponsorship-for-most-consulting-jobs-why-14062975.html
  (page: did not load (403))
## ORCL  (8 leads)
- Fri 27 Nov | MarketBeat | Oracle Corporation $ORCL Shares Purchased by Entropy Technologies LP
  https://www.marketbeat.com/instant-alerts/filing-oracle-corporation-orcl-shares-purchased-by-entropy-technologies-lp-2026-11-27/
  > Oracle Corporation $ORCL Shares Purchased by Entropy Technologies LP - Entropy Technologies LP more than doubled its Oracle stake in the third quarter, adding 20,667 shares to reach 41,309 shares valued at about $5.67 million.
- Fri 27 Nov | AOL.com | Michael Burry Shares Stark Warning About AI Boom, as Nvidia, Oracle and Meta Face Surging Debt Insurance Costs
  https://www.aol.com/articles/michael-burry-shares-stark-warning-083128000.html
  > "The Big Short" investor Michael Burry has drawn attention to concerns that rising borrowing risks among major AI companies and data center developers could threaten the financing behind the industry’s massive infrastructure expansion. AI Credit Risks Rise as CDS Spreads Widen 17-19, five-year CDS spreads had climbed to 316 basis points for Oracle Corp.
- Fri 27 Nov | MarketBeat | Ardmore Road Asset Management LP Makes New Investment in Oracle Corporation $ORCL
  https://www.marketbeat.com/instant-alerts/filing-ardmore-road-asset-management-lp-makes-new-investment-in-oracle-corporation-orcl-2026-11-27/
  > Ardmore Road Asset Management LP Makes New Investment in Oracle Corporation $ORCL - Ardmore Road Asset Management opened a position of 331,002 Oracle shares, valued at about $45.4 million, making Oracle 2.1% of its portfolio.
- Fri 27 Nov | Blockchain News | Oracle (ORCL) Stock Price Prediction: Rebound attempt faces heavier overhead supply
  https://blockchain.news/news/20261127-price-prediction-orcl-rebound-attempt-faces-heavier-overhead-supply
  > Price action is improving, but the trend is still damaged Oracle (ORCL) is attempting a rebound from a weak stretch, with the current price at $108.74 and an intraday range of $105.34 to $109.81.
- Fri 27 Nov | Seeking Alpha | Oracle Corporation: Assessing The Preferred Which Now Yields Over ~9%
  https://seekingalpha.com/article/4972425-oracle-corporation-assessing-the-preferred-which-now-yields-over-9-percent
- Fri 27 Nov | Yahoo Finance | Wondering Why Oracle Fell? Here's What The Bears Saw
  https://finance.yahoo.com/markets/stocks/articles/wondering-why-oracle-fell-heres-012625677.html
- Thu 26 Nov | Billionaires.Africa | American billionaire Larry Ellison's own votes carry Oracle's $884 million pay plan
  https://www.billionaires.africa/2026/11/26/american-billionaire-larry-ellisons-own-votes-carry-oracles-884-million-pay-plan/
- Thu 26 Nov | Yahoo Finance | ‘Room to Spare,’ Says Investor About Oracle Stock
  https://finance.yahoo.com/markets/stocks/articles/room-spare-says-investor-oracle-215243159.html
## COST  (8 leads)
- Fri 27 Nov | TradingKey | Costco Absorbs Its $30 Special Dividend and Stays Near Records, With $1,090.46 Next
  https://www.tradingkey.com/analysis/stocks/us-stocks/262324874-costco-absorbs-30-special-dividend-near-records-1090-46-pivot-black-friday-november-27-2026-tradingkey
  > Costco Absorbs Its $30 Special Dividend and Stays Near Records, With $1,090.46 Next Costco recently absorbed its $30 special dividend with minimal price disruption, supported by strong net sales and a 7.3% rise in underlying October comparable sales.
- Fri 27 Nov | Blockchain News | Costco (COST) Stock Price Prediction: Pullback Holds Just Below Key Resistance as Sales Momentum Stays Intact
  https://blockchain.news/news/20261127-price-prediction-cost-pullback-holds-just-below-key-resistance
  > Sales momentum is still doing the heavy lifting Costco’s latest reported operating data support the broader bullish case. On November 4, 2026, the company reported October net sales of $24.50 billion, up 12.6% year over year, with first nine-week sales up 12.8% to $54.52 billion.
- Fri 27 Nov | JournalArta | Costco Stock Holds Near $1,087 as Defensive Demand Lifts Valuation
  https://journalarta.com/en/2026/11/27/costco-holds-near-1087-as-defensive-demand-offsets-three-day-dip/
  > Costco holds near $1,087 as defensive demand offsets three-day dip Costco Wholesale shares closed at $1,086.81 on Wednesday, holding a 10.59% monthly gain against a falling S&P 500 as defensive buyers and holiday demand support the stock.
## NFLX  (8 leads)
- Fri 27 Nov | Barchart.com | Is Netflix Stock Underperforming the Nasdaq?
  https://www.barchart.com/story/news/9028797/is-netflix-stock-underperforming-the-nasdaq
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | Simply Wall St | Does Studio Purchase Change The Bull Case For Netflix Stock (NFLX)?
  https://simplywall.st/stocks/us/media/nasdaq-nflx/netflix/news/does-studio-purchase-change-the-bull-case-for-netflix-stock
  > - Netflix recently acquired the Radford Studio Center in Los Angeles for about US$380 million and secured NFL Thanksgiving Eve football rights through 2029, expanding both its production footprint and live content slate.
- Fri 27 Nov | The Globe and Mail | Netflix Stock and Higher Content Spend: Can Margins Hold Firm in 2027?
  https://www.theglobeandmail.com/investing/markets/stocks/DIS-N/pressreleases/9021375/netflix-stock-and-higher-content-spend-can-margins-hold-firm-in-2027/
  > Netflix Stock and Higher Content Spend: Can Margins Hold Firm in 2027? NetflixNFLX is entering 2027 with heavier content and live-programming investments, raising the question of whether its operating margin can keep expanding.
## INTC  (8 leads)
- Fri 27 Nov | MarketBeat | Intel Corporation $INTC Shares Newly Bought by CSM Advisors LLC
  https://www.marketbeat.com/instant-alerts/filing-intel-corporation-intc-shares-newly-bought-by-csm-advisors-llc-2026-11-27/
  > Intel Corporation $INTC Shares Newly Bought by CSM Advisors LLC - CSM Advisors initiated a position in Intel during the third quarter, buying 97,334 shares valued at approximately $11.7 million. Institutional investors collectively own 64.53% of the company’s stock.
- Fri 27 Nov | 富途牛牛 | Intel Stock Option Guide: AI Chip Sector Sees Broad-Based Rally—Can the Rebound Continue?
  https://news.futunn.com/en/post/1005839418/intel-stock-option-guide-ai-chip-sector-sees-broad-based
  (page: only 0 words came back (a paywall or a page the reader cannot see): open it by hand if it matters)
- Fri 27 Nov | Trefis | How Much More Could You Lose In Intel Stock?
  https://www.trefis.com/stock/intc/articles/629327/how-much-more-could-you-lose-in-intel-stock/2026-11-27
  > How Much More Could You Lose In Intel Stock? Today’s big story: Anthropic Broke Its $83 IPO Price. Intel stock closed at $54.47 on Wednesday, 61.4% below its highest close of the past year, $140.94 on June 22. Its worst day was October 30, a 28.6% drop right after its quarterly report.
## LLY  (8 leads)
- Fri 27 Nov | www.tokenpost.com | Eli Lilly Trades Near $1,401 Pivot as Momentum Signals Stay Mixed
  https://www.tokenpost.com/news/investing/63391
  > Eli Lilly (LLY) shares traded near a key pivot at $1,401.19 in a Nov. 27 market snapshot, with neutral momentum readings and slightly bearish positioning offset by stronger buying in the latest one-hour flow data. The stock was at $1,401.15 at 3:50 a.m.
- Fri 27 Nov | Blockchain News | Eli Lilly (LLY) Stock Price Prediction: Lilly holds near pivot as bullish analyst targets meet mixed short-term positioning
  https://blockchain.news/news/20261127-price-prediction-lly-lilly-holds-near-pivot-as-bullish
  > What moved LLY shares Eli Lilly (LLY) is changing hands at $1,401.15, with a 24-hour range of $1,408.03 to $1,394.40. That leaves the stock sitting almost exactly on its 20-day simple moving average and at the reported pivot point of $1,401.19, which makes this a technically compressed setup rather than a clean trend breakout.
- Fri 27 Nov | Simply Wall St | Is Eli Lilly (LLY) Undervalued As New FDA Eye Risk Warnings Hit GLP 1 Drugs?
  https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/is-eli-lilly-lly-undervalued-as-new-fda-eye-risk-warnings-hi
  > Eli Lilly (LLY) just faced a meaningful regulatory shift. The US FDA will require new warning labels on its GLP-1 drugs, including Mounjaro and Zepbound, to highlight risks of the rare eye condition NAION.
Read 87 lead pages for you (logged in the research log); open a page only where the excerpt is not enough.
- No leads: ABUK, CLHO, JUFO, ALCN, MFPC, EAST, AMOC, SKPC.
