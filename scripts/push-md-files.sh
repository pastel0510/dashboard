#!/bin/bash
# Push md files to gitgud.io

set -e

WORKSPACE="/home/riverbank1229/.openclaw/workspace"
cd "$WORKSPACE"

# Check if there are any changes
if git diff --quiet && git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Add all .md files
git add *.md memory/*.md 2>/dev/null || true

# Commit with timestamp
git commit -m "Auto-update $(date -u '+%Y-%m-%d %H:%M UTC')"

# Push
git push origin master
