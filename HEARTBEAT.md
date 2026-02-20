# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Cloudflare Status Monitoring
Check https://www.cloudflarestatus.com/ periodically and notify Shadow when current issues are resolved.

Active issues to track:
- BYOIP prefixes impact (still restoring as of Feb 20 20:50 UTC)
- 1.1.1.1 landing page 403 errors (fix implemented, monitoring)
- Bot Management / JSD detections (still investigating, JSD disabled since Feb 18)
- Higher 429 errors (fix implemented, monitoring)

Notify when these show "Operational" or "Resolved".
