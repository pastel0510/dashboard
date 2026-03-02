#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime

# Load items
with open('/home/riverbank1229/.openclaw/workspace/items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Filter function
def is_excluded(title, description):
    text = (title + ' ' + description).lower()

    # Sports keywords (Finnish and English)
    sports_keywords = ['urheilu', 'kori', 'jääkiekko', 'hiihto', 'hockey', 'basketball',
                       'mm-karsinta', 'sm-liiga', 'veikkausliiga', 'nba', 'nhl', 'jalkapallo',
                       'football', 'tennis', ' Formula', 'F1', 'moottoriurheilu', 'kisat',
                       'kilpailu', 'maastohiihto', 'alppihiihto', 'taitoluistelu', 'hiihto',
                       'kestävyyshiihto', 'pikkuvauhti', 'maastojuoksu', 'juoksu', 'maila',
                       'pesäpallo', 'baseball', ' golf', 'tennis', 'boxing', 'paini',
                       'wrestling', 'moottori', 'racing', 'rally', 'motogp', 'moottoripyörä',
                       'superbike', 'nordic', 'hiihto', 'ski', 'skate', 'snowboard']

    # Trump/Elon Musk keywords
    person_keywords = ['trump', 'elon musk', 'musk']

    # Cybersecurity/CVE/technical security keywords
    security_keywords = ['cve', 'hacker', 'hakkeroi', 'tietomurto', 'haavoittuvuus',
                         'vulnerability', 'exploit', 'malware', ' ransomware', 'phishing',
                         'cyber', 'tietoturva', 'tietoturva', 'security flaw', 'zero-day']

    # Check sports
    for kw in sports_keywords:
        if kw in text:
            return True

    # Check Trump/Musk (always exclude regardless of context)
    for kw in person_keywords:
        if kw in text:
            return True

    # Check cybersecurity/technical security
    for kw in security_keywords:
        if kw in text:
            return True

    return False

# Apply filter
filtered = []
for item in items:
    if is_excluded(item['title'], item.get('description', '')):
        continue
    filtered.append(item)

print(f"Filtered from {len(items)} to {len(filtered)} items", file=sys.stderr)

# Rank: primarily by recency (pubTimestamp if available, otherwise treat as old)
# If we had pubTimestamp, we'd use it; our JSON doesn't have it after re-parse
# But items are already sorted by recency from the parser, so we'll just take the first 8
top_items = filtered[:8]

if len(top_items) < 8:
    print(f"Warning: Only {len(top_items)} items available after filtering", file=sys.stderr)

# Format date nicely
def format_date(pub_date):
    # Try to parse various formats
    for fmt in ['%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z',
                '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']:
        try:
            dt = datetime.strptime(pub_date, fmt)
            return dt.strftime('%d %b %Y')
        except:
            continue
    # Fallback
    return pub_date.split()[0:4] if len(pub_date.split()) >= 4 else pub_date

# Build bulletin
bulletin_lines = []
bulletin_lines.append("🇫🇮 Finnish News Bulletin — " + datetime.now().strftime('%d %b %Y') + " (last 24 h)")
bulletin_lines.append("")
bulletin_lines.append("")
for i, item in enumerate(top_items, 1):
    date_str = format_date(item['pubDate'])
    title = item['title']
    # Create a short summary (5 words max from description or title)
    desc = item.get('description', '').strip()
    if desc:
        # Take first few words, remove any HTML tags
        desc_clean = re.sub(r'<[^>]+>', '', desc)
        words = desc_clean.split()[:5]
        summary = ' '.join(words) + ('...' if len(desc_clean.split()) > 5 else '')
    else:
        # Use title as summary, truncated
        words = title.split()[:5]
        summary = ' '.join(words) + ('...' if len(title.split()) > 5 else '')

    link = item['link']

    bulletin_lines.append(f"📅 {date_str} • **{title}**")
    bulletin_lines.append(summary)
    bulletin_lines.append(link)
    bulletin_lines.append("")

bulletin = "\n".join(bulletin_lines)
print(bulletin)

# Also save raw bulletin for parsing
with open('/home/riverbank1229/.openclaw/workspace/bulletin.txt', 'w', encoding='utf-8') as f:
    f.write(bulletin)
