#!/usr/bin/env python3
import re

# Read the bulletin
with open('/home/riverbank1229/.openclaw/workspace/bulletin.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse entries (separated by blank lines)
entries = []
current = []
for line in content.split('\n'):
    if line.strip() == '':
        if current:
            entries.append(current)
            current = []
    else:
        current.append(line)
if current:
    entries.append(current)

# Take first 3 stories (skip header lines)
story_entries = []
for entry in entries:
    if len(entry) >= 3 and entry[0].startswith('📅 '):
        story_entries.append(entry)
    if len(story_entries) >= 3:
        break

# Write HTML
html_lines = []
for entry in story_entries:
    # Parse first line: 📅 <date> • **<title>**
    first_line = entry[0]
    # Extract date: after 📅 and before •
    date_part = first_line.split('•')[0].replace('📅', '').strip()
    # Extract title: between **...**
    title_match = re.search(r'\*\*(.+?)\*\*', first_line)
    title = title_match.group(1) if title_match else first_line.split('•')[1].strip()

    summary = entry[1].strip()
    url = entry[2].strip()

    html_lines.append('<div class="bulletin-item">')
    html_lines.append(f'<p class="date-line">📅 {date_part}</p>')
    html_lines.append(f'<h3>{title}</h3>')
    html_lines.append(f'<p>{summary}</p>')
    html_lines.append(f'<a href="{url}">Read more</a>')
    html_lines.append('</div>')

html = '\n'.join(html_lines)

with open('/home/riverbank1229/.openclaw/workspace/dashboard-data/finnish.txt', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Wrote {len(story_entries)} entries to dashboard-data/finnish.txt")
