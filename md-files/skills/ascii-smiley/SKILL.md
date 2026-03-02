---
name: ascii-smiley
description: "Generate a random happy ASCII art smiley face. Use when the daily cron fires or when asked."
metadata:
  {
    "openclaw":
      {
        "emoji": "😊",
        "slash":
          [
            {
              "name": "smiley",
              "description": "Generate a random happy ASCII smiley",
            },
          ],
      },
  }
---

# ASCII Smiley Skill

Generate a random happy ASCII art smiley face and send it.

## Smiley Options

Use Python or shell to randomly pick one from this list:

```
\( ^_^ )/
<(^v^)>
(^_^)
(◕‿◕)
(◕ᴗ◕)
(◠‿◠)
(◡‿◡)
ヽ(^‿^)ノ
╰(◕‿◕)╯
(⌒‿⌒)
(´｡• ᵕ •｡`)
(≧◡≦)
(˶‿˶)
(ᵔ◡ᵔ)
ヽ(•‿•)ノ
(─‿‿─)
(¬‿¬)
(≧ᴗ≦)
(⌐■_■)
(☞ﾟヮﾟ)☞
☜(ﾟヮﾟ☜)
ヽ(⌐■_■)ノ♪
(｡◕‿◕｡)
(*^‿^*)
(◠ᴗ◠)
(◕ᴗ◕✿)
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
(◠‿・)—☆
ヽ(⌒‿⌒)ノ
(´• ω •`)
(◕‿↼)
(｡･ω･｡)
(◠‿◠✿)
```

## Steps

1. Use Python to randomly select one smiley. Write a small Python script to a temp file and run it:

```
python3 /tmp/pick_smiley.py
```

Where `/tmp/pick_smiley.py` contains:
```python
import random
smileys = [r"\( ^_^ )/","<(^v^)>","(^_^)","(◕‿◕)","(◕ᴗ◕)","(◠‿◠)","(◡‿◡)","ヽ(^‿^)ノ","╰(◕‿◕)╯","(⌒‿⌒)","(´｡• ᵕ •｡`)","(≧◡≦)","(˶‿˶)","(ᵔ◡ᵔ)","ヽ(•‿•)ノ","(─‿‿─)","(¬‿¬)","(≧ᴗ≦)","(⌐■_■)","(☞ﾟヮﾟ)☞","☜(ﾟヮﾟ☜)","ヽ(⌐■_■)ノ♪","(｡◕‿◕｡)","(*^‿^*)","(◠ᴗ◠)","(◕ᴗ◕✿)","(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧","(◠‿・)—☆","ヽ(⌒‿⌒)ノ","(´• ω •`)","(◕‿↼)","(｡･ω･｡)","(◠‿◠✿)"]
print(random.choice(smileys))
```

2. Send the selected smiley (and ONLY the smiley) as a Telegram message to chat ID 55163462 using the message tool.

3. After the tool confirms delivery, output exactly: `NO_REPLY`

## Notes

- Do NOT output the smiley as text in your response — send it ONLY via the message tool
- No additional text, no hearts, no commentary
- One smiley per invocation
