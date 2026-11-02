---
title: Learnings and principles
owner: Ethan Silvey
as_of: 2026-11-01
source: Ethan's statements in the claude.ai Project (Feb–Oct 2026, see sources.md)
---

# Learnings and principles

Hard-won and costly to relearn. Do not re-litigate these without new evidence; if you
have new evidence, file a proposal. Source tags `[chat-id, date]` → `sources.md`.

## Market and growth

- **The acquisition engine is the constraint, not the product.** 2026 growth is
  yield-led (revenue +4.4%, bookings +1.3% Jan–Aug, `CLAUDE.md` §2). The job is turning
  that into volume growth without giving the yield back. (The "wins on price ~80% of
  the time" line is `[UNSOURCED]` — Ethan's own figure with no quote log and, by his
  account, no competitor pricing data [9dd8fd89, 2026-05-03]. Never use it externally.)
- The market is small and known: ~19,000 U.S. funeral homes. Filter out consumer traffic.
- **Success metrics:** quote requests from identified funeral homes, and AI citation
  rate. Not raw sessions.
- **Enterprise groups (SCI, Everstory, Carriage) are the highest-leverage plays** —
  portal lock-in, corporate reporting, and revenue-share structures independents can't
  replicate.
- **International corridors are the highest-margin opportunity.** Corridor expertise
  (Mexico/LatAm, Israel, China, Pacific/Asia) is a durable differentiator. Prioritize
  homes with high international volume.
- **The portal is the moat** — switching costs and corporate data visibility that price
  competition can't match. Ethan also wants portal analytics and user-behavior data
  captured so it can later be offered back to funeral home groups [86f9e25c, 2026-03-11].
- Eagle's Wings is competitive on only 1–2 airlines, where its carrier relationships let
  it push shipments; on average CSI is cheaper, especially at the scale of groups with
  100+ locations [7f2add68, 2026-02-20]. The ~10% EWA fee stays `[ASSUMPTION]` — Ethan
  said he was "not 100% sure" of it.
- **High-net-worth / white-glove clients are price-inelastic** and prioritize service.
  UHNW families are reached through intermediaries — family offices and estate
  attorneys — not directly [de7d319c, 2026-04-18].
- **Published claims must survive diligence** by enterprise groups and federal buyers.
  Accuracy beats the bigger number (case counts, ownership wording, gateway counts)
  [6c9305c6, 2026-09-17].

## Outreach and positioning

- **Backup-option framing works.** Position CSI as an addition, not a replacement,
  with directors loyal to an existing vendor.
- **Lead with discovery questions, not a pitch.** Cold email opens the conversation; the
  call closes it. This shaped every sequence, call script and the LinkedIn playbook
  [7b7210d9, 2026-10-30]. Use email to get a live conversation, not to explain the
  whole value proposition in writing [ac30efb5, 2026-05-06].
- **Warm-network and warm-intro activation is the primary motion** for the new reps
  [7b7210d9, 2026-10-30].
- **Speed (fast confirmation) is the right cold LinkedIn hook** for funeral directors
  [c57f43c3, 2026-06-09].
- Positioning: "experts on demand" for funeral directors. Brand pillars: speed,
  transparency, affordability, convenience. Approved paperwork hook: "Funeral directors
  don't have to drive to the consulate anymore." [3be24ce8, 2026-08-27]. Trade-show
  collateral theme: give time back to funeral directors, prominent call to action,
  international special services featured [fb8fecaa, 2026-04-04].
- **Published thought leadership names no competitors**, so CSI reads as a neutral
  expert [7b7210d9, 2026-10-30].
- Gatekeepers: if they withhold a name or email, leave the rep's details and a callback
  time; ask for five minutes up front. Ask existing customers open-ended feedback
  questions. When someone says "send me information," encourage them to share it with
  colleagues; don't ask about volume [9dd8fd89, 2026-05-03].
- Trade shows: directors stroll for swag but are open to networking. Passive
  booth-sitting ("do you guys do a lot of ship-outs?") is the thing to fix
  [9dd8fd89, 2026-05-03].
- **Partnership strategy:** two-way referrals are the low/no-cost lever. The goal is
  foreign partners doing lead-gen for CSI — steering families and U.S. funeral homes to
  CSI, and reselling CSI lanes with their own markup.
- In partner-facing copy, refer to Bergen generically as a "network partner," and omit
  CDC paperwork detail from inbound-process collateral [50840dd5, 2026-10-20].
- **IMS is a valued partner that refers significant business**; support it, don't compete
  with it, including in federal work [c5370b26, 2026-09-29]. National Mortuary Shipping
  and Bergen are allies and customers too (`CLAUDE.md` §5).

## Sales team

- Sales reps attend booking-process sessions for awareness, not training; reps do not
  do bookings. Day 1 onboarding is operations-led so reps have firsthand operational
  credibility [7b7210d9, 2026-10-30].

## Portal and product

- New shippers should be able to book without first creating an account; the account is
  auto-created on first booking (email as username, password set afterwards)
  [86f9e25c, 2026-03-11].
- Keep the customer front end and the agent back end as compatible as possible
  [86f9e25c, 2026-03-11].

## Data and compliance

- OMS dashboard data before 2023 is unreliable (migration artifacts).
- **SBA size calculations:** 13 CFR 121.104(a) excludes amounts freight forwarders
  collect for others. Never apply gross pass-through in an SBA size calculation.
- Federal work uses NAICS 812210 / PSC G001, not the freight codes CSI first registered
  under [c5370b26, 2026-09-29].
- **HubSpot company-name search is not a reliable de-duplication check** — it missed
  Carriage, Service Corporation, Park Lawn and Davidson Funeral. Check customers manually
  against OMS records [f9105c8e, 2026-10-13].
- Never invent operational facts for gateway or corridor pages; wait for the Kim/Susej
  ops questionnaire [6c9305c6, 2026-09-17].

## Operations and platform

- Verify domain ownership and renewal status before any platform migration.
  Single-vendor dependency on a web developer is a material operational risk.
- Kyri is a single point of dependency across critical workloads
  [57fb3179, 2026-09-29].
- Schedule platform migrations away from peak winter mortality season
  [57fb3179, 2026-09-29].
- Rebooking after cancellations is an unmeasured margin leak: CSI absorbs the cost ~99%
  of the time [5044cd91, 2026-02-02].
