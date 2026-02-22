#!/bin/bash
# Free Model Monitor - Check for new/deprecated free models
# Run via cron every 2-3 days

set -euo pipefail

WORKSPACE="$HOME/.openclaw/workspace"
STATE_FILE="$WORKSPACE/memory/free-models-state.json"
CONFIG_FILE="$HOME/.openclaw/openclaw.json"
LOG_FILE="$WORKSPACE/logs/free-model-monitor.log"

mkdir -p "$(dirname "$STATE_FILE")" "$(dirname "$LOG_FILE")"

log() {
    echo "[$(date -Iseconds)] $1" >> "$LOG_FILE"
}

# Load current models from OpenClaw config
get_current_models() {
    jq -r '.models.providers | to_entries[] | 
        select(.key == "opencode-zen" or .key == "kilocode" or .key == "nvidia" or .key == "openrouter") |
        {provider: .key, models: [.value.models[].id]} | 
        "\(.provider)|\(.models | join(","))"' "$CONFIG_FILE" 2>/dev/null || echo ""
}

# Check OpenRouter for free models
check_openrouter_free() {
    curl -s "https://openrouter.ai/api/v1/models" 2>/dev/null | \
        jq -r '.data[] | select(.pricing.prompt == "0" and .pricing.completion == "0") | .id' | \
        sort -u || echo ""
}

# Check NVIDIA NIM for free models
check_nvidia_free() {
    local nvidia_key
    nvidia_key=$(jq -r '.models.providers.nvidia.apiKey // empty' "$CONFIG_FILE" 2>/dev/null)
    if [[ -n "$nvidia_key" && "$nvidia_key" != "null" && "$nvidia_key" != "__OPENCLAW_REDACTED__" ]]; then
        curl -s "https://integrate.api.nvidia.com/v1/models" \
            -H "Authorization: Bearer $nvidia_key" 2>/dev/null | \
            jq -r '.data[].id' 2>/dev/null || echo ""
    else
        # Fallback: check NVIDIA's public model list
        curl -s "https://build.nvidia.com/explore/discover/models" 2>/dev/null | \
            grep -oP 'model-id="[^"]+"' | cut -d'"' -f2 || echo ""
    fi
}

# Load previous state
load_state() {
    if [[ -f "$STATE_FILE" ]]; then
        cat "$STATE_FILE"
    else
        echo '{"lastChecked": null, "providers": {}}'
    fi
}

# Save current state
save_state() {
    local state="$1"
    echo "$state" > "$STATE_FILE"
}

# Main check
main() {
    log "Starting free model check..."
    
    local current_state
    current_state=$(load_state)
    
    local new_models=()
    local deprecated_models=()
    local changed_models=()
    
    # Check OpenRouter
    log "Checking OpenRouter..."
    local openrouter_free
    openrouter_free=$(check_openrouter_free)
    
    # Get models currently configured in OpenRouter
    local current_openrouter
    current_openrouter=$(jq -r '.models.providers.openrouter.models[].id // empty' "$CONFIG_FILE" 2>/dev/null | sort -u)
    
    # Compare - find new free models on OpenRouter not in config
    while IFS= read -r model; do
        if [[ -n "$model" && ! "$current_openrouter" =~ "$model" ]]; then
            # Check if this is a potentially interesting model
            local model_info
            model_info=$(curl -s "https://openrouter.ai/api/v1/models" 2>/dev/null | \
                jq -r ".data[] | select(.id == \"$model\") | {name: .name, context: .context_length}" 2>/dev/null)
            if [[ -n "$model_info" ]]; then
                new_models+=("openrouter/$model|$model_info")
            fi
        fi
    done <<< "$openrouter_free"
    
    # Build report
    local report=""
    local has_changes=false
    
    if [[ ${#new_models[@]} -gt 0 ]]; then
        has_changes=true
        report+="\n🆓 NEW FREE MODELS DETECTED:\n"
        for entry in "${new_models[@]}"; do
            local model_name="${entry%%|*}"
            local model_info="${entry#*|}"
            report+="  • $model_name\n    $model_info\n"
        done
    fi
    
    if [[ ${#deprecated_models[@]} -gt 0 ]]; then
        has_changes=true
        report+="\n⚠️ DEPRECATED MODELS:\n"
        for model in "${deprecated_models[@]}"; do
            report+="  • $model\n"
        done
    fi
    
    if [[ ${#changed_models[@]} -gt 0 ]]; then
        has_changes=true
        report+="\n💰 MODELS NOW PAID:\n"
        for entry in "${changed_models[@]}"; do
            report+="  • $entry\n"
        done
    fi
    
    # Update state
    local new_state
    new_state=$(jq -n \
        --arg checked "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        --arg openrouter "$openrouter_free" \
        '{"lastChecked": $checked, "openrouterFree": ($openrouter | split("\n"))}')
    save_state "$new_state"
    
    # Output report if changes detected
    if [[ "$has_changes" == "true" ]]; then
        echo -e "$report"
        log "Changes detected, report generated."
    else
        log "No changes detected."
        echo "NO_CHANGES"
    fi
}

main "$@"
