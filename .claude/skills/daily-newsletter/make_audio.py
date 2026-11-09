#!/usr/bin/env python3
"""Record the edition read aloud in a natural voice, for the site's Listen button (free: Kokoro, an open voice model
that runs here; no account or key).

Usage (from the repo root, after the edition is final):
  python3 .claude/skills/daily-newsletter/make_audio.py EDITION [--voice af_heart,am_michael] [--local] [--force]

EDITION is the file key (2026-11-06, or 2026-10-28-v2). It reads the blocks read_aloud.py gives (the same ones the
site highlights), writes an MP3 and data/audio/EDITION.json (when each block starts), and publishes the MP3 on the
repo's "audio" branch, which holds only the last KEEP editions' audio (it is rewritten each time, so the audio never
piles up in the repo's history); the site plays it through the jsDelivr CDN. Commit data/audio/ afterwards.
--local writes the MP3 next to the manifest instead, for testing (do not commit it).

The first run of a session installs kokoro-onnx and downloads the model (about 330 MB, from Hugging Face; the export
that also reports each sound's length, so the site can highlight the word being read): a few
minutes in all, then about a fifth of the audio's length to record (around 5 minutes a voice for a full edition, so
about 10 for the site's two). A voice already recorded from the same text is kept, not recorded again. If anything
fails it says so and exits 0: the site then reads the edition with the device's own voice, so the run goes on.
"""
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import read_aloud as R   # noqa: E402

ROOT = R.ROOT
AUDIO = os.path.join(ROOT, "data", "audio")
CACHE = os.path.expanduser("~/.cache/daily-newsletter/kokoro")
HF = "https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX"
REPO = "omarelabd318/Daily-Newsletter"
BRANCH = "audio"
KEEP = 8   # a week of editions plus the Saturday recap
VOICES = ["af_heart", "am_michael"]   # the site's voices, the first the default; others: af_bella, af_nicole, am_puck,
                                      # am_fenrir, am_onyx, am_echo, bf_emma, bm_george
NAMES = {"af_heart": "Heart", "af_bella": "Bella", "af_nicole": "Nicole", "am_michael": "Michael", "am_puck": "Puck",
         "am_fenrir": "Fenrir", "am_onyx": "Onyx", "am_echo": "Echo", "bf_emma": "Emma", "bm_george": "George"}
GAP = {"title": 0.8, "section": 0.55, "heading": 0.4, "text": 0.5}   # silence after each kind of block, in seconds
GAP_BEFORE_SECTION = 0.5


def sh(*a, **k):
    return subprocess.run(list(a), check=True, capture_output=True, text=True, cwd=ROOT, **k).stdout.strip()


def deps():
    try:
        import kokoro_onnx, soundfile  # noqa: F401
        return
    except ImportError:
        pass
    for extra in ([], ["--break-system-packages"]):
        r = subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check", *extra, "kokoro-onnx", "soundfile"],
                           capture_output=True, text=True)
        if not r.returncode:
            break
    import importlib
    importlib.invalidate_caches()


def model(voices):
    import numpy as np
    os.makedirs(os.path.join(CACHE, "voices"), exist_ok=True)
    m = os.path.join(CACHE, "model-timestamped.onnx")   # the export that also reports how long each sound lasts
    if not os.path.exists(m) or os.path.getsize(m) < 300e6:
        urllib.request.urlretrieve(f"{HF}-timestamped/resolve/main/onnx/model.onnx", m + ".part")
        os.replace(m + ".part", m)
    for v in voices:
        f = os.path.join(CACHE, "voices", v + ".bin")
        if not os.path.exists(f):
            urllib.request.urlretrieve(f"{HF}/resolve/main/voices/{v}.bin", f)
    return m, {v: np.fromfile(os.path.join(CACHE, "voices", v + ".bin"), dtype=np.float32).reshape(-1, 1, 256) for v in voices}


def sentences(text, size, limit=460):
    """The text in sentences, each short enough for one pass of the model (size: its length in phonemes; the model
    takes 510). A longer sentence is split at the comma nearest its middle, or else at a space."""
    out = []
    # a sentence ends at . ! or ? followed by a space and a capital, a digit or a quote (so not inside 54.01 or a.m.)
    for s in re.findall(r"\S.*?(?:[.!?]+[\"”’)]*(?=\s+[A-Z0-9\"“‘(])|$)", text):
        todo = [s.strip()]
        while todo:
            s = todo.pop(0)
            if not s:
                continue
            if size(s) <= limit:
                out.append(s)
                continue
            mid = len(s) // 2
            commas = [i for i, c in enumerate(s) if c == "," and 20 < i < len(s) - 20]
            cut = min(commas, key=lambda i: abs(i - mid)) + 1 if commas else (s.rfind(" ", 0, mid) if s.rfind(" ", 0, mid) > 0 else mid)
            todo[:0] = [s[:cut].strip(), s[cut:].strip()]
    return out


SPELLED = re.compile(r"(\b[A-Z](?:-[A-Z])+\b)")


class Voice:
    """Kokoro run directly: each sentence's audio, and when each of its words starts."""

    def __init__(self, voice):
        import numpy as np
        import onnxruntime as ort
        from kokoro_onnx.tokenizer import Tokenizer
        m, styles = model([voice])
        self.np, self.style = np, styles[voice]
        self.sess = ort.InferenceSession(m)
        self.tok = Tokenizer()
        self.lang = "en-gb" if voice.startswith("b") else "en-us"

    def phon(self, t):
        # spelled-out letters (A-I, I-P-O, U-A-E) get each letter's name: left to the phonemizer, a lone "A" reads as
        # the article ("Tech and uh-eye") and a middle one is swallowed
        parts = [p for p in SPELLED.split(t) if p.strip()]
        out = [self.letter(p) if SPELLED.fullmatch(p) else self.tok.phonemize(p, self.lang).strip() for p in parts]
        return " ".join(x for x in out if x).replace(" .", ".").replace(" ,", ",")

    def letter(self, run):
        if not hasattr(self, "_names"):
            self._names = {}
        for L in run.split("-"):
            if L not in self._names:
                self._names[L] = self.tok.phonemize(L + ".", self.lang).rstrip(".").strip()
        return "".join(self._names[L] for L in run.split("-"))

    def say(self, sentence):
        np = self.np
        ph = self.phon(sentence)
        ids = self.tok.tokenize(ph)
        wav, dur = self.sess.run(None, {"input_ids": np.array([[0, *ids, 0]], dtype=np.int64), "style": self.style[len(ids)],
                                        "speed": np.array([1.0], dtype=np.float32)})
        wav, dur = wav.ravel().astype(np.float32), dur.ravel()
        per = len(wav) / max(dur.sum(), 1e-6)                        # samples per duration frame
        starts = np.concatenate([[0], np.cumsum(dur)])[1:-1] * per   # each phoneme's first sample (the pads dropped)
        # each spoken word's place in the sentence's phonemes: in proportion to its own phonemes, snapped to the
        # nearest word gap, so the timing stays right where the sentence joins words ("for a") or splits them ("54.01")
        words = sentence.split()
        own = [len(self.phon(w)) + 1 for w in words]
        gaps = [i + 1 for i, c in enumerate(ph) if c == " "]
        kept = [c for c in ph if c in self.tok.vocab]
        pos, acc, out = 0, 0, []
        for w, n in zip(words, own):
            at = round(acc / sum(own) * len(kept))
            near = min(gaps, key=lambda g: abs(g - at)) if gaps and acc else 0
            prev = pos if out else -1
            pos = near if abs(near - at) <= 4 and near > prev else max(at, prev + 1)
            out.append((w, float(starts[min(pos, len(starts) - 1)]) / 24000 if len(starts) else 0.0))
            acc += n
        return wav, out


def record(key, voice, out_mp3):
    import numpy as np
    import soundfile as sf
    V = Voice(voice)
    d = datetime.date.fromisoformat(key[:10])
    bl = [{"sec": "", "n": 0, "kind": "title", "text": f"Daily Newsletter. {d:%A, %B} {d.day}, {d.year}."}] + R.load(key)
    sr, parts, segs, t = 24000, [], [], 0.0
    pause = lambda s: (parts.append(np.zeros(int(sr * s), dtype=np.float32)), s)[1]
    for i, b in enumerate(bl):
        if b["kind"] == "section" and i:
            t += pause(GAP_BEFORE_SECTION)
        # letters spelled out ("A I") become one word ("A-I"): said as letter names, and timed as the one word on the page
        text = re.sub(r"\b[A-Z](?: [A-Z])+\b", lambda m: m.group(0).replace(" ", "-"), R.speakable(b["text"]))
        if b["kind"] in ("section", "heading") and not text.endswith((".", "?", "!")):
            text += "."
        seg = {"sec": b["sec"], "n": b["n"], "t": round(t, 2), "w": []}
        for j, sent in enumerate(sentences(text, lambda x: len(V.phon(x)))):
            if j:
                t += pause(0.12)
            a, words = V.say(sent)
            seg["w"] += [[round((t + at - seg["t"]) * 100), w] for w, at in words]
            parts.append(a)
            t += len(a) / sr
        segs.append(seg)
        t += pause(GAP[b["kind"]])
    wav = out_mp3[:-4] + ".wav"
    sf.write(wav, np.concatenate(parts), sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-b:a", "48k", out_mp3], check=True)
    os.remove(wav)
    return segs, round(t, 1)


def publish(files):
    """files: {name: local path or None to keep from the branch}. Rewrites the audio branch as one commit holding
    exactly these files and returns its sha."""
    env = dict(os.environ, GIT_INDEX_FILE=os.path.join(tempfile.mkdtemp(), "index"))
    old = {}
    try:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True, capture_output=True)
        for line in sh("git", "ls-tree", "FETCH_HEAD").splitlines():
            meta, name = line.split("\t", 1)
            old[name] = meta.split()[2]
    except subprocess.CalledProcessError:
        pass   # no audio branch yet
    for name, path in files.items():
        blob = sh("git", "hash-object", "-w", path) if path else old.get(name)
        if blob:
            subprocess.run(["git", "update-index", "--add", "--cacheinfo", f"100644,{blob},{name}"], cwd=ROOT, env=env, check=True)
    tree = subprocess.run(["git", "write-tree"], cwd=ROOT, env=env, check=True, capture_output=True, text=True).stdout.strip()
    sha = sh("git", "commit-tree", tree, "-m", f"Audio for the last {KEEP} editions (rewritten each day)")
    for n in range(5):
        r = subprocess.run(["git", "push", "-q", "-f", "origin", f"{sha}:refs/heads/{BRANCH}"], cwd=ROOT, capture_output=True, text=True)
        if not r.returncode:
            return sha
        time.sleep(2 ** (n + 1))
    raise RuntimeError(r.stderr.strip())


def warm(url):
    """Fetch a little of a new file so the CDN has it cached (its first answer cannot be read part by part, which Safari
    needs to play and seek)."""
    try:
        urllib.request.urlopen(urllib.request.Request(url, headers={"Range": "bytes=0-1023", "User-Agent": "DailyNewsletter/1.0"}), timeout=60).read()
    except Exception:
        pass


def main(a):
    args = [x for x in a if not x.startswith("--")]
    voices = a[a.index("--voice") + 1].split(",") if "--voice" in a else VOICES
    if "--voice" in a:
        args.remove(a[a.index("--voice") + 1])
    if len(args) != 1:
        sys.exit(__doc__)
    key = args[0]
    local = "--local" in a
    src = os.path.join(ROOT, "editions", key + ".md")
    if not os.path.exists(src):
        sys.exit(f"No edition {key}")
    import hashlib
    digest = hashlib.sha1(open(src, "rb").read()).hexdigest()[:12]   # the text the audio was made from
    os.makedirs(AUDIO, exist_ok=True)
    man = os.path.join(AUDIO, key + ".json")
    try:
        old = json.load(open(man)) if os.path.exists(man) else {}
    except Exception:
        old = {}
    # --force records again even from the same text (after a change to how figures and abbreviations are read)
    done = {v["voice"]: v for v in old.get("voices", [])} if old.get("source") == digest and not local and "--force" not in a else {}
    try:
        deps()
        t0, entries, made, report = time.time(), [], {}, []
        for voice in voices:
            name = f"{key}-{voice}.mp3"
            if voice in done:   # recorded already from this same text: kept as it is
                entries.append(done[voice])
                report.append(f"{NAMES.get(voice, voice)} kept")
                continue
            t1 = time.time()
            mp3 = os.path.join(AUDIO if local else tempfile.mkdtemp(), name)
            segs, dur = record(key, voice, mp3)
            made[name] = mp3
            entries.append({"voice": voice, "name": NAMES.get(voice, voice), "duration": dur, "file": name, "segments": segs})
            report.append(f"{NAMES.get(voice, voice)} {dur / 60:.1f} min, {os.path.getsize(mp3) / 1e6:.1f} MB in {time.time() - t1:.0f}s")
        if local:
            for e in entries:
                e["url"] = f"data/audio/{e['file']}"
            json.dump({"edition": key, "source": digest, "voices": entries}, open(man, "w"), separators=(",", ":"))
            print(f"Recorded {key} locally: " + "; ".join(report) + ".")
            return
        # keep the newest KEEP editions' audio; the older manifests go (the site then uses the device's voice)
        mans = sorted(f[:-5] for f in os.listdir(AUDIO) if f.endswith(".json"))
        keep = sorted(set(mans + [key]))[-KEEP:]
        files, kept = {}, {}
        for k2 in keep:
            m = {"edition": key, "source": digest, "voices": entries} if k2 == key else json.load(open(os.path.join(AUDIO, k2 + ".json")))
            for v in m["voices"]:
                files[v["file"]] = made.get(v["file"])   # None: already on the branch
            kept[k2] = m
        sha = publish(files)
        for k2, m in kept.items():
            for v in m["voices"]:
                v["url"] = f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/{v['file']}"
            json.dump(m, open(os.path.join(AUDIO, k2 + ".json"), "w"), separators=(",", ":"))
        for k2 in mans:
            if k2 not in kept:
                os.remove(os.path.join(AUDIO, k2 + ".json"))
        for k2, m in kept.items():
            for v in m["voices"]:
                warm(v["url"])
        print(f"Audio for {key}: " + "; ".join(report) + f"; {time.time() - t0:.0f}s in all; published on the {BRANCH} branch "
              f"({len(kept)} editions kept). Commit data/audio/.")
    except Exception as e:
        print(f"Audio not made ({type(e).__name__}: {e}). The site reads this edition with the device's voice instead.")


if __name__ == "__main__":
    main(sys.argv[1:])
