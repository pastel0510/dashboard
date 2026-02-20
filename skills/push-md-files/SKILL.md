# push-md-files

Push workspace md files to git@gitgud.io:unreached2457/md-files.git

## Usage

Run this skill to commit and push all .md files from the workspace.

## Script

```bash
#!/bin/bash
set -e

WORKSPACE="/home/riverbank1229/.openclaw/workspace"
CONFIG_DIR="$WORKSPACE/config"
OPENCLAW_CONFIG="/home/riverbank1229/.openclaw/openclaw.json"
CRON_CONFIG="/home/riverbank1229/.openclaw/cron/jobs.json"

cd "$WORKSPACE"

# Ensure config dir exists
mkdir -p "$CONFIG_DIR"

# Sanitize openclaw.json
if [ -f "$OPENCLAW_CONFIG" ]; then
    cat "$OPENCLAW_CONFIG" | sed \
        -e 's/"apiKey": "[^"]*"/"apiKey": "YOUR_API_KEY"/g' \
        -e 's/"botToken": "[^"]*"/"botToken": "YOUR_TELEGRAM_BOT_TOKEN"/g' \
        -e 's/"token": "[^"]*"/"token": "YOUR_GATEWAY_TOKEN"/g' \
        > "$CONFIG_DIR/openclaw.json.example"
fi

# Sanitize cron/jobs.json
if [ -f "$CRON_CONFIG" ]; then
    cat "$CRON_CONFIG" | sed \
        -e 's/"to": "[0-9]*"/"to": "YOUR_CHAT_ID"/g' \
        -e 's/"to": "-[0-9]*"/"to": "YOUR_CHAT_ID"/g' \
        > "$CONFIG_DIR/cron-jobs.json.example"
fi

# Add all .md files and config examples
git add *.md memory/*.md config/*.example skills/*/SKILL.md 2>/dev/null || true

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit with timestamp
git commit -m "Auto-update $(date -u '+%Y-%m-%d %H:%M UTC')"

# Push
git push origin master
```
