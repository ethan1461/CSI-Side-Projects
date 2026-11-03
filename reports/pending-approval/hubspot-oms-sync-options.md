# HubSpot ↔ OMS database — keeping them in sync

**DRAFT for Ethan, to share with Kyri.** Not sent (`CLAUDE.md §7.1`).
**Date:** 2026-11-03 · **Prompted by:** Kyri, 2026-11-02 — *"Does Hubspot have any tools to make sure things stay in sync?"* and *"I gotta imagine other companies have this problem… where they have their own canonical DB of customers and don't want it to split between quickbooks, IT, Hubspot, etc."*
**Confidence:** High on the architecture. **Medium on vendor pricing** — every figure below came from third-party comparison sites that disagree with each other, and each is flagged. Confirm on the vendors' own pages before committing to anything.

---

## The answer

**Kyri is right, and the fix is simpler than a two-way sync: don't build one.**

Other companies do have this problem, and the settled answer is not bidirectional sync. It is **one-way sync with field-level ownership** — every field has exactly one system allowed to write it, data flows in one direction only, and nothing ever round-trips.

For CSI that means:

| | Owns | Flows |
|---|---|---|
| **OMS database** | Who the funeral home is, and everything they've ever done — identity, address, booking history, lane and carrier mix, discount eligibility, group membership | **→ into HubSpot, one way** |
| **HubSpot** | Everything that happened *between CSI and a human* — calls, emails, meetings, sequence membership, deal stage, owner, notes | **Stays in HubSpot. Never written back** |

**Nothing is ever written in both places**, so there is nothing to diverge and no conflict resolution to design. The "last-writer-wins" and update-loop problems the integration vendors write about only exist if you choose two-way, and CSI has no reason to.

**Kyri's instinct — "that will always just query the ground truth DB so that'll always be right" — holds completely for the richer funeral home page he described.** That page should query the database directly, not HubSpot. The sync below exists only so a salesperson sees booking history inside the tool they work in all day.

---

## Why this shape, specifically

The thing that makes CSI's case easy is that **the two systems want different data and barely overlap.**

- The OMS will never know that Otto called a funeral director on Tuesday.
- HubSpot will never know that funeral home #8814 shipped 23 caskets to Santo Domingo.

The only genuinely shared field is the **identity** of the funeral home — name, address, phone — and the database should win on all of it, because that is where the record is created when a booking happens.

So the hard question in most CRM integrations ("who wins when both change?") doesn't arise. **It is a reporting sync, not a data merge.**

---

## What the account layer looks like

Use HubSpot's **standard Company object**, not a custom object.

Two reasons, and the second is the one that matters: custom objects need HubSpot **Enterprise** ([multiple sources agree](https://www.meticulosity.com/blog/do-you-need-hubspot-enterprise-for-custom-objects), and CSI's tier needs confirming) — but even on Enterprise it would be the wrong call, because lists, sequences, reporting and the association model all work natively against Companies and support custom objects more thinly. A funeral home *is* a company. Model it as one.

**Fields synced from the database (read-only in HubSpot, locked):**

`funeral_home_id` ← the join key, and the most important field in the whole design
`name` · `address` · `city` · `state` · `country` · `phone`
`booking_count` · `first_booking_date` · `last_booking_date`
`is_discount_eligible` · `funeral_home_group` · `is_shipper`

**Fields HubSpot owns (never written back):**

owner · lifecycle stage · lead status · all activity and logged calls · sequence membership · deals · notes

**The one rule that makes it work:** the synced fields are set read-only in HubSpot's property settings, so a salesperson cannot overwrite a booking count by hand. That is what actually prevents divergence — not the sync mechanism.

---

## The options, cheapest first

### Option A — Kyri and Alex push from the OMS *(recommended)*

A scheduled job on CSI's side reads the funeral home table and upserts into HubSpot via the CRM API, keyed on `funeral_home_id`. Nightly is ample; booking counts do not need to be real-time.

- **Cost:** engineering time only. No subscription, ever.
- **Scale:** 18,876 records is small. HubSpot's batch endpoints handle 100 records per call, so a full sync is ~190 calls, and a daily delta would be a few dozen.
- **Why it suits CSI:** it is one scheduled job writing one object. Kyri said *"no need to re-invent a CRM from scratch"* — this isn't that. It is an export with an API call on the end, and it reuses whatever the nightly booking export job becomes.
- **Risk:** it is custom code CSI owns and must maintain. Small, but real.

### Option B — Reverse ETL (Hightouch, or Census, now Fivetran)

Purpose-built tools for exactly this: point at a database, map fields, sync to HubSpot, with scheduling, retries and error handling solved.

- **Cost:** genuinely unclear. Third-party sources put Hightouch anywhere from **a free tier** to **$450/mo** to **$1,000/mo** for production ([CostBench](https://costbench.com/stats/reverse-etl-pricing-2026/), [a HubSpot-specific guide](https://datatoolindex.pages.dev/use-cases/best-reverse-etl-for-hubspot-sync/)). **Verify directly.**
- **Watch out:** standalone **Census accounts must migrate into Fivetran by 1 April 2026** or syncs pause ([RFP wiki](https://www.rfp.wiki/crm-marketing/customer-data-platforms/hightouch/census)). Don't start there.
- **When it's worth it:** if CSI later syncs several systems — QuickBooks, the portal, the OMS — into several destinations. For one table into one destination it is overkill.

### Option C — HubSpot Operations Hub Data Sync

HubSpot's native sync. It connects to supported *applications*, and the warehouse connector is **Snowflake**, not Postgres. CSI's OMS is not a supported source, so this does not solve the problem without putting a warehouse in between.

- **Verdict:** not applicable today.

### Option D — iPaaS (Workato, Tray, Zapier, Make)

Generic connectors. Workable, but adds a subscription, a vendor and a place for logic to hide. **Worse than A for this use case.**

### Option E — Two-way sync (Stacksync and similar)

What the vendor content that dominates search results is selling ([Stacksync](https://www.stacksync.com/blog/strategic-framework-for-hubspot-and-postgresql-bidirectional-integration)). It brings conflict resolution, loop prevention and change tracking.

- **Verdict: don't.** Every one of those problems is created by choosing two-way. CSI has no field that both systems should write.

---

## Recommendation

**Option A.** One scheduled job, one direction, field-level ownership, synced fields locked read-only.

If CSI's integration needs grow to several sources and destinations, revisit Hightouch then. Today it would be a subscription to avoid writing roughly a day of code.

---

## On the Change Order question

Ethan's note to Kyri: *"I obv would rather ur help in doing it but if it's something that necessitates a change order then it's something I have to get Donald and my mom to sign off on."*

Three things worth putting in front of him, and **CSI should state its read without pretending to rule** (`§9.6`):

1. **The funeral home export already exists** — he sent it on 2026-11-03. The sync is that query plus an API call and a scheduler.
2. **It overlaps heavily with the nightly booking export** already requested as EA-45-02. If that gets built, this is largely the same plumbing pointed at a different destination. **Worth asking him to scope them together** rather than as two jobs.
3. **The richer funeral home page he proposed needs none of this.** It queries the database directly, as he said. It should be scoped and decided separately, on its own merits — and `sales-lead` wants exactly the same view for account planning, so it has more demand behind it than Kyri probably realises.

---

## What CSI can do this week without waiting

**The sync is not a prerequisite for the first build.** A one-time load creates the account layer now, and the sync keeps it current later.

1. Match the OMS funeral home records to HubSpot contacts on email domain and name. 4,450 OMS records carry an email; 3,142 HubSpot contacts do.
2. Create Company records from the matched set, carrying `funeral_home_id`.
3. Associate contacts to companies, and set lifecycle from booking history — **customer** if they have ever booked, **lead** if not.
4. Hand Otto and Stacy four working lists — **but not at the headline sizes.** `sales-lead` established on 2026-11-03 that the one-time segment is **474 callable, not 845**, and churned is **322, not 412**. The difference is a record-creation change: from June 2026 the OMS began creating funeral home records at 4-5x the prior rate, with the shipper flag collapsing from ~93% to ~27% and non-US records jumping from 0.9% to 27%. **Those are receiving homes at destination, not customers who failed to return.** See `reports/fy27-target-lists.md`.

**The one thing to decide before step 2:** that `funeral_home_id` is carried on every Company record from the very first one created. Everything else is recoverable. **A company record created without the join key is orphaned from booking history permanently**, and nobody notices until the sync is switched on months later and half the records won't match.

---

## Suggested reply to Kyri

> You're right, and I don't think we want two-way. The way this normally gets solved is one-way with clear ownership: the database owns who the funeral home is and what they've shipped, HubSpot owns what we've said to them. Those fields get locked read-only in HubSpot so nobody can overwrite booking history by hand, and nothing ever writes back to you — so there's nothing to diverge.
>
> Practically that's a nightly job reading the funeral home table and upserting into HubSpot on `funeral_home_id`. There are tools that do it (Hightouch and similar) but for one table into one destination they look like a subscription to avoid writing a day of code.
>
> Two things worth your read: whether this is close enough to the nightly export we already asked about that they should be scoped together, and your rich funeral home page — which needs none of this, queries the DB directly like you said, and our sales side wants the same view. Might be worth doing that one first regardless.
>
> Happy to take that call whenever.

---

**Sources** (third-party, and they disagree — verify before relying on any figure):
[CostBench reverse ETL pricing 2026](https://costbench.com/stats/reverse-etl-pricing-2026/) · [Best reverse ETL for HubSpot sync](https://datatoolindex.pages.dev/use-cases/best-reverse-etl-for-hubspot-sync/) · [Hightouch vs Census, RFP wiki](https://www.rfp.wiki/crm-marketing/customer-data-platforms/hightouch/census) · [Do you need HubSpot Enterprise for custom objects](https://www.meticulosity.com/blog/do-you-need-hubspot-enterprise-for-custom-objects) · [HubSpot custom objects API guide](https://developers.hubspot.com/docs/api-reference/latest/crm/objects/custom-objects/guide.md) · [Stacksync on bidirectional integration](https://www.stacksync.com/blog/strategic-framework-for-hubspot-and-postgresql-bidirectional-integration)
