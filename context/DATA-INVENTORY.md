# Data inventory

**Last updated:** 2026-11-12 (data-analyst: the shipment-level export and the QuickBooks
customer summary landed 2026-11-10 — Missing item 1 and item 2 both close, item 3 and
item 4 unchanged. See `reports/customer-cohort-analysis.md`)
**Source:** Ethan's local `Cargo Sales` folder (one-time export, 345 files, 2026-09-06), plus the exports placed in `data/raw/` on 2026-11-02.

What the team has, what each file unlocks, and what is still missing. Every agent
should read this before claiming a number is unavailable — and before assuming one
is available.

---

## Access constraints

**The OMS / internal admin system is off-limits to agents.** CSI's security officer
declined programmatic access. All OMS-derived data must arrive as a manual export
placed in `data/raw/` by a human. Treat the OMS as an offline source, not a queryable
one.

**Resolved 2026-11-10 by a route nobody had tried: Rednodo.** Claudio and Lucas at
Rednodo built CSI's legacy system and supplied the shipment-level history directly, in a
day. It did not have to come from the OMS at all. **Before specifying another OMS build,
ask whether Rednodo already holds the data** — it is the cheaper and faster route for
anything historical.

Consequence (now historical): **no shipment-level data existed in this repo until
2026-11-10.** See [Missing](#missing)
below — this is the single largest gap. It blocks churn vs. acquisition vs. frequency,
lane volume, corridor mix, account value, CAC and cohort work. **The route is a build,
not a permission:** Ethan confirmed 2026-11-02 that the Flight Confirmation List, Ready to
Invoice List and Collect Shipments pages have no export function. Specified in
`reports/oms-export-spec.md`; requested in `reports/pending-approval/engineering-ask-2026-45.md`.

---

## `data/raw/` — gitignored, never committed

Contains personal contact data. `CLAUDE.md §7.2` applies in full: anonymize before
analysis, never send names to a third-party tool, never put a name in a deliverable.

### Present in `data/raw/` on 2026-11-02

| File | Shape | What it unlocks, and the caveat |
|---|---|---|
| `analytics-nov-daily-20261102.csv` | Header totals (revenue $150,742.43, 115 bookings, 0 missing revenue, 0 missing funeral home link) and daily `Period, Year, Revenue, Bookings` rows for Nov 2025 and Nov 2026 | Aggregate only. **`Period` is a flight or service date, not a creation date:** 2026 rows run to Nov 13, eleven days past the pull (`context/metric-definitions.md` M-02). The tie-out reference for any booking-level file |
| `shipments-since-2022-20261110.xlsx` | Sheet `Shipments`, **48,715 rows × 4 cols**: `booking_id`, `shipping_funeral_home_id`, `flight_date`, `status`. From **Rednodo (Claudio/Lucas)**, the legacy system's builders — not the OMS | **The dependency four agents were blocked on.** Unblocks M-12–M-14, M-17, cohort and churn analysis, account value, the CAC denominator. **Annual booking counts are identical to the OMS analytics export** for 2023/24/25 and Jan–Aug 2026, so this is the system of record for volume. Caveats: the legacy system was still being adopted through H1 2022 (9 bookings in Jan 2022 vs 896 in Dec), so `history_begins` is **2022-08-01**; 2,183 rows (4.5%) have no funeral home; 1,270 have no flight date; 27 have impossible dates (26 of them the same mis-keyed `2060-02-02`); 162 account IDs are absent from the funeral-home master. **No revenue column**, so revenue-weighted churn (M-15) stays blocked. Carries **no decedent or family data** |
| `sales-by-customer-summary-20261110.xlsx` | QuickBooks "Sales by Customer Summary", **1,428 customer rows × 2016–2026** annual accrued revenue. Header on row 5. From **Donald** | Revenue history back to 2016 — six years earlier than anything else the team has. **Two traps: a row literally named `TOTAL` sits inside the customer list and doubles every annual figure if summed naively, and an `ALREADY PAID` pseudo-customer carries $1.49M.** Exclude both and QuickBooks ties to the OMS analytics export within **1.3%** for 2023–2025, which partly closes the `CLAUDE.md §6` concern. Accrued, not cash. 2026 is partial, to Nov 10. Donald's grouping instruction (Bergen FL+NJ as one; Ortiz Delta, R.G. Ortiz Bronx, Rivera Janet, Rivera Celsa, Ponce as one) is applied in `scripts/analyze_customer_cohorts.py` and logged in `data/derived/revenue-customer-grouping-log.csv` |
| `rates-published-20261102.csv` | 6,919 rows × 12 cols, 19 carriers. **`shipment_rate_type` blank on all rows.** 181 duplicated keys (487 rows); 133 carry conflicting prices, all `flat`; text in 5 `published_rate` and 5 `discount_rate` cells | Supersedes `rates-export-20260906.csv`. Defect list: `data/derived/rate-defect-keys.csv` (`scripts/rate_defects.py`) |
| `rates-contracted-20261102.csv` | 157 data rows × 14 cols, four carriers (American, Delta, Southwest, United), all typed `Casket`; `effective_as_of` blank on 153 | The cost side (M-07). Reports cite 156 lanes; the file has 157 data rows and the difference is not traced. **15 carriers with 6,441 published lanes have no contracted row** |
| `rates-special-20261102.csv` | Customer-specific rates (27 per `reports/carrier-margin-resolved.md`) × 16 cols, including `funeral_home_id` and `funeral_home_group_id` | Partner pricing (National Mortuary Shipping, Bergen) is deliberate, not leakage. Proves the OMS holds a funeral home group hierarchy |
| `carrier-invoices/` | `UA-278010.csv`, `UA-287331.csv` (also as `.xls`), `DL-6890376.xlsx`, `SOA-2026-10-26.xlsx` | Realized margin (M-08) via `scripts/realized_margin.py`. **Decedent names appear in United `Shipper Reference` and Delta `Nature of Goods` and `Shipping Location`; `Customer` is dropped as a precaution.** Strip at load. The `SOA` file has not been analysed |
| `freightflow-agreement.pdf` | 46 pages | The contract. Read in `reports/freightflow-agreement-review.md` |

### Received 2026-09-06 — **not present in this checkout's `data/raw/` on 2026-11-02**

`data/raw/` is gitignored, so absence here does not prove the files are gone from
Ethan's machine; it does mean no agent can re-read them. Derived outputs from the first
file remain in `data/derived/` (`annual-totals.csv`, `monthly-by-year.csv`). The
HubSpot row is a live system, not a file.

| File | Shape | What it unlocks |
|---|---|---|
| `analytics-2022-2026-monthly.csv` | Monthly revenue + bookings, Sep 2022 – Sep 2026. 823 bookings missing funeral home link | **The trend baseline.** Reconciled in `reports/analytics-reconciliation.md` — confirms the plateau, refutes the volume decline, corrects CLAUDE.md's H1 figures |
| `analytics-2026-ytd.csv` | 2026 YTD: $10,408,976 / 7,725 bookings through 2026-09-06 | Current-year tracking. September is partial (274 bookings) |
| `rates-export-20260906.csv` | 6,383 lanes × 8 cols: airline, origin/destination (airport, zone, region, country, state), rate_type, published_rate, discount_rate | Lane-level rate structure. **Only 156 lanes carry both published and discount** — all four US domestic majors; zero international coverage |
| `rates-jan-2026.xls` | 8 carrier tabs: American, Southwest, Delta, United, Copa/IBC, Viva/Volaris, Avianca, plus a discounts & special rates tab. Columns include Origin, Destination, **Published**, **discount** | **Carrier cost.** Contribution margin per lane becomes computable. Validates the EWA ~10% comparison against real published rates |
| `latam-rate-unification.xlsx` | 47 rows × 18 cols: carrier, origin, destination, csi domestic cost, csi intl cost, csi trucking cost, customer price, csi domestic/intl/total profit, historical split, unified intl price | A **worked margin model** for LatAm corridors. The method here generalizes to other corridors |
| `sci-locations-june.xlsx` | 4,439 active SCI locations × 24 cols: name, address, phone, Location Code, Location ID, Location Status, Product Line, Business Line. Plus tabs for location changes, new, closed | The **enterprise account map** for SCI/Dignity. Location-level activation planning, pilot scoping, territory assignment |
| `hitlist-2026.xlsx` | Sheet1: 22 SCI premier locations with contact names, priority, outreach status. California tab: 167 funeral homes with contact, title, email, date contacted, notes | The active target list. Note this is **~189 accounts, not the 878** referenced in `CLAUDE.md §6` |
| `hubspot-contacts-2026-04-19.xlsx` | 3,416 contacts × 10 cols: Record ID, name, email, email domain, IP city/state, phone | Contact-level CRM export. **Contacts, not accounts** — no company, deal, or shipment association |
| **HubSpot live portal (MCP, read at run time)** — baseline `data/derived/hubspot-baseline-2026-11-02.csv`, report `reports/hubspot-defect-baseline.md` | 3,574 contacts, **0 companies**, 1 deal, 1 ticket (2026-11-02). 99.4% unowned, 100% lifecycle "lead", 80.8% no phone, no OMS key property | Supersedes the 3,416-row April export for counts. Added by revops-crm, TASK-0009. Still missing: person-level duplicate pairs (needs a contact export in `data/raw/`) and the OMS funeral-home list for the crosswalk |
| `crm-dump-3.xlsx` | 24 rows: Account, City, Contact_Name, Phone, Email, Status_Hint | Small manual dump |
| `crm-dump-claude-1.xlsx` | 433 rows: name, email, email domain, phone, city, state | Larger manual dump |
| `state-shows-2026.xlsx` | 81 rows: State, Association, Convention Dates, Priority?, City, Registration Link, Notes | Trade show calendar with priority flags. Feeds the show-as-campaign work |
| `pricing-calculator-v3.xlsx`, `pricing-calculator-v1.xlsx` | Single-column layout sheets (v1 has INPUTS_Master, CALCS_Engine, OUTPUT_Quote, OUTPUT_Dashboard, REFERENCE_Data) | The savings-claim engine. Any external savings figure traces here |

## `context/` — committed, loaded into agent sessions

| File | What it is |
|---|---|
| `fy26-growth-plan-memo.md` | **Read this first.** The FY26 plan of record (Jan 2026). Three pillars, KPI framework, quarterly roadmap. Diverges from `CLAUDE.md` in several places — see [Conflicts](#conflicts) |
| `sales-playbook-v2-2026.md` | Sales playbook v2, 28 tables. Input to improve, not a blocker |
| `oms-requirements.md`, `oms-tech-specs.md`, `oms-saas-product.md` | OMS scope, technical specification, and the SaaS product concept |
| `okrs-2026-master.md`, `okrs-2026-ba.md`, `okrs-2026-cro.md`, `okrs-2026-dob.md` | 2026 OKRs, master plus per-role |
| `west-coast-hitlist.md` | Jeff Shafer's West Coast target accounts, 17 tables |
| `illinois-show-contacts.md` | Illinois show contact list |
| `keynote-one-pager.md` | Keynote positioning one-pager |

## Deliberately excluded

Present in the source folder, **not** brought into this repo: employee résumés (12+
named individuals), CA employment files, the Kyri contract negotiation set with
attorney comments, NDAs, and ~240 MB of brand kit and marketing collateral. These are
HR, legal, and personal records with no bearing on the growth program. Do not request
them.

---

## Conflicts

`CLAUDE.md` and `fy26-growth-plan-memo.md` disagree. Neither has been reconciled.
**Flag the conflict rather than picking a side.**

| Topic | `CLAUDE.md` | FY26 memo |
|---|---|---|
| Revenue | H1 2026 = $8,599,462 (annualizes to ~$17.2M) | FY25 ≈ $14.5M, FY24 ≈ $14.2M |
| Growth | Four consecutive years of <3% growth | FY26 target ≥$15.0M — itself only ~3.4% over FY25 |

**Revenue conflict: RESOLVED 2026-09-06.** The system export settles it — FY25 was
$14,417,145, matching the memo. CLAUDE.md's H1 2026 figures are overstated by ~13% and
its "volume declining" claim is seasonality, not trend. See
`reports/analytics-reconciliation.md`. The remaining conflicts below are unresolved.
| Enterprise targets | SCI/Dignity, Everstory (~80 locations), Carriage | SCI/Dignity, Carriage, Foundation Partners, Park Lawn. **Everstory not mentioned** |
| Oct 25–28 Charlotte event | FIAT-IFTA Global Convention | NFDA |
| Team size | 4 named booking agents | 6–8 ops agents, 2–3 sales reps |
| Strategy scope | Pillar A only (share capture) + marketing | Adds **Pillar B** (software platform distribution — Afterword, Funeral365, FuneralOne, OneDirector; plus government/SAM.gov) and **Pillar C** (automation) |
| Mix | not stated | ~50% international / 50% domestic |

The revenue conflict is the important one. H1 2026 annualized is ~19% above FY25,
which would contradict the plateau premise the entire team is built on. Most likely
explanations: different reporting bases (management reporting vs. the H1 analytics
dashboard), seasonality, or a definitional difference in "landed booking." **This is
now the reconciliation the data-analyst should run first**, and it can be run without
OMS access because both figures are already in this repo.

---

## Missing

Ranked by how much each blocks.

1. ~~**Shipment-level records.**~~ **LARGELY CLOSED 2026-11-10.**
   `shipments-since-2022-20261110.xlsx` delivers booking date, shipping funeral home and
   status for all 48,715 bookings since 2022. **Still missing from it, and what each gap
   blocks:** *revenue per booking* (M-15 revenue-weighted churn, realised yield per
   account, account value in dollars); *origin gateway, destination, domestic/international
   flag, carrier, service type* (lane volume, corridor mix, cremation substitution, the
   2026 yield question, every margin figure needing volume as well as rate); *the account
   merge/rename log* (162 shipping IDs absent from the funeral-home master cap confidence
   on the attrition finding at ~15%). **Ask Rednodo first, not the OMS** — they supplied
   the first file in a day. Full specification remains `reports/oms-export-spec.md`.
2. ~~**Legacy-system extract** for the OMS reconciliation described in `CLAUDE.md §6`.~~
   **CLOSED 2026-11-10 for volume and revenue.** The shipment file *is* the legacy
   extract. Bookings tie exactly for 2023–2025 and Jan–Aug 2026; QuickBooks revenue ties
   within 1.3%. The §6 warning should be narrowed rather than repeated wholesale — see
   `reports/customer-cohort-analysis.md` §5. **One live discrepancy remains:** QuickBooks
   annualises 2026 to ~$14.4M (+1.3% on 2025) while the OMS Jan–Aug like-for-like showed
   +4.4%. A ~$0.45M gap in the current year, open with Donald.
3. **Marketing spend by channel by month** for the ~$20K. Blocks CAC by channel.
4. **Quote log** (quotes issued vs. booked). The "wins on price ~80% of the time"
   claim in `CLAUDE.md §2` has no source in this repo. Ethan has confirmed no quote
   log exists, so this figure should be labeled `[UNSOURCED]` wherever it appears and
   never used externally. The OMS specification does describe saved quotes and the
   portal has quote requests; whether they are stored in a queryable form is
   EA-45-08, a question to Kyri and Alex.
5. **The 878-account HubSpot workbook.** What arrived is ~189 accounts plus a
   contact-level export. May be retrievable from HubSpot directly.
6. **Mid-year report.** Referenced by Ethan, not present in the export.
7. **Portal adoption data** — accounts onboarded, bookings through portal vs. phone.
   Untested premise behind the switching-cost moat thesis. Specified as a per-booking
   flag (`created_via_portal`) and portal columns on the funeral home master
   (EA-45-02, -03); event-level logging is PO-45-01.
8. **Cost-to-serve / agent time per booking.** Likely does not exist. Confirming that
   it does not is itself a finding. Whether the OMS captures booking duration is a
   Kyri and Alex question (EA-45-04), not an operations one; how long work takes is
   Vadim, Kim and Susej; what an hour costs is Donald.
9. **Contracted (cost) rates for 15 carriers.** 6,441 published lanes belong to carriers
   with no contracted row: IAG 5,565, Emirates Sky Cargo 552, Aeromexico 88, Air India
   57, Philippines Airlines 57, Lufthansa 53, Amerijet 24, Volaris 10, Avianca 8, Swiss
   Air 8, Korean Air 7, Copa 6, Viva Aerobus 4, IBC Airways 1, El Al 1. Six of these
   (Aeromexico, Air India, Philippines, Swiss Air, Amerijet, El Al) are not named in
   `CLAUDE.md §4.3`. Two routes: Vadim's rate sheets (TASK-0018, a snapshot) and the
   system (EA-45-07).
10. **OMS funeral home master and a join key.** HubSpot has no OMS key and no company
    records, so no CRM account joins to booking history. EA-45-03; try the documented
    bulk CSV first.
11. **Per-shipment carrier cost across carriers.** Today two carriers' hand-delivered
    invoices (about 85 AWBs). The Airline Invoice Audit would cover all (EA-45-06).

---

## Google Drive — live, reachable via connector (added 2026-11-02)

The Google Drive connector is active in this environment. Agents can **read** Drive
directly; nothing is written back without approval (`CLAUDE.md §7.1`). Material found
there since the September snapshot:

| File | What it is | Who should read it |
|---|---|---|
| **`Global_Repatriation_Partners`** | 202 international repatriation counterparts across North America, Mexico, LatAm and beyond. Columns: priority, decision-maker name and title with confidence rating and source URL, ops contact, email, phone, drafted outreach email and LinkedIn note, verification notes, FIAT-IFTA membership. Status column reads "Draft, awaiting Ethan's approval" | **corpdev** (partnership economics, acquisition screening universe), **market-intel** |
| **`Cargo Sales International - NFDA Form (Responses)`** | 12 NFDA show leads, Oct 26–27, already matched against OMS booking history: YTD domestic/international bookings and last booking date per lead. Two SCI/Dignity locations. One existing customer at 10 domestic + 10 international flagged "get them on the portal" | **revops-crm**, **sales-lead** |
| **`CSI Territory Hit Lists — Otto (Midwest) & Stacy (West Coast)`** | Territory assignments for the two new sales hires | **sales-lead**, **revops-crm** |
| **`CSI Sales Training — Sessions 1–5`** | Competitive teardown, positioning & messaging, outreach strategy, customer profiles, territory activation | **sales-lead** |
| **`CSI Outreach Email Sequence (3-Touch)`**, **`CSI Call Framework — Discovery-First Phone Script`**, **`CSI LinkedIn Warmup Playbook`** | Current outreach assets | **sales-lead**, **marketing-lead** |
| **`CSI Industry Report — Death Is Rising (2026)`** | Industry trend piece | **market-intel**, **marketing-lead** |
| **`2026 NFDA Planning`** (Kyri) | NFDA show planning | **gtm-strategist** |
| **`CSI_Baseline_Capture_C1_C2`** | Baseline capture, Sept 2026 | **data-analyst** |
| **`CSI — Sales & Marketing Hub`** (folder) | Container for the above | — |

### ⚠️ Unverified claims already in draft outreach

The `Global_Repatriation_Partners` outreach drafts — currently awaiting approval —
contained two claims that did not match this repo. One is closed, one is open:

- ~~**"eight U.S. gateways (JFK, IAD, MIA, BOS, DFW, IAH, LAX and SFO)"** vs. five
  gateways.~~ **RESOLVED.** Eight is canonical (Ethan, October 2026;
  `context/brain/company-facts.md`). The drafts are correct on this point; any
  5- or 6-gateway mention in older material is the stale one. Gateways differ in
  capability (pickup is MIA, IAH and LAX only), so a flat "eight gateways" claim still
  needs each gateway's own capabilities stated.
- **"about 12,000 loved ones a year"** vs. 10,985 actual bookings in 2025
  (`data/derived/annual-totals.csv`). **Still open.** Held pending the claims register
  (TASK-0012).

**Resolve the open claim before any of these send.** `CLAUDE.md §7.3` and `§7.1`. Owner:
**legal-risk** for claims substantiation, **corpdev** for the partnership program itself.

## Still unreachable

- **The OMS.** No programmatic access; manual exports only. Booking-level records,
  per-shipment carrier cost, funeral home master, and international contract rates all
  remain outstanding. **product** owns the export specification
  (`reports/oms-export-spec.md`) and the standing Monday ask
  (`reports/pending-approval/engineering-ask-2026-45.md`, staged for Ethan).
- **The local `Cargo Sales` folder** on Ethan's computer. Remote Control shows no shared
  folders. To make it reachable: on that computer, open the Claude desktop app →
  Settings → Claude Code → Remote Control, and add the folder to the shared list.
