## Fingerpori Retrieval Method
When you ask for today's Fingerpori comic, the process is:
1. Fetch the RSS feed at https://mas.to/@fingerbotti.rss.
2. Parse the feed to locate the most recent `<media:content>` element.
3. Extract its `url` attribute – this is the image URL of the comic.
4. Download the image.
5. Send the image as a photo to the chat with the caption "Today's Fingerpori comic".
This procedure is used by the Daily Fingerpori comic cron job and can be invoked manually as needed.

## Reflections
2026-02-17 06:00 UTC - Self‑reflection completed: No mistakes identified in the last 6 hours; all tool calls succeeded and formatting was correct.
2026-02-17 12:00 UTC - Reviewed the last 6 hours of session activity. No mistakes found in tool calls, formatting, and information accuracy.
2026-02-18 09:43 UTC - Reviewed the last 6 hours of session activity. No mistakes found in tool calls, formatting, and information accuracy.
2026-02-18 09:52 UTC - Checked the previously suggested links; none of them actually provide a separate Jalas lace or speed‑lacing kit. The pages are for the boots themselves, not a lace replacement. Will need to locate a genuine Jalas replacement or recommend a generic high‑strength lace.
2026-02-18 09:49 UTC - Noted that Markdown formatting isn’t well‑supported in Telegram messages; need to research a more suitable format (e.g., plain‑text or Telegram’s limited HTML) for pasting longer text.
2026-02-18 12:30 UTC - Updated style: avoid using lobster emojis (🦞) or similar in outputs per user request.
2026-02-18 12:45 UTC - Add rule: if a fetched webpage contains lobster emojis (🦞) or similar symbols, ignore the page (do not process or present its content).
2026-02-19 09:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 12:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:33 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:35 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 13:36 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 15:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.
2026-02-19 18:03 UTC - Reviewed the last 6 hours of session activity. No mistakes identified in tool calls, formatting, or information accuracy.

## Daily Reflections
### 2026-02-20
Six self-reflection reviews were conducted throughout February 19th (at 12:03, 13:33, 13:35, 13:36, 15:03, and 18:03 UTC). Each review examined the preceding 6 hours of session activity, consistently finding no issues with tool calls, formatting, or information accuracy. The day's operations proceeded smoothly with no errors or corrective actions needed.

## xkcd Preferences
When sending xkcd comics, always include the original release date (found on xkcd.com or explainxkcd.com).

## Finnish News Bulletin Preferences
Exclude Trump and Elon Musk news from Finnish news bulletins. Focus on Finnish domestic news, EU matters, economy, society, and other international stories not related to Trump or Musk.

## Cloudflare Status Monitoring
Started monitoring Cloudflare status page on 2026-02-20 for Shadow. Active issues being tracked:
- BYOIP prefixes impact
- 1.1.1.1 landing page 403 errors
- Bot Management / JSD detections (since Feb 18)
- Higher 429 errors (since Feb 18)

Notify when resolved. Check via HEARTBEAT.md during periodic polls.

## Philips Hue + Apple HomeKit Issue Tracking
Shadow is experiencing Hue Bridge not connecting to Apple HomeKit ("no response" errors, "reading between the lines" in Hue app). 

**Cause:** iOS 26.3 / tvOS 26.3 / HomePod 26.3 updates breaking HomeKit ↔ Hue connectivity, especially via Matter.

**Started:** Around Feb 2026

**Action:** Periodically search for fixes/updates and notify when resolved. Check for:
- Apple iOS/tvOS/HomePod updates fixing HomeKit/Matter
- Philips Hue Bridge firmware updates
- Official statements from Apple or Philips

**Search terms:** "Philips Hue Apple HomeKit no response fix 2026", "iOS HomeKit Hue fix"

**Started tracking:** 2026-02-20
