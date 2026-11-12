# Weekly Recap (Saturdays)

Every Saturday a separate run publishes a weekly recap alongside that day's regular edition. It sums up
the week from Sunday to Saturday. The daily rules on voice, sources, figure checks, linking visuals,
placement and standing alone all apply; the daily section list, word budgets, Today at a Glance links and
Stocks Watch do not.

- **File:** `editions/DATE-recap.md`, where DATE is the Saturday. In `editions/index.json` add
  `{"date": "DATE", "id": "DATE-recap", "label": "Weekly Recap", "summary": "..."}` and keep every other
  entry, including that day's regular edition.
- **Research:** start from that week's editions in `editions/` (Sunday to Saturday, including any second
  edition of a day), then search for how each big story developed and ended up. Report where things stand
  now, not what was said on each day. Check every figure as usual.
- **Length:** about 2,050 to 2,400 words, a 9 to 10 minute read. A guide, not a limit.
- **First line:** an italic sentence with the week's dates and what it was about, for example
  `*Week of 25 to 31 October 2026: a rate hold, a weaker pound and Egypt's Saudi deployment vote.*`
- **Sections,** in this order, each as `##` with exactly these titles:
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
- On the recap page, the site draws year-long trend lines next to the Markets This Week rows by itself;
  nothing to add for that.
- **Data log check:** before committing, run
  `python3 .claude/skills/daily-newsletter/check_log.py DATE`. Fix any real problem it finds in
  `data/markets.json` with log_figures.py (checking the figure at the source first), commit the fix, and
  list anything left unfixed in the final reply's Publishing note. It does not go in the recap itself.
- Every item opens with a bold lead-in, as in the daily edition. Never refer to the daily editions
  themselves ("as reported on Tuesday"): write about the events and their dates.

