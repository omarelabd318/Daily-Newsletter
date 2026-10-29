# Daily Newsletter

A daily briefing on Egypt, world news, markets, sports and culture, published at
https://daily-newsletter-eg.vercel.app. The site is a single static page deployed on Vercel from this
repo; every push to `main` redeploys it. There is no build step.

## How it works

- `index.html` is the whole site: the page, its styles and a small Markdown renderer. It reads
  `editions/index.json`, shows the newest edition, and offers an archive with search, Older/Newer links,
  a Dark/Light switch (follows the device setting until you pick one, then remembered per device), green
  and red arrows on price changes, and a print-friendly layout.
- Each edition is a Markdown file in `editions/`:
  - `YYYY-MM-DD.md` for the daily edition (Cairo date),
  - `YYYY-MM-DD-recap.md` for the Saturday weekly recap,
  - any other `YYYY-MM-DD-<name>.md` for an extra edition on the same day.
- `editions/index.json` lists the editions. `id` and `label` are only needed for a recap or an extra
  edition on a day that already has one:

```json
{
  "editions": [
    { "date": "2026-10-29", "summary": "One short line about the top stories" },
    { "date": "2026-10-31", "id": "2026-10-31-recap", "label": "Weekly Recap", "summary": "..." }
  ]
}
```

The site sorts by `id` (or `date`), newest first, and opens the newest one. A link such as
`https://daily-newsletter-eg.vercel.app/#2026-10-29` opens a specific edition; refreshing the page always
returns to the newest.

## Market data

`data/markets.json` holds the figures each edition showed (exchange rates, Egyptian gold, EGX30, Brent,
US indices, Bitcoin and the Stocks Watch prices), one entry per edition date. Runs add to it with
`.claude/skills/daily-newsletter/log_figures.py`. The site uses it to draw a small trend line next to
matching table rows (the last seven logged values, or about a year on the weekly recap), and the weekly
recap uses it for weekly, monthly and yearly changes. Entries marked `seed` were backfilled from market
history back to 2021 when the log was started (Egyptian stocks, EGX30 and gold from investing.com exports,
the rest from Yahoo Finance). `.claude/skills/daily-newsletter/market_facts.py` reads the log for the
Stocks Watch YTD column and context lines such as 52-week highs and lows, streaks and "highest since".
`data/holidays.json` lists the Egyptian public holidays that close the EGX (projected dates are marked
`expected` until announced). The edition checker compares Stocks Watch figures with the log, and the
Saturday recap runs `.claude/skills/daily-newsletter/check_log.py` to catch gaps and odd values.
`data/markets.xlsx` is a spreadsheet copy of the same data (headline figures, Egypt stocks, US stocks),
refreshed by `.claude/skills/daily-newsletter/export_xlsx.py` on every run.

## Who writes the editions

Scheduled Claude Code cloud tasks (managed at claude.ai, not in this repo):

| Task | When (Cairo time) | Writes |
|---|---|---|
| Daily Newsletter | Sunday to Thursday, 9:30 | `editions/DATE.md` |
| Daily Newsletter (Weekend) | Friday and Saturday, 11:30 | `editions/DATE.md` |
| Weekly Recap | Saturday, 13:48 | `editions/DATE-recap.md` |
| Backup checks | about two hours after each of the above | re-run the task if nothing was published |

Each run researches the day's news, writes the edition, checks it, commits and pushes to `main`, and
sends a short summary by push notification and email.

## House rules and checker

The editorial rules live in `.claude/skills/daily-newsletter/SKILL.md`: sections and word guide, where
each kind of story goes, Today at a Glance links, Stocks Watch, Number of the day, Explained boxes,
go-to sources for figures, figure checks, continuing stories and the weekly recap format.

Before every push, runs check the edition with:

```
python3 .claude/skills/daily-newsletter/check_edition.py editions/YYYY-MM-DD.md
```

Errors (wrong sections, broken links, invalid `index.json`) must be fixed before publishing; warnings
(voice, possible repeats, length) are for judgement.

## Markdown the site supports

`##` and `###` headings, paragraphs, bullet and numbered lists, **bold**, *italic*,
`[links](https://...)`, in-page links `[text](#story-anchor)`, `| tables |`, `> quotes` (a quote that
starts with `**Explained:` shows as a small explainer box) and `---`. Every story that opens with a bold
lead-in such as `**Rate decision:**` gets the anchor `#story-rate-decision`.
