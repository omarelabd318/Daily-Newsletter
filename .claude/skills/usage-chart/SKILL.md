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

Base projections on the last few normal runs plus the changes made since, give a range,
and say in the note what they assume. Needs matplotlib (`pip install matplotlib`).
After sending the chart, add a few lines: the range's total, what drove the biggest
days, and how the last projection compared with what happened.
