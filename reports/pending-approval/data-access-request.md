# DRAFT — for Ethan's approval before sending

**To:** Kyri, Alex
**From:** Ethan
**Re:** Read-only reporting access + three data fixes
**Status:** Draft. Not sent. `CLAUDE.md §7.1`.

---

> ## ⚠️ SUPERSEDED IN PART — read this before using anything below
>
> **Three premises in this draft are wrong.** Corrected by Ethan 2026-11-02. `product`
> is producing the authoritative version as TASK-0003
> (`reports/pending-approval/engineering-ask-2026-45.md`). Use that one. This file is
> kept for the clause research and the framing notes, not as the ask.
>
> | This draft says | Actually true |
> |---|---|
> | Booking-level detail may already export from Flight Confirmation / Ready to Invoice / Collect Shipments, so the ask might be a permission request | **None of those pages has export functionality.** The booking-level export is a genuine build — a Change Order, not a permission |
> | International contracted rates may be a permission Vadim can grant | **Neither Ethan nor Vadim holds that access. Kyri and Alex do.** It stays on this ask. Separately, Vadim holds the current rate sheets themselves — that request went to him directly |
> | Booking duration data may be an operations question | **Whether the system captures it is a Kyri/Alex question.** CSI is starting to be able to track it; nobody is sure it exists yet |
>
> **Also decided:** per the Week 45 plan §8, **drop item 5** (the read-only Postgres role).
> The FreightFlow agreement makes it a Change Order, and trading the easy win to win that
> argument is a bad trade. Items 1–3 go as Error Response Requests inside contract scope;
> the **nightly export is the one feature ask**.
>
> **Knock-on for the plan:** the engineering ask can no longer shrink. It is larger and
> more certain than when the plan was written, which makes the Friday test — one
> prioritized ask leaving the building — matter more, not less.

---

## Context for Ethan (delete before sending)

This asks for three things, deliberately ordered cheapest-to-hardest so the easy wins
aren't held hostage to the access conversation:

1. **Three bug fixes** — small, concrete, and genuinely broken. These stand on their own
   merit and don't require anyone to agree about AI access.
2. **A nightly export job** — no new access surface at all. This is the one I'd push
   hardest for, because it solves the recurring problem permanently.
3. **A read-only reporting role** — the real ask, framed to address their actual
   objection rather than argue with it.

The framing that matters: Kyri and Alex's concern is **admin access and write
capability**, which is correct and which none of this requires. Don't lead with "so
Claude can read it" — lead with "so reporting doesn't depend on someone manually
exporting CSVs." Both are true; the second is the one that makes it their problem too.

---

## The note

Hi both,

Three asks, smallest first. The first three are bugs we found in the rate data this
week; the last two are about making reporting sustainable.

### 1. Duplicate rows in the rates table

The Rates Reference says the unique key on a rate is
`airline + origin_type + origin + destination_type + destination + rate_type`, and that
the importer blocks duplicates.

In the current export that isn't holding. **181 key combinations appear more than once —
487 rows in total — and 133 of those have *conflicting* published rates.** Example:
American Airlines, zone West → zone West, rate_type `flat` appears three times, at
$207.19, $615.94, and $207.19 again.

Two questions:
- Is the uniqueness constraint actually enforced at the database level, or only in the
  bulk-import validator? If it's only in the validator, rows added through the UI or
  carried over from the legacy system would bypass it.
- When a booking prices against a lane with two conflicting rates, which one wins?

This matters beyond tidiness: we can't tell what a booking would actually be charged on
133 lanes, which makes any margin or pricing analysis unreliable there.

### 2. `shipment_rate_type` is empty in the rates export

Every one of the 6,919 rows in the rates export has a blank `shipment_rate_type`, while
the contracted-rates export has it populated (all `Casket`).

That means we can't tell a casket rate from a cremated-remains rate in the published
table — and those are very different prices on the same lane. It's almost certainly why
we're seeing what look like duplicates in item 1.

If the field exists on the record and is just missing from the export, adding it to the
export is the fix. If it isn't on the record, that's a bigger conversation.

Concretely: populating this would take our usable margin sample from 33 lanes to roughly
129.

### 3. International contracted rates

The contracted-rates export covers 156 lanes — all American, Delta, United and Southwest.
There are no contracted rates for any international carrier: IAG alone has 5,565 lanes
with published rates and no cost, plus Emirates, Lufthansa, Volaris, Avianca, Copa,
Korean, Viva and IBC.

International is where we make our best margin, and it's the half of the book where we
can't see cost at all. I'm asking Vadim whether these live outside the system — the
Rates Reference mentions "Vadim's rate sheet" for the Volaris MIA → Central America
bundle, so some may never have been loaded. If they're in the system and just restricted,
can they be included in the contracted export?

### 4. A nightly export job to Google Drive

Rather than someone manually pulling CSVs every time we need to look at something, could
we schedule a nightly job that drops a standard set of exports into a Drive folder?

No new access, no live connection, no API — just a cron job writing files we already
generate by hand.

The set I'd want:
- Bookings (booking-level: ID, booking date, landed date, shipping funeral home ID,
  receiving funeral home, origin gateway, destination airport and country,
  domestic/international flag, carrier, AWB, revenue, carrier cost, accessorials, status,
  cancellation and rebooking flags)
- Funeral home records
- Rates — published, contracted, special, bundled
- Airline invoice audit / discrepancy report
- Analytics monthly summary

**Important:** bookings must be exported with decedent and family fields stripped **at
the query**, not removed afterward. We don't want that data leaving the system at all.

### 5. Read-only reporting access

The bigger ask, and I want to be precise about what I'm *not* asking for: no admin
access, no write capability, no access to the application itself.

What I'm asking for is a **separate Postgres role with SELECT granted on a defined set of
reporting views** — not on base tables, and not including decedent or family columns.
Something like:

```sql
CREATE ROLE csi_reporting LOGIN PASSWORD '...';
GRANT USAGE ON SCHEMA reporting TO csi_reporting;
GRANT SELECT ON ALL TABLES IN SCHEMA reporting TO csi_reporting;
-- no INSERT, UPDATE, DELETE, no DDL, no access to public schema
```

The views would exclude PII by construction, so the credential can't reach it even if
someone wanted to. Connection limited to a specific IP or through a bastion, whatever
fits how you run things.

I understand the concern about agents hitting the system, and I think it's the right
instinct — I don't want write access anywhere near this either. A read-only role on
PII-free views is a different thing: it's the standard way a reporting layer gets built,
it can't modify anything, and it can be revoked in one statement if it ever looks wrong.

If item 4 lands, item 5 becomes less urgent — so if you only have bandwidth for one,
do 4.

Happy to talk through any of it.

Ethan

---

## Notes for Ethan (delete before sending)

- **Expect pushback on 5, not on 1–3.** Items 1–3 are bugs; nobody argues with bugs.
- **Item 4 is the real win.** It removes the manual export loop permanently and asks for
  nothing new security-wise. If they push back on it, the objection is about effort, not
  risk — and a cron job writing five CSVs is a couple of hours.
- **If they say no to 5:** accept it and take 4. Don't trade the easy win to win the
  argument. We can revisit once there's a track record.
- **Don't offer AWS access.** It's far broader than needed, it would alarm them, and it
  gives infrastructure rather than data.
- From the admin dashboard, **Rate Sheets** already notes that "contracted carrier costs
  are restricted to a smaller admin set" — so the permission model you're asking them to
  extend already exists. Worth mentioning if they're receptive.