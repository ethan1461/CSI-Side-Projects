# Task intake — Ethan's direction to the team

**How to use this:** write what you want each agent to do in its box below. Don't worry
about formatting, scoping, or sequencing — write it the way you'd say it to a person.
The orchestrator converts each line into a properly-scoped task in `tasks/active/`, with
an artifact, a success criterion, and a line to the metric stack, and tells you what it
had to drop to stay under the limits.

**Two limits it will enforce** (`CLAUDE.md §10`): max 5 open tasks per agent, max 15
across the whole team. Fourteen agents × five tasks is forty-five workstreams and no
program. If you write more than fits, the orchestrator ranks and backlogs the rest — and
tells you what it backlogged so you can override.

**What makes a good line here:** the outcome you want, not the method. "Tell me what CSI
is worth and what would have to be true to be worth more" is better than "build a DCF
with a 10% WACC." The agents are good at method; they need the question.

Each agent below has a **suggested first task** based on what's blocking or what you've
already flagged. Accept it, edit it, or cross it out and write your own.

---

## Command

### pm-orchestrator — the task ledger, sequencing, the quality gate, your working partner
*Suggested:* Convert this intake into the Week 1 plan. Rank by what unblocks the most
agents, publish `reports/weekly/2026-45-plan.md`, and tell me what you backlogged and why.

> **Ethan:**
>
>

---

## Intelligence

### data-analyst — numerical truth, metric definitions, measurement, attribution, ROAS
*Suggested:* Google Ads is live and ROAS is unmeasurable. Tell me what tracking exists
today, what's missing, and whether call tracking with dynamic number insertion is in
place — because without it paid search is unmeasurable by construction.

> **Ethan:**
>
>

### market-intel — competitors, market sizing, adjacent verticals, corridor watch
*Suggested:* Size the US human remains shipping market from public sources and estimate
CSI's share, with the method shown. corpdev needs it for the valuation narrative and
nobody has ever put a defensible number on it.

> **Ethan:**
>
>

---

## Revenue

### gtm-strategist — segmentation, ICP, corridor priority, new verticals, distribution partnerships
*Suggested:* 2026 growth is yield, not volume (+4.4% revenue on +1.3% bookings). Tell me
where the volume comes from without giving back the yield — ranked, with what we should
decline.

> **Ethan:**
>
>

### marketing-lead — content, brand, campaigns, SEO/AEO, paid media and ROAS
*Suggested:* Hold on new campaigns until data-analyst confirms tracking exists
(`CLAUDE.md §9.2`). Meanwhile: audit what's running now, what it costs, and what we can
and cannot say about it.

> **Ethan:**
>
>

### sales-lead — pipeline, enterprise groups, playbooks, new-hire enablement
*Suggested:* Otto and Stacy are live against a CRM we know is dirty. Build their first
30 days — what to call, what to say, what not to promise — and route the 12 NFDA leads.

> **Ethan:**
>
>

### revops-crm — HubSpot, account resolution, interaction logging, account-level marketing state
*Suggested:* Audit HubSpot and tell me how bad it is in numbers: duplicates, staleness,
orphaned contacts, accounts with no owner. Proposal only — no writes without approval.

> **Ethan:**
>
>

### pricing-strategist — route economics, willingness-to-pay, alternative data, rate architecture
*Suggested:* We now have real carrier invoices. Rank our lanes by actual margin and tell
me where we're underpriced — and where the 133 conflicting-rate routes are costing us.

> **Ethan:**
>
>

---

## Finance and corporate

### finance — P&L, unit economics, budget, cash, revenue leakage
*Suggested:* **Priority.** Every United shipment carries ~$33 above the contracted rate
in misc and tax charges — ~$358K/year at our volume. Establish whether we bill it
through. This is the lead item for the Donald conversation.

> **Ethan:**
>
>

### corpdev — valuation, acquisitions, capital strategy, strategic partnerships
*Suggested:* Value the business. Range it across the margin uncertainty rather than
picking a point, and tell me what would have to be true to be worth more. Capital is
Priority 1.

> **Ethan:**
>
>

---

## Operations and delivery

### operations — cost to serve, capacity, rework, carrier performance, SLA, OMS adoption
*Suggested:* We don't know cost to serve and it may not be instrumented at all. Tell me
whether it exists, and if not, the cheapest way to find out — a two-week time sample
beats a year of estimates.

> **Ethan:**
>
>

### product — OMS and portal requirements, roadmap, exports, adoption
*Suggested:* Write the export specification — exactly what we need out of the OMS, at
what grain, with PII stripped at the query. Prioritized, so Kyri and Alex get one good
ask instead of six partial ones (`CLAUDE.md §9.6`).

> **Ethan:**
>
>

---

## Control functions

### compliance — consular and documentation rules, customs, TSA/IATA, country rulebook
*Suggested:* Start the country rulebook with our priority corridors — Dominican Republic
first, since it's our highest-volume international lane and it's in the routing note.
Cite and date every rule.

> **Ethan:**
>
>

### legal-risk — contracts, risk register, liability, insurance, claims substantiation
*Suggested:* Already running on the FreightFlow agreement. Next: the risk register, led
by shipment-failure liability — what we're exposed to when remains are lost, damaged or
delayed, and what our customer agreements actually say.

> **Ethan:**
>
>

---

## Anything that doesn't fit an agent

Write it here and the orchestrator will route it or tell you nobody owns it — which is
itself useful to know.

> **Ethan:**
>
>

---

## Things the orchestrator should know about this cycle

Context that changes how work gets sequenced — a deadline, a meeting, something you've
already promised someone, something to leave alone this week.

> **Ethan:**
>
>
