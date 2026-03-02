# Restore Guide

Complete guide to rebuild the OpenClaw assistant from backup.

## Prerequisites

- Linux machine (tested on Fedora/RHEL)
- Git installed
- OpenClaw installed (see https://docs.openclaw.ai or clone from source)
- API keys ready (see below)

## Quick Restore

```bash
# 1. Clone the workspace backup
git clone git@gitgud.io:unreached2457/md-files.git ~/.openclaw/workspace

# 2. Clone the RSS translator (optional)
git clone git@gitgud.io:unreached2457/rss-translator.git ~/.openclaw/workspace/rss-translator

# 3. Set up config files
cd ~/.openclaw/workspace
cp config/openclaw.json.example config/openclaw.json
cp config/cron-jobs.json.example config/cron-jobs.json
```

## API Keys Required

Edit `config/openclaw.json` and replace these placeholders:

| Placeholder | Get from |
|-------------|----------|
| `YOUR_API_KEY` | https://opencode.ai (OpenCode Zen provider) |
| `YOUR_NVIDIA_API_KEY` | https://build.nvidia.com |
| `YOUR_BRAVE_API_KEY` | https://brave.com/search/api/ |
| `YOUR_TELEGRAM_BOT_TOKEN` | Talk to @BotFather on Telegram |
| `YOUR_GATEWAY_TOKEN` | Generate a secure random token |
| `YOUR_CHAT_ID` | Message @userinfobot on Telegram |

## Cron Jobs Setup

Edit `config/cron-jobs.json` and replace:
- All `YOUR_CHAT_ID` → your actual Telegram chat ID (numeric)

Current scheduled jobs:

| Job | Schedule | Description |
|-----|----------|-------------|
| Fingerpori comic | Daily 7:10 UTC | Today's Fingerpori comic |
| Security Bulletin | Mon 5:50 UTC (72h) | Weekly security roundup |
| Security Bulletin | Tue-Fri 5:50 UTC (24h) | Daily security news |
| CVE Bulletin | Weekdays 9:00 Helsinki | High/critical CVEs |
| Finnish News | Daily 15:00 UTC | Finnish domestic news |
| Science News | Every 2 days 15:02 UTC | Space & science news |
| xkcd | Daily 8:00 UTC | Random xkcd comic |
| ASCII Smiley | Weekdays 8:00 Helsinki | Daily smiley |
| Selfhst Weekly | Fridays 14:00 UTC | Self-hosted projects |
| Hue HomeKit Monitor | Daily 9:00 Helsinki | Check for fix |
| Self-reflection | Every 3 hours | Log mistakes to MEMORY.md |
| Daily reflection | Daily 0:00 UTC | Summarize day's reflections |
| Push md files | Every 6 hours | Backup to git |
| RSS Translator | Hourly | Translate RSS feeds |
| OpenClaw update | Daily 4:00 UTC | Check for updates |

## Skills Reference

All skills are in `skills/` directory:

| Skill | Trigger | Description |
|-------|---------|-------------|
| `ascii-smiley` | `/smiley` | Random ASCII smiley |
| `cve-bulletin` | `/cve-bulletin` | Daily CVE bulletin |
| `cve-bulletin-automation` | Manual | Full CVE pipeline |
| `cve-summary` | `/cve-summary <CVE-ID>` | Summarize specific CVE |
| `fingerpori` | `/fingerpori` | Today's Fingerpori comic |
| `finnish-news-bulletin` | Manual | Finnish news roundup |
| `hue-homekit-monitor` | `/hue-status` | Check Hue/HomeKit fix |
| `push-md-files` | Manual | Push workspace to git |
| `science-news-bulletin` | Manual | Science/space news |
| `security-bulletin` | Manual | Security news bulletin |
| `selfhst-weekly` | `/selfhst-weekly` | Self-hosted projects |
| `test-crons` | `/test-crons` | Run all cron jobs for testing |
| `update-opencve-kb` | Manual | Update CVE knowledge base |
| `xkcd` | `/xkcd` or `/xkcd <topic>` | xkcd comics |

## Additional Setup

### RSS Translator (optional)

```bash
cd ~/.openclaw/workspace/rss-translator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Edit `feeds.yaml` to configure which feeds to translate.

### OpenCVE Knowledge Base (for CVE skills)

```bash
# Download the CVE knowledge base (~500MB)
cd ~/.openclaw/workspace
# Either download from backup or run:
/openclaw update-opencve-kb
```

## Verification

After restore, verify everything works:

1. **Check OpenClaw status:**
   ```bash
   openclaw status
   ```

2. **Test a skill:**
   ```
   /smiley
   ```

3. **Test cron jobs:**
   ```
   /test-crons
   ```

4. **Check memory loaded:**
   ```
   What do you remember about my preferences?
   ```

## Troubleshooting

### "Model not found" errors
- Verify API keys in `config/openclaw.json`
- Check model IDs match provider's available models

### Cron jobs not running
- Verify chat ID is numeric (not a string like "@username")
- Check `openclaw status` shows gateway is running

### Skills not loading
- Ensure `skills/` folder exists in workspace
- Check SKILL.md files are present

### Telegram not responding
- Verify bot token is correct
- Check you've started a conversation with the bot
- Ensure your chat ID is in `allowFrom` list

## Backup Locations

| Repo | Contents |
|------|----------|
| `git@gitgud.io:unreached2457/md-files.git` | Workspace, skills, config, memory |
| `git@gitgud.io:unreached2457/rss-translator.git` | RSS translator tool |

## Files Not Backed Up

These are regenerated or downloaded:
- `.venv/` - Python virtual environment (recreate with `pip install`)
- `node_modules/` - npm packages (reinstall if needed)
- `opencve-kb.zip` - CVE database (download via `/update-opencve-kb`)
- `fingerpori_today*.jpeg` - Temporary comic images
- `.openclaw/` - OpenClaw internal state

---

**Last updated:** 2026-02-21
