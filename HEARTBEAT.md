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
- 13.3.2026 (~18:25 UTC): **MAJOR DEVELOPMENT** — ByteToBreach leaked full source code of Sweden's E-Government platform from compromised **CGI Sverige** infrastructure. Actor explicitly references Viking Line as example of companies blaming subcontractors.
- 13.3.2026 (~06:00 UTC): **SWEDISH MEDIA** — Expressen reports Viking Line breach linked to same actor as CGI Sverige hack
- 13.3.2026 (~09:00 UTC): **SWEDISH MEDIA** — Aftonbladet reports CGI Sverige hacked, "multiple authorities active", connects to Viking Line
- 13.3.2026 (~09:30 UTC): **INVESTIGATION OPENED** — Sweden officially probes e-government platform source code leak from CGI Sverige. Reports explicitly link ByteToBreach to both CGI Sverige hack and Viking Line as "an ongoing campaign targeting Swedish and European infrastructure via CGI's managed services footprint."
- 13.3.2026: Finnish media still on subcontractor narrative, no ByteToBreach connection reported

**Current status:** ⚠️ ESCALATED. Sweden has opened an official investigation into the CGI Sverige breach. Multiple international outlets now linking ByteToBreach to both CGI Sverige and Viking Line. Finnish media still only reporting subcontractor narrative.

**Sources to check:**
- DarkWeb Informer Viking Line: https://darkwebinformer.com/viking-line-ferries-allegedly-breached-with-full-passenger-database-and-payment-data-leaked/
- DarkWeb Informer CGI Sverige: https://darkwebinformer.com/full-source-code-of-swedens-e-government-platform-leaked-from-compromised-cgi-sverige-infrastructure/
- TradingView/Cointelegraph: https://www.tradingview.com/news/cointelegraph:077d8119f094b:0-sweden-probes-reported-leak-of-e-government-platform-source-code/
- Aftonbladet: https://www.aftonbladet.se/nyheter/a/ArvG0E/cgi-sverige-uppges-vara-hackade-flera-myndigheter-aktiva
- Expressen: https://www.expressen.se/nyheter/sverige/uppgift-sveriges-digitala-plattform-hackad-av-aktor/
- Iltalehti.fi, Verkkouutiset.fi, IS.fi, MTV Uutiset, HS.fi, Yle.fi
- Viking Line press releases
- Traficom/Kyberturvallisuuskeskus statements

**Last checked:** 2026-03-13 12:32 UTC — Sweden officially investigating. Finnish media still repeating subcontractor narrative.

Notify Shadow if:
- Finnish media reports on CGI Sverige / bytetobreach connection
- Viking Line responds to the bytetobreach claims
- Number of affected customers disclosed with exact figure
- Payment/card data confirmed by authorities
- Data confirmed published on BreachForums/Telegram with proof
- Customers start receiving notifications
- CGI Sverige or Swedish authorities issue statement on Viking Line specifically

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

**Last checked:** 2026-03-13 12:32 UTC — No new developments.

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

**Last checked:** 2026-03-13 12:32 UTC — No new developments.

Notify Shadow if:
- Posti files official breach notification
- More users confirmed affected
- Official apology or compensation announced
- Authorities open investigation
- NEW fine imposed specifically for the Feb 25 data exposure

## Strix Halo Crash Issue (Mar 2026)
Monitor for fixes/workarounds for AMD Strix Halo crashing after few hours.

**Current status:** Shadow upgraded to kernel 6.19.4 (was on 6.17.0). Monitoring for resolution.

**Last checked:** 2026-03-13 12:32 UTC — No new fixes.

Notify Shadow if:
- Crash resolved after kernel upgrade
- Crash persists after kernel upgrade
- BIOS/firmware update released
- AMD releases driver fix
- New workaround discovered
