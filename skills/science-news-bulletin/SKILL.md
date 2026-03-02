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

**CRITICAL:** You must ONLY use links from the following domains:
- nature.com
- science.org
- nasa.gov (including jpl.nasa.gov)
- esa.int
- space.com
- newscientist.com
- phys.org
- scientificamerican.com

**DO NOT use aggregator sites** (e.g., scitechdaily.com, sci.news, others). If a search result is from any other domain, ignore it even if it seems relevant.

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

### 3. Verify article links (CRITICAL)

**Before including any URL in the bulletin, verify it works:**
- Fetch each article URL using `web_fetch` to confirm it returns actual content
- If a URL returns 404 or redirects to a homepage, find the correct URL or drop the story
- **Do NOT assume URL patterns** or use placeholder URLs
- Links must return the actual article, not an error page or unrelated content

**User rule:** "When putting links to the dashboard or any bulletin, make sure they work and return what they promise."

### 4. Write the bulletin

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
