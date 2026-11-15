#!/usr/bin/env python3
"""Change the desk's big JSON files in place without reading or rewriting them whole: desk/days/DATE.json (about
50 KB, three quarters the same from one day to the next), desk/stocks.json (125 KB) and desk/views.json (40 KB).
The run reads only the parts it changes and writes only those; the rest is kept byte for byte as json.dump writes it.

Usage (from the repo root):
  desk_json.py day DATE [ASOF]        start desk/days/DATE.json from the newest day file: sets date, asOf (default:
                                      the template's), fetched (now, Cairo) and drops "sample"; prints an outline
                                      (each part's path, size and opening words) so the run sees what to rewrite
  desk_json.py outline FILE [PATH]    the same outline for any part of a file
  desk_json.py show FILE PATH ...     print those parts as JSON (several paths in one call)
  desk_json.py set FILE PATCH         apply a patch: a JSON object of {path: value} from a file, or - for stdin
  desk_json.py news PATCH             add news items to desk/stocks.json: {"TICKER": [item, ...], ...}, newest first,
                                      an item whose url is already there replaced rather than added twice

FILE: day (the newest day file), day:DATE, stocks, views, or a path under the repo.
PATH: keys separated by "/" (tickers such as BRK.B keep their dot). In a list: a number (0 first, -1 last), "+" to
append, "^" to put first, or key=value to pick the element whose key has that value, e.g.
  egypt/finding                       pages/us/outlook               views/id=2026-11-09-egal-earnings/updates/+
  stocks/COMI/lastResults             egypt/calls/0/text
A value of "__delete__" removes the key or element. Each set prints what changed and checks the file still parses.

Examples:
  desk_json.py day 2026-11-16 2026-11-15
  desk_json.py show day egypt/finding egypt/calls pages/egx/outlook
  desk_json.py set day:2026-11-16 - <<'EOF'
  {"egypt/finding": "...", "egypt/calls": [...], "pages/egx/news/^": {...}}
  EOF
"""
import datetime
import glob
import json
import os
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # quiet when piped to head

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DELETE = "__delete__"


def resolve(name):
    if name == "day":
        return sorted(glob.glob(os.path.join(ROOT, "desk", "days", "*.json")))[-1]
    if name.startswith("day:"):
        return os.path.join(ROOT, "desk", "days", name[4:] + ".json")
    if name in ("stocks", "views"):
        return os.path.join(ROOT, "desk", name + ".json")
    return name if os.path.isabs(name) else os.path.join(ROOT, name)


def load(path):
    return json.load(open(path))


def save(path, data):
    """Written as the files already are (indent 1, no trailing newline unless the file had one), so a diff shows
    only what changed."""
    nl = os.path.exists(path) and open(path, "rb").read()[-1:] == b"\n"
    text = json.dumps(data, ensure_ascii=False, indent=1) + ("\n" if nl else "")
    json.loads(text)
    with open(path, "w") as f:
        f.write(text)


def parts(path):
    return [p for p in path.strip("/").split("/") if p != ""]


def step(node, key, create=False):
    """The child of node at key, for reading (create=False) or as a parent for writing (create=True)."""
    if isinstance(node, list):
        if "=" in key:
            k, v = key.split("=", 1)
            for x in node:
                if isinstance(x, dict) and str(x.get(k)) == v:
                    return x
            raise KeyError(f"no element with {key}")
        return node[int(key)]
    if key not in node:
        if not create:
            raise KeyError(key)
        node[key] = {}
    return node[key]


def get(data, path):
    node = data
    for k in parts(path):
        node = step(node, k)
    return node


def put(data, path, value):
    ks = parts(path)
    node = data
    for k in ks[:-1]:
        node = step(node, k, create=True)
    last = ks[-1]
    if isinstance(node, list):
        if last == "+":
            node.append(value)
        elif last == "^":
            node.insert(0, value)
        else:
            if "=" in last:
                k, v = last.split("=", 1)
                i = next((i for i, x in enumerate(node) if isinstance(x, dict) and str(x.get(k)) == v), None)
                if i is None:
                    if value == DELETE:
                        return "absent"
                    node.append(value)
                    return "added"
            else:
                i = int(last)
            if value == DELETE:
                del node[i]
                return "removed"
            node[i] = value
        return "set"
    if value == DELETE:
        return "removed" if node.pop(last, None) is not None else "absent"
    node[last] = value
    return "set"


def preview(v, n=70):
    if isinstance(v, str):
        s = v
    elif isinstance(v, dict):
        s = next((v[k] for k in ("text", "title", "finding", "name", "headline", "id") if isinstance(v.get(k), str)), "")
    else:
        s = ""
    s = " ".join(s.split())
    return (s[:n] + "…") if len(s) > n else s


def outline(node, path="", depth=0, max_depth=2):
    size = len(json.dumps(node, ensure_ascii=False))
    label = path or "(top)"
    if isinstance(node, list):
        print(f"{'  ' * depth}{label}  [{len(node)}]  {size:,} b  {preview(node[0]) if node else ''}")
    elif isinstance(node, dict) and depth < max_depth:
        if path:
            print(f"{'  ' * depth}{label}  {{}}  {size:,} b")
        for k, v in node.items():
            outline(v, f"{path}/{k}".lstrip("/"), depth + (1 if path else 0), max_depth)
    else:
        print(f"{'  ' * depth}{label}  {size:,} b  {preview(node) or json.dumps(node, ensure_ascii=False)[:70]}")


def read_patch(arg):
    return json.load(sys.stdin if arg == "-" else open(arg))


def cmd_day(date, asof=None):
    days = sorted(p for p in glob.glob(os.path.join(ROOT, "desk", "days", "*.json")) if os.path.basename(p) < date + ".json")
    out = os.path.join(ROOT, "desk", "days", date + ".json")
    if os.path.exists(out):
        print(f"{os.path.relpath(out, ROOT)} already exists: left as it is.")
        data = load(out)
    else:
        data = load(days[-1])
        data.pop("sample", None)
        data["date"] = date
        if asof:
            data["asOf"] = asof
        cairo = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2)))
        data["fetched"] = cairo.strftime("%a, %b ") + str(cairo.day) + cairo.strftime(", %H:%M Cairo")
        save(out, data)
        print(f"{os.path.relpath(out, ROOT)} started from {os.path.basename(days[-1])}: date {date}, asOf {data.get('asOf')}, fetched {data['fetched']}.")
    print("Every part below is still the template's: rewrite what changed with `set` (show a part first if needed).")
    outline(data)


def cmd_set(name, patch_arg):
    path = resolve(name)
    data, patch = load(path), read_patch(patch_arg)
    before = os.path.getsize(path)
    for p, v in patch.items():
        try:
            print(f"{put(data, p, v):8s} {p}")
        except (KeyError, IndexError, ValueError) as e:
            print(f"FAILED   {p}: {e}")
    save(path, data)
    print(f"{os.path.relpath(path, ROOT)}: {before:,} -> {os.path.getsize(path):,} bytes, parses.")


def cmd_news(patch_arg):
    path = resolve("stocks")
    data, patch = load(path), read_patch(patch_arg)
    for t, items in patch.items():
        if t not in data["stocks"]:
            print(f"FAILED   {t}: not a desk stock")
            continue
        news = data["stocks"][t].setdefault("news", [])
        items = items if isinstance(items, list) else [items]
        urls = {x.get("url") for x in items if x.get("url")}
        kept = [x for x in news if x.get("url") not in urls]
        data["stocks"][t]["news"] = sorted(items, key=lambda x: x.get("date", ""), reverse=True) + kept
        print(f"news     {t}: {len(items)} item(s), {len(news) - len(kept)} replaced")
    save(path, data)
    print(f"desk/stocks.json saved, parses.")


def main(a):
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        return
    c = a[0]
    if c == "day":
        cmd_day(a[1], a[2] if len(a) > 2 else None)
    elif c == "outline":
        data = load(resolve(a[1]))
        outline(get(data, a[2]) if len(a) > 2 else data, a[2] if len(a) > 2 else "")
    elif c == "show":
        data = load(resolve(a[1]))
        for p in a[2:]:
            try:
                print(f"== {p}\n{json.dumps(get(data, p), ensure_ascii=False, indent=1)}")
            except (KeyError, IndexError, ValueError) as e:
                print(f"== {p}: not found ({e})")
    elif c == "set":
        cmd_set(a[1], a[2])
    elif c == "news":
        cmd_news(a[1])
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
