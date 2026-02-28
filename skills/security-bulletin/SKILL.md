---
name: security-bulletin
description: "Generate a curated cybersecurity news bulletin covering the top stories from the last N hours. Use when asked for a security briefing, or when the weekly/daily cron fires. Searches BleepingComputer, The Hacker News, Dark Web Informer, and Kevin Beaumont's posts."
metadata:
  {
    "openclaw":
      {
        "emoji": "🔐",
        "slash":
          [
            {
              "name": "security-bulletin",
              "description": "Generate a cybersecurity news bulletin. Optionally pass hours (24 or 72).",
            },
          ],
      },
  }
---

# Security Bulletin Skill

Generate a curated bulletin of the top cybersecurity stories from the last N hours and deliver it as a single message.

## Parameters

- `hours` — lookback window. Default: `24`. Use `72` for Monday (covering the weekend).
- `count` — number of stories. Default: `8`.

## Steps (follow in order)

### 1. Search each source

In addition to the web‑search sources, also fetch the **GCVE Known‑Exploited‑Vulnerabilities RSS** feed (`https://db.gcve.eu/known-exploited-vulnerabilities.rss`). Parse its `<item>` entries, keep those whose `<pubDate>` falls within the look‑back window (`hours`). Treat each matching entry as a story with:
- **Title** = the `<title>` value (usually a CVE identifier and brief description)
- **Summary** = the `<description>` content
- **Link** = the `<link>` URL

These RSS entries should be merged with the other sources before scoring and ranking.


Use the **web search tool** to query each source for recent stories. Run searches in parallel where possible.

Search queries (substitute `hours` as appropriate):

| Source | Query |
|--------|-------|
| BleepingComputer | `site:bleepingcomputer.com cybersecurity news last {hours} hours` |
| The Hacker News | `site:thehackernews.com last {hours} hours` |
| Dark Web Informer | `site:darkwebinformer.com last {hours} hours` |
| Kevin Beaumont | `Kevin Beaumont security "site:doublepulsar.com OR site:infosec.exchange/@GossiTheDog"` |

Fetch the top results from each. Prioritise stories that appear across multiple sources — cross-coverage signals importance.

### 2. Score and rank

Rank by:
1. **Impact** — active exploitation, widespread affected systems, critical CVEs
2. **Novelty** — new attack techniques or zero-days
3. **Coverage** — mentioned by multiple sources
4. **Recency** — published within the `hours` window; skip older stories

Discard stories outside the time window. If fewer than `count` qualifying stories exist, deliver what is available and note the shortage.

### 3. Write the bulletin

Select up to `count` stories. Include **at most one** CVE entry; if a CVE appears, add a TLDR line with a 10‑word summary. All other entries should be regular cybersecurity news and must contain only plain text (no markdown, no asterisks):

```
📅 <date> • Title: <story title>
Summary: <5‑word summary of the article>
Link: <direct article URL>
TLDR: <10‑word CVE summary>   # only for the single CVE entry
```

Where `<date>` is the publication date in a short format (e.g., "27 Feb 2026" or "2026-02-27").

If multiple CVEs are found, pick the most critical/high‑impact one for the TLDR and treat the rest as regular news (omit TLDR). Separate each story with a blank line and do not add numbering, bullets, or extra headers.

### 4. Deliver

Wrap in a header and footer, then send as a **single message**:

```
🔐 Security Bulletin — <date> (last <hours> h)

<stories>

Sources: BleepingComputer · The Hacker News · Dark Web Informer · Kevin Beaumont
```

## Notes

- **This task is slow.** Searching and reading 8+ articles typically takes 3–8 minutes. Set `timeoutSeconds: 600` or higher on the cron job.
- **Model selection matters.** A reasoning-capable model (e.g. `openrouter/openai/gpt-oss-120b` or `openrouter/minimax/minimax-m2.1`) writes better summaries. Avoid running this on a large local Ollama model with a short cron timeout — it will time out.
- **No speculation.** Only include stories with a verifiable published URL. Do not invent summaries from partial snippets.
- **Kevin Beaumont** posts on Mastodon (`infosec.exchange/@GossiTheDog`) and his blog (`doublepulsar.com`). Check both. He often breaks enterprise security stories early.

## Cron recommendations

Two jobs cover the week cleanly:

| Job | Schedule | Window | Notes |
|-----|----------|--------|-------|
| Monday bulletin | `50 5 * * 1` UTC | 72 h | Covers Fri–Mon |
| Tue–Fri bulletin | `50 5 * * 2-5` UTC | 24 h | Daily |

Both jobs should specify:
```
model: openrouter/openai/gpt-oss-120b   # fast cloud model avoids local timeout
timeoutSeconds: 600
```
