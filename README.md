# CSI Growth Agent Team — Setup

An orchestrated Claude Code agent team for Cargo Sales International: a PM/orchestrator
coordinating four specialists (data, GTM, marketing, sales) against a single metric —
**net new landed bookings per month, and the cost to acquire them.**

---

## Install

Drop this folder into a new directory and open Claude Code in it. Claude Code reads
subagents from `.claude/agents/*.md` at the project level, and reads `CLAUDE.md`
automatically as project context.

```
csi-agent-team/
├── CLAUDE.md                       ← shared context, loaded into every session
├── .claude/agents/
│   ├── pm-orchestrator.md
│   ├── data-analyst.md
│   ├── gtm-strategist.md
│   ├── marketing.md                ← agent name: marketing-lead
│   └── sales.md                    ← agent name: sales-lead
├── templates/                      ← task, handoff, weekly report schemas
├── tasks/{active,done,backlog}/    ← the task ledger; PM owns it
├── handoffs/                       ← cross-agent requests, PM routes
├── reports/
│   ├── weekly/
│   └── pending-approval/           ← anything awaiting your sign-off
├── data/{raw,derived}/             ← raw is read-only, always
└── context/                        ← metric definitions, research, source docs
```

Run `/agents` in Claude Code to confirm all five are registered. If one doesn't appear,
check the frontmatter — a name collision or a malformed `tools` line makes a file fail
silently.

---

## Before the first cycle

Two things determine whether this works:

**1. Load the context folder.** The agents are only as good as what's in `context/`.
Drop in: the H1 analytics export, the 878-account HubSpot workbook, the pricing
calculator, the sales playbook, the mid-year report, the OMS/portal spec, and the
Exhibit A deliverables list. Anonymize anything with decedent or family data first —
`CLAUDE.md §7.2` makes this a hard rule and the agents will refuse to work around it.

**2. Decide what the agents can actually touch.** Right now every agent is read/write on
the repo and read-only on the world. Nothing publishes, sends, spends, or writes to
HubSpot without you. If you later connect the HubSpot MCP server, restrict it to
read-only for the agents and keep writes behind your approval — the guardrails in
`CLAUDE.md §7.1` assume that.

---

## Kicking it off

```
Use the pm-orchestrator subagent. Read CLAUDE.md and everything in context/.
Then produce the Week 1 plan: the task set per agent (max 5 each), the dependency
chain, and the one thing that must be true by Friday. Do not create tasks that
depend on numbers we haven't verified yet.
```

The PM will front-load the data-analyst — reconciliation, metric definitions, the
volume-decline decomposition — while the other three do discovery and drafting that
doesn't depend on unverified numbers. That sequencing is deliberate and the PM is
instructed to defend it if you push to skip ahead.

After that, weekly:

```
Use the pm-orchestrator subagent. Run the Monday cycle: review last week's reports,
route open handoffs, and set this week's tasks.
```

You can also invoke a specialist directly when you want one thing:

```
Use the gtm-strategist subagent to size the mid-size independent segment (2–20
locations) and recommend whether it's worth a dedicated motion.
```

---

## The design choices worth knowing about

**Max 5 open tasks per agent.** Written as a hard constraint on the PM, not a
suggestion. A specialist with nine tasks does nine mediocre things.

**The PM is the only agent that creates tasks.** Specialists claim and complete. This
is what keeps four capable agents from generating work for each other indefinitely.

**Agents don't call each other directly.** They write handoffs; the PM routes them. It
costs a round trip and buys you a single coherent view of what the team is doing.

**Nothing goes live.** Every agent drafts and stages to `reports/pending-approval/`.
Publishing, sending, spending, and HubSpot writes all require your explicit approval.

**Measurement precedes spend.** The PM will block a campaign launch until the analyst
confirms tracking exists. That rule is there specifically because the $20K-with-no-
attribution year already happened once.

**The campaign collaboration pattern you described is wired in explicitly:** marketing
proposes → GTM sets audience/offer/threshold → data specifies and confirms tracking →
marketing builds → you approve → data reports weekly → GTM decides scale/iterate/kill.
The PM is told to create this as a linked task chain rather than four independent tasks.

**Two guardrails I added that you didn't ask for, and would recommend keeping.** First:
decedent and family PII never leaves the repo, and never goes into a third-party AI tool.
Your marketing agent is going to want to paste real data into external content tools, and
in this industry that's the one mistake that isn't recoverable. Second: a tone contract
in `CLAUDE.md §7.4` — loved ones, never "cargo"; no urgency manipulation; no humor. AI
content engines drift toward growth-marketing voice by default, and that voice would cost
you accounts here.

---

## Where this will need your judgment

The prompts encode a specific diagnosis: **the plateau is a distribution problem, not a
product problem.** That's well-supported by the H1 data — declining volume with rising
yield, an 80% price-win rate, and no measurable acquisition engine. But the data-analyst
is explicitly instructed to test it rather than assume it, and to say so loudly if the
decomposition shows this is actually a **retention** problem. If that comes back, most of
the GTM and marketing plan should be rebuilt around it. Watch for that finding in the
first two weeks; it's the one result that would redirect the whole program.
