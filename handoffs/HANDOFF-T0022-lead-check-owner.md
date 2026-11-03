# HANDOFF-T0022-lead-check-owner — marketing-lead → pm-orchestrator

**Raised:** 2026-11-03
**Related task:** TASK-0022 (Part 1)
**Urgency:** THIS WEEK (task due 2026-11-10)
**Status:** OPEN

## What I need
**A named human to check the paid-search leads against the OMS.** My proposal:

- **Owner of the check: Susej Roffe** (Bookings Director; works in the OMS daily). Alternate: Kim Soto. This is a lookup of funeral home records against booking history, **about 2 to 3 hours**, and it is not a personnel or performance matter.
- **Ethan** exports one report from Google Ads (read-only): Call details for Campaign #1 and Leads-Search-1, 1 Sep to 2 Nov. This is the only way to check the 15 phone leads. No account change.
- **`revops-crm`** attaches company names to the 21 matched HubSpot contacts inside HubSpot, so the owner does not need HubSpot access.
- **`data-analyst`** tells us what fires the "Contact" conversion on the website (about 42 conversions have no contact record).

If Susej and Kim are both full, any person with OMS search access works; the method needs no judgment about the business beyond "is this a funeral home".

## Why I need it
The 78 leads are the only evidence paid search can pay for itself. Break-even is 5 to 6 bookings out of 78. I can identify 21 of the 78 and none of them is a new account that booked. The rest needs OMS lookups, and agents have no OMS access (`CLAUDE.md §5`).

## What I will do with it
Fill the result table in `reports/paid-search-lead-conversion.md` and re-run it, apply the decision rule in section 4 (scale / hold / reduce), and fold the answer into the attribution spec's baseline.

## When I need it
**By Fri 2026-11-07**, so the result is in the 2026-11-10 report. Re-check on 2026-12-15 for longer lags. Nothing is blocked in the meantime; spend stays inside the envelope Ethan already set.

## What I'll do if I don't get it
Keep the recommendation at HOLD, keep spend below ~$100/day, and wait for EA-45-02 (booking-level export), after which the match becomes a script and needs no one. That is slower: until then paid search remains unmeasured, which is the problem this task exists to end.

## PM decision
_(pm-orchestrator to fill)_
