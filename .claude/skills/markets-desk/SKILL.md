---
name: markets-desk
description: House rules for the Markets Desk, the daily markets analysis page planned next to the Daily Newsletter (what moved and why, which EGX sectors it helps or hurts, the reader's 24 stocks, the week ahead, open views). Use whenever writing, designing or reviewing the desk.
---

# Markets Desk

Status: the page is built at `/desk/` (`desk/index.html`) for review; it is not yet written by the daily run.
These are the rules agreed so far; add to them as the desk is finished.

## Files

- `desk/days/DATE.json`: one day's desk in two sections, `egypt` and `global` (shown as "USA"),
  each with its own finding, close figures, top call, board, note under Stocks, week ahead and open views.
  `desk/days/2026-10-30.json` is the reference for its shape. `"sample": true` marks sample content.
- `desk/index.json`: `{"desks": [{"date": "DATE", "summary": "..."}]}`; the page opens the newest.
- The charts, Your stocks and every change and YTD figure are drawn by the page from
  `data/markets-recent.json`, so log the day's figures before publishing a desk.

## What it is

A daily page of well-informed market analysis for one reader in Cairo who knows finance: terms such as
basis points, T-bills, YTD and P/E need no explanation. The newsletter says what happened; the desk says
what it means for Egyptian markets and the reader's stocks. It is published every day, from the same run
and the same research as the newsletter.

## Two sections

The desk has two sections, switched from the sidebar (`#egypt`, `#global`): **Egypt** (the EGX, the pound,
Egyptian gold and rates, the 12 Egyptian stocks) and **USA** (US markets and the 12 US stocks; its close
card lists the S&P 500 first, then the Nasdaq and the Dow Jones). Both close
cards also carry a Global group: oil, gold in dollars, the dollar index and Bitcoin. Each has its own top call, winners and losers, stocks, week ahead
and open views. A story goes in the section whose markets it moves; a global story that clearly reaches
Egypt goes in both, told from each side.

## The top call: Egypt first

In the Egypt section, the top call is the one story that matters most for **Egyptian markets and the
reader's Egyptian stocks**. In USA, it is the story that matters most for US markets and the
reader's US stocks.

- **A global story leads only when it clearly reaches Egypt**, through a channel the call names: oil
  prices, US interest rates and the dollar, money flowing in or out of emerging markets, Gulf investment,
  or Suez and Red Sea traffic. A big move abroad with no such link is not the top call, however large it
  is (for example, Alphabet falling 12.6% on its results: the EGX30 rose the same day).
- **Global stories still have a place**: in the USA section, where such a story can be the top
  call (Alphabet's fall was). When it does not reach Egypt, the Egypt section leaves it out.
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

## Who bought and who sold

In the Egypt section, a card with the EGX's net equity flows for the latest session by investor group
(Egyptian, Arab and foreign; institutions and individuals), in EGP bn, from the EGX's daily report as
carried by Mubasher, EnterpriseAM, Youm7 or Arab Finance. Check the six figures against a second report
and that they net to about zero; until they match, set `"confirmed": false` with the source named. Say in
one line what drove them, and flag a day distorted by an offering or block trade (as 29 October was by
Banque du Caire's), so the reader does not read it as a vote on the market. Never write who bought or
sold elsewhere on the desk without these figures behind it.

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
index chart (EGX30 or Nasdaq) as the largest block; a side card (Egypt: pound or dollar; USA: oil);
then winners and losers, Stocks with the 1D–1Y switch, the week ahead and open views. On a phone the top
call comes first.
