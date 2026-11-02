---
title: Who owns which data, and how to ask for it
owner: pm-orchestrator (maintains), Ethan (sends every request)
as_of: 2026-11-01
source: Ethan, 2026-11-01 — "Whatever data we need, we should be asking our colleagues for."
---

# Data owners and data requests

**Standing rule (Ethan, 2026-11-01):** when the team needs data it doesn't have, the
answer is to ask the colleague who owns it. Not to estimate around the gap, not to wait
for it to appear. A missing number is a request someone hasn't sent yet.

## How a request works

1. The agent that hits the gap checks this file and `context/DATA-INVENTORY.md` first,
   so the same colleague is never asked twice for the same thing.
2. It drafts the request from `templates/data-request-template.md` into
   `reports/pending-approval/data-requests/` and adds a row to **Open requests** below
   (via `/brain-propose`, like any brain change).
3. **Ethan sends it.** Agents never contact colleagues directly (`CLAUDE.md` §5:
   agents draft, never send).
4. When the data arrives, a human places it in `data/raw/`; the requesting agent updates
   `DATA-INVENTORY.md`, and the PM closes the row.

**Make requests easy to say yes to:** one owner, one ask, the exact fields and period,
the smallest version that would still unblock the decision, and the decision it
unblocks. Bundle asks to the same person into one message per week at most.
Kim Soto and Susej Roffe prefer async questionnaires to meetings.

## Who owns what

Owners marked *likely* are the team's best guess; the first request to them confirms it.

| Data | Owner | Notes |
|---|---|---|
| Margin analytics, lane profitability, cost to serve | Donald (Finance) | `CLAUDE.md` §5 |
| Revenue and margin on secondary services (consulate support, pickup/drop-off, other ancillary fees) | Donald — *likely* | Ethan to confirm the route |
| Marketing spend by channel by month | Donald — *likely* | Blocks CAC and ROAS |
| International carrier costs (IAG, Emirates, Lufthansa, etc.) | Donald / Vadim | `CLAUDE.md` §4.3 |
| Shipment-level OMS export | Alex (builds exports), Kyri (OMS) | Biggest single gap |
| Legacy-system extract for reconciliation | Vadim / Alex — *likely* | |
| Portal adoption (accounts onboarded, portal vs. phone bookings) | Kyri / Vadim | |
| Booking-desk practice, rework, exceptions | Kim Soto, Susej Roffe | Questionnaire, not meeting |

## Open requests

| # | Ask | Owner | Unblocks | Drafted | Status |
|---|---|---|---|---|---|
| 1 | Revenue and gross margin on secondary services, by fee type, FY2025 and 2026 YTD | Donald — *likely* | Full revenue model; pricing and valuation work | 2026-11-01 | Draft in `reports/pending-approval/data-requests/` — awaiting Ethan |
