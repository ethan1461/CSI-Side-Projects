# TASK-0025 — Scope the FreightFlow amendment and build the diligence pack

**Owner:** legal-risk
**Created:** 2026-11-24 by pm-orchestrator (created retroactively — see Log)
**Due:** 2026-11-24
**Priority:** HIGH
**Status:** DONE — delivered 2026-11-24, pending quality review

## Objective

CSI owns the OMS but cannot today staff, integrate or scale it without FreightFlow's
agreement, and Ethan has decided to pursue an acquisition programme that runs straight
into that. Scope the amendment CSI would want, separate what is genuinely negotiable from
the Developer's core economics, tighten the counsel brief to what actually gates the
conversation, and turn the diligence list into a checklist with named holders.

## Line to the metric

Enterprise value. The platform dependency is the longest-lead-time item in the roll-up
thesis because it needs counsel and a counterparty's agreement, and the revenue share gets
more expensive to renegotiate as portal volume rises.

## Deliverable

`reports/freightflow-amendment-scope.md` — **delivered.**

## Success criteria

- [x] Ranked list of what CSI needs changed, by what blocks the thesis
- [x] Negotiable versus core economics separated
- [x] Counsel brief tightened to the gating items
- [x] Diligence pack as a checklist with named holders
- [x] The §10 non-disparagement problem addressed
- [ ] Quality review by pm-orchestrator against `CLAUDE.md` §8 — **outstanding**

## Constraints

No contact with FreightFlow, Kyri, Alex or any third party. Nothing drafted to be sent, no
proposed amendment language. Not legal advice. Did not re-read the signed PDF. Kyri is
never described as CSI's CTO.

## Dependencies

- **Blocked on Ethan and Donald:** locating the **executed** agreement with its Effective
  Date, Acceptance Date and Change Orders (gate G0). Both prior reports rest on an unsigned
  copy with a blank Effective Date, so every clause finding is provisional until that is
  re-checked.
- **Counsel gates:** G1 (T4 — is a raise a "Sale of CSI"), G2 (I1/I2 plus I6/I7), **G3/N1 —
  new** (may CSI have others integrate on its own code), G4 (S9/K3, only if hiring is in
  the ask), **G5/N2 — new** (what Ethan may say to the Developer about acquisition plans).
- **Handoffs raised:** corpdev (negotiability, six judgements, sent early);
  product (five constraints on migration design and data intake).

## Log

- 2026-11-24 — **created retroactively.** The work was commissioned directly in-session
  when Ethan asked for the agent force deployed, and I briefed legal-risk without opening a
  ledger entry first. That was my process error, not the agent's; it flagged the gap in its
  handback and asked for the entry. `CLAUDE.md` §10 — all work flows through `tasks/`.
- 2026-11-24 — delivered. Nine items ranked: four hygiene, three tradeable, two core
  economics. **The thesis is blocked by the hygiene items and the trades, and only dragged
  by the economics** — the revenue share is ninth, at roughly $45K a year at $2M of portal
  revenue. Six of ~40 open items gate the conversation. 17-item diligence pack with
  accountable holders; five of those cost hours and need no counsel.
- 2026-11-24 — **corrected my grounding report in three places, all reducing severity.**
  "Satisfied" on ownership was too strong; "a third party can decline each integration"
  overstates the Change Order test and turns on new question N1; §9.1 blocks hiring the
  people who know the system rather than staffing as such. All three accepted and applied
  to `reports/ai-rollup-thesis-grounding.md` §6.2.
