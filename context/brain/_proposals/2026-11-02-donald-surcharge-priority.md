---
proposed_by: Claude (main session, acting for finance)
date: 2026-11-02
target_file: context/brain/data-owners.md
type: add
status: open
---

# Make the carrier surcharge gap the lead item for the Donald conversation

## Current text (if any)

> DR-001 currently frames the Donald meeting around secondary-service margins
> (consulate support, pickup and drop-off, ancillary charges), which remain unknown.
> That item stays. This proposal adds a larger one above it.

## Proposed text

> **Donald — priority item for the scheduled conversation (added 2026-11-02).**
>
> **Question:** Do we bill the carrier misc-and-tax surcharge through to the funeral
> home, or do we absorb it?
>
> **Why it leads:** Every one of the 77 United air waybills invoiced in billing periods
> 45–46 carried a charge above the net AWB value. Mean $32.60, median $36.40, maximum
> $60.40, and **not one shipment without it**. That is 4.44% of carrier cost. At 2025
> volume (10,985 bookings) it annualises to roughly **$358,000** `[ESTIMATE — assumes
> the pattern holds across all carriers and all booking types; only United and Delta
> invoices have been seen]`.
>
> If it is billed through, this is a non-issue and the question closes in one sentence.
> If it is absorbed, it is larger than every routing decision the team has found
> combined, and it is recoverable without winning a single new customer.
>
> **Supporting signal:** the OMS Extra Line Items catalog lists `FS — FUEL SURCHARGE`
> with a **Flexible** calculation type and a **$0.00 default rate**. A surcharge that
> defaults to zero and relies on an agent to set it per booking is a plausible leak
> path, though not proof of one.
>
> **What would settle it:** one invoice to a funeral home for a shipment we can trace
> to a carrier invoice. Compare what CSI paid against what CSI billed. One example
> answers it.
>
> **Secondary question for the same conversation:** 56 of 77 United shipments already
> carried a carrier discount, averaging $257. Is that discount reflected in what we
> charge, or does it fall to margin? Either answer is useful; we currently do not know
> which it is.
>
> **Evidence:** `reports/carrier-margin-resolved.md`,
> `data/derived/realized-margin-by-lane.csv`, `scripts/realized_margin.py`.
> **Owner:** Donald. **Raised by:** Ethan, 2026-11-02.

## Evidence

- `data/raw/carrier-invoices/UA-278010.csv`, `UA-287331.csv` — 77 air waybills, United
  billing periods 45 and 46, Sep–Oct 2026
- `scripts/realized_margin.py` — computes the gap between `Nett Value of AWB` and
  `Total Due UA (Invoice Currency)`
- Extra Line Items screenshot supplied by Ethan, 2026-11-02 — `FS` fuel surcharge at
  $0.00 default

## Why another agent would act differently

**finance** would otherwise walk into the Donald meeting leading with secondary-service
margins, which are unknown but small, instead of a quantified ~$358K question that one
invoice comparison can close. **pricing-strategist** would otherwise model lane margin
from contracted rates and be systematically ~4.4% optimistic on every lane, because the
contracted rate is not what CSI actually pays.
