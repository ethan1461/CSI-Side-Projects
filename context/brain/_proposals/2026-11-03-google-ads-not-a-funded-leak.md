---
proposed_by: marketing-lead
date: 2026-11-03
target_file: CLAUDE.md §3.6 (Ethan applies), context/brain/initiatives/google-ads.md
type: correct
status: open
---

# Google Ads is a small unmeasured pilot, not an "active, funded leak"

## Current text (if any)

> `CLAUDE.md §3.6`: "Measurement debt — CSI has never connected a marketing dollar to a booking. Google Ads is now live with budget committed and **ROAS is currently unmeasurable.** This is an active, funded leak, not a theoretical one."
>
> `context/brain/initiatives/google-ads.md`: "PMax cost-per-lead looked implausibly low and Search showed zero conversions".

## Proposed text

> 6. **Measurement debt** — CSI has never connected a marketing dollar to a booking. Google Ads has run since 30 Aug 2026 at about $2,000 a month (roughly 0.17% of revenue), and **its reported return is not usable**: the account's headline conversions were inflated by a $200 value assigned to YouTube "contacts", since removed, and Performance Max is paused. The real figure is 78 search-sourced leads at about $33 each, of which nobody has yet checked how many became bookings. The cost is small; the failure to measure is the problem. See `reports/paid-search-lead-conversion.md`.
>
> google-ads.md: replace the "Search showed zero conversions" line with: "Oct 2026: Search shows 55 conversions (Leads-Search-1). Performance Max's conversions were inflated; see TASK-0022."

## Evidence

- `reports/google-ads-should-we-pull-back.md` (spend ~$3,605 since launch, 0.17% of revenue; 368 of 391 Campaign #1 conversions from YouTube at an assigned $200).
- `data/raw/google-ads-20261103/` (`Performance by channel.csv`: Search 55 conversions; `028a841e-Search_terms_insight_report.csv`).
- Note: spend is $3,605 on the billing basis and about $4,118 on the weekly cost series in the exports; the difference is unexplained (`reports/paid-search-lead-conversion.md` §1).

## Why another agent would act differently

"Funded leak" tells every agent to treat paid search as an emergency and to cut it. It is a small, unproven pilot that costs about three shipments' yield; the right action is to measure it, and a hold or modest scale decision depends on that.
