# HANDOFF-sci-unlabelled — data-analyst → revops-crm

**Raised:** 2026-11-18
**Related task:** SCI evidence base for the 2 December 2026 vendor-leader meeting
**Urgency:** WHEN CONVENIENT — not before 2 December, but before the next SCI target list is built
**Status:** OPEN

## What I need

**Tag 37 funeral-home accounts as SCI group members in HubSpot and, if a human can, in the OMS
`funeral_home_group` field.**

`data/derived/sci-unlabelled-locations.csv` — 37 rows, each with `funeral_home_id`, business name,
state, the match tier, and the SCI register location it matched.

You are the only agent that writes to HubSpot (`CLAUDE.md §7.1`), so this is a proposal to you, not
an instruction. The OMS half is manual: agents have no programmatic access (`CLAUDE.md §5`), so if
the group field should be corrected there it is a request to Vadim or the booking desk, not a write.

## Why I need it

These 37 accounts ship with CSI **and** match a location in SCI's own June 2026 active-location
register, on either name + 5-digit ZIP, or a register phone number that belongs to exactly one
location. **None of them is labelled SCI anywhere in CSI's systems.**

The volume is immaterial — **46 bookings across five years** between them, a median of 1. The
account-planning defect is
not:

- A rep working one of these accounts does not know it is a Dignity location, so the conversation
  is pitched as an independent rather than as part of a group CSI already has a corporate
  relationship and a portal pilot with.
- Any SCI-scoped list, report or territory cut built from HubSpot or from the OMS group field
  silently excludes them.
- CSI's published SCI footprint figures understate by 15 locations active in 2026 (38 across the
  whole history). I have reported the figure both
  ways (`reports/sci-relationship-evidence.md` §2 and §5) precisely because the labelling is
  incomplete. Fixing the label removes the need for two columns.

## What I will do with it

Collapse the strict/wide split in `scripts/sci_relationship_evidence.py` to a single definition, so
the next run of the SCI evidence pack produces one footprint number instead of two that need
explaining. The script already reconciles the two and the reconciliation is tested; once the labels
are right the reconciliation becomes a no-op and the output gets simpler.

## When I need it

**Not before 2 December** — do not change the label set while Ethan is working from the current
figures, because the published 123 / 1,198 numbers rest on today's labelling and they tie to
`reports/customer-cohort-analysis.md`.

**Before the next SCI-scoped target list or territory cut is built.** If that is in the FY27 list
work, then before it.

## Caveats you should apply before writing

**Three, and they matter because a wrong group tag on a 23-year-old account is a write nobody can
defend:**

1. **Match tiers are not equal.** 17 of the 37 matched on **both** name+ZIP and a unique register
   phone (`T2_name_zip_and_phone`) — two independent signals, and I would write those without
   further checking. 20 matched on **one** signal only (`T3_single_signal`). I would spot-check the
   single-signal rows against the matched register location name in the CSV before writing.
2. **Shared-phone matches are deliberately absent from this list.** 1,276 rows of SCI's register
   carry the same Houston head-office number, so a shared-phone match is evidence of nothing. 174
   accounts matched that way and are excluded. **Do not add them back.**
3. **The register is June 2026, five months stale.** A name+ZIP match could be a location SCI has
   since divested, or a home SCI acquired after CSI's record was created. A refreshed register from
   Pam (requested in `reports/sci-relationship-evidence.md` §8 item 4) would settle it. If you want
   to wait for that, waiting is defensible.

Per `CLAUDE.md §7.1`, log the before/after values in `reports/` before writing and spot-check a
sample after. 37 records is under the 25-record threshold for merges but these are property updates,
not merges, so the discipline applies rather than the gate.

## What I'll do if I don't get it

The strict/wide split stays in the script and in the report, which is the status quo: both numbers
published, the difference explained, nobody misinformed. The cost is that every SCI figure needs a
sentence of explanation forever, and the 37 accounts keep getting worked as independents. That is a
small, permanent tax rather than a blocker.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
