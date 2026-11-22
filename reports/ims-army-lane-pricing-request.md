# The IMS Army lane request — what it actually is, and the spec to pull it

**Date:** 2026-11-22 · **For:** Ethan, Cheryl, Donald · **Due:** IMS needs it Tuesday
**Requested by:** Paul Prikos (IMS) via Cheryl, 2026-11-20. Alex asked what is needed.

---

## Lead finding: these are not prospective lanes. CSI already runs them.

Paul's ten "Top 10 Funeral Homes (ARMY)" were matched against
`data/derived/partner-billed-homes-manifest-20261118.csv`. **All ten are existing CSI
accounts, and nine of the ten are billed predominantly to IMS.**

| Funeral home | Partner-billed | Self-billed | Main partner |
|---|---:|---:|---|
| Borthwick Mortuary (SCI #4873) ****** | 486 | 15 | MIXED |
| John A Gentleman Mortuary ****** | 287 | 28 | IMS |
| LaFayette Funeral Home | 97 | 10 | IMS |
| Weeks Dryer Mortuary | 95 | 5 | IMS |
| Crotty Funeral Home & Cremation | 69 | 4 | IMS |
| McReynolds Nave Larson | 48 | 4 | IMS |
| The Springs Funeral Services | 43 | **108** | IMS |
| Hart and Bruce Funeral Home | 22 | 1 | IMS |
| D W Brooks Funeral Home | 14 | 0 | IMS |
| Dearly Beloved Mortuary Services | 11 | 0 | IMS |
| **Total partner-billed** | **1,172** | 175 | |

*(An eleventh name, "Hot Springs F.H" — 1 partner booking, NMS — matched on the word
"Springs" and is not Paul's "Springs (Colorado)". Excluded.)*

**So the stakes are not IMS's alone.** 1,172 bookings in the manifest window reach CSI
through this partner on these ten homes. **If IMS loses the Army renewal, CSI loses that
volume** — it does not transfer to CSI, it transfers to whoever wins. That reframes a
Tuesday favour into protecting a material block of CSI's own book.

**I have not annualised it and will not guess.** The manifest spans 2022–2026 and the window
differs per home. The pull below returns the real figure.

**Two notes on the table.** Borthwick is an **SCI location** and the two homes Paul starred
as important are the two largest — he knows where his volume is. **The Springs is the only
one CSI bills directly more often than IMS does** (108 vs 43), and it is tagged Foundation
Partners, which sits on the `okrs-2026-cro.md` exclusion list; worth not treating it as an
ordinary IMS lane.

---

## DECIDED 2026-11-22 by Ethan

> **Is CSI bidding the same Army vehicle?** — *"No."* So this is ordinary supplier-to-bidder
> quoting. The `§7.5` concern below is closed.
>
> **Which rate?** — **SUPERSEDED. Ethan, later on 2026-11-22: *"We want to show PUBLISHED
> rate, not discount."*** The sheet carries rate-card rates, not partner or discount pricing.
>
> My earlier recommendation was the rates IMS pays today. Ethan has decided otherwise and
> that is the instruction. **It is also the more defensible choice on a point I had not
> weighted properly:** a discount rate written into a federal bid document can circulate
> well beyond the bid, and partner pricing visible to the market resets expectations across
> the whole partner tier. Published rate exposes nothing.
>
> **The consequence to watch** stands either way: IMS prices this bid off CSI's rate card,
> which is the highest number CSI quotes. If they lose on price, the 1,172 bookings below
> are what leaves with them. Worth revisiting deliberately after the bid rather than
> discovering it in the 2027 numbers.
>
> **Scope also clarified:** the ten homes are **origins**. The pull is every shipment
> *from* those homes over the last six months, not lanes into them.

**Donald still confirms the rate basis before the sheet leaves** — he owns margin, and the
lanes may have moved. That ask is in `reports/pending-approval/emails-2026-11-22/04-cheryl-donald-asks.md`.

**Steps 1 and 2 of the sequence below are now closed. Alex can fill the rate column.**

---

## The decision that had to come before the pull — retained for the record

Cheryl's concern — *"want to be confident we are using the right rates"* — is the whole
problem, and **it is not a data question. It is a pricing decision for Ethan, Cheryl and
Donald** (`CLAUDE.md §7.6`: no agent changes or sets a live rate; `§7.1`: any pricing figure
shown externally is approval-gated).

CSI holds at least three different prices per lane:

| | What it is | Appropriate here? |
|---|---|---|
| **Published rate** | What a funeral home pays off the rate card | **No** — IMS is partner tier, and quoting this makes IMS uncompetitive on a bid CSI benefits from winning |
| **`discount_rate`** | A second *customer* price, not CSI's cost (`reports/carrier-margin-resolved.md`) | Possibly — this is the partner-tier price |
| **`contracted_rate`** | CSI's own cost from the carrier | **Never leaves CSI.** Not a quote |

**Someone has to say which price IMS is quoted, and whether it is the rate they pay today or
a sharpened one for the bid.** Both directions cost money: the published rate risks IMS
losing a contract that carries 1,172 of CSI's bookings; a sharpened rate is a commitment CSI
has to honour for the contract term, on lanes where **cost data does not exist for 93% of the
published lane book** (`CLAUDE.md §4.3`).

**Recommendation:** quote the rates IMS pays today, flagged as current and subject to carrier
confirmation, and treat any sharpening as a separate decision Donald prices properly rather
than one made under a Tuesday deadline.

---

## One thing to confirm before anything goes out

**Is CSI bidding, or planning to bid, this same Army vehicle?**

`context/brain/initiatives/federal-contracting.md` records that CSI is pursuing federal work,
that **IMS is "the dominant federal incumbent,"** and the standing instruction **"do not
position against IMS."** The main tracked recompete there is a Navy IDIQ, not this, so the
answer is probably no.

If the answer is no, this is ordinary supplier-to-bidder quoting and entirely routine. **If
the answer is yes, it is not** — supplying rates to a rival bidder on a contract you are also
chasing is a different conversation and one for counsel, not for a Tuesday turnaround
(`§7.5`). One sentence from you closes this; I am raising it because nobody else in the chain
is positioned to notice.

---

## The spec for Alex

Alex asked what is needed. Not a shipment count — **a lane-level price sheet**.

**One row per origin–destination pair per funeral home**, covering the last 24 months:

| Column | Notes |
|---|---|
| `funeral_home` | business name only |
| `funeral_home_id` | OMS id |
| `origin_airport` | IATA |
| `destination_airport` | IATA |
| `carrier` | |
| `shipments_24mo` | the count Paul will also want |
| `last_shipment_date` | staleness check on the rate |
| `rate_quoted` | **whichever rate the decision above lands on — not the cost** |
| `rate_basis` | which rate card the figure came from, so it is auditable |

**Hard requirements on the pull (`CLAUDE.md §7.2`):**

- **No decedent names, no family names, no addresses.** Drop them at the query, not after.
  OMS flight-confirmation and ready-to-invoice lists display decedent names by design, and
  pickup lists carry `Deceased Name` — so this must be aggregated to the lane, never a
  shipment list.
- **Aggregate.** "14 shipments on JFK→HNL," never fourteen rows that could be matched back.
- **The file is checked before it leaves CSI.** A sheet going to a partner for a federal bid
  is exactly the handoff `§7.2` names as a checkpoint.

**Also worth asking Alex:** whether origin and destination are reliably populated. The
current export has no origin/destination columns at all, which is a known gap
(`CLAUDE.md §4.3`) and the reason CSI cannot do lane margin today. **If they exist in the
system and simply were not exported, that is worth knowing far beyond this request** — it
unblocks lane profitability for pricing-strategist and finance both.

---

## Recommended sequence

| # | Step | Owner |
|---|---|---|
| 1 | ~~Confirm CSI is not bidding the same vehicle~~ **DONE — not bidding** | Ethan |
| 2 | ~~Decide which rate IMS is quoted~~ **DONE — PUBLISHED rate** (Ethan, 2026-11-22) | Ethan |
| 3 | ~~Pull the lane sheet~~ **DONE for shipments** — `scripts/build_ims_army_lane_sheet.py`, 190 shipments from the ten origins since 2026-05-26. Origin/destination/carrier columns still need filling by Booking ID | pm-orchestrator / Alex |
| 4 | Check the file for decedent/family data before it leaves | legal-risk checkpoint |
| 5 | Send to Paul | Cheryl |

**Steps 1 and 2 are closed.** Alex can build and fill the sheet. Donald's confirmation of
the rate basis (step 4a) happens before it leaves CSI, alongside the `§7.2` data check.
