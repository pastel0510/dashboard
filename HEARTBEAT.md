# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Cloudflare Status Monitoring
Check https://www.cloudflarestatus.com/ periodically and notify Shadow when current issues are resolved.

Active issues to track:
- Data Loss Prevention (DLP) (Degraded Performance, Newark NJ latency — last update Feb 21, 09:57 UTC, still working on fix. No new updates since then)

Resolved:
- Bot Management / JSD detections — RESOLVED Feb 21, 10:13 UTC
- Workers AI — RESOLVED (now Operational)
- 1.1.1.1 landing page 403 errors — RESOLVED Feb 20, 22:23 UTC
- BYOIP prefixes impact — RESOLVED Feb 21, 00:27 UTC
- Higher 429 errors — RESOLVED (fix implemented Feb 19, monitoring completed)

Notify when remaining issues show "Operational" or "Resolved".
