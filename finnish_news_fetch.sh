#!/bin/bash

# Finnish News Bulletin Generator - Simplified

FEEDS=(
    "https://yle.fi/rss/uutiset/paauutiset"
    "https://yle.fi/rss/uutiset/tuoreimmat"
    "https://yle.fi/rss/t/18-34837/fi"
    "https://www.iltalehti.fi/rss/uutiset.xml"
    "https://www.is.fi/rss/tuoreimmat.xml"
)

OUTPUT="/home/riverbank1229/.openclaw/workspace/items.tsv"
> "$OUTPUT"

CURRENT_TIME=$(date +%s)
TIME_WINDOW=$((24 * 60 * 60))

for feed in "${FEEDS[@]}"; do
    echo "Fetching: $feed" >&2
    content=$(curl -sL "$feed" 2>/dev/null)
    [ -z "$content" ] && continue

    # Extract items between <item> tags
    echo "$content" | grep -oP '(?s)<item>.*?</item>' | while read -r item; do
        title=$(echo "$item" | grep -oP '(?s)(?<=<title>).*?(?=</title>)' | head -1 | sed 's/^\s*//;s/\s*$//')
        link=$(echo "$item" | grep -oP '(?s)(?<=<link>).*?(?=</link>)' | head -1 | sed 's/^\s*//;s/\s*$//')
        pubDate=$(echo "$item" | grep -oP '(?s)(?<=<pubDate>).*?(?=</pubDate>)' | head -1 | sed 's/^\s*//;s/\s*$//')
        description=$(echo "$item" | grep -oP '(?s)(?<=<description>).*?(?=</description>)' | head -1 | sed 's/^\s*//;s/\s*$//')
        [ -z "$title" ] && [ -n "$(echo "$item" | grep -oP '(?s)<title><!\[CDATA\[.*?\]\]></title>')" ] && \
            title=$(echo "$item" | grep -oP '(?s)(?<=<!\[CDATA\[).*?(?=\]\]></title>)' | head -1)

        # Skip if missing essential fields
        [ -z "$title" ] && continue
        [ -z "$link" ] && continue

        # Convert pubDate to timestamp
        if [[ "$pubDate" =~ [A-Za-z]{3},\s+[0-9]{1,2}\s+[A-Za-z]{3}\s+[0-9]{4}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}\s+[+-][0-9]{4} ]]; then
            # RFC 822 format: "Sat, 28 Feb 2026 00:00:00 +0000"
            pub_timestamp=$(date -d "$(echo "$pubDate" | sed 's/^[A-Za-z]\+,\s*//;s/\s\+[A-Za-z]\+$//')" +%s 2>/dev/null || echo 0)
        elif [[ "$pubDate" =~ [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2} ]]; then
            # ISO 8601 format
            pub_timestamp=$(date -d "$(echo "$pubDate" | sed 's/T/ /;s/\..*//')" +%s 2>/dev/null || echo 0)
        else
            pub_timestamp=0
        fi

        # Check if within time window
        if [ $pub_timestamp -gt $((CURRENT_TIME - TIME_WINDOW)) ]; then
            echo -e "$title\t$link\t$pubDate\t$description" >> "$OUTPUT"
        fi
    done
done

# Convert to JSON
echo "[" > /home/riverbank1229/.openclaw/workspace/items.json
FIRST=1
while IFS=$'\t' read -r title link pubDate description; do
    [ -z "$title" ] && continue

    title_esc=$(echo "$title" | sed 's/"/\\"/g')
    link_esc=$(echo "$link" | sed 's/"/\\"/g')
    desc_esc=$(echo "$description" | sed 's/"/\\"/g')

    if [ "$FIRST" -eq 0 ]; then
        echo "," >> /home/riverbank1229/.openclaw/workspace/items.json
    fi
    FIRST=0

    cat >> /home/riverbank1229/.openclaw/workspace/items.json <<EOF
{
  "title": "$title_esc",
  "link": "$link_esc",
  "pubDate": "$pubDate",
  "description": "$desc_esc"
}
EOF
done < "$OUTPUT"
echo "]" >> /home/riverbank1229/.openclaw/workspace/items.json

# Print count
wc -l < "$OUTPUT"
