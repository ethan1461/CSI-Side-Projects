# The search terms report, measured

**Date:** 2026-11-25 · **Source:** Google Ads search terms export, 1 Sep – 24 Nov 2026,
supplied by Ethan · **Script:** `scripts/analyze_search_terms.py`
**Replaces the estimate table** in `reports/paid-search-negative-keywords.md` §6, which said
it should be replaced the moment this export existed.
**Confidence:** High on every figure here; they are sums over the export.

---

## The answer

**Three findings, and they reorder the whole paid-search to-do list.**

1. **Tier A negative keywords do almost nothing. 3 terms, 3 clicks, $10.21 — 0.3% of
   total spend.** The §6 scenarios modelled 15%, 30% and 45% of clicks blocked. The
   measured figure is **1.9% of visible clicks and 0.3% of all spend.** Apply the list
   anyway, because it costs nothing and stops future drift, but it is not a lever.
2. **88% of spend has no visible query**, so no negative keyword can reach it. This is
   the real wall and it is not the one anyone was working on.
3. **CSI is appearing on its own partners' brand names.** Around **$54** of spend on
   searches for International Mortuary Shipping and National Mortuary Shipping. The money
   is trivial; the relationship exposure is not. **This is the one thing to act on today.**

---

## 1. Where the money actually went

| | Clicks | Cost | Conversions |
|---|---|---|---|
| **Total: Campaign** (Google's own figure) | 2,290 | **$3,305.40** | 129.0 |
| of which itemised as named queries | 162 | $400.80 | 19.5 |
| of which **"Other search terms"** — Google will not disclose them | 758 | **$1,811.25** | 51.5 |
| **unexplained remainder** | **1,370** | **$1,093.35** | 58.0 |

**Only 12% of spend is attached to a query anyone can read.** 55% sits in "Other search
terms", which Google withholds below its disclosure threshold. The remaining 33% does not
appear in a search terms report at all — most likely Performance Max, which does not report
queries this way.

**That is the finding that matters for method.** The negative-keyword workstream, the Tier A
and Tier B lists, the match-type review — all of it operates on the 12%. It cannot be made
to work on the rest, however well it is done. `§9.2` says instrumentation precedes spend,
and this is what the absence of instrumentation looks like from the inside: the account
will not tell you what you bought.

## 2. Tier A, measured

| | Terms | Clicks | Cost | Conversions |
|---|---|---|---|---|
| All itemised queries | 702 | 162 | $400.82 | 19.5 |
| **Tier A would block** | **3** | **3** | **$10.21** | **0.0** |
| Kept | 699 | 159 | $390.61 | 19.5 |

Two rules fired at all: `yourself` (2 clicks, $5.72) and `pet` (1 click, $4.49). Not one of
the 52 phrase-match family terms — "my mother", "my husband", "fly with ashes" — appears in
a single visible query.

**s = 0.019. ρ = 0.00.** Those are the two parameters §6 could not observe, and against
visible spend they make the list a rounding error.

**Do not read this as "families are not clicking."** Fourteen of the 21 identified HubSpot
leads were personal email addresses, so families plainly are. It means **they are arriving
through queries Google is not showing us** — which is the §1 finding again, from the other
direction.

## 3. The partner-brand problem

Visible spend on searches for CSI's own partner tier:

| Query | Clicks | Cost | Conversions |
|---|---|---|---|
| international mortuary shipping | 10 | $21.77 | 0.0 |
| national mortuary shipping and cremation | 2 | $14.00 | 2.0 |
| national mortuary services | 2 | $10.31 | 0.0 |
| national mortuary | 1 | $7.89 | 0.0 |
| **Total** | **15** | **~$53.97** | **2.0** |

**International Mortuary Shipping and National Mortuary Shipping are partner tier**
(`CLAUDE.md` §7.1, standing authority 1). NMS is among CSI's largest partners *and* largest
customers, buys at roughly 22% margin as a deliberate alliance structure, and Ethan has
named deepening these relationships a top priority (`CLAUDE.md` §5).

**So CSI is spending money to appear in front of people searching for a company that is
simultaneously its ally, its customer and its supplier.** If anyone at NMS or IMS searches
their own firm and sees a CSI ad, that is a conversation nobody wants, over $54.

### This is a disagreement with the earlier report, stated rather than quietly reversed

`reports/paid-search-negative-keywords.md` §4 lists competitor names — explicitly including
National Mortuary Shipping and Bergen — as **"Not blocked,"** reasoning that *"a director
comparing carriers is a prospect."*

**That reasoning is sound for a competitor and wrong for a partner,** and the earlier
analysis did not weigh the alliance against the prospect. On a true competitor — Inman,
Eagle's Wings, ILS — I agree with it entirely and would not block. On the partner tier the
risk and the reward are not close: at most a couple of conversions a quarter against a
relationship Ethan has ranked a top priority.

**Recommendation: add the partner-tier brand names as negatives.** Bergen, National
Mortuary Shipping, International Mortuary Shipping, Las Rosas and their obvious variants.
Leave genuine competitors alone. `§7.1` — a campaign change, so Ethan executes.

## 4. Brand terms: the best-converting thing visible, and don't touch them

| | Terms | Clicks | Cost | Conversions | Cost/conv |
|---|---|---|---|---|---|
| CSI brand | 4 | 48 | $78.71 | **5.0** | **$15.74** |
| All visible queries | 702 | 162 | $400.82 | 19.5 | $20.03 |

Brand is **19.6% of visible cost and 26% of visible conversions**, at a cost per conversion
a quarter better than the account average.

**I suggested earlier today that brand terms might be the existing-customer leak. On this
data that was wrong, and the honest position is more awkward than either version:** brand
converts *because* those searchers already intended to contact CSI. The conversions are
real and they are probably not incremental — which is the classic brand-bidding question,
unanswerable without a holdout test.

At **$78.71 across 85 days — about 93 cents a day — it is too small to be worth the
argument.** Leave it. Spend the attention on §1 and §3.

## 5. What the visible queries do show

The queries that are there read like the business CSI wants: *funeral homes that transport
bodies to mexico near me*, *repatriación latina*, *international funeral services*,
*transferring dead body to another country cost*, *traslado de cenizas a cuba*,
*international funeral service new jersey perth amboy*. Spanish-language queries appear
repeatedly and convert.

**Three of the top twenty are family price-shopping** — "how much does it cost to transport
a dead body from one state to a[nother]", "transferring dead body to another country cost",
"traslado de cenizas a cuba". That is Tier B territory, not Tier A, and §4 of the
negative-keywords report was right to hold Tier B pending exactly this export. **On this
evidence Tier B is worth revisiting**, since the price-shopping pattern is visible and
Tier A's family phrasing is not.

## 6. Revised priority order

| | Action | Who | Effect |
|---|---|---|---|
| **1** | **Block partner-tier brand names.** Bergen, NMS, IMS, Las Rosas | Ethan, campaign change | Removes a relationship risk for ~$54 of spend. No downside |
| **2** | **Find out what the 33% unexplained spend is.** If Performance Max, it reports no queries and that is a structural decision, not an optimisation | Ethan, read-only | Determines whether 88% of spend is knowable at all |
| 3 | Revisit **Tier B** against this export | marketing-lead, then Ethan applies | The price-shopping pattern is visible; the Tier A pattern is not |
| 4 | Apply **Tier A** | Ethan | 0.3% of spend. Do it because it is free, not because it matters |
| 5 | Leave brand terms alone | — | Best-converting visible segment, 93 cents a day |
| — | ~~Customer-match exclusion audience~~ | — | **Deprioritised.** The existing customers most likely arrived on brand terms, which §4 says to leave. Revisit only if §2 shows generic-term spend reaching them |

**And the standing conclusion is unchanged, now with a measured basis:** until a query can
be tied to a call and a call to a booking, this account cannot be optimised, only guessed
at. That is DNI and a lead-source field, and nothing in this export changes it.
