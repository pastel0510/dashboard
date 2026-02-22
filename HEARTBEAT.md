# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

## Cloudflare Status Monitoring
Check https://www.cloudflarestatus.com/ periodically and notify Shadow when current issues are resolved.

Active issues to track:
- Data Loss Prevention (DLP) (Degraded Performance, Newark NJ latency — last update Feb 21, 09:57 UTC, still working on fix. No new updates since then)

Resolved:
- Bot Management / JSD detections — RESOLVED Feb 21, 10:13 UTC
- Workers AI — RESOLVED (now Operational)
- 1.1.1.1 landing page 403 errors — RESOLVED Feb 20, 22:23 UTC
- BYOIP prefixes impact — RESOLVED Feb 21, 00:27 UTC
- Higher 429 errors — RESOLVED (fix implemented Feb 19, monitoring completed)

Notify when remaining issues show "Operational" or "Resolved".

## Tokmanni Data Leak Investigation (Feb 2026)
Monitor for updates on the Tokmanni customer data situation.

**Timeline:**
- 18.2.2026: BreachForums listing ~473k Tokmanni records for sale
- 19.2.2026: Screenshots of customer data appeared online (possibly Telegram)
- 20.2.2026: Tokmanni's Maarit Mikkonen initially said leak traced to customer's infected machine
- 21.2.2026: **UPDATE** — Tokmanni clarifies: leaked data is NOT from their systems. The infected computer theory was wrong. Screenshots removed from online. Still unknown: what data leaked, how many affected, if data is authentic. Tokmanni maintains this was NOT a breach of their systems.

**Current status:** Tokmanni denies any breach of their systems. Source of leaked data remains unknown. Screenshots have been removed.

**Sources to check for updates:**
- Iltalehti.fi, Verkkouutiset.fi, MTV Uutiset
- Tokmanni press releases: https://tokmannigroup.com/en/newsroom/
- BreachForums / Telegram for new data listings

Notify Shadow if:
- New statements from Tokmanni
- Confirmed breach source identified
- Data proven authentic or fake
- Customers notified of breach
