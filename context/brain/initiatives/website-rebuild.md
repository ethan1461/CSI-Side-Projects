---
title: Website rebuild, Rednodo exit and site privacy
owner: Ethan Silvey (build: Kyri)
as_of: 2026-11-01
source: d1fa8e90, 6c9305c6, ed2e6f96 (see sources.md); CLAUDE.md §6
---

# Website rebuild

**Goal:** rebuild cargosalesintl.com on Next.js integrated with the OMS, make the portal
the focal point, improve AI/agent discoverability, roll out the new brand kit, and end
the dependency on Rednodo. Ethan's aim: "an SEO marketer's dream" once branch, gateway
and corridor pages exist [6c9305c6, 2026-09-17; d1fa8e90, 2026-09-16].

**Owner:** Ethan. Build and 301 redirects: Kyri. Legacy code/GTM/DNS until cutover:
Claudio (Rednodo).

## Legacy site (as found Sept 2026)

Laravel 8 (end of life), EN/ES pages; booking and quote forms post to the ERP API at
erp.cargosalesintl.com with no thank-you page; contact form uses HubSpot; a small admin
panel runs the blog. 242 live URLs, of which 140 are auto-generated tag pages; ~51 real
English pages. Organization schema exists [d1fa8e90; 6c9305c6].

## Status

- Domain in a CSI-controlled GoDaddy account, renewed through 2032, 2FA on; Microsoft
  365 mail does not depend on the web host [6c9305c6, 2026-09-17].
- Dates: SEO/redirect review target 2026-10-09; DNS TTLs lowered ~2026-10-12; **DNS
  cutover target 2026-10-14 — status unknown since 2026-09-17** (open-questions #1).
- As of 2026-09-17 Claudio had confirmed 9 of 17 requested fixes; the DB dump looked
  incomplete (10 of ~70 articles); full archive first requested 2026-08-20.
- DNS hygiene issues found 2026-09-17: stale SPF, DMARC at p=none, leftover records.
- Defensive domain **cargosales.us** (same GoDaddy account) does not resolve; renew
  before **2026-11-06** (time-bound) [6c9305c6].
- **Privacy (Oct 2026):** no privacy policy was linked anywhere on the site, including
  the online-booking form — accepted as a priority fix. Website document uploads are
  saved on the ERP server and emailed to the shared bookings inbox; access, retention
  and deletion practices unclear [ed2e6f96, 2026-10-30].
- A shared production code zip contained live credentials and a database dump; the
  sender should circulate a sanitized copy and the vendor rotate credentials
  [d1fa8e90, 2026-09-16]. Rotation status unknown.

## Key decisions

- Redirect each tag page to the nearest surviving service/corridor page; never
  mass-redirect to the homepage [6c9305c6].
- Gateway pages state each gateway's own capabilities; no invented operational facts
  before the Kim/Susej questionnaire returns [6c9305c6].
- Before handover, get Rednodo's deployment, retention and storage details in writing;
  ask for configuration, never send customer files [ed2e6f96].
- Copy references a single canonical fact sheet [6c9305c6].

## Next steps

Confirm cutover; privacy policy live; cargosales.us renewal; credential rotation;
complete archive/DB from Rednodo; tracking fixes (`google-ads.md`).
