---
proposed_by: Claude (main session)
date: 2026-11-02
target_file: context/brain/company-facts.md, context/brain/data-owners.md
type: add
status: open
---

# Carrier selection is an unmanaged margin decision; Donald owns rate-table input

Two facts from Vadim Shapiro's written reply to Ethan, 2026-11-02. Both change how
other agents should work, which is why they belong in the brain rather than only in a
report.

## Proposed text — `company-facts.md`

> **Carrier selection is an unmanaged margin decision.** On lanes where more than one
> carrier serves the route, which carrier an agent picks materially changes CSI's
> margin, and nothing on screen guides the choice. The COO has given verbal guidance
> for years; adherence varies by agent, by his own account. No record exists of which
> carrier was chosen on any booking, so the leak cannot currently be sized.
>
> **The worked example (Vadim, 2026-11-02):** MIA→GUA earns **$375 on Avianca** and
> **over $700 on Volaris**. CSI's own rate sheet prices both at **$1,450** to the
> funeral home, so the customer's price, service and routing are identical and the
> entire gap is margin. Implied carrier cost: ~$1,075 Avianca, under $750 Volaris —
> `[DERIVED from Vadim's margin statement, not a rate card]`. Neither carrier has a
> contracted rate in the OMS.
>
> **Status: real, unsized.** Sizing needs carrier-per-booking (EA-45-02) and a list of
> lanes with a genuine two-carrier choice (requested from Vadim).
>
> ⚠️ **`CLAUDE.md §7.7` boundary — measure the decision, never the decider.** The data
> that would size this sits one join away from who booked it. No agent in this
> workforce produces anything that ranks or identifies individual booking agents, and
> every export built for this work excludes agent identity at the query, as
> `reports/oms-export-spec.md §4.2` already requires.

## Proposed text — `data-owners.md`

> **Rate table input — Donald.** Vadim, 2026-11-02: *"I am not 100 percent sure why
> there are so many rates in system for the lanes where you are seeing multiples. I
> believe Donald is in charge of inputting that data."* Marked **believed, not
> confirmed** — Vadim hedged, and Donald has not been asked yet.
>
> **Consequence:** rate-table anomalies go to Donald before they go to Kyri and Alex
> (`CLAUDE.md §9.6`, colleague first). Two items were struck from the week-45
> engineering ask on this basis: the blank `shipment_rate_type` and the uniqueness-key
> question. Opening an Error Response Request against the developer for rows a
> colleague enters by hand would be wrong on the facts and expensive in credibility.
>
> This also puts rate-table hygiene alongside margin analytics, cost-to-serve and lane
> profitability in Donald's column — he now owns both the margin question and the data
> that answers it.

## Evidence

`reports/carrier-selection-margin-leak.md` (Vadim's reply quoted in full, with the
$1,450/$1,450 cross-check against `data/raw/vadim-rate-sheet-20260813.xls`).
`reports/vadim-rate-sheet-reconciliation.md` for the rate-table reconciliation.

## Why another agent would act differently

- **operations** — this is the largest operating-leverage finding to date and it is in
  its lane. It should own the lane list once Vadim sends it.
- **pricing-strategist** — has been modelling rate architecture on the assumption that
  the price CSI charges is the lever. On these lanes the price is identical and
  **carrier choice is the lever**, which is a different kind of recommendation.
- **product** — the fix is a screen, not a memo. EA-45-12 exists because of this.
- **finance / corpdev** — an unmanaged margin decision repeated across ~11,000
  shipments a year is a diligence finding as well as an opportunity. It should not
  reach a valuation narrative as upside until it is sized.
- **Everyone** — the §7.7 boundary above. This is the finding in the program most
  likely to tempt an agent into producing per-person analysis.

## Caveat

Vadim's margin figures are the COO's recollection, not a rate card, and Donald owns
margin analytics. They are internally consistent with Vadim's own sheet, which is why
confidence is high that the gap is real — but the specific dollar figures should carry
`[VADIM 2026-11-02, unconfirmed]` until Donald confirms them.
