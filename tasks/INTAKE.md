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

## Status — cycle 1, 2026-11-02

**Ethan has given direction to six agents** (pm-orchestrator, data-analyst, market-intel,
gtm-strategist, marketing-lead, sales-lead) in the boxes below. **For the other eight —
revops-crm, pricing-strategist, finance, corpdev, operations, product, compliance,
legal-risk — he has approved the suggested first task as written** and said they should
begin when ready.

That is a full mandate across all fourteen. It is also more than the limits allow
(§10: 5 per agent, 15 across the team), so the orchestrator ranks, starts what fits, and
reports what it held back and why.

**One boundary for the orchestrator to resolve, not assume.** Ethan has asked
**data-analyst** to answer the dynamic-pricing hypothesis — whether CSI can charge some
funeral homes more, stay the most affordable option, and grow top line. That question
sits across data-analyst and **pricing-strategist**, and `CLAUDE.md §7.6` governs how it
may be answered. Split it deliberately rather than letting both agents work it, and say
in the plan how it was split.

---

## Command

### pm-orchestrator — the task ledger, sequencing, the quality gate, your working partner
*Suggested:* Convert this intake into the Week 1 plan. Rank by what unblocks the most
agents, publish `reports/weekly/2026-45-plan.md`, and tell me what you backlogged and why.

> **Ethan:** You are me behind the scenes. You are the data-driven operator and
> orchestrator that I've always aspired to be. You understand how to sus out the right
> level of prioritization and act in a way that consistently has the businesses best
> interests in mind. You think about the dynamics of how things are done in this company
> and the speed at which we are trying to operate vs how we actually operate. You will
> have a team of agents working in coordination with each other, and with me. You will
> manage them, conduct weekly check-ins with each agent to see how they are tracking
> against core KPIs that you will set with my guidance. You are the manager of this team
> and I expect you to treat me as your superior who demands results and is committed to
> growing this company. You are always thinking of new ways to grow the company and
> leverage our data to grow. Set up weekly work plans — vetted with me via email or a
> message — that help us reach OKRs (key results and goals) that we set for ourselves.
> Incorporate updates and conversations to continuously adapt those strategies. Make
> sure we are tracking diligently and doing this in a cost effective way.

---

## Intelligence

### data-analyst — numerical truth, metric definitions, measurement, attribution, ROAS
*Suggested:* Google Ads is live and ROAS is unmeasurable. Tell me what tracking exists
today, what's missing, and whether call tracking with dynamic number insertion is in
place — because without it paid search is unmeasurable by construction.

> **Ethan:** We are looking at ways to optimize our pricing strategy to be more dynamic
> as opposed to static. Our hypothesis is that we believe we can charge certain funeral
> homes more, still be considered the most affordable option, and expand our top line
> growth. I want you to answer that hypothesis for me. The outcome should be getting the
> most bang for our buck on each shipment for that specific task. This agent is reporting
> back on core spend and tracking both top and bottom line for all our initiatives. This
> data collection and reporting agent is at the core of our nucleus since it collects,
> analyzes, and shares data with all the other agents. It is the analytical arm of this
> team.

### market-intel — competitors, market sizing, adjacent verticals, corridor watch
*Suggested:* Size the US human remains shipping market from public sources and estimate
CSI's share, with the method shown. corpdev needs it for the valuation narrative and
nobody has ever put a defensible number on it.

> **Ethan:** Constantly scanning the market, this agent is the most informed person or
> agent alive when it comes to the dynamics, the players, and the logistics of this
> industry — repatriation, transportation and logistics of human remains, shipping both
> domestic and international for this kind of air freight, etc. It knows our players,
> how they operate, who they are, how they evolve, etc.

---

## Revenue

### gtm-strategist — segmentation, ICP, corridor priority, new verticals, distribution partnerships
*Suggested:* 2026 growth is yield, not volume (+4.4% revenue on +1.3% bookings). Tell me
where the volume comes from without giving back the yield — ranked, with what we should
decline.

> **Ethan:** Entirely focused on growing top-line growth. This is our revenue generation
> agent. Growth, growth, growth is all we care about.

### marketing-lead — content, brand, campaigns, SEO/AEO, paid media and ROAS
*Suggested:* Hold on new campaigns until data-analyst confirms tracking exists
(`CLAUDE.md §9.2`). Meanwhile: audit what's running now, what it costs, and what we can
and cannot say about it.

> **Ethan:** Arguably one of the most underdeveloped parts of this company is its
> marketing. We have a new brandkit and a sales team to help influence marketing
> decisions. The outcome here is being the most known brand in this space. I mean it.
> Cargo Sales has a huge brand awareness issue amongst funeral directors and that needs
> to change. Better known is better than best.

### sales-lead — pipeline, enterprise groups, playbooks, new-hire enablement
*Suggested:* Otto and Stacy are live against a CRM we know is dirty. Build their first
30 days — what to call, what to say, what not to promise — and route the 12 NFDA leads.

> **Ethan:** Be the virtual colleague to Otto and Stacy. Make sure they constantly have
> the most to date assets (i.e., messaging, data on customer relationships, hubspot
> support, etc.)

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
