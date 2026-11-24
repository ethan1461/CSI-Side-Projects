# HANDOFF — data-analyst → product

**Raised:** 2026-11-24
**Related task:** TASK-0024 / the AI-roll-up thesis automation pilot
**Urgency:** THIS WEEK — the window closes the moment a pilot ships
**Status:** OPEN

## What I need

**Do not ship an automation pilot until its baseline exists.** Specifically: tell me
which workflow you intend to pilot, and give me two weeks' notice before anything
changes in it.

## Why I need it

This is the one irreversible thing in the whole programme. From
`reports/ai-rollup-thesis-grounding.md`, Fig's rule is *"baseline before close"* and
*"document impact in a form that survives a buyer's quality-of-earnings review."*

**Once a pilot ships without a before-measurement, the capacity claim is permanently
unprovable.** There is no way to reconstruct the before. A capacity gain CSI cannot
evidence is worth nothing in a valuation and nothing in a decision about whether to do
more of it. A rough baseline taken first beats a precise one taken after, and the
difference is not recoverable at any price later.

## What I will do with it

Compute the before-figures against **M-28's six-cell typology**, which is now binding in
`context/metric-definitions.md` and which was written so a pilot's target workflow maps
onto one or two cells rather than smearing across all of them:

| # | Cell |
|---|---|
| 1 | Domestic, clean |
| 2 | Domestic, reworked (rebooked after carrier cancellation) |
| 3 | International export, no consular requirement |
| 4 | **International export, consular / apostille required** |
| 5 | Inbound onward leg |
| 6 | Cremated remains, any destination |

## Which workflow I would pilot, and how confident I am

**Cell 4 — international export with consular or apostille documentation.** Confidence:
**medium**, and I want to be clear it is a reasoned prior, not a measurement.

**The case for it:** it is the most rule-bound, highest-volume paperwork in the business
(`grounding` §1's criterion is *"reading, drafting, reconciling, scheduling, answering and
documenting"*); mix is roughly 50% international `[ASSUMPTION — FY26 memo, `CLAUDE.md
§4.2`]`; and international carries ~41% rate-card gross margin against ~35% domestic
(M-07), so capacity released there is worth more per hour.

**What I cannot yet tell you, and will not guess.** Which workflows are *most repetitive*
needs the lane-concentration and international-share results from
`scripts/db/platform_metrics_round1.py`, which Ethan has not yet run. I have sent the PM
a set of corrections to that script first — as written it cannot produce a usable
concentration curve (details in my handback to the PM; the material ones are that the
lane grain is the wrong unit for repetition, and that a booking with a repeated airport
in its leg chain silently vanishes from the result).

**One correction worth having now, because it will change your reading of the numbers
when they arrive.** Repetition is not well measured by airport pair. A MIA→SDQ and a
JFK→SDQ share almost all of their documentation, because the paperwork is driven by
**destination country × shipment type**, not by the airport pair. An airport-pair
concentration curve therefore **understates** how rule-bound the work is, possibly
substantially. When the data lands I will publish it on the country × type grain.

## What I need from you, concretely

1. **The candidate workflow**, in one line, mapped to a cell above.
2. **Two weeks' notice** before behaviour changes in it. That is the length of the touch-
   time tally M-28 specifies.
3. **Your view on one question I cannot answer from data**: does the OMS record a
   request-received timestamp distinct from airline-submitted? It is already ranked in
   `context/metric-definitions.md`'s engineering-ask list (items 2 and 4) and it is the
   difference between an audit-grade baseline and a self-reported one. If it exists, the
   baseline is nearly free. If it does not, it is the highest-value small build in the
   programme.

## When I need it

Before any pilot ships. If one is already in flight, tell me today and I will say what
can still be salvaged — usually a concurrent control group on unchanged volume, which is
weaker than a before-baseline but not worthless.

## What I'll do if I don't get it

I will say plainly, in writing, that the pilot's capacity impact is unmeasurable and that
no figure from it may be used in a valuation, a lender conversation or an acquisition
narrative (`CLAUDE.md §7.3`). That is a worse outcome for you than for me, and it is the
honest fallback rather than a threat.

## A tone constraint that belongs in your pilot design, not in review

`grounding` §1 names it and `CLAUDE.md §7.4` makes it binding: **the capacity has to go
into the paperwork behind the call, never the call.** A funeral director reaching a named
human at 3am is the product. Any automation a customer experiences as "you now get a bot"
damages the thing being sold, and it is listed in the sources as one of three red flags
that kill this model. Cell 4 is attractive partly because it is entirely back-office.

## PM decision
<Filled by pm-orchestrator.>
