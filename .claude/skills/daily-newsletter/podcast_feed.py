#!/usr/bin/env python3
"""The Listen recordings as podcast feeds, one per voice: data/audio/feed-heart.xml and data/audio/feed-michael.xml,
served at https://daily-newsletter-eg.vercel.app/podcast/heart.xml and /podcast/michael.xml.

Usage (from the repo root; make_audio.py runs it after each recording):
  python3 .claude/skills/daily-newsletter/podcast_feed.py

Each episode is one edition the audio branch still holds (the last eight), newest first, with the edition's summary
from editions/index.json. Add a feed in a podcast app by its URL (Apple Podcasts: Library, the menu, Follow a Show by
URL; Overcast: +, Add URL). The feeds are not listed in any podcast directory.
"""
import datetime
import json
import os
import urllib.request
from email.utils import format_datetime
from xml.sax.saxutils import escape

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
AUDIO = os.path.join(ROOT, "data", "audio")
SITE = "https://daily-newsletter-eg.vercel.app"
CAIRO = datetime.timezone(datetime.timedelta(hours=2))
FEEDS = {"af_heart": "heart", "am_michael": "michael"}


def size(e):
    """The MP3's size in bytes: from the manifest, or else asked of the CDN."""
    if e.get("bytes"):
        return e["bytes"]
    try:
        r = urllib.request.urlopen(urllib.request.Request(e["url"], method="HEAD"), timeout=20)
        return int(r.headers.get("Content-Length") or 0)
    except Exception:
        return 0


def hms(sec):
    sec = int(round(sec))
    return f"{sec // 3600}:{sec // 60 % 60:02d}:{sec % 60:02d}"


def main():
    try:
        index = {(e.get("id") or e["date"]): e for e in json.load(open(os.path.join(ROOT, "editions", "index.json")))["editions"]}
    except Exception:
        index = {}
    mans = []
    for f in sorted(os.listdir(AUDIO), reverse=True):
        if f.endswith(".json"):
            try:
                mans.append(json.load(open(os.path.join(AUDIO, f))))
            except Exception:
                pass
    sizes = {}
    for voice, slug in FEEDS.items():
        name = voice.split("_")[1].title()
        items = []
        for m in mans:
            key = m["edition"]
            e = next((v for v in m.get("voices", []) if v["voice"] == voice and v.get("url", "").startswith("http")), None)
            if not e:
                continue
            d = datetime.date.fromisoformat(key[:10])
            recap = key.endswith("-recap")
            title = (f"Weekly Recap, week to {d:%B} {d.day}" if recap else f"{d:%A, %B} {d.day}")
            when = datetime.datetime(d.year, d.month, d.day, 14 if recap else 10, 0, tzinfo=CAIRO)
            summary = (index.get(key) or {}).get("summary") or ("The week's stories in review." if recap else "Today's edition.")
            link = f"{SITE}/#{key}"
            n = sizes.setdefault(e["url"], size(e))
            items.append(f"""    <item>
      <title>{escape(title)}</title>
      <description>{escape(summary)} Read the edition: {escape(link)}</description>
      <link>{escape(link)}</link>
      <guid isPermaLink="false">{escape(key)}-{voice}</guid>
      <pubDate>{format_datetime(when)}</pubDate>
      <enclosure url="{escape(e['url'])}" length="{n}" type="audio/mpeg"/>
      <itunes:duration>{hms(e.get('duration', 0))}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>
    </item>""")
        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Daily Newsletter ({name})</title>
    <link>{SITE}/</link>
    <atom:link href="{SITE}/podcast/{slug}.xml" rel="self" type="application/rss+xml"/>
    <description>The Daily Newsletter read aloud each morning: Egypt, the world, the region and the markets, about half an hour. Read by {name}.</description>
    <language>en-us</language>
    <itunes:author>Daily Newsletter</itunes:author>
    <itunes:image href="{SITE}/podcast/cover.png"/>
    <image><url>{SITE}/podcast/cover.png</url><title>Daily Newsletter ({name})</title><link>{SITE}/</link></image>
    <itunes:category text="News"><itunes:category text="Daily News"/></itunes:category>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""
        with open(os.path.join(AUDIO, f"feed-{slug}.xml"), "w") as f:
            f.write(xml)
        print(f"Podcast feed ({name}): {len(items)} episodes, {SITE}/podcast/{slug}.xml")


if __name__ == "__main__":
    main()
