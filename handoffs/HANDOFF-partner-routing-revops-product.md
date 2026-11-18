# HANDOFF-partner-routing — data-analyst → revops-crm, product, pm-orchestrator

**Raised:** 2026-11-18
**Related task:** correction to `reports/customer-cohort-analysis.md`
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need

**Three separate things, from three owners.**

### 1. revops-crm — check whether partner-routed homes were written into HubSpot segments

`reports/fy27-target-lists.md` and `data/derived/fy27-seg*.csv` were built on the
population this correction contaminates. **Segment 4 (net-new) and segment 1 (one-time)
are the exposed ones.** I need to know whether any partner-routed home has been written
into a HubSpot segment, list, or lifecycle stage that could put it in front of a rep or
into a sequence.

Nothing has gone out — §7.1 gates sends — so this is containable. But a partner's customer
sitting in a prospecting segment will eventually be worked by someone.

**I will send you the exact `funeral_home_id` list once the manifest lands.** What I need
from you now is whether those segments have been populated in HubSpot yet, and if so
whether anything downstream (a list, a workflow, an owner assignment) reads from them.

### 2. product — add bill-to to the standing booking-level export

**`reports/oms-export-spec.md` is missing the single field that makes every CSI account
metric correct.** Every churn, retention, acquisition, cohort and account-value figure CSI
has ever published is wrong without it, including all of M-12 through M-17 in
`context/metric-definitions.md`.

The field, as the invoicing code computes it:

```sql
COALESCE(csi_new_shipper_to_invoice.shipper_id,
         csi_booking_shipper_information.shipper_funeral_home_id) AS bill_to_funeral_home_id
```

Source: `backend/quickbooks_service.py`. The other session found
`csi_new_shipper_to_invoice` by reading that file — **it was not on anyone's list of
tables**, which is worth noting in its own right about how much of CSI's commercial logic
is only discoverable in code.

**For the Monday engineering ask**, ranked high, stated as CSI's read and not a ruling:
this is **new work, not a bug** — the export spec never asked for the field. One column on
an export that already exists. It unblocks data, gtm, sales, marketing, revops and corpdev
simultaneously, which by the §9.6 ranking rule should put it near the top.

### 3. pm-orchestrator — two documents to change, one gap to close

- **`CLAUDE.md` §4.1** — add partner-routed booking identification to the established
  list. §4.3 can lose nothing yet; the per-home manifest is still outstanding.
- **`CLAUDE.md` §4.3** — the "shipment-level records" blocker should note that account
  metrics additionally require bill-to, not just `funeral_home_id` + `booking_date`. The
  two-column export ranked #1 in `metric-definitions.md` would **not** have been enough.
  Three columns, not two.
- **`CLAUDE.md` §7.1, standing authority 4** — segments exclude "freemail, chat-origin,
  non-funeral-home domains, and receiving homes." **Partner-routed originating homes are a
  fifth category and are not named.** This is a gap in the standing authority rather than
  an agent error, and it needs Ethan to close it. I am not proposing the wording; the
  decision about how CSI treats a partner's customer in its own CRM is his and Cheryl's.

**Do not merge the brain proposal from the 2026-11-12 cohort report** — it carries the 411
figure and the retention framing, both withdrawn.

## Why I need it

Without (2) this correction has to be redone by hand every quarter from a database nobody
in the agent team can reach. With it, it is a column.

## What I will do with it

Re-baseline M-12 through M-17 against bill-to and publish the corrected definitions,
including the new **M-13a** exclusion rule already stated in the correction block.

## When I need it

(1) this week — containment. (2) in Monday's engineering ask. (3) in Monday's decision
document.

## What I'll do if I don't get it

(1) I will assume the segments are populated and send the exclusion list as a removal
request rather than a filter. (2) I will keep running this from relayed aggregates, which
means every quarter's correction depends on another session having database access and is
not reproducible from this repo — I will label the figures accordingly. (3) The §7.1 gap
stays open and I will flag it again on the next segment build rather than let it pass
silently.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
