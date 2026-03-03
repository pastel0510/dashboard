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
| YLE Foreign | `https://yle.fi/rss/t/18-34953/fi` | Ulkomaat (foreign news from Finnish perspective) |
| YLE Economy | `https://yle.fi/rss/t/18-19274/fi` | Talous (economy) |
| YLE Politics | `https://yle.fi/rss/t/18-38033/fi` | Politiikka |
| Iltalehti News | `https://www.iltalehti.fi/rss/uutiset.xml` | Tabloid news |
| Iltalehti All | `https://www.iltalehti.fi/rss/rss.xml` | All sections |
| Ilta-Sanomat | `https://www.is.fi/rss/tuoreimmat.xml` | Tabloid news |
| Helsingin Sanomat | `https://www.hs.fi/rss/tuoreimmat.xml` | Major newspaper |
| Turun Sanomat | `https://www.ts.fi/rss/tuoreimmat.xml` | Major regional newspaper |
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

### 2. Verify Article Links (CRITICAL)

**Before including any article URL in the bulletin, you MUST verify it works:**
- Fetch the article URL using `web_fetch` to confirm it returns actual content
- **Do NOT use placeholder URLs or assume URL patterns** (e.g., don't guess `art-2000010666975.html`)
- If a link returns 404 or redirects to a homepage, drop the story — do NOT search for an alternative URL
- Links must return actual article content, not error pages

**User instruction:** "When putting links to the dashboard or any bulletin. Make sure that they work and return what they promise."

### 3. Optional: Web Search Enhancement

If web search is available and not rate-limited, use it to:
- Find additional context for major stories
- Cross-reference coverage across sources

**Important:** When using web search, you MUST restrict queries to the following Finnish domains only:
- `site:yle.fi`
- `site:iltalehti.fi`
- `site:iltasanomat.fi`
- `site:hs.fi`
- `site:ts.fi`
- `site:kauppalehti.fi`

**If web search fails (rate limit, timeout, etc.)**, proceed with RSS-only data. The bulletin should still be deliverable.

**Search queries (only if search works):**
- `site:yle.fi uutiset`
- `site:iltalehti.fi uutiset`
- `site:iltasanomat.fi uutiset`
- `site:hs.fi uutiset`
- `site:ts.fi uutiset`
- `site:kauppalehti.fi uutiset`

**Never include links from non-Finnish domains** (e.g., bloomberg.com, reuters.com, pravda.ru, etc.). The bulletin should only cover Finnish news from Finnish sources.

### 4. Score and Rank

Rank by:
1. **Impact** — major political, economic, or social significance
2. **Novelty** — breaking news, new developments
3. **Coverage** — mentioned by multiple sources
4. **Recency** — published within the `hours` window; skip older stories

Discard stories outside the time window. If fewer than `count` qualifying stories exist, deliver what is available and note the shortage.

### 5. Filter Content

**Important:** Only include general news (politics, economy, society, culture, weather, etc.). Do NOT include:
- Sports (urheilu) — exclude all sports-related news
- Cybersecurity or hacking news
- CVE or vulnerability reports
- Technical IT security topics
- Trump or Elon Musk related news (per user preference)
- **Foreign country news** — exclude stories primarily about other countries (e.g., Russia, Ukraine, USA, Sweden, Estonia). Focus on Finnish domestic news, EU matters affecting Finland, or international news where Finland is the subject.

### 6. Write the Bulletin

Select up to `count` stories. Format each entry as:

```
📅 <date> • **<story title>**
<5‑word summary of the article>
<direct article URL>
```

Where `<date>` is the publication date in a human-readable short format (e.g., "27 Feb 2026" or "2026-02-27").

- Include the DATE at the start of each entry (before the title)
- Bold the title with `**...**` (Telegram renders this as bold)
- Summary is 5 words max, placed directly under the title line with no label
- Link on its own line, no label prefix
- Separate each story with a blank line, no numbering or bullets

### 7. Deliver

Wrap in a header and footer, then send as a **single message**:

```
🇫🇮 Finnish News Bulletin — <date> (last <hours> h)

<stories>

Sources: YLE · Helsingin Sanomat · Turun Sanomat · Iltalehti · Ilta-Sanomat · Kauppalehti
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
