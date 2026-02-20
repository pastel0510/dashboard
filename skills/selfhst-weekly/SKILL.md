---
name: selfhst-weekly
description: "Fetch selfh.st weekly newsletter and summarise 10 new/updated self-hosted projects."
metadata:
  {
    "openclaw": {
      "emoji": "🔧",
      "slash": [{"name": "selfhst-weekly", "description": "Self-Host Weekly — 10 new projects"}]
    }
  }
---

# Self-Host Weekly Skill

Fetch the latest selfh.st weekly edition and extract up to 10 self-hosted projects with their links.

## STRICT RULES

- **ONLY report projects and links that are literally present in the fetched page.** Do not add, invent, or extrapolate any project names, descriptions, or URLs from your training data.
- **Every project MUST include its URL.** If you cannot find the URL for a project on the page, skip it.
- If you cannot find 10 projects on the page, list however many you find — do not pad with invented ones.
- Do not include general news, drama, opinion pieces, YouTube videos, or non-software links. Projects and tools only.

## Steps

1. Fetch the RSS feed to find the latest edition URL:
   `web_fetch https://selfh.st/rss/`
   Parse the first `<link>` item inside an `<item>` block to get the latest weekly post URL (format: `https://selfh.st/weekly/YYYY-MM-DD/`)

2. Fetch the full article page:
   `web_fetch <latest-weekly-url>`

3. The fetched page contains project entries displayed as **bookmark cards**. In the markdown output, these appear as hyperlinks in the form `[Project Name](https://project-url)` or as linked titles with short descriptions. Look specifically in sections labelled **"New"**, **"Updated"**, or any project/tool listing section.

   For each project card found, extract:
   - **Project name** — the linked title text
   - **One-line description** — the short description text shown below the title on the card (from the page, verbatim or lightly trimmed)
   - **Project URL** — the actual href link from the bookmark card (not selfh.st's own URL)
   - **Why it's featured** — the context or reason it appears in the newsletter (e.g., new release, major update, new feature, etc.)

4. Select up to 10 projects, prioritising NEW ones over updated ones.

## Output Format

Send to Telegram chat ID 55163462. **Use EXACTLY two blank lines (two empty lines) between each numbered entry.** This is required for readability.

```
🔧 Self-Host Weekly — [date from page]

[N] Projects to Check Out:

1. **[Project Name]** — [one-line description from page]
[project URL]
_Why: [reason it's featured]_


2. **[Project Name]** — [one-line description]
[URL]
_Why: [reason]_


3. **[Project Name]** — [one-line description]
[URL]
_Why: [reason]_


[...up to 10]


Read more: [weekly article URL]
```

Rules:
- Two blank lines between every entry (as shown above)
- No headlines, no drama, no YouTube links
- Every entry MUST have a URL
- Projects and tools only
