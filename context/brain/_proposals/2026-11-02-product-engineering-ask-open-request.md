---
proposed_by: product
date: 2026-11-02
target_file: context/brain/data-owners.md
type: add
status: open
---

# Record the first standing engineering ask as open request #2, and say the shipment-level export is a build

## Current text (if any)

> | Shipment-level OMS export | Alex (builds exports), Kyri (OMS) | Biggest single gap |

> | # | Ask | Owner | Unblocks | Drafted | Status |
> | 1 | Revenue and gross margin on secondary services, by fee type, FY2025 and 2026 YTD | Donald | Full revenue model; pricing and valuation work | 2026-11-01 | Meeting next week (main agenda item); Ethan texting Donald 2026-11-02 |

## Proposed text

> Replace the "Shipment-level OMS export" row with:
>
> | Shipment-level OMS export | Alex (builds exports), Kyri (OMS) | Biggest single gap. **A build, not a permission:** Ethan confirmed 2026-11-02 that the Flight Confirmation List, Ready to Invoice List and Collect Shipments pages have no export function. Specified in `reports/oms-export-spec.md`. |
>
> Add to **Open requests**:
>
> | 2 | The standing Monday engineering ask, week 45: 11 ranked items. Cohort extract (4 columns, full history); booking-level file nightly to Drive; funeral home master; whether the OMS captures booking duration; carrier invoice lines; contracted rates for the 15 carriers that have none; whether quotes are stored; three rate-table defects as Error Response Requests; funeral-home-required-before-invoicing. Item IDs `EA-45-01` to `EA-45-11` | Kyri, Alex (colleague questions go separately to Vadim, Kim, Susej, Donald) | Churn, acquisition vs. frequency, account value, lane and corridor volume, realized margin, portal adoption, CAC denominator | 2026-11-02 | Staged for Ethan in `reports/pending-approval/engineering-ask-2026-45.md`; not sent. Classification and any quoted hours are recorded in its Part 4 tracker |

## Evidence

- `reports/oms-export-spec.md` (field-level specification).
- `reports/pending-approval/engineering-ask-2026-45.md` (the ranked ask).
- `tasks/active/TASK-0003-oms-export-specification-and-engineering-ask.md` (premise corrected by Ethan, 2026-11-02: no export buttons exist).

## Why another agent would act differently

An agent that needs OMS data is told to check this file before drafting a request. As it stands it would see "biggest single gap" with no status and could draft a duplicate request, or assume a button exists, which Ethan has confirmed it does not.
