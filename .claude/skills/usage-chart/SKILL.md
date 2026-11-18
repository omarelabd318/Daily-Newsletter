---
name: usage-chart
description: How to show the owner how much Claude usage the daily scheduled runs (Daily Newsletter, Weekly Recap, Markets Desk) take. Use whenever asked for a usage chart, a cost chart, "how much usage", the share of the weekly limit, or a projection of the runs' usage.
---

# Usage chart for the daily runs

The owner wants usage shown one way, every time: **one PNG bar chart drawn by
`usage_chart.py`**, sent to them as an image (SendUserFile, display render), not a table
or a page of text.

What the chart shows (the script does all of it):
- One group per day, two bars: **Markets Desk** (blue) and **Newsletter** (red; on
  Saturdays that is the Weekly Recap). Each bar is labelled with its list-price cost
  (`$10.04`).
- Left axis: cost per run in list-price dollars. Right axis: share of the weekly limit,
  with 1% ≈ $3.50 (`dollars_per_percent` in runs.json).
- A gold **"Weekly limit:"** row under the day labels with each day's total share (3.6%).
- Today's label says "(today)". Days still to come are **projected**: paler hatched
  bars with a range (error bar) and a `~$7.00` label, behind a dashed divider, with a
  short note above them on what the projection assumes.
- A run that went wrong (a model fallback, a crash and resume) gets a hatched bar and a
  short grey note with an arrow. Black diamonds mark what was projected earlier for a
  day that has since run, so the projection can be checked against the real figure.
- **Under the bars, words and quality** (quality.py, run by the chart itself): one line per run of the words it
  published, and a "Quality:" row with each run's score, D (desk) and N (newsletter), green 95+ (holding), amber
  85-95 (watch), red below 85 (dropped). Each run is scored against the same kind of run before it on weighted
  pillars. Newsletter: Coverage (stories in each section and part), Verification (side-session stories confirmed at
  a second outlet, in all and per research block, and open points), Sourcing (links, outlets, Egyptian outlets,
  reliance on one outlet, pages read), Depth (words per story in Egypt News and Markets, figures in Markets),
  Freshness (source links dated within two days, lead-ins repeated from the day before) and Process (searches and
  pages against the floors). Desk: Coverage (calls, views, week ahead, news, stocks researched), Verification
  (flows, research floors), Depth, Sourcing and Discipline (short headlines, wrong-ifs, tagged news). A missing
  section or a checker error costs points; fewer words count only below 80% of usual.
- The title gives the range and its total: "Daily runs, Tue Nov 10 to Mon Nov 16: ~$128,
  ≈37% of the weekly limit".

## Getting the figures

1. `runs.json` holds every run's cost so far. Add the days that are missing.
2. A run's cost is the `total_cost_usd` of the **last** `result` event of its session
   (`list_events` with `kinds: ["result"]`, limit 100). That total is cumulative, so take
   the last one, not the sum. `list_triggers` gives each task's `last_run.session_id`;
   for older runs, use the sessions recorded earlier or the commits' Claude-Session
   lines.
3. Note anything unusual in `newsletter_flag` (with `flag_at`: [x offset in days, y in $]
   to place the note) and set `"hatch": true` for a run that went wrong.

## Drawing it

```bash
python3 .claude/skills/usage-chart/usage_chart.py START END OUT.png --today DATE \
  --proj DATE=desk,lo,hi:news,lo,hi ... --earlier DATE=desk,news --proj-note "..."
```

After a change meant to cut cost, pass `--baseline-end` with the last day before it (e.g. `--baseline-end
2026-11-18` for the Nov 19 cuts), so every later run is compared with the runs before the change, not with other
runs after it. `python3 .claude/skills/usage-chart/quality.py START END [--baseline-end DATE]` prints the same
scores with each run's pillars and figures and what fell short (LOW: ...); quote those lines when a run scores
below 95. `--blocks` adds the newsletter's verification per research block (egypt, markets, world, other, checks:
confirmed in full + partly, of the stories checked), where a cheaper research model shows first; `--detail` prints
every measure against its baseline. The research log split pages the main run opened from pages read by scripts
and side sessions on Nov 15, so pages are compared in total; only the floors use the main run's own.

Base projections on the last few normal runs plus the changes made since, give a range,
and say in the note what they assume. Needs matplotlib (`pip install matplotlib`).
After sending the chart, add a few lines: the range's total, what drove the biggest
days, how the last projection compared with what happened, and whether quality held (any run below 95, and why).
