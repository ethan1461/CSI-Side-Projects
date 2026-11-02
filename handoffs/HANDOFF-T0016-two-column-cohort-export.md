# HANDOFF-T0016 — data-analyst → product

**Raised:** 2026-11-02
**Related task:** TASK-0016 (feeds TASK-0003, due Wed 2026-11-04)
**Urgency:** THIS WEEK (the ask is due Wednesday)
**Status:** OPEN

## What I need

**One line item in the Monday engineering ask, ranked separately from the full
booking-level export: a two-column history export, `funeral_home_id` and `booking_date`,
one row per landed booking, full OMS history.**

Nothing else. No revenue, no lane, no carrier, no status, no names — and explicitly no
decedent or family columns (`CLAUDE.md §7.2`).

It must be ranked as its own line, not folded into the booking-level row specification,
**so that a "no" or a "that's a Change Order with a price" on the full export is not
automatically a no to this.** Two integer-ish columns from one table is a materially
smaller build than the full row spec, and it may fall in a different contract bucket.

Also useful, if it costs nothing to add: the same two columns for the 823 bookings that
have no `funeral_home_id`, so the unattributed set can be sized by period rather than
only in total.

## Why I need it

Six metrics in `context/metric-definitions.md` are BLOCKED on exactly these two columns
and on nothing else — M-12 active account, M-13 new account, M-14 reactivated, M-15
churned and churn rate, M-16's measurement, M-17 shipments per retained account.

The classification logic is already written and tested (`src/metrics.py`,
`tests/test_metrics.py`, 19 known-answer tests passing). **The day the file lands the answers come out the
same day**, with no further analysis to commission. That is the whole argument for
ranking it high: it is the largest unblock per unit of engineering effort on the board.

It is also the only route. Verified via the HubSpot connector on 2026-11-02: HubSpot has
**no custom objects and no shipment or shipping-funeral-home property**, so there is no
CRM-side substitute for any account metric. (This also resolves conflict C16 — see
`context/brain/_proposals/2026-11-02-c16-attribution-gap-resolved.md`.)

## What I will do with it

Run `classify_accounts` over the full history and publish the volume decomposition that
`CLAUDE.md §2` says is still unanswered: how much of the 1.3% booking growth is accounts
gained, how much is accounts lost, and how much is retained accounts shipping more or
less often. Revenue-weighted churn needs one more column (revenue) and can wait; the
account-count decomposition does not.

Downstream consumers that are currently blocked and would unblock together:
`gtm-strategist` (segment targeting, decline list), `sales-lead` (account scoring),
`marketing-lead` (CAC denominator), `corpdev` (retention as a valuation input),
`revops-crm` (customer vs. prospect, via the crosswalk in HANDOFF-T0009).

## When I need it

**Wording into the ask by Wed 2026-11-04.** The data itself whenever engineering can
deliver it; week 46 would let the decomposition land in that week's reports.

Note on sequencing: this does **not** replace HANDOFF-T0009's funeral-home master ask.
That one gets names and the HubSpot crosswalk; this one gets cohort behaviour. They share
a key and should go in the ask together, but either is useful without the other —
cohort analysis works on opaque IDs and needs no names at all, which is also why it
carries no PII risk.

## What I'll do if I don't get it

There is no fallback, and I want that on the record rather than softened. These six
metrics cannot be approximated from monthly aggregates — a monthly total contains no
information about which accounts produced it. If the export does not happen, the honest
position is that **CSI cannot say whether its flat volume is a retention problem or an
acquisition problem**, and every GTM and marketing plan that assumes one or the other is
assuming. I will keep publishing M-03, M-07, M-08, M-11 and the data-quality metrics, and
will say plainly in each report that the decomposition is unavailable and why.

One partial route worth testing first (`§9.6` — ask a colleague before engineering):
**can Kim or Susej export a booking list from the OMS admin screens by hand, even for a
single recent month?** One month of two columns would not give churn (that needs two
years), but it would give the per-account frequency distribution, which is the
`[ASSUMPTION]` holding up the N=365 window choice in `context/metric-definitions.md`.
Worth asking before it is paid for.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
