# After logging: what after_log.py's steps do, and what to do with what they flag

Read this only when `after_log.py DATE` prints something to act on. On a day it prints only ok lines, skip it.

**Bonus shares and splits** (`corporate_actions.py --check`): when an Egyptian stock in the log
has passed its ex-date (the first session without the right to the free shares), confirm the ratio in the
company's disclosure (Mubasher or Arab Finance, cross-checked against the reference price the script
estimates), then run `corporate_actions.py --apply TICKER EXDATE BONUS` once (BONUS is free shares per
share: 0.25 for one for every four) and refresh the spreadsheet. Without it, the charts show a fall that
never happened to holders and the changes and YTD figures come out too low. Cash dividends are not adjusted.

**Gaps** (`fill_gaps.py DATE 10 --write`): it finds figures missing from the last ten entries although the entries around them have them, and fills each
from a dated source (Yahoo, Nasdaq or CoinGecko history; the desk's intraday file for Egyptian stocks; the last
weekday's pound rates for Friday and Saturday closes), printing every value beside its neighbours. Check any line
it marks as more than 8% from a neighbour, and fill the `MANUAL` lines it lists by hand with log_figures.py when a
source confirms the figure (or leave them, and say so in the final reply).

**The week behind the trend lines** (`fetch_intraday.py`, bringing the desk's intraday prices up to the last
session, then `week_snapshot.py DATE`): it saves `data/weeks/DATE.json`, the last five sessions hour by hour for the desk's stocks and the indexes, which the
site draws as this edition's "Last 7 days" lines; commit it, and `desk/intraday.json`, with the edition.

The spreadsheet copy, `data/markets.xlsx`, is rewritten by GitHub Actions after the push (the "Audio and chores"
workflow, `export_xlsx.py`): do not run it in the run.

