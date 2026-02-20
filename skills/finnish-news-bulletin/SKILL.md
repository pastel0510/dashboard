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

## Steps (follow in order)

### 1. Search each source

Use the **web search tool** to query each Finnish news source for recent stories. Run searches in parallel where possible.

Search queries (substitute `hours` as appropriate):

| Source | Query |
|--------|-------|
| YLE | `site:yle.fi/a uutiset` |
| Helsingin Sanomat | `site:hs.fi uutiset` |
| Turun Sanomat | `site:ts.fi uutiset` |
| Iltalehti | `site:iltalehti.fi uutiset` |
| Ilta-Sanomat | `site:iltasanomat.fi uutiset` |
| Kauppalehti | `site:kauppalehti.fi uutiset` |

Fetch the top results from each. Prioritise stories that appear across multiple sources — cross-coverage signals importance.

### 2. Score and rank

Rank by:
1. **Impact** — major political, economic, or social significance
2. **Novelty** — breaking news, new developments
3. **Coverage** — mentioned by multiple sources
4. **Recency** — published within the `hours` window; skip older stories

Discard stories outside the time window. If fewer than `count` qualifying stories exist, deliver what is available and note the shortage.

### 3. Write the bulletin

Select up to `count` stories. Format each entry as:

```
**Title:** <story title>
**Summary:** <10‑word summary of the article>
**Link:** <direct article URL>
```

Separate each story with a blank line and do not add numbering, bullets, or extra headers.

**Important:** Only include general news (politics, economy, society, culture, weather, etc.). Do NOT include:
- Sports (urheilu) — exclude all sports-related news
- Cybersecurity or hacking news
- CVE or vulnerability reports
- Technical IT security topics

### 4. Deliver

Wrap in a header and footer, then send as a **single message**:

```
🇫🇮 Finnish News Bulletin — <date> (last <hours> h)

<stories>

Sources: YLE · Helsingin Sanomat · Turun Sanomat · Iltalehti · Ilta-Sanomat · Kauppalehti
```

## Notes

- **This task is slow.** Searching and reading articles typically takes 3–8 minutes. Set `timeoutSeconds: 600` or higher on the cron job.
- **Model selection matters.** A reasoning-capable model writes better summaries.
- **No speculation.** Only include stories with a verifiable published URL.
- **Finnish language:** The articles will be in Finnish. Summaries should be in Finnish for Finnish news sources.

## Cron recommendations

Daily bulletin at 17:00 Helsinki time (15:00 UTC):

```
schedule: "0 15 * * *" (UTC)
model: openrouter/openai/gpt-oss-120b
timeoutSeconds: 600
```
