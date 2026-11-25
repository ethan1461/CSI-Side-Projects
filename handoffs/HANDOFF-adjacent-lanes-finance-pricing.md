# HANDOFF — gtm-strategist → finance and pricing-strategist

**Raised:** 2026-11-24
**Related task:** adjacent lane sizing (`reports/adjacent-lane-sizing.md` §3)
**Urgency:** THIS WEEK
**Status:** OPEN

## What I need

Two things, and the second matters more than the first.

1. **DR-001 closed** — Donald's revenue and gross margin on secondary services, by fee type,
   FY25 and FY26 YTD (`context/brain/data-owners.md`, open request #1, drafted **2026-11-01**).
   Specifically, for consular and documentation work: **what CSI charges per international
   shipment today, and what it costs.**
2. **One consolidated international pricing recommendation, not two.** My lane 2 and
   `reports/the-25m-gap.md` §3's **$500 international margin floor** are the same dollar
   counted twice, and whoever writes the margin plan needs to know that before it reaches
   Ethan.

## Why I need it

**On (1).** Ethan says consular fees are charged **"at cost for the most part"**
(`the-25m-gap.md` §3). On that basis, moving international documentation from at-cost to a
priced service at **+$75 to +$150 per shipment** across CSI's **5,651 international
shipments a year** is **$424K–$848K of EBITDA at roughly 100% incremental margin** — the
work is already being performed by people already on payroll.

**That is the largest single number my whole report produced, and it is the only one that
needs no new buyer, no facility, no licence and no acquisition.** It is also entirely
`[ASSUMPTION]`, because nobody can tell me the current fee or its margin. The request to
the one person who holds it has been open 23 days.

**On (2), and this is the part that could do real damage if it is missed.** Two reports now
carry an international pricing uplift:

| Report | Lever | Sized at |
|---|---|---|
| `the-25m-gap.md` §3 | $500 international margin floor | $550K–$1.1M |
| `adjacent-lane-sizing.md` §3 (2a) | Reprice consular work from at-cost | $424K–$848K |

**If the floor is implemented by raising the all-in international price, these are one
lever.** I have deliberately **excluded** 2a from my report's totals for exactly this reason
(§5), and said so in the handoff to pm-orchestrator. But a plan that adds the organic levers
to the adjacent lanes and reports ~$2.6M against a ~$2.0M requirement would be wrong by
roughly the size of the gap it claims to close. The consolidated defensible optimistic range
is **~$1.9M–$2.2M.**

The substantive question only you two can answer: **is the right instrument a higher all-in
international price, or an itemised documentation fee?** They are not equivalent. An itemised
fee is defensible to a funeral director who can see the consular work being done, it can be
sold to buyers CSI does not carry (my lane 2b), and it does not touch the air rate that
underwrites the "no booking fee" position — which `ai-rollup-screen-and-platform-control.md`
§6.6 upgraded to Strong-with-caveat precisely because the axis is *whether a brokerage fee
exists at all*. A higher all-in rate is simpler and quieter but it erodes the one
differentiator CSI's cold outreach runs on. **My view is the itemised fee, and I would rather
be argued out of it than have both lanes priced independently.**

## What I will do with it

- Replace lane 2a's `[ASSUMPTION]` uplift with a real fee-and-margin figure and re-run
  `scripts/size_adjacent_lanes.py`, which takes a minute.
- Scope lane 2b's test (my recommendation #5: offer the documentation package to 40 accounts
  that ship with someone else, kill it if fewer than 5 will pay $400). **I cannot price that
  test until I know what the work costs**, and pricing it wrong is how a test produces an
  unreadable answer.
- Drop lane 2a from any GTM plan entirely if you conclude it belongs to the margin
  workstream. That is the right outcome and I am not defending territory.

## When I need it

**DR-001: this week** — it has already waited three. Ethan sends it; it is one conversation
with Donald, who per `context/brain/data-owners.md` prefers to talk first and then share.

**The consolidation question: before Monday's decision document**, so the two levers reach
Ethan as one recommendation rather than as two numbers he has to reconcile himself.

## What I'll do if I don't get it

Lane 2 stays `[ASSUMPTION]` and I will say so wherever it is quoted — it is already labelled
that way in `reports/adjacent-lane-sizing.md` §3. The report's verdict does not change,
because 2a is excluded from the totals anyway. **What I cannot do without it is tell anyone
whether CSI is leaving $424K or $848K on the table, or nothing at all** — if the consular
fee is already priced above cost, the number is zero and my §3 is wrong. That possibility is
exactly why the request matters.

**The smallest version that would still unblock me:** one figure. Average secondary-service
revenue per international shipment, FY26 YTD, and whether it is above or below cost.

## PM decision

<Routed / rejected / merged, with a one-line reason. Filled by pm-orchestrator.>
