---
title: Customer portal (incl. SCI pilot)
owner: Ethan Silvey (build: Kyri, Alex)
as_of: 2026-11-01
source: Ethan's statements in the claude.ai Project — 86f9e25c, e7361fde, cc6236ef, 9f4a41e6, 49e74d16, ed2e6f96 (see sources.md)
---

# Customer portal

**Goal:** a funeral-home-facing portal where homes and groups quote, book, track and
manage shipments — the switching-cost moat and the corporate-reporting hook for
enterprise groups (`learnings-and-principles.md`).

**Owner:** Ethan. Build: Kyri and Alex. SCI side: Pam Heath.

## Status (as of 2026-11-01; latest source 2026-10-30)

- **Mar 2026 — V1 built** [86f9e25c, 2026-03-11]: admin "Portal Customer Onboarding"
  page (pick a funeral home → its emails become users → Create Users); Manage Users tab
  (access, password reset); customer view with booking summary, quote requests and new
  booking requests. The quote tool shows estimated prices and cargo-facility hours.
  OMS booking statuses: Pending, Booked, Waiting Airline, Booking saved as draft.
- Feb 2026 plan: wireframes Q1, beta ~June, July platform deadline [e7361fde].
- May 2026: Ethan told Everstory the portal launches in July [cc6236ef]. Whether it did:
  open question.
- **Jun 2026:** built portal demoed to SCI (Quote → Booking → Tracking); pilot shortlist
  sent [9f4a41e6, 2026-06-28].
- **Aug 2026: SCI pilot approved** for a small number of locations. Location intake
  checklist and intro wording sent to Pam for her Friday comms; Lauren kept in the loop.
  Pilot copy value props: instant quotes, real-time flight tracking, centralized booking
  history — which are live is unconfirmed [49e74d16, 2026-08-13].
- **Oct 2026:** portal training Round 2 for the sales reps on 2026-10-29, led by Kyri and
  Alex [7b7210d9]. **Document upload** (passports, death certificates, consular papers)
  is **on hold pending a privacy legal review**, which Ethan agreed to; Kyri and Alex
  raised it [ed2e6f96, 2026-10-30].

## Key decisions

- Auto-create the account on first booking (email as username) [86f9e25c].
- Capture portal analytics and user behavior for later resale to groups [86f9e25c].
- Keep customer front end and agent back end compatible [86f9e25c].
- SCI pilot is the gate for later SCI work (Feb 2026 plan) [e7361fde].
- Planned features listed in Feb–Jun 2026: email-parsing intake, quote calculator,
  tracking dashboard, document upload/download, SCI white-label regional tenants,
  role-based access, SSO [e7361fde; 9f4a41e6].

## Next steps / open

- Which SCI locations are live and who sent the introductions (status unknown since
  2026-08-13).
- Privacy review outcome and privacy-lawyer engagement (`open-questions.md`).
- First-portal-booking incentive at NFDA: `nfda-2026.md`.
- Hosting for the new OMS/portal is undecided: `aws.md`.
