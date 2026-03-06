#!/bin/bash
# push-md-files: Commit and push all .md files to git

set -e

REPO_URL="git@gitgud.io:unreached2457/md-files.git"
WORKSPACE_DIR="$HOME/.openclaw/workspace"
TIMESTAMP=$(date -u +"%Y-%m-%d_%H-%M-%S")
COMMIT_MSG="Update markdown files - $TIMESTAMP (UTC)"

cd "$WORKSPACE_DIR"

# Initialize git repo if needed
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Check if remote exists and set/update it
if git remote get-url origin &>/dev/null; then
    CURRENT_URL=$(git remote get-url origin)
    if [ "$CURRENT_URL" != "$REPO_URL" ]; then
        echo "Updating remote URL..."
        git remote set-url origin "$REPO_URL"
    fi
else
    echo "Adding remote origin..."
    git remote add origin "$REPO_URL"
fi

# Find and add all .md files (excluding venv and node_modules)
echo "Finding markdown files..."
find "$WORKSPACE_DIR" -type f -name "*.md" \
    ! -path "*/venv/*" \
    ! -path "*/.venv/*" \
    ! -path "*/node_modules/*" \
    ! -path "*/.git/*" > /tmp/md-files-list.txt

if [ ! -s /tmp/md-files-list.txt ]; then
    echo "No markdown files found to commit."
    exit 0
fi

# Add files to git (force to bypass gitignore)
echo "Adding files to git..."
while IFS= read -r file; do
    git add -f "$file"
done < /tmp/md-files-list.txt

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit."
    exit 0
fi

# Commit
echo "Committing changes..."
git commit -m "$COMMIT_MSG"

# Push
echo "Pushing to $REPO_URL..."
git push origin main || git push origin master || git push origin HEAD

echo "✅ Successfully pushed markdown files!"
