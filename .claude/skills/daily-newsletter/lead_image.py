#!/usr/bin/env python3
"""The edition's lead image: find an openly licensed photo, and attach one to an edition.

Usage:
  lead_image.py search "Badr Abdelatty" ["second query" ...]   list candidates with license, creator and source
  lead_image.py use DATE URL --caption "..." --alt "..." --credit "..." --source PAGE_URL --license "CC BY 2.0"
                                                               download, resize and attach it to the edition
  lead_image.py remove DATE                                    take the image off an edition

The newsletter may only publish images it has the right to publish. A credit line is not a license: news photos
belong to the agency or outlet that took them. So `search` asks Openverse (a catalogue of openly licensed images
from Flickr, Wikimedia Commons and others, including the photo services of governments and international bodies) and
lists only licenses that allow reuse and editing: CC BY, CC BY-SA, CC0 and public domain. Non-commercial and
no-derivatives licenses are left out (the page crops the image and prints it in black and white).

`use` saves the picture as editions/img/DATE.jpg (at most 1400 pixels wide) and writes `image` on the edition's
entry in editions/index.json: {"src", "alt", "caption", "credit", "license", "url"}. The page shows it above the
lead story in paper mode, with the caption and the credit linked to its source page.
"""
import io
import json
import os
import sys
import urllib.parse
import urllib.request

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
INDEX = os.path.join(ROOT, "editions", "index.json")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
OK = {"by": "CC BY", "by-sa": "CC BY-SA", "cc0": "CC0", "pdm": "Public domain"}


def get(url, timeout=45):
    last = None
    for _ in range(3):   # Openverse times out now and then: three tries
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout).read()
        except Exception as e:
            last = e
    raise last


def search(queries):
    for q in queries:
        url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode({"q": q, "page_size": 20, "license": ",".join(OK)})
        try:
            res = json.loads(get(url)).get("results", [])
        except Exception as e:
            print(f'"{q}": the search failed ({e}). Try again, or go without an image.')
            continue
        print(f'"{q}": {len(res)} usable')
        for i, r in enumerate(res[:12], 1):
            lic = OK.get(r["license"], r["license"]) + (" " + r["license_version"] if r.get("license_version") and r["license"] in ("by", "by-sa") else "")
            print(f"  {i}. {r['title'][:90]}")
            print(f"     by {r.get('creator') or 'unknown'} | {lic} | {r['source']} | {r['width']}x{r['height']}")
            print(f"     image: {r['url']}")
            print(f"     page:  {r.get('foreign_landing_url')}")


def entry(data, date):
    for e in data["editions"]:
        if e.get("date") == date and not e.get("id"):
            return e
    sys.exit(f"No daily edition for {date} in editions/index.json: publish the edition first.")


def use(date, url, opt):
    need = [k for k in ("caption", "alt", "credit", "source", "license") if not opt.get(k)]
    if need:
        sys.exit("Missing: " + ", ".join("--" + k for k in need) + ". Every image carries a caption, a description, a credit, its source page and its license.")
    if not any(x in opt["license"].lower() for x in ("cc by", "cc0", "public domain")) or any(x in opt["license"].lower() for x in ("nc", "nd")):
        sys.exit("License must be CC BY, CC BY-SA, CC0 or public domain (not NC or ND).")
    try:   # the image library is not in every run's container: install it on first use
        from PIL import Image
    except Exception:
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--force-reinstall", "pillow"], capture_output=True)
        from PIL import Image
    im = Image.open(io.BytesIO(get(url))).convert("RGB")
    if im.width < 700:
        sys.exit(f"Only {im.width} pixels wide: too small to print across the lead column.")
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)))
    os.makedirs(os.path.join(ROOT, "editions", "img"), exist_ok=True)
    rel = f"editions/img/{date}.jpg"
    im.save(os.path.join(ROOT, rel), "JPEG", quality=82, optimize=True)
    data = json.load(open(INDEX))
    entry(data, date)["image"] = {"src": rel, "alt": opt["alt"], "caption": opt["caption"], "credit": f"{opt['credit']} · {opt['license']}", "license": opt["license"], "url": opt["source"]}
    json.dump(data, open(INDEX, "w"), indent=1, ensure_ascii=False)
    open(INDEX, "a").write("\n")
    print(f"{rel} ({im.width}x{im.height}, {os.path.getsize(os.path.join(ROOT, rel)) // 1024} KB) attached to {date}")


def main():
    a = sys.argv[1:]
    if len(a) >= 2 and a[0] == "search":
        search(a[1:])
    elif len(a) >= 3 and a[0] == "use":
        opt = {a[i][2:]: a[i + 1] for i in range(3, len(a) - 1) if a[i].startswith("--")}
        use(a[1], a[2], opt)
    elif len(a) == 2 and a[0] == "remove":
        data = json.load(open(INDEX))
        entry(data, a[1]).pop("image", None)
        json.dump(data, open(INDEX, "w"), indent=1, ensure_ascii=False)
        open(INDEX, "a").write("\n")
        try:
            os.remove(os.path.join(ROOT, "editions", "img", a[1] + ".jpg"))
        except OSError:
            pass
        print(f"image removed from {a[1]}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
