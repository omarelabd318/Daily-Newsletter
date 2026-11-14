# Puzzles (every edition)

Each edition (on Saturdays, the recap) has a crossword and a killer sudoku, played at `/puzzles/` and shown as a Puzzles row on the paper-mode
front page. `puzzles.py` builds both; the run only writes the clues. Keep it cheap: one `make`, one clues file.

1. `python3 .claude/skills/daily-newsletter/puzzles.py make YYYY-MM-DD --news WORD,WORD` with the edition's date and
   up to three plain words from the day's stories (NILE, GAZA, TRAIN: never a person's name). It takes a few seconds
   (about a minute on Saturdays, the larger 11 by 11 grid) and prints the grid and the answers needing clues. The
   killer sudoku gets harder through the week (Sunday easy, Saturday hardest) and is checked to have one solution.
2. Read the answers. If one is a name, an abbreviation or an obscure word, run `make` again with
   `--avoid WORD` (the same `--news`), and add lasting ones to `AVOID` in the script. Do not run `make` again after
   writing clues unless you mean to: a changed grid needs new clues.
3. Write the clues to a JSON file `{"ANSWER": "clue", ...}` and run `puzzles.py clues YYYY-MM-DD FILE`. Most clues
   are general knowledge or wordplay a solver must think about (not dictionary definitions only, and never giving
   the answer away in its own words); one to three point at the day's news (`"It ran again on the Cairo-High Dam
   line this week"`). Every fact in a news clue must be in the edition. A clue may not contain its answer.
4. `puzzles.py check YYYY-MM-DD` must pass (every answer clued, cages joined and summing right). Commit
   `data/puzzles/YYYY-MM-DD.json` with the edition.
