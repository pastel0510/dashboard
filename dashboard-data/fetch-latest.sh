#!/bin/bash
# Dashboard Update Script - builds and pushes to GitHub Pages

DASHBOARD_REPO="/tmp/dashboard"
WORKSPACE="/home/riverbank1229/.openclaw/workspace"
DASHBOARD_DATA="$WORKSPACE/dashboard-data"
GITHUB_REPO="git@github.com:pastel0510/dashboard.git"

echo "=== Dashboard Update Starting ==="

# Fetch weather data first
export DASHBOARD_DATA="/home/riverbank1229/.openclaw/workspace/dashboard-data"
python3 "$DASHBOARD_DATA/fetch-weather.py"

# Clone if missing or not a git repo
if [ ! -d "$DASHBOARD_REPO/.git" ]; then
    echo "Cloning dashboard repo..."
    rm -rf "$DASHBOARD_REPO"
    git clone "$GITHUB_REPO" "$DASHBOARD_REPO" 2>&1
fi

cd "$DASHBOARD_REPO" || exit 1
git config user.name "pastel0510"
git config user.email "pastel0510@users.noreply.github.com"

git fetch origin main
git reset --hard origin/main

# Build index.html from template with bulletin data
python3 << 'EOF'
import os, datetime, sys

data_dir = os.environ.get('DASHBOARD_DATA', '/home/riverbank1229/.openclaw/workspace/dashboard-data')

with open(os.path.join(data_dir, 'template.html')) as f:
    html = f.read()

for name in ['finnish', 'science', 'security', 'cve']:
    path = os.path.join(data_dir, f'{name}.txt')
    if os.path.exists(path):
        with open(path) as f:
            content = f.read()
        html = html.replace('{{' + name.upper() + '_BULLETIN}}', content)
    else:
        html = html.replace('{{' + name.upper() + '_BULLETIN}}', '<p>No data yet</p>')

# Weather HTML
weather_file = os.path.join(data_dir, 'weather.html')
if os.path.exists(weather_file):
    with open(weather_file) as f:
        weather_content = f.read()
    html = html.replace('{{WEATHER}}', weather_content)
else:
    html = html.replace('{{WEATHER}}', '<p>Weather data unavailable</p>')

# Self-Host Weekly HTML
selfhst_file = os.path.join(data_dir, 'selfhst.html')
if os.path.exists(selfhst_file):
    with open(selfhst_file) as f:
        selfhst_content = f.read()
    html = html.replace('{{SELFHST_BULLETIN}}', selfhst_content)
else:
    html = html.replace('{{SELFHST_BULLETIN}}', '<p>No data yet</p>')

# Remote images: read .url files and embed directly
for img in ['bunny', 'xkcd', 'fingerpori']:
    url_file = os.path.join(data_dir, f'{img}.url')
    if os.path.exists(url_file):
        with open(url_file) as f:
            url = f.read().strip()
        if url:
            html = html.replace('{{' + img.upper() + '_URL}}', f'<img src="{url}" alt="{img.capitalize()}">')
        else:
            html = html.replace('{{' + img.upper() + '_URL}}', f'<p>No {img} today</p>')
    else:
        html = html.replace('{{' + img.upper() + '_URL}}', f'<p>No {img} today</p>')

# Bunny Reddit link
reddit_file = os.path.join(data_dir, 'bunny_reddit.txt')
if os.path.exists(reddit_file):
    with open(reddit_file) as f:
        reddit_url = f.read().strip()
    html = html.replace('{{BUNNY_REDDIT}}', f'<a href="{reddit_url}" target="_blank" style="color:#00ff88;font-size:0.85em;">View on Reddit</a>' if reddit_url else '<span style="color:#666;font-size:0.85em;">No link</span>')
else:
    html = html.replace('{{BUNNY_REDDIT}}', '<span style="color:#666;font-size:0.85em;">No link</span>')

# Smiley: read .txt file
smiley_file = os.path.join(data_dir, 'smiley.txt')
if os.path.exists(smiley_file):
    with open(smiley_file) as f:
        smiley = f.read().strip()
    html = html.replace('{{SMILEY}}', smiley if smiley else 'No smiley today')
else:
    html = html.replace('{{SMILEY}}', 'No smiley today')

import datetime as dt
from zoneinfo import ZoneInfo

# Get current time in Helsinki timezone (automatically handles DST)
helsinki_time = dt.datetime.now(ZoneInfo('Europe/Helsinki'))
# Determine UTC offset
utc_offset = helsinki_time.strftime('%z')
offset_str = f"UTC{int(utc_offset[:3])}"
timestamp = helsinki_time.strftime('%Y-%m-%d %H:%M')
html = html.replace('{{TIMESTAMP}}', timestamp)
html = html.replace('{{UTC_OFFSET}}', offset_str)

with open('/tmp/dashboard/index.html', 'w') as f:
    f.write(html)
print('Built index.html')
EOF

# Commit and push
git add -A
git commit -m "Dashboard $(date -u '+%Y-%m-%d %H:%M')" || echo "No changes"
git push origin main 2>&1 | tail -3

echo "=== Dashboard Updated ==="
echo "URL: https://pastel0510.github.io/dashboard/"
