# OMS export specification

**Owner:** product · **Date:** 2026-11-02 · **Task:** TASK-0003 · **Spec version:** 1.0
**Status:** DRAFT for Ethan. Travels with `reports/pending-approval/engineering-ask-2026-45.md`, which is the ranked ask and the authoritative version of what is being requested.
**Audience:** Kyri and Alex, through the Monday ask. Written to be built without a follow-up call.

**Confidence.** High on what CSI needs and why. Medium on the order of work. **Low on which fields already exist in the OMS** — CSI cannot see the schema. So the field table has a column for the engineer to fill (Exists / Derivable / Does not exist), and "does not exist" is a feature request, not a dead end (`CLAUDE.md §9.6`). A one-page reply in that shape is worth more than a meeting.

---

## 0. The answer

CSI needs one file: **one row per booking, nightly, in a Drive folder, built from an explicit list of columns that cannot contain decedent or family data.** Because that is a build, it is asked for in three layers, each useful without the next, so a "no" to a bigger layer is never a "no" to a smaller one.

| Layer | What | Size of the ask | What it unblocks |
|---|---|---|---|
| **D0 Cohort extract** | 4 columns, full history: `booking_id`, `shipping_funeral_home_id`, `flight_date`, `status` | One query, run once | Active, new, reactivated and churned accounts, churn rate, shipments per retained account (`context/metric-definitions.md` M-12 to M-17); the volume decomposition `CLAUDE.md §2` says is unanswered |
| **D1 Booking-level file** | 18 Tier 1 columns, plus Tier 2/3 as they exist; dated CSV, nightly (weekly is acceptable) | One query plus a schedule | Lane volume, corridor mix, account value, realized margin, cancellation and rebooking rates, portal adoption, CAC denominator |
| **Companion files** | Funeral home master (D3), carrier invoice lines (D4), contracted rates for every carrier (D5) | Ride the same schedule | The HubSpot crosswalk, per-shipment carrier cost, international margin |

**Hard requirement on every file: decedent and family fields are excluded at the query, by an explicit column allowlist, never removed afterwards (`CLAUDE.md §7.2`).** Section 4.2 names the columns.

**Manual fallback if engineering declines** (Section 12): partial and honest about it. Donald's QuickBooks sales-by-customer summary for account value and churn at monthly grain; carrier invoice files for lane volume on the carriers that send them. It does not give lane x account x cost per booking, cancellations, or cohorts by origin.

---

## 1. Ground facts, so nobody re-litigates them

**No export function exists on the Flight Confirmation List, the Ready to Invoice List or Collect Shipments** (Ethan, 2026-11-02). This is not a "turn on a button" request and is not to be re-tested next cycle. Those pages also display the decedent's name by design (`CLAUDE.md §7.2`), so a screen-copy route would put names on exactly the path that rule forbids.

| Source | What it gives today | Status |
|---|---|---|
| Analytics Export (admin) | Daily or monthly **totals only**: revenue, bookings, average revenue per booking, count of bookings missing revenue, count missing a funeral home link | Exists. Aggregate. Its `Period` is a flight or service date, not a creation date: the 2026-11-02 pull carries 2026 rows up to Nov 13 and its header totals (115 bookings, $150,742.43) equal the sum of those rows (`context/metric-definitions.md` M-02; arithmetic re-checked for this spec) |
| Rates exports (published, contracted, special) | Dated 2026-11-02 | Exist. Carry the defects in Section 10 and the coverage gap in Section 8 |
| Funeral Home Records bulk CSV | Documented in the admin tools (`reports/analytics-reconciliation.md`) | **Unverified.** Ethan's 2026-11-02 confirmation covered the three pages above, not this one. First thing to try (Section 6) |
| Airline Invoice Audit | A page that compares carrier invoices to CSI bookings and contract rates | Export function unknown |
| Skipped Validation Bookings | A page listing bookings that bypassed validation | Export function unknown |
| Carrier invoices | Hand-delivered files in `data/raw/carrier-invoices/`, Sep-Oct 2026: United, Delta, and one further file (`SOA-2026-10-26.xlsx`) not yet analysed | Partial: two carriers analysed, a few weeks. Decedent names sit in named columns (Section 4.2) |
| QuickBooks | Invoice system of record (`reports/freightflow-agreement-review.md §2.5`) | Not yet asked. The fallback in Section 12 |

**Sizing.** About 43,600 bookings across the whole OMS history (`context/metric-definitions.md` M-23); 29,303 from Jan 2024 through Aug 2026 (10,867 + 10,985 + 7,451, `CLAUDE.md §2`). The full file is a few MB to low tens of MB. Volume is not the difficulty.

---

## 2. Datasets, and how they map to the ask

| Dataset | Ask item | Notes |
|---|---|---|
| D0 Cohort extract | EA-45-01 | Strict subset of D1. Listed separately so a "no" to D1 is not a "no" to D0 |
| D1 Booking-level file | EA-45-02 | The nightly job lives here |
| D3 Funeral home master | EA-45-03 | May need no build |
| D6 Timestamps (booking duration) | EA-45-04 | Questions first; fields join D1 if they exist |
| D4 Carrier invoice lines | EA-45-06 | |
| D5 Contracted rates, all carriers | EA-45-07 | |
| Quote persistence | EA-45-08 | Question first |
| Rate-table defects (what "fixed" looks like) | EA-45-05, -09, -10 | Section 10 |
| Funeral home required before invoicing | EA-45-11 | Section 4.7 |

---

## 3. D0 — Cohort extract (the smallest thing that unblocks the most)

**Why separate.** `HANDOFF-T0016` (data-analyst): six binding metrics are blocked on a funeral home ID and a date and on nothing else, the classification logic is already written and tested (`src/metrics.py`), and the answer would come out the day the file lands.

| Column | Type | Definition |
|---|---|---|
| `booking_id` | string | OMS booking reference. One row per booking. Free, and it makes duplicates and later joins possible |
| `shipping_funeral_home_id` | string | ID of the funeral home record that tenders the shipment. **Null where the OMS has none. Do not drop those rows** (823 across history; sizing them by period is a stated need) |
| `flight_date` | date | Scheduled departure date of the first leg. The date the analytics export groups on (M-02 binds cohort work to it) |
| `status` | enum | Raw OMS status. Needed because "landed" means completed and not cancelled (M-02); CSI cannot apply that without it, and should not ask you to guess the definition |

- **Period:** all of history, no date filter (the OMS begins 2022-09-01; cohort classification needs the look-back, M-12 to M-15).
- **Run:** once, CSV, delivered to the Drive folder (Section 4.1). No schedule needed.
- **Floor.** If anything above is a problem, the floor is `shipping_funeral_home_id` plus one date. `booking_id` and `status` are the two additions product made to the data-analyst's two-column request; drop either rather than hold the extract. If excluding non-completed bookings in the query is easier than sending `status`, do that and tell us the filter you applied.
- **Difference from the request as written.** The data-analyst asked for "one row per landed booking" and no status. We send all statuses and let CSI filter, because the status filter the analytics export applies is itself unconfirmed (M-02) and CSI would rather see the values than inherit a guess.

---

## 4. D1 — Booking-level file

### 4.1 Parameters

| Parameter | Value |
|---|---|
| **Grain** | One row per booking. `booking_id` unique. Drafts, cancelled and replaced bookings are included, with their status; CSI filters |
| **Period** | **Required:** every booking created on or after 2024-01-01. **Requested, same query with an earlier date:** 2022-09-01 (OMS start) as look-back for first-booking dates. Pre-2023 rows reflect migration artifacts (`context/brain/company-facts.md`); analysis treats them as look-back only |
| **Cadence** | v0: one manual run of the Tier 1 columns. v1: nightly at about 03:00 ET, **full snapshot of every row in the window**, not incremental, because status, revenue and cancellation change after creation. Weekly is acceptable if nightly is a burden: nothing CSI does needs intraday freshness |
| **Format** | UTF-8 CSV (RFC 4180), header row, comma, LF. Dates `YYYY-MM-DD`. Timestamps ISO 8601 UTC (`2026-11-02T14:03:22Z`). Booleans `true`/`false`. Money as decimal USD, two places, no symbol, no thousands separator. **Empty means null; null is not 0.** IDs are strings (preserve leading zeros) |
| **File names** | `bookings_YYYYMMDD.csv` and `bookings_YYYYMMDD.manifest.json` (run time UTC, `spec_version`, row count, created-date window, column list in order). Files are **new each run and never overwritten** |
| **Retention** | Keep the last 35 nightly files and the first-of-month file forever. Snapshots are how CSI tells a restated number from a wrong one |
| **Delivery** | A Drive folder CSI creates and owns ("OMS Exports"). The job writes files into it. Who can see the folder is Ethan's call (`CLAUDE.md §7.1`); how the job authenticates is yours. Agents read the folder through the existing Drive connector. **Nothing in this request gives anyone write access to the OMS** |
| **Failure** | No partial file. A missing night is visible as a missing file; CSI's weekly check catches it. No alerting build asked for |
| **Companion files** | D3, D4 and D5 use the same folder, naming and format: `funeral_homes_YYYYMMDD.csv`, `carrier_invoice_lines_YYYYMMDD.csv`, `contracted_rates_YYYYMMDD.csv` |

### 4.2 PII — a requirement, not a preference

**Decedent and family fields are excluded at the query that produces the file. They are not removed afterwards, by anyone, in any script or spreadsheet** (`CLAUDE.md §7.2`). Once a name has reached a temp file, a log or a terminal it cannot be recalled.

1. **Allowlist, not denylist.** The query names exactly the columns in 4.3. No `SELECT *`. Adding a column is a spec change (new `spec_version`), not a convenience.
2. **No intermediate copy.** No file, table, log line or error message outside the OMS may contain an excluded column, including temp files and failure output.
3. **Free text is excluded entirely.** Notes, remarks, special instructions, comments, internal memos, document names, email subjects and bodies. That is where names leak. Every string column in the file is an ID, a code, an enumeration or a funeral home's business name.
4. **Named exclusions.** Observed in CSI data, or required by concept:

| Concept | Where observed, or why required |
|---|---|
| Deceased name | Flight Confirmation and Ready to Invoice lists (displayed by design); pickup lists (`Deceased Name`); AWB and TSA documents (throughout) |
| Delta invoice `Nature of Goods`, `Shipping Location` | Carrier invoices (`CLAUDE.md §7.2`) |
| United invoice `Shipper Reference` | Carrier invoices (`CLAUDE.md §7.2`) |
| Invoice `Customer` | Dropped as a precaution by `scripts/realized_margin.py`; do not export it |
| Family or next-of-kin name, phone, email, address | Required by concept |
| Consignee name, phone, email, address **when not a funeral home record** | A receiver can be a family address. Receiving fields come only from the funeral home table (4.3 rows 21 and 22) |
| Pickup address, place of death | Pickup airport is fine; street address or facility name is not |
| Date of death, birth, age, sex, cause of death | Required by concept |
| Death certificate number or contents; burial transit permit number; passport or ID numbers | Required by concept |
| Attached document names or images | Required by concept |
| Booking agent identity, and any per-agent field | `CLAUDE.md §7.7`: this is process instrumentation, not performance monitoring |
| Individual portal user names and emails | Required by concept; only a count appears (D3) |

5. **Anything we did not think of.** If you know of any other column in the booking tables that can carry a person's name or contact details, leave it out and tell us which, so this list gets longer.
6. **Verification.** (a) CSI compares every file's header row to this spec and rejects any file with a column that is not on the list. (b) Before the first delivery, the engineer states in writing which tables and columns the query reads. (c) CSI looks at the first file's business-name columns for person-like names. (d) If a name appears anyway, Ethan is told the same day, plainly (`CLAUDE.md §7.2`).

### 4.3 Fields

**Tier 1 is the smallest file that unblocks the churn, lane, corridor, account-value and margin work. Tier 2 each has a named consumer. Tier 3 is lowest priority and conditional.** If a Tier 1 field is a problem, say which; do not hold the file.

Last column is for the engineer: **E** exists as named, **D** derivable (say how), **N** does not exist.

| # | Field | Type | Definition and allowed values | Tier | Unblocks (who) | E/D/N |
|---|---|---|---|---|---|---|
| 1 | `booking_id` | string | OMS booking reference, unique, never reused | 1 | Everyone: primary key, dedupe, joins to D4 and D6 | |
| 2 | `awb_number` | string | AWB as stored (`NNN-NNNNNNNN`); null until issued. If several, the AWB of the first revenue leg, and tell us if bookings can carry more than one | 1 | finance, pricing, operations: the join to carrier invoices (D4) and realized margin (M-08) | |
| 3 | `booking_created_date` | date | When the booking record was first created, including as a draft | 1 | data-analyst (first-booking date, cohorts), marketing-lead (CAC window, M-18) | |
| 4 | `flight_date` | date | Scheduled departure of the first leg | 1 | data-analyst (tie-out to the analytics export, M-02), operations | |
| 5 | `landed_date` | date | Date recorded as arrived at the final destination airport. If the OMS holds only a scheduled arrival, send it as `scheduled_arrival_date`, leave this null and say so in the data dictionary | 1 | Everyone using "landed booking" (M-02, M-03); finance | |
| 6 | `status` | enum | Raw OMS status, unmodified. Please supply every value with a one-line meaning (known: Pending, Booked, Waiting Airline, Booking saved as draft) | 1 | Everyone: decides which rows count (M-02) | |
| 7 | `shipping_funeral_home_id` | string | ID of the funeral home record that tenders the shipment. Null only where the OMS has none; never drop the row | 1 | revops-crm (HubSpot crosswalk), data-analyst (M-12 to M-17), sales-lead, gtm-strategist, corpdev (concentration) | |
| 8 | `shipping_funeral_home_name` | string | Business name from that record | 1 | revops-crm: sanity check on the join | |
| 9 | `origin_airport` | IATA | Departure airport of the first leg | 1 | pricing-strategist, gtm-strategist, operations | |
| 10 | `destination_airport` | IATA | Final arrival airport | 1 | pricing-strategist, gtm-strategist, market-intel | |
| 11 | `destination_country` | ISO 3166-1 a2 | Country of the destination airport | 1 | gtm-strategist, market-intel, compliance (country priority), corpdev | |
| 12 | `is_international` | bool | The OMS's own flag as the desk uses it. If none exists, derive `origin_country` differs from `destination_country` and say so | 1 | pricing, finance (the 35% / 41% split), corpdev | |
| 13 | `airline` | string | Airline holding the AWB, **spelled exactly as in the rates exports' `airline` column** (e.g. "United Airlines", "IAG") so it joins without a lookup | 1 | finance, pricing, operations | |
| 14 | `shipment_rate_type` | enum | Casket, Cremated Remains, and any other value the OMS uses. List them | 1 | pricing (M-07 needs it), finance | |
| 15 | `revenue_total` | decimal | Total charged to the customer, all lines, USD. State in the dictionary whether this is invoiced or booked, and whether tax is in it. **Null = not priced; 0.00 = priced at zero** | 1 | Everyone. Ties to the analytics `Total Revenue` (M-06, M-11, M-24) | |
| 16 | `is_cancelled` | bool | The OMS cancelled state | 1 | operations, finance, data-analyst (M-02) | |
| 17 | `is_rebooked` | bool | True where the booking replaced another or was itself replaced (the OMS flag as is) | 1 | operations (M-22) | |
| 18 | `created_via_portal` | bool | True where the customer created the request in the customer portal; false where an agent created the booking | 1 | product (portal adoption), data-analyst, sales-lead | |
| 19 | `status_changed_at` | timestamp | Time of the last status change | 2 | operations | |
| 20 | `scheduled_arrival_date` | date | Scheduled arrival at the final destination | 2 | operations; used if `landed_date` does not exist | |
| 21 | `receiving_funeral_home_id` | string | ID of the receiving party **only where it is a record in the funeral home table**; else null | 2 | corpdev (partner network economics), gtm, sales | |
| 22 | `receiving_funeral_home_name` | string | Business name from that record only. **Never from a free-text consignee field** | 2 | as above | |
| 23 | `shipping_funeral_home_group_id` | string | Parent group from the funeral home record | 2 | corpdev, sales-lead, gtm (enterprise rollup) | |
| 24 | `origin_country` | ISO a2 | Country of the origin airport | 2 | pricing, finance | |
| 25 | `destination_state` | string(2) | US state, where `destination_country` is US | 2 | gtm, sales (domestic corridors) | |
| 26 | `gateway` | IATA | The CSI gateway the shipment is handled through, if the OMS records one | 2 | operations (gateway load), gtm | |
| 27 | `rate_type` | enum | `flat` or `var`, as in the rates tables | 2 | pricing | |
| 28 | `chargeable_weight`, `weight_unit` | decimal, enum | As priced | 2 | pricing, finance (variable rates cannot be checked without it) | |
| 29 | `revenue_air_charge` | decimal | The rate-based air charge to the customer | 2 | finance, pricing (the spread stream) | |
| 30 | `accessorials_total` | decimal | Sum of extra line items (consulate, pickup, drop-off, documentation, trucking, surcharges) | 2 | finance, pricing (the secondary-service stream; DR-001) | |
| 31 | `carrier_cost_expected` | decimal | Cost per the contracted rate at booking, if the system computes it | 2 | finance, pricing | |
| 32 | `carrier_cost_invoiced` | decimal | Total due on the matched carrier invoice; null until matched | 2 | finance (leakage), pricing (realized margin, M-08) | |
| 33 | `price_basis` | enum | Which price applied: published, discount, special, bundled, manual | 2 | pricing: the empirical answer to "which of two conflicting rates wins" (EA-45-10) | |
| 34 | `rate_row_id` | string | ID of the rate row used; null if manual | 2 | pricing, product: shows which duplicate rows are actually used | |
| 35 | `skipped_validation` | bool | The booking passed through Skipped Validation Bookings | 2 | finance (mispricing risk) | |
| 36 | `cancelled_date` | date | When cancelled | 2 | operations | |
| 37 | `cancellation_reason` | enum | Whatever codes exist (customer, airline, flight disruption, error...). List them | 2 | operations (open question #12, M-22) | |
| 38 | `rebooked_from_booking_id` | string | If this booking replaced another, that booking's ID | 2 | operations, finance (absorbed rebooking cost) | |
| 39 | `origination_channel` | enum | How the request reached CSI **as far as the system itself knows** (portal, parsed email, agent entry, other). **No agent tagging by hand** | 2 | product, data-analyst, sales | |
| 40 | `booking_created_at` | timestamp | Creation time | 3 | operations, data-analyst (EA-45-04) | |
| 41 | `request_received_at` | timestamp | When the request arrived (email received time, or portal submission) | 3 | operations: the start of the desk's turnaround KR (M-21) | |
| 42 | `submitted_to_airline_at` | timestamp | When the booking request was submitted to the airline | 3 | operations: the end of the turnaround KR | |
| 43 | `airline_confirmed_at` | timestamp | When the airline confirmed or rejected | 3 | operations | |
| 44 | `leg_count` | int | Number of flight legs | 3 | pricing (complexity), operations | |
| 45 | `routing` | string | Airports in order, hyphen-separated (`SFO-LAX-MIA-BOG`) | 3 | pricing (route choice, as in the routing note) | |
| 46 | `submitter_email_domain` | string | **Domain only**, never the address, and only where the submitter is a funeral home user | 3 | revops-crm (form-to-booking match, C16), marketing (CAC join) | |

Field 46 deviates from `HANDOFF-T0009`, which asked for the booking contact email. CSI cannot confirm whose address that field holds (it can be a family member's), and `§7.2` bars family contact data. A domain does the job for funeral homes and leaks nothing for families. **Lead source** (the brief listed it here) lives on the funeral home record (D3), because it is a property of the account relationship and duplicating it per booking would only create a second place for it to disagree.

**Tier 3 fields 40 to 43 are the booking-duration question (EA-45-04, Section 9).** Do not build them before CSI has the answer to what already exists.

**Charge lines (optional, Tier 3 sidecar).** If extra line items are stored as rows, a second file `booking_charges_YYYYMMDD.csv` with `booking_id`, `charge_code`, `charge_label` (from the catalog, not typed text), `amount`, `is_carrier_pass_through`. The OMS Extra Line Items catalog already lists codes (for example FS, fuel surcharge, flexible, default $0.00; `context/brain/_proposals/2026-11-02-donald-surcharge-priority.md`). This is how the United $33-per-shipment pass-through question (TASK-0004) gets answered across all carriers instead of 77 invoices. Lowest rank; present so it is not lost.

### 4.4 Where the answer may be "the system does not track that"

That is a feature request, not a fact about CSI (`§9.6`). CSI's guess at what may be absent, so it can be ranked rather than discovered:

| Possibly absent | Smallest version | Unblocks |
|---|---|---|
| Request-received, submitted-to-airline and confirmation timestamps; a status history | Stamp the two timestamps as a side effect of actions agents already take | M-21, M-10, the cost-to-serve chain (TASK-0008) |
| Cancellation reason; the link from a replacement booking to the original; any record of the rebooking cost CSI absorbs (~99% of the time, never measured) | Reason code plus the link. The cost is computed from carrier invoices, never typed in | M-22, open question #12 |
| Which price row priced a booking (`price_basis`, `rate_row_id`) | Two fields written when the price is applied | The 133-lane conflict question, answered from evidence |
| Origination channel finer than portal versus agent | Nothing: phone and typed-in email are probably indistinguishable to the system. The phone path stays, and the desk is not asked to tag | Portal adoption is still measurable from field 18 |
| Quote records | EA-45-08 | Win rate, quote-to-book |
| Expected carrier cost at booking | Leave null; D4 supplies actual cost | Realized margin |

### 4.5 Edge cases

- **Several AWBs or carriers on one booking.** One row. `awb_number` is the first revenue leg; D4 carries every AWB. Tell us if this happens.
- **Cancelled, then rebooked.** Both bookings stay as rows, linked by field 38. **State whether a cancelled booking carries revenue or has it reversed**, so sums do not double count. Whether the OMS creates a new booking record on rebooking is unconfirmed (M-01, M-22); CSI is also asking Kim and Susej, as it is a question about how the desk works.
- **Drafts.** Included, with their status. Revenue null if not priced.
- **Revenue null versus zero.** The analytics export reports a `Bookings Missing Revenue` count and its November pull contains a booking priced at 0.00. The two must stay distinguishable.
- **Edited bookings.** One row, current state. History belongs to D6.
- **Missing funeral home.** Exported as null. The row is never dropped.
- **Receiver is a family address.** Receiving fields are null. Nothing is read from a free-text field.
- **Test or duplicate-draft bookings.** Tell us how they are identified, or add `is_test`.
- **Currency.** USD. If anything else exists, add a `currency` column.
- **Hard deletes.** Tell us whether bookings are ever removed rather than cancelled.
- **Time zones.** Dates as the OMS stores them; state the assumption in the dictionary. Timestamps in UTC.

### 4.6 Acceptance — what CSI runs on the first file

Owner: data-analyst (`HANDOFF-T0003-data-analyst`). All re-runnable scripts, per `§9.3`.

| Test | Pass |
|---|---|
| **A. Header** | Columns equal this spec exactly, in order. Any other column rejects the file (the PII control) |
| **B. Key** | `booking_id` unique; row count equals the manifest |
| **C. Tie-out** | Monthly booking count and revenue, grouped by `flight_date`, compared with the analytics series (`data/derived/monthly-by-year.csv` and the November daily export), trying `flight_date`, `booking_created_date` and `landed_date` until one matches. Proposed tolerance 0.5% per month `[ASSUMPTION — data-analyst to set]`. **A gap is reported, not a rejection:** it is the OMS-to-legacy reconciliation defect (`CLAUDE.md §6`) finally visible at row level, and any month outside tolerance is listed with its cause or marked unexplained |
| **D. Null report** | Null rate per column. `shipping_funeral_home_id` null count compared with the known 823 lifetime and 59 for 2026 YTD (M-23); revenue nulls with `Bookings Missing Revenue` |
| **E. Enumerations** | Distinct values of `status`, `shipment_rate_type`, `price_basis`, `cancellation_reason` reported, and compared to the data dictionary |
| **F. Join** | Every non-null `shipping_funeral_home_id` exists in D3; every non-null `awb_number` is a valid 11-digit AWB whose first three digits match the airline |
| **G. Spot trace** | Ten bookings chosen by CSI by ID from the OMS screen agree field by field with the file. Done by Vadim or Susej, who already see those screens |

**Done** = A to F pass and C is reported.

### 4.7 Out of scope

Any decedent or family field; attachments; any agent-level field; write access of any kind; a real-time feed; dashboards; history before 2022-09; changes to pricing logic. Also out of scope here, and tracked as EA-45-11: stopping the next 823 bookings from losing their funeral home. The export makes it visible; it does not prevent it.

---

## 5. Portal adoption — what these fields compute

The retention thesis ("do portal-active accounts retain and grow better?") needs three inputs and no others: `created_via_portal` per booking (field 18), the portal fields on the funeral home record (D3), and the account classification in `src/metrics.py`. **Definitions of "portal-onboarded", "portal-active" and "share of bookings through the portal" are not in `context/metric-definitions.md`, and this spec does not invent them** (`handoffs/HANDOFF-T0003-data-analyst`). Until they are, the file simply makes them computable.

Instrumentation: the OMS records `created_via_portal` as a side effect of the booking path, so measuring adoption adds no work for the desk or for funeral directors.

---

## 6. D3 — Funeral home master

**Try this first.** The admin tools document a bulk CSV export of Funeral Home Records. If it works and carries the fields below, **there is nothing to build**: tell us who runs it and how often. If it works but lacks fields, only the missing columns are asked for. Ethan or Susej can test it in five minutes (`HANDOFF-T0009` asks for the same colleague-first check).

One row per funeral home record. Weekly is enough. `funeral_homes_YYYYMMDD.csv`.

| Field | Definition | Unblocks |
|---|---|---|
| `funeral_home_id` | The same ID as D1 field 7. Unique | revops-crm (the join key HubSpot lacks: no OMS key property exists there), data-analyst |
| `legal_name`, `dba_name` | Business names | revops-crm (matching on DBA variants) |
| `address_street`, `address_city`, `address_state`, `address_postal_code`, `address_country` | **Business** address | revops-crm, sales-lead, gtm (territory) |
| `business_phone` | Business line | revops-crm (match key) |
| `email_domain` | **Domain only**, not individual addresses | revops-crm (match key) |
| `parent_group_id`, `parent_group_name` | Corporate group (the OMS holds this hierarchy; `rates-special` carries `funeral_home_group_id`) | corpdev, sales-lead, gtm (SCI, Everstory, Carriage rollups) |
| `record_status` | Active, inactive, archived as the OMS uses | data-analyst |
| `record_created_date` | When the record was created in the OMS | data-analyst, marketing (CAC) |
| `portal_onboarded_date`, `portal_last_login_date`, `portal_user_count` | Dates and a **count**, never user names or emails | product (adoption), data-analyst |
| `has_special_rates` | True where the funeral home has customer-specific rates | pricing |
| `hubspot_company_id` | If the OMS stores one | revops-crm |
| `lead_source` | If stored. **CSI believes it is not**; HubSpot may be its system of record (C12), so revops-crm confirms before anyone builds it | marketing (CAC), finance, gtm |

**Excluded:** individual contact names, direct phones and emails, owner or director names, notes and any free text. HubSpot holds the contacts; this file exists to join accounts, not people.

Acceptance: `funeral_home_id` unique; every D1 ID exists here; duplicates by name and postal code are reported (account-resolution input for revops-crm, not a rejection).

---

## 7. D4 — Carrier invoice lines (the Airline Invoice Audit)

One row per AWB per carrier invoice, from the data behind the Airline Invoice Audit page. Nightly or weekly, `carrier_invoice_lines_YYYYMMDD.csv`.

| Field | Definition |
|---|---|
| `invoice_number`, `invoice_date` or `billing_period` | As on the carrier invoice |
| `airline` | Spelled as in the rates exports |
| `awb_number`, `booking_id` | The match; `booking_id` null if unmatched |
| `match_status` | Matched, unmatched, variance |
| `origin_airport`, `destination_airport`, `chargeable_weight`, `weight_unit` | As invoiced |
| `base_freight`, `miscellaneous_charges`, `taxes`, `total_due`, `currency` | The charge split. Today United's total includes about $33 per shipment above the contracted rate (TASK-0004, 77 AWBs); the split is what shows whether it is billed through |
| `contracted_cost_expected`, `variance_amount` | As the audit computes them |

**Excluded at the query:** United `Shipper Reference`; Delta `Nature of Goods` and `Shipping Location`; `Customer`; every remark or free-text column.

**Period.** From 2026-01-01 if the audit holds it; smallest version, the last 90 days for every carrier.
**Unblocks.** finance (leakage on all carriers, not two), pricing (realized margin by lane, M-08), operations (carrier performance), data-analyst (M-08, M-09). Today CSI works from hand-delivered files covering two carriers and a few weeks (85 AWBs, United and Delta, per `reports/pending-approval/booking-team-routing-note.md`), which is thin enough that the $358K extrapolation is labelled `[ESTIMATE]`.

---

## 8. D5 — Contracted rates, every carrier the system holds

Same columns as `rates-contracted-20261102.csv`: `airline, origin_type, origin, destination_type, destination, shipment_rate_type, rate_type, contracted_rate, currency, included_weight, weight_unit, flat_overage_surcharge, effective_as_of, source_reference`.

**The gap, measured on the 2026-11-02 files** (`rates-published-20261102.csv`, 6,919 rows; `rates-contracted-20261102.csv`):

| | Lanes |
|---|---|
| Published lanes belonging to the four carriers that have contracted rates (American, Delta, Southwest, United) | 478 |
| Published lanes belonging to **15 carriers with no contracted row at all** | **6,441** |
| Of those: IAG 5,565 · Emirates Sky Cargo 552 · Aeromexico 88 · Air India 57 · Philippines Airlines 57 · Lufthansa 53 · Amerijet 24 · Volaris 10 · Avianca 8 · Swiss Air 8 · Korean Air 7 · Copa 6 · Viva Aerobus 4 · IBC Airways 1 · El Al 1 | |

The carrier list in `CLAUDE.md §4.3` and `context/metric-definitions.md` M-07 names nine of these. Aeromexico, Air India, Philippines Airlines, Swiss Air, Amerijet and El Al are not named there and are in the file; flagged to the orchestrator.

**The question comes first.** Are contracted rates for those carriers loaded in the system at all? There are two possible reasons for the gap, and they need different fixes:
1. **Never loaded** (the Rates Reference mentions "Vadim's rate sheet" for the Volaris bundle). CSI loads from its own sheets; Vadim's sheets are being requested separately (TASK-0018). The remaining need is the system as source of truth.
2. **Loaded but restricted** to the smaller admin set that neither Ethan nor Vadim is in. Then the ask is simply for them to be included in the export.

**Smallest version.** Answer yes or no for IAG (5,565 lanes, 86% of the 6,441 lanes with no contracted row at all and the largest single block); if yes, include IAG in the contracted export. Then Emirates.

Also in this export, **two format defects** (found while verifying this spec): `effective_as_of` is blank on 153 of 157 data rows, and on the other four holds a raw HTTP date string (`Tue, 20 Oct 2026 00:00:00 GMT`) instead of an ISO date; and all 157 rows are typed `Casket`, so **cost for cremated-remains shipments appears nowhere**. Tell us whether it is held at all. (Reports cite 156 contracted lanes; the file has 157 data rows. The difference is not traced.)

---

## 9. D6 — Booking duration: six questions, then fields if they exist

CSI is starting to be able to track how long a booking takes, and nobody is sure the system captures it (Ethan, 2026-11-02). This is a question about the system, so it is yours (`§9.6`); how long work takes and what an hour costs are asked of Vadim, Kim, Susej and Donald separately and are never combined here.

| # | Question | Why it matters |
|---|---|---|
| Q1 | When a booking is started, even as a draft, is a creation timestamp stored? (The specification says a dashboard entry is created when booking starts.) | The start of any duration measure |
| Q2 | When a request arrives by email and the agent drags the .eml into the OMS, is the email's received time kept on the booking? Is a portal submission time kept? | The start event of the desk's turnaround KR (M-21). Without it, the KR cannot be evidenced |
| Q3 | Is a timestamp stored when the booking request is submitted to the airline? | The end event of that KR |
| Q4 | Does the OMS keep a status history (each change with its time), or only the current status? | Duration by stage without any new field |
| Q5 | Is the airline's confirmation or rejection time stored? | Airline turnaround; rework |
| Q6 | Are edits after submission logged with time and kind? | Rework and the rebooking cost chain (M-22) |

**Answer format:** for each, *exists / exists but unreliable / not stored*; if stored, the table and column, and since when it is reliable. **If not stored**, the smallest version is two stamped fields (`request_received_at`, `submitted_to_airline_at`) written as a side effect of actions agents already take. **Nobody is asked to type anything**: a plan that assumes the desk absorbs new manual work fails silently (`§11`).

**Constraint (`§7.7`).** Duration is process instrumentation, reported by booking type. No agent identifier appears in any export, and nothing here is for assessing a person.

**Unblocks.** operations (TASK-0008), finance and pricing (cost to serve, once Donald supplies the cost of an hour), corpdev (the unmeasured term in the valuation), data-analyst (M-10, M-21), and the Bookings Directors' own KR2.

---

## 10. Rate-table defects — what "fixed" looks like

Evidence: `scripts/rate_defects.py` → `data/derived/rate-defect-keys.csv` (181 rows, one per duplicated key, with every price seen). Re-runnable on any later export, which is the acceptance test. Unit tests: `tests/test_rate_defects.py`.

| Defect | Measured on `rates-published-20261102.csv` | Fixed when |
|---|---|---|
| **EA-45-05** `shipment_rate_type` blank | 6,919 of 6,919 published rows (the contracted export fills it: all `Casket`) | Populated on every published row, or a written reason it cannot be |
| **EA-45-09** the documented uniqueness key is violated, and free text sits in numeric columns | 181 keys appear more than once (487 rows). 43 are exact repeats; 133 carry different prices; 5 carry text. Separately, `published_rate` is text on 5 rows ("varies per city") and `discount_rate` is text on 5 ("take $35 off pub" x4, "equal to pub"), all American | Re-running the script on the next export reports zero duplicate keys, or any remainder is explained by a documented key that includes `shipment_rate_type`; numeric columns are numeric |
| **EA-45-10** conflicting prices on one key | 133 keys. **All 133 are `flat` rates. 120 differ by more than 2x** (median 2.8x, maximum 4.3x). By airline: Southwest 49, American 43, Aeromexico 24, Delta 17. Example: American, zone West to zone West, flat: $207.19, $615.94, $207.19 | CSI has marked which row is correct (CSI decides; engineers do not guess a price), the others are retired, and the script reports zero conflicts |

**These three may share one root cause, and CSI cannot tell.** If casket and cremated-remains prices were stored as separate rows that differ only by `shipment_rate_type`, then the "duplicates" are legitimate rows the export has flattened, the documented key is wrong, and the fix is one. The blank field is exactly what would show that. This is a hypothesis `[HYPOTHESIS]`, not a finding; the answer is one query for whoever can see the table.

**Why severity matters here.** The rates are what funeral homes pay and what the desk and the quote tools read. A 2x to 4x spread on one lane is not rounding. CSI does not know whether the quote tool or portal reads these rows; that is question 2 in EA-45-10.

---

## 11. How we will know it worked (`§9.2`: the measure exists before the build)

| Measure | Baseline | Target | Read by |
|---|---|---|---|
| Time from sending the ask to a classification on each item | n/a | Every item classified within one week | The Part 4 tracker; legal-risk records it |
| Time from classification to first D0 file | n/a | Reported, not targeted | The tracker |
| The six blocked metric families computed from the first file (M-12 to M-17; lane volume; corridor mix; account value; margin by lane) | 0 of 6 computable | Computed within 5 working days of the first file | data-analyst |
| Tie-out table exists and every month outside tolerance has a cause | None | Yes | data-analyst |
| Decision latency on a booking-level question | Unanswerable | Same day | data-analyst |
| `shipping_funeral_home_id` null count by month | 59 in 2026 YTD at Sep 6; 0 in the Nov 1-13 window | Trend visible; recurrence of nulls is a defect | data-analyst (M-23) |
| Hours the items consumed, by classification | Unknown | Recorded per item | legal-risk (tracks outcomes; does not screen) |

---

## 12. Manual fallback — if the answer is no, or no price is agreed

A ladder. Each rung is partial, and the document says what it does not give.

**Inside the ask.** (1) D0 only, once. (2) D1 Tier 1, once, then again quarterly on request. (3) D1 nightly with Tier 2. Declining a rung leaves the smaller rungs standing.

**If all of that is declined**, with CSI's own hands and no agent touching the OMS:

| Fallback | Source and owner | Gives | Does **not** give |
|---|---|---|---|
| **F1. Account revenue by month** | Donald: QuickBooks sales-by-customer **summary**, by month, January 2024 to date. Customer totals only, no line detail or memo fields, so no decedent text | Account value, churn and frequency at monthly grain, joined to HubSpot by name. `[ASSUMPTION — QuickBooks customers map to funeral homes; Donald confirms]`. Invoices are the source of truth in CSI's own contract analysis | Lane, corridor, carrier, status, cancellation, cohorts by origin |
| **F2. Lane volume by carrier** | Carrier invoice files CSI already receives (United and Delta analysed; one further file not yet read), placed in `data/raw/carrier-invoices/` weekly. `scripts/realized_margin.py` strips the name columns at load | Lane volume and realized cost for those carriers, by AWB | Account; carriers that do not send files; cancelled bookings |
| **F3. Filtered analytics exports** | Vadim or Susej: does the Analytics Export accept filters (funeral home, airline, destination)? If yes, a rotating series of filtered aggregate pulls | Some account and lane counts, with no PII | Everything per booking; unknown whether filters exist |

**Rejected, on purpose:** a two-week hand-kept sample by the desk. It adds manual work to a 24/7 desk (`§11`), which this program does not do.

**What the fallback means for the program.** It answers "is account revenue concentrating or leaking" and gives a rough lane weighting. It cannot answer whether growth in bookings is acquisition, retention or frequency, which is the question `CLAUDE.md §2` leaves open, or whether any lane loses money after cost to serve. For those, the export is the only route (`HANDOFF-T0016`).

---

## 13. Assumptions, open questions, and what would change this

- **`[ASSUMPTION]` Acceptance status.** Support Services start at the Initial Deliverables Acceptance Date (`reports/freightflow-agreement-review.md §1.1`). The OMS deliverables were formally rejected in May 2026 and the current status is unknown (`context/brain/open-questions.md` #30). Every contract-bucket read in the ask assumes acceptance has happened; if it has not, the same items may sit inside the fixed-fee build.
- **`[ASSUMPTION]` The `Period` is a flight date.** Strongly evidenced (Section 1, M-02) and tested by Acceptance C, not asked of engineering. The question of what `Period` means and which statuses the analytics export includes goes to Vadim, Kim and Susej first (`§9.6`, M-02).
- **`[ASSUMPTION]` QuickBooks customers map to funeral homes** (F1).
- **`[ASSUMPTION]` 0.5% tie-out tolerance** (Acceptance C).
- **`[HYPOTHESIS]` The three rate defects share a root cause** (Section 10).
- **Unverified:** whether the Funeral Home Records bulk CSV works; whether the Airline Invoice Audit and Skipped Validation Bookings pages export; whether the OMS stores quotes; who holds the contracted rate permission beyond Kyri and Alex.
- **What would raise confidence on field availability:** the engineer's E/D/N column and a data dictionary (status values, `shipment_rate_type` values, definition of `revenue_total`, definition of `landed_date`, time zone). About an hour of someone's time who knows the schema.
- **What would change the ranking:** Vadim's answer on how the desk picks a route (reorders EA-45-10 only); data-analyst's quote-log specification (TASK-0002, due Friday) which refines EA-45-08 next week.
- **This spec is not a Change Order or a request to begin chargeable work.** Classification is Kyri and Alex's; CSI states its read in the ask.
