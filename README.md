# Daily Newsletter

A daily briefing on Egypt, world news, markets, sports and culture, published at
https://daily-newsletter-eg.vercel.app. The site is a single static page deployed on Vercel from this
repo; every push to `main` redeploys it. There is no build step.

## How it works

- `index.html` is the whole site: the page, its styles and a small Markdown renderer. It reads
  `editions/index.json`, shows the newest edition, and offers an archive with search, Older/Newer links,
  a Dark/Light switch (follows the device setting until you pick one, then remembered per device), green
  and red arrows on price changes, and a print-friendly layout.
- Both the newsletter and the Markets Desk can be added to a phone's home screen as separate apps
  (iPhone: Share, then Add to Home Screen; Android Chrome: menu, then Add to Home screen or Install app).
  `manifest.webmanifest` and `desk/manifest.webmanifest` describe them, with icons in `icons/`; they open
  full screen without the browser bar. There is no service worker, so each launch loads the latest edition.
- Launched from the home screen, each shows a short opening screen (`splash.js`) once per launch, until the page is
  ready (0.7 to 1.8 seconds; on a phone it waits for a tap, with "Tap to open" once the page is ready): the Newsletter's front page with the day's summary as its headline, the Desk's chart mark
  with the EGX30's last close (the line green or red with the day) and a board of six more: EGX70, Dollar, Gold 24k, Brent, S&P 500 and Bitcoin. Links and browser tabs on a phone skip it.
  On a computer (a mouse and a window 900px or wider) it shows too, once per tab, when the start page is opened from a
  bookmark, the address bar or another site (not when moving between the site's own pages), in a wide layout with more
  on it: the Newsletter as a black-and-white broadsheet front page with the day's real stories (a dateline with the
  edition's number, the date and Cairo; the Big Story with the start of its report in two justified columns; the
  number of the day as a black panel and the quote of the day; six more stories from Today at a Glance in ruled
  columns; what to watch today along the foot, in the newsletter's own colours: paper, light or dark as set), the Desk with the EGX30 beside the board of six, the desk's finding and what comes next. It stays 4.5 to 6.5
  seconds...  `data-look` on its
  `<script>` tag picks one of three looks per app; `?splash=1`, `2` or `3` previews one in any browser (`&hold` keeps
  it up). On an iPhone the startup images in `icons/startup/` cover the moment before the page starts; they are the
  opening screen's first frame, rendered by `node icons/make_startup.js` (instructions at the top of the file). The
  Newsletter's opening screen on a phone, its startup images and its app icon all use the newsletter's paper colours
  (the sheet on its ground); the icons are rendered by `node icons/make_icons.js`.
- `/puzzles/` also has **The Globe**, a country-finding game: one mystery country a day (picked from the date, the
  same for everyone) and unlimited practice rounds. Each guess is painted on a turning globe, redder the closer its
  border is to the answer's. It needs no daily work: its map and the border-to-border distances are in
  `puzzles/globe/world.json`, built once by `puzzles/globe/build.mjs` from Natural Earth (world-atlas); `lib.js` is
  d3-array, d3-geo and topojson-client, bundled.
- On a phone (640px and narrower) both have their own layout. The newsletter (`phone.css`, `phone.js`): a compact
  masthead, the market tape and Quick Hits as strips you swipe, the sections as chips, a bar that follows you down the
  page with the section you are in and a reading-progress line, a tab bar (Today, Sections, Listen, Archive, Desk),
  sheets for the sections, the look and the archive (its Puzzles button lists every day's crossword, killer sudoku and globe game,
  oldest on the left, newest on the right), a swipe sideways to the older or newer edition (older editions lie to the
  left: swipe left for the newer one), a Share button,
  and a note when a newer edition comes out while the page is open. The desk (the phone part of `desk/nav.js`): a
  header that keeps the Egypt / US / Global switch and the page chips at the top, search and light/dark as icons, and
  a tab bar (Today, Stocks, Views, Listen, More). Larger screens are unchanged.
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
The site loads `data/markets-recent.json` (the last 400 days, rewritten by log_figures.py) and only falls
back to the full log for older editions. `.claude/skills/daily-newsletter/fetch_figures.py` fetches the
day's prices in one go at the start of each run.
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
