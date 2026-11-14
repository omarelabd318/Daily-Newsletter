# Results days

From mid-October to late November, and again each quarter, the desk's stocks report. Two steps, both kept in
`desk/stocks.json` and shown on the stock's page (Coming up) and, on the day, in the dashboards' Since yesterday:

- **Before (up to three days ahead):** follow the earnings-preview skill's Steps 1, 2 and 4 to write `"preview"`:
  `{"date", "period", "consensus", "watch": [...], "source", "url", "written"}`. `consensus` is one sentence with the
  published estimates and where they come from ("Analysts expect EPS of $1.25 on revenue of $35bn, LSEG"); leave it
  out when none is published, as for most Egyptian companies, rather than guessing. `watch` is the three to five
  things that will decide the reaction, ranked, one line each in figures (for a bank: net interest margin, loan
  growth, provisions; for a fertilizer maker: volumes after the gas cuts, urea prices). Skip the skill's
  scenario table and options-implied move unless a source publishes them. check_desk.py warns when a stock reports
  within three days without one.
- **Read the filing, not only the report of it.** For an Egyptian company: the earnings release or financial
  statements on its investor-relations page, or the disclosure the EGX publishes (Mubasher's news page for the stock
  links it). For a US company: the earnings release (8-K) and the 10-Q, through FactIQ's search_company_filings when
  the run has it, else the company's investor page. Take from it what outlets leave out: profit attributable to
  shareholders, one-off items (currency gains, provision releases, revaluations, asset sales), the share count, the
  segment figures and the guidance in the company's words. A one-off that moved profit by 10% or more goes in the
  headline and, for an Egyptian stock, into `eps_norm` in desk/fairvalue.json with the reason. If the filing cannot
  be opened, add `"basis": "outlet reports; the filing was not read"` to `lastResults`.
- **After (the day they come out):** follow the earnings-analysis skill's method, not its format (no 8-12 page
  report, no charts): lead with the verdict, quantify the gap, say why, and say what it means for the desk's view.
  Write `"lastResults"`: `{"date", "period", "verdict" (beat, miss, in line or mixed), "headline" (one line in
  figures), "points": [two to four lines: the numbers against the estimate or last year, the guidance], "thesis"
  (one sentence: what it changes for the desk's view or projection on the stock), "source", "url"}`. With no
  published estimate, judge against last year's quarter and the preview's watch list, and say so in the headline.
  For an Egyptian stock, also record the figures with set_results.py (step 7). Then add the news to any open view on
  the stock, and change its confidence if the results move the case (Views: the record).
- **Every desk stock that reported, not only the day's lead.** The brief's "Results to record" (results_due.py)
  lists every desk stock with results out in the last ten days and not yet recorded, with the SEC's figures (US) or
  the first outlets' pages already read (Egypt), and the Egyptian stocks whose `lastResults` is written but whose
  set_results.py is not run. Work from that list rather than checking all 39 by hand; for each one whose latest
  results are not yet in `lastResults` (reported since the last run,
  or left undone by an earlier one, such as Elsewedy, e-finance, Emaar Misr and Eastern on November 12, 2026): write `lastResults`, run set_results.py (Egyptian
  stocks) so its fair value uses the new figures, and remove or correct its entry in desk/calendar.json. A results
  season can bring five in a day; give each two lines if time is short, but leave none on old figures. The run's
  summary names any left undone and why.
