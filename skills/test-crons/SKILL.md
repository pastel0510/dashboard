---
name: test-crons
description: "Run all enabled cron jobs sequentially for testing, wait for each to finish, reflect on results, and auto-fix any errors found."
metadata:
  {
    "openclaw": {
      "emoji": "🧪",
      "slash": [
        {
          "name": "test-crons",
          "description": "Run all enabled cron jobs in sequence, wait for each, reflect on results and auto-fix errors."
        }
      ]
    }
  }
---

# Test Cron Jobs Skill

Run every enabled cron job one at a time. Wait for each to finish before starting the next. Reflect on results and auto-fix errors.

**IMPORTANT — tool usage rules for this skill:**
- Use the **`cron` tool** to list and trigger jobs. Do NOT use `exec` or bash to interact with cron jobs — there is no `openclaw` CLI available in the sandbox.
- Use the **`read` tool** to inspect session files.
- Use the **`exec` tool only** for the session-age polling check described in Step 2c.
- Do NOT fabricate results. If a step fails, report the actual error and move on.

## Step 1 — Load the job list

Use the **`read` tool** to read `/home/riverbank1229/.openclaw/cron/jobs.json`.

From the `jobs` array, collect all entries where:
- `enabled: true`
- `payload.kind == "agentTurn"` — skip `systemEvent` jobs (they can't be tested as agent turns)

Output: `🧪 Starting cron test — N jobs queued: <name1>, <name2>, ...`

## Step 2 — Run each job in sequence

For each job in array order:

### 2a. Announce start
Output: `▶️ [K/N] <job name> (id: <first 8 chars of id>)`

### 2b. Trigger the job
Call the **`cron` tool** with the job's ID to trigger it. Example: `cron run <job-id>`.

Record the current time as `trigger_time`.

### 2c. Wait for completion

Poll every 5 seconds using **`exec`** with this command:

```
python3 -c "import os,glob,time; files=[f for f in glob.glob('/home/riverbank1229/.openclaw/agents/main/sessions/*.jsonl') if '.reset.' not in f]; newest=max(files,key=os.path.getmtime) if files else None; age=time.time()-os.path.getmtime(newest) if newest else 999; print(f'AGE={age:.1f}')"
```

Continue polling until **either**:
- `AGE` exceeds `10` seconds — the session has gone quiet, job is done
- 4 minutes have elapsed since `trigger_time` — mark as **TIMED_OUT**

Minimum wait: 8 seconds regardless of AGE (give the job time to start).

### 2d. Read the result

After the job completes, use the **`read` tool** to read the last 30 lines of the newest session JSONL file (the one just modified). Look for:
- Any `"isError": true` tool results — capture the error message
- The final assistant text content
- Any question the model asked (requests for information)

Record: `{ name, status: "ok"|"error"|"timed_out", notes: "..." }`

## Step 3 — Summary and reflection

After all jobs have run, output:

```
🧪 Test complete (N/N)

✅ <name> — ok
❌ <name> — <brief error>
⏱️ <name> — timed out
```

Then for each **failed or timed-out** job:
1. Re-read the full session JSONL to identify the root cause
2. Determine if the fix belongs in `jobs.json` (wrong message/model/config) or a `SKILL.md`
3. Apply the fix immediately with the **`edit` or `write` tool**
4. Output: `🔧 Fixed <name>: <what was changed>`

If all jobs passed: `✅ All jobs passed. No fixes needed.`

## Notes

- **Never use exec to trigger cron jobs** — use the `cron` tool directly.
- `systemEvent` jobs (e.g. water reminder) are skipped — they inject directly into sessions.
- Jobs run in their own isolated sessions; delivery messages appear in this chat as they complete.
- Environmental failures (e.g. third-party site returning 403) are noted but not "fixed" in config.
- After auto-fixing, do NOT re-run the fixed jobs — just document the change.
- The Telegram chat ID for sending messages is `55163462` (see TOOLS.md).
