---
title: Google Ads / Performance Max and conversion tracking
owner: Ethan Silvey
as_of: 2026-11-01
source: 94319f3f, 9d6d7fa8, 6c9305c6 (see sources.md); CLAUDE.md §3.6, §9.2
---

# Google Ads

**Goal:** paid search that produces quote requests from identified funeral homes —
measurable against bookings. Today ROAS is unmeasurable (`CLAUDE.md` §3.6).

## Status

- **Aug 2026:** campaign relaunch with Performance Max; keyword strategy by theme
  (corridor repatriation, consular documents, gateway geo, competitor conquesting, brand
  defense) plus negatives, headlines and descriptions [94319f3f, 2026-08-30]. That copy
  was built on the stale five-gateway and inbound-customs claims —
  see `deliverables-index.md`.
- **Tracking gaps as of 2026-09-17** [6c9305c6]: phone/email conversion actions exist
  but triggers were not attached; a duplicate GA4 tag needed removing; the GA4 tag had
  been deleted from GTM and needed restoring; hardcoded tags were to be removed; an older
  Ads account still loads through a Google Tag destination (payment-method status
  unknown). Legacy forms post via AJAX with no thank-you page, blocking simple
  conversion tracking. Needs DNI call tracking.
- Oct 2026: optimization call upcoming; PMax cost-per-lead looked implausibly low and
  Search showed zero conversions — reconcile reported leads with the bookings team
  [9d6d7fa8, 2026-10-04].
- Ethan asked for aggressive Google Ads and LinkedIn budget plans for the NFDA/FIAT-IFTA
  window; plan drafted, execution unknown [9d6d7fa8]. Conflicts with
  instrumentation-before-spend (**C13**).

## Next steps

- Confirm the tracking fixes landed (open question) before any further spend decision.
- Live ad assets: check for stale gateway/customs claims.
- Tag and account IDs are read from the live systems, not stored here.
