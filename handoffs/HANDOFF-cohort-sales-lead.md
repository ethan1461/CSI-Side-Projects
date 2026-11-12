# HANDOFF-cohort-01 — data-analyst → sales-lead

**Raised:** 2026-11-12
**Related task:** customer cohort analysis (`reports/customer-cohort-analysis.md`)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need
Two things, and the first is work rather than information.

1. **Otto and Stacy to work the 48-account at-risk list** in
   `data/derived/accounts-at-risk-volume-decline.csv`, and the 62-account win-back list
   in `data/derived/accounts-dormant.csv`. Both are ranked, carry state and corporate
   group, and contain business names only — safe to hand to a rep as-is (`§7.2`).
2. **Fifty structured calls from the stopped-account population**, asking one question:
   why did you stop? Any 50 of the 349. I need the reasons coded into a short taxonomy
   (price, service failure, a competitor named, no cases to ship, contact left, other).

## Why I need it
The analysis contradicts the working assumption. **Flat volume is caused by accounts
stopping entirely, not by the base shrinking or by weak acquisition.** 349 of the 777
funeral homes that shipped in 2023 have placed no booking at all in 2026, taking 1,067
bookings a year — **54% of everything the acquisition engine has added since.** The
accounts that stay are down only 2.3% in three years.

The at-risk list is **1,301 bookings at stake, roughly 12% of annual volume and ~$1.75M
of revenue** `[ESTIMATE, at the 2026 yield of $1,346]`. That is more than three years of
net acquisition output (+692 bookings), sitting in 48 named accounts. **Defending it is a
week of calls; replacing it through acquisition would take roughly 770 new funeral homes**
at the current 1.7 first-year bookings per new account.

I also need the 50 calls because **churn here is inferred from silence, never observed**
(`metric-definitions.md` M-15). I can tell you that an account stopped. I cannot tell you
why, and no file CSI holds can. This is the cheapest instrument available and it needs no
engineering.

## What I will do with it
Code the reasons into a taxonomy, publish the distribution, and recompute the attrition
finding split by reason so CSI knows which part of the 1,067 bookings is addressable and
which is demographics. That turns a diagnosis into a target.

## When I need it
Lists are usable Monday. Call reasons by end of Q1 FY27 — and if they slip, the FY27
plan gets built on inferred churn rather than observed churn, which is exactly the
mistake `CLAUDE.md §2` was rewritten to correct.

## Three things you should also know
- **57% of the funeral homes CSI won last year never placed a second booking within the
  year, and it is getting worse**: 365-day second-booking rate 51.9% (2023 cohort) →
  45.8% → 42.9%. Year-one cohort survival 46.0% → 38.9% → 36.0%.
  `data/derived/accounts-one-and-done.csv` holds the 302 accounts won since Jan 2025 that
  booked once and never came back. **This is an onboarding list, not a prospecting list** —
  CSI has already paid to acquire these.
- **CSI keeps its real customers.** Accounts shipping ≥4 times a year churn at **9.5%**;
  accounts shipping fewer churn at **53.8%**. Never quote the blended 35% figure to anyone.
- **`Carriage Services` has zero bookings in the entire 48,715-row history**, despite
  appearing in the FY26 memo as an enterprise account in play. Either it has never
  produced volume or its locations are keyed under names CSI does not recognise. Worth ten
  minutes before it is forecast again.

## What I'll do if I don't get it
The lists stand on their own and the PM can route them directly. Without the 50 calls I
will publish the attrition finding with "reason unknown" against all 1,067 bookings and
say plainly that CSI chose not to ask.

## PM decision
<Filled by pm-orchestrator.>
