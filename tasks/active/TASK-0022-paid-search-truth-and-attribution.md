# TASK-0022 — Check the 78 leads, then spec the attribution that ends the argument

**Owner:** marketing-lead
**Created:** 2026-11-03 by pm-orchestrator
**Due:** 2026-11-10
**Priority:** HIGH
**Status:** IN PROGRESS — Parts 1 and 2 delivered; landing-page review PARTIAL (blocked on page text); lead check awaiting named owner

## Objective

`reports/google-ads-should-we-pull-back.md` (2026-11-03) established that the account's
headline numbers were fiction: **368 of 391 Performance Max conversions came from YouTube**,
carrying a **$200 value someone typed into a settings field**, which is what produced a
reported 31.59x return. HubSpot gained 45 contacts across the entire nine-week ad window and
September and October are indistinguishable from the eight months before the ads started.

Ethan has since **removed the $200 value and paused Performance Max entirely.**

What survives is real and small: **78 leads from search traffic at $32.63 each, including 15
phone-call leads.** Nobody knows whether any of them became a booking. That is the question
this task answers — first by hand, then permanently.

## Line to the metric

Enabling, then primary. CSI has spent a year unable to connect a marketing dollar to a
booking. At ~$470–550 contribution per booking, **CSI can afford about 14 leads per booking
and break even.** If more than 1 in 14 of the 78 converts, paid search is profitable and
should be scaled into a category growing 25% a year where CSI holds 23.67% impression share.
If not, the budget frees up. **Either answer is worth having.**

## Deliverable

### Part 1 — the manual check, this week

`reports/paid-search-lead-conversion.md`. Take the 78 search-sourced leads from the window
and check them against bookings by hand. Report: how many converted, over what lag, at what
value, and the implied cost per booking against the ~14-lead break-even.

**This needs a human with system access, not an agent.** The deliverable is the method, the
matched list, the result, and a named owner for the checking itself — raise a handoff to the
orchestrator to get that person assigned. **Do not let this stall because the data needs a
human; say who and keep moving.**

### Part 2 — the attribution spec

`reports/quote-attribution-spec.md`, written to go into the Monday engineering ask.

**The pieces already exist, which is why this is cheap.** CSI's quote system issues numbered
quotes (#52194 observed) carrying the shipping funeral home's name, email and phone. The OMS
has `funeral_home_id` and booking records. The missing links are only:

1. Capture the ad click identifier (`gclid`) on the quote form and store it with the quote.
2. Make the quote queryable, with its funeral home and its date (this is engineering ask
   item EA-45-08 — **do not duplicate it, reference it**).
3. Join quote → booking, which the booking-level export (EA-45-02) already enables.

Specify the fields, the join, and what CSI could then report. Keep it to a page an engineer
can build from.

## Also in scope, and it is not a marketing question

Two of the account's trending search terms are **"how much does it cost to ship a body to
another state"** (+217%) and **"can you transport a dead body yourself"** (400/month).

**Those are families, not funeral directors.** CSI sells to funeral directors, never end
consumers (`§1`). Two consequences: some paid traffic cannot buy at any price, and
**grieving families are reaching CSI's website.**

Review what those visitors land on and report whether it meets `§7.4` — warm, unhurried,
specific, and written as though a grieving family might read it, because they are. **Do not
change any page.** Report what you find and recommend.

## Success criteria

- [ ] The 78 leads checked, or a named human owner assigned and the method documented
- [ ] Result stated against the ~14-lead break-even, with a clear scale / hold / stop recommendation
- [ ] Attribution spec is buildable without a follow-up call
- [ ] Landing-page review against `§7.4` delivered with specific line-level findings
- [ ] Every figure traceable to `data/raw/google-ads-20261103/` (`§7.3`)

## Constraints

- **Google Ads is read-only for agents** (`§5`). No budget, bid or campaign changes — Ethan
  executes all of them. Recommend freely; touch nothing.
- **Do not publish or stage any content, page or ad.** `§7.1`.
- The $9.23 cost-per-conversion and 31.59x return figures are **not to be repeated anywhere**
  without the correction attached. They are in the FY26 record and will resurface.
- `CLAUDE.md §3.6` calls Google Ads "an active, funded leak." At ~$2,000/month and 0.17% of
  revenue that framing is wrong. **File a brain proposal to correct it** rather than editing
  `CLAUDE.md` directly.

## Dependencies

- Blocked by: none for Part 1 analysis.
- Related: EA-45-02 and EA-45-08 in `reports/pending-approval/engineering-ask-2026-45.md`
- Inputs: `data/raw/google-ads-20261103/` (15 reports), `reports/google-ads-should-we-pull-back.md`

## Approval gate

Analysis and specs are free. **Any campaign change, any page edit, any published content is
gated** (`§7.1`).

## Log
- 2026-11-03 — Created. Supersedes most of TASK-0001, which is revised to point here.

- 2026-11-03 — Claimed by marketing-lead. Delivered: `reports/paid-search-lead-conversion.md` (method, cost basis, first-pass match of 21 of 78 leads via `scripts/paid_search_lead_match.py`; result UNRESOLVED, recommendation HOLD), `reports/quote-attribution-spec.md` (for the week-46 engineering ask; references EA-45-02 and EA-45-08), `reports/landing-page-tone-review.md` (address-level findings only; `www.cargosalesintl.com` does not resolve from this session, so no line-level text was read). Handoffs raised: `handoffs/HANDOFF-T0022-lead-check-owner.md` (proposes Susej Roffe, alt. Kim Soto), `handoffs/HANDOFF-T0022-landing-page-text.md`. Brain proposal filed: `context/brain/_proposals/2026-11-03-google-ads-not-a-funded-leak.md`.
- 2026-11-03 — Finding for the orchestrator: the earlier report's $1,600.92 (Leads-Search-1) and ~$3,605 total are not reproducible from the 15 exports, which give $1,736.97 and ~$4,118. Cost per lead is $32.63 (billing basis) or $34.37 (export basis). Needs Ethan or Donald to confirm which is net of credits. Also: the two trending search terms are not in the exports; only in the earlier report.
- 2026-11-03 — Nothing in Google Ads, HubSpot or any page was changed. Success criteria status: 78 leads — owner proposed, method documented (met); result vs break-even — stated as unresolved with hold (met); spec (met); line-level review (NOT met, blocked); traceability (met, with the two exceptions above).

## Outcome
