# Paid search lead conversion — did the 78 leads become bookings?

**Date:** 2026-11-03 · **Task:** TASK-0022 Part 1 · **Author:** marketing-lead
**Sources:** `data/raw/google-ads-20261103/` (15 reports, 1 Sep – 2 Nov 2026), HubSpot (live read, contacts created since 30 Aug), `data/raw/oms-funeral-homes-20261103.csv`, `data/raw/hubspot-all-contacts-20261102.csv`
**Script / output:** `scripts/paid_search_lead_match.py` → `data/derived/paid-search-lead-match.csv` (+ `.meta.json`). Output holds HubSpot record IDs and OMS funeral home IDs only. No names, emails or phones are written anywhere.
**Confidence:** High on the method and the cost basis. **Low on the result, because it is not yet knowable from the data we hold.** What would raise it: the three pulls in section 3.

> **Correction to carry with every figure from this account.** The account's own headline of 446 conversions, a cost per conversion of $9.23 and a 31.59x return is not real. 368 of Campaign #1's 391 conversions came from YouTube, each carrying a $200 value typed into a settings field (`reports/google-ads-should-we-pull-back.md`). Ethan has removed that value and paused Performance Max. Do not quote the old figures without this note.

---

## The answer

1. **Result: unresolved, not negative.** The bar is low: CSI breaks even if roughly **5 to 6 of the 78 leads** become a booking (1 in 14). We can identify who only 21 of the 78 leads were, and of those 21, **none is a new account that has booked since**. That is not evidence against paid search, because 57 of the 78 have no identity in any system we hold.
2. **Recommendation: HOLD.** Stay inside the envelope already recommended ($70/day, to $85/day only if cost per conversion holds in the $30s). **Do not go past ~$100/day, and do not treat paid search as proven**, until the check in section 3 is done. It is also not a STOP: the bar is 1 in 14, and most of the leads are unchecked.
3. **The check needs a human with OMS access.** I have proposed a named owner and a time budget in `handoffs/HANDOFF-T0022-lead-check-owner.md`. Everything the human needs is below.

## 1. What the 78 are, and what they cost

| Source | Clicks | Conversions | Cost (exports) | Cost per lead |
|---|---|---|---|---|
| Campaign #1, Google Search channel only | 412 | 23 (8 Contact + **15 phone call leads**) | $943.86 | $41.04 |
| Leads-Search-1 | 1,233 | 55 | $1,736.97 | $31.58 |
| **Combined** | **1,645** | **78** | **$2,680.83** | **$34.37** |

Files: `028a841e-Search_terms_insight_report.csv` (Campaign #1 channel rows), `7184c97a-Landing_page_report.csv` (row "Total: Search" for Leads-Search-1), `Performance by channel.csv` (55 Search conversions).

**Flag on the earlier report's cost basis.** `google-ads-should-we-pull-back.md` used $1,600.92 for Leads-Search-1 ($32.63 per lead, ~$3,605 total spend since launch). **I cannot reproduce those two figures from the 15 exports.** The exports give $1,736.97 for Search, and a weekly cost series (`Cost and engagement.csv`) that sums to **$4,118** for the account. The gap is plausibly billing credits or a different date cut (the earlier report cites a billing summary screenshot that is not in this folder), but it is unexplained. **Both are shown: $32.63 per lead on the billing basis, $34.37 on the export basis.** Neither changes the conclusion. Ethan or Donald to confirm which is net-of-credit.

**Break-even.** A booking yields about $1,346 at 35% to 41% gross margin, so $470 to $550 of contribution. Those margins are rate-card margin on contracted lanes, unweighted by volume and excluding cost to serve (`reports/carrier-margin-resolved.md`), so treat the bar as approximate.

| Cost basis | Spend | Bookings needed to break even |
|---|---|---|
| Billing basis | ~$2,545 | 4.6 to 5.4 |
| Export basis | $2,680.83 | 4.9 to 5.7 |

So **5 to 6 bookings out of 78**, or 1 in 14. A first booking from a new account is worth more than one booking, which this ignores; it is deliberately conservative.

## 2. What the first-pass match found (21 of 78)

Of the 78 conversions, HubSpot holds **21 contacts** with source PAID_SEARCH and a gclid on their first page view, created 10 Sep to 2 Nov. The other 57 are not in HubSpot as paid-search contacts. I matched the 21 to the OMS funeral home master (exact email, then business email domain).

| | Count |
|---|---|
| Paid-search contacts in HubSpot | 21 |
| Business email domain / generic (gmail etc.) | 6 / 15 |
| Matched to an OMS funeral home | 2 (both by domain) |
| of which have booking history | 2 |
| of which **first booking is on or after the contact date (new account)** | **0** |
| No OMS match | 19 |

**Reading it.**
- The two matches are **existing accounts**, so any later bookings are not new business. Whether the ad prompted extra volume from a customer already shipping is unknowable from aggregates.
- **Fifteen generic-domain contacts are not automatically families.** Small independent funeral homes do use gmail; at least one paid-search contact is a funeral service on a gmail address. A name-and-email match cannot settle this. A human who knows the market can.
- **Control:** of all 46 contacts created in the window (any source), 13 have booking history and 4 have a first booking on or after their contact date. So the OMS join works; it is the paid-search contacts that mostly do not resolve.
- **Not independent evidence of new accounts.** `first_booking_date` and `last_booking_date` are account-level fields. This pass cannot count bookings or revenue, only whether any exist after the contact date. Booking-level data (EA-45-02) removes this limit.
- **Campaign mapping is unverified.** The gclid URLs carry three campaign IDs (13 contacts on ending `…453898`, 7 on `…234358022`, 1 on `…194896964`). None equals the ID in the search terms export (`8504940155`), so I cannot say which contacts came from Campaign #1 (now paused) and which from Leads-Search-1. Ethan can map them in the Ads UI in one minute.

## 3. The method for the human check

Time estimate: **2 to 3 hours** with OMS access. The owner needs three inputs.

| # | Input | Who pulls it | Covers |
|---|---|---|---|
| A | `data/derived/paid-search-lead-match.csv`, the 21 matched/unmatched contacts by HubSpot record ID | Done (this report). `revops-crm` can attach company names inside HubSpot | 21 form leads |
| B | **Google Ads call details report** for Campaign #1 and Leads-Search-1, 1 Sep to 2 Nov: call start, duration, caller area code, status. Ethan exports it (read-only, no change to the account) | Ethan | The **15 phone-call leads**, the most credible signal in the account |
| C | The ~42 other form conversions: find out what fires them. The brain records that the conversion triggers were unattached as of 17 Sep and that legacy forms post by AJAX with no thank-you page, so some "Contact" events may be clicks, not submissions | `data-analyst` (GA4 / GTM), after the brain's open tracking question is answered | Up to 42 conversions that have no contact record |

Steps for the owner:
1. For each HubSpot contact in A without an OMS match, search the OMS by the contact's company name and email domain. Record `funeral_home_id` or "not a customer".
2. For each call in B, match the caller number to the OMS funeral home phone. Record the same.
3. For every matched funeral home, read off **first booking date, bookings since the lead date, and revenue** from the OMS. Record **days from lead to first booking** (the lag).
4. Mark each: **new account / existing account / not a funeral home / unresolved**. Existing-account bookings are reported separately and not counted toward the bar.
5. Fill the table below and send it back to marketing-lead, who re-runs the figures. **Re-check on 15 Dec** to catch bookings with a longer lag; funeral homes add a backup carrier slowly.

| Result table (to complete) | Value |
|---|---|
| Leads checked | __ of 78 |
| Of those: funeral homes / not funeral homes / unresolved | __ / __ / __ |
| **New-account bookings** (count, revenue, median lag) | __ , $__ , __ days |
| Existing-account bookings after lead date (count, revenue) | __ , $__ |
| **Implied cost per new-account booking** (spend ÷ bookings) | $__ vs break-even ~$470–550 |
| Leads per new-account booking | __ vs break-even ~14 |

## 4. Decision rule, set before the number arrives

| New-account bookings from the 78 | Action |
|---|---|
| **6 or more** (better than 1 in 14) | Scale. Raise the ~$100/day gate in steps; Ethan executes |
| **2 to 5** | Hold at current spend and run the attribution spec (`reports/quote-attribution-spec.md`) to read it properly. The sample is too small to call |
| **0 or 1 after the 15 Dec re-check** | Reduce toward a minimal brand-and-intent keyword set and redirect the money. Report the negative result |

**Statistical honesty.** At ~35 leads a month and a 1-in-14 bar, break-even is about 2.5 bookings a month. That is a tiny count. One checking round cannot separate a 1-in-14 rate from 1-in-40. `data-analyst` should confirm the minimum test length; my expectation is that a clear read needs three to four months of attributed data, which is the case for building the spec now.

## 5. What I did not do
Google Ads is untouched. No page, ad or HubSpot record was changed. Names seen in a live HubSpot read were used only to confirm the query and are not recorded.
