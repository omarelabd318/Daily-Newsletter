#!/usr/bin/env python3
"""The daily puzzles for paper mode: a crossword and a killer sudoku, in data/puzzles/DATE.json.

Usage (from the repo root):
  puzzles.py make DATE [--news WORD,WORD] [--avoid WORD,WORD]
                                            build both puzzles (--avoid: answers not to use, to remake a grid
                                            with a weak answer; add lasting ones to AVOID below) for the edition (a few seconds); prints the crossword's
                                            answers, which still need clues
  puzzles.py clues DATE FILE                add the clues: FILE is JSON {"ANSWER": "clue", ...}, one per answer
  puzzles.py check DATE                     fail if an answer has no clue or a puzzle is missing
  puzzles.py show DATE                      print both grids

Crossword (built like a newspaper's, after the NYT's rules): a symmetric grid (it looks the same turned upside down),
every answer three letters or more, every letter in both an across and a down answer. 9 by 9 from Sunday to Friday,
11 by 11 on Saturday, so it takes ten minutes or more. Answers are words solvers know (see words()), so little
crossword filler: --news adds up to three words from the day's stories (NILE, SUEZ, GAZA), placed when
they fit. The script fills the grid; the run writes the clues, most of them general, a few pointing at the news.

Killer sudoku: the 9 by 9 sudoku rules (each row, column and box holds 1 to 9 once) with no starting digits; cages of
cells show their sum and hold no digit twice. The script checks there is exactly one solution. Cages grow larger
through the week (Sunday easy, Saturday hard).
Both are generated from the date, so running make again gives the same puzzles.
"""
import datetime
import json
import os
import random
import re
import sys
import time

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
OUT = os.path.join(ROOT, "data", "puzzles")
CACHE = os.path.expanduser("~/.cache/daily-newsletter/words.json")
AVOID = set("""abort anal anus arse bitch boob butt cock crap cunt damn dick dildo dyke fag fuck gay gook hell homo jap kike
lesbo nazi nigga nigger penis piss porn prick pussy rape rapist semen sex sexy shit slut spic tit tits twat vagina whore wank
kill killer killed murder suicide terror bomb bombs isis jihad nst leni tara marc dyn est cal cay stoye rio
ana pete ted las mil yale lama dis ave para sal els ral tad ams ens""".split())


def deps():
    try:
        import wordfreq  # noqa: F401
    except ImportError:
        import subprocess
        for extra in ([], ["--break-system-packages"]):
            if not subprocess.run([sys.executable, "-m", "pip", "install", "-q", *extra, "wordfreq"], capture_output=True).returncode:
                break


XWORD = "https://raw.githubusercontent.com/Crossword-Nexus/collaborative-word-list/main/xwordlist.dict"


STRICT = {3: 4.3, 4: 3.9, 5: 3.6}       # how common an answer must be (wordfreq's zipf scale; 3.3 for longer ones)
LOOSE = {3: 3.7, 4: 3.4, 5: 3.1}        # the 11 by 11 grid needs a wider choice of words or it rarely fills


def words(loose=False):
    """{length: [word, ...]} most familiar first. A word must pass two lists: the Crossword Nexus collaborative word
    list (constructors' scores of how good an answer is; 50 and up kept), and a large English frequency list (so the
    answer is one a solver knows: short answers must be commoner still, which keeps out crossword filler such as ESNE
    or ALOE-type obscurities). Cached after the first run (about 8 MB, a few seconds)."""
    if os.path.exists(CACHE):
        cached = json.load(open(CACHE))
        if cached.get("v") == 2:
            lim = LOOSE if loose else STRICT
            return {int(L): [w for w, z in v if z >= lim.get(int(L), 2.9 if loose else 3.3) and w.lower() not in AVOID]
                    for L, v in cached["w"].items()}
    deps()
    import urllib.request
    from wordfreq import zipf_frequency
    raw = urllib.request.urlopen(urllib.request.Request(XWORD, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read().decode("utf-8", "replace")
    # ...and a third, against names and abbreviations: the word, or the word it is a plural or verb form of, is in an
    # English dictionary in lower case (proper nouns there are capitalized)
    try:
        from english_words import get_english_words_set
    except ImportError:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "english-words"], capture_output=True)
        from english_words import get_english_words_set
    dic = get_english_words_set(["web2", "gcide"], lower=False, alpha=True)

    def common(w):
        if w in dic:
            return True
        return any(w.endswith(suf) and len(w) - len(suf) >= 3 and (w[: -len(suf)] + back) in dic
                   for suf, back in (("ies", "y"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""), ("ing", "e"), ("er", ""), ("ers", ""), ("ly", "")))
    out = {}
    for line in raw.splitlines():
        w, _, sc = line.partition(";")
        if not re.fullmatch(r"[A-Z]{3,11}", w) or not sc.strip().isdigit() or int(sc) < 50 or w.lower() in AVOID:
            continue
        if not common(w.lower()):
            continue
        z = zipf_frequency(w.lower(), "en")
        if z < LOOSE.get(len(w), 2.9):
            continue
        out.setdefault(len(w), []).append((z, w))
    out = {L: [(w, round(z, 2)) for z, w in sorted(v, reverse=True)] for L, v in out.items()}
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump({"v": 2, "w": out}, open(CACHE, "w"))
    return words(loose)


# ---------------- crossword ----------------
def pattern(n, rng, blacks):
    """A symmetric grid of n by n (it looks the same turned upside down) with about `blacks` black squares, placed at
    random where they keep every run of white squares three or more long; kept only if all white squares join up and
    no answer is longer than 7 (8 on an 11 grid): long stacks are what make a grid hard to fill with good words. Most
    tries fail; each takes a few milliseconds. Returns rows of '.' (white) and '#' (black), or None."""
    g = [["."] * n for _ in range(n)]
    cells = [(r, c) for r in range(n) for c in range(n) if (r, c) <= (n - 1 - r, n - 1 - c)]
    rng.shuffle(cells)
    placed = 0
    for r, c in cells:
        if placed >= blacks:
            break
        if r == n // 2 and c == n // 2:
            continue
        g[r][c] = g[n - 1 - r][n - 1 - c] = "#"
        if valid(g, n):
            placed += 1 if (r, c) == (n - 1 - r, n - 1 - c) else 2
        else:
            g[r][c] = g[n - 1 - r][n - 1 - c] = "."
    return g if valid(g, n, final=True, top=7 if n <= 9 else 8) else None


def runs(line):
    out, i = [], 0
    while i < len(line):
        if line[i] == "#":
            i += 1
            continue
        j = i
        while j < len(line) and line[j] != "#":
            j += 1
        out.append((i, j - i))
        i = j
    return out


def valid(g, n, final=False, top=None):
    top = top or n
    for r in range(n):
        if any(L < 3 or (final and L > top) for _, L in runs(g[r])):
            return False
    for c in range(n):
        if any(L < 3 or (final and L > top) for _, L in runs([g[r][c] for r in range(n)])):
            return False
    if final:   # every white square joined to every other; no answer longer than 9 on a 9 grid is fine
        whites = [(r, c) for r in range(n) for c in range(n) if g[r][c] == "."]
        seen, todo = {whites[0]}, [whites[0]]
        while todo:
            r, c = todo.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (r + dr, c + dc)
                if 0 <= q[0] < n and 0 <= q[1] < n and g[q[0]][q[1]] == "." and q not in seen:
                    seen.add(q)
                    todo.append(q)
        if len(seen) != len(whites):
            return False
    return True


def slots(g, n):
    out = []
    for r in range(n):
        for c, L in runs(g[r]):
            out.append(("A", r, c, L, [(r, c + k) for k in range(L)]))
    for c in range(n):
        for r, L in runs([g[x][c] for x in range(n)]):
            out.append(("D", r, c, L, [(r + k, c) for k in range(L)]))
    return out


def fill(g, n, W, rng, news, limit=6.0):
    """Fill the white squares with words (common ones tried first, with some shuffling so each day differs). News
    words go in first where they fit. Returns {cell: letter} or None."""
    S = slots(g, n)
    by_len = {}
    for L in {s[3] for s in S}:
        pool = W.get(L, [])[:12000]
        top, rest = pool[:1500], pool[1500:]
        rng.shuffle(top)
        by_len[L] = top + rest
    rank = {L: {w: i for i, w in enumerate(ws)} for L, ws in by_len.items()}
    memo = {}
    index = {}
    for L, ws in by_len.items():
        for w in ws:
            for i, ch in enumerate(w):
                index.setdefault((L, i, ch), set()).add(w)
    grid, used, t0 = {}, set(), time.time()

    def cands(s):
        L, cells = s[3], s[4]
        key = (L, "".join(grid.get(c, "?") for c in cells))
        if key in memo:
            return memo[key]
        fixed = [(i, ch) for i, ch in enumerate(key[1]) if ch != "?"]
        if not fixed:
            out = by_len[L]
        else:
            sets = sorted((index.get((L, i, ch), set()) for i, ch in fixed), key=len)
            res = set(sets[0])
            for x in sets[1:]:
                res &= x
                if not res:
                    break
            out = sorted(res, key=rank[L].get)
        memo[key] = out
        return out

    def solve():
        if time.time() - t0 > limit:
            return False
        open_ = [s for s in S if any(c not in grid for c in s[4])]
        if not open_:
            return True
        best, bc = None, None
        for s in open_:   # the slot with fewest choices goes next (counting is cheap; used words are only
            c = cands(s)    # struck out where few are left, since that is where it matters)
            if len(c) <= 8:
                c = [w for w in c if w not in used]
            if not c:
                return False
            if best is None or len(c) < len(bc):
                best, bc = s, c
                if len(c) == 1:
                    break
        bc = [w for w in bc if w not in used]
        # only the best few are tried at each step: when a corner will not fill it is cheaper to start a fresh
        # grid than to dig through thousands of alternatives
        for w in bc[:12]:
            new = [c for c in best[4] if c not in grid]
            for c, ch in zip(best[4], w):
                grid[c] = ch
            used.add(w)
            # every crossing answer this completes must be a word too (one filled square by square is not checked
            # by the slot search, which only looks at slots with an empty square)
            done = [x for x in S if x is not best and any(c in new for c in x[4]) and all(c in grid for c in x[4])]
            made = ["".join(grid[c] for c in x[4]) for x in done]
            if all(m in rank.get(len(m), {}) and m not in used and m != w for m in made) and len(set(made)) == len(made):
                used.update(made)
                if solve():
                    return True
                used.difference_update(made)
            used.discard(w)
            for c in new:
                del grid[c]
        return False

    # news words: each in the first slot of its length where it still fits
    for w in news:
        for s in S:
            if s[3] == len(w) and all(grid.get(c, ch) == ch for c, ch in zip(s[4], w)):
                for c, ch in zip(s[4], w):
                    grid[c] = ch
                used.add(w)
                break
    for w in news:
        for L in {len(w)}:
            for i, ch in enumerate(w):
                index.setdefault((L, i, ch), set()).add(w)
            by_len.setdefault(L, []).insert(0, w)
            rank[L] = {x: i for i, x in enumerate(by_len[L])}
    return dict(grid) if solve() else None


def crossword(date, news, avoid=()):
    d = datetime.date.fromisoformat(date)
    n = 11 if d.weekday() == 5 else 9
    rng = random.Random("crossword" + date)
    W = words(loose=n > 9)
    if avoid:
        bad = {x.upper() for x in avoid}
        W = {L: [w for w in v if w not in bad] for L, v in W.items()}
    news = [re.sub(r"[^A-Z]", "", x.upper()) for x in news][:3]
    news = [x for x in news if 3 <= len(x) <= n]
    tries = 0
    for attempt in range(20000):
        g = pattern(n, rng, rng.choice([16, 18, 20]) if n == 9 else rng.choice([24, 26, 28]))
        if not g:
            continue
        tries += 1
        if tries > 150:
            break
        got = fill(g, n, W, rng, news if tries <= 40 else [], limit=1.5 if n == 9 else 3.0)
        if not got:
            continue
        S = slots(g, n)
        num, nums = 0, {}
        for r in range(n):
            for c in range(n):
                if g[r][c] == "#":
                    continue
                if any(s[1] == r and s[2] == c for s in S):
                    num += 1
                    nums[(r, c)] = num
        ans = {"across": [], "down": []}
        for s in sorted(S, key=lambda s: (nums[(s[1], s[2])], s[0])):
            ans["across" if s[0] == "A" else "down"].append({"n": nums[(s[1], s[2])], "row": s[1], "col": s[2], "len": s[3],
                                                            "answer": "".join(got[c] for c in s[4]), "clue": ""})
        rows = ["".join(got.get((r, c), "#") for c in range(n)) for r in range(n)]
        placed = [w for w in news if any(a["answer"] == w for k in ans for a in ans[k])]
        return {"size": n, "grid": rows, "clues": ans, "news": placed}
    raise RuntimeError("no crossword could be filled")


# ---------------- killer sudoku ----------------
COMBOS = {}


def combos(size, total):  # (kept for reference: the solver above does not need it)
    key = (size, total)
    if key not in COMBOS:
        from itertools import combinations
        COMBOS[key] = [set(c) for c in combinations(range(1, 10), size) if sum(c) == total]
    return COMBOS[key]


def count_solutions(cages, cap=2, node_cap=None):
    """The solutions the cages allow (up to two), as {cell: digit} dicts, found with OR-Tools' CP-SAT solver: a
    second solution is looked for by forbidding the first. A fraction of a second even for Saturday's large cages."""
    try:
        from ortools.sat.python import cp_model
    except ImportError:
        import subprocess
        for extra in ([], ["--break-system-packages"]):
            if not subprocess.run([sys.executable, "-m", "pip", "install", "-q", *extra, "ortools"], capture_output=True).returncode:
                break
        from ortools.sat.python import cp_model
    m = cp_model.CpModel()
    x = {(r, c): m.NewIntVar(1, 9, f"x{r}{c}") for r in range(9) for c in range(9)}
    for i in range(9):
        m.AddAllDifferent([x[(i, c)] for c in range(9)])
        m.AddAllDifferent([x[(r, i)] for r in range(9)])
        m.AddAllDifferent([x[(i // 3 * 3 + a, i % 3 * 3 + b)] for a in range(3) for b in range(3)])
    for cg in cages:
        cells = [x[tuple(c)] for c in cg["cells"]]
        m.Add(sum(cells) == cg["sum"])
        if len(cells) > 1:
            m.AddAllDifferent(cells)
    found = []
    for _ in range(cap):
        sv = cp_model.CpSolver()
        sv.parameters.max_time_in_seconds = 10
        sv.parameters.num_workers = 4
        st = sv.Solve(m)
        if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            if st == cp_model.UNKNOWN:
                return None
            break
        sol = {k: sv.Value(v) for k, v in x.items()}
        found.append(sol)
        # forbid this solution: at least one cell differs
        diff = []
        for k, v in x.items():
            b = m.NewBoolVar("")
            m.Add(v != sol[k]).OnlyEnforceIf(b)
            m.Add(v == sol[k]).OnlyEnforceIf(b.Not())
            diff.append(b)
        m.AddBoolOr(diff)
    return found


def full_grid(rng):
    g = [[0] * 9 for _ in range(9)]

    def ok(r, c, d):
        return all(g[r][x] != d for x in range(9)) and all(g[x][c] != d for x in range(9)) and \
            all(g[r // 3 * 3 + a][c // 3 * 3 + b] != d for a in range(3) for b in range(3))

    def go(i):
        if i == 81:
            return True
        r, c = divmod(i, 9)
        ds = list(range(1, 10))
        rng.shuffle(ds)
        for d in ds:
            if ok(r, c, d):
                g[r][c] = d
                if go(i + 1):
                    return True
                g[r][c] = 0
        return False
    go(0)
    return g


def pieces(cells):
    """The joined-up groups a set of cells falls into."""
    left, out = set(cells), []
    while left:
        start = left.pop()
        grp, todo = [start], [start]
        while todo:
            r, c = todo.pop()
            for q in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if q in left:
                    left.discard(q)
                    grp.append(q)
                    todo.append(q)
        out.append(grp)
    return out


def killer(date):
    d = datetime.date.fromisoformat(date)
    level = (d.weekday() + 1) % 7          # Sunday 0 (easiest) to Saturday 6 (hardest)
    sizes = [[2, 2, 2, 3], [2, 2, 3, 3], [2, 3, 3], [2, 3, 3, 4], [3, 3, 4], [3, 3, 4, 4], [3, 4, 4, 5]][level]
    rng = random.Random("killer" + date)
    for attempt in range(300):
        sol = full_grid(rng)
        free = {(r, c) for r in range(9) for c in range(9)}
        cages = []
        order = sorted(free, key=lambda x: rng.random())
        for start in order:
            if start not in free:
                continue
            want = rng.choice(sizes)
            cells, digits = [start], {sol[start[0]][start[1]]}
            free.discard(start)
            while len(cells) < want:
                nb = [(r + dr, c + dc) for r, c in cells for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                nb = [q for q in nb if q in free and sol[q[0]][q[1]] not in digits]
                if not nb:
                    break
                q = rng.choice(nb)
                cells.append(q)
                digits.add(sol[q[0]][q[1]])
                free.discard(q)
            cages.append({"cells": cells, "sum": sum(sol[r][c] for r, c in cells)})
        # single cells merge into a neighbouring cage when that keeps its digits distinct (a lone cell is a given)
        for cg in [x for x in cages if len(x["cells"]) == 1]:
            r, c = cg["cells"][0]
            for other in cages:
                if other is cg or len(other["cells"]) >= 5:
                    continue
                if any(abs(r - a) + abs(c - b) == 1 for a, b in other["cells"]) and sol[r][c] not in {sol[a][b] for a, b in other["cells"]}:
                    other["cells"].append((r, c))
                    other["sum"] += sol[r][c]
                    cg["cells"] = []
                    break
        cages = [x for x in cages if x["cells"]]
        # make the solution unique: while the cages allow a second solution, a cell where the two differ leaves its
        # cage for a neighbouring one that can take its digit (or stands alone, as a given); a search that runs too
        # long splits the largest cage instead
        def move(cell):
            r, c = cell
            home = next(x for x in cages if cell in x["cells"])
            for other in cages:
                if other is not home and len(other["cells"]) < 5 and any(abs(r - a) + abs(c - b) == 1 for a, b in other["cells"]) \
                        and sol[r][c] not in {sol[a][b] for a, b in other["cells"]}:
                    break
            else:
                other = {"cells": [], "sum": 0}
                cages.append(other)
            home["cells"].remove(cell)
            home["sum"] -= sol[r][c]
            other["cells"].append(cell)
            other["sum"] += sol[r][c]
            # taking a cell out can cut its old cage in two; each piece becomes a cage of its own (a cage is always
            # one joined shape)
            parts = pieces(home["cells"])
            if len(parts) > 1:
                cages.remove(home)
                cages.extend({"cells": q, "sum": sum(sol[a][b] for a, b in q)} for q in parts)
            cages[:] = [x for x in cages if x["cells"]]
        found = None
        for step in range(60):
            found = count_solutions(cages)
            if found is not None and len(found) == 1:
                break
            if found is None:
                big = max(cages, key=lambda x: len(x["cells"]))
                move(big["cells"][-1])
            else:
                diff = [cell for cell in found[0] if found[0][cell] != found[1][cell]]
                move(rng.choice(diff))
        if found is not None and len(found) == 1:
            return {"level": level, "solution": "".join(str(sol[r][c]) for r in range(9) for c in range(9)),
                    "cages": [{"sum": x["sum"], "cells": [r * 9 + c for r, c in sorted(x["cells"])]} for x in cages]}
    raise RuntimeError("no killer sudoku with one solution")


# ---------------- files ----------------
def path(date):
    return os.path.join(OUT, date + ".json")


def make(date, news, avoid=(), new_killer=False):
    os.makedirs(OUT, exist_ok=True)
    t = time.time()
    old = json.load(open(path(date))) if os.path.exists(path(date)) else {}
    cw = crossword(date, news, avoid)
    # clues already written for the same answers are kept
    have = {a["answer"]: a["clue"] for k in ("across", "down") for a in (old.get("crossword") or {}).get("clues", {}).get(k, []) if a.get("clue")}
    for k in ("across", "down"):
        for a in cw["clues"][k]:
            a["clue"] = have.get(a["answer"], "")
    data = {"date": date, "crossword": cw, "killer": (not new_killer and old.get("killer")) or killer(date)}
    json.dump(data, open(path(date), "w"), ensure_ascii=False, indent=1)
    open(path(date), "a").write("\n")
    show(date)
    need = [a["answer"] for k in ("across", "down") for a in cw["clues"][k] if not a["clue"]]
    print(f"\nMade in {time.time() - t:.1f}s. {len(need)} answers need clues"
          + (f" (news words placed: {', '.join(cw['news'])})" if cw["news"] else "") + ":\n" + " ".join(need))


def clues(date, file):
    data = json.load(open(path(date)))
    given = {k.upper(): v.strip() for k, v in json.load(open(file)).items()}
    for k in ("across", "down"):
        for a in data["crossword"]["clues"][k]:
            if a["answer"] in given:
                a["clue"] = given[a["answer"]]
    json.dump(data, open(path(date), "w"), ensure_ascii=False, indent=1)
    open(path(date), "a").write("\n")
    return check(date)


def check(date):
    if not os.path.exists(path(date)):
        print(f"ERROR: no puzzles for {date}: run puzzles.py make {date}")
        return 1
    data = json.load(open(path(date)))
    miss = [a["answer"] for k in ("across", "down") for a in data["crossword"]["clues"][k] if not a.get("clue")]
    bad = [a["answer"] for k in ("across", "down") for a in data["crossword"]["clues"][k] if a.get("clue") and a["answer"].lower() in a["clue"].lower()]
    for m in miss:
        print(f"ERROR: crossword answer {m} has no clue")
    for b in bad:
        print(f"ERROR: the clue for {b} contains the answer")
    split = []
    if not data.get("killer"):
        print("ERROR: no killer sudoku")
    else:
        sol = data["killer"]["solution"]
        for cg in data["killer"]["cages"]:
            cells = [(i // 9, i % 9) for i in cg["cells"]]
            if len(pieces(cells)) > 1 or cg["sum"] != sum(int(sol[i]) for i in cg["cells"]):
                split.append(cg)
                print(f"ERROR: killer cage {cg} is not one joined shape or its sum is wrong: run make "
                      f"again with --new-killer")
        if sorted(i for cg in data["killer"]["cages"] for i in cg["cells"]) != list(range(81)):
            split.append(None)
            print("ERROR: the killer cages do not cover the grid once")
    fail = miss or bad or split or not data.get("killer")
    print(f"Puzzles {date}: {'ok' if not fail else 'fix the errors above'}.")
    return 1 if fail else 0


def show(date):
    data = json.load(open(path(date)))
    cw = data["crossword"]
    print(f"Crossword {cw['size']}x{cw['size']}:")
    for row in cw["grid"]:
        print("  " + " ".join(row))
    for k in ("across", "down"):
        print(k.upper() + ": " + "; ".join(f"{a['n']} {a['answer']}" + (f" = {a['clue']}" if a.get("clue") else "") for a in cw["clues"][k]))
    ks = data["killer"]
    print(f"Killer sudoku, level {ks['level']} of 6, {len(ks['cages'])} cages.")


def main(a):
    if len(a) >= 2 and a[0] == "make":
        news = a[a.index("--news") + 1].split(",") if "--news" in a else []
        avoid = a[a.index("--avoid") + 1].split(",") if "--avoid" in a else []
        return make(a[1], news, avoid, "--new-killer" in a)
    if len(a) == 3 and a[0] == "clues":
        sys.exit(clues(a[1], a[2]))
    if len(a) == 2 and a[0] == "check":
        sys.exit(check(a[1]))
    if len(a) == 2 and a[0] == "show":
        return show(a[1])
    print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
