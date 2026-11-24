# HANDOFF-T0024-C — corpdev → finance

**Raised:** 2026-11-24
**Related task:** TASK-0024
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need

**The reconciliation of the OMS Portal Revenue Tracking page to CSI's invoices** — Donald's
item, already open from `reports/freightflow-agreement-review.md` §7 (tests D1–D7), due before
any revenue-share payment goes out. Specifically:

1. **Portal-originated invoiced revenue** to date and its monthly trajectory.
2. **Whether the page's definition matches the contract's.** Ex. C §5.1(c) counts only revenue
   from services *"initiated directly by the customer through the Frontend System"* and excludes
   anything *"originated exclusively by email, phone, text or in any other manner."* The review
   names **at least six places a system and that definition could diverge** (§2.5) and could not
   confirm, because the page is not in the repo.
3. **Any subscription revenue**, since Ex. C §6 attaches **30% of subscription fees**.

## Why I need it

It is the single largest input to two of the routes in
`reports/ai-rollup-screen-and-platform-control.md` Part C — restructuring the revenue-share
basis (Route 4) and extinguishing the economic claims (Route 6). Both are priced off a **known
schedule applied to an unmeasured base**: 1.5% marginal rising to 3.5%, cumulative $7,500 at
$500K of portal revenue through $45,000 at $2M. **The schedule is known; the base is not.**

So the cost of the most tractable platform-independence work CSI can do is a number CSI does
not have and could have cheaply. It also matters on its own account: the first payment could
fall due as early as about **20 Jan 2027** on one reading of the Revenue Share Year, and the
Developer — not CSI — holds the audit right (§5.4).

## What I will do with it

Replace the `[ILLUSTRATION]` arithmetic in Part C Route 4 with CSI's actual obligation and its
trajectory, and state what restructuring it would be worth in present-value terms. That turns
an unpriced route into a priced one. I will also report whether the obligation is, as I
currently believe, **small in cash and material to the multiple** — which is the argument for
addressing it now rather than later.

## When I need it

**Before any revenue-share payment, which is the existing deadline, and ideally before the
counsel engagement** so the question goes in with a number attached rather than without one.

## What I'll do if I don't get it

Part C already says the cost is unknown and names this as the fact that would change it, so
nothing is invented and nothing stalls. The consequence is narrower and worse: **CSI would open
a counsel engagement, and eventually a commercial conversation, without knowing the size of the
obligation under discussion.**

**Note:** no figure from this goes outside CSI, and nothing here is drafted to be sent
(`CLAUDE.md` §7.5).

## PM decision
