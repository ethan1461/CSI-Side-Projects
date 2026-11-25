# HANDOFF — gtm-strategist → operations

**Raised:** 2026-11-24
**Related task:** adjacent lane sizing (`reports/adjacent-lane-sizing.md` §§4c, 8)
**Urgency:** WHEN CONVENIENT — one extra line in a questionnaire you are already sending
**Status:** OPEN

## What I need

**Two questions added to the booking-desk questionnaire (`TASK-0019`).** Nothing new sent,
nothing extra scheduled — Kim Soto and Susej Roffe prefer async questionnaires
(`context/brain/data-owners.md`) and you already own that channel.

1. **"Roughly how many enquiries a month come in about bringing someone *into* the US from
   abroad, and what do we do with them?"** Turned away, referred to a partner, handled as a
   domestic leg after someone else clears — the disposition matters as much as the count.
2. **"When we do handle an inbound case, how is it recorded in the OMS — as one booking, or
   as a domestic booking from the arrival gateway?"**

## Why I need it

**Question 1 is the cheapest way to size the one genuinely new market of the three lanes I
was asked to size.** Inbound repatriation is the only flow that sits outside market-intel's
$74M category. My estimate of the US-wide pool is **2,000–8,000 cases a year**, built from
unpublished components, and it is the weakest number in my report. But the question CSI
actually needs answered is narrower and free: **is there unmet inbound demand already
arriving at CSI's door?** The desk knows. Nobody has asked.

**Question 2 resolves a real ambiguity about CSI's own data, and it bears on a live
conversation.** In the geography workbook, **150 of 47,881 bookings (0.3%) have a non-US
origin** — about 35 a year (`data/raw/geo_1_sending.tsv`). Two readings:

- CSI's inbound volume really is a rounding error, **or**
- inbound onward legs are booked from the arrival gateway and look domestic, in which case
  **CSI cannot count its own inbound volume at all.**

This matters because `reports/bergen-gateway-partnership-prep-2026-11-24.md` §1 argues CSI
"already buys this capability in," implying a recapturable spend line. On reading one that
spend is **$7K–$14K a year** `[ESTIMATE]`. The desk's answer tells us which reading is true,
and one line from Susej settles it faster than any export.

## What I will do with it

- Replace `L1B_CASES` and the §4c paragraph in `reports/adjacent-lane-sizing.md`, and re-run
  `scripts/size_adjacent_lanes.py`.
- If the desk reports material turned-away inbound demand, lane 1b reopens as a standalone
  recommendation and the Bergen gateway capability moves from optional to load-bearing.
- If the answer is "almost none ever comes in," I will record that as a closed question so
  nobody sizes this lane again.

## When I need it

With the next questionnaire, whenever that goes. No separate send.

## Two related items for the Monday engineering ask, which you hold

Flagging rather than filing, since the queue is yours and pm-orchestrator's:

1. **There is no field that marks a booking as inbound.** CSI's read is that this is new work
   rather than a defect — but per `CLAUDE.md` §9.6 that is Kyri's and Alex's call to make,
   not CSI's, so **state the read and let them classify it.** It unblocks inbound sizing and
   nothing else today, so **rank it low and send it anyway.**
2. **Cost to serve is the binding constraint on two of my three lanes, not price.** Lane 1b
   (inbound case management) and lane 2b (documentation for buyers CSI does not carry) are
   both labour-heavy against a desk already on 24/7 load. Per `CLAUDE.md` §9.6 the split
   holds: **Vadim owns how long a booking takes, Donald owns what an hour costs.** If
   `TASK-0008` is producing hours per booking type, **an inbound case and an
   international-documentation case are the two types I most need** and neither is a
   standard lane.

## What I'll do if I don't get it

Lane 1b stays `[ESTIMATE]` at 2,000–8,000 cases and the §4c ambiguity stays open, labelled
as such. **The verdict does not change** — inbound would have to be roughly four times my
central case before the three lanes reached $2M. But CSI will keep not knowing whether it is
turning away demand for a service it could sell, which is the kind of thing that is cheap to
learn now and expensive to learn from a competitor.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
