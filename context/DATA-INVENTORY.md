# Data inventory

**Last updated:** 2026-09-06
**Source:** Ethan's local `Cargo Sales` folder (one-time export, 345 files).

What the team has, what each file unlocks, and what is still missing. Every agent
should read this before claiming a number is unavailable — and before assuming one
is available.

---

## Access constraints

**The OMS / internal admin system is off-limits to agents.** CSI's security officer
declined programmatic access. All OMS-derived data must arrive as a manual export
placed in `data/raw/` by a human. Treat the OMS as an offline source, not a queryable
one.

Consequence: **no shipment-level data exists in this repo.** See [Missing](#missing)
below — this is the single largest gap and it blocks the reconciliation and
volume-decomposition work described in `CLAUDE.md §9`.

---

## `data/raw/` — gitignored, never committed

Contains personal contact data. `CLAUDE.md §7.2` applies in full: anonymize before
analysis, never send names to a third-party tool, never put a name in a deliverable.

| File | Shape | What it unlocks |
|---|---|---|
| `rates-jan-2026.xls` | 8 carrier tabs: American, Southwest, Delta, United, Copa/IBC, Viva/Volaris, Avianca, plus a discounts & special rates tab. Columns include Origin, Destination, **Published**, **discount** | **Carrier cost.** Contribution margin per lane becomes computable. Validates the EWA ~10% comparison against real published rates |
| `latam-rate-unification.xlsx` | 47 rows × 18 cols: carrier, origin, destination, csi domestic cost, csi intl cost, csi trucking cost, customer price, csi domestic/intl/total profit, historical split, unified intl price | A **worked margin model** for LatAm corridors. The method here generalizes to other corridors |
| `sci-locations-june.xlsx` | 4,439 active SCI locations × 24 cols: name, address, phone, Location Code, Location ID, Location Status, Product Line, Business Line. Plus tabs for location changes, new, closed | The **enterprise account map** for SCI/Dignity. Location-level activation planning, pilot scoping, territory assignment |
| `hitlist-2026.xlsx` | Sheet1: 22 SCI premier locations with contact names, priority, outreach status. California tab: 167 funeral homes with contact, title, email, date contacted, notes | The active target list. Note this is **~189 accounts, not the 878** referenced in `CLAUDE.md §6` |
| `hubspot-contacts-2026-04-19.xlsx` | 3,416 contacts × 10 cols: Record ID, name, email, email domain, IP city/state, phone | Contact-level CRM export. **Contacts, not accounts** — no company, deal, or shipment association |
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

1. **Shipment-level records.** One row per shipment, with booking date, shipping
   funeral home, origin gateway, destination, domestic/international flag, carrier,
   revenue, status. Ideally FY2024–FY2026. Nothing in this repo contains it. Blocks:
   volume-decline decomposition, churn vs. acquisition vs. frequency, active-account
   definition, lane volume, and every margin figure that needs volume as well as rate.
   **Requires a manual OMS export.**
2. **Legacy-system extract** for the OMS reconciliation described in `CLAUDE.md §6`.
3. **Marketing spend by channel by month** for the ~$20K. Blocks CAC by channel.
4. **Quote log** (quotes issued vs. booked). The "wins on price ~80% of the time"
   claim in `CLAUDE.md §2` has no source in this repo. Ethan has confirmed no quote
   log exists, so this figure should be labeled `[UNSOURCED]` wherever it appears and
   never used externally.
5. **The 878-account HubSpot workbook.** What arrived is ~189 accounts plus a
   contact-level export. May be retrievable from HubSpot directly.
6. **Mid-year report.** Referenced by Ethan, not present in the export.
7. **Portal adoption data** — accounts onboarded, bookings through portal vs. phone.
   Untested premise behind the switching-cost moat thesis.
8. **Cost-to-serve / agent time per booking.** Likely does not exist. Confirming that
   it does not is itself a finding.
