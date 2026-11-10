# RESUME — HubSpot work, blocked on connector, 2026-11-10

**For the next session.** This session lost the HubSpot connector mid-run. Connectors load at
session start, so this work cannot finish here. Everything below is staged and verified; nothing
needs re-deriving.

## Do these in order

### 1. Finish the owner assignment — 621 records

`reports/fy27-owner-assignment-log.csv` marks every row `WRITTEN` / `PENDING` / `SKIPPED`.

- **170 WRITTEN** already (Seg 1, batches 1–17). Leave them.
- **621 PENDING** — set `hubspot_owner_id` from the `new_owner` column, batches of 10.
  Re-writing an already-written row is harmless, so a full re-run is safe if simpler.
- **5 SKIPPED** — no state, deliberately unowned. Do not guess a region for them.

Owner IDs: **Otto Briede 102528265**, **Stacy Cotty 102528264**. Resolve with `search_owners`
rather than trusting these if anything looks off.

The rule, already applied and not to be re-litigated: Midwest→Otto, West→Stacy, and the remaining
Northeast/South pool ordered by `call_rank` alternating from Otto at position 1, restarting
separately per segment. Ethan ruled this on 2026-11-10.

**Then run the read-back that is still owed** — a sample across both reps and both segments,
recorded in `reports/fy27-owner-assignment.md`. Three pilot records were checked; that is not
enough and the report says so.

### 2. The four segment lists — check the scope first

The previous attempt failed on a missing connector scope: `cms.membership.access_groups.write`.

**Before retrying, establish whether that scope now exists.** If it does, build the four static
lists from the member files, named as planned in `reports/fy27-lists-in-hubspot.md`.

**If it does not** — likely, since it is a Content Hub feature CSI may not subscribe to —
**do not keep trying.** Switch to the property approach, which Ethan has already been briefed on:

- Ethan creates a company property `fy27_segment` (the connector cannot create properties).
- Populate it from the member files via the ordinary record-write path, which works.
- Values: `one-time`, `churned`, `enterprise`, `net-new`.
- Segments then become a saved view filtered on property + owner, which is better than a static
  list anyway: it is visible on the record, it survives, and it does not silently go stale.

### 3. Pick up the NFDA handoff

`handoffs/HANDOFF-nfda-2026-contacts-revops-crm.md` — create eight NFDA 2026 contacts with source
and owner. It had not landed when revops-crm last ran, so it was correctly skipped. None of the
eight exists in HubSpot as of 2026-11-10. **No sequences, no enrolment.**

## State as of this session's end

- **2,306 Companies.** 2,305 from the OMS build, all carrying distinct `oms_funeral_home_id`;
  one extra ("Return Home", no OMS id, owned by Otto) that predates nothing and is most likely
  ordinary CRM use. Left alone.
- **505 contact→company associations**, verified by query.
- Lifecycle 2,276 customer / 30 lead. `csi_partner_tier` true on 18.
- Join rates: Seg 1 474/474, Seg 2 322/322, Seg 3 249/320, Seg 4 18/5,709. The two shortfalls are
  never-booked records that were deliberately excluded from the account layer — expected, not a
  defect.

## Still Ethan's, not an agent's

- Whether to create ~5,691 Companies for never-booked records, or work Segment 4 from the CSV.
  **Recommendation on file: work it from the CSV** — highest cost per booking, CAC unmeasurable.
- The 20-call diagnostic on Segment 1: 259 of the 474 are held pending it.
- Segment 3 is Ethan-gated end to end. No outreach naming SCI, Foundation Partners, Carriage or
  Northstar.
