# Weekly Recap (Saturdays)

From November 14, 2026 the recap is Saturday's only edition: there is no regular Saturday edition (the EGX and
Wall Street are closed and EnterpriseAM does not publish). It sums up the week from Sunday to Saturday and opens with
the news since Friday's edition. So the recap run also does the daily jobs a Saturday still needs, listed under
"Saturday's daily jobs" below. The daily rules on voice, sources, figure checks, linking visuals,
placement and standing alone all apply; the daily section list, word budgets, Today at a Glance links and
Stocks Watch do not.

- **File:** `editions/DATE-recap.md`, where DATE is the Saturday. In `editions/index.json` add
  `{"date": "DATE", "id": "DATE-recap", "label": "Weekly Recap", "summary": "..."}` and keep every other
  entry. There is no regular edition for a Saturday from November 14, 2026.
- **Research:** start from that week's editions, read in one short digest:
  `python3 .claude/skills/daily-newsletter/week_digest.py DATE` (Sunday to Friday, second editions included: each
  edition's Today at a Glance and every story's lead-in and first sentence, where each running topic stands now,
  and the side-session notes saved this week). Open an edition in full only for a story you need in full or its
  links; the side sessions read the editions and the saved notes (`editions/notes/`) in full for their own blocks.
  Then search for how each big story developed and ended up (search.py first, several queries per call, as
  `refs/research-agents.md` describes; web search and full pages for what its excerpts do not settle). Report where things stand
  now, not what was said on each day. Check every figure as usual.
- **Length:** about 2,050 to 2,400 words, a 9 to 10 minute read. A guide, not a limit.
- **First line:** an italic sentence with the week's dates and what it was about, for example
  `*Week of 25 to 31 October 2026: a rate hold, a weaker pound and Egypt's Saudi deployment vote.*`
- **Sections,** in this order, each as `##` with exactly these titles:
  0. **Since Friday:** what is new since Friday's edition went out: two to four items, only stories that matter
     (a decision, an attack, a big result), each `**Label:** two or three sentences` with its source, the same as a
     daily story. Never pad: on a quiet day write one item saying the main stories of the week stand as below. A
     story that changed since Friday is told here as it now stands and not repeated in full further down. Then two
     lines: `**Weather:** Cairo today and tomorrow in one sentence` and `**What to watch today:** ...` as in a daily
     edition. About 150 to 300 words in all, on top of the recap's length.
  1. **The Week in Brief:** a numbered list of 7 to 10 of the week's biggest stories, Egypt first, each
     `**Label:** one sentence`. No links.
  2. **What Tied the Week Together:** the week's essay, 200 to 260 words in two or three paragraphs with no bold
     lead-ins: the thread that connects the week's biggest stories, told as cause and effect (a rate decision, the
     pound, who bought the bills, what that did to the EGX; a war headline, oil, the import bill). Say what changed
     for a reader in Egypt between last Saturday and this one, and what is still unresolved going into next week.
     It is analysis, not opinion or forecast: every link in the chain rests on a fact and figure already in the
     recap, and where the connection is the outlets' or analysts' reading, say whose. If the week had no single
     thread, say so and take the two that mattered. Write it last, after the other sections.
  3. **Egypt This Week:** 4 to 6 items on the main Egyptian stories, each with where it stands now.
  4. **Region and World:** 4 to 6 items, regional first, then the rest of the world.
  5. **Markets This Week:** a short paragraph on the week, then a table
     `| Item | Week close | Weekly change |` covering EGX30, USD/EGP, gold 21K per gram in Egypt, Brent,
     S&P 500, Nasdaq, Dow Jones and Bitcoin, then one line each on the week's best and worst EGX30 stocks if known.
  6. **Sports This Week:** the week's main results and stories as separate items, Egyptian football first,
     with no sport headings.
  7. **Culture and Tech:** 3 to 5 short items from tech, AI, entertainment and culture.
  On the first Saturday of a month, add **Month in Numbers** right after Markets This Week: one line on
     the month, then a table `| Item | Start of month | End of month | Change |` for EGX30, USD/EGP, gold
     21K, Brent, S&P 500, Dow Jones and Bitcoin, taken from the first and last entries of the previous month in
     `data/markets.json` (say "not logged" where a figure is missing).
  In the last Saturday recap of December, also add **Year in Numbers** right after Markets This Week (and
     after Month in Numbers if both appear): one line on the year, then the table that
     `python3 .claude/skills/daily-newsletter/market_facts.py DATE --year` prints, then one line each on
     the year's best and worst stocks from that table.
  8. **How It Played Out:** go through the What to watch today lines in this week's daily editions and
     pick the 4 to 6 events that mattered most (a rate decision, a vote, a data release, a big match).
     For each, one item: what was expected and what actually happened, for example
     `**Central bank meeting:** Expected to hold; it held rates at 22% and signalled cuts in December.`
     Skip anything already covered in full above; say "postponed" or "no decision yet" where that is the
     case. Do not mention the daily editions themselves.
  9. **The Week Ahead:** the key scheduled events for the coming week (central bank meetings, data,
     holidays and closures, big matches).
  10. **Sources:** the links used.
- **Saturday's daily jobs** (the run does these as a daily run would, following the main skill):
  - **Figures:** `fetch_figures.py DATE`, check them, and log them with `log_figures.py DATE ...` as the main skill's
    "Fetch the figures first" and "Log the day's figures" describe. The EGX is closed, so its figures are Thursday's
    and are not logged again; Wall Street's are Friday's closes; gold, Brent, Bitcoin and the pound are the latest.
    The desk's Saturday run relies on this entry.
  - **Puzzles:** the Saturday crossword (11 by 11) and the week's hardest killer sudoku, made, clued and checked as
    the main skill's "Puzzles" section describes; commit `data/puzzles/DATE.json`. The recap page shows them.
  - **Research log:** log every search and page under `newsletter` (the recap is Saturday's newsletter).
- On the recap page, the site draws year-long trend lines next to the Markets This Week rows by itself;
  nothing to add for that.
- **Data log check:** before committing, run
  `python3 .claude/skills/daily-newsletter/check_log.py DATE`. Fix any real problem it finds in
  `data/markets.json` with log_figures.py (checking the figure at the source first), commit the fix, and
  list anything left unfixed in the final reply's Publishing note. It does not go in the recap itself.
- Every item opens with a bold lead-in, as in the daily edition. Never refer to the daily editions
  themselves ("as reported on Tuesday"): write about the events and their dates.

## Side sessions on Saturday

The recap uses the same side sessions and batching as a daily edition (`refs/research-agents.md`), with these
blocks: (1) Since Friday (what is new since Friday's edition, every section); (2) the week in Egypt (news and
markets, from the week's editions and data/topics.json, and where each story stands now); (3) the week in the region
and the world; (4) the week's markets, the coming week's calendar and In Other News. Saturday's figures, puzzles and
check_log.py stay in the main run. Their NAMEs for the saved notes: since-friday, egypt, world, markets. Blocks 2 to
4 start from the week's saved notes in `editions/notes/` (the daily side sessions' checked facts and sources) and
search for how each story developed since, rather than researching each day's stories again.

Start blocks 3 and 4 with `model: "sonnet"`: they mostly follow up stories the week's editions already covered and
confirm where each stands and its figures, and they write no published prose. Blocks 1 and 2 (what is new since
Friday, and the week in Egypt) run on the run's own model (leave `model` out): their notes decide the recap's lead
stories. The main run still writes every word and opens a page itself where a Sonnet note says "Open:" something
that matters.
