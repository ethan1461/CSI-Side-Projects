---
proposed_by: data-analyst
date: 2026-11-18
target_file: context/brain/accounts-and-pipeline.md
type: correct
status: open
---

# SCI's "4,439 active locations" is a corporate register, not 4,439 funeral homes — the penetration denominator is 1,582

## Current text (if any)

From `context/brain/accounts-and-pipeline.md`, the SCI / Dignity Memorial row:

> Jun 2026: built portal demoed (Quote → Booking → Tracking); pilot shortlist sent (incl. Riverside
> Gordon, Riverside-Stanetsky, Star of David, Bailey Memorial, Hines-Rinaldi, Palm Mortuary Las
> Vegas branches).

And from `CLAUDE.md §5`:

> SCI / Dignity Memorial (portal pilot approved, 4,439 active locations mapped, Pam driving next
> steps)

## Proposed text

Append to the SCI / Dignity Memorial row in `accounts-and-pipeline.md`:

> **The 4,439 mapped locations are a corporate location register, not funeral homes, and must never
> be used as a penetration denominator.** 486 legal-posting rows, 486 legal-parent rows, 466
> overhead and 40 legal rows are accounting structures; 625 operating rows are cemeteries. 2,961 are
> operating and **1,582 are on SCI's Funeral Home Product Line — and 243 of the 246 SCI locations
> CSI serves sit on that one product line.** Use **1,582**. On it, CSI is active in **138 locations
> (8.7%)** and has ever shipped for **248 (15.7%)**. Quoting 123/4,439 ≈ 2.8% understates CSI's
> position by roughly a factor of three. Working: `reports/sci-relationship-evidence.md` §1,
> `data/derived/sci-denominator.csv`, `scripts/sci_relationship_evidence.py`.
>
> **Three further measured facts about this relationship, as of 2026-11-18:**
> - **It is concentrated.** 10 locations of 248 carry 57.9% of SCI volume; 5 carry 45.9%. Seven of
>   the top ten are Jewish-tradition chapels (the Israel corridor); the others are Honolulu and two
>   Florida homes. Four of the top five are the August 2026 pilot shortlist locations — the pilot is
>   running where the relationship lives.
> - **It is geographically narrow.** Florida, Hawaii and Nevada are 78% of SCI volume. Texas and
>   California hold 66 SCI shipping locations and produce 232 bookings all-time, despite both having
>   a CSI gateway *and* pickup service.
> - **It is low-yield.** SCI is ~11% of CSI's bookings but 7.8% of its revenue; revenue per booking
>   is $1,087 against CSI's ~$1,312. Expanding SCI on today's mix dilutes yield.

Also correct the parenthetical in `CLAUDE.md §5` from "4,439 active locations mapped" to
"4,439 register rows mapped, of which 1,582 are funeral-home locations — see
`context/brain/accounts-and-pipeline.md` before quoting any penetration figure".

## Evidence

- `reports/sci-relationship-evidence.md` (data-analyst, 2026-11-18), §1–§4
- `data/derived/sci-denominator.csv`, `sci-concentration.csv`, `sci-geography.csv`,
  `sci-revenue-by-year.csv`, each with a `.meta.json`
- `scripts/sci_relationship_evidence.py` v1.0.0; 51 tests in
  `tests/test_sci_relationship_evidence.py`, all passing. The strict definition reproduces the
  97 / 120 / 123 shipping-location figures in `reports/customer-cohort-analysis.md` exactly, so the
  two reports tie.
- Source: `data/raw/sci-location-report-202606.xlsx`, sheet `Active SCI Location`, columns
  `location type`, `Business Line`, `Product Line`.

## Why another agent would act differently

**It already happened.** `reports/sci-footprint-strategy-2026-12.md` (gtm-strategist, 2026-11-18)
§1 recommends Ethan open the 2 December SCI meeting by saying CSI reaches "fewer than three in a
hundred Dignity locations" — a figure computed on 4,439. The real figure is ~8.7%. An agent that
reads "4,439 active locations mapped" in `CLAUDE.md §5` and divides by it will understate CSI's
position in front of the largest funeral home group in the country, and a vendor leader who knows
her own register will know it includes 486 legal posting locations and 625 cemeteries.

The concentration and low-yield facts change decisions too: gtm-strategist's own reversal condition
for its headline recommendation was "if SCI volume is concentrated in a handful of locations", and
`CLAUDE.md §0` judges work on *profitable* volume, which a 17%-below-book relationship bears on
directly.
