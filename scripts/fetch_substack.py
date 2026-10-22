"""Fetch the latest Substack posts into _data/substack.json for the homepage."""
import html
import json
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

FEED_URL = "https://doomscrollingbabel.manoel.xyz/feed"
OUT = Path(__file__).resolve().parent.parent / "_data" / "substack.json"
N_POSTS = 3

req = urllib.request.Request(FEED_URL, headers={"User-Agent": "Mozilla/5.0 (homepage feed fetcher)"})
with urllib.request.urlopen(req, timeout=30) as resp:
    root = ET.fromstring(resp.read())

posts = []
for item in root.find("channel").findall("item")[:N_POSTS]:
    enclosure = item.find("enclosure")
    posts.append({
        "title": html.unescape(item.findtext("title", "")).strip(),
        "subtitle": html.unescape(item.findtext("description", "")).strip(),
        "link": item.findtext("link", "").strip(),
        "image": enclosure.get("url") if enclosure is not None else None,
        "date": item.findtext("pubDate", "").strip(),
    })

# Keep the previous file if the feed came back empty
if not posts:
    sys.exit("No posts found in feed; leaving existing data untouched.")

OUT.write_text(json.dumps(posts, indent=2, ensure_ascii=False) + "\n")
print(f"Wrote {len(posts)} posts to {OUT}")
