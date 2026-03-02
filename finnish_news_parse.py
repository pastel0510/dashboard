#!/usr/bin/env python3
import json
import sys
import feedparser
import time
from datetime import datetime, timedelta

FEEDS = [
    "https://yle.fi/rss/uutiset/paauutiset",
    "https://yle.fi/rss/uutiset/tuoreimmat",
    "https://yle.fi/rss/t/18-34837/fi",
    "https://www.iltalehti.fi/rss/uutiset.xml",
    "https://www.is.fi/rss/tuoreimmat.xml",
]

# Time window: last 24 hours
now = time.time()
time_window = 24 * 60 * 60
items = []

for feed_url in FEEDS:
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            # Get publication time
            pub_time = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                pub_time = time.mktime(entry.published_parsed)
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                pub_time = time.mktime(entry.updated_parsed)

            if pub_time is None:
                continue

            # Filter by time window
            if pub_time < now - time_window:
                continue

            # Extract fields
            title = entry.get('title', '').strip()
            link = entry.get('link', '').strip()
            description = entry.get('description', '').strip()

            if not title or not link:
                continue

            items.append({
                'title': title,
                'link': link,
                'pubTimestamp': pub_time,
                'pubDate': entry.get('published', ''),
                'description': description
            })
    except Exception as e:
        print(f"Error fetching {feed_url}: {e}", file=sys.stderr)
        continue

# Sort by publication time (newest first)
items.sort(key=lambda x: x['pubTimestamp'], reverse=True)

# Output as JSON
print(json.dumps(items, indent=2, ensure_ascii=False))
