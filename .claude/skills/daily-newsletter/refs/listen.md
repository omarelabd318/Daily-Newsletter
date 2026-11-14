# Listen (the edition read aloud)

The site's Listen button reads every edition aloud with the device's own voice; each daily edition and the recap
also get a recorded natural voice. GitHub Actions runs
`python3 .claude/skills/daily-newsletter/make_audio.py EDITION` after each push (`.github/workflows/publish.yml`;
the run itself only checks names with `--names` before the push, and never records). It
records the edition in the site's two natural voices, Heart and Michael (around 10 minutes, plus a few minutes the
first time to install the voice model; a voice already recorded from the same text is kept), publishes the
MP3 on the repo's `audio` branch (which holds only the last 8 editions' audio, a week plus the recap, and is rewritten each time: never
commit an MP3 to main) and writes `data/audio/EDITION.json`; commit `data/audio/` with the edition. If it prints
"Audio not made", go on: the site falls back to the device's voice, and say so in the final reply.
It also rewrites the two podcast feeds (`data/audio/feed-heart.xml` and `feed-michael.xml`, served at
/podcast/heart.xml and /podcast/michael.xml, with `data/audio/cover.png` as their artwork), which list the editions
the audio branch holds; they go in with `data/audio/`.

What it reads is `read_aloud.py`'s list: every section but Sources and the two watch tables, headings, paragraphs,
list items and Explained boxes, with figures written as they are said (EGP 54.01 as "54.01 pounds", 3.9% as "3.9
percent"). `listen.js` on the site builds the same list from the page to highlight the block being read; change
both together.

**Making it sound natural.** Most mistakes the voice makes fall into a few kinds, and each has a fix that applies to
every edition from then on, never to one edition alone:
- **A name said wrong** (Houthis, Abu Qir, Edita, Orascom): before recording, run `make_audio.py --names EDITION`. It
  lists the names in the edition the voice has not been checked on, with the sounds it will use. Read them: a wrong one
  goes into `pronounce.json`'s "words" with its sounds (copy the style of the entries there: IPA, a stress mark before
  the stressed vowel), a right one into "checked", so it is not listed again. Arabic names are the usual trouble:
  stress usually falls on the long vowel (ma-DOU-ly, ju-HAY-na, sa-WEE-ris).
- **A figure, unit or abbreviation read badly:** fix the rule in `read_aloud.py`'s `speakable` (and the same rule in
  `listen.js`), never the edition's text. Already handled: times (10pm as "ten P M", with no stops that made it pause),
  clock times run together (3:30 as "three thirty", with no stop at the colon), other currencies (EUR 4.10 as "4.1 euros"), "a share" after a price, a unit said once ("207.4 million dollars from
  110.2 million"), dates as ordinals ("November first", as American broadcasters say it), "re-" said "ree" in
  refinance and rebound (`pronounce.json`'s "prefix_re"), and long sentences never split inside a number.
- **A pause in the middle of a phrase:** the voice model sometimes stops for breath mid-phrase ("a fifth session ...
  in a row"). make_audio.py shortens any silence of more than a quarter of a second that does not follow punctuation,
  and says how many it shortened. If a listener still reports one, the sentence is usually too long: write shorter
  sentences in the edition.
When a listener reports a mistake, find which kind it is, fix the rule or the lexicon, and rerecord only the edition
they are listening to (`make_audio.py EDITION --force`); earlier editions are not rerecorded.

