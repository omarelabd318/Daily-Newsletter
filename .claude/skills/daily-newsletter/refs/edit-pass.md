# Edit pass, before the checker

When the edition is written, read it once from the top as its editor, not its writer, and fix what you find:

- **Leads:** each item's first sentence states the news with its figure. Rewrite one that opens on background, a
  date or a quote.
- **Why it matters:** an Egypt, economy or markets item whose point for a reader in Egypt is not plain gets one
  closing clause that says it (what it does to prices, the pound, jobs, a stock). Never a moral, never filler.
- **Against earlier editions:** for each continuing story, find the last edition that carried it and read only
  that story (`grep -n -A3 "Name" editions/*.md | tail`, not the whole file) and check that names, titles, counts and figures agree; where they differ, check the source
  and say what changed ("revised from 125").
- **Arithmetic:** recompute every percentage change, total and "highest since" from the figures in the text and the
  data log.
- **Glance and text agree:** each Today at a Glance line says what its story says, with the same figure.
- **Once only:** no story, figure or explanation appears in two sections; no "today" or "yesterday" that is wrong
  for the edition's date; no term left unexplained on first use.

Then publish as refs/finish.md describes (`publish.py newsletter DATE --push-if-clean`). End the final reply with one line, `Edit pass: N changes`, naming the biggest.

