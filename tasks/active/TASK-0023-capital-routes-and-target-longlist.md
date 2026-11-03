# TASK-0023 — Capital routes and an acquisition target longlist

**Owner:** corpdev
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-12
**Priority:** CRITICAL
**Status:** DONE — delivered 2026-11-03. Both reports in `reports/`. Nothing staged for sending; no contact made with anyone.

## Objective

Ethan, 2026-11-03: raising capital and identifying acquisition targets is **"one of the core
priorities for us right now."** Capital has been Priority 1 since this team was formed and
nothing has been produced against it.

Deliver two things: **the realistic routes to capital for a business like CSI**, and **a
researched longlist of acquisition candidates.** Both research-only. Ethan makes every
approach, without exception.

## Line to the metric

Compounding scoreboard — enterprise value. Inorganic volume is one of the four fronts in
`§0`, and the only one with nothing against it yet.

## ⚠️ Read `CLAUDE.md §7.5` in full before starting. It is not boilerplate.

**These are absolute and no reasoning gets around one:**

- **No contact with any target, investor, lender, banker or broker.** Not an email, not a
  LinkedIn connection, not a "quick question" to a website form. Agents build lists and
  model. Ethan makes every approach.
- **No securities language.** No offering documents, no PPM, no subscription materials, no
  investor solicitation. Internal models are fine; an instrument offered to an investor is
  not. Anything investor-facing is marked **DRAFT — NOT FOR DISTRIBUTION — REQUIRES COUNSEL
  REVIEW**.
- **Antitrust.** Targets are competitors. **Never draft or suggest any communication to a
  competitor about pricing, customer allocation, market division or bidding.** Where
  analysis needs competitor pricing, use public sources only and say so. **Pre-close a
  target is a competitor, not a colleague** — no operational coordination, no joint
  planning, no "once we own them" integration assumptions.
- **No binding language.** Nothing that reads as an offer, LOI, term sheet, commitment or
  agreement to agree.
- **Target names and deal terms never leave the repo** (`§7.1`).
- **National Mortuary Shipping and Bergen are allies, not targets.** They are among CSI's
  largest partners *and* customers, Ethan has named deepening those relationships a top
  priority, and any acquisition or equity framing involving either is **his conversation
  alone** (`§5`).

## Deliverable

### Part 1 — `reports/capital-routes.md`

The realistic financing routes for a 23-year-old, ~$15M revenue, family-held logistics
broker. Cover at minimum: SBA and conventional bank debt, asset-based and receivables
financing, search funds and independent sponsors, lower-middle-market private equity,
family offices, seller financing in an acquisition structure, and angel or high-net-worth
individuals.

For each: **what it typically funds, what it costs, what it demands of the balance sheet and
the owners, what control it takes, and what CSI would need to have ready.** Say which ones
CSI could realistically access *today* versus after twelve months of preparation.

**Lead with what would disqualify CSI**, not what's available. That is the more useful half.

### Part 2 — `reports/acquisition-target-longlist.md`

A researched longlist from **public sources only**. Screen on: service overlap, gateway or
corridor footprint that complements CSI's eight, international and consular capability,
apparent scale, ownership and likely succession position, and any public signal of
transition.

**Rank by strategic fit, not by availability.** Flag every one where the alliance rules
above or an antitrust concern applies.

### Part 3 — the readiness gap

**The most valuable thing in this task, and it goes first in whichever report Ethan reads.**

Three facts you must build around rather than discover late:

1. **Customer concentration is severe.** Top 10 accounts are **31.3%** of lifetime bookings,
   top 50 are **56.6%** (`data/raw/oms-funeral-homes-20261103.csv`). Four of the top nine are
   Bergen NJ, Bergen FL, NMS and IMS — about 17% between them. **Frame this correctly:** per
   `§5` these are partner-channel relationships, deliberate and long-standing, not four
   customers who might churn next quarter. It is still a diligence finding and any lender
   will price it.
2. **CSI's financials may not be ready to be read by an outsider.** Nobody has confirmed
   whether the books are cash or accrual, what level of assurance exists (compiled,
   reviewed, audited), or how carrier cost is booked. Those questions went to Arty, CSI's
   accountant, on 2026-11-03 (`reports/pending-approval/emails-2026-11-02/03-arty.md`).
   **A valuation built on unreconciled or cash-basis numbers is worse than no valuation**
   (`§7.3`), so flag this as gating rather than modelling around it.
3. **Key-person and platform risk is real and uncovered.** The OMS is built and maintained
   by a contractor under an agreement with no key-person clause, and **a sale of CSI
   auto-terminates that agreement** (`reports/freightflow-agreement-review.md §14.3`). That
   belongs in the readiness gap and in the risk register. **Kyri is not CSI's CTO and must
   never be described as one in anything an outsider reads.**

## Success criteria

- [ ] Every target sourced from a named public source, cited (`§7.3`)
- [ ] No contact attempted with anyone, and the deliverables contain nothing that could be sent
- [ ] Alliance and antitrust flags applied per-target
- [ ] Readiness gap leads with what would fail diligence, not what CSI is worth
- [ ] No projections, no valuation figure in these two reports — **that is TASK-0006 and it is gated on Arty's answers**

## Dependencies

- Blocked by: none for research.
- **Gates TASK-0006 (valuation):** do not produce a valuation range until the basis of
  accounting and assurance level are known.
- Inputs: `reports/freightflow-agreement-review.md`, `data/raw/oms-funeral-homes-20261103.csv`, `context/fy26-growth-plan-memo.md`

## Approval gate

**Everything in this task is approval-gated for any use outside the repo** (`§7.1`, `§7.5`).
Both reports stay in `reports/`. Nothing is staged for sending, because nothing here is
ever sent.

## Log
- 2026-11-03 — Created. Ethan named capital and acquisitions a core priority and asked for this agent to be among the first started.
- 2026-11-03 — Claimed by corpdev. Read `CLAUDE.md` §7.5 in full before starting, plus
  `§5` (alliances), `context/brain/00-INDEX.md`, `company-facts.md`,
  `accounts-and-pipeline.md`, `data-owners.md`, `initiatives/acquisitions.md`,
  `initiatives/international-partners.md`, `initiatives/federal-contracting.md`,
  `reports/freightflow-agreement-review.md` and the drafted Arty note.
- 2026-11-03 — **Part 3 (readiness gap) built first, not last**, and it leads both reports.
  It is the most valuable output of the task. Concentration figures independently
  re-derived and confirmed: top 10 = **31.32%**, top 50 = **56.58%**; the four
  partner-channel accounts (Bergen NJ 6.93%, IMS 5.20%, Bergen FL 3.20%, NMS 1.39%) =
  **16.72%**, four of the top nine. Framed per `§5` as deliberate alliance structure, not
  churn risk — and still flagged as a finding a lender will price.
- 2026-11-03 — Made it a script rather than an analysis (`§9.3`): `scripts/account_concentration.py`
  (v1.0.0, 18 pytest known-answer tests passing), outputs
  `data/derived/account-concentration.csv` and `-top.csv` with `.meta.json` each.
  Identifier columns dropped **at load** per `§7.2`, dropped list recorded in the meta.
  `ruff` and `black` are not installed in this environment, so formatting was not verified
  by tool — flagged for the orchestrator.
- 2026-11-03 — **Part 1 delivered:** `reports/capital-routes.md`. Eleven routes, ranked for
  CSI as it is, **leading with what would disqualify CSI** rather than what is available.
  Six disqualifiers; two are gating (basis of accounting/assurance level, and FreightFlow
  §14.3 auto-termination on a Sale of CSI with the "bona fide financing" carve-out unread
  by counsel). Includes a three-tier diligence-readiness checklist with owners.
- 2026-11-03 — **Part 2 delivered:** `reports/acquisition-target-longlist.md`. Public
  sources only, every target cited inline, ranked by strategic fit with alliance and
  antitrust flags applied per target. Allies excluded by name: Bergen NJ/FL, NMS, IMS, and
  Rowland Brothers (a Bergen partner) — any acquisition or equity framing involving them is
  Ethan's alone per `§5`.
- 2026-11-03 — **No valuation figure, multiple or projection appears in either report.**
  TASK-0006 remains gated on Arty's four answers, as this task requires.
- 2026-11-03 — **No contact attempted with any target, investor, lender, banker or broker.**
  Research was public search, trade press and directory listings. Three competitor domains
  (`internationalremainsshipping.com`, `mortuary-shipping.com`, `ewacares.com`) failed to
  resolve and would need allowing in the session's network settings; the limitation is
  stated in the report rather than worked around.

## Outcome

**Delivered.** `reports/capital-routes.md`, `reports/acquisition-target-longlist.md`,
`scripts/account_concentration.py` + tests + derived outputs.

**The four things the orchestrator should carry to Ethan, in order:**

1. **Two gating items block every capital route, and both are one email or one call.**
   (a) Send the Arty note — basis of accounting, assurance level, how carrier cost is
   booked, entity structure. (b) Engage counsel on FreightFlow §14.3: whether a financing
   or recapitalization is a "Sale of CSI," and a cleared form of words for describing the
   platform and the vendor relationship. **CSI currently cannot accurately describe its own
   technology to an outsider**, which blocks all eleven routes.
2. **A free piece of capital-strategy work this week:** the SBA size determination already
   pending from Palermo Landsman & Ross (for federal contracting) answers the SBA-lending
   eligibility question at the same time. Add the lending question to it. CSI's ~$15.0M
   revenue against the $12.5M standard noted for NAICS 812210, plus the co-located
   affiliate, makes this live. Also: **CSI's TSA and IATA certifications sit in Southern
   Cross Trading, not in CSI** — a structural finding for both valuation and risk.
3. **The question only Ethan can answer, and it collapses the report:** how much control is
   the family willing to give up, and is a sale on the table at any horizon? The brain holds
   nothing on ownership by design. The readiness work is identical whichever answer he
   gives, so none of it waits — but the question should be answered before any outside
   conversation opens.
4. **Market-structure finding worth a brain proposal:** public sources indicate **Eagle's
   Wings Air and Inman Shipping Worldwide are one ownership group** (David McComb, Fort
   Wayne IN). If it verifies, two of the three competitors named in `CLAUDE.md` §3 are one
   company, the largest competitor is not acquirable at CSI's size, and CSI's inorganic path
   runs through small corridor and gateway specialists instead.

**Also flagged:** CSI cannot open a data room as things stand — operational exports carry
decedent and family data by design (`§7.2`), and a strip-and-check step with a named owner
has to exist before any file leaves CSI. Cheap, unglamorous, and the item most likely to be
skipped.

**Handoffs raised, for routing:** `operations` (integration capacity — no target is called
integrable until this returns, and note that migrating an acquired book into the OMS needs
a FreightFlow Change Order the Developer may refuse); `finance` (cash conversion cycle — the
unmeasured float is probably CSI's cheapest capital); `data-analyst` (restate concentration
by revenue and margin; resolve BACKLOG B-01); `market-intel` (B-03 amended); `legal-risk`
(extract the FreightFlow §9.2 22-name competitor list — the cheapest, highest-yield next
step in this workstream); `compliance` (Cuba-corridor exposure); `gtm-strategist`
(assistance/insurance channel as a partnership lane, and a split on MorTrac).
