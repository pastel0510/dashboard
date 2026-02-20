# push-md-files

Push workspace md files to git@gitgud.io:unreached2457/md-files.git

## Usage

Run this skill to commit and push all .md files from the workspace.

## Script

```bash
#!/bin/bash
set -e

WORKSPACE="/home/riverbank1229/.openclaw/workspace"
cd "$WORKSPACE"

# Add all .md files and config examples
git add *.md memory/*.md config/*.example 2>/dev/null || true

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Commit with timestamp
git commit -m "Auto-update $(date -u '+%Y-%m-%d %H:%M UTC')"

# Push (try main first, then master)
git push origin main 2>/dev/null || git push origin master
```
