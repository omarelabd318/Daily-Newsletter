# Fair value

`/desk/fairvalue/` (in Egypt's menu; `?m=us` in the United States menu) ranks stocks by how far they trade below or above the desk's own fair value, with four
grades each. `desk/fairvalue.json` holds it; `fetch_fairvalue.py` rebuilds the figures every morning and keeps the
`judgement` block, which only the run writes. The script's docstring is the exact method; the reasoning:

- **It is a ranking inside the EGX, not a verdict on the market.** At Egyptian rates an absolute model (discounting at
  the T-bill yield plus a premium) calls nearly every stock dear, because the market prices rates to fall. So the
  discount rate is solved for, not assumed: the rate at which the median stock is fairly priced on its assets. The
  page states the market-level reading separately (the median earnings yield against the after-tax T-bill yield).
- **Three estimates, because each fails differently.** Earnings (EPS times a peer P/E, tilted up to 25% for return on
  equity and profit growth) fails on one-off profits; assets (book value times the P/B its ROE justifies) fails on
  asset-light companies, so it is skipped above 6 times book; analysts fail when targets are stale, so an undated
  consensus far from everything else is dropped. Fair value is their weighted average (40, 30, 30) and needs two.
- **Banks are measured against banks** (their own discount rate and P/E): they always look cheap against industry.
- **Confidence is the spread between the estimates**, not a feeling. The two lists show medium and high only.

**Wall Street** (the tab's second market, `us` in the file): US common stocks worth $50bn or more, the same method
with three changes: long-run growth 6%, weights of earnings 30, assets 20 and analysts 50 (reported US earnings carry
more one-offs, and targets come from many analysts), and no earnings estimate when the P/E is outside 4 to 60. Its
judgement block is `judgementUS`, same fields. Notes are only needed for the desk's 18 US stocks.

What the run adds, in `judgement[TICKER]` (the script never touches it):
- `brokers`: a fair value or target found in the day's stock research and checked at the outlet:
  `{"firm", "value", "kind": "fair" or "target", "date", "url"}`. A target is brought back one year; entries count
  for 180 days. Add every one the research finds: this is the estimate that most needs the desk's own work.
- `eps_norm` with `eps_reason`: replace 12-month EPS when it misleads (a one-off gain or loss, a currency windfall, a
  commodity peak, new shares on the way). Use a figure from the filing or a broker, never a guess, and say which.
- `exclude`: a reason a stock cannot be rated on these terms at all (profit that is mostly revaluation, a merger that
  will change every per-share figure). It is then listed under Not rated with that reason.
- `note` and `noted`: the desk's line on the stock: the catch behind a cheap price or what a dear one is paying for.
  One or two sentences in figures. Write or refresh it for the ten cheapest and ten dearest and for every desk stock;
  review it when the company reports, when its confidence changes, or when it is more than a month old.

Each week (Sunday) read the whole table for figures that cannot be right (a P/E under 3, upside above 80%): the
cause is usually a bonus issue the source has not caught up with, parent-only earnings, or a stale target; fix it with
`eps_norm` or `exclude` and say why. When results come out for a desk stock, rerun the script after set_results.py.
The open view `2026-11-11-value-basket` scores the model (cheapest five desk stocks against the dearest five, to
February 11, 2027); when it is judged, open the next one from the table as it then stands, and if the model loses
twice running, rework the weights before opening a third. Never present a fair value as a forecast or advice: write
"the desk's fair value", and keep the page's line that a model and a judgement can both be wrong.
