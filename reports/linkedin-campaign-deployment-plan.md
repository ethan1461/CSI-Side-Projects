# LinkedIn campaign — deployment plan

**Date:** 2026-11-25 · **Requested by:** Ethan · **For:** Ethan to execute
**Status:** Plan. **Nothing has been created, spent, published or sent** (`CLAUDE.md`
§7.1 — activating a paid campaign, publishing content and spending money are all
approval-gated, and Ethan executes every one).
**Confidence:** High on structure and sequence. **`[ESTIMATE]` on every cost figure** —
LinkedIn rates vary by audience and season, and CSI has no LinkedIn history to calibrate
against. Treat the budget as a test size, not a forecast.

---

## Why LinkedIn, in one paragraph

**Google search cannot tell a funeral director from a grieving family, and that single
fact is what broke the last $4,117.** Fourteen of 21 identified leads were personal email
addresses; the conversion signal the bidder optimises toward is families filling in a form.

**On LinkedIn the targeting is the qualifier.** You select job title, industry and company,
and families do not appear in that set. The lead-gen form then captures name, company and
title natively — which is the exact gap that left 57 of 78 Google leads unidentifiable.
That is a structurally better-shaped channel for this business, not merely another one.

**The honest counterweight:** LinkedIn clicks cost several times Google's, and funeral
directors may simply not be there. This is an older, local, relationship-led profession.
**Step 1 settles that for free, before a dollar moves.**

---

## Stage 0 — four things before anything is built

**Three of these are gates, not preferences.** Do them in any order; all are free.

### 0.1 Confirm the audience exists `[20 minutes, free, no spend]`

In **LinkedIn Campaign Manager**, create an audience without creating a campaign, and read
the estimated size:

- **Job titles:** Funeral Director, Funeral Home Manager, Funeral Home Owner, Mortician,
  Embalmer, Funeral Service Manager, Director of Operations
- **Industry:** Funeral Services (LinkedIn has this as a standard industry)
- **Location:** United States
- **Seniority** as an alternative cut: Owner, Partner, Director, Manager

**The decision:** LinkedIn needs 300 members minimum to serve. For a test worth running you
want **5,000+**. Under about 2,000 and the channel does not exist for CSI at this targeting,
and the rest of this plan should be shelved rather than forced.

**Report the number back before Stage 1.** Everything downstream scales off it.

### 0.2 Build the matched audience from CSI's own data `[better than interest targeting]`

CSI already holds real funeral director contacts — the NFDA 2026 list and HubSpot. A
**Company or Contact matched audience** uploaded from that list beats title-targeting,
because it is people CSI knows exist rather than people LinkedIn guesses at.

Campaign Manager → **Audiences** → **Create audience** → **Upload a list** (company names or
contact emails). LinkedIn needs roughly 300 matches to activate it.

Use this for **Stage 2 retargeting and for a lookalike**, not as the only Stage 1 audience —
a matched list of current customers is exactly who you do *not* want to pay to reach, per
the finding that 3 of 4 matched Google leads were existing accounts. **Upload two lists:
customers (to exclude) and prospects (to target).** `revops-crm` can produce both.

### 0.3 Install the LinkedIn Insight Tag — this is the §9.2 gate

**`CLAUDE.md` §9.2: instrumentation precedes spend, and it is the one rule that may not be
waived for urgency. CSI has already spent a year of marketing budget it cannot account for.**

Campaign Manager → **Analyze** → **Insight Tag** → get the snippet → Kyri or Alex adds it
site-wide. Then define conversions for the quote page, the online-booking page and the
contact page.

**And connect LinkedIn Lead Gen Forms to HubSpot.** HubSpot has a native LinkedIn Ads
integration; once connected, a form fill creates a HubSpot contact with company and title
attached. **That is the loop Google never had.** Do not launch without it.

### 0.4 Clear the creative — and two items genuinely need it

Two checks, and the second is the one that could stop a video running.

**`§7.2` — decedent and family data.** The three Brian testimonials, especially
`03_CargoSalesChangesLifes`, need watching end to end before they run as paid ads. §7.2 is
absolute: no real decedent or family name in marketing material, ever, under any
circumstance. **Nobody should assume a video made in 2024 was cleared against a rule nobody
was applying then.**

**A signed release for Brian.** He appears to be a customer giving a testimonial. Using a
named individual's likeness in paid advertising needs his written consent. **Route to
`legal-risk` to confirm a release exists before the testimonial set runs.** If it does not,
the Disrupt Media hook videos still work and this is a delay, not a blocker.

**`§7.1` and `§7.3` — competitive and pricing claims.** `OverPayForTransport_CargoSales.mp4`
makes a competitive price claim by its title alone, and `NoBookingFee_CargoSales.mp4` makes a
pricing claim. Both are approval-gated externally. Note that **`CLAUDE.md` §4.2 records the
"Eagle's Wings charges ~10%" figure as an `[ASSUMPTION]` from four data points that "must
never be used externally."** If `OverPayForTransport` rests on that, it does not run until
TASK-0012's claims register substantiates it.

**"No booking fee" is different and it is safe:** it is a fact about CSI's own pricing, it is
CSI's strongest differentiator (`CLAUDE.md` §1), and it needs no comparison to stand up.

---

## Stage 1 — video views, to build an audience cheaply

**Do not start with lead generation.** At LinkedIn's cost per click, going straight for leads
means paying premium rates to reach people who have never heard of CSI. Video views are the
cheapest thing LinkedIn sells, and **everyone who watches becomes retargetable** — which is
what Stage 2 runs on.

| | |
|---|---|
| **Objective** | Video views (under Awareness) |
| **Audience** | From 0.1, minus the customer exclusion list from 0.2 |
| **Budget `[ESTIMATE]`** | $30/day, 3 weeks ≈ **$630** |
| **Format** | Single video, in-feed |
| **Success test** | Cost per view, and **25% / 50% / 75% completion rates** — completion is the real signal, not impressions |

### Creative, mapped to the files that exist

All in Google Drive. **Two are already in the right aspect ratios**, which matters more than
most people expect — LinkedIn's feed favours 4:5 and 1:1, and 16:9 wastes most of a phone
screen.

| File | Ratio | Use |
|---|---|---|
| `01_WorkingWithCargoSales_Brian_4x5.mp4` | **4:5 — ideal** | **Lead with this.** A real funeral director on how CSI works, in a profession that buys on relationship. Highest-trust format available |
| `02_RelationshipWithCargoSales_Brian_4x5.mp4` | **4:5 — ideal** | Second in rotation |
| `NoBookingFee_CargoSales.mp4` | check | **The strongest hook CSI has.** Safe on claims. Crop to 4:5 if it is 16:9 |
| `WeHaveASolution_CargoSales_9x16.mp4` | 9:16 | Works, though 4:5 outperforms 9:16 in the LinkedIn feed. Usable without re-editing |
| `ImpossiblePossible_CargoSales.mp4` | check | Hold as a fourth variant |
| `03_CargoSalesChangesLifes_Brian_4x5.mp4` | 4:5 | **Hold pending the §7.2 watch-through.** The title is the reason |
| `OverPayForTransport_CargoSales.mp4` | check | **Hold pending claim substantiation** (0.4) |
| `CargoSales_Promo_Rough_1_16x9.mp4` | 16:9, rough cut | Do not use. Rough cut, wrong ratio |

**Run three variants, not one.** LinkedIn needs creative variety to avoid fatigue in a small
audience, and three gives a readable comparison.

### Two production notes that decide whether video works at all

**Captions, burned in.** The large majority of LinkedIn video is watched with sound off. A
testimonial nobody can hear is a still image. If the files have no captions, that is a small
edit and it is not optional.

**The first three seconds carry it.** If the Brian videos open with a logo or a slow
establishing shot, re-cut so they open on him speaking. In-feed video competes against a
thumb, not against other ads.

**`§7.4` applies to every frame.** Warm, competent, unhurried. No urgency devices, no humour,
nothing that reads as growth marketing. **These run in a public feed, so grieving families
will see them** — that is the standard, not funeral directors alone.

---

## Stage 2 — lead generation, retargeting the viewers

Launch once Stage 1 has run two to three weeks and built a viewer pool.

| | |
|---|---|
| **Objective** | Lead generation |
| **Audience** | **Video viewers from Stage 1** (LinkedIn builds this automatically), plus the prospect matched audience from 0.2. Customers still excluded |
| **Budget `[ESTIMATE]`** | $40/day, 3 weeks ≈ **$840** |
| **Format** | **LinkedIn Lead Gen Form** — pre-filled from the profile, so it captures name, company, title and email with one tap |
| **Offer** | Not "contact us". Something worth a name — the corridor or country guide, a rate comparison for their lanes, or the shipping masterclass if the PFDA conversation lands |
| **Success test** | **Cost per lead where the company is a funeral home.** Not cost per lead |

**The form is the whole point.** It solves the identity problem natively: every lead arrives
with a company name attached, so the OMS check that took three weeks to arrange for Google
becomes a lookup that works from day one.

**Ask for as little as the form allows** — name, company, title, work email. Every extra
field costs completions, and company plus title is all that is needed to qualify.

---

## Budget, timeline and what decides it

| Week | Action | Spend `[ESTIMATE]` |
|---|---|---|
| 0 | Stage 0: audience check, matched lists, Insight Tag, HubSpot connection, creative clearance | **$0** |
| 1–3 | Stage 1 video views | ~$630 |
| 4–6 | Stage 2 lead gen, retargeting viewers | ~$840 |
| **Total** | **6 weeks** | **~$1,500** |

**Context for that number:** CSI's entire Google programme has cost $4,117 since August. A
$1,500 LinkedIn test is a real commitment at this company's scale and should be treated as
one — which is why Stage 0 is free and gates everything after it.

### The decision rule, set now rather than after the numbers arrive

Borrowed deliberately from `reports/paid-search-lead-conversion.md` §4, which worked.

| Result after 6 weeks | Action |
|---|---|
| Cost per **funeral-home** lead under ~$150, and leads are identifiable | **Scale.** Raise budget in steps, add a second audience cut |
| $150–$400 per funeral-home lead | **Hold** and improve the offer and creative before spending more |
| Over $400, or the leads are not funeral homes | **Stop.** Report the negative result. `§9.7` — a negative result is a result, and it frees budget |
| Audience under ~2,000 at Stage 0 | **Do not start.** The channel does not exist at this targeting |

**Break-even reference:** a booking contributes roughly $470–$550. So a funeral-home lead is
worth paying for if better than about one in three converts at $150 a lead — and unlike
Google, a LinkedIn lead arrives with a company name, so **that conversion rate is knowable
from the first week.**

---

## What this plan deliberately does not do

- **No outreach, no InMail, no connection requests.** `§7.1` gates sending any LinkedIn
  message to a real prospect. This is advertising only. Sponsored InMail is a separate
  decision and a separate risk.
- **No Coframe or landing-page testing yet.** At CSI's traffic volume an A/B test takes
  months to read. Revisit at ten times the traffic.
- **No claim about competitors** until TASK-0012's register substantiates one.
- **No new creative commissioned.** Everything in Stage 1 exists already. If the test works,
  that is when a production budget is worth discussing.

## Open items for Ethan

1. **Run 0.1 and report the audience size.** Everything else depends on it.
2. **Decide on the Brian testimonials** — is there a signed release? If not, `legal-risk`
   needs to say what is required.
3. **Watch `03_CargoSalesChangesLifes` end to end** against `§7.2` before it goes near an ad
   account.
4. **Ask Kyri or Alex for the Insight Tag install** — it belongs in this week's engineering
   note, and it is a snippet rather than a project.
5. **`revops-crm` produces two lists:** current customers to exclude, prospects to target.
