---
proposed_by: data-analyst
date: 2026-11-02
target_file: context/brain/open-questions.md
type: conflict
status: open
---

# C16 — not the same gap; the 58 was never a booking count

## Current text (if any)

> | C16 | Missing funeral-home attribution | 58 HubSpot records missing shipping-FH data [22cc12e7, 2026-09-28] | 59 OMS bookings in 2026 missing FH attribution [`CLAUDE.md` §4.1] | needs data-analyst reconciliation (likely the same gap in two systems) |

## Proposed text

> **C16 — reconciled 2026-11-02 by `data-analyst` and `revops-crm` independently, same
> answer. Not the same gap.** HubSpot has **no custom objects and no booking object**,
> so no HubSpot record can carry a booking-level shipping funeral home. The OMS 59
> counts *bookings* in 2026; the HubSpot 58 counted *contact* records across all
> history — different unit, different period, different system. `revops-crm` could not
> reproduce the 58 from any measurable HubSpot view
> (`reports/hubspot-defect-baseline.md §5`).
>
> **Authoritative attribution figure:** the OMS analytics export field
> `Bookings Missing Funeral Home Link` — **59 for 2026 YTD, 823 across full OMS
> history** (≈99.2% and ≈98.1% attribution completeness). Whatever the 58 counted, it
> was not bookings; it must not be used as an attribution figure.
> Definition and reporting rule: `context/metric-definitions.md` M-23.
>
> **One question remains for Ethan, and it is provenance, not measurement:** did the 58
> come from a saved HubSpot view or list? If so, those 58 record IDs make the match a
> one-line check. Until then C16 stays open on that narrow point only.
>
> **The larger consequence, which outlives C16:** HubSpot holds no shipment history of
> any kind, so no account metric — active, churn, retention, account value — can be
> sourced from the CRM. The booking-level OMS export is the only route.

Keep C16 in the conflicts list but narrow it to the provenance question, and record that
the unit question is settled.

Also affects open question **#31** ("Were the May HubSpot cleanup queue (1,494) and the 58
records missing shipping-FH data cleaned up?"). The second half of #31 should be struck:
there are no such HubSpot records to clean. The 1,494-record cleanup queue is unaffected.

## Evidence

- HubSpot connector, read-only, 2026-11-02 (`data-analyst`):
  `discover_hubspot_schema` with `SEARCH_OBJECT_TYPES` for "shipment booking funeral
  home" returned **zero** results; `GET_OBJECT_TYPES` returned 30 types, **all**
  `HUBSPOT_DEFINED_OBJECTS`, no custom object. `search_properties` on `COMPANY` for
  `shipping_funeral_home`, `funeral_home`, `last_booking`, `shipment_count` returned
  only HubSpot's own meetings/engagement properties — no CSI shipment property on the
  company object.
- `reports/hubspot-defect-baseline.md §5` (`revops-crm`, same day, independently):
  the 58 is not reproducible from any measurable view; HubSpot's funeral-home fields sit
  on **contacts**, with `funeral_home` blank on all 3,574 and `funeral_home_name`
  missing on 3,549; 1 deal and no booking object. That report is the authority on the
  HubSpot side and this proposal does not restate its counts.
- OMS counts: `CLAUDE.md §4.1`; `reports/analytics-reconciliation.md` Finding 5 (823
  across full history, not 58).
- Denominators: `data/derived/annual-totals.csv`.

## Why another agent would act differently

`revops-crm` would otherwise spend part of TASK-0009/TASK-0013 hunting 58 HubSpot records
that do not exist, and would report a defect class that is not a defect. The larger
finding matters more: **HubSpot has no shipment history whatsoever**, so no account
metric — active, churn, retention, account value — can ever be sourced from the CRM. Any
agent planning account analysis off HubSpot is planning against data that is not there,
and the booking-level OMS export is the only route.
