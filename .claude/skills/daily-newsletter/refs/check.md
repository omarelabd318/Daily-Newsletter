# Check before committing

Run the checker on the new edition from the repo root:

```
python3 .claude/skills/daily-newsletter/check_edition.py editions/YYYY-MM-DD.md
```

It reports:

- **Errors** (exit code 1): missing or misordered section titles, missing Markets, Stocks Watch or In Other News parts,
  a top-level `#` title, HTML, a first line that is not an italic intro, a Today at a Glance item with no
  link or a link to an anchor that does not exist, a missing What to watch today line, or an
  `editions/index.json` that does not parse or has no entry for the date. Fix all of these before committing.
- **Figures and links** (also errors or warnings): each currency-table level and each EGX30, S&P 500, Nasdaq, Dow,
  Brent and Bitcoin level written in the text is compared with the data log for the date; a mismatch is a warning
  to fix the text or the log. Every Sources link is opened: a dead page (not found) is an error, to be replaced with
  a working link to the same story; links a site refuses to check are only counted. `--no-links` skips the link
  check when offline.
- **Warnings:** first-person words or names outside quotes, sections far outside their word budget, and
  bold lead-ins that look like the same story in two sections. Read each one and fix the real problems;
  some are false alarms (a quoted "we", "US" as a country). A word-count warning is information only:
  never cut a worthwhile story to clear it.

If a story is flagged as appearing twice, keep it in the section the rules above give it and remove it
from the other.
