# Research in side sessions (sub-agents), and batching

Why: a run pays again at every step for everything it has open. A page read by the main run stays in it, and is
paid for, at every step to the end. A side session (the Task tool's sub-agent) starts nearly empty, reads the
pages, checks the figures and hands back short notes; its pages never enter the main run. The research is the
same research: the same searches, outlets and two-source checks. Only where it is held changes. The main run still
chooses the stories, writes every word, and opens any page itself when a note is not enough.

## Batching: several actions in one step

Every step re-sends everything open, so put independent actions in one step:

- Searches: send four to six web searches in one response, not one per step.
- Logging: one research_log.py call per batch, several queries or URLs at once
  (`research_log.py DATE newsletter search "q1" "q2" "q3"`, `... page URL1 URL2`).
- Pages: read several at once with `articles.py --log DATE newsletter URL URL ...` rather than one fetch each.
- Files: read the files you need in one step; write a whole section with one Write or Edit, not a string of
  small edits; fix all of a checker run's findings in one pass, then run it once more.
- Commands: chain quick commands that do not depend on each other's output into one call.

## The newsletter's side sessions

After reading editions/brief.md, editions/articles.md and the figures (fetch_figures.py), choose the day's stories,
then start these side sessions **all in one step** (several Task calls in one response, so they run at once). Each
gets the prompt below with its own block filled in. They log their own searches and pages with research_log.py
(the log is locked, so they can log at the same time), so do not log their work again.

1. **Egypt:** run `read_enterprise.py` and fetch https://cairoscene.com; the Egypt News stories chosen and other
   Egyptian candidates; Egypt Markets (EGX movers, central bank, corporate news). Also return EnterpriseAM items
   useful to any other section, marked by section.
2. **Region and world:** Regional and Gulf, and Top World Headlines.
3. **Global markets and calendar:** Global Markets (what moved and why, bonds, crypto), the day's data releases
   and central banks, the Economic Calendar (holidays, closures, results and IPO dates, data, fixtures). Use FactIQ
   where it holds the figure, as the skill's FactIQ paragraph describes.
4. **In Other News:** Tech and AI, Sports (Egyptian football first; results and fixtures with dates and Cairo
   times), Health and Science, Entertainment and Culture.
5. **Checks:** every figure in the Stocks Watch and Currency and Commodities Watch tables that fetch_figures.py
   could not confirm or flagged, plus the corrections check (yesterday's key figures against what is now known).

Quick Hits, Weather (weather.py), Worth Knowing and the puzzles stay in the main run.

### The prompt for each side session

> You are researching part of today's Daily Newsletter (DATE, Cairo) in the repo at REPO. Read
> .claude/skills/daily-newsletter/SKILL.md's sections on checking figures, sources and US English before
> starting. Your block: BLOCK. Candidate stories and leads: LEADS (with links from editions/brief.md and
> editions/articles.md; read editions/articles.md for what is already read). Research each story at its outlet and
> confirm every figure at a second, independent outlet (two pages with the same wording are one source).
> Batch your work: several searches per step, several pages per articles.py call. Log every search and every page
> you open with `python3 .claude/skills/daily-newsletter/research_log.py DATE newsletter search|page ...`
> (several per call). Do not write or edit any file in the repo except through research_log.py.
> Return notes only, in this format, about 120 words a story at most:
> `### Headline in plain words` then bullets: each fact with its figure, the basis of the figure (consolidated
> or standalone, quarter or nine months, nominal or real, year on year or month on month) and its date;
> `Source:` outlet and URL for each fact; `Checked:` the second outlet and URL, or "single source" or "same
> wording as X"; quotes word for word in quotation marks with the speaker; `Why it matters:` one line;
> `Open:` anything unclear or conflicting. Then a last line listing stories you dropped and why (old, unconfirmed,
> not news). No prose beyond this.

Write the sections from the notes. Open a page yourself only where a note says "Open:" something that matters,
or a figure is single-source and the story needs it (articles.py, logged). The checker counts the side sessions'
searches and pages, which they log themselves.
