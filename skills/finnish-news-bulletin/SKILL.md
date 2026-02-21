---
name: finnish-news-bulletin
description: "Generate a curated Finnish general news bulletin covering top stories from major Finnish news sources. Use when asked for Finnish news, or when the daily cron fires."
metadata:
  {
    "openclaw":
      {
        "emoji": "🇫🇮",
        "slash":
          [
            {
              "name": "finnish-news",
              "description": "Generate a Finnish news bulletin from major sources.",
            },
          ],
      },
  }
---

# Finnish News Bulletin Skill

Generate a curated bulletin of the top Finnish news stories from major Finnish news sources and deliver it as a single message.

## Parameters

- `hours` — lookback window. Default: `24`.
- `count` — number of stories. Default: `8`.

## RSS Feed Sources (Primary)

Use RSS feeds as the primary source. They have no rate limits and are always available.

### RSS Feed URLs

| Source | RSS URL | Notes |
|--------|---------|-------|
| YLE Main News | `https://yle.fi/rss/uutiset/paauutiset` | Finland's public broadcaster |
| YLE Latest | `https://yle.fi/rss/uutiset/tuoreimmat` | Most recent stories |
| YLE Domestic | `https://yle.fi/rss/t/18-34837/fi` | Kotimaa (domestic news) |
| YLE Foreign | `https://yle.fi/rss/t/18-34953/fi` | Ulkomaat (foreign news) |
| YLE Economy | `https://yle.fi/rss/t/18-19274/fi` | Talous (economy) |
| YLE Politics | `https://yle.fi/rss/t/18-38033/fi` | Politiikka |
| Iltalehti News | `https://www.iltalehti.fi/rss/uutiset.xml` | Tabloid news |
| Iltalehti All | `https://www.iltalehti.fi/rss/rss.xml` | All sections |
| Ilta-Sanomat | `https://www.is.fi/rss/tuoreimmat.xml` | Tabloid news |
| Helsingin Sanomat | `https://www.hs.fi/rss/tuoreimmat.xml` | Major newspaper (may be paywalled) |
| Kauppalehti | `https://www.kauppalehti.fi/rss/latest` | Business news |

## Steps (follow in order)

### 1. Fetch RSS Feeds

Fetch RSS feeds using `web_fetch` or `curl`. Parse the XML to extract:
- Title
- Link
- Publication date
- Description/summary

Fetch from at least 3-4 sources to get broad coverage. Prioritize:
1. YLE Main News (comprehensive, free)
2. YLE Latest (most recent)
3. Iltalehti or Ilta-Sanomat (popular coverage)
4. Kauppalehti (economy/business)

**Example curl command:**
```bash
curl -sL "https://yle.fi/rss/uutiset/paauutiset" | head -200
```

RSS feeds are XML. Extract `<item>` elements with `<title>`, `<link>`, `<pubDate>`, and `<description>`.

### 2. Optional: Web Search Enhancement

If web search is available and not rate-limited, use it to:
- Find additional context for major stories
- Cross-reference coverage across sources

**If web search fails (rate limit, timeout, etc.)**, proceed with RSS-only data. The bulletin should still be deliverable.

**Search queries (only if search works):**
- `site:yle.fi uutiset` — for YLE specific stories
- `site:iltalehti.fi uutiset` — for Iltalehti stories

### 3. Score and Rank

Rank by:
1. **Impact** — major political, economic, or social significance
2. **Novelty** — breaking news, new developments
3. **Coverage** — mentioned by multiple sources
4. **Recency** — published within the `hours` window; skip older stories

Discard stories outside the time window. If fewer than `count` qualifying stories exist, deliver what is available and note the shortage.

### 4. Filter Content

**Important:** Only include general news (politics, economy, society, culture, weather, etc.). Do NOT include:
- Sports (urheilu) — exclude all sports-related news
- Cybersecurity or hacking news
- CVE or vulnerability reports
- Technical IT security topics
- Trump or Elon Musk related news (per user preference)

### 5. Write the Bulletin

Select up to `count` stories. Format each entry as plain text (no markdown, no asterisks):

```
Title: <story title>
Summary: <10‑word summary of the article>
Link: <direct article URL>
```

Separate each story with a blank line and do not add numbering, bullets, or extra headers.

### 6. Deliver

Wrap in a header and footer, then send as a **single message**:

```
🇫🇮 Finnish News Bulletin — <date> (last <hours> h)

<stories>

Sources: YLE · Helsingin Sanomat · Iltalehti · Ilta-Sanomat · Kauppalehti
```

## Resilience

- **RSS feeds always work** — no rate limits, no authentication required
- **Web search is optional** — if it fails, still produce the bulletin from RSS data
- **Never fail silently** — if all sources fail, report the error clearly

## Notes

- **This task can be slow.** Fetching and parsing RSS typically takes 2–5 minutes. Set `timeoutSeconds: 600` on the cron job.
- **Model selection matters.** A reasoning-capable model writes better summaries.
- **No speculation.** Only include stories with a verifiable published URL.
- **Finnish language:** The articles will be in Finnish. Summaries should be in English for the bulletin.

## Cron recommendations

Daily bulletin at 17:00 Helsinki time (15:00 UTC):

```
schedule: "0 15 * * *" (UTC)
model: openrouter/openai/gpt-oss-120b
timeoutSeconds: 600
```
