# DRAFT — to Alex, Kyri, Donald and Cheryl: IMS Army rates, for validation

**Status:** Draft for Ethan. He sends it (`CLAUDE.md §7.1`).
**Attach:** `data/derived/ims-army-published-rates-2026-11-22.xlsx`

---

## Notes for Ethan — delete before sending

**The point of this email is that nothing goes to Paul until three sources agree.** Our
OMS pull, Donald's invoicing data, and Alex's own run. The email says so explicitly at the
top and again at the bottom, because the Tuesday deadline creates pressure to send what we
have.

**The technical section is deliberately detailed.** Alex and Kyri can only check our work if
they can see it, and the two things most likely to be wrong — the bill-to rule and the zone
resolution — are both judgement calls we made from reading their code rather than from
documentation.

**The "varies per city" finding is the one to lead with.** It is 88 of 286 shipments, all
Borthwick, all American casket out of Honolulu. That is a gap in CSI's own rate card, not a
data problem, and it is the single thing standing between this sheet and being complete.

**No rate is set or changed anywhere** (`§7.6`). No decedent or family data was read or
written at any point (`§7.2`) — the deceased table carries airport columns and was
deliberately not joined.

---

## The note

**Subject:** IMS Army rates — pulled, needs validating before it goes out

All,

Paul at IMS asked for the published rates on the shipments we handle out of ten funeral
homes that feed their Army contract. They're renewing and want to present competitively.
Cheryl has been chasing this; I've now pulled it.

**Before anything else: I don't want to send this to Paul until we've checked it against a
second source.** We'd be handing a partner a rate sheet for a federal bid. If it's wrong, it
is wrong in a room we don't control. Asks for each of you below.

---

**What we pulled**

286 shipments, 500 flight legs, booked between 5 January and 19 November 2026. These are
only the shipments we **billed to IMS** — those ten homes also ship with us directly and
through other partners, and that volume is excluded.

Across 176 distinct lanes. Borthwick in Honolulu is by far the largest at 133 of the 286;
John A Gentleman is 51.

**179 of the 286 now carry a published rate. 107 do not**, and every one of those says why on
its own row.

---

**Alex, Kyri — how we did it, so you can tell me where it's wrong**

Four steps, and I think steps 2 and 3 are where a mistake would hide.

1. **Which shipments count as IMS's.** We took bill-to as
   `COALESCE(csi_new_shipper_to_invoice.shipper_id, csi_booking_shipper_information.shipper_funeral_home_id)`
   and filtered to IMS, funeral home 2767. That rule came from reading
   `quickbooks_service.py`. **If that isn't how invoicing actually resolves the bill-to,
   everything downstream is the wrong population.**

2. **What lane each shipment flew.** Legs come from `csi_booking_domestic_airline` and
   `csi_booking_inter_airline`, with origin and destination joined to `csi_iata_codes`. We
   deliberately ignored `leg_type` and ordered the legs by **connectivity** instead — chain
   each leg's destination to the next leg's origin — because the leg id only sorts within a
   booking and some domestic flights are stored as international legs. Booking 43730
   (DEN–BHM) and 45029 (HNL–DFW–DCA) are both filed as international. The lane is then the
   first leg's origin to the last leg's destination.

3. **Which carrier.** We took the carrier from the **flight-number prefix**, not the airline
   text field, because that field has mixed case, trailing spaces and is blank on 8 legs.
   That turned up a conflict worth a look: **booking 43730 has airline "AMERICAN AIRLINES"
   against flight number WN3073**, which is a Southwest number.

4. **The rate.** We learned the hard way that the four US carriers price **zone to zone, not
   airport to airport**, that each carrier keeps its own zone column on the airport row, and
   that rates split by shipment type. So for each lane end we resolve, in order: an exact
   airport row, then the US state row, then that carrier's own zone — matching
   case-insensitively, since three United rows read "MIdwest". American's Hawaii and Puerto
   Rico rates are state rows rather than zones, which took a while to find.

**The specific things I'd like you to check:**

- **Is the bill-to rule right?** Everything rests on it.
- **Is the resolution order right** — airport, then state, then zone? Or does rate search
  try them in a different order?
- **`rate_id` is not unique.** It repeats with identical values, so we keyed on the row's
  values instead and dropped 5 exact duplicates from 632 rows. Is that nullable, repeating
  id deliberate?

---

**The thing that blocks a third of this: "varies per city"**

**88 of the 286 shipments cannot be priced**, and they are all the same thing: **Borthwick,
casket, out of Honolulu, on American.** American's published rate for casket from Hawaii is
not a number in our card — it is the literal text **"varies per city"**, one string standing
in for every destination.

Delta has proper figures on the same lanes — HNL to Central is $1,198.30, to Northeast
$1,334.12. American's rows simply were never filled in.

**So two thirds of Borthwick's shipments go to IMS blank**, and Borthwick is both our largest
origin here and one of the two homes Paul flagged as important.

**Alex, Kyri — do the real American Hawaii rates exist somewhere we didn't look?**
`csi_contracted_rates`, `csi_customer_special_rates` or `csi_bundled_rates`? If they genuinely
don't exist anywhere, that's a gap in the card worth fixing regardless of IMS.

**Two smaller ones while you're in there:** United publishes **casket rates only** — no ashes,
no infant — which affects far more than this request. And **5 of the 286 bookings have no
shipment type recorded** at all; they're priced as nothing rather than guessed.

---

**Donald — two asks**

**First, would you run the same thing from your side?** What we actually invoiced IMS for
these 286 bookings. I want to see our OMS pull and your invoicing data land on the same
population and the same lanes before anything goes out. If the counts differ, I'd rather find
out now than after Paul has it.

**Second, there's a rate decision only you should make.** Our card currently holds **two or
more active rates for the same carrier, route and shipment type in 106 combinations** —
American Central to Central casket is live at both $632.19 and $637.19. Nothing in the table
says which supersedes the other, so the sheet shows both. **That affects 64 of the 179 priced
rows.** A rate sheet going to a partner shouldn't carry two prices. Either you rule on which
is current, or we re-pull with the last-updated timestamp and take the most recent — but I'd
rather you looked, because this smells like old rates left active rather than a convention.

There's a **Rate conflicts** tab listing every one.

---

**Cheryl — please hold**

I know Paul wanted this Tuesday. **I'd rather be a few days late and right.** Once Alex or
Donald confirms the population and we've settled the duplicate rates, it goes out the same
day.

One thing worth knowing when you do send it: a third of it will be blank unless we find the
Hawaii rates, and the blanks are concentrated in Borthwick. Better to tell Paul that up front
than let him find it.

---

**On the sheet itself.** Five tabs: a Read me explaining the method in plain terms, the
shipments, a by-lane view, a by-funeral-home summary, and the rate conflicts. Every unpriced
row states its reason. Nothing has been estimated to fill a gap — where we don't have a
number, there's no number.

Thanks all.

Ethan
