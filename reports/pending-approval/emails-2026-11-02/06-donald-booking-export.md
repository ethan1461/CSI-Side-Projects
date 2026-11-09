# DRAFT — to Donald, on the booking export

**Status:** Draft for Ethan. Not sent (`CLAUDE.md §7.1`).

---

## Notes for Ethan — delete before sending

**Why this goes to Donald rather than Kyri and Alex.** You can pull revenue data but not shipment records. Donald's access is wider, and if he can run this it costs nothing and arrives this week rather than whenever a Change Order gets agreed. **It is also the same request as item 1 of the engineering ask** — so if Donald can produce it, that item closes before it is sent.

**Keep the column list short on purpose.** Four columns is a query someone can run in minutes. The longer booking-level file stays in the engineering ask as an export-button request, because that one is recurring and this one is not.

**Note the §7.2 line at the end.** It is there because it needs to be in writing every time, not because Donald would get it wrong.

---

## The note

**Subject:** Can you pull a booking history export?

Hi Donald,

Quick one — I'm trying to answer a question I can't currently get at, and I think you might be able to run the export.

**What I'm after:** every booking in the system since the start of 2021, with just four columns:

- `booking_id`
- `shipping_funeral_home_id`
- `flight_date`
- `status`

If a booking has no funeral home attached, keep the row and leave the ID blank — those are interesting in their own right.

**Why it matters.** Right now I can tell you our monthly totals but I can't tell you whether a given funeral home is active, lapsed or gone, how many we lose a year, or whether the ones who come back ship more than the ones who don't.

Which means **I can't say whether our flat volume is a retention problem or an acquisition problem** — and those need completely different responses. If we're losing customers as fast as we win them, hiring more salespeople doesn't fix it. If we're just not winning enough new ones, it does.

It also lets us start grouping customers properly so we can treat our best accounts differently from the ones who used us once.

**On format:** a CSV is ideal. If it's easier to break it into a few exports by year, that works fine. And if the system won't give it to you either, tell me and I'll put it to Kyri and Alex — I just didn't want to spend a Change Order on something we might already be able to run.

**One thing to flag:** please no decedent or family name fields in the export — just the four columns above. Easier to leave them out of the query than to strip them afterwards.

Thanks — this is probably the single most useful thing anyone could hand me right now.

Ethan
