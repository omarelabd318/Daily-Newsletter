# Research in side sessions (sub-agents), and batching

Why: a run pays again at every step for everything it has open. A page read by the main run stays in it, and is
paid for, at every step to the end. A side session (the Task tool's sub-agent) starts nearly empty, reads the
pages, checks the figures and hands back short notes; its pages never enter the main run. The research is the
same research: the same searches, outlets and two-source checks. Only where it is held changes. The main run still
chooses the stories, writes every word, and opens any page itself when a note is not enough.

## News research: search.py first

Most of a run's cost is raw text sitting open and re-sent at every step: a web search's result list and summary
(about 600 words) and each full page it leads to (700 to 3,000 words). For news, search with
`python3 .claude/skills/daily-newsletter/search.py --log DATE newsletter|desk "query 1" "query 2" ...` first (the
main run adds `--short`: one line and a figures fragment a page, the full excerpts appended to editions/search.md),
several queries per call (English and Arabic queries can share a call; `--days N` for older stories). For each query
it searches Google News, reads the top four pages at their outlets at once and prints outlet, date, link and an
excerpt of about 80 words with the figures and their basis, marks pages with the same wording as one source and lists
the pages that would not load: about 400 words a query, for four outlets' text. It logs each query as a search and
each page as read, in one call, so the floors count them; do not log them again.

Use the built-in web search and full page reads for what it cannot reach: data and official pages (central banks,
statistics offices, exchanges, results filings), a page it lists as not read that matters, a page whose excerpt is
not enough, a figure that needs its full context or a second outlet the excerpts do not give, and anything older
than the news feed holds. Log those as before (`search`, `page`). The pages floor counts pages opened by hand: the
confirmations and full reads still go there.

## Batching: several actions in one step

Every step re-sends everything open, so put independent actions in one step:

- Searches: four to eight queries in one search.py call; any web searches four to six to a response, not one per step.
- Logging: one research_log.py call per batch, several queries or URLs at once
  (`research_log.py DATE newsletter search "q1" "q2" "q3"`, `... page URL1 URL2`).
- Pages: read several at once with `articles.py --log DATE newsletter URL URL ...` rather than one fetch each.
- Files: read the files you need in one step, and never read again a file you already have open (keep working from
  what you read; after your own Write or Edit the file is as you wrote it). Write each section with one Write or
  Edit, not a string of small edits. Run each checker once per pass: fix all its findings in one pass, then run it
  once more to confirm.
- Commands: chain quick commands that do not depend on each other's output into one call.

## The newsletter's side sessions

After reading editions/brief.md, editions/articles.md and the figures (fetch_figures.py), choose the day's stories,
then start these side sessions **all in one step** (several Task calls in one response, so they run at once). Each
gets the prompt below with its own block and NAME filled in (NAME in brackets after each block). They log their own searches and pages with research_log.py
(the log is locked, so they can log at the same time), so do not log their work again.

1. **Egypt** (`egypt`): run `read_enterprise.py` and fetch https://cairoscene.com; the Egypt News stories chosen and other
   Egyptian candidates; Egypt Markets (EGX movers, central bank, corporate news). Also return EnterpriseAM items
   useful to any other section, marked by section.
2. **Region and world** (`world`): Regional and Gulf, and Top World Headlines.
3. **Global markets and calendar** (`markets`): Global Markets (what moved and why, bonds, crypto), the day's data releases
   and central banks, the Economic Calendar (holidays, closures, results and IPO dates, data, fixtures). Use FactIQ
   where it holds the figure, as the skill's FactIQ paragraph describes.
4. **In Other News** (`other`): Tech and AI, Sports (Egyptian football first; results and fixtures with dates and Cairo
   times), Health and Science, Entertainment and Culture.
5. **Checks** (`checks`; start this one with `model: "sonnet"`: it compares figures between sources and writes no prose that
   is published): every figure in the Stocks Watch and Currency and Commodities Watch tables that fetch_figures.py
   could not confirm or flagged, plus the corrections check (yesterday's key figures against what is now known).
   Start sessions 2 and 4 with `model: "sonnet"` too: their stories rarely lead the edition, and the main run
   writes every word from their notes. Sessions 1 and 3 (Egypt, and global markets and the calendar) run on the
   run's own model (leave `model` out): their notes shape the lead stories and the Markets section.

### Saved notes, for the desk

Each side session also writes the notes it returns, word for word, to `editions/notes/DATE-NAME.md` (the
Weekly Recap's: `editions/notes/DATE-recap-NAME.md`). The edition's commit takes them with editions/. The Markets
Desk starts from them rather than researching the same stories again, so they carry every source and check.

Quick Hits, Weather (weather.py), Worth Knowing and the puzzles stay in the main run.

### The prompt for each side session

> You are researching part of today's Daily Newsletter (DATE, Cairo) in the repo at REPO. Read
> .claude/skills/daily-newsletter/SKILL.md's sections on checking figures, sources and US English before
> starting. Your block: BLOCK. Candidate stories and leads: LEADS (with links from editions/brief.md and
> editions/articles.md; read editions/articles.md for what is already read). Research each story at its outlet and
> confirm every figure at a second, independent outlet (two pages with the same wording are one source).
> Research news with `python3 .claude/skills/daily-newsletter/search.py --log DATE newsletter "q1" "q2" ...` first,
> several queries per call (Arabic queries too): it reads the top pages and prints short excerpts, and logs itself.
> Use web search and full page reads only for what it cannot reach (data and official pages, a page it could not
> read, an excerpt that is not enough, a figure that needs its context), and log those with
> `python3 .claude/skills/daily-newsletter/research_log.py DATE newsletter search|page ...` (several per call).
> Stop researching a story once each figure has its outlet and one independent confirmation: about two pages
> opened per story beyond search.py's excerpts, more only where sources conflict. Do not write or edit any file in the repo except through research_log.py, and one notes
> file: when done, write the notes you return, exactly, to editions/notes/DATE-NAME.md.
> Return notes only, about 60 to 80 words a story (more only for a story with many figures), in this format:
> `### Headline in plain words` then terse bullets, no prose and no full sentences where a fragment does: each fact
> with every figure, its basis (consolidated or standalone, quarter or nine months, nominal or real, year on year
> or month on month) and its date; `Src:` outlet and URL; `Chk:` the second outlet and URL, or "single source" or
> "same wording as X"; quotes word for word in quotation marks with the speaker; `Why:` a few words; `Open:` only
> if something is unclear or conflicting. Keep every figure, basis and source; cut background the main run does not
> need to write the story. Then one line listing stories you dropped and why (old, unconfirmed, not news).

Wait for all five before writing (never leave one running in the background past the final reply). Write the
sections from the notes, each section in one Write or Edit. Open a page yourself only where a note says
"Open:" something that matters, or a figure is single-source and the story needs it (search.py or articles.py,
logged). The checker counts the side sessions' searches and pages, which they log themselves. Do not read the saved
notes files again: they are the notes already returned to you.
