# Puzzles (every edition)

Each edition (on Saturdays, the recap) has a crossword and a killer sudoku, played at `/puzzles/` and shown as a Puzzles row on the paper-mode
front page. `puzzles.py` builds both; the run only writes the clues. Keep it cheap: one `make`, one clues file.

**Who makes them: a Sonnet side session**, not the main run (the main run holds 150-200k tokens by then, and the
make, the answers and about 45 clues would add several steps at that size). Once the edition (or the recap) is
written, start one side session with `model: "sonnet"`, in the foreground, in the same response as the main run's
next step (the index, topics and names step), with this prompt, filling in DATE, KEY (DATE, or DATE-recap on a
Saturday) and up to three plain news words:

> Make today's puzzles for the Daily Newsletter in the repo at REPO. Read
> .claude/skills/daily-newsletter/refs/puzzles.md, steps 1 to 4, and follow them for DATE, with --news WORDS. For
> the one to three news clues, read only the stories you need in editions/KEY.md (grep the lead-in and its
> paragraph; do not read the whole file); every fact in a news clue must be in the edition. Do not commit: the main
> run publishes data/puzzles/. Start nothing in the background. Return at most 40 words: PUZZLES OK or what failed.

The main run then only confirms PUZZLES OK before publishing (`puzzles.py check DATE` again if the session failed).

1. `python3 .claude/skills/daily-newsletter/puzzles.py make YYYY-MM-DD --news WORD,WORD` with the edition's date and
   up to three plain words from the day's stories (NILE, GAZA, TRAIN: never a person's name). The crossword is 11 by 11
   every day and leaves out every answer from the last 14 days' crosswords, so it takes one to two minutes (run it in
   the background if the shell times out at two); it prints the grid and the answers needing clues (about 45). The
   killer sudoku gets harder through the week (Sunday easy, Saturday hardest) and is checked to have one solution.
2. Read the answers. If one is a name, an abbreviation or an obscure word, run `make` again with
   `--avoid WORD` (the same `--news`), and add lasting ones to `AVOID` in the script. Do not run `make` again after
   writing clues unless you mean to: a changed grid needs new clues.
3. Write the clues to a JSON file `{"ANSWER": "clue", ...}` and run `puzzles.py clues YYYY-MM-DD FILE`. Most clues
   are general knowledge or wordplay a solver must think about (not dictionary definitions only, and never giving
   the answer away in its own words); one to three point at the day's news (`"It ran again on the Cairo-High Dam
   line this week"`). Every fact in a news clue must be in the edition. A clue may not contain its answer.
4. `puzzles.py check YYYY-MM-DD` must pass (every answer clued, cages joined and summing right). Commit
   `data/puzzles/YYYY-MM-DD.json` and `data/puzzles/index.json` (the archive's list, rewritten by make and clues) with the edition.
