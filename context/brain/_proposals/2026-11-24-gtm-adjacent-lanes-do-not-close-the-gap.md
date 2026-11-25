---
proposed_by: gtm-strategist
date: 2026-11-24
target_file: context/brain/learnings-and-principles.md
type: add
status: open
---

# The three adjacent lanes do not contain the ~$2M, and ship-out preparation is the customer's revenue, not CSI's

## Current text (if any)

Addition to the **Market and growth** section. The two bullets nearest in subject are:

> - **Enterprise groups (SCI, Everstory, Carriage) are the highest-leverage plays** —
>   portal lock-in, corporate reporting, and revenue-share structures independents can't
>   replicate.
> - **International corridors are the highest-margin opportunity.** Corridor expertise
>   (Mexico/LatAm, Israel, China, Pacific/Asia) is a durable differentiator. Prioritize
>   homes with high international volume.

Neither changes. The three bullets below are added after them.

## Proposed text

> - **The adjacent lanes do not close the EBITDA gap, and this has been sized.** The three
>   lanes outside the sized category — the assistance and insurance channel, documentation
>   and consular bureaus, and gateway trade services — carry a **central case of ~$324K a
>   year** of new EBITDA against a **~$2M requirement**. At 100% capture of all three they
>   reach ~$5.1M, so $2M is ~39% of three markets CSI does not serve at all today
>   `[ESTIMATE]`. **The pools are not too small; the share CSI would need is as implausible
>   as the share in-category consolidation needed.** Evidence:
>   `reports/adjacent-lane-sizing.md`. **This is the third independent falsifier of the
>   roll-up thesis and it agrees with the first two.**
> - **Never enter ship-out preparation, and never price a lane off its pool.** Funeral home
>   ship-out preparation is **$3,000–$6,600 per case** on public FTC-mandated price lists —
>   **two to five times CSI's $1,346 air-transport yield**, and a pool of ~$165M–$360M,
>   larger than the air-transport category CSI competes in and entirely outside it
>   `[ESTIMATE]`. **It is also the sending funeral home's own revenue, and the sending
>   funeral home is CSI's customer.** A broker that opens prep rooms at eight gateways
>   competes with the accounts it sells to, in an industry that runs on relationships and
>   remembers. The mirror risk is already on record — a funeral-home consolidator that
>   builds its own shipping desk disintermediates CSI. Treat gateway work as **capability
>   worth partnering for, never as margin to take**.
> - **Two pricing levers on international volume are the same dollar.** The **$500
>   international margin floor** (`reports/the-25m-gap.md` §3, $550K–$1.1M) and **repricing
>   consular work CSI performs at cost** (`reports/adjacent-lane-sizing.md` §3, $424K–$848K)
>   are one lever seen twice if the floor is implemented as a higher all-in price. **Any plan
>   that adds both is wrong by roughly the size of the gap it claims to close.** The
>   consolidated defensible optimistic range for all organic plus adjacent levers is
>   **~$1.9M–$2.2M**, not ~$4.1M.

## Evidence

- `reports/adjacent-lane-sizing.md` (verdict, §§1–5, and the recommendation table in §7)
- `scripts/size_adjacent_lanes.py` → `data/derived/adjacent-lane-sizing.csv` + `.meta.json`,
  with `tests/test_size_adjacent_lanes.py`
- `reports/repatriation-category-size.md` §§2.3, 5 (the category and its Act II row)
- `reports/ai-rollup-screen-and-platform-control.md` §§B.4, B.5, E.1 (the lanes, surfaced)
- `reports/the-25m-gap.md` §§2–3 (the requirement and the organic levers)
- Public funeral home general price lists and the FTC Funeral Rule disclosure requirement,
  cited in full in `reports/adjacent-lane-sizing.md` Sources

## Why another agent would act differently

Three agents are currently pointed at these lanes on the understanding that they are where
the EBITDA has to come from (`ai-rollup-thesis-grounding.md` §6.4). Without this recorded,
corpdev extends a target longlist into lane 2 where no block of the required size exists,
pricing-strategist and gtm-strategist independently price the same international dollar and
double-count it, and someone eventually finds the $165M–$360M preparation pool and proposes
entering it — which is the one move that would damage the customer base CSI's whole franchise
rests on.
