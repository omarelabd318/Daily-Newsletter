# Judging views and writing their lessons (desk/views.json)

Read at the judging step, after the day's figures are logged. The rules for making views stay in SKILL.md
("Views: the record"); add any new rule under its "Lessons from judged views", not here.

3. **Judge** with `python3 .claude/skills/markets-desk/judge_views.py --write`, after logging the day's figures.
   It marks an entry wrong as soon as a close (or, for tests marked `"intraday": true`, a price inside the
   session) meets one of its `wrongIf` tests, judges each entry on its due date from its `track`, keeps
   "on track" and "open" current, and writes each verdict's result line. Judge by hand only what it reports it
   cannot decide (a wrong-if that is not a price, such as "the gas allocations are restored"). Never delete or
   rewrite a judged entry: wrong calls stay on the record.

4. **Write the lesson** for every entry judged that day (right, wrong or closed), in its `lesson`:
   `{"date", "text", "tag"}`. `text` is two sentences: what decided it, in figures (the driver that moved, by how
   much, against what the view assumed), and what the desk does differently because of it, or "nothing: the reasoning
   held" when a right call was right for its stated reason. A call that came right for a different reason than the one
   given says so. `tag` is a short slug for the kind of lesson (`one-driver`, `level-too-close`, `news-priced-in`,
   `horizon-too-short`, `reasoning-held`...). The Views page shows it under the verdict. When the same tag appears
   on two wrong calls, turn it into a rule under "Lessons from judged views" below, and apply it from then on.

