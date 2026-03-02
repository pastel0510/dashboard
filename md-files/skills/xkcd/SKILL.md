---
name: xkcd
description: "Send a random xkcd comic or search for comics by topic. Use when asked for xkcd, a random comic, or searching for a specific theme."
metadata:
  {
    "openclaw":
      {
        "emoji": "🤓",
        "slash":
          [
            {
              "name": "xkcd",
              "description": "Send a random xkcd comic. Optionally pass a number, e.g. /xkcd 353",
            },
            {
              "name": "xkcd-search",
              "description": "Search xkcd comics by topic. E.g. /xkcd-search programming",
            },
          ],
      },
  }
---

# xkcd Skill

Send a random xkcd comic, fetch a specific one by number, or search for comics by topic.

## API

```bash
# Latest comic (use its number to know the current max)
curl -s "https://xkcd.com/info.0.json"

# Specific comic by number
curl -s "https://xkcd.com/353/info.0.json"
```

Response fields: `num`, `title`, `alt` (hover text — often the real punchline), `img` (image URL).

## Modes

### 1. Random Comic (default)

1. Fetch `https://xkcd.com/info.0.json` to get the current max `num`.
2. Pick a random integer between 1 and `num`, skipping 404 (it intentionally returns HTTP 404 — that's the joke).
3. Fetch `https://xkcd.com/<random>/info.0.json`.

### 2. Specific Number (`/xkcd <N>`)

Fetch `https://xkcd.com/<N>/info.0.json` directly.
If N is 404, reply: "xkcd #404: Not Found — that's the whole comic." and stop.

### 3. Search by Topic (`/xkcd-search <topic>` or "find xkcd about <topic>")

Use **web search** to find relevant xkcd comics:

```
Query: site:xkcd.com <topic>
```

Also search explainxkcd for better topic matching:

```
Query: site:explainxkcd.com <topic>
```

**Steps:**
1. Run web search with the topic
2. Parse results to extract comic numbers from URLs (e.g., `xkcd.com/353/` → comic #353)
3. Present top 3-5 matches with titles and comic numbers
4. Ask user which one to send, or send the first match if only one good result

**Example searches:**
- "xkcd about programming" → search `site:xkcd.com programming`
- "xkcd about sudo" → search `site:xkcd.com sudo`
- "xkcd about compilers" → search `site:xkcd.com compiler`

## Download and Send

### Download the image

```bash
curl -sL "<img url>" -o /tmp/xkcd_<num>.png
```

### Send as photo

Send the image as a photo with caption:

```
xkcd #<num> — <title>

🖱 <alt text>
```

Always include the `alt` hover text — it's often the actual joke.

**After sending the photo, do NOT send any additional text message.** The photo with its caption is the complete response.

## Notes

- No freshness check needed — any comic from the archive is fair game.
- A lightweight model handles this fine; it's just curl requests and a photo send.
- Comic #404 is the only special case (intentional HTTP 404).
- For searches, explainxkcd.com has transcripts and tags which improve topic matching.
