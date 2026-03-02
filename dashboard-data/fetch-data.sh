#!/bin/bash
# Fetch latest data from cron runs and save to dashboard data directory

WORKSPACE="/home/riverbank1229/.openclaw/workspace"
DASHBOARD_DATA="$WORKSPACE/dashboard-data"
CRON_STATE_DIR="$WORKSPACE/.openclaw/cron"

echo "=== Fetching latest data for dashboard ==="

# JSON helper
parse_json() {
    python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data)"
}

# 1. Get latest Finnish bulletin (from cron run history)
echo "Fetching Finnish bulletin..."
python3 -c "
import json

# Read cron state
with open('$WORKSPACE/.openclaw/gateway/state.json') as f:
    state = json.load(f)

jobs = state.get('cron', {}).get('jobs', [])
for job in jobs:
    if job.get('name') == 'Finnish News Bulletin':
        last_summary = job.get('state', {}).get('lastRunSummary', '')
        if last_summary:
            # Extract content between **Title:** and **Link:** or end
            import re
            items = re.findall(r'\*\*Title:\*\* ([^\n]+)\n\*\*Summary:\*\* ([^\n]+)\n\*\*Link:\*\* ([^\n]+)', last_summary)
            html = ''
            for title, summary, link in items[:3]:
                html += f'''<div class=\"bulletin-item\">
    <h3>{title}</h3>
    <p>{summary}</p>
    <a href=\"{link}\">Read more</a>
</div>'''
            with open('$DASHBOARD_DATA/finnish.txt', 'w') as f:
                f.write(html)
            print('Saved Finnish bulletin')
            break
" 2>/dev/null || echo "Could not fetch Finnish bulletin"

# 2. Get latest Science bulletin
echo "Fetching Science bulletin..."
python3 -c "
import json

with open('$WORKSPACE/.openclaw/gateway/state.json') as f:
    state = json.load(f)

jobs = state.get('cron', {}).get('jobs', [])
for job in jobs:
    if 'Science' in job.get('name', ''):
        last_summary = job.get('state', {}).get('lastRunSummary', '')
        if last_summary:
            import re
            items = re.findall(r'\*\*Title:\*\* ([^\n]+)\n\*\*Summary:\*\* ([^\n]+)\n\*\*Link:\*\* ([^\n]+)', last_summary)
            html = ''
            for title, summary, link in items[:3]:
                html += f'''<div class=\"bulletin-item\">
    <h3>{title}</h3>
    <p>{summary}</p>
    <a href=\"{link}\">Read more</a>
</div>'''
            with open('$DASHBOARD_DATA/science.txt', 'w') as f:
                f.write(html)
            print('Saved Science bulletin')
            break
" 2>/dev/null || echo "Could not fetch Science bulletin"

# 3. Get latest Security bulletin
echo "Fetching Security bulletin..."
python3 -c "
import json

with open('$WORKSPACE/.openclaw/gateway/state.json') as f:
    state = json.load(f)

jobs = state.get('cron', {}).get('jobs', [])
for job in jobs:
    if 'Security' in job.get('name', '') and 'Mon' not in job.get('name', ''):
        last_summary = job.get('state', {}).get('lastRunSummary', '')
        if last_summary:
            import re
            items = re.findall(r'\*\*Title:\*\* ([^\n]+)\n\*\*Summary:\*\* ([^\n]+)\n\*\*Link:\*\* ([^\n]+)', last_summary)
            html = ''
            for title, summary, link in items[:3]:
                html += f'''<div class=\"bulletin-item\">
    <h3>{title}</h3>
    <p>{summary}</p>
    <a href=\"{link}\">Read more</a>
</div>'''
            with open('$DASHBOARD_DATA/security.txt', 'w') as f:
                f.write(html)
            print('Saved Security bulletin')
            break
" 2>/dev/null || echo "Could not fetch Security bulletin"

echo "=== Data fetch complete ==="
