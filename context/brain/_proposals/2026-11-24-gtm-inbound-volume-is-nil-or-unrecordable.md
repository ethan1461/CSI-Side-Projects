---
proposed_by: gtm-strategist
date: 2026-11-24
target_file: context/brain/company-facts.md
type: add
status: open
---

# CSI's inbound volume is ~0.3% of the book — the capability gap is real, the volume behind it is not

## Current text (if any)

> - **Inbound (into-U.S.) model:** a licensed customs partner from CSI's network clears the
>   remains at the arrival gateway; CSI then handles the domestic onward leg and final
>   delivery anywhere in the U.S. For U.S.-bound imports CSI refers partners to its network
>   (often partners at Bergen). The network is CSI's core strength.

## Proposed text

> - **Inbound (into-U.S.) model:** a licensed customs partner from CSI's network clears the
>   remains at the arrival gateway; CSI then handles the domestic onward leg and final
>   delivery anywhere in the U.S. For U.S.-bound imports CSI refers partners to its network
>   (often partners at Bergen). The network is CSI's core strength.
> - **But the volume behind that model is a rounding error, or CSI cannot see it.**
>   **150 of 47,881 bookings (0.3%) in the geography workbook have a non-US origin** — about
>   35 a year across ~4.3 years (`data/raw/geo_1_sending.tsv`, computed in
>   `scripts/size_adjacent_lanes.py`). Either CSI's inbound volume really is negligible, or
>   inbound onward legs are booked from the arrival gateway and recorded as domestic, in
>   which case **CSI cannot count its own inbound volume at all.** The sending field carries
>   the shipping funeral home's location, not the shipment's origin, and **there is no field
>   that marks a booking as inbound.** Unresolved; the desk (Vadim, Susej, Kim) can settle
>   it in one question. Evidence: `reports/adjacent-lane-sizing.md` §4c.
> - **Consequence for any inbound argument:** the case for inbound gateway or clearance
>   capability is **not** "CSI already pays a third party for this" — on reading one that
>   spend is roughly **$7K–$14K a year** `[ESTIMATE]`. It is **"CSI cannot serve this flow at
>   all today."** Those are different arguments and only the second is supported.

## Evidence

- `reports/adjacent-lane-sizing.md` §4c and §8
- `data/raw/geo_1_sending.tsv`, `data/raw/geo_2_receiving.tsv`
- `scripts/size_adjacent_lanes.py` → `data/derived/adjacent-lane-sizing.csv` (+ `.meta.json`)
- Contrasts with `reports/bergen-gateway-partnership-prep-2026-11-24.md` §1, which states
  CSI "already buys this capability in rather than owning it" — true about the structure,
  unsupported about the scale.

## Why another agent would act differently

Any agent sizing an inbound opportunity, or arguing for inbound capability, currently has
no way to know that the volume behind CSI's inbound model is ~0.3% of the book — corpdev
scored gateway trade services top of its board partly on a recapturable-cost premise, and
sales or marketing could reasonably describe inbound as an established service line. With
this recorded, the inbound argument gets made on market access rather than cost recapture,
and nobody re-derives the 0.3% from the workbook.
