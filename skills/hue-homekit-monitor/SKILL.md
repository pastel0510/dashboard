---
name: hue-homekit-monitor
description: "Monitor Philips Hue + Apple HomeKit connectivity issue and alert when a fix is officially released."
metadata:
  {
    "openclaw": {
      "emoji": "💡",
      "slash": [{"name": "hue-status", "description": "Check Philips Hue HomeKit fix status"}]
    }
  }
---

# Philips Hue HomeKit Monitor

Track the ongoing Philips Hue ↔ Apple HomeKit connectivity issue and notify when a fix is officially available.

## Background

Since ~February 2026, iOS/HomePod updates broke Hue Bridge → HomeKit connections via Matter. Users cannot re-add Philips Hue to Apple Home until this is fixed.

## Known Broken State (as of Feb 2026)
- iOS ~18.x (current version)
- HomePod software ~18.x
- Hue Bridge Pro not responding in Apple Home
- Matter protocol issues

## Process

1. Search for official fix announcements:
   - Apple Security Releases: https://support.apple.com/en-us/HT201222
   - Philips Hue blog: https://www.philips-hue.com/support/en/explore/topics/ firmware-update
   - r/Hue on Reddit (check comments, not just title)

2. **VERIFICATION REQUIRED** before alerting:
   - Must be from OFFICIAL Apple or Philips source, OR
   - Must have MULTIPLE independent Reddit comments confirming the fix works
   - Check if top comments say "still broken" or "not fixed" — if so, DO NOT alert
   - iOS version numbers in 26.x are LIKELY ERRORS (current iOS is ~18.x)

3. Compare against known broken state

## Output

- **If NO confirmed fix:** Output nothing (stay silent — do NOT send a message)
- **If FIX confirmed:** Send Telegram message to 55163462:

```
💡 Philips Hue HomeKit Fix Available!

[Description of what was fixed and which update contains the fix]

You can now re-add your Philips Hue to Apple Home.

Source: [link]
```

## Notes

- Only alert when there is a confirmed fix — do not send "still broken" updates
- Be skeptical of Reddit posts claiming fixes — check comment sections
- iOS 26.x version numbers are almost certainly errors (current iOS is ~18.x)
- If unsure, stay silent
- Better to miss a real fix than to send a false alarm
