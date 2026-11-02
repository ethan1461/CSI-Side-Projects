---
title: Ways of working
owner: Ethan Silvey
as_of: 2026-11-01
source: Ethan's statements in the claude.ai Project (Feb–Oct 2026, see sources.md)
---

# Ways of working

Source tags `[chat-id, date]` → `sources.md`.

## How Ethan wants drafts

- **Short-form drafts with multiple variant options**, not a single recommendation.
  Iteration is the norm. Emails come in two versions: warm/conversational and
  polished/professional [7b7210d9, 2026-10-30]. Creative assets (ad headlines etc.)
  come grouped by angle; expect several rounds [94319f3f, 2026-08-30].
- Concise, conversational copy. Lead with the customer's pain point, not features.
- Voice: direct, confident, concrete claims; no vague flattery [50840dd5, 2026-10-20].
- Warm but polished — safe to forward internally. Enterprise follow-ups are
  forward-ready, with no casual phrasing; themes are gratitude, partnership and
  conviction about value [9f4a41e6, 2026-06-28].
- He prefers specific line edits (or rephrases drafts himself) over wholesale rewrites
  [50840dd5, 2026-10-20], and prescriptive, specific guidance over general frameworks
  [9d6d7fa8, 2026-10-04].
- He sends detailed, often pasted feedback (including from outside sources) and expects
  all of it incorporated [7b7210d9, 2026-10-30].
- **When an operational fact changes (e.g. the gateway list), update every material that
  carries it**, not just the current one [7b7210d9, 2026-10-30]. See
  `deliverables-index.md` → stale material.
- Lists and trackers as **Excel (.xlsx)**, not CSV, so he can track them live.
- Enterprise deliverables in two forms: an interactive artifact and a .docx
  [9dd8fd89, 2026-05-03; 9f4a41e6, 2026-06-28]. Collateral as editable .docx layout
  options on light backgrounds with navy/cyan, not dark HTML [fb8fecaa, 2026-04-04].
- Branded HTML loses styling in PDF export; long-form reports go to Markdown for Claude
  Design [7b7210d9, 2026-10-30].
- **Deliverables for the sales reps are standalone PDF/Excel files**, never Drive or Docs
  links — the reps cannot reach Drive [7b7210d9, 2026-10-30].
- Territory hit lists: one row per funeral home (never per corporate group), sorted by
  volume, with a "Corporate Group/Network" column [7b7210d9, 2026-10-30].
- Event and conference data is checked against official association websites
  [7b7210d9, 2026-10-30]. Verify exhibitors' business models on the web rather than
  assuming; tier exhibitor lists (competitor recon, software partners, supply chain,
  referral/consulting, direct prospects, booth neighbors) with a goal per tier
  [398df582, 2026-06-09].
- LinkedIn: connection notes ≤300 characters including spaces [de7d319c, 2026-04-18];
  cold copy 1–2 sentences [c57f43c3, 2026-06-09]; sequential posts split by angle and
  never repeat stats [3be24ce8, 2026-08-27].
- Models (e.g. pricing calculators): build the math back end first and the UI later;
  inputs stay dynamic; start from averages; show a per-route micro view and an annual
  macro view; separate domestic and international versions [7f2add68, 2026-02-20].
- Planning trackers are organised by quarter, in chronological order, tagged
  conditional on approvals, and tied to each owner's roles and KRs; Ethan tracks them in
  Asana [e7361fde, 2026-02-16].
- Programs run from a master tracker (tasks, gates, risks, vendor actions), a charter,
  and a canonical fact sheet that all copy references [6c9305c6, 2026-09-17].
- CSO to-do lists stay tightly scoped to near-term, owned actions. No strategic framing
  items or long-horizon plays on them.

## Getting data

- **Data the team needs, we ask our colleagues for** (Ethan, 2026-11-01). Agents draft
  the request; Ethan sends it. Owners and open requests: `data-owners.md`.
- Which customer document types CSI collects: ask Cheryl (Microsoft 365 Global Admin)
  [ed2e6f96, 2026-10-30].
- AWS/server configuration questions go to Rednodo in writing; never send Rednodo
  actual customer files [ed2e6f96, 2026-10-30].

## Approval gates

- Nothing publishes, sends, spends, or writes to HubSpot without Ethan's sign-off.
- **Operations sign-off is required on every factual claim before publication.**
- Credentials are never shared with Claude or with agents. Whether a logged-in browser
  session counts is open (**C14**, `open-questions.md`).
- Files containing live credentials or database dumps are never forwarded; ask for a
  sanitized copy and credential rotation [d1fa8e90, 2026-09-16].
- Draft copy never mentions the family relationship between the CSO and the CEO
  (`CLAUDE.md` §5) [af828b2f, 2026-04-29].

## Working with the team

- New business is led by Ethan and Vadim with CEO support; Kim Soto and Susej Roffe stay
  on core bookings and are not given strategic-initiative tasks [e7361fde, 2026-02-16].
- Kim Soto and Susej Roffe (Bookings Directors) prefer async questionnaires over live
  interviews.
- Kyri is engaged only when blocked or for implementation handoff, not managed as a
  workstream owner.
- Ethan handles vendor requests himself, in numbered batches, and offers a call if
  faster [6c9305c6, 2026-09-17].
- Internal operating norms (all-hands, March 2026) [a7877708, 2026-03-04]: work messages
  from the oldest unread forward; acknowledge every question with a timeframe — "no
  message should die in silence"; client-facing concerns go through Vadim first; other
  problems escalate to Kim, Susej, Vadim, Ethan, Cheryl or Donald.

## Brand

- Branded collateral follows the CSI brand design kit (kept in Claude Design projects).
  Brand kit v1 carried wrong figures — see `deliverables-index.md`.

## Tools in use

HubSpot (CRM; 878-account target workbook), Microsoft 365 (mail), OMS + customer portal
(internal), Google Ads / Performance Max (live; conversion tracking incomplete — see
`initiatives/google-ads.md`), Next.js website (domain at GoDaddy, moving DNS to
Cloudflare), AWS (legacy ERP), Asana (Ethan's planning), SAM.gov, USAspending.gov,
Sunbiz. LinkedIn people searches in a browser throttle after ~50–75 per session
[50840dd5, 2026-10-20]; agents do not use LinkedIn without Ethan.

## Industry landscape

- Associations: NFDA, FIAT-IFTA, ICCFA, TFDA, IFDA, state FDAs (NY State, NY Metro,
  NJ, Illinois).
- Competitors tracked: Eagle's Wings Air, Inman Shipping Worldwide, ILS. National
  Mortuary Shipping and IMS are partners as well as competitors (`CLAUDE.md` §5).
- Software integration candidates: FuneralOne, Passare, Osiris, Arrange Hub, Tukios,
  MorTrac, Funeral 365.
