#!/bin/bash
# Dashboard updater - runs after cron jobs to update the public dashboard

DASHBOARD_REPO="/tmp/dashboard"
WORKSPACE="/home/riverbank1229/.openclaw/workspace"
DASHBOARD_DATA="$WORKSPACE/dashboard-data"

echo "=== Dashboard Update Starting ==="

# Change to dashboard repo
cd "$DASHBOARD_REPO" || exit 1

# Pull latest
git fetch origin master
git reset --hard origin/master

# Read current template
cat "$DASHBOARD_DATA/template.html" > index.html

# Replace placeholders using | delimiter to handle slashes in HTML
# 1. Finnish Bulletin
if [ -f "$DASHBOARD_DATA/finnish.txt" ]; then
    FINNISH=$(cat "$DASHBOARD_DATA/finnish.txt")
    # Escape for sed
    FINNISH_ESCAPED=$(echo "$FINNISH" | sed 's/"/\\"/g' | sed 's/\//\\\//g')
    sed -i "s|{{FINNISH_BULLETIN}}|${FINNISH_ESCAPED}|g" index.html
else
    sed -i 's|{{FINNISH_BULLETIN}}|<p>No data yet</p>|g' index.html
fi

# 2. Science Bulletin
if [ -f "$DASHBOARD_DATA/science.txt" ]; then
    SCIENCE=$(cat "$DASHBOARD_DATA/science.txt")
    SCIENCE_ESCAPED=$(echo "$SCIENCE" | sed 's/"/\\"/g' | sed 's/\//\\\//g')
    sed -i "s|{{SCIENCE_BULLETIN}}|${SCIENCE_ESCAPED}|g" index.html
else
    sed -i 's|{{SCIENCE_BULLETIN}}|<p>No data yet</p>|g' index.html
fi

# 3. Security Bulletin
if [ -f "$DASHBOARD_DATA/security.txt" ]; then
    SECURITY=$(cat "$DASHBOARD_DATA/security.txt")
    SECURITY_ESCAPED=$(echo "$SECURITY" | sed 's/"/\\"/g' | sed 's/\//\\\//g')
    sed -i "s|{{SECURITY_BULLETIN}}|${SECURITY_ESCAPED}|g" index.html
else
    sed -i 's|{{SECURITY_BULLETIN}}|<p>No data yet</p>|g' index.html
fi

# 4. Bunny
if [ -f "$DASHBOARD_DATA/bunny.jpg" ]; then
    cp "$DASHBOARD_DATA/bunny.jpg" .
    BUNNY='<img src="bunny.jpg" alt="Bunny of the Day">'
    sed -i "s|{{BUNNY}}|$BUNNY|g" index.html
else
    sed -i 's|{{BUNNY}}|<p>No bunny yet</p>|g' index.html
fi

# 5. xkcd
if [ -f "$DASHBOARD_DATA/xkcd.jpg" ]; then
    cp "$DASHBOARD_DATA/xkcd.jpg" .
    XKCD='<img src="xkcd.jpg" alt="xkcd">'
    sed -i "s|{{XKCD}}|$XKCD|g" index.html
else
    sed -i 's|{{XKCD}}|<p>No xkcd yet</p>|g' index.html
fi

# 6. Fingerpori
if [ -f "$DASHBOARD_DATA/fingerpori.jpg" ]; then
    cp "$DASHBOARD_DATA/fingerpori.jpg" .
    FINGERPORI='<img src="fingerpori.jpg" alt="Fingerpori">'
    sed -i "s|{{FINGERPORI}}|$FINGERPORI|g" index.html
else
    sed -i 's|{{FINGERPORI}}|<p>No Fingerpori yet</p>|g' index.html
fi

# Timestamp
TIMESTAMP=$(date -u "+%Y-%m-%d %H:%M UTC")
sed -i "s|{{TIMESTAMP}}|$TIMESTAMP|g" index.html

# Add GitLab CI for Pages
cat > .gitlab-ci.yml << 'CIEOF'
pages:
  stage: deploy
  script:
    - mv index.html public/
  artifacts:
    paths:
    - public
  only:
    - master
CIEOF

# Commit and push
git add -A
git commit -m "Dashboard update $(date -u '+%Y-%m-%d %H:%M UTC')" || echo "No changes to commit"
git push origin master

echo "=== Dashboard Updated ==="
