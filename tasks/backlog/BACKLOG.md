# Backlog — ranked, 2026-11-03

**Suggested tasks, not assigned.** Each is a real question raised by something that landed on
2026-11-02 or 2026-11-03. Promoted to `tasks/active/` with a full task file when activated.

**Ranking rule:** what it unblocks per unit of effort, with `§10`'s cap in mind — no agent
runs more than 5 active tasks, and most of the roster should be dormant most of the time.

---

## Tier 1 — ready now, high value

### B-01 · Cohort and churn analysis · `data-analyst`
**Nine BLOCKED metrics just became computable and nobody has noticed.** `context/metric-definitions.md`
marks M-12 through M-17 (active, new, reactivated, churned, churn rate, shipments per
retained account) as blocked on a booking-level export. **The funeral home table carries
`booking_count`, `first_booking_date` and `last_booking_date` on 2,536 accounts** — that is
most of the cohort picture without engineering. Produce the real churn rate, the cohort
curve, and update the metric definitions from BLOCKED to LIMITED with the limits stated.
*Caveat to resolve first: booking counts sum to 52,269 against ~43,600 bookings in OMS history.*

### B-02 · Carrier-selection decision capture · `operations` + `product`
Design the one-click "why" field for EA-45-12 — *no space / not a known shipper / weight /
routing or timing / customer request / other*. **This manufactures the dataset that does not
exist:** today nobody can tell a correct routing from a mistaken one on any booking, which is
why the POS case is unresolvable and the margin leak unsizeable. One build, two outcomes.

### B-03 · Competitor set from auction data · `market-intel`
Google Ads auction insights named real domains with real impression share, against CSI at
23.67%. **Corrected 2026-11-03 by `corpdev`: `swacargo.com` at 22.74% is Southwest Airlines
Cargo, not a competing broker — I listed it as a competitor and that was wrong.**

The refinement worth carrying: Southwest Cargo is on CSI's **cost** side as a carrier, *and*
is the direct-booking alternative a funeral home would use instead of CSI. That is precisely
what `§1` differentiator #1 answers — *"funeral homes pay the same air rate they'd pay calling
the airline direct."* **So an airline outbidding CSI on its own search terms is a positioning
finding, not a competitor-set finding.**

Genuine broker domains to profile: **internationalremainsshipping.com 27.60%,
mortuary-shipping.com 10.69%, natmortuarysh…, altogetherfuner…, mortrack.com**. Note that
the first two **failed to resolve** from this session and need allowing. Apply `§5` alliance
rules throughout.

### B-04 · Triage the 807 chat-origin contacts · `revops-crm`
**A `§7.2` exposure, not a hygiene item.** 807 HubSpot contacts were created by website chat,
160+ on personal email addresses. Bereaved families reach CSI that way. They are currently
excluded from every list as a precaution — that is the right default but it is not a
resolution. Establish what is in them **without reading conversation content**, and recommend.

---

## Tier 2 — ready, second order

### B-05 · Booking-desk capacity model · `operations`
Vadim: *"I am not sure how we can improve them with the staff we have at our disposal."*
Ethan's FY27 target is explicitly held open on capacity. Model what the desk can absorb at
current headcount. **Vadim owns hours per booking; Donald owns what an hour costs** (`§9.6`)
— ask each for their half, never combine without Donald. **Nothing that assesses individuals**
(`§7.7`).

### B-06 · SCI location mapping · `gtm-strategist`
**The largest identified addressable pool CSI has.** SCI has 4,439 locations; 242 are in the
OMS and 189 have ever booked. Northstar is 45 locations / 41 booking / 2,896 lifetime
bookings — far denser. Work out why, and what mapping the rest is worth. Pam drives SCI and
**anything naming them needs Ethan every time** (`§7.1`).

### B-07 · Bundled rates — why wasn't it used? · `product`
The rate lookup returns a **$2,100 bundled package** (East Coast → MIA → IBC → Caribbean,
trucking included) for the exact POS journey quoted at $3,150. Bundles exist, are cheaper,
and apparently weren't reached for. How are they surfaced, how are they priced, how often
are they used?

### B-08 · Known-shipper status by carrier · `compliance`
CSI's own quote template says quotes are *"subject to… the shipper's known shipper status
with the respective airlines."* **Nobody has that recorded anywhere queryable**, and it may
rule out carriers at any price. Establish what CSI holds, with whom.

### B-09 · Partner pricing structure · `pricing-strategist`
Vadim's sheet quantifies the alliance for the first time: NMS at **$20–95 off published**
across 24 Delta lanes, NMS on AA Central America **$1,580 vs $1,775**, **Bergen at $2,300 on
USA→Europe against $3,430** — the widest spread in the book. Per `§5` model it as deliberate
structure. **Any recommendation raising NMS or Bergen rates goes to Ethan, never into a
general rate proposal.**

---

## Tier 3 — valuable, not yet

### B-10 · Risk register v1 · `legal-risk`
Nothing exists. Candidates already identified: sale auto-terminates the FreightFlow
agreement; no key-person cover on the OMS contractor; liability capped at 12 months' fees
with no data-breach carve-out; customer concentration at 31.3% in the top 10; the unsigned
agreement copy.

### B-11 · The 270 OMS-flagged duplicates · `revops-crm`
The OMS flags them itself with `duplicate_group_id` and `duplicate_sibling_ids` — the hard
part is done. **One already matters: Meierhoffer appears twice with the discount flag set on
one record and not the other.** Merges above 25 records go to Ethan.

### B-12 · Trinidad / POS country rulebook · `compliance`
A live lane with a quote outstanding and a documented consular requirement list already in
hand. A cheap first entry in the country rulebook.

### B-13 · Content for the growing category · `marketing-lead`
*"national mortuary shipping"* is **+25% year over year**; several professional terms are up
50–100%. CSI holds 23.67% impression share. The organic opportunity is probably larger than
the paid one and costs no media. **Gated behind TASK-0022** — instrumentation precedes spend.

### B-14 · Surcharge across all carriers · `finance`
77 of 77 United air waybills carried ~$33 above contracted rate. **Blocked until Donald's
2026-11-04 meeting** establishes whether it is billed through, absorbed, or already in the
quoted rate. Do not start before that answer.

### B-15 · Revenue per account · `finance`
The funeral home table gives booking *volume* per account; it gives no dollars. Account
value, and therefore concentration by revenue rather than by count, needs the QuickBooks
sales-by-customer summary requested from Donald.
