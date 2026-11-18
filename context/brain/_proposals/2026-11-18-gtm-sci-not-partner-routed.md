---
proposed_by: gtm-strategist
date: 2026-11-18
target_file: context/brain/accounts-and-pipeline.md
type: add
status: open
---

# SCI's footprint is not reachable through partner-routed volume — it is one location (Honolulu)

## Current text (if any)

> none — this is an addition to the SCI / Dignity Memorial row's context in
> `accounts-and-pipeline.md` → "Enterprise groups".

## Proposed text

> **SCI volume is almost entirely direct, not partner-routed.** Of 292 SCI-identified OMS
> funeral home records, only **5 appear in the partner-billed manifest**, carrying 498
> partner-billed bookings — of which **Borthwick Mortuary (SCI #4873, Honolulu) is 486
> (97.6%)**, almost certainly NMS/IMS Pacific consolidation. Palm Downtown (SCI #1008) is
> the mirror case: 63 self-billed against 3 partner-billed, i.e. a direct CSI customer who
> occasionally arrives via a partner.
> **Consequence: "expand the SCI footprint" cannot be reframed as reclaiming locations CSI
> already serves through a partner. There are no such locations at scale.** SCI growth has
> to come from the ~4,300 mapped locations that have never appeared in a CSI booking.
> Any approach to the Borthwick volume would read as moving 486 bookings off a partner's
> book, which `CLAUDE.md §5` forbids. If a three-way Pacific conversation is ever worth
> having, **NMS or IMS initiates it, not CSI.**

## Evidence

- `reports/sci-footprint-strategy-2026-12.md` §7 (gtm-strategist, 2026-11-18), which
  states the method and the `[PROVISIONAL]` label.
- Cross-check of `data/raw/oms-funeral-homes-20261109.csv` (292 SCI records: 242 with
  `funeral_home_group = SCI`, 50 by the `(SCI Location #…)` naming convention) against all
  535 rows of `data/derived/partner-billed-homes-manifest-20261118.csv`.
- `reports/customer-cohort-analysis.md`, 2026-11-18 correction block, for the bill-to
  definition of partner-routed.

**Caveat to carry with the fact:** identification is by group field plus name convention,
and the manifest covers only the four IMS/NMS/Bergen bill-to IDs. `data-analyst`'s
`reports/sci-relationship-evidence.md` should confirm it before the figure is quoted as
settled.

## Why another agent would act differently

The Borthwick row looks, in isolation, like evidence of a large recoverable pool of SCI
locations CSI already serves without holding the relationship — an attractive and much
easier growth story than winning new locations. It is one location. Without this on the
record, `sales-lead`, `corpdev` or a future gtm task will reopen that reframe, build a plan
on it, and risk a partner relationship Ethan has named a top priority for a pool that does
not exist.
