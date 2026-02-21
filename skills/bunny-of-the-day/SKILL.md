---
name: bunny-of-the-day
description: Fetch the top-voted bunny/rabbit picture from r/bunnies and r/rabbits in the last 24 hours and send it. Use when asked for bunny pictures, or when the daily cron fires.
metadata:
  {
    "openclaw": {
      "emoji": "🐰",
      "slash": [
        {
          "name": "bunny",
          "description": "Send today's top-voted bunny picture from Reddit"
        }
      ]
    }
  }
---

# Bunny of the Day Skill

Fetches the most upvoted bunny/rabbit image from Reddit (r/bunnies + r/rabbits) in the last 24 hours and sends ONE picture.

## Usage

Run manually:
- "Send me today's bunny"
- "/bunny"

Automated:
- Daily cron at 10 PM Europe/Helsinki

## How it works

1. Agent calls the Python script to fetch Reddit data
2. Script outputs JSON with top bunny (image URL, title, upvotes, etc.)
3. Agent sends the image to Telegram using the message tool

## Script

`scripts/fetch_bunny.py` — returns JSON with top bunny data

## Agent Instructions

When this skill is triggered:

1. Run the fetch script:
```bash
python3 ~/.openclaw/workspace/skills/bunny-of-the-day/scripts/fetch_bunny.py
```

2. Parse the JSON output (last line starting with `{`)

3. Send the image to Telegram:
```
message action=send target=55163462 media=<image_url> caption=<caption>
```

4. Caption format:
```
🐰 {title}

r/{subreddit} • {ups} upvotes
{permalink}
```
