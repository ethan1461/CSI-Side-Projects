# SCI portal pilot — the evidence, the report spec, and the free-deployment model

**Author:** product · **Date:** 2026-11-18 · **For:** Ethan Silvey (CSO), via pm-orchestrator
**Status:** **INTERNAL PREPARATION ONLY.** Nothing here goes to SCI, Dignity, Pam or Lauren without Ethan's written approval (`CLAUDE.md §7.1`).
**Revises:** `reports/sci-footprint-strategy-2026-12.md` §2, §3 (Ideas 2, 4, 5), §4 (precondition 4). Premises changed are listed in §10.
**Source handling (`§7.2`):** Ethan supplied a screenshot of the OMS Portal Revenue Tracking page. It carries a `Deceased Name` column. **I did not see the image, and nothing from that column is in this document.** I worked from Ethan's written summary of the page (funeral home, booker count, route, dates, charges, status, tier panel) and from CSI's own repo data. Every shipment-history figure below was computed from a four-column export (`booking_id`, `shipping_funeral_home_id`, `flight_date`, `status`) that holds no decedent or family data. The screenshot should stay out of the repo, Drive and HubSpot.
**Confidence:** **High** on the revenue-share finding (§3) and the verification results (§5). **Medium** on the status update (§4) until the 13 booking references are matched. **Low** on the free-deployment payback (§8): the two numbers that decide it, desk time per portal booking and incremental bookings per adopting location, have never been measured.

---

## The answer, in eight lines

1. **The platform-SLA constraint is withdrawn.** Ethan is right: the portal is an additional channel and the 24/7 named agent is the service. Struck from the strategy (§2). One narrow point survives, about a *written* SLA CSI might sign, and it does not bound what he can say.
2. **The "revenue share already built" is not a revenue share to customers. It is what CSI owes its software developer.** The five tiers on that page, 1.5% on the first $500,000 rising to 3.5% above $2,000,000, are the Ex. C §5 schedule of the FreightFlow agreement (`reports/freightflow-agreement-review.md §2.2`), and "Total Rev Share Pool" is the running accrual of what CSI pays *out* on customer-initiated portal revenue. **It is not a hook for SCI, it cannot be shown to SCI, and every SCI portal booking adds to it.** This inverts the premise in the brief, and it is the most important thing in this report (§3).
3. **Free deployment is a better offer than the $999 tier, and it also avoids a cost.** It sidesteps the Developer's 30% share of subscription fees (agreement Ex. C §6). It is not costless: each portal-initiated dollar carries a 1.5% to 3.5% channel cost to the Developer (§8).
4. **The status update Ethan can give is real but small, and he should say both halves.** 13 portal bookings, $12,458.44 in total charges, 15 Sep to 14 Nov, four homes (all four are SCI by CSI's records), seven bookers. That is roughly 7% of SCI bookings flying in the same window, at about 4 of the 55 SCI locations that shipped (§4, §5).
5. **The page and the shipment history do not obviously agree.** The four homes show 15 bookings flying in the window; the page shows 13 portal bookings. Either these four homes moved almost entirely to the portal, or the two use different date bases. **Do not state a portal share until the 13 references are matched** (§5).
6. **The defensible record is buildable by January, and 13 rows of it can be built before 2 December.** The page already links booking to home, booker and route. What is missing is the denominator, bill-to, timestamps and a phone-versus-portal comparison (§6). The engineering ask narrows from "what does the portal log?" to four specific items.
7. **Bill-to is in the report spec as a condition, not a column.** A booking invoiced to a partner never counts as CSI-billed SCI volume (§7).
8. **Promotion is worth what it puts in front of the right 20 locations, not how many it reaches.** Top-10 locations are 57.9% of SCI volume. Ranked forms of promotion are in §9; a vendor-bulletin mention ranks last.

---

## 1. What I verified, and what I could not

| Check | Result | Confidence |
|---|---|---|
| Which of the four homes are SCI/Dignity, by the OMS group field | **Palm Downtown (id 2267, SCI #1008, Las Vegas), Palm South Jones (id 2272, SCI #1012, Las Vegas) and Hines Rinaldi (id 2052, SCI #9738, Silver Spring MD) all carry `funeral_home_group = SCI`** in `data/raw/oms-funeral-homes-20261109.csv`. **Hines Rinaldi is also SCI**, not a non-SCI fourth home: the brief grouped it apart, but the OMS group field and its June 2026 pilot-shortlist listing both say SCI. | High |
| "Funeraria Del Angel Lincoln" | **Not labelled SCI in the OMS group field.** The nearest record is id 12475 "Funeraria Del Angel Lincoln Heights" (Los Angeles), group field blank, which `sci-unlabelled-locations.csv` matches to register entry #4908 on name, ZIP and phone (tier T2). It shares an address with a second record that carries a dignitymemorial.com contact. **The page's name is not exactly the OMS name, so this is an inference.** One booking in the history, flown 2026-10-09, status Booked. | Medium |
| All four in CSI's SCI location set | Yes: all four ids are among the 248 in `sci-location-trajectory.csv`. | High |
| The 13 portal bookings in shipment history | **Not matchable today.** I do not have the booking references. The four homes show 15 bookings with flight dates 15 Sep to 14 Nov in `shipments-since-2022-20261110.xlsx`, all status Booked (Palm Downtown 9, Palm South Jones 3, Hines Rinaldi 2, Lincoln Heights 1). The export ends 10 Nov, so the page's last four days are not in it. | n/a |
| Booking counts for the same homes agree across sources | **They do not.** Palm Downtown: 70 in the shipment export, 71 in the partner manifest (3 partner, 63 self, 5 other-billed), 75 in the OMS master. Hines Rinaldi: 68 vs 73. Palm South Jones: 38 vs 38. Different cut dates and definitions probably explain it; none is documented. This is `CLAUDE.md §6` showing up again. | High that they differ; cause unknown |
| Partner-billed exposure among the four | Only Palm Downtown appears in `partner-billed-homes-manifest-20261118.csv` (3 partner-billed of 71). The other three are absent from it, consistent with zero partner-billed bookings; the manifest's inclusion rule should be confirmed. Per-booking bill-to for the 13 is still needed. | Medium |

**What the shipment export cannot tell us:** which bookings were portal-initiated (no channel column), bill-to, lane, creation date. It has no draft or quote-converted statuses at any of the four homes or anywhere in SCI (the only `Quote converted to booking` rows in history are 10, none at SCI), so **it cannot show abandonment** at SCI.

---

## 2. Correction 1: the platform SLA constraint is withdrawn

**Struck from `sci-footprint-strategy-2026-12.md`:** the "Hard constraint" under Idea 2 and the framing of precondition 4 in §4, which bounded what Ethan may say about service by the platform's 24-hour Level 1 restoration, 6am to 11:59pm uptime measurement and absence of service credits.

**Why it was wrong.** It treated the portal as the service. It is an additional channel. A funeral director can always book, manage and track by phone or email, and the named 24/7 agent is the path CSI has always run. Platform downtime reduces convenience; it does not break the promise. Ethan can speak freely about service. He should not stop saying "call us any time" because the portal exists.

**What narrowly survives, and it is not a constraint on 2 December.**

- A **contractual** SLA, in writing, with remedies, that CSI might one day sign with SCI cannot be stronger than what sits behind it. That is `TASK-0017`, still unclaimed, and it belongs in the primacy conversation (strategy §4), not this meeting. Nothing in the proposal below is a contractual SLA.
- One operational question I have not seen answered anywhere, offered as a note and not a bound: the desk itself works in the OMS. "A named human always answers" is true regardless. "And actions it at normal speed during a long OMS outage" depends on a desk contingency I cannot find documented. That is a question for `operations` and does not limit what Ethan says.

---

## 3. The finding nobody had raised, and it runs the other way

**Short version: the revenue-share panel is the cost side, not the offer side. Do not take it near SCI.**

### What the page is

| What Ethan read off the page | What the contract says | Match |
|---|---|---|
| Five marginal tiers, 1.5% at $0 to $500K, 3.5% above $2M | Ex. C §5.1(b): 1.5% / 2.0% / 2.5% / 3.0% / 3.5% at $500K / $1M / $1.5M / $2M, marginal (`freightflow-agreement-review.md §2.2`) | Both known endpoints and the marginal structure match |
| "$487,541.56 remaining to Tier 2" | $500,000 − $12,458.44 = $487,541.56 | Ties exactly: confirms a $500K first boundary |
| Effective 1.5% on $12,458.44 = $186.88 | 0.015 × $12,458.44 = $186.8766 | Ties |
| Counts only portal bookings | "Shipment Revenue" counts only services "initiated directly by the customer through the Frontend System" (Ex. C §5.1(c)) | Same population |

**Who built it for whom.** The agreement review already described "live customer portal revenue and tiered revenue share calculations" as the page the Developer built so CSI can compute **what CSI owes the Developer**, annually, within 20 days of the Revenue Share Year end (Ex. C §5.3). The Developer, not CSI, holds the audit right (§5.4). `[I have not seen the page itself; the match is on the tier schedule, the arithmetic, and the page's name. A page-level confirmation from Kyri or Alex is a five-minute question.]`

**Answers to Ethan's four questions.**

| Question | Answer |
|---|---|
| Who was it built for? | CSI's software developer, as the calculation of CSI's payment obligation. |
| Has any group been offered it? | No evidence of any offer, and it is not a CSI programme that can be offered: it is a term of CSI's vendor agreement. |
| Live or illustrative? | The calculation is live (it shows a current effective rate on real bookings). Whether a payment is **due** turns on the Revenue Share Year ambiguity (first payment possibly about 20 Jan 2027, 20 Mar 2027, or 20 Jan 2028; counsel question R1). |
| Margin impact at SCI's volume? | It is a cost to CSI, not a share to SCI. Arithmetic ceiling `[ILLUSTRATION]`: if all of SCI's 2025 revenue ($1,047,999, `sci-revenue-by-year.csv`) were portal-initiated and nothing else were, CSI would owe $7,500 + 2.0% × $547,999 = **$18,460**, an effective 1.76%. The *marginal* cost is set by CSI-wide portal revenue, not by SCI alone. |

### Why this matters for 2 December

1. **No CSI-to-SCI revenue share exists.** Idea 5 in the strategy (a volume rebate against a measured baseline) is still a legitimate structure, but it is a *new* instrument. Nobody has built it, priced it or approved it. It must not be described to SCI as something that is "already built".
2. **Showing the tiers to SCI would disclose a term of CSI's confidential vendor agreement.** It is also a number in front of SCI that is not SCI's (`§7.1` pricing claims; `§7.6`).
3. **Every SCI portal booking raises CSI's payment to the Developer.** That is a channel cost on CSI's own books, and it reaches 3.5% on revenue above $2M of portal-initiated invoicing across the *whole* customer base. Promoting adoption is therefore not free to CSI even when the software is free to SCI (§8).
4. **The page is the only record of the 13 bookings, and it was built by the party paid on its output.** The agreement review makes this a structural point, not an allegation. For a record that must survive SCI's scrutiny, the numbers have to tie to **CSI's invoices (QuickBooks)**, not to the page (§6).
5. **A customer rebate paid as a credit may or may not reduce the base the Developer is paid on.** Counsel questions R2 and R3 cover it. Do not design a rebate before they are answered.

**Handoff to `finance` raised** (`handoffs/HANDOFF-sci-portal-finance.md`). No rate goes in front of SCI until Donald has seen the arithmetic.

---

## 4. The status update Ethan can give

**What changed from the strategy's §2.** The strategy's script said: *"What I cannot give you today is a usage picture."* That is no longer accurate. CSI can give a partial one, and a partial real one is stronger than a gap conceded.

### What the page establishes (CSI's own record)

| Fact | Value | Source |
|---|---|---|
| Portal bookings | **13** | Admin page |
| Total charges | **$12,458.44** (about **$958.34** per booking; arithmetic) | Admin page |
| Period | 15 Sep to 14 Nov 2026 (61 days) | Admin page |
| Status | All Booked | Admin page |
| Distinct bookers | **7** (13 bookings across 7 people, so at least one repeated; arithmetic) | Admin page |
| Homes | **4**: two Las Vegas Palm chapels (both SCI by OMS group field), one Silver Spring MD (SCI), one Los Angeles (SCI by register match) | Page + OMS master |
| Geography | Nevada is one of the three states that carry 78% of SCI volume (`reports/sci-relationship-evidence.md`) | Evidence report |

### What it sits against (my computation, `[ESTIMATE]`, both windows approximate)

| Comparison | Value | Method and limit |
|---|---|---|
| SCI bookings flying 15 Sep to 10 Nov | **199** at 55 locations (163 excluding Borthwick, which is 97% partner-billed) | Shipment export filtered to the 248 SCI ids. Flight-date basis; export ends 10 Nov, the page runs to 14 Nov |
| Portal bookings as a share of those | **about 6.5% to 8.0%** (13 ÷ 199 and 13 ÷ 163) | Windows and date bases differ. **Indicative only.** Do not quote it |
| Locations with a portal booking vs. locations that shipped | **4 of 55** in the window; 4 of 138 active in 2026; 4 of 1,582 funeral-home-line locations (0.25%) | Assumes the four named homes are the only homes on the page |

### What it cannot support, and what Ethan should not say

- **Adoption rate.** There is no onboarded or invited denominator yet.
- **"Going well", "growing", "x% of bookings".** Nobody has the comparison.
- **That the bookings are incremental.** They may be phone bookings that moved.
- **That $12,458.44 is revenue.** The page says "total charges". The contract measures what CSI *invoices* (agreement review D2). Until Donald ties the 13 to invoices, call it "total charges on the page".
- **Anything about the revenue-share panel.**
- **A named booker's activity** in any SCI-facing material. Counts only (§7).

### Two observations worth knowing before the room (not for the room)

- **The three homes Ethan can name are not the largest.** Palm Southwest (id 2274, SCI #5260, 111 bookings in history, the largest Palm location in CSI's data) is not among the four on the page.
- **The June pilot shortlist's Florida chapels (Riverside Gordon, Riverside-Stanetsky, Star of David, Bailey Memorial) do not appear** among the four homes. Those are the high-volume Israel-corridor chapels the evidence report puts at the top of SCI volume. Only Hines Rinaldi and Palm (Las Vegas) from the shortlist show portal use. Whether the Florida chapels were onboarded and prefer the phone, or were never onboarded, is the first thing to learn (it changes the whole promotion plan, §9).

### Suggested script (replaces the strategy's §2 paragraph)

> "Here is what the pilot has produced, and where it is thin. Since mid-September, four of your locations have booked thirteen shipments through the portal, from seven different people on your teams. That is a small number against the volume we do together, and I would rather say so. What we can do now is put every one of those bookings in front of you with a reference you can check. What I cannot yet give you is the comparison: how those locations book when they do not use the portal. The monthly report I would like to agree today gives you both. And for any of your locations, the phone and email path is the same one that has always worked; the portal is an easier way in, not a different service."

**Three jobs:** it states the number plainly, it offers to be checked, and it turns the thinness into the ask. It also uses Ethan's own point (the manual path always works) as a feature.

---

## 5. Verification results Ethan needs before he cites any of it

1. **Run before 2 Dec (13 rows, one afternoon):** ask Kyri or Alex for the 13 booking references. Match each to `booking_id` in the shipment export (assumes the page's "booking reference" is the same identifier; unverified). Expected: all 13 found, all Booked. A reference that is not found is the finding.
2. **Resolve the 13-versus-15 tension.** If the page's period is on *booking-created* date and the history's `flight_date` is the travel date, the two windows overlap partly, and 13 of 15 is a coincidence of bases. If both are flight dates, **these four homes sent about 87% of their recent bookings through the portal**, which would be extraordinary for the audience CLAUDE.md describes and would be worth finding out how it happened. The 13 references answer it.
3. **Tie the 13 to QuickBooks invoices (Donald).** This is what turns "total charges" into revenue and makes the record auditable independently of the page.
4. **Bill-to for the 13.** Palm Downtown is the only one of the four with partner-billed history (3 of 71). Confirm none of the 13 is invoiced to a partner.
5. **Confirm Lincoln Heights is the page's "Del Angel Lincoln".** One record, one question for Kyri or Alex.

None of these needs an engineering build.

---

## 6. A defensible, auditable SCI pilot record: what exists, what is missing, how to get it

**The standard.** "Defensible and auditable" means three things, and the spec below is built to meet all three: **(a)** every number traces to a booking reference SCI can check against its own records; **(b)** the references reconcile to CSI's invoices, not only to the platform page; **(c)** the definitions and the location list are versioned, so month 4 is comparable to month 1.

### The gap analysis, metric by metric

| Metric asked for | Exists today? | Where it comes from | Needs engineering? |
|---|---|---|---|
| Bookings, revenue, which locations, which people, over what period | **Yes** (§4) | Portal Revenue Tracking page | **No.** But a *column-limited export* of the page does (ask 1 below), because the page displays decedent names and cannot be shared or archived as-is |
| Adoption against eligible locations | **Partly.** Numerator (locations with a portal booking) is on the page. **Denominators do not exist**: invited, onboarded accounts, universe | Invited: the pilot location list Pam received (Cheryl / Ethan records). Onboarded: portal user/account table (spec D3: `portal_onboarded_date`, `portal_user_count`, already in EA-45-03). Universe: **1,582** funeral-home-line locations, 1,830 shipping-capable (`sci-denominator.csv`) | **Question first** (ask 2). Invited list is a human lookup |
| Repeat usage per booker | **Derivable now** from the page: bookings per booker, bookers with 2+ | Page | No. Report as counts and a distribution, **not names** |
| Portal vs phone/email split at the same locations | **Derivable now, once refs are matched.** Anti-join: all bookings at the pilot homes from the shipment export, minus the portal refs. Reliable going forward via `created_via_portal` (spec field 18 in EA-45-02) | Shipment export + page refs; later D1 | **No for report #1.** Yes (already requested) for automation |
| Time-to-book | **No** | Needs quote timestamp and booking-request timestamp. Spec fields `request_received_at` (41) and quote persistence (EA-45-08) were requested as questions | **Yes**, narrowed in ask 3 |
| Errors or abandonment | **No for SCI.** No drafts or quote-converted rows at any SCI home in history | Needs quote persistence and failed-submission logging | **Yes**, folded into ask 3 |
| Invoice bill-to | **Per home, partly.** Manifest holds 535 partner-routed homes. **Per booking, not available.** | Production-database session can produce it; invoicing code computes `COALESCE(csi_new_shipper_to_invoice.shipper_id, csi_booking_shipper_information.shipper_funeral_home_id)` (`HANDOFF-partner-routing-revops-product.md`) | **Yes**, already ranked in the Monday ask as a column on the booking export |
| On-time performance, documentation turnaround, escalations | **No.** Manual for report #1 | Escalation log: booking desk. Turnaround: `compliance` baseline | Not an engineering item for #1 |

### The engineering ask, narrowed

`reports/pending-approval/engineering-ask-2026-46.md` asked, in open form, what the portal logs at event level. **That question is now partly answered:** the system records, for each portal-originated booking, the home, the person who booked it, the route, the flight date, the charges, the status and a link to the booking. Those four items from the open question can be dropped. What remains, in order, stated as CSI's read and not a ruling on scope (`§9.6`):

| # | Ask | Unblocks | Bug or new? |
|---|---|---|---|
| 1 | **A column-limited export of Portal Revenue Tracking**, with `Deceased Name` and any free-text or document field **excluded at the query**. Columns: booking reference, shipping funeral home id, funeral home name, booker (as a stable user id), booking created timestamp, flight date, origin and destination, total charges, status, `created_via_portal` | The pilot record; every month after | New (export button, the same shape as EA-45-02) |
| 2 | **Does the portal keep a user table with onboarded date, last login and a per-home user count?** And can a login or a quote be tied to a home, not only a booking? | Adoption against eligible; the funnel | Question, then maybe new |
| 3 | **Are quote events persisted, and is a submission timestamp kept?** (Quote started, quote shown, booking request submitted, booking confirmed by an agent; plus a failed-submission or abandoned-draft flag.) | Time-to-book, abandonment | New; EA-45-08 already asks the first half |
| 4 | **How does the page decide a booking is "portal"?** Customer started and finished it, or started and an agent completed it, or any booking on a portal account? | Whether the 13 are what they appear to be; the contract definition (agreement review D1) | Question |
| 5 | **Bill-to on every booking in the booking export** (`bill_to_funeral_home_id`) | A report SCI can rely on | New (already in the Monday ask) |

Ask 4 also matters outside this report: it decides what the portal-adoption metric means, and it is the same question the revenue-share arithmetic turns on.

**How to get the record, in three steps, and what each costs.**

| Step | By | What | Cost |
|---|---|---|---|
| **0** | Before 2 Dec | The 13 references from Kyri or Alex, matched to the shipment export, bill-to checked, tied to invoices by Donald | One request, about 13 rows of manual work, no build |
| **1** | **January: report #1** | A re-runnable script over (page export) + (booking export with bill-to) + the SCI location list, producing the monthly file in §7. Manual inputs for escalations and turnaround | A script (`scripts/`, tests per `§8`) and asks 1 and 5 |
| **2** | Spring | Automated from `created_via_portal` and event logging; corporate view inside the portal (strategy Idea 4) | Asks 2 and 3, then the portal build |

**Fallback if ask 1 is declined:** the references can still come from Kyri or Alex as a typed list for step 0 and as a monthly CSV for step 1. Nothing about the SCI meeting depends on the button existing.

---

## 7. The monthly SCI pilot report: field specification

**Purpose.** This is the single ask of 2 December. One file per month, one named recipient at SCI, built by a script, reproducible from the same inputs.

**Hard rules, in order of priority.**

1. **`§7.2`: decedent and family data are excluded at the query**, by an explicit column allowlist, not removed afterwards. The report carries counts and booking references only. The allowlist is recorded in the script's `.meta.json`. `legal-risk` checkpoints report #1 before it leaves CSI.
2. **Invoice bill-to is non-negotiable.** A booking counts as CSI-billed SCI volume only if its bill-to is the SCI location, or an SCI legal entity on a list that Ethan and Donald agree. A booking whose bill-to is a partner is **excluded from the CSI-billed count and from every ratio**. **Default (Ethan to confirm):** the SCI-facing report states the basis in its definition line ("bookings invoiced by CSI to the location") and does not name the partners or describe their volume (`CLAUDE.md §5` treats NMS, IMS and Bergen as allies). The *internal* reconciliation sheet shows the excluded count, so the exclusion is auditable inside CSI.
3. **Internal cost and margin never appear** (`§7.1`; `§7.3` for anything about CSI's rate card).
4. **Location level by default.** Counts of bookers per location; **no individual booker names** in anything SCI receives unless SCI's named recipient asks. Naming SCI staff by activity reads as monitoring them.
5. **Reconciles.** The sum of the report's invoiced amounts ties to QuickBooks for the same booking references, with the difference printed. If it does not tie, the report says so and by how much.

### A. Header block

| Field | Notes |
|---|---|
| Reporting month, data cut timestamp | Cut date is stated; late changes appear next month, flagged |
| Definitions version | Increments on any change; the change is described on page one |
| SCI location list version and date | The list of in-scope locations; the denominator for every adoption figure |
| Basis line | "CSI-billed bookings, by invoice bill-to; flight-date basis for volume, invoice basis for amounts" |
| Reconciliation line | Bookings in report; bookings in booking export for the same locations; difference and why |

### B. Per location, per month (one row each)

| Field | Source | Ready for #1? |
|---|---|---|
| SCI location id, name, SCI location code | OMS master + SCI register | Yes (`sci-location-trajectory.csv`) |
| Bookings (CSI-billed) | Booking export with bill-to | Needs ask 5, or interim manual pull |
| Bookings via portal; via phone or email | `created_via_portal`, or anti-join on page refs | Yes, interim |
| Lane: origin gateway, destination, domestic or international | Booking export (lane fields) | Needs EA-45-02 lane columns |
| Invoiced amount | QuickBooks by booking reference, or booking export once invoiced amount is in it | Donald's tie in step 0 |
| Escalations (count and how each resolved) | Booking desk log | Manual, acceptable for #1 |
| On-time performance | OMS | **May not be instrumented. Say so in the report if not** |
| Documentation turnaround | `compliance` baseline (same metric as the EWA report's recommendation 6) | Manual, acceptable for #1 |

### C. Portal block (one section, whole-group and per location)

| Field | Definition |
|---|---|
| Locations **invited** | On the pilot list SCI gave CSI |
| Locations **onboarded** | At least one portal account exists |
| Locations **active** in month | At least one portal booking in the month |
| Active share | Active ÷ onboarded, **and** active ÷ universe (1,582), both shown |
| Portal share of bookings | Portal ÷ CSI-billed bookings, **only at onboarded locations** |
| Bookers per active location; repeat bookers | Counts and a distribution, no names |
| Time-to-book | Median, when asks 3 is built; blank and labelled until then |
| Draft or abandoned requests | Same |

### D. The audit pack (one table, one row per booking, same month)

Booking reference, location id, flight date, origin and destination, status, invoiced amount, channel (portal / phone-email), bill-to class (self / SCI entity). **No decedent, family, free-text or document field.** SCI can check any row against its own records. This is the file that makes the report auditable, and it costs almost nothing once the export exists.

### E. What the report does *not* include, deliberately

Cost, margin, rate-card detail, partner names, anything per individual person, anything that reads as a price comparison (`§7.1`: an external pricing claim is gated every time).

### Instrumentation of the report itself (`§9.2`)

Success is not "report sent." Track: report #1 delivered and **acknowledged** by a named person by 31 Jan 2027 (the strategy's own metric); number of SCI-requested changes to the definitions after report #1 (a sign the record is being *used*); number of rows SCI challenges or corrects (a sign it is being *checked*); and hours to produce, so the "automate or go quarterly" decision in the strategy is made on a measurement.

---

## 8. Correction 2: free deployment for promotion, modelled

**The proposition.** Portal available to every SCI location at no cost, in exchange for SCI promoting its use. Everything else is unchanged: air rates and secondary-service fees stay as they are, and no booking fee is introduced. Ethan should say "no cost to deploy or use" and not "free service". **Written terms, if any, go through counsel** (`§7.5`: no binding language from an agent); on 2 December this is a stated intention.

### Why it is stronger than the $999 tier

- It costs SCI nothing, so the vendor leader has no budget to defend.
- It asks for something SCI can give: attention and a channel.
- It avoids the Developer's **30% share of subscription fees net of costs** (agreement Ex. C §6), which a paid tier would trigger.
- Every adopting location becomes harder to displace. **This is a thesis, not a measurement**: nobody has yet shown portal-active accounts retain better than phone-only ones. The pilot report is how CSI gets that evidence, and the analysis design belongs with `data-analyst`.

### What it costs CSI

**Three costs. Only the first has a number today.**

**1. The channel cost to the Developer.** 1.5% to 3.5% of every dollar CSI invoices on a customer-initiated portal booking, on the marginal tier of *total* portal revenue (§3).

| Per booking at SCI's average yield ($1,087, `sci-revenue-by-year.csv` method) | Developer share |
|---|---|
| Bottom tier, 1.5% | **$16.31** (16.305) |
| Top tier, 3.5% | **$38.05** (38.045) |
| Rate-card gross margin on that booking, 35% domestic `[ESTIMATE, rate-card margin per carrier-margin-resolved.md, excludes cost to serve, SCI's domestic share unknown]` | $380.45 |
| Net of 1.5% share | **$364.14** |

**2. Desk and support load.** Onboarding, password resets, "how do I" calls, bookings that arrive incomplete and are finished by an agent. **No measurement exists** (`CLAUDE.md §4.3`: cost to serve is not instrumented). The split is `§9.6`: **Vadim** owns minutes per booking and per onboarding; **Donald** owns what an hour costs. I do not combine them, and I have not guessed either.

**3. Build cost.** Today the admin Portal Customer Onboarding page is one home at a time (pick a home, its emails become users, create). Of the 1,582 funeral-home-line locations, **the OMS master labels about 300 as SCI** and about 390 more match the register without a label (`sci-match-tiers.csv`), so **on the order of 900 or more locations plausibly have no OMS record at all** `[ESTIMATE, upper bound; matches include other product lines]`. Deploying to "all locations" without a manual onboarding queue means either a bulk-provisioning feature or self-registration on first booking (an existing design decision, [86f9e25c]). Cost unknown; Kyri and Alex classify.

### The design choice that keeps the cost in check

**Make access universal and pace the promotion.** The offer is "every location may use it." The cost is driven by *active* locations, not deployed ones, and CSI controls active locations through the promotion schedule (§9). Do not pre-create 1,582 accounts. Stage promotion cluster by cluster, and size each stage with Vadim before it starts. A surge of 100 first-time users in a week is a desk event.

### The two payback tests

**Test A. A phone booking that moves to the portal (not incremental).** CSI gains nothing in margin and **pays the Developer 1.5% to 3.5%** (the $16.31 to $38.05 above). It breaks even only if the desk saves enough time. The break-even is a hurdle, not an estimate:

| Minutes the desk saves per migrated booking | Hourly value of desk time needed to break even at 1.5% | At 3.5% |
|---|---|---|
| 10 | $97.83 | $228.27 |
| 20 | $48.92 | $114.14 |
| 30 | $32.61 | $76.09 |

**Donald supplies the actual hourly figure.** If the portal does not remove at least this many minutes per booking, a migrated booking is a net cost, and "tech must reduce work" (`CLAUDE.md`) becomes a P&L result and not a slogan. **This is why the desk time-study (§12, handoff to `operations`) is the item that decides whether the offer pays.**

**Test B. A location ships more because it is on the portal (incremental).** Break-even incremental bookings per active location per year = annual support cost S ÷ $364.14.

| Annual support cost per active location (a dollar grid, **not** an estimate) | Incremental bookings needed |
|---|---|
| $500 | 1.4 |
| $1,000 | 2.8 |
| $2,500 | 6.9 |

For scale: SCI locations that shipped in 2025 averaged **8.94 bookings** (`sci-footprint-by-year.csv`). A $2,500 support cost would need a 77% uplift on the average location; $1,000 needs about 31%. **The retention case is the alternative:** a retained location is worth about **$3,401 a year in gross margin** (8.94 bookings × $1,087 × 35%) `[ESTIMATE, same limits]`, and it is the value of the thesis if portal-active locations really do stay.

**Network scale** (arithmetic on 1,582 locations; **incremental bookings per location is unknown and nobody has measured it**):

| Active share of 1,582 | Active locations | Gross margin at 1 incremental booking each | At 3 |
|---|---|---|---|
| 1% | 16 | $5,826 | $17,478 |
| 5% | 79 | $28,767 | $86,301 |
| 10% | 158 | $57,534 | $172,602 |
| 25% | 396 | $144,199 | $432,598 |

These are *before* support cost and build cost. They are not a forecast; they size how much any plausible outcome is worth against SCI's existing ~$1.05M annual revenue.

### What this means in one paragraph

**The offer pays if either (a) the portal saves the desk real minutes per booking, or (b) portal-active locations retain or grow materially better, and the report in §7 measures both within a quarter.** It does not pay on migrated bookings with no desk saving, because the Developer share makes those cost money. **That test is cheap to run and must run before the offer is broadened beyond the first two clusters.**

### Gates (my proposal; Ethan and Vadim set the numbers)

1. **At 90 days from the first SCI promotion:** desk touches per portal booking compared with phone, from the §12 sample. If portal is not lower, **stop broadening** and fix the flow.
2. **Escalations at portal-active locations** are not higher than at comparable phone-only locations.
3. **Active share of the top-10 locations** (57.9% of SCI volume): the first measure of whether promotion reached the locations that matter.

### Risks, plainly

- **SCI's own third-party review.** A group-wide deployment may trigger SCI's vendor-risk or IT security review, and document upload is already held for a privacy legal review. **Ask Pam early what SCI needs**; the duration is unknown and could be the real critical path.
- **Developer incentive.** CSI's payment grows with portal adoption. That is a structural fact to model (finance), not an allegation.
- **Yield dilution.** SCI volume runs about 17% below CSI's average yield (`sci-relationship-evidence.md`). More SCI volume, even incremental, is lower-margin per booking than CSI's book.
- **The portal's value to the director.** Funeral directors phone. A portal that SCI promotes but that adds a step will be abandoned, and SCI will attribute that to CSI.

---

## 9. What "promote its usage" has to mean: ranked by worth to CSI

**Method.** Worth = (locations reached that actually ship) × (likelihood a promoted location books through the portal) × (how long the effect lasts) ÷ (desk load it creates when it lands). No measurement exists for the middle terms, so this is a reasoned ranking, and **every row below carries a source tag so the first report measures which form worked** (`§9.2`: instrumentation precedes spend).

| Rank | Form | Reach | Why this rank | What CSI must do | Risk |
|---|---|---|---|---|---|
| **1** | **A standing placement where a director orders a vendor.** CSI is already an approved SpenseMart vendor (brain: company-facts); the listing, and SCI's written how-to-ship-remains procedure, carry "book through the portal, or call us" with a link | Every location, at the moment of need | The only form that reaches a director when they have a case. Costs SCI a one-time edit. Lasts. Highest conversion per unit of SCI effort | Confirm what the listing can carry. One landing page that is the phone number **and** the portal | Unknown what SpenseMart permits. Ask Pam |
| **2** | **A named SCI leader introduces CSI's portal to the top-volume locations directly.** Top 10 locations are 57.9% of SCI volume; Florida, Hawaii and Nevada are 78% | About 10 to 25 locations, **most of the volume** | **Highest worth per introduction, by an order of magnitude.** Moving ten locations matters more than reaching a thousand. This is also where the desk can be ramped safely | A short list of locations and what to say; a named CSI contact for each | Borthwick (Honolulu) is partner-billed: **exclude it from the target list**. Top-10 may include other partner-dominant locations |
| **3** | **A live session** (Kyri and Alex, or a CSI agent) opened by an SCI regional leader, for directors in the same cluster | A cluster, 20 to 50 directors | Converts those who attend; builds the peer proof the audience trusts. Not durable on its own | Presenter time; a recording | Kyri and Alex time is the scarcest on the team; budget it |
| **4** | **Inclusion in new-director onboarding and the vendor training deck** | New hires only | Durable and cheap, but slow: it reaches people as they start, not the 138 active locations | A two-slide insert | Slow |
| **5** | **Peer testimonials circulated by SCI** (the Palm testimonial collection already underway) | Those who read it | Credible with this audience; supports 1 to 3 rather than replacing them | Collected by Otto and Stacy | Needs director consent; `§7.2` no family detail; each needs Ethan's approval |
| **6** | **A mention in a vendor bulletin or newsletter** | Broad, shallow | One-off, passive, low conversion; directors skim | Nothing | **Do not accept this as the whole commitment** |

### What "promote" should mean, minimum

Put in these terms in the room. It is concrete without being a contract:

1. **A named person at SCI who owns it** (the same person who receives the monthly report).
2. **One standing placement** (rank 1).
3. **One direct introduction to a named list of top-volume locations** (rank 2).
4. **The monthly report is how both sides see whether it is working.**

**A bulletin mention alone is not "promotion".** If that is all SCI offers, CSI should treat the deployment as a pilot extension, not a rollout.

### The tag (`§9.2`)

Every promotion form gets its own link or code, so the first login records **which form brought the director**. Without it, the report in §7 shows that adoption rose but not why, and the next prioritisation round cannot tell a form that worked from one that did not.

---

## 10. The premises that change in the strategy

| Strategy statement | Now |
|---|---|
| §2 hard constraint: no system-dependent turnaround, platform SLA bounds Ethan | **Withdrawn** (§2 above). Contractual SLA point survives, narrowly |
| §4 precondition 4: "a platform position that supports a real SLA" | Applies to a *written* SLA in the primacy conversation, not to what Ethan says in December |
| §2: "CSI cannot report pilot usage" | **Wrong.** The admin page gives bookings, homes, people, routes, charges. Denominators, phone split, time-to-book and abandonment are still missing |
| Elite tier ($999/month) in `context/oms-saas-product.md` | Replaced by **free deployment for promotion**, as Ethan said. The paid tier is also now less attractive: the Developer takes 30% of subscription fees net of costs |
| Idea 5: rebate against a measured baseline, with "revenue share" language | A customer rebate **does not exist**. The page's rev-share panel is CSI's payment to the Developer. Do not describe a rebate as already built. It stays a structure for `pricing-strategist` and Donald |
| §1: "123 shipping locations against the 4,439 mapped is ~2.8%" | **Superseded** by `reports/sci-relationship-evidence.md`: the denominator is 1,582 funeral-home-line locations; 8.7% active, 15.7% ever shipped. Raised only because the free-deployment arithmetic must use the same denominator |
| The one ask is the monthly report | **Stands, and is now the verification instrument for the promotion commitment** |
| Idea 4: corporate reporting in the portal | Stays "direction, not date." The report in §7 is the deliverable version |

---

## 11. Defaults I took, open questions, and what would raise confidence

**Defaults taken and flagged (`§7.1`, reverse if wrong).**

1. **All four named homes are treated as SCI.** Three by OMS group field; Lincoln Heights by register match (inference).
2. **The page is the Developer's calculation tool**, from the tier match, not from seeing it.
3. **The page's "total charges" is not treated as invoiced revenue.**
4. **Report scope excludes partner-billed bookings silently from the SCI-facing report** (definition line only, no partner names). Reverse if Ethan wants the existence of partner routing disclosed.
5. **No booker names in anything SCI receives.**
6. **Free deployment means access for all, promotion paced.** Ethan said "all their locations"; I kept the offer universal and made only the *promotion* staged.

**Open, and who has the answer.**

| Question | Who | Unblocks |
|---|---|---|
| The 13 booking references; confirm page = Developer's calculation; how "portal" is defined | Kyri or Alex | §5 checks 1, 2, 5; the whole §4 status update |
| Tie the 13 to invoices | Donald | Revenue, not "charges" |
| Does portal booking reduce desk touches? Onboarding minutes? | Vadim, Susej, Kim (hours); Donald (cost per hour) | Whether the offer pays (Test A) |
| What can the SpenseMart listing and SCI procedure carry? | Pam | Rank 1 form |
| Which locations were invited, and did the August introductions go out? | Cheryl or Ethan's records | Invited denominator; whether the Florida chapels were ever approached |
| Does SCI require a vendor security or privacy review for a group-wide rollout? | Pam, via Ethan | Critical path |
| Revenue Share Year reading; whether a customer rebate credit reduces the Developer's base | Counsel, via `legal-risk` | Any rebate structure |

**What would raise confidence most:** the 13 references. One request that settles §4, §5 and the first step of §6.

---

## 12. Handoffs raised

- `handoffs/HANDOFF-sci-portal-finance.md`: product → finance. The revenue-share finding; model the Developer share as a channel cost; tie the 13 bookings to invoices; no rate to SCI before Donald.
- `handoffs/HANDOFF-sci-portal-gtm-strategist.md`: product → gtm-strategist. The revised premises (§10), the proposition and the promotion ranking.
- `handoffs/HANDOFF-sci-portal-operations.md`: product → operations. Desk load from free deployment: the time-study that decides Test A, onboarding minutes, ramp capacity.

**Recommended for pm-orchestrator to route:** counsel questions R1 to R3 from the agreement review to `legal-risk`, because the answer to "what counts as portal-initiated" decides both the Developer payment and what the adoption metric means. Two brain proposals are filed (SLA constraint withdrawn; the rev-share panel's identity) under `context/brain/_proposals/`.

## Sources

Repo: `CLAUDE.md §§1, 2, 4.3, 5, 6, 7.1, 7.2, 7.3, 7.5, 7.6, 9.2, 9.6`; `reports/sci-footprint-strategy-2026-12.md`; `reports/sci-relationship-evidence.md`; `reports/freightflow-agreement-review.md §2`; `reports/oms-export-spec.md` (fields 18, 41; D3; EA-45-08); `reports/pending-approval/engineering-ask-2026-46.md`; `handoffs/HANDOFF-sci-portal-product.md`; `handoffs/HANDOFF-partner-routing-revops-product.md`; `context/brain/initiatives/customer-portal.md`; `context/brain/open-questions.md` (4, 10, 18).
Data (aggregates only, read by script, `-I` mode): `data/raw/shipments-since-2022-20261110.xlsx` (four columns, no decedent or family fields), `data/raw/oms-funeral-homes-20261109.csv` (business records), `data/derived/sci-location-trajectory.csv`, `sci-denominator.csv`, `sci-footprint-by-year.csv`, `sci-revenue-by-year.csv`, `sci-match-tiers.csv`, `sci-unlabelled-locations.csv`, `partner-billed-homes-manifest-20261118.csv`.
Not in the repo and not seen: the Portal Revenue Tracking page and its screenshot. Method for §1, §4 and §5 counts: ad-hoc aggregation in the session scratchpad; the monthly version becomes `scripts/` at report step 1.
