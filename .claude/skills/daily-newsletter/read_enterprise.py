#!/usr/bin/env python3
"""Print the whole EnterpriseAM Egypt AM edition as plain text: every story in full, with its own link.

Usage:
  python3 .claude/skills/daily-newsletter/read_enterprise.py

Use this instead of a web-fetch summary, which can shorten or drop items and gives no story links.
Each story is printed as a heading, its link (for the Sources list) and its full text. Items without a
page of their own have no link: credit them to the edition page with "(used for N items)".
"""
import html
import re
import sys
import urllib.request

URL = "https://enterpriseam.com/egypt/am-edition/"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
SKIP = re.compile(r"^(Sections|About|Privacy & Support|Get Enterprise ?AM daily|An independent publication|"
                  r"This publication is proudly sponsored|Become a morning regular|My EnterpriseAM|Sign in|"
                  r"Check your email)", re.I)


def text(fragment):
    fragment = re.sub(r"<(script|style|svg|noscript)[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    fragment = re.sub(r"<(br|/p|/li|/h[1-6]|/tr|/div)[^>]*>", "\n", fragment, flags=re.I)
    fragment = re.sub(r"<li[^>]*>", "- ", fragment, flags=re.I)
    fragment = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    lines = [re.sub(r"[ \t\xa0]+", " ", l).strip() for l in fragment.splitlines()]
    junk = re.compile(r"^(-|Share Story|Open in new tab.*|Copy Link|Facebook.*|X -->|LinkedIn.*|WhatsApp.*|Tags:)$")
    out = []
    for l in lines:
        if l and not junk.match(l) and (not out or l != out[-1]):
            out.append(l)
    return "\n".join(out)


def main():
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    try:
        page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except Exception as e:
        sys.exit(f"Could not load {URL}: {e}. Fall back to a web fetch of the page.")
    # Split at every h2/h3: each block is one section or story.
    parts = re.split(r"(<h[23][^>]*>.*?</h[23]>)", page, flags=re.S | re.I)
    stories = 0
    for i in range(1, len(parts) - 1, 2):
        head = text(parts[i]).replace("\n", " ").strip()
        if not head or SKIP.match(head):
            continue
        block = parts[i] + parts[i + 1]
        links = re.findall(r'href="(https://enterpriseam\.com/egypt/\d{4}/\d{2}/\d{2}/[^"#?]+)"', block)
        body = text(parts[i + 1])
        if len(body) < 40:
            continue
        stories += 1
        print(f"\n## {head}")
        print(f"Link: {links[0] if links else 'none of its own (credit the edition page)'}")
        print(body[:6000])
    if not stories:
        sys.exit("No stories found: the page layout may have changed. Fall back to a web fetch of the page.")
    print(f"\n[{stories} sections read from {URL}]")


if __name__ == "__main__":
    main()
