---
name: markets-desk
description: House rules for the Markets Desk, the daily markets analysis page planned next to the Daily Newsletter (what moved and why, which EGX sectors it helps or hurts, the reader's 24 stocks, the week ahead, open views). Use whenever writing, designing or reviewing the desk.
---

# Markets Desk

Status: the page is built at `/desk/` (`desk/index.html`) for review; it is not yet written by the daily run.
These are the rules agreed so far; add to them as the desk is finished.

## Files

- `desk/days/DATE.json`: one day's desk (the finding, the close figures, the top call, the board, the notes
  under Your stocks, the week ahead and the open views). `desk/days/2026-10-30.json` is the reference for
  its shape. `"sample": true` marks sample content.
- `desk/index.json`: `{"desks": [{"date": "DATE", "summary": "..."}]}`; the page opens the newest.
- The charts, Your stocks and every change and YTD figure are drawn by the page from
  `data/markets-recent.json`, so log the day's figures before publishing a desk.

## What it is

A daily page of well-informed market analysis for one reader in Cairo who knows finance: terms such as
basis points, T-bills, YTD and P/E need no explanation. The newsletter says what happened; the desk says
what it means for Egyptian markets and the reader's stocks. It is published every day, from the same run
and the same research as the newsletter.

## The top call: Egypt first

The top call is the one story that matters most for **Egyptian markets and the reader's stocks**.

- **A global story leads only when it clearly reaches Egypt**, through a channel the call names: oil
  prices, US interest rates and the dollar, money flowing in or out of emerging markets, Gulf investment,
  or Suez and Red Sea traffic. A big move abroad with no such link is not the top call, however large it
  is (for example, Alphabet falling 12.6% on its results: the EGX30 rose the same day).
- **Global stories still have a place**: a stock in the reader's US list goes in a one-line note under the
  USA tab of Your stocks, and a market-wide move abroad goes in the close figures, saying in a few words
  whether it reaches Egypt ("no direct read-through to the EGX").
- **Prefer the story that ties the day together**: the pound, the EGX30's move and who was buying, the
  central bank, rather than the loudest headline.

## How a call is written

Follow the morning-note skill in this repo (lead with the one thing that matters, always take a view,
"no news" is a valid answer). Every call, in the top call and on the winners and losers board, has:

- **what happened**, in figures, from checked sources;
- **the view**: a plain statement, kept apart from the facts;
- **the stocks it moves**, named;
- **wrong if**: what would show the view is wrong, specific enough to check (thesis-tracker skill);
- **a confidence level**: high, medium or low. "Momentum, not news" or "no company news found" means low.

Never present an unconfirmed claim as fact. A claim from a single source goes in a notice under the call
("reported by one source, not confirmed; the view does not rely on it"), and the view is written without it.

## Winners and losers

Two short lists, helped and hurt: EGX sectors or stocks, each with its driver, one line of reasoning
grounded in real figures, and a confidence level. Use the sector-overview skill for what drives a sector.

## The week ahead

The events that can move Egyptian markets and the reader's stocks, each rated high, medium or low impact,
with one line on why it matters (catalyst-calendar skill). Dates are checked like any other fact.

## Open views

Every view is tracked until it is right, wrong or closed, and checked each morning against the data log.
Wrong views stay on the record, marked wrong; the record is never cleaned (thesis-tracker skill).

## Figures

The same sources and checks as the newsletter: `fetch_figures.py` first, a second source for every figure,
closing prices only, and a grey dash for any figure not confirmed that morning. Trend lines, changes over
periods and YTD come from `data/markets.json`.

## Design

Laid out as the mock-up: the achromatic-ledger style from the design-taste-frontend skill, on the
newsletter's colours and fonts with its dark mode. A pinned close column on the left; the top call and its
EGX30 chart as the largest block; then winners and losers, Your stocks with the 1D–1Y switch, the week ahead
and open views. On a phone the top call comes first.
