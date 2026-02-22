---
name: free-model-monitor
description: "Monitor free model offerings from OpenCode, Kilocode, and NVIDIA. Alert when new powerful free models appear or when existing free models are being deprecated."
metadata:
  openclaw:
    emoji: "🆓"
---

# Free Model Monitor

Monitor Shadow's CRITICAL model infrastructure for deprecation and new opportunities.

## Tracked Models (ALERT ON ANY CHANGE)

**Primary Model:** `kilocode/z-ai/glm-5:free` — MUST monitor closely

**Fallback Chain (in order):**
1. `opencode-zen/glm-5-free`
2. `nvidia/meta/llama-3.3-70b-instruct`
3. `opencode-zen/minimax-m2.5-free`
4. `kilocode/minimax/minimax-m2.5:free`
5. `opencode-zen/kimi-k2.5-free`

## Providers to Monitor

### OpenCode-Zen (opencode.ai/zen)
Models: glm-5-free, minimax-m2.5-free, kimi-k2.5-free, trinity-large-preview-free

### Kilocode (api.kilo.ai)
Models: stepfun/step-3.5-flash:free, minimax/minimax-m2.5:free, z-ai/glm-5:free

### NVIDIA (integrate.api.nvidia.com)
Models: meta/llama-3.3-70b-instruct, nvidia/llama-3.3-nemotron-super-49b-v1

### OpenRouter (for new models)
Free tier models worth tracking

## How to Run

```bash
# Check OpenRouter for all free models
curl -s "https://openrouter.ai/api/v1/models" | jq -r '.data[] | select(.pricing.prompt == "0") | "\(.id)"' | sort

# Check NVIDIA NIM API
curl -s "https://integrate.api.nvidia.com/v1/models" -H "Authorization: Bearer $NVIDIA_API_KEY" | jq '.data[].id'
```

## Detection Logic

1. Load current free models from config (~/.openclaw/openclaw.json)
2. Fetch latest model lists from each provider
3. Compare:
   - **NEW**: Models not in current config but now available for free
   - **DEPRECATED**: Models in current config but no longer available
   - **CHANGED**: Models that switched from free to paid

## Alert Format

```
🆓 FREE MODEL UPDATE

NEW MODELS:
- provider/model-name: Description (context: 128k, reasoning: yes/no)

DEPRECATED:
- provider/model-name: No longer available

CHANGED:
- provider/model-name: Now requires payment ($X/input, $Y/output)
```

## Storage

Store last-seen model list in: `~/.openclaw/workspace/memory/free-models-state.json`

```json
{
  "lastChecked": "2026-02-21T23:00:00Z",
  "providers": {
    "opencode-zen": ["glm-5-free", "minimax-m2.5-free", ...],
    "kilocode": ["stepfun/step-3.5-flash:free", ...],
    "nvidia": ["meta/llama-3.3-70b-instruct", ...],
    "openrouter": ["arcee-ai/trinity-large-preview:free", ...]
  }
}
```

## Notes

- Run every 2-3 days via cron
- Only notify when there are actual changes
- Focus on powerful models (context > 32k, or reasoning capability)
- Ignore tiny models (< 7B params unless they have special capabilities)
