---
name: fingerpori
description: "Fetch and deliver today's Fingerpori comic strip from Mastodon RSS. Use when asked to get the Fingerpori comic, or when the daily cron fires."
metadata:
  {
    "openclaw":
      {
        "emoji": "🦞",
        "slash": [{ "name": "fingerpori", "description": "Fetch and send today's Fingerpori comic" }],
      },
  }
---

# Fingerpori Skill

Fetch the latest Fingerpori comic from the Mastodon RSS feed and deliver it as a photo.

## Steps (follow in order)

### 1. Fetch the RSS feed

Use the **`web_fetch` tool** to fetch `https://mas.to/@fingerbotti.rss`.

> **Do NOT use `exec curl` for this step** — the server blocks requests from the sandbox IP with 403. The `web_fetch` tool bypasses this.

### 2. Find the latest `<media:content>` entry

Parse the XML returned by web_fetch to locate the first (newest) `<item>` that contains a `<media:content url="..."/>` element. Extract that URL.

### 3. Verify the date (for scheduled/cron runs)

Check the `<pubDate>` of that item. If the date is **not today** (UTC), do not deliver — instead output:

> "Fingerpori not yet posted today (latest: `<pubDate>`). Will retry next run."

Do not error or send a broken image. If this is an on-demand `/fingerpori` invocation (not a cron run), skip the date check and deliver the most recent comic regardless.

### 4. Download the image

Use `exec` to download the image (curl works fine for the image CDN):

```bash
curl -sL "<url>" -o /tmp/fingerpori_today.jpg
```

If the download fails (non-200, empty file, or not an image), announce:

> "Could not download Fingerpori image from `<url>`. Feed may be temporarily unavailable."

### 5. Send as photo

Use the `message` tool to send the downloaded file as a Telegram photo:
- `action`: `send`
- `target`: `55163462` (Telegram chat ID — do NOT use `"telegram"` as the target)
- `media`: `/tmp/fingerpori_today.jpg`
- `caption`: `Today's Fingerpori comic`

## Notes

- Step 1 (RSS fetch) **must** use `web_fetch`. Step 4 (image download) uses `exec curl`. They use different tools because the RSS server blocks sandbox IPs.
- The RSS feed is `https://mas.to/@fingerbotti.rss` (Mastodon Atom/RSS; `<media:content>` holds the image URL).
- Comics are typically posted in the morning Helsinki time (UTC+2/UTC+3). If running before ~07:00 UTC the feed may not yet have today's entry.

## Cron recommendation

One job at 07:10 UTC (after Helsinki morning publication) is sufficient. Remove any duplicate Fingerpori jobs — multiple jobs at different times result in the same comic being sent several times per day.

```
schedule: "10 7 * * *" (UTC) — daily after Helsinki morning post
model: use a fast, small model (e.g. ollama/qwen3:14b or openrouter/openai/gpt-oss-120b)
timeoutSeconds: 120
```
