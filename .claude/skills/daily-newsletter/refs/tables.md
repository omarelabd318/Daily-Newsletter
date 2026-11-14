# Stocks Watch tables

`## Stocks Watch` comes right after Markets and before Currency and Commodities Watch. It has two parts,
`### Egypt` first, then `### USA`. Each part is one table and nothing else: no paragraphs and no bullet
points. Under each heading, put one italic line saying which close the table shows, for example
`*EGX close, Tuesday 27 October*` or `*US close, Tuesday 27 October*`. If the run happens while the EGX is
trading, say so and give the time, for example `*EGX intraday, 11:49 Cairo*`.

The site adds a 1D / 1W / 1M / 6M / 1Y switch above each table: 1D shows the Change you write, the
other periods are worked out from the data log, and the trend line redraws over the same period.

Columns: `| Stock (ticker) | Close | Change | YTD |`, with the price in EGP or USD and the change as a
percentage with a sign, for example `+1.2%`. The site colours signed changes green or red with an arrow,
and bolds moves of 5% or more, so always write the sign. Take Change from the source. Take YTD (change
since the last close of the previous year) from the data log: log the day's figures first (see "Log the
day's figures"), then run `python3 .claude/skills/daily-newsletter/market_facts.py DATE --ytd`. Write
`n/a` for YTD when it prints n/a, and for notable movers that are not in the log.

List these every day, in this order:

| Egypt (EGX) | USA |
|---|---|
| Commercial International Bank (COMI) | Apple (AAPL) |
| Talaat Moustafa Group (TMGH) | Microsoft (MSFT) |
| Telecom Egypt (ETEL) | Nvidia (NVDA) |
| Palm Hills Developments (PHDC) | Amazon (AMZN) |
| Elsewedy Electric (SWDY) | Alphabet (GOOGL) |
| Orascom Construction (ORAS) | Meta (META) |
| Fawry (FWRY) | Tesla (TSLA) |
| Abu Qir Fertilizers (ABUK) | JPMorgan Chase (JPM) |
| EFG Holding (HRHO) | Exxon Mobil (XOM) |
| Cleopatra Hospital (CLHO) | Broadcom (AVGO) |
| Juhayna Food Industries (JUFO) | Berkshire Hathaway (BRK.B) |
| Alexandria Containers (ALCN) | Walmart (WMT) |

After the fixed rows, add up to three rows for other stocks with a notable move or notable news that
day, marked in italics, for example `| *Misr Cement Qena (MCQE), notable mover* | 167.85 | +8.5% | n/a |`.
Leave them out when nothing stands out. Every mover row shows its close, like the fixed rows: get it by
adding the tickers to the fetch command, for example
`python3 .claude/skills/daily-newsletter/fetch_figures.py DATE egx.MCQE us.ORCL`, which also gives YTD for
US stocks (write `n/a` for YTD when it has none). Movers are not logged.

On weekends the EGX is closed Friday and Saturday and US markets Saturday and Sunday. Show the last
session's close with its date. On EGX holidays, listed in `data/holidays.json`, do the same and say why in
the italic line, for example `*EGX closed today for Sham el-Nessim; last close Sunday 2 May*`, and log
the figures as usual (the last close again). The checker warns when a listed closure is not mentioned. If a price cannot be confirmed, write `n/a` rather than guessing.

The checker compares every Stocks Watch row with the data log: the close with what was logged for the
date, and the change with the move from the previous logged close (from the previous close to the live
price for an intraday table). A warning there means one of the two figures is wrong: recheck both at the
source and fix the table or re-run log_figures.py before publishing.

It also compares each logged close with the stock's last trade in the desk's intraday prices for that session. A
gap over 0.5% on the EGX or 1% in the US is an error that blocks publishing, unless the stock's own quote at its
source (Mubasher, Nasdaq) gives the logged figure as its close, which the checker looks up itself (an EGX close can
sit off the last trade, since the exchange sets it from the session's final trades). If it still errors, open the
quote: fix the log if it is wrong, or, where the close is right but the source would not answer the checker, record
it with `python3 .claude/skills/daily-newsletter/research_log.py DATE newsletter close TICKER PRICE "Mubasher"`.

## Currency and Commodities Watch table

Use four columns: `| Item | Level | Note | YTD |`.

- **Italic line first:** under the heading, one italic line saying which rates the table shows, for example
  `*USD/EGP is the central bank's rate; other currencies are market mid-rates.*` Then do not repeat
  "Market mid-rate" in the Notes.
- **Notes:** about 6 words, so rows stay on one line. Use them for one short point ("highest since
  March", "fourth rise running", "central bank rate"), or leave a Note empty when there is nothing to add.
  Do not repeat the day's change: the site adds a Change column to this table by itself, worked out from
  the data log, with a 1D / 1W / 1M / 6M / 1Y switch. That is one more reason to log every figure daily.
- **YTD:** the change since the last close of the previous year, from
  `python3 .claude/skills/daily-newsletter/market_facts.py DATE --ytd` after logging, with a sign
  (`+17.8%`). Write `n/a` when the figure is not in the log that day, and `—` for central bank rates,
  certificates and T-bills, which have no YTD.

Right after the USD/EGP row, add `| US dollar index (DXY) | 102.19 | ... | +4.0% |`: the dollar against six major
currencies, with the day's change in the Note, so readers can tell whether a move in the pound is the
dollar strengthening everywhere or something specific to Egypt. Say which in the Note when it is clear,
for example `+0.4%; dollar firmer worldwide` or `-0.3%; pound's fall is local`.

The site draws a trend line beside every row whose figure is in the data log: USD, EUR, SAR, AED, KWD,
QAR and GBP against the pound, the dollar index, 21K, 24K and 18K gold, the gold pound, global gold and
Brent. Log all of these every day so the lines stay up to date. Rates, certificates and T-bills change
too rarely for a line and get none.

Mark a figure the sources disagree on with `(unconfirmed)` right after it, in any table. The site shows
it as a small * that says "Unconfirmed" on hover, so it takes no extra space.
