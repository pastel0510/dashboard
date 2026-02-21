---
name: scan-secrets
description: "Scan all configured git repos for leaked secrets and API keys, report findings in chat."
metadata:
  {
    "openclaw": {
      "emoji": "🔍",
      "slash": [
        {
          "name": "scan-secrets",
          "description": "Scan all git repos for leaked secrets and API keys. Alerts sent to Telegram automatically."
        }
      ]
    }
  }
---

# Scan Secrets Skill

Run the secrets scanner across all configured repositories, report findings in this conversation.

**IMPORTANT — tool usage rules for this skill:**
- Use the **`exec` tool** to run the scanner script. Do NOT use the `cron` tool.
- Do NOT re-send Telegram alerts — the script handles Telegram automatically.
- Report the raw output and exit code to the user.
- Do NOT fabricate results. If the script errors, report the actual error.

## Step 1 — Run the scanner

Use the **`exec` tool** to run:

```
python3 /home/riverbank1229/.openclaw/secrets-scanner/scan_secrets.py --all-repos --commits 50
```

Capture stdout, stderr, and the exit code.

## Step 2 — Interpret the exit code

| Exit code | Meaning |
|-----------|---------|
| `0` | Clean — no secrets found |
| `1` | Secrets detected — Telegram alert already sent |
| `2` | Config error — check scanner output for details |

## Step 3 — Report results

Output the full scanner output verbatim, then summarize:

- **Exit 0:** "Scan complete. No secrets found across all repos."
- **Exit 1:** "Secrets detected! See findings above. A Telegram alert has already been sent."
- **Exit 2:** "Scanner encountered a config error. Output: [error details]"

## Notes

- The Telegram alert is sent by the script itself — do NOT send a second alert.
- To add a new repo to the scan, edit `/home/riverbank1229/.openclaw/secrets-scanner/config.json`.
- To suppress false positives, edit `/home/riverbank1229/.openclaw/secrets-scanner/allowlist.json`.
- To test clean notification: add `--notify-clean` to the exec command.
- Bypass pre-commit hook if needed: `git commit --no-verify` (use sparingly).
