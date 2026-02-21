# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Cloudflare Status Monitoring
Check https://www.cloudflarestatus.com/ periodically and notify Shadow when current issues are resolved.

Active issues to track:
- Bot Management / JSD detections (Degraded Performance, JSD disabled since Feb 18, fix in progress)
- Higher 429 errors (fix implemented, monitoring as of Feb 20 16:26 UTC)
- Data Loss Prevention (DLP) (Degraded Performance, Newark NJ latency)

Resolved:
- 1.1.1.1 landing page 403 errors — RESOLVED Feb 20, 22:23 UTC
- BYOIP prefixes impact — RESOLVED Feb 21, 00:27 UTC

Notify when remaining issues show "Operational" or "Resolved".
