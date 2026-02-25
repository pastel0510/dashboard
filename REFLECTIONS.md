## 2026-02-25 06:20 UTC
- **Gateway was dead:** Auto-update to 2026.2.24 started at 04:00 UTC, stopped the gateway, but the cron agent running the update script died with the gateway before it could complete. Manually ran `update-openclaw.sh` — updated to v2026.2.24 and restarted gateway (PID 289307).
- **Mass rate-limit cascade fixed:** All 14 cron jobs were using `opencode-zen/glm-5-free` which hit rate limits every hour overnight (`"No available auth profile for opencode (all in cooldown or unavailable)"`). Switched all jobs to `kilocode/z-ai/glm-5:free`.
- **Hue monitor errors:** 4 consecutive failures with malformed web search query containing number `2071223010` (model artifact). Should resolve after model switch to kilocode.

## 2026-02-24 07:24 UTC
- **Delivery failure recovered:** `kilocode/z-ai/glm-5:free` returned `stopReason: "error"` after exec tool successfully returned smiley `(─‿‿─)`. The response was generated but never sent to the user. Smiley delivered manually via Telegram Bot API. Recovery pattern documented in MEMORY.md under "Model Error Recovery (stopReason: error)" so self-reflection cron can detect and recover from future occurrences.

## 2026-02-22 00:03 UTC
- **Security issue RESOLVED:** Hardcoded API keys in `rss-translator/translate_feeds.py` were fixed in commit 2dcde47. Keys now load from `.env` file via environment variables. `.env` added to `.gitignore`. User should still rotate the previously exposed keys.

## 2026-02-21 18:03 UTC
- **Formatting mistake:** Bulletin skills used markdown formatting (`**bold**`, `_italic_`) which Telegram doesn't render in plain text messages. Fixed in commit 85568f4 by switching to plain text field names. Affected: Finnish, Science, Security, and Self-Host Weekly bulletin skills.

## 2026-02-21 09:04 UTC
- **File corruption detected:** REFLECTIONS.md was completely overwritten with a heartbeat poll message instead of reflection log content. The entire history was lost. This appears to be a mistake in another process/cron job writing the wrong content to the wrong file. File restored from MEMORY.md backup.

## 2026-02-21 06:03 UTC
- **Security Issue Found:** Hardcoded API keys in `rss-translator/translate_feeds.py` — NVIDIA and OpenCode API keys are embedded directly in source code that's pushed to a git repository. This is a security risk. Should use environment variables or a config file excluded from git. User should rotate these keys.

## 2026-02-19 12:03 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-19 13:33 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-19 13:35 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-19 13:36 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-19 15:03 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-19 18:03 UTC
- Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## 2026-02-20 18:45 UTC
- Unanswered question detected:
  - [2026-02-20T18:45:12.200Z] "get me todays finnish news bulletin"

## 2026-02-21 20:45 UTC
- Unanswered message detected (appears to be a heartbeat poll):
  - [2026-02-21T20:45:17.002Z] Conversation info (untrusted metadata) - heartbeat poll not responded to

## 2026-02-23 06:00 UTC
- Unanswered message detected (appears to be Telegram metadata/false positive):
  - [2026-02-23T06:00:07.767Z] Conversation info (untrusted metadata) - likely false positive, just message context

## 2026-02-23 21:04 UTC
- Unanswered message detected (appears to be system metadata/false positive):
  - [2026-02-23T21:04:10.237Z] Queued announce messages while agent was busy - likely false positive, just system queue status
