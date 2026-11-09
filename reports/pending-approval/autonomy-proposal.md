# Making this agentic — the bottleneck isn't the guardrails

**DRAFT for Ethan, 2026-11-09.** A proposed change to how agents and the orchestrator operate. Nothing is adopted until he approves.

---

## The diagnosis, and it surprised me

I expected to find that `§7.1` was too strict. **It isn't.** Go through what it gates:

publishing · sending email to a real person · HubSpot actions that put a message in front of someone · changing who can see a file · spending money · naming enterprise accounts externally · pricing claims · changing live rates · contacting an investor or target · deleting data

**Not one of those is what stopped work this week.** Every one is a thing that reaches a customer, a partner, or CSI's money, and every one should still need you.

What actually stopped work was three different things.

### 1. Agents asked instead of defaulting

`revops-crm` stopped and asked you to confirm four partner IDs — **Bergen NJ 2734, Bergen FL 1764, NMS 2239, IMS 2767** — matched from names that read `Bergen Funeral Service (New Jersey)`, `National Mortuary Shipping`, `International Mortuary Shipping, LLC`. There was no ambiguity. It should have proceeded, flagged the assumption, and let you reverse it.

It did that because the task file told it to, and I wrote the task file. **That's my error, not a guardrail problem.**

### 2. I queued decisions instead of making reversible ones

14 items in `pending-approval`, 11 brain proposals. Most are reversible in minutes. I treated "Ethan should know" as "Ethan must decide first," which are different things.

### 3. One genuine hard blocker

**The HubSpot connector has no property-creation tool.** I checked: `discover_hubspot_schema` is read-only, `manage_crm_objects` writes records not schema. That one really is yours, and no policy change fixes it.

**So: one of three blockers was real. The other two were mine.**

---

## Proposed change 1 — default and proceed

**Add to `CLAUDE.md §7.1`:**

> **When an agent hits a question that is not on the approval list above, it does not stop.**
> It takes the most defensible option, records the choice and its reasoning in the task log,
> flags it in the handback, and continues.
>
> **The test is reversibility, not importance.** If being wrong costs an hour to undo, decide
> and flag it. If being wrong is expensive or hard to reverse — a merge, a deletion, anything
> `§7.1` already gates — stop as before.
>
> **"I assumed X, here is why, reverse it if wrong" is a complete and acceptable outcome.**
> Stopping to ask a question with an obvious answer is not.

Under this rule, `revops-crm` would have built 2,305 company records last Tuesday.

---

## Proposed change 2 — standing authorities

Decisions you have effectively already made, written down so nobody asks again. **Each one is yours to confirm or strike:**

| # | Standing authority | Why it's safe |
|---|---|---|
| 1 | **Partner tier** is Bergen NJ/FL, NMS, IMS, Las Rosas, and the 17 `is_discount_eligible` accounts | §5 already names them; the IDs match unambiguously |
| 2 | **Lifecycle** is set from booking history — customer if ever booked, lead if not | Mechanical, re-runnable |
| 3 | **Agents may create and populate HubSpot properties** when you have created them | Already free under §7.1; the limit is the connector, not policy |
| 4 | **Segments exclude** freemail, chat-origin, non-funeral-home domains, and receiving homes | Already established, repeatedly |
| 5 | **Territory**: Otto Midwest, Stacy West, Northeast/South split per the hitlist | Your own instruction, 2026-11-03 |
| 6 | **Brain proposals merge automatically** when evidenced by a file in `reports/` and not contradicting §5 or §7 | They are internal notes, reversible by editing |
| 7 | **Internal colleague questions** (Vadim, Kim, Susej, Maya, Donald) go in the weekly batch without pre-approval | They are colleagues, not customers. §7.1 gates customers |

**Number 7 is the one I'd most like.** Right now every internal question waits for you to send it, which makes you a relay.

---

## Proposed change 3 — one decision document a week

Instead of a growing queue, **one document every Monday**: what needs you, ranked, with a recommendation and a default for each. If you don't answer, **the default happens Friday** and I tell you what it did.

That inverts the current model. Today, silence blocks. Under this, silence means "use your judgement," and you keep a veto.

---

## Proposed change 4 — the orchestrator stops waiting

**Agents sat idle for five days because I was waiting for you.** That was the wrong instinct. If an agent is blocked, there is almost always unblocked work in its lane.

**New rule for me:** no agent stays idle on a blocker for more than one working day. If a blocker holds, I re-task it onto something in the backlog and say so.

---

## What stays exactly as it is

- Everything in the `§7.1` approval list. **No change proposed to any of it.**
- `§7.2` data handling — the strictest rule, untouched.
- `§7.5` corpdev liability, `§7.6` pricing, `§7.7` personnel — untouched.
- Merges and deletions above 25 records still stop.
- **One agent writes to HubSpot.**

**The proposal loosens nothing that touches a customer, a partner, the public, or CSI's money.** It changes what happens when an agent meets an ordinary question.

---

## What I'd expect to change

| | Today | Under this |
|---|---|---|
| Company records built | 10 | 2,305 |
| Brain proposals pending | 11 | ~2 that genuinely need you |
| Items in `pending-approval` | 14 | the ones that reach a person |
| Decisions you make per week | ~25, unranked | ~5, ranked, with defaults |
| Agent idle time on a blocker | 5 days | 1 day |

---

## The honest risk

**Agents will sometimes be wrong, and you will find out after the fact rather than before.**

That is the trade. The mitigation is that every assumption is logged, flagged in the handback, and reversible — and that the irreversible category is exactly what `§7.1` already protects.

My view: **this week cost more than a handful of wrong assumptions would have.** Four agents produced real findings and then nothing happened for five days. But it is your call, and if you'd rather keep a tighter leash on a specific area, say which and I'll carve it out.
