## Fingerpori Retrieval Method
When you ask for today's Fingerpori comic, the process is:
1. Fetch the RSS feed at https://mas.to/@fingerbotti.rss.
2. Parse the feed to locate the most recent `<media:content>` element.
3. Extract its `url` attribute – this is the image URL of the comic.
4. Download the image.
5. Send the image as a photo to the chat with the caption "Today's Fingerpori comic".
This procedure is used by the Daily Fingerpori comic cron job and can be invoked manually as needed.

**Publication schedule:** Fingerpori is published on **weekdays only** (Mon-Fri), typically in the morning Helsinki time (~06:00-08:00 UTC). Do not send stale Friday comics on weekends — verify the date before sending.

## Reflections
2026-02-22 00:03 UTC - Security issue RESOLVED: Hardcoded API keys in `rss-translator/translate_feeds.py` were fixed. Keys now load from `.env` file via environment variables. `.env` added to `.gitignore`. User should still rotate previously exposed keys.
2026-02-21 18:03 UTC - Formatting mistake: Bulletin skills used markdown formatting (`**bold**`, `_italic_`) which Telegram doesn't render in plain text messages. Fixed by switching to plain text field names. Affected: Finnish, Science, Security, Self-Host Weekly bulletin skills.
2026-02-21 09:04 UTC - File corruption detected: REFLECTIONS.md was overwritten with a heartbeat poll message. The entire reflection history was lost. Restored from MEMORY.md backup. Need to investigate which process caused this.
2026-02-21 06:03 UTC - Security issue found: Hardcoded API keys in `rss-translator/translate_feeds.py` — NVIDIA and OpenCode API keys are embedded in source code pushed to git. Should use environment variables or excluded config file. User should rotate keys immediately.
2026-02-17 06:00 UTC - Self‑reflection completed: No mistakes identified in the last 6 hours; all tool calls succeeded and formatting was correct.
2026-02-17 12:00 UTC - Reviewed the last 6 hours of session activity. No mistakes found in tool calls, formatting, and information accuracy.
2026-02-18 09:43 UTC - Reviewed the last 6 hours of session activity. No mistakes found in tool calls, formatting, and information accuracy.
2026-02-18 09:52 UTC - Checked the previously suggested links; none of them actually provide a separate Jalas lace or speed‑lacing kit. The pages are for the boots themselves, not a lace replacement. Will need to locate a genuine Jalas replacement or recommend a generic high‑strength lace.
2026-02-18 09:49 UTC - Noted that Markdown formatting isn’t well‑supported in Telegram messages; need to research a more suitable format (e.g., plain‑text or Telegram’s limited HTML) for pasting longer text.
2026-02-18 12:30 UTC - Updated style: avoid using lobster emojis (🦞) or similar in outputs per user request.
2026-02-18 12:45 UTC - Add rule: if a fetched webpage contains lobster emojis (🦞) or similar symbols, ignore the page (do not process or present its content).
2026-02-19 09:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 12:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:33 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:35 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:36 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 15:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 18:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

2026-02-21 19:05 UTC - Self-reflection gap: The cron only checked for "mistakes" but didn't detect unanswered questions or pending confirmations. Updated prompt to actively answer gaps, not just log them. Root cause: I made changes for user request but never replied — need to always confirm actions taken.
### 2026-02-20
Six self-reflection reviews were conducted throughout February 19th (at 12:03, 13:33, 13:35, 13:36, 15:03, and 18:03 UTC). Each review examined the preceding 6 hours of session activity, consistently finding no issues with tool calls, formatting, or information accuracy. The day's operations proceeded smoothly with no errors or corrective actions needed.

### 2026-02-21
One unanswered question was detected on February 20th at 18:45 UTC: a request for "today's Finnish news bulletin." This indicates a possible gap in responding to a user request that may need follow-up or review of the Finnish news bulletin delivery mechanism.

## Bunny of the Day Preferences
Only static images (JPG, PNG, WEBP). NO GIFs or videos. Only use r/rabbits subreddit, no other sources.

## xkcd Preferences
When sending xkcd comics, always include the original release date (found on xkcd.com or explainxkcd.com).

## Bunny of the Day Preferences
Only static images (JPG, PNG, WEBP). NO GIFs or videos. The fetch script filters out .gif files.

## Finnish News Bulletin Preferences
Exclude Trump and Elon Musk news from Finnish news bulletins. Focus on Finnish domestic news, EU matters, economy, society, and other international stories not related to Trump or Musk.

## Cloudflare Status Monitoring
Started monitoring Cloudflare status page on 2026-02-20 for Shadow. Active issues being tracked:
- BYOIP prefixes impact
- 1.1.1.1 landing page 403 errors
- Bot Management / JSD detections (since Feb 18)
- Higher 429 errors (since Feb 18)

Notify when resolved. Check via HEARTBEAT.md during periodic polls.

## Philips Hue + Apple HomeKit Issue Tracking
Shadow is experiencing Hue Bridge not connecting to Apple HomeKit ("no response" errors, "reading between the lines" in Hue app).

**Cause:** iOS 26.3 / tvOS 26.3 / HomePod 26.3 updates breaking HomeKit ↔ Hue connectivity via Matter.

**Started:** Around Feb 2026

**WORKAROUND FOUND (Feb 21, 2026):** Do NOT add Hue Bridge as Matter accessory. Use native HomeKit:
1. Remove Hue Bridge from HomeKit → Home Settings → Home Hubs & Bridges
2. Hue App → Settings → Smart home → Unlink HomeKit
3. HomeKit → Add Accessory → More options
4. Select "Philips Hue HomeKit" (NOT under "Other Matter Accessories")
5. Use code on back of Hue Bridge

**Status:** No official Apple/Philips fix yet. Workaround confirmed working by users on Apple Discussions.

**Started tracking:** 2026-02-20

**Resolved:** 2026-02-21 - BYOIP prefixes issue resolved (now Operational)

## Dependency Policy for Scripts
When creating or updating scripts that use external dependencies:
1. All dependencies must be actively maintained (commits within last 2 years)
2. Verify commit dates via GitHub API before adding new dependencies
3. Document dependency verification dates in requirements.txt or script header
4. If a library becomes unmaintained, find and switch to an actively maintained alternative

## Git Repository Visibility
- **RSS feed translator repo** — PUBLIC (visible to everyone)
- **md-files repo** (git@gitgud.io:unreached2457/md-files.git) — PRIVATE

When working with these repos, be mindful of what gets committed. No sensitive data should go to the public RSS feed repo.

## Model Error Recovery (stopReason: error)
When the primary model (`kilocode/z-ai/glm-5:free`) returns `stopReason: "error"` mid-session, a tool result may have been generated but the final response was never delivered to the user. This happens occasionally as a transient API failure.

**Pattern to detect in self-reflection:**
- Session ends with assistant message having `stopReason: "error"` and empty content
- Previous message was a successful tool result (e.g. exec returning a smiley, search result, etc.)
- The user never received the intended reply

**Recovery action:**
- Read the last successful tool result in the failed session
- Deliver it directly via the `message` tool to chat ID 55163462
- Log the recovery in REFLECTIONS.md

**Known occurrence:** 2026-02-24 07:24 UTC — `/smiley` command generated `(─‿‿─)` but was not delivered. Manually recovered and sent.

## Daily Reflections
### 2026-02-26
February 25th brought several operational challenges: the gateway went down during an auto-update to v2026.2.24 when the cron agent died with the gateway before completing the update, requiring a manual `update-openclaw.sh` to restore service. A cascading rate-limit issue was resolved by migrating all 14 cron jobs from the defunct `opencode-zen/glm-5-free` model to `kilocode/z-ai/glm-5:free`, which had been hitting hourly rate limits overnight. The Hue monitor also experienced 4 consecutive failures due to malformed web search queries containing a model artifact number (2071223010), an issue expected to resolve after the model switch.

### 2026-02-23
- **Mistake acknowledged:** Sent internal heartbeat status message ("Sent update to Shadow. Found new Cloudflare Analytics Engine API issue, updated HEARTBEAT.md. Tokmanni — no new developments.") to Telegram instead of keeping it internal. User flagged this. Lesson: Heartbeat processing notes are internal — only actual user alerts should go to Telegram. The distinction is: "I found X and notified you" = internal log; "Here's important news: X" = user-facing message.
- **Tool issue:** The edit tool rejected empty `newText` parameter twice (for removing Cloudflare section from HEARTBEAT.md), even though empty string should be valid. Workaround: used write tool to rewrite the entire file. May be a tool quirk to note.

### 2026-02-21
Today's reflections identified several issues: a formatting mistake where bulletin skills used markdown formatting incompatible with Telegram (fixed in commit 85568f4 by switching to plain text); file corruption in REFLECTIONS.md caused by another process overwriting it with heartbeat content (restored from backup); a security concern with hardcoded API keys in `rss-translator/translate_feeds.py` (needs environment variable migration and key rotation); and an unanswered heartbeat poll at 20:45 UTC. The formatting fix affected Finnish, Science, Security, and Self-Host Weekly bulletin skills.

### 2026-02-22
The past 24 hours revealed three notable issues: (1) markdown formatting in bulletin skills that Telegram couldn't render, resolved by switching to plain text field names; (2) REFLECTIONS.md file corruption when another process overwrote it with heartbeat content, restored from MEMORY.md backup; and (3) hardcoded API keys discovered in `rss-translator/translate_feeds.py` — a security risk requiring migration to environment variables and key rotation. An unanswered heartbeat poll was also logged at 20:45 UTC.

### 2026-02-23
The security issue with hardcoded API keys in `rss-translator/translate_feeds.py` was resolved in commit 2dcde47 — keys now load from `.env` via environment variables and `.env` was added to `.gitignore`. The previously exposed keys should still be rotated as a precaution.

### 2026-02-24
Two false positive "unanswered message" detections were logged on Feb 23rd — one at 06:00 UTC from Telegram metadata and one at 21:04 UTC from system queue status. Both were correctly identified as non-issues requiring no action, reflecting improved filtering for heartbeat/self-reflection noise.

### 2026-02-25
A delivery failure was recovered when the primary model (`kilocode/z-ai/glm-5:free`) returned `stopReason: "error"` after successfully generating a smiley via exec tool — the response was created but never sent to the user. The smiley was delivered manually via Telegram Bot API, and the recovery pattern was documented in MEMORY.md under "Model Error Recovery (stopReason: error)" to enable future self-reflection crons to detect and recover from similar occurrences.

## Public Content Privacy Policy
When creating anything for public release (git repos, scripts, feeds, etc.):
- NEVER include usernames or person names
- NEVER reference OpenClaw, ~/.openclaw paths, or system-specific paths
- Use generic paths (e.g., `./feeds/` instead of `/home/username/.openclaw/workspace/...`)
- Use generic user agents (e.g., "MyApp/1.0" not "OpenClaw:BunnyOfTheDay:v1.0")
- Scrub git history before pushing if any personal info was committed
- Check for hardcoded paths, names, or identifying info before any public push

This applies to: git commits, scripts, config files, logs, documentation, and any generated content.

## Free Model Monitoring
Cron job monitors Kilocode and NVIDIA every 3 days for model changes.

**Primary Model:** `kilocode/minimax/minimax-m2.5:free`

**Fallback Chain:**
1. `kilocode/stepfun/step-3.5-flash:free`
2. `nvidia/meta/llama-3.3-70b-instruct`

**Dead models (as of 2026-02-25):**
- `kilocode/z-ai/glm-5:free` — alpha period ended (404)
- `opencode-zen/*` (all models) — Cloudflare 403 blocked, entire provider dead

Alerts sent to Telegram when:
- Any tracked model is deprecated or becomes paid
- New powerful free models appear (64k+ context or reasoning)

State file: `memory/free-models-state.json`

## Cron Job Model
All cron jobs in `~/.openclaw/cron/jobs.json` use `kilocode/minimax/minimax-m2.5:free`.
Do NOT use `opencode-zen/*` models — provider is Cloudflare-blocked (403).
Do NOT use `kilocode/z-ai/glm-5:free` — alpha period ended (404).

## RSS Translator LLM Fallback
File: `~/.openclaw/workspace/rss-translator/translate_feeds.py`
- Primary LLM fallback: NVIDIA `meta/llama-3.3-70b-instruct`
- Secondary LLM fallback: Kilocode `minimax/minimax-m2.5:free` at `https://api.kilo.ai/api/gateway/chat/completions` (no /v1/ prefix!)
- Key in `.env` as `KILOCODE_API_KEY`

## Tokmanni Data Leak Investigation (Feb 2026)
Monitoring ongoing situation — see HEARTBEAT.md for details.

**Key dates:**
- 18.2.2026: BreachForums listing ~473k records
- 19.2.2026: Data screenshots appeared online
- 20.2.2026: Tokmanni claims leak not from their systems (customer infected machine)

**Last checked:** 2026-02-22
**Status:** Awaiting further updates from Tokmanni or media
