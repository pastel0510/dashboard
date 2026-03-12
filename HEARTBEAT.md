# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.

# IMPORTANT: When updating "Last checked" timestamps, ALWAYS use the write tool
# to rewrite this entire file. Never use the edit tool — timestamps change every
# run so exact-text matching will always fail.

## Viking Line Data Breach (Mar 12, 2026) — ESCALATED
Monitor for updates on the Viking Line customer data breach.

**Timeline:**
- 12.3.2026 (morning): Iltalehti reports customer data breached at Viking Line
- 12.3.2026: Viking Line confirms breach — occurred at subcontractor
- 12.3.2026: Breach involves pre-order (tax-free advance order) data
- 12.3.2026: Reported to Traficom and Kyberturvallisuuskeskus
- 12.3.2026 (~08:30): **UPDATE** — HS reports: subcontractor is **Digitalist Experience**
- 12.3.2026: **UPDATE** — Exposed data includes **contact info** (names, addresses, phone, email)
- 12.3.2026: **UPDATE** — Data **may have been published online** (location unknown)
- 12.3.2026: **UPDATE** — No "sensitive" (arkaluonteinen) data leaked per Viking Line
- 12.3.2026: Reported to **tietosuojavaltuutettu** (Data Protection Ombudsman)
- 12.3.2026 (~10:45): **UPDATE** — Affected customers: "not hundreds of thousands" — exact number unknown
- 11.3.2026 (14:46 UTC): **MAJOR ESCALATION** — DarkWeb Informer: threat actor "bytetobreach" claims FULL breach of Viking Line, not just subcontractor
- 12.3.2026 (~14:33 UTC): **CONFIRMED** — Threat actor claims: complete passenger database + NetAxept payment API data (transaction history, onboard purchases), vehicle reg plates, system credentials. Data allegedly available for FREE download. Attack chain: Solr LFI (2021) → Tomcat creds → reverse shell → pivot to master server.
- 12.3.2026 (~10:15 UTC): Yle article — Viking Line comms director Boijer-Svahnström: "thousands, not hundreds of thousands" affected. No criminal report filed yet. Still subcontractor narrative.

**Current status:** ⚠️ ESCALATED. Viking Line's claim of "only contact info, no sensitive data" is contradicted by threat actor claiming full passenger DB + payment transaction data from all ships. Finnish media (Yle, Iltalehti, IS, HS) still repeating Viking Line's "subcontractor pre-order duty-free only" narrative — none have picked up the bytetobreach / full breach angle.

**Sources to check:**
- DarkWeb Informer: https://darkwebinformer.com/viking-line-ferries-allegedly-breached-with-full-passenger-database-and-payment-data-leaked/
- Iltalehti.fi, Verkkouutiset.fi, IS.fi, MTV Uutiset, HS.fi, Yle.fi
- Viking Line press releases
- Traficom/Kyberturvallisuuskeskus statements
- BreachForums for data listings

**Last checked:** 2026-03-12 22:02 UTC — No new developments (midnight in Finland, 30 min since last check).

Notify Shadow if:
- Viking Line responds to the bytetobreach / DarkWeb Informer claims
- Number of affected customers disclosed with exact figure
- Payment/card data confirmed by authorities
- Data confirmed published on BreachForums/Telegram with proof
- Customers start receiving notifications

## Tokmanni Data Leak Investigation (Feb 2026)
Monitor for updates on the Tokmanni customer data situation.

**Timeline:**
- 18.2.2026: BreachForums listing ~473k Tokmanni records for sale
- 19.2.2026: Screenshots of customer data appeared online (possibly Telegram)
- 20.2.2026: Tokmanni's Maarit Mikkonen initially said leak traced to customer's infected machine
- 21.2.2026: **UPDATE** — Tokmanni clarifies: leaked data is NOT from their systems. The infected computer theory was wrong. Screenshots removed from online. Still unknown: what data leaked, how many affected, if data is authentic. Tokmanni maintains this was NOT a breach of their systems.

**Current status:** Tokmanni denies any breach of their systems. Source of leaked data remains unknown. Screenshots have been removed.

**Sources to check:**
- Iltalehti.fi, Verkkouutiset.fi, MTV Uutiset
- Tokmanni press releases: https://tokmannigroup.com/en/newsroom/
- BreachForums / Telegram for new data listings

**Last checked:** 2026-03-12 22:02 UTC — No new developments.

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
- Posti official updates: https://www.postiasiakastuki.fi/fi//hairiot
- Data Protection Ombudsman statements

**Last checked:** 2026-03-12 22:02 UTC — No new developments.

**Note:** Include source links in all update notifications.

Notify Shadow if:
- Posti files official breach notification FOR THE FEB 25, 2026 INCIDENT
- More users confirmed affected by Feb 25 incident
- Official apology or compensation announced for Feb 25 incident
- Authorities open investigation into Feb 25 incident
- NEW separate fine imposed specifically for the Feb 25 data exposure

## Strix Halo Crash Issue (Mar 2026)
Monitor for fixes/workarounds for AMD Strix Halo crashing after few hours.

**Current status:** Shadow upgraded to kernel 6.19.4 (was on 6.17.0). Monitoring for resolution.

**Known issues:**
- AMD GPU driver bug (cwsr_enable) — fix: disable via amdgpu cwsr_enable=0
- ROCm/AI + video encoding causes GPU hangs (GitHub ROCm#5665)
- Memory allocation issues with large models
- Kernel ≥ 6.18.4 required (older kernels have gfx1151 bug)
- Avoid linux-firmware-20251125 (breaks ROCm)

**Sources to check:**
- Reddit r/LocalLLaMA, r/ASUS
- ASUS ROG forums
- GitHub ROCm issues
- GitHub kyuz0/amd-strix-halo-toolboxes
- Framework BIOS updates: https://frame.work/support/enclosures/desktop

**Last checked:** 2026-03-12 22:02 UTC — No new fixes.

Notify Shadow if:
- Crash resolved after kernel upgrade
- Crash persists after kernel upgrade
- BIOS/firmware update released
- AMD releases driver fix
- New workaround discovered
