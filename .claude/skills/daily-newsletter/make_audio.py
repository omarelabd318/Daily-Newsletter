#!/usr/bin/env python3
"""Record the edition read aloud in a natural voice, for the site's Listen button (free: Kokoro, an open voice model
that runs here; no account or key).

Usage (from the repo root, after the edition is final):
  python3 .claude/skills/daily-newsletter/make_audio.py EDITION [--voice af_heart] [--local]

EDITION is the file key (2026-11-06, or 2026-10-28-v2). It reads the blocks read_aloud.py gives (the same ones the
site highlights), writes an MP3 and data/audio/EDITION.json (when each block starts), and publishes the MP3 on the
repo's "audio" branch, which holds only the last KEEP editions' audio (it is rewritten each time, so the audio never
piles up in the repo's history); the site plays it through the jsDelivr CDN. Commit data/audio/ afterwards.
--local writes the MP3 next to the manifest instead, for testing (do not commit it).

The first run of a session installs kokoro-onnx and downloads the model (about 330 MB, from Hugging Face; the export
that also reports each sound's length, so the site can highlight the word being read): a few
minutes in all, then about a fifth of the audio's length to record (around 5 minutes for a full edition). If anything
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
VOICE = "af_heart"   # the site's voice; others: af_bella, af_nicole, am_michael, am_puck, am_fenrir, bf_emma, bm_george
NAMES = {"af_heart": "Heart", "af_bella": "Bella", "af_nicole": "Nicole", "am_michael": "Michael", "am_puck": "Puck",
         "am_fenrir": "Fenrir", "bf_emma": "Emma", "bm_george": "George"}
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


def sentences(text, tokenize, limit=480):
    """The text in sentences, each short enough for one pass of the model (long ones split at commas)."""
    out = []
    # a sentence ends at . ! or ? followed by a space and a capital, a digit or a quote (so not inside 54.01 or a.m.)
    for s in re.findall(r"\S.*?(?:[.!?]+[\"”’)]*(?=\s+[A-Z0-9\"“‘(])|$)", text):
        s = s.strip()
        while s and len(tokenize(s)) > limit:
            cut = s.rfind(",", 0, len(s) // 2 + 40)
            cut = cut + 1 if cut > 20 else len(s) // 2
            out.append(s[:cut].strip())
            s = s[cut:].strip()
        if s:
            out.append(s)
    return out


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
        return self.tok.phonemize(t, self.lang)

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
        text = R.speakable(b["text"])
        if b["kind"] in ("section", "heading") and not text.endswith((".", "?", "!")):
            text += "."
        seg = {"sec": b["sec"], "n": b["n"], "t": round(t, 2), "w": []}
        for j, sent in enumerate(sentences(text, lambda x: V.tok.tokenize(V.phon(x)))):
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


def main(a):
    args = [x for x in a if not x.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    key = args[0]
    voice = a[a.index("--voice") + 1] if "--voice" in a else VOICE
    if voice in args:
        args.remove(voice)
    local = "--local" in a
    if not os.path.exists(os.path.join(ROOT, "editions", key + ".md")):
        sys.exit(f"No edition {key}")
    os.makedirs(AUDIO, exist_ok=True)
    try:
        deps()
        t0 = time.time()
        name = f"{key}-{voice}.mp3"
        mp3 = os.path.join(AUDIO if local else tempfile.mkdtemp(), name)
        segs, dur = record(key, voice, mp3)
        size = os.path.getsize(mp3)
        entry = {"voice": voice, "name": NAMES.get(voice, voice), "duration": dur, "file": name, "segments": segs}
        if local:
            entry["url"] = f"data/audio/{name}"
            json.dump({"edition": key, "voices": [entry]}, open(os.path.join(AUDIO, key + ".json"), "w"), separators=(",", ":"))
            print(f"Recorded {key} locally: {dur / 60:.1f} min, {size / 1e6:.1f} MB, in {time.time() - t0:.0f}s.")
            return
        # keep the newest KEEP editions' audio; the older manifests go (the site then uses the device's voice)
        mans = sorted(f[:-5] for f in os.listdir(AUDIO) if f.endswith(".json"))
        keep = sorted(set(mans + [key]))[-KEEP:]
        files, kept = {}, {}
        for k2 in keep:
            if k2 == key:
                files[name] = mp3
                kept[k2] = {"edition": key, "voices": [entry]}
            else:
                m = json.load(open(os.path.join(AUDIO, k2 + ".json")))
                for v in m["voices"]:
                    files[v["file"]] = None
                kept[k2] = m
        sha = publish(files)
        for k2, m in kept.items():
            for v in m["voices"]:
                v["url"] = f"https://cdn.jsdelivr.net/gh/{REPO}@{sha}/{v['file']}"
            json.dump(m, open(os.path.join(AUDIO, k2 + ".json"), "w"), separators=(",", ":"))
        for k2 in mans:
            if k2 not in kept:
                os.remove(os.path.join(AUDIO, k2 + ".json"))
        print(f"Audio for {key}: {dur / 60:.1f} min in the {NAMES.get(voice, voice)} voice, {size / 1e6:.1f} MB, recorded in "
              f"{time.time() - t0:.0f}s; published on the {BRANCH} branch ({len(kept)} editions kept). Commit data/audio/.")
    except Exception as e:
        print(f"Audio not made ({type(e).__name__}: {e}). The site reads this edition with the device's voice instead.")


if __name__ == "__main__":
    main(sys.argv[1:])
