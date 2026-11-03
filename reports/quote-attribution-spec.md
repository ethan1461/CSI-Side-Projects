# Quote attribution spec — ad click to quote to booking

**Date:** 2026-11-03 · **Task:** TASK-0022 Part 2 · **Author:** marketing-lead · **For:** Monday engineering ask (week 46), as a supplement to EA-45-02 and EA-45-08
**Goal:** every paid click that becomes a quote can be followed to a booking and a dollar, so cost per booking is a query, not an argument.
**Type (CSI's read, not a ruling):** feature, small. Fields and a join on records that already exist. Kyri and Alex classify it.

## What already exists (so this stays small)
- The quote system issues numbered quotes (#52194 observed) that carry the shipping funeral home's name and email.
- The OMS holds `funeral_home_id` and booking records.
- HubSpot already stores the ad click ID on the contact's **first page view** (`hs_analytics_first_url` contains `gclid` for the 21 paid-search contacts since 30 Aug). So the click ID reaches the website; it is lost before the quote.

## The three missing links

### 1. Capture the click ID on the quote request (new work)
On any page, when the URL contains `gclid`, `gbraid` or `wbraid`, store it in a **first-party cookie for 90 days** along with the landing URL and first-touch timestamp. On the quote form, submit them as hidden fields and **store them on the quote record**:

| Field | Type | Note |
|---|---|---|
| `gclid`, `gbraid`, `wbraid` | text, nullable | Whichever the click carried. Do not alter the case |
| `landing_url` | text | First page of the visit, **query string stripped of everything except the three IDs and `utm_*`** |
| `utm_source`, `utm_medium`, `utm_campaign`, `utm_term` | text, nullable | Same cookie |
| `first_touch_at` | timestamp | When the cookie was set |
| `lead_channel` | enum | `web_form`, `phone_dni`, `portal`, `agent_entered`. Required |
| `call_id` | text, nullable | For `phone_dni`: the call-tracking provider's call ID (see "Phone path") |

Quotes created by an agent from a phone call, or inside the portal, will have blank click fields; that is expected. `lead_channel` is what lets us say how much is unattributed rather than hide it.

**For engineering to answer (E / D / N: exists, derivable, doesn't exist):** (a) is the quote created from the website form, the portal, or only by an agent? (b) the brain notes the legacy forms post by AJAX with no thank-you page; does the quote form do that too, and can a confirmation event fire on success?

### 2. Make the quote queryable (this is **EA-45-08**; referenced, not duplicated)
EA-45-08 asks whether quotes are stored with price, lane and date and linked to the booking. This spec adds only the nine fields above to that request. **Minimum from EA-45-08 that attribution needs:** `quote_id`, `quote_created_at`, `shipping_funeral_home_id`, `origin`, `destination`, `quoted_total`, `status`. Smallest version: a nightly CSV to the Drive folder alongside EA-45-02, one row per quote.

**Excluded at the query, named columns only (`CLAUDE.md §7.2`):** decedent name, family contact, consignee, free-text notes, agent identity, and the funeral home's individual contact names, emails and phones. The funeral home is identified by `shipping_funeral_home_id` alone.

### 3. Join quote to booking (enabled by EA-45-02)
Add **one column to the EA-45-02 booking file: `source_quote_id`** (null when the booking did not start from a quote). That is the entire join:

```
click (gclid) -> quote.quote_id -> booking.source_quote_id -> booking.revenue
                  quote.shipping_funeral_home_id -> OMS funeral home (new vs existing account)
```

**If `source_quote_id` cannot be stored**, the fallback join is `shipping_funeral_home_id` + same origin and destination + booking date within 30 days of the quote. It is looser; the unmatched share will be reported.

## Phone path (required; the buyer phones)
Most funeral directors phone rather than fill in a form, so form attribution alone will understate paid search. Dynamic number insertion (DNI) by campaign, or Google Ads call reporting with call assets, stores a `call_id`, caller number, start time and campaign. The booking desk records the `call_id` on the quote or booking when the agent opens one. **Ethan decides the provider and the spend; this is not an engineering item except for the one field.** Until it exists, call volume is read from the Google Ads call details report and matched to funeral home phone by hand (see `reports/paid-search-lead-conversion.md`).

## What CSI can report once built (weekly, by `data-analyst`)
| Report | Definition |
|---|---|
| Leads → quotes → bookings by campaign and keyword (`utm_term`) | Counts at each step, with the median days between steps |
| **Cost per quote, cost per booking** | Spend ÷ attributed quotes and bookings, by campaign |
| **Contribution return on ad spend** | Attributed booking revenue × contribution margin ÷ spend. Margin per `reports/carrier-margin-resolved.md` with its limits attached. Never the platform's own conversion value |
| New-account vs existing-account split | Via `funeral_home_id` against first booking date (needs EA-45-01) |
| Unattributed share | Quotes with `lead_channel` = `agent_entered` or blank click fields, as a % of all quotes |

**Offline conversion import (later, Ethan's decision).** With `gclid` and booking revenue on the same row, the real booking can be uploaded to Google Ads so the bidder learns from bookings rather than form fills. This changes a live campaign and is approval-gated under `§7.1`; it is the reason the click ID is stored. Do not enable before the join has run for at least a month and been reconciled.

## Acceptance test (what "done" means)
1. Click a test ad URL with a `gclid`, submit a test quote, and see all nine fields on the stored quote.
2. Convert that test quote to a test booking and see `source_quote_id` filled on the EA-45-02 row.
3. Cookie survives navigation across at least three pages and an overnight gap.
4. The export contains none of the excluded columns. Header checked against this list.
5. Row counts: quotes exported vs quotes in the system, reported, with any difference explained.

## Why it is worth ranking
Ten working streams already depend on EA-45-02. This adds one column and nine fields to work being asked for anyway, and it is the only way to answer whether paid search pays for itself at a size where the answer is statistically readable (~35 leads a month). Without it the manual check is the only instrument and has to be repeated by a person.

**Rank suggestion:** directly behind EA-45-08, since it is meaningless without it. **Confidence:** high that the join works as drawn; low on build effort until engineering answers 1(a) and 1(b).
