# HANDOFF-cohort-06 — data-analyst → revops-crm

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
**Three HubSpot lists built from three CSVs I have already produced**, plus an account
health property if one exists. You are the only agent that writes to HubSpot
(`CLAUDE.md §7.1`), so these come through you rather than from me.

| Source | Rows | Proposed list | Why it is a list and not a report |
|---|---|---|---|
| `data/derived/accounts-at-risk-volume-decline.csv` | 48 | "At risk — volume decline" | Otto and Stacy need it in the tool they work in, ranked by bookings at stake |
| `data/derived/accounts-dormant.csv` | 62 | "Dormant — win back" | Carries days since last booking, so it sorts itself |
| `data/derived/accounts-one-and-done.csv` | 302 | "Won, never re-booked" | An onboarding-failure cohort, **not a prospecting list** — label it so nobody cold-pitches an existing customer |

Each row carries `funeral_home_id`, business name, state, corporate group and an
`is_partner_tier` flag. **Business names only — no individual contact, email, phone or
address is read by the script at all**, so there is nothing here to strip (`§7.2`).

**Matching:** `funeral_home_id` is the OMS key. `scripts/match_oms_hubspot.py` and the
account-layer work already solved OMS→HubSpot resolution, so please reuse that rather than
matching on name — my own name join to QuickBooks left **30 names ambiguous and 156
unmatched**, and I deliberately left them unjoined rather than guessing. Report the match
rate and leave the misses out rather than approximating them.

**Please also set `is_partner_tier` accounts aside for Ethan** rather than putting them in
a rep's working list. `Scarpa-Las Rosas Funeral Home` appears on both the at-risk and
dormant lists (17 bookings in 2024, 4 in 2025, none in 2026). Per `CLAUDE.md §5` that is a
relationship question, not a sales task.

## Why I need it
Flat volume is caused by accounts stopping entirely: **349 of the 777 funeral homes that
shipped in 2023 have placed no booking in 2026, taking 1,067 bookings a year** — 54% of
everything acquisition has added since. The at-risk list alone is **1,301 bookings at
stake, ~12% of annual volume.** A CSV in `data/derived/` does not get worked; a HubSpot
list does.

## What I will do with it
Re-run `scripts/analyze_customer_cohorts.py` quarterly and hand you the diff, so the lists
stay live rather than becoming a November 2026 snapshot. If HubSpot can hold the account
state, the quarterly refresh becomes a comparison rather than a rebuild — and **that gives
CSI its first measurable retention metric**, because I will be able to tell you whether
accounts on the at-risk list recovered.

## When I need it
Lists in HubSpot before Monday, so the field has them for the week. Log the writes in
`reports/` before executing, per `§7.1`'s destructive-and-bulk discipline — these are
creates rather than overwrites, so the risk is low, but 302 rows is above the 25-record
line for care if any of it merges or overwrites.

## What I'll do if I don't get it
The CSVs stand alone and the PM can route them to sales directly as files. The cost is
that nothing is tracked and the quarterly re-run has nothing to compare against.

## One finding you will care about independently
**`Carriage Services` has zero bookings in the entire 48,715-row shipment history**,
despite being named in the FY26 memo as an enterprise account in play. The account
dimension has three Carriage records and none has ever shipped. Either the relationship has
never produced volume, or Carriage locations are keyed in the OMS under names CSI does not
recognise as Carriage — which would be a `funeral_home_group` population gap of exactly the
kind the account layer exists to fix. Worth checking before it is forecast again.

## PM decision
<Filled by pm-orchestrator.>
