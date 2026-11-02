# The IAD→POS quote: a second, worse failure mode

**Date:** 2026-11-02 · **Source:** Vadim Shapiro (COO), forwarded to Ethan with a live quote
**Verified against:** `data/raw/rates-published-20261102.csv`, `data/raw/vadim-rate-sheet-20260813.xls`
**Confidence:** **High** on every rate below — all are direct reads from the current published export. **Unknown** on what the booking screen actually displayed to the agent, which is the one fact that decides what the fix is. §4 says how to get it.

---

## The answer

Yesterday's finding was that carrier choice leaks margin at an unchanged customer price. **This is the opposite and it is worse: the customer gets quoted roughly double, and CSI loses the account.**

A quote went out for IAD→POS at **over $3,000**, built as a two-carrier routing via Miami. **The system holds a single-carrier through rate on that lane at $1,545.**

That is not a margin problem. **It is a direct hit on the first thing CSI sells** — `CLAUDE.md §1`, differentiator #1: *"No booking fee. Funeral homes pay the same air rate they'd pay calling the airline direct."* A funeral director who calls the airline and hears half the number has been shown, in one phone call, that the central claim is not true. Vadim's read is right: they are unlikely to call again.

**And the timing is the worst part.** Otto and Stacy are going to market now, pitching exactly that promise.

---

## 1. What the system actually holds for IAD→POS

Every option the published rate table can price on this lane:

| Carrier | Basis | Rate | Note |
|---|---|---|---|
| **American** | US → Caribbean, flat | **$1,545** | **Cheapest single-carrier through rate in the system** |
| **American** | US → Caribbean, flat | $772.50 | The lighter-weight row — exactly 2.0x below, the casket/cremains pattern again |
| **United** | US → Caribbean, flat | **$1,650** | Vadim's figure, to the dollar |
| IBC | MIA → Caribbean, flat | $1,450 | Needs a Miami positioning leg |
| Amerijet | MIA → POS, flat | $2,050 | Needs a Miami positioning leg |
| IAG | IAD → POS, **variable** | $17.25/kg | At a typical casket weight this is **~$3,450** |

**Reconstructing the quote.** American IAD→MIA (Northeast→Southeast zone) is $631.88. Add Amerijet MIA→POS at $2,050 and you get **$2,681.88** before fuel and accessorials — which lands "over $3,000" exactly as described.

| | Amount |
|---|---|
| Quoted | **$3,000+** |
| Best in-system through rate (American) | **$1,545** |
| **Gap** | **~$1,455, or about 2x** |

---

## 2. The finding Vadim did not intend to send

**He quotes American at $1,775. The system says $1,545.**

$1,775 is American's **Central America** rate. Port of Spain prices off the **Caribbean** rate, and the system is right.

This matters, and not as a gotcha — it is the most useful thing in the whole exchange:

> **The person whose job it is to catch these errors is himself working from recall that is $230 off the system, on the lane he chose as his example.**

He is not careless. He is doing from memory what no one should have to do from memory. **And it breaks the "more competent workforce" diagnosis.** If the COO — who built the guidance, who polices it, who has every incentive to get this one right in writing to the CSO — is off by $230 on a single lane, then the problem is not the calibre of the people. **It is that the right number is not in front of anyone at the moment they need it.** Hiring differently does not change that.

---

## 3. "There is absolutely nothing we can do" — respectfully, no

Vadim's words: *"There is absolutely nothing we can do to fix this issue. While we have some of the people working here that work here, this will continue to happen."*

The first half is wrong, and it is worth being direct about because it is the difference between a hiring problem and a one-week build.

**The system already knew the answer.** American at $1,545 and United at $1,650 are both in the published table today. This was not a data gap — nothing had to be researched, loaded or discovered. A quote left the building at roughly twice a number the system was already holding.

**That makes it checkable in software.** A rule at quote time:

> *When a multi-carrier routing is priced, compare it to the cheapest single-carrier through rate on the same origin–destination. If it exceeds it by more than ~25%, show both and require the agent to pick deliberately.*

Not a block. Not an approval queue. Nothing slower at 2am. Just: **you are about to quote $3,000 on a lane where the table holds $1,545 — is that intended?** There are legitimate reasons it might be (no space, embargo, timing, a family's service date), and the agent should always be able to proceed. But it stops being invisible.

**This single rule would have caught this exact quote**, and it does not depend on who is on shift.

What it does *not* fix: judgment, service recovery, consular complexity, and everything else Vadim is carrying. His broader operational concerns are real and this does not answer them. But "nothing can be done" about *this* is not accurate, and accepting it would mean leaving the fix unbuilt.

---

## 4. What we do not know, and it decides the fix

**We know the rate existed in the system. We do not know what the agent was shown.** Those are different problems:

| If… | Then the problem is | And the fix is |
|---|---|---|
| The OMS displayed American at $1,545 and United at $1,650 alongside the multi-carrier option | Information was present and not used | The guardrail in §3, plus Vadim's guidance encoded (EA-45-12) |
| The OMS did **not** surface the through rates — because resolving `US → Caribbean` for `IAD → POS` requires the system to know POS sits in region Caribbean | **The agent had no realistic way to find it** | A rate-resolution defect, and a genuine Error Response Request |

**I cannot tell which from the data, and the difference is the whole argument.** The second case would mean a quote everyone is treating as a people problem is in fact a software problem — and that an agent is being corrected for something the screen never showed them.

**Three questions, in priority order:**

1. **To Kyri and Alex:** when an agent prices IAD→POS, does the system surface American's and United's `US → Caribbean` rates automatically, or must the agent know to look for a region-level rate? *(This is the one that matters most and it is a yes/no.)*
2. **To Vadim:** can he forward the quote screen itself, not just the quote — what the agent saw when choosing?
3. **To Vadim:** the beginning-of-year meeting notes and calls he refers to. He says the same issues were raised then and he stopped resending them. **Those notes are a dataset nobody has asked for** — they would tell us which problems are chronic versus new, and he has clearly been keeping the list.

---

## 5. The line, and it matters more here than anywhere

**Vadim named an individual booking agent in his note. That name appears nowhere in this report, in any dataset, in any task, or in any agent's output, and it will not.**

`CLAUDE.md §7.7` keeps this workforce out of personnel matters, and `reports/carrier-selection-margin-leak.md §5` set the rule a day before this arrived: **measure the decision, never the decider.**

So, for every agent touching this:

- **No analysis is produced that identifies, counts, ranks or compares individual booking agents.** Not as a deliverable, not as an intermediate step, not "just to size it."
- **Agent identity is excluded at the query** on every export, exactly as decedent fields are (`reports/oms-export-spec.md §4.2`).
- **No agent drafts anything supporting or opposing a staffing decision.** Vadim has proposed replacing people. That is Ethan's and Cheryl's call, informed by people who are not us, and nothing in this repo should read as evidence for a personnel file.
- **The quote itself is operational data** and may sit alongside decedent information (`§7.2`). If it is retrieved, it is read for the rate construction and nothing else.

This is not squeamishness. **A single named example is not evidence about a person** — it is one quote, on one lane, with no information about how many others that agent priced correctly, or what the screen showed. Building a case from it would be bad analysis before it was anything else.

---

## 6. What changes because of this

| | Before | Now |
|---|---|---|
| **The problem** | Carrier choice leaks margin at an unchanged customer price | **Two failure modes.** Margin leak (MIA→GUA), *and* over-quoting that costs the customer (IAD→POS). The second attacks differentiator #1 |
| **EA-45-08** (is there a quote log?) | "We can't compute a quote-to-booking rate" | **We cannot see what we are telling customers.** A quote went out at 2x and was caught by one person reading it by chance. This is now a control gap, not an analytics gap |
| **EA-45-10** (does the quote tool read multi-row lanes?) | Theoretical | Live. Vadim confirms quotes go out straight from the system, right or wrong |
| **EA-45-12** (margin rank at carrier selection) | Show the better-margin option | **Scope widens: show the cheapest through rate too.** Margin and customer price are different checks and this lane needs the second one |
| **Sales enablement** | — | Otto and Stacy are pitching "same price as the airline" while this is live. `sales-lead` should know before it happens in front of a prospect |
| **Measurement** | Margin per booking | **Add: quoted price versus best available through rate.** That ratio is measurable the day a quote log exists, and it is the number that says whether this is rare or routine |

---

## 7. For Ethan, when you come back

**Three things, and only the first is urgent tonight.**

1. **Question 1 in §4 should go to Kyri and Alex.** If the Monday ask has already gone, send it as a two-line follow-up rather than waiting for week 46 — it is a yes/no, and the answer determines whether this is a training conversation or a bug.
2. **Vadim has told you twice in one day that he is at the end of his rope** — "nothing we can do," "I largely stopped resending the same stuff over and over again." A COO who has stopped escalating is a bigger risk than any single quote. The calendar time in the draft note to him matters more now than it did this morning.
3. **"A more competent workforce" is a conclusion drawn from an incomplete picture**, and §2 is the reason to say so. I am not arguing against it — staffing is yours and Cheryl's, and he may be right about things this analysis cannot see. But it should not be decided on this example, because this example has a software fix and its headline number is wrong in the direction that makes the agent look worse than the evidence supports.
