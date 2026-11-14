# The desk's side sessions (sub-agents), and batching

The same reasons and rules as the newsletter's (`.claude/skills/daily-newsletter/refs/research-agents.md`, "News
research: search.py first" and "Batching"): news research through
`python3 .claude/skills/daily-newsletter/search.py --log DATE desk "q1" "q2" ...` first, several queries per call
(it logs itself), with web search and full page reads kept for data pages, filings and what its excerpts do not
settle; several page reads, log lines and file reads per step, and no file read twice; each section, and each
file, written in one Write or Edit; each checker run once per pass, its findings fixed in one pass.

**The main run does not read the brief's per-stock news leads** (about 6,000 of its 7,000 words): read
`desk/brief.md` up to that part with `sed '/^## News leads by stock/,$d' desk/brief.md`. The stocks session reads
the leads and returns what matters as notes; open a stock's leads yourself (`sed -n '/^## TICKER /,/^## /p'
desk/brief.md`) only for a point its note leaves open.

After wait_desk_data.py reports READY (or run_data.py has run) and you have read today's edition and desk/brief.md,
start these two side sessions **in one step** (two Task calls in one response, so they run at once). The main run
meanwhile copies the template to desk/days/DATE.json and starts on the close cards and the figures it already has.

1. **Stocks** (start it with `model: "sonnet"`: it gathers and checks, and writes no published text; the main run
   writes every published word, the `news` items and `lastResults` included, and makes every call on a stock):
   - "Results to record" in the brief: for each stock listed, read the filing (or two outlets that agree) and
     return its figures (profit attributable to shareholders, the period, the year-earlier figure, shares, equity,
     one-offs) with the source; run set_results.py for Egyptian stocks and fetch_valuation.py TICKER with those
     figures (numbers only), and correct desk/calendar.json's dates.
   - Stock research for every stock with leads in the brief, as "Stock research, every day" describes: judge each
     lead from its excerpt (the per-stock leads in desk/brief.md are read here, not in the main run), open the
     page where the excerpt is not enough, check what moves a stock at a second outlet (search.py first), and log one stock line each with `research_log.py DATE desk stock TICKER "..."`. Every desk stock that
     moved 3% or more gets a line. Return each news item as a note (date, what happened, outlet and URL, second
     source), not written into desk/stocks.json.
   The main run then writes the `news` items and `lastResults` into desk/stocks.json from the notes, all in one
   edit or one short script, not stock by stock.
2. **Markets and macro** (on the run's own model: leave `model` out): the day's Egyptian macro and policy stories (the pound, rates, inflation, reserves,
   gas, Suez), the US session and data, central banks, and a second source for every figure the desk's stories
   will use that the edition does not already carry (FactIQ where it holds it, as the skill's FactIQ paragraph
   describes). It starts from the newsletter's saved side-session notes, `editions/notes/DATE-*.md` (on a
   Saturday `DATE-recap-*.md`, and Friday's for the Egypt section): their facts are already checked at two
   outlets, with sources, so it does not search for or check them again. It researches only what the notes do not
   hold or what has moved since they were written (the desk's own angle, flows, movers' reasons, news since the
   edition). Where no notes exist for the day, it researches in full as before. Returns notes only; it writes no
   repo file except through research_log.py.

## The prompt for each side session

> You are researching part of today's Markets Desk (DATE, Cairo) in the repo at REPO. Read
> .claude/skills/markets-desk/SKILL.md's sections BLOCK-SECTIONS and the newsletter skill's rules on checking
> figures and sources before starting. Your block: BLOCK. Start from desk/brief.md (the macro block reads it
> without the per-stock news leads: `sed '/^## News leads by stock/,$d' desk/brief.md`) and the parts of the
> edition the desk uses (`python3 .claude/skills/markets-desk/edition_for_desk.py DATE`; open editions/DATE.md, or
> DATE-recap.md on a Saturday, only for a story needed in full), and for the macro block from the saved notes in editions/notes/ (do not re-check
> what they already checked). Confirm every figure at a second, independent outlet (two pages with the same
> wording are one source). Research news with `python3 .claude/skills/daily-newsletter/search.py --log DATE desk
> "q1" "q2" ...` first, several queries per call (it reads the top pages, prints short excerpts and logs itself);
> use web search and full page reads only for data pages, filings and what the excerpts do not settle, several
> pages per `articles.py --log DATE desk URL ...` call. Log those searches and pages, and every stock line, with
> `python3 .claude/skills/daily-newsletter/research_log.py DATE desk search|page|stock ...` (several per call).
> Stop on a story once each figure has its outlet and one independent confirmation: about two pages opened per
> story beyond search.py's excerpts, more only where sources conflict.
> FILES-YOU-MAY-WRITE. Return notes only, about 60 to 80 words per item (a stock with no news: one line), no prose:
> `### TICKER or topic: headline` then terse bullets, each fact with every figure, its basis (consolidated or
> standalone, quarter or nine months, year on year) and date; `Src:` outlet and URL; `Chk:` second outlet and URL,
> or "single source"; `Angle:` a few words on what it means for the stock, sector or market; `Open:` only if
> something is unclear. Keep every figure, basis and source; cut background. End with one line per item done to the
> files (results recorded, news added) and anything left undone and why.

For the stocks session FILES-YOU-MAY-WRITE is "You may run set_results.py and fetch_valuation.py (numbers only) and
correct dates in desk/calendar.json; write nothing else: return news items and results as notes". For the macro session it
is "Do not write any repo file except through research_log.py".

Wait for both before writing (never leave one running in the background). Write the desk from the notes and the brief, each section and file in one Write or Edit. Open a page yourself only for an "Open:" point that matters to a story.
On a Saturday the stocks session covers the US stocks and any Egyptian stock with news, and there may be no results
to record.
