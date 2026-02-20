---
name: science-news-bulletin
description: "Generate a curated science and space news bulletin covering top stories from major science news sources. Use when asked for science news, or when the daily cron fires."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔬",
        "slash":
          [
            {
              "name": "science-news",
              "description": "Generate a science and space news bulletin.",
            },
          ],
      },
  }
---

# Science & Space News Bulletin Skill

Generate a curated bulletin of the top science and space news stories and deliver it as a single message.

## Parameters

- `hours` — lookback window. Default: `24`.
- `count` — number of stories. Default: `8`.

## Steps (follow in order)

### 1. Search each source

Use the **web search tool** to query each science news source for recent stories. Run searches in parallel where possible.

Search queries (substitute `hours` as appropriate):

| Source | Query |
|--------|-------|
| Nature | `site:nature.com news last 24 hours` |
| Science | `site:science.org news last 24 hours` |
| NASA | `site:nasa.gov news` |
| ESA | `site:esa.int news` |
| Space.com | `site:space.com news` |
| New Scientist | `site:newscientist.com news` |
| Phys.org | `site:phys.org news` |
| Scientific American | `site:scientificamerican.com news` |

Fetch the top results from each. Prioritise stories that appear across multiple sources — cross-coverage signals importance.

### 2. Score and rank

Rank by:
1. **Impact** — major scientific breakthroughs, discoveries, missions
2. **Novelty** — new discoveries, first observations, breakthroughs
3. **Coverage** — mentioned by multiple sources
4. **Recency** — published within the `hours` window; skip older stories

Discard stories outside the time window. If fewer than `count` qualifying stories exist, deliver what is available.

### 3. Write the bulletin

Select up to `count` stories. Format each entry as:

```
**Title:** <story title>
**Summary:** <10‑word summary of the article>
**Link:** <direct article URL>
```

Separate each story with a blank line and do not add numbering, bullets, or extra headers.

**Include:** Space missions, astronomy, physics, biology, climate science, medical research, technology breakthroughs, Earth science.

**Exclude:** Politics (unless directly science-related), sports, entertainment, opinion pieces.

### 4. Deliver

Wrap in a header and footer, then send as a **single message**:

```
🔬 Science & Space Bulletin — <date> (last <hours> h)

<stories>

Sources: Nature · Science · NASA · ESA · Space.com · New Scientist · Phys.org · Scientific American
```

## Notes

- **This task is slow.** Searching and reading articles typically takes 3–8 minutes. Set `timeoutSeconds: 600` or higher on the cron job.
- **Model selection matters.** A reasoning-capable model writes better summaries.
- **No speculation.** Only include stories with a verifiable published URL.

## Cron recommendations

Daily bulletin at 17:02 Helsinki time (15:02 UTC):

```
schedule: "2 15 * * *" (UTC)
model: openrouter/openai/gpt-oss-120b
timeoutSeconds: 600
```
