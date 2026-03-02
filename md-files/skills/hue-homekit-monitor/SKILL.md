---
name: hue-homekit-monitor
description: "Monitor Philips Hue + Apple HomeKit connectivity issue and alert when a fix is released."
metadata:
  {
    "openclaw": {
      "emoji": "💡",
      "slash": [{"name": "hue-status", "description": "Check Philips Hue HomeKit fix status"}]
    }
  }
---

# Philips Hue HomeKit Monitor

Track the ongoing Philips Hue ↔ Apple HomeKit "no response" / Matter connectivity issue and notify when a fix is available.

## Background

Since ~February 2026, iOS/HomePod updates broke Hue Bridge → HomeKit connections. User cannot re-add Philips Hue to Apple Home until this is fixed.

## Process

1. Search for recent updates on the issue:
   - web_search: `Philips Hue Apple HomeKit fix update 2026`
   - web_search: `Philips Hue Matter HomeKit "no response" resolved`
   - web_fetch: https://hueblog.com (check for fix announcements)

2. Check if a fix has been released by either Apple (iOS update) or Philips (Hue app/firmware update)

3. Compare against known broken state (as of Feb 20, 2026: iOS 26.3 / HomePod 26.3 breaking Matter/Hue connections)

## Output

- **If NO fix yet:** Output nothing (stay silent — do NOT send a message)
- **If FIX found:** Send Telegram message to 55163462:

```
💡 Philips Hue HomeKit Fix Available!

[Description of what was fixed and which update contains the fix]

You can now re-add your Philips Hue to Apple Home.

Source: [link]
```

## Notes

- Only alert when there is a confirmed fix — do not send "still broken" updates
- Check Apple release notes and Philips Hue blog/changelog
- If unsure, stay silent
