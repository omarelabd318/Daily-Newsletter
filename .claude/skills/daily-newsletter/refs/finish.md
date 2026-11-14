# Finishing a run: checks, fixes and publishing in a fresh side session

Why: by the time the edition (or the desk) is written, the main run has every note, page and draft open, and each
further step re-sends all of it. The checker runs, the link and figure fixes, the commit and the push are about a
quarter of a run's steps but, at that size, a third of its cost. A side session that starts with only the finished
file does them for a small part of that. The writing is finished before it starts: it fixes mechanical problems and
hands anything that needs an editor's judgment back to the main run.

## What the main run does first

Before handing over, the main run has: written the edition (or the desk's files), done the edit pass, added the
editions/index.json entry, tagged the topics and rewritten their "Where it stands" (`topics.py`, the skill's
"Running topics"), made the puzzles, and logged the figures. Everything the checker needs is on disk.

## The hand-off

Start one side session with `model: "sonnet"` and wait for it (not in the background): its report is the last
thing the main run needs before the final reply. KIND is `newsletter`, `recap` or `desk`; FILE is
`editions/DATE.md`, `editions/DATE-recap.md`, or `desk/days/DATE.json` and the desk's other files.

> You are finishing today's KIND (DATE, Cairo) in the repo at REPO. The text is written and edited; your job is to
> check it, fix mechanical problems, and publish. Read .claude/skills/daily-newsletter/refs/finish.md, "What the
> finishing session may fix", and follow it. Run `python3 .claude/skills/daily-newsletter/publish.py KIND DATE`.
> Fix what that section allows, in one pass, then run it once more. If no ERROR is left and nothing needs the main
> run, run `publish.py KIND DATE --push`. If the push reports a rebase conflict, merge the files by hand keeping
> both runs' entries (data/markets.json, data/research/DATE.json and the like hold separate keys per run), commit,
> and run --push again. Start nothing in the background. Return at most 150 words: PUBLISHED and the commit, or
> NOT PUBLISHED and why; each fix made (one line each); each ERROR or WARNING left for the main run, quoted, with
> the section it is in; warnings left as information only (word counts, links a site refused to check).

## What the finishing session may fix

Mechanical only, each with the smallest change that fixes it:

- **A dead source link** (checker ERROR): find the same story at the same or another outlet (search.py or a web
  search) and replace the link, in Sources and in the text. Never drop the story.
- **A figure that does not match the data log** (checker WARNING): check the figure at its source; fix whichever is
  wrong, the text's number or the log (`log_figures.py`), never the wording around it.
- **Format errors:** a broken anchor, a misnamed or misordered heading, a missing blank line, a table cell, invalid
  JSON in index.json, desk/days or desk/index.json.
- **Names the voice may say wrong:** run `python3 .claude/skills/daily-newsletter/make_audio.py --names EDITION`
  (newsletter and recap) and fix them in pronounce.json as refs/listen.md describes.
- **A first-person word or a name outside quotes:** rephrase that clause only, keeping its meaning.
- **US spelling** the checker flags.

Everything else goes back to the main run unchanged, quoted in the report: a story in two sections, a section below
its minimum, a research shortfall, a voice problem beyond one clause, a desk view to judge or a mover's reason to
find, flows to add, and any fix that would change what a story says. Word-count warnings are information only:
never cut text to clear one.

## After the report

If the session published, the main run writes the final reply from the report. If it left something for the main
run, the main run fixes it (one Edit per section) and runs `publish.py KIND DATE --push` itself; it does not start
a second finishing session. Either way, nothing runs in the background once the final reply is written: no side
session, no background command, nothing that could finish later and wake the session again.
