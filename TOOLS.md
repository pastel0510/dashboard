# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Telegram

- **Primary chat ID: `55163462`** — this is Shadow's personal Telegram chat. Use this as the `target` whenever you need to send a message, photo, or file via the `message` tool. Never use `"telegram"` as the target — it must be the numeric chat ID.

---

## Gateway / OpenClaw Process

**NEVER restart, kill, or stop the OpenClaw gateway process yourself.** Do not run `pkill`, `kill`, `SIGTERM`, or any command targeting the gateway or openclaw processes. Do not run `start-openclaw.sh` or `openclaw gateway` commands. Gateway management is handled externally — if it seems unresponsive, report it to the user and wait. Attempting to restart it from within a session will kill the gateway and cause an outage.

---

Add whatever helps you do your job. This is your cheat sheet.
