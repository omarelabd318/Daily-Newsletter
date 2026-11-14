# The desk's side sessions (sub-agents), and batching

The same reasons and batching rules as the newsletter's (`.claude/skills/daily-newsletter/refs/research-agents.md`,
"Batching"): several searches, page reads, log lines and file reads per step; whole sections written in one Write
or Edit; the checker's findings fixed in one pass.

After wait_desk_data.py reports READY (or run_data.py has run) and you have read today's edition and desk/brief.md,
start these two side sessions **in one step** (two Task calls in one response, so they run at once). The main run
meanwhile copies the template to desk/days/DATE.json and starts on the close cards and the figures it already has.

1. **Stocks** (it owns desk/stocks.json until it returns: do not edit that file meanwhile):
   - "Results to record" in the brief: for each stock listed, read the filing (or two outlets that agree), write
     `lastResults` as the skill's "Results days" section describes, run set_results.py for Egyptian stocks and
     fetch_valuation.py TICKER, and correct desk/calendar.json.
   - Stock research for every stock with leads in the brief, as "Stock research, every day" describes: judge each
     lead from its excerpt, open the page where the excerpt is not enough, check what moves a stock at a second
     outlet, add the items to the stock's `news` in desk/stocks.json, and log one stock line each with
     `research_log.py DATE desk stock TICKER "..."`. Every desk stock that moved 3% or more gets a line.
2. **Markets and macro:** the day's Egyptian macro and policy stories (the pound, rates, inflation, reserves,
   gas, Suez), the US session and data, central banks, and a second source for every figure the desk's stories
   will use that the edition does not already carry (FactIQ where it holds it, as the skill's FactIQ paragraph
   describes). Returns notes only; it writes no repo file except through research_log.py.

## The prompt for each side session

> You are researching part of today's Markets Desk (DATE, Cairo) in the repo at REPO. Read
> .claude/skills/markets-desk/SKILL.md's sections BLOCK-SECTIONS and the newsletter skill's rules on checking
> figures and sources before starting. Your block: BLOCK. Start from desk/brief.md and editions/DATE.md (or
> DATE-recap.md on a Saturday). Confirm every figure at a second, independent outlet (two pages with the same
> wording are one source). Batch your work: several searches per step, several pages per
> `articles.py --log DATE desk URL ...` call. Log every search, page and stock line with
> `python3 .claude/skills/daily-newsletter/research_log.py DATE desk search|page|stock ...` (several per call).
> FILES-YOU-MAY-WRITE. Return notes only, about 100 words per item at most: `### TICKER or topic: headline` then
> bullets, each fact with its figure, its basis (consolidated or standalone, quarter or nine months, year on
> year) and date; `Source:` outlet and URL; `Checked:` second outlet and URL, or "single source"; `Desk angle:`
> one line on what it means for the stock, sector or market; `Open:` anything unclear. End with one line per
> item done to the files (results recorded, news added) and anything left undone and why.

For the stocks session FILES-YOU-MAY-WRITE is "You may write desk/stocks.json (news, lastResults), desk/calendar.json
and, through set_results.py and fetch_valuation.py, the valuation entries; nothing else". For the macro session it
is "Do not write any repo file except through research_log.py".

Write the desk from the notes and the brief. Open a page yourself only for an "Open:" point that matters to a story.
On a Saturday the stocks session covers the US stocks and any Egyptian stock with news, and there may be no results
to record.
