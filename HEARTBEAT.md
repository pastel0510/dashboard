# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

# IMPORTANT: When updating "Last checked" timestamps, ALWAYS use the write tool
# to rewrite this entire file. Never use the edit tool — timestamps change every
# run so exact-text matching will always fail.

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

**Last checked:** 2026-03-07 03:42 UTC — No new developments on either case.

Notify Shadow if:
- New statements from Tokmanni
- Confirmed breach source identified
- Data proven authentic or fake
- Customers notified of breach

## Posti Omaposti Data Breach (Feb 25, 2026) — ACTIVE
Serious privacy incident: Users saw other people's data in Omaposti app.

**Timeline:**
- 25.2.2026 (morning): Users report seeing strangers' data (names, packages, letters, salary slips)
- Multiple users saw the same "Hi Sara!" greeting with Sara's pickup info
- Posti CISO claims: "test in the service" caused "single wrong person's data visible"
- Media reports contradict: multiple people affected, salary info exposed
- App taken offline for maintenance
- Posti had NOT yet reported to Data Protection Ombudsman as of midday
- 25.2.2026 (~15:33 Helsinki): Posti announces outage fixed, service restored

**Current status:** Service restored. Posti maintains only "single person's data" was exposed. Users have filed reports with Data Protection Ombudsman.

**Sources to check:**
- HS.fi, IS.fi, Turun Sanomat, Verkkouutiset
- Posti official updates: https://www.posti.fi/fi/asiakastuki/hairiot
- Data Protection Ombudsman statements

**Last checked:** 2026-03-07 03:42 UTC — No new developments on either case.

**Note:** Include source links in all update notifications.

Notify Shadow if:
- Posti files official breach notification FOR THE FEB 25, 2026 INCIDENT
- More users confirmed affected by Feb 25 incident
- Official apology or compensation announced for Feb 25 incident
- Authorities open investigation into Feb 25 incident
- NEW separate fine imposed specifically for the Feb 25 data exposure
