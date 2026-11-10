# DRAFT — to Claudio and Lucas (Rednodo), on the shipment history export

**Status:** Draft for Ethan. He sends it himself — he has the relationship (`CLAUDE.md §7.1`).

---

## Notes for Ethan — delete before sending

**Why this note is short.** Donald's words were "Claudio or Lucas can walk you thru how to do
that." That could mean they run it, or they show you where to run it. The note is written to
accept either answer rather than presuming, because presuming the wrong one wastes a round trip.

**Four columns on purpose.** It is a query someone can run in minutes. Every extra column is a
reason for it to become a project. The wider booking-level file stays in the engineering ask as a
recurring export; this one is a one-off.

**The §7.2 line is not optional and not about trust.** It goes in every request for operational
data, every time, to anyone. Easier to leave names out of a query than to strip them afterwards.

**What this unblocks, so you can judge how hard to push:** churn, reactivation, frequency,
lane and corridor volume, and account-level anything. It is the single largest blocked dependency
in the repo and four agents are waiting on it.

**First query when it lands** is Donald's own claim — Bergen growing, Ortiz declining. It is
specific and falsifiable, and it tells us whether an experienced read of this business can be
trusted where the data is thin. That matters well beyond this one question.

---

## The note

**Subject:** Shipment history pull — since 2022

Hi Claudio, Lucas,

Hope you're both well.

I'm trying to answer a question about our customer base that I can't currently get at, and Donald
mentioned you two would be the people to point me in the right direction.

**What I'm after:** every shipment in the old system since the start of 2022, with four columns:

- `booking_id`
- `shipping_funeral_home_id`
- `flight_date`
- `status`

If a booking has no funeral home attached, keep the row and leave the ID blank — those turn out to
be interesting in their own right.

**Happy either way on how we do this.** If it's quicker for one of you to just run it and send a
CSV, that's great. If it's easier to show me or Donald where to pull it ourselves, that works too
and probably saves you the next five times I ask. Breaking it into a few files by year is
completely fine.

**One thing to flag:** please no decedent or family name fields — just the four columns above.
Easier to leave them out of the query than to strip them afterwards.

**Why I'm asking.** Right now I can tell you our monthly totals, but I can't tell you whether a
given funeral home is active, lapsed or gone, how many we lose in a year, or whether the ones who
come back ship more than the ones who don't. Which means I can't say whether our flat volume is a
retention problem or a new-client problem — and those call for completely different responses.

No rush on timing, but it's probably the most useful thing anyone could hand me right now.

Thanks both,

Ethan
