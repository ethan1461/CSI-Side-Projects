---
title: OMS ("the System") build and vendor acceptance
owner: Ethan Silvey (with Donald); vendor Kyri
as_of: 2026-11-01
source: a7877708, a52e1b09 (see sources.md)
---

# OMS build and acceptance

**Goal:** replace the legacy ERP with the new OMS ("the System") as the cornerstone of
operations, delivered by Kyri under a contract with Exhibit A deliverables.

## Status

- Mar 2026: staff told to use the System, not work around it, and report every bug to
  Kyri and Alex [a7877708, 2026-03-04].
- **May 2026: initial deliverables formally rejected** under contract §4.4 after a
  2026-05-03 video review, with acceptance expected once fixed [a52e1b09, 2026-05-06].
  Ethan's three core required changes:
  1. Align data between the new and legacy systems (Exhibit A §§6, 8).
  2. Funeral-home search filters (§1).
  3. All of §7 On-Demand Shipment Tracking (agent tracking module, disruption alerts,
     status emails to shipping funeral homes).
- Other items flagged: email/text parsing errors (~50% of bookings per Donald, May 2026,
  substantiation not shown); auto dashboard entry on booking start (§2); audit/compliance
  exports and agent performance analytics (§8). §9 funeral-home front end considered
  delivered by Kyri; Donald put it at ~80% [a52e1b09].
- OMS reports did not tie to the legacy system in May 2026 — origin of the "OMS numbers
  not trusted" rule.
- **Status unknown since 2026-05-06** (acceptance, remaining items, whether the §7
  tiered scoping draft was sent). See `open-questions.md`.

## Sources of truth

Contract terms are not stored here. Data-trust rules: `company-facts.md` → Technology.
