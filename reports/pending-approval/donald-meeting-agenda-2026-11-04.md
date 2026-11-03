# Donald — Wednesday 2026-11-04, ~2:30pm

**Purpose:** get the four numbers that are currently blocking the most work, and settle two questions about data only he can answer.

**Run time:** ~55 minutes across five items. If you lose time, **items 1 and 2 are the ones that cannot slip** — everything else can go by email.

**Send ahead, the morning of:** nothing long. One line is enough: *"Five things, mostly about where numbers live rather than what they are. The first one's about carrier invoices and it's the one I most want your read on."*

---

## Before you walk in — three handling notes

1. **Do not lead with "$358,000."** Lead with **"every one of 77 shipments."** The pattern is solid and unarguable; the annual figure is an `[ESTIMATE]` extrapolated from two weeks on one carrier, and he will be right to push on it. If you open with the big number you spend the meeting defending an extrapolation instead of learning what the charges are.
2. **Item 3 is a question, not an accusation.** Vadim *believes* Donald enters the rate data. That is hearsay and Donald hasn't been asked. Multiple rate rows per lane are probably correct — our own analysis says they're casket versus lighter-weight. Ask, don't assert.
3. **Item 4 (concentration) is new information for him too, most likely.** It is not a problem to solve in this meeting. It is a fact to put on the table because it changes how a raise gets priced, and he owns that conversation.

---

## 1 · Carrier invoices above contracted rate — 15 min

**Your stated priority, and the only item here with real money attached today.**

**What we found.** Across the United invoices for September and October — about 85 air waybills — **every single one of the 77 we could match carried roughly $33 above the contracted rate** in miscellaneous charges and tax. Not most. All 77. That is about 4.4% of carrier cost on that sample.

**What you want out of it — one of three answers:**
- These are billed through to the funeral home, and here's where it shows up → *close it, stop worrying.*
- These are absorbed → *it's a real annual number and we size it properly.*
- Already built into the quoted rate → *fine, but then our margin figures are overstated by 4.4% and we should know that.*

**What to ask for:** the same cut for American, Delta and Southwest, so we know whether it is a United billing practice or an industry-wide one. That is the difference between a vendor conversation and a pricing conversation.

**Do not say:** that this is leakage, or that anyone has been missing it. We genuinely don't know which of the three it is.

---

## 2 · Secondary services — revenue and margin — 12 min

**The standing item, and still the biggest hole in the picture.**

Secondary services are **one of CSI's two revenue streams** (`CLAUDE.md §1`) — consulate support, pickup and drop-off, other ancillaries — and we currently have **no idea what they contribute or what they earn.** We don't estimate them, because guessing at half a revenue model is worse than admitting the gap.

**Ask for:** revenue and gross margin **by fee type**, FY2025 and FY2026 to date.

**Why it matters more than it sounds:** every margin number CSI quotes (~35% domestic, ~41% international) is **rate-card margin on the air freight only.** If secondary services are a materially different margin, the blended number everyone is working from is wrong — including anything that eventually goes to a lender.

**Concrete hook you now have:** the pickup line on a live quote we looked at this week was **$300**. One real data point to anchor the question.

---

## 3 · The rate table and the discount roster — 12 min

**Two questions, and the second one has money on it.**

### 3a. Does he enter the rate data?

Vadim thinks so. If yes:
- **Lanes carrying more than one rate row** — our read is these are a casket rate and a lighter-weight rate on the same lane, which would make them correct. Is that right?
- **`shipment_rate_type` is blank on all 6,919 published rows** but filled on contracted ones. Can he populate it, or does the screen not offer it?
- **`included_weight`, `weight_unit` and `flat_overage_surcharge` are blank on all 6,919 rows too.** This is the bigger one — it means a flat rate of $1,545 covers an unstated weight with an unstated overage charge, so **none of the 1,171 flat rates is quotable for a heavy shipment.** Does he enter these, or has he never seen those fields? *(If he's never seen them, it's an export or UI defect and goes to Kyri — which is our current read.)*
- **Confirm the Avianca/Volaris margins.** Vadim quoted MIA→GUA at $375 on Avianca and over $700 on Volaris. He owns margin; we'd rather have his numbers than Vadim's recollection before acting on it.

### 3b. The discount roster doesn't match — this is the new one

The OMS flags **17 funeral homes** as discount-eligible. Vadim's working rate sheet lists **16**. They do not agree:

| Account | Lifetime bookings | On Vadim's sheet | Flagged in OMS |
|---|---|---|---|
| **Las Rosas Funeral Home (Brooklyn)** | **673** | **Yes** | **No** |
| **Dunn & Sons Funeral Services (DC)** | **170** | **Yes** | **No** |
| Villa Americas Funeral Home (NJ) | 378 | No | Yes |
| Karen C. Funeral Services (DC) | 38 | No | Yes |

**Las Rosas is the 11th largest account CSI has.** Either they are being quoted off a discount the system doesn't know about — which is a control gap — or they should be getting one and aren't, which is a relationship risk on a 673-booking account. Both are worth ten minutes.

**Ask:** who maintains `is_discount_eligible`, how does an account get on it, and which list is authoritative when they disagree?

*(Also worth a mention: Meierhoffer Funeral Home appears twice, as a flagged record and an unflagged one. A duplicate pair where the discount flag differs — exactly the kind of thing to resolve before anyone merges records.)*

---

## 4 · Customer concentration — 8 min, informational

**New, from the funeral home records Kyri sent over this morning. He may not have seen it laid out this way.**

Of **18,876** funeral home records, only **2,536 have ever booked** and **1,756 have booked in the last twelve months.** That is the real customer base.

Within it, concentration is severe:

| | Share of lifetime bookings |
|---|---|
| **Top 10 accounts** | **31.3%** |
| Top 25 | 44.5% |
| Top 50 | 56.6% |
| Top 100 | 68.6% |

**The framing that matters, and get this right in the room:** the top four include **Bergen (NJ and FL), National Mortuary Shipping and International Mortuary Shipping** — about 17% of lifetime volume between them. Per `CLAUDE.md §5` Bergen and NMS are **partners as well as customers**, and that discount structure is deliberate. So this is **partner-channel concentration, not four customers who might churn next quarter** — a different and more defensible risk profile.

**It is still a diligence finding.** Any lender or buyer will price it. Better that Donald sees it now, from us, than in someone else's diligence memo. **No decision needed in this meeting** — just make sure he's seen it.

**One caveat to state out loud:** the booking counts in this file sum to 52,269, against roughly 43,600 bookings in OMS history. That doesn't reconcile yet — possibly the count includes cancellations, or counts both shipping and receiving homes. **The concentration shares are robust to that; the absolute numbers aren't.** Say so before he asks.

---

## 5 · Three data asks — 8 min, hand them over and move on

Don't discuss these. Hand over the list and ask which are easy.

| Ask | Why | Smallest version |
|---|---|---|
| **Marketing spend by channel by month**, FY25 and FY26 YTD | The only thing standing between CSI and knowing whether Google Ads works. Budget is being spent right now and not one dollar can be connected to a booking | Google Ads alone, monthly totals |
| **Fully-loaded cost per booking agent hour** | Cost to serve. **This has to come from him** — Vadim owns how long a booking takes, Donald owns what an hour costs, and the two should not be combined without him | A single blended figure |
| **QuickBooks sales-by-customer summary**, monthly, Jan 2024→. Customer totals only, no line detail, no memo fields | Account **revenue**. Kyri's file gives booking counts but not dollars, so this ask just got smaller — we need revenue per account, not the whole picture | FY2026 YTD only |

**Note the third one shrank because of Kyri's file.** Worth saying — it shows the asks are being pruned as data arrives, not stacked.

---

## What you're walking out with, if it goes well

1. Which of the three explanations the surcharge is.
2. A date for secondary-services revenue and margin by fee type.
3. Whether the rate table is his, and who owns the discount flag.
4. Donald having seen the concentration numbers.
5. Three data asks in his hands with a sense of which are cheap.

**If you only get two:** items 1 and 2.
