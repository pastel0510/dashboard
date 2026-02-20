# MD Files

Automated backup of OpenClaw workspace markdown files.

## Contents

- `AGENTS.md` - Agent workspace instructions
- `SOUL.md` - Agent persona
- `USER.md` - User profile
- `MEMORY.md` - Long-term memory
- `HEARTBEAT.md` - Periodic task checks
- `TOOLS.md` - Local tool notes
- `IDENTITY.md` - Agent identity
- `memory/` - Daily memory logs

## Skills

Custom OpenClaw skills in `skills/`:

- `ascii-smiley` - Generate random ASCII smiley faces
- `cve-bulletin` - Generate CVE bulletin from recent vulnerabilities
- `cve-bulletin-automation` - Full CVE bulletin pipeline automation
- `cve-summary` - Summarize specific CVEs
- `fingerpori` - Fetch daily Fingerpori comic
- `finnish-news-bulletin` - Finnish news roundup
- `hue-homekit-monitor` - Monitor Hue + HomeKit connectivity issues
- `push-md-files` - Push md files to this repo
- `science-news-bulletin` - Science and space news roundup
- `security-bulletin` - Cybersecurity news roundup
- `selfhst-weekly` - Self-hosted projects weekly summary
- `test-crons` - Test all cron jobs
- `update-opencve-kb` - Update local OpenCVE-KB repo
- `xkcd` - Fetch xkcd comics

## Config (Sanitized)

- `config/openclaw.json.example` — API keys replaced with placeholders
- `config/cron-jobs.json.example` — Cron job templates (chat ID placeholder)

To restore: copy examples to `~/.openclaw/`, remove `.example`, fill in your keys.

## Auto-sync

Files are automatically committed and pushed every 6 hours via OpenClaw cron.
