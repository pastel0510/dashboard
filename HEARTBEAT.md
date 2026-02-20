# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Cloudflare Status Monitoring
Check https://www.cloudflarestatus.com/ periodically and notify Shadow when current issues are resolved.

Active issues to track:
- BYOIP prefixes impact (mitigated, restoring)
- 1.1.1.1 landing page 403 errors (fix implemented, monitoring)
- Bot Management / JSD detections (fix in progress since Feb 18)
- Higher 429 errors (fix in progress since Feb 18)

Notify when these show "Operational" or "Resolved".
