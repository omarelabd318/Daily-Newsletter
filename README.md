# Daily Newsletter

A static, dark-theme site that shows a daily newsletter (world news, Egypt, markets, sports and more). Deployed on Vercel from this repo. No build step.

## How it works

- `index.html` is the whole site. It reads `editions/index.json`, shows the newest edition, and offers an archive and older/newer buttons.
- Each edition is a Markdown file at `editions/YYYY-MM-DD.md`.
- `editions/index.json` lists the editions:

```json
{
  "editions": [
    { "date": "2026-10-25", "summary": "One short line about the top stories" }
  ]
}
```

Newest first is fine; the site sorts by date anyway.

## Adding an edition (done by the daily scheduled run)

1. Write `editions/YYYY-MM-DD.md` (Cairo date). Supported Markdown: `##`/`###` headings, paragraphs, bullet and numbered lists, **bold**, *italic*, `[links](https://...)`, `|tables|`, `> quotes`, `---`.
2. Add (or replace, if the date already exists) the entry in `editions/index.json`.
3. Commit and push to `main`. Vercel redeploys automatically.
