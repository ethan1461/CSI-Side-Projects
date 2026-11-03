# FY27 target lists: four segments, a bottom-up build, and the first action

**TASK-0021** · sales-lead · 2026-11-03 · **Status: lists built from OMS history; HubSpot lists proposed through `revops-crm`, not written**
Script: `scripts/fy27_target_lists.py` (re-runnable; tests in `tests/test_fy27_target_lists.py`) · Lists: `data/derived/fy27-seg{1..4}-*.csv`, `fy27-sample20.csv` · All figures: `data/derived/fy27-target-lists-summary.json`
Source: `data/raw/oms-funeral-homes-20261103.csv` (18,876 rows), duplicate tiering from `data/derived/oms-company-plan.csv`. As-of date 2026-11-03.

---

## The answer

1. **The four sources do not sum to 556. On the assumptions below they sum to about 230 (range 45 to 690).** The base case is 42% of the gap closed. The high case clears 556 only if roughly 300 SCI locations are live, 3,000 cold accounts are worked, and Otto and Stacy spend their whole year dialling. Ethan needs this before the OKRs are published. Section 5.
2. **The 845 may not be 845 customers who did not come back. The data points to a record-creation change in June 2026.** First-booking records ran at about 34 a month through May (91 to 97% flagged as shippers). From June they run at 144 to 199 a month, and only 22 to 35% are flagged as shippers. In June to August the OMS shows 521 "first-booking" homes, about 420 more than the pre-June pace, in a quarter where total bookings rose only 75 year on year (2,635 to 2,710). Demand did not add 420 homes. **Something changed in how homes get a record or a booking count.** Section 2.
3. **So the question is now three questions, and a phone sample answers all of them.** Did they ship once and stay with CSI? Did they try CSI and leave? Or were they never the shipping home (a receiving home, a duplicate record)? **First action: 20 scripted calls by Otto and Stacy, before any campaign is designed.** Script and sample are staged in `reports/pending-approval/sales-lead-sample20-call-script.md`. Section 1.
4. **Even taken at face value, 845 is 474 callable homes.** After removing enterprise-group homes (24), likely duplicates (113), non-US homes (177) and homes booked in the last 14 days or with no date (56), 474 remain, and 215 of those are flagged as shippers.
5. **The biggest pool is not what the headline says.** Of the 16,340 never-booked records, 10,243 are outside the US (mostly Dominican Republic, Mexico, El Salvador, Honduras, Guatemala: almost certainly receiving homes, not prospects for an export service). The callable US pool is **5,709**, and only **341** of those have a shipper account.
6. **Territory is a gap, not a detail.** 69% of callable one-time homes (328 of 474) sit in the Northeast and South. Otto (Midwest) and Stacy (West) have no rule covering them. Ethan decides who calls them. Section 6.

Confidence: **high** on the counts (direct from the export). **Medium** on the June interpretation (the signature is clear; the cause is unconfirmed). **Low** on every conversion rate in section 5, which is why they are ranges and why the sample comes first.

---

## 1. First action: 20 scripted calls, before any campaign

**Why before anything else.** Segment 1 is the cheapest volume CSI can chase, and we are about to point two new reps at it without knowing what the homes are. The right response differs by answer:

| If the calls show... | Then the response is... |
|---|---|
| **A. Ships rarely, CSI is already the vendor** | No campaign. A light quarterly check-in. Move rep time to segments 3 and 4A. |
| **B. Tried CSI, chose someone else** | A displacement-by-insertion play ("add us as a backup, keep your vendor") built on the *stated reasons*, in their words. |
| **C. Never the shipping home (receiving only), or a duplicate or closed record** | Segment 1 is a data problem, not a sales list. Resize it to the shipper-flagged homes. Receiving homes become a different conversation (a referral and relationship one), not a "come back" one. |

**Design (proposed, needs Ethan's approval of the script).**
- **20 homes**, drawn by a fixed-seed hash so the draw is reproducible (`data/derived/fy27-sample20.csv`). US, not duplicate, not enterprise, not partner, first booked at least 14 days ago, phone on file. 10 calls each for Otto and Stacy, regardless of territory (it is a phone sample).
- **Stratified on purpose:** 4 shipper-flagged homes first booked before June; 8 shipper-flagged first booked June onward; **8 not shipper-flagged**. The last stratum is the one that tells us whether the June surge is real customers.
- **Up to three attempts per home** across two days. Log every call the same day in a shared sheet (outcome code, reason in the home's own words). HubSpot stays untouched until `revops-crm` has the properties.
- **Outcome codes:** A1 ships rarely, no other vendor; A2 ships rarely, uses another vendor too; B chose another vendor (reason: price, speed, existing relationship or habit, did not know CSI could, a problem with CSI); C receiving or consignee only; D closed, wrong or duplicate record; E no answer after three attempts.
- **Decision rules, set now so the result cannot be bent afterwards.** (1) If a third or more of reached homes are C or D, treat segment 1 as a data question first. (2) If 40% or more of reached true shippers (A plus B) are B, design the backup-vendor sequence from the stated reasons. (3) If most are A, no campaign. (4) **Any problem-with-CSI answer goes to Vadim and Kim that week.** It is a service fix, not a sales objection.
- **Honest limit:** 20 calls with perhaps 10 to 12 reached gives direction, not a rate. 7 of 12 and 5 of 12 cannot be told apart. We are reading *reasons*, not percentages. If the read is ambiguous, extend by another 20 from the same strata.
- **Dates and owners:** Ethan approves the script Wed 2026-11-04. Otto and Stacy call Thu 11-05 to Mon 11-09. I write the read-out Tue 11-10. Ethan decides the campaign shape Wed 11-11.

**What Otto and Stacy do in the meantime (none of it depends on the answer):** the 12 NFDA form responses already matched to booking history (warm and perishable, including the customer doing 10 domestic and 10 international shipments flagged for the portal); segment 4A (341 homes with a shipper account that never booked); segment 2A (23 lapsed homes with five or more bookings). Anything naming a group goes to Ethan first.

---

## 2. What changed in June 2026

| First-booking month | New homes | Flagged as shipper |
|---|---|---|
| Jan to May 2026 (monthly) | 29 to 39 (avg 34) | 91 to 97% |
| Jun 2026 | 153 | 33% |
| Jul 2026 | 199 | 22% |
| Aug 2026 | 169 | 23% |
| Sep 2026 | 162 | 35% |
| Oct 2026 | 144 | 24% |

Source: `first_booking_by_month` in the summary JSON. Of the 844 one-timers by my count, **130 were first booked before June (118 shipper-flagged) and 713 from June on (178 shipper-flagged, 535 not).**

**What this rules in and out.**
- *Not Google Ads.* The relaunch was August (`context/brain/initiatives/google-ads.md`); the step starts in June, and ads leads would arrive as shippers.
- *Not demand.* June to August bookings are up 75 on last year (+2.8%) against about 420 excess first-booking records. If those were new customers, bookings would be up by at least that.
- *Consistent with* the OMS starting to create or count receiving funeral homes from June (the export spec shows receiving-home fields come from this table), or with a migration or bulk import. **That is a hypothesis. I cannot confirm it from this file.**
- `created_date` is **blank on all 18,876 rows.** With it we would know in one query whether June's cohort is new records or new activity.

**Why it matters beyond this task.** CLAUDE.md and the task brief read this as "CSI acquired 845 new accounts." I do not think that is safe to say until the calls and the three data questions in section 7 are answered. It also says "not one has come back": that is true by definition of the segment. In the 2026 first-booking cohorts, about 190 of roughly 970 homes (19%) *have* booked a second time.

**Base rate the task framing needs.** Share of first-booking cohorts (excluding partners and groups) that have booked at least twice:

| Cohort | Homes | Booked 2+ | Age now |
|---|---|---|---|
| 2022 | 438 | 85.4% | 4+ years |
| 2023 | 302 | 65.9% | 3+ years |
| 2024 | 282 | 60.3% | 2+ years |
| 2025 | 270 | 51.5% | 1+ years |
| 2026 Q1 | 83 | 36.1% | 7 to 10 months |
| 2026 Q2 | 213 | 30.5% | 4 to 7 months |
| 2026 Q3 | 514 | 16.9% | 1 to 4 months |

Read across cohorts, roughly 14 to 18% of homes still on one booking return in a given year *with no programme at all* (`[ESTIMATE]`: difference between adjacent cohorts, cross-sectional, so only indicative). **"20% of one-timers booking once more" is therefore close to what happens anyway. The incremental number is the lift above that, and it is smaller.** Section 5 models lift, not the whole return.

---

## 3. Sizes and exclusion waterfalls

Exclusions applied everywhere: the four partners (IDs 2734, 1764, 2239, 2767; none appear in a prospecting list); likely duplicates (OMS flag or revops-crm's `hold_duplicate` tier) held for the desk, not merged; enterprise-group homes routed to segment 3; non-US homes not routed to Otto or Stacy; **the 1,117 freemail and 807 chat-origin HubSpot contacts are not in any list** (these lists are built from OMS records, not contacts, and when `revops-crm` associates contacts it must skip both groups, section 7).

| Step | Seg 1 one-time | Seg 2 churned | Seg 4 net-new |
|---|---|---|---|
| As defined | 844 (brief says 845; see note) | 412 | 16,340 |
| less partners / enterprise-group homes | 820 | 377 | 16,269 |
| less likely duplicates | 707 | 332 | 16,061 |
| less non-US | 530 | 322 | 5,818 |
| less booked <14 days ago or undated (S1) / no phone (S4) | **474** | **322** | **5,709** |

Note on 845 versus 844: one record (ID 20801) carries a first-booking date of 2060, a data defect I excluded; one (ID 3015) has no dates at all and sits in the "too fresh or undated" step. 28 records in total carry a 2060 last-booking date, and 89 carry any date after today (probably scheduled flights, but the 2060 ones are typos). Flagged in section 7.

Segment 3 is not filtered this way: it is 320 mapped group records (below).

---

## 4. The four segments

### Segment 1: One-time customers (474 callable of 844)
- **Call order:** (1) the 20-call sample; (2) after the read-out, tier 1A, **215 shipper-flagged homes, most recent first booking first**; (3) tier 1B, 259 homes not shipper-flagged, **held until the sample says what they are.** List: `fy27-seg1-one-time.csv`.
- **Reason to call (1A):** a learning call, not a pitch. "We handled an arrangement with you in [month]. How did it go, and how do you usually handle these?" Recent first booking is the warmest moment to hear about a problem and fix it.
- **By territory (callable):** Otto 84, Stacy 60, no rule 328, no state 2. Shipper-flagged: Otto 39, Stacy 32, no rule 144.
- **Not in the 474:** 177 non-US (Dominican Republic 33, Mexico 25, El Salvador 20, Guatemala 17, Honduras 13...), 113 held duplicates (8 of the 35 OMS-flagged ones have a sibling record that booked earlier or more, so some "one-timers" may have come back under a second ID), 24 group homes, 56 too fresh or undated.

### Segment 2: Churned (322 callable of 412)
- **Size and value:** mean 2.3 lifetime bookings, median 1, 949 lifetime bookings in total. Last booking 2022: 76 homes, 2023: 167, 2024: 169. "Lifetime" means since the OMS history starts (2022).
- **Call order:** 2A, **23 homes with 5+ bookings**, longest-standing first; 2B, **78 homes with 2 to 4**; 2C, **221 single-booking homes, verify-only** (one call or one note to confirm they are still operating, then dormant). List: `fy27-seg2-churned.csv`.
- **Reason to call:** "We have not worked together since [year]. What changed?" For homes silent 24+ months the first question is whether the home still exists or has been sold; the OMS has no status field. Dormant is a real outcome here.
- **By territory:** Otto 51, Stacy 40, no rule 228.

### Segment 3: Enterprise (320 mapped records). **Every contact needs Ethan.**

| Group | Mapped | Ever booked | Booked in last 12 mo | Lifetime bookings | Median bookings per booked location per year `[ESTIMATE]` |
|---|---|---|---|---|---|
| SCI (of 4,439 total locations) | 242 | 189 | 138 | 4,169 | 2.0 |
| Northstar | 45 | 41 | 36 | 2,896 | 6.6 |
| Foundation Partners | 30 | 19 | 13 | 633 | 8.5 |
| Carriage | 3 | 0 | 0 | 0 | n/a |

- **Call order (all gated):** (1) protect what exists: the 138 SCI locations already booking get service, not a campaign; (2) the Pam-led pilot locations; (3) the 53 mapped SCI locations that never booked, once corporate comms allow; (4) **the 4,197 unmapped SCI locations**, which need a location master list from corporate before anyone can work them; (5) Northstar and Foundation Partners as corporate conversations (Northstar not yet approached).
- **Two things worth Ethan's attention.** Northstar and Foundation Partners locations book at three to four times SCI's per-location rate (small samples: 41 and 19 booked locations; `[ESTIMATE]`). And **Everstory has zero records tagged in the OMS**, so its ~80 locations cannot be sized or mapped from this data.
- **Territory:** SCI mapped: Stacy 61, Otto 17, no rule 151, no state 11. Foundation Partners: 29 of 30 West. Not routed to a rep until Ethan rules.
- **No outreach is drafted here.** SCI status since 2026-08-13 is unknown to me (`accounts-and-pipeline.md`); the location-level activation plan waits on Ethan and Pam.

### Segment 4: Net-new (5,709 callable US of 16,340)
- **Call order:** 4A, **341 homes with a shipper account that never booked** (someone already opened an account: the warmest cold list CSI has); then 4B, **5,368 homes**, ranked by how many active shipper homes CSI already has in the same state (peer proof, easier to reference). List: `fy27-seg4-net-new.csv`. Ranked last overall because CAC is unmeasurable.
- **Reason to call:** no booking fee, and "add us as a backup, keep your vendor." A first call asks for nothing but a name for 3am.
- **By territory:** Otto 1,284, Stacy 735, no rule 3,686.
- **Why 10,243 are out:** non-US. Dominican Republic 1,551, Mexico 1,336, El Salvador 875, Honduras 693, Guatemala 655. These look like receiving homes. That is a corridor-partnership question for `gtm-strategist`, not a cold-call list.
- **Instrumentation before spend:** every 4B call is logged with outcome code and minutes spent, so CSI gets its first measured cost per booking from this segment.

---

## 5. Bottom-up build to 556

**Method.** Incremental FY27 bookings above the 2026 run rate, per segment: accounts won x bookings per account in FY27. Every rate is `[ASSUMPTION]` and labelled so; none is measured at CSI. Numbers come from `build_model()` in the script, so changing a rate re-runs the table.

| Input | Low | Base | High |
|---|---|---|---|
| S1 lift in return rate, shipper-flagged (215), above the ~14 to 18%/yr that happens anyway `[ASSUMPTION]` | 3 pts | 8 pts | 15 pts |
| S1 lift, not shipper-flagged (259) `[ASSUMPTION]` | 0 | 3 pts | 8 pts |
| S2 reactivation, 2+ bookings (101) `[ASSUMPTION]` | 3% | 6% | 10% |
| S2 reactivation, single booking (221) `[ASSUMPTION]` | 0 | 1% | 2% |
| S3 SCI locations live in FY27 `[ASSUMPTION]` | 25 | 100 | 300 |
| S3 bookings per live location per year `[ASSUMPTION]`, anchored to the SCI median of 2.0 | 1.0 | 2.0 | 2.0 |
| S3 share of year live (average) `[ASSUMPTION]` | 50% | 50% | 50% |
| S4A conversion of 341 shipper-account homes `[ASSUMPTION]` | 5% | 10% | 20% |
| S4B cold accounts worked / conversion `[ASSUMPTION]` | 1,000 / 0.5% | 2,000 / 1% | 3,000 / 2% |
| Bookings per won account in FY27 `[ESTIMATE]`: OMS median 1.2/yr, mean 1.5/yr for low-volume repeat homes (n=470) | 1.0 | 1.5 | 2.0 |

| Source | Low | Base | High |
|---|---|---|---|
| 1. One-time | 7 | 38 | 106 |
| 2. Churned | 3 | 12 | 29 |
| 3. Enterprise (SCI only) | 13 | 100 | 300 |
| 4. Net-new | 22 | 81 | 256 |
| **Total** | **44** | **231** | **691** |
| **Gap to 556** | **512** | **325** | **(135)** |

**What this says, plainly.**
- **Base case reaches 42% of 556. The sources do not carry +5% on their own.**
- **Segment 1 is small.** The task brief's "20% of 845 is 169 at no acquisition cost" counts accounts, counts the returns that happen anyway, and counts homes we may not be able to call. Net of those, the base case is about 25 accounts and 38 bookings.
- **Enterprise is the swing, and it is the least controllable.** To close the base gap with SCI alone needs about **425 SCI locations live** (about 10% of 4,439), against 138 mapped today that already book. Every SCI figure here is a guess about a pilot whose status I do not know.
- **High case is a capacity problem.** It needs about 12,100 dial attempts a year; two reps at 30 dials a day over 200 selling days is 12,000 `[ASSUMPTION]`. The base case needs about 9,100. Neither leaves room for ramp-up, enterprise work, or the NFDA follow-up.
- **What is not in the sum:** share-of-wallet growth at the ~1,800 homes already booking, Northstar and Foundation Partners (high per-location yield, Northstar not yet approached at corporate level), the NMS and Bergen channel (Ethan's relationships), trade-show leads, and Everstory. I have not sized them because there is no booking-level data to size them from. I will not invent a number to fill the gap.
- **The 556 itself is soft.** It is +5% of an approximate 2026 run rate, and it assumes no attrition from the existing base. Churn vs acquisition cannot be measured without a booking-level export (CLAUDE.md §4.3).

**Recommendation to Ethan.** Publish the OKRs on controllable inputs (calls completed, homes reached, second bookings won, SCI locations live) with the 230 to 690 range stated, not on 556 as the sum of four lists. Revisit after the sample read-out and the SCI pilot status.

---

## 6. Territory and routing (a decision for Ethan)

There is no territory rule, and the data shows why one is needed. Proposed rule used in the list files: **Midwest states to Otto; West states (Pacific plus Mountain) to Stacy; everything else "unassigned"; non-US not routed.**

| Segment | Otto | Stacy | Unassigned (Northeast/South) | No state |
|---|---|---|---|---|
| 1 callable (474) | 84 | 60 | 328 | 2 |
| 2 callable (322) | 51 | 40 | 228 | 3 |
| 4 callable (5,709) | 1,284 | 735 | 3,686 | 4 |

The densest states (NY, NJ, PR, FL, TX, NC) have no owner. Jeff Shafer's West Coast patch overlaps Stacy's (conflict C5 in the brain). **Decision needed:** who calls the Northeast and South. Options: (a) Otto and Stacy split those lists by alternating rank, since the motion is phone-led; (b) Jeff or another owner takes them; (c) leave them until the Midwest and West lists are exhausted. I recommend (a) for the sample and tier 1A only, then reassess. Owner assignment in HubSpot waits for this ruling.

---

## 7. Handoffs, data requests and decisions

**Staged for Ethan:** `reports/pending-approval/sales-lead-sample20-call-script.md` (script, sample, decision rules). Nothing is sent. No list is enrolled in any sequence.

**Handoffs raised (routed by the PM):**
- `handoffs/HANDOFF-T0021-revops-lists.md`: five static lists to build once `funeral_home_id` exists; exclusion rules; skip freemail and chat contacts when associating.
- `handoffs/HANDOFF-T0021-june-cohort.md`: three questions about `booking_count`, `is_shipper` and the June 2026 step. Ask Susej and Kim first (how a booking creates or links a home record), then Kyri and Alex (blank `created_date` on all rows; 2060 dates on 28 records).

**Decisions for Ethan this week:** (1) approve the 20-call script by Wed 11-04; (2) territory rule for the Northeast and South; (3) OKR form (inputs and a range, or 556); (4) whether Pam's pilot location list and SCI's full location master list can be requested (his call; I have not contacted anyone).

**Not done, deliberately:** nothing written to HubSpot; no email or LinkedIn draft aimed at any named account or person; no ranking or comparison of booking agents; no estimate of secondary-service margin.

**What would raise confidence:** the sample read-out (fixes the S1 rates), the three OMS questions (fixes the S1 and S4 sizes), SCI pilot status and the location master list (fixes S3), and a booking-level export (fixes the baseline and the churn assumption).
