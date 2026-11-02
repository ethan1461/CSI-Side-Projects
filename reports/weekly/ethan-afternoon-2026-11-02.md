# This afternoon — a 2h45 plan

**Built:** Monday 2026-11-02. Companion to `reports/weekly/ethan-todo-2026-11-03.md` (tomorrow's list).

**Revised** after Ethan: all four emails go out this afternoon or tonight, not tomorrow.
**He is right and my Wednesday hold on Kyri and Alex was over-cautious** — today is
Monday, so tonight is on-cadence for the standing Monday ask, and Part 4 of that format
exists precisely so struck items can return in a later week without it reading as
ad-hoc. Holding would have cost two days on the three highest-value items to avoid an
outcome the format already handles.

**The shape:** 10 minutes of clicking that must happen *before* the emails, 40 minutes of
sending, 15 minutes of the rest of the clicking, **95 minutes of actual thinking on the
one question nobody can answer for you**, 10 minutes to close out.

---

## Block 0 · 0:00–0:10 · Two clicks that change what you send

Do these first — one of them changes the Kyri/Alex email.

- [ ] **Click the Funeral Home Records bulk CSV export** in the admin tools. Documented but never verified. **If it works and carries the EA-45-03 fields, edit that item to "this works — who runs it, and how often?" before sending.** If it doesn't, send as written. Either way it stays in the list.
- [ ] **Decide on the security officer.** The nightly export is the first scheduled data flow out of the OMS since they declined agent access. It is not agent access — it's a PII-stripped file into a CSI-owned Drive folder — but they should hear it from you, not from Kyri. Doesn't block sending.

---

## Block 1 · 0:10–0:50 · Send all four

All drafted in `reports/pending-approval/emails-2026-11-02/`. Read, cut the "Notes for
Ethan" block at the top of each, send.

| Order | To | Why this order | Your decision in it |
|---|---|---|---|
| 1 | **Vadim** (`01-vadim.md`) | The lane list is the highest-return ask open anywhere in the program, and he's warm right now | Whether to quote his own $375/$700 back to him before Donald confirms it. Cut that paragraph if not — the ask works without it |
| 2 | **Donald** (`02-donald.md`) | Sets next week's agenda. He prefers to talk first, so it's a short note, not a data request | None in the draft. But **in the room, don't lead with "$358,000."** Lead with "every one of 77 shipments." The pattern is solid; the annual figure is an extrapolation and he'll be right to push |
| 3 | **Arty** (`03-arty.md`) | Meeting is this week, and four of its questions gate the valuation work | **Whether to tell him you're exploring a raise.** One sentence, marked optional. A real call — it's a confidence, and every question stands without it |
| 4 | **Kyri and Alex** (`04-kyri-alex.md`) | Goes last so the three internal answers are already in flight when they read it | Covered in Block 0 |

**One edit I made because this now goes out before Donald replies.** The ask told Kyri and
Alex, in the body, that *Donald* enters the rate data and two items were therefore his.
Vadim hedged — "I *believe* Donald is in charge" — and nobody has asked Donald yet.
Naming a colleague to an outside vendor as responsible for a defect, on an unconfirmed
belief, before he can answer, isn't something to put in writing. Every mention in the sent
text now reads **"maintained on our side."** Same message, no name attached to a defect.
Donald's name stays in the internal notes you delete.

---

## Block 2 · 0:50–1:05 · Three clicks that unblock three agents

- [ ] **Provision Otto and Stacy as HubSpot users** (and Jeff if he'll own records). 3,553 of 3,574 contacts have no owner and ownership can't be assigned to non-users. **The hard blocker on the highest-value CRM fix.**
- [ ] **Export all contacts from HubSpot** to `data/raw/` — Record ID, first, last, email, domain, phone, company, state, record source, create date. *Or* just read the number on Contacts → Actions → Manage duplicates and tell me. Duplicate volume can't be sized through the connector at all.
- [ ] **Two questions only you can answer:** which saved view was the "58" (closes the C16 attribution gap), and what was the 2023 bulk import of 2,283 contacts (the lead source for 64% of the database).

---

## Block 3 · 1:05–2:40 · The question only you can answer

**Put the phone away for this one.** Everything above is execution. This is the thing the
whole team is currently guessing at.

### The question

**KR3.1's monthly bookings target is blank, because CSI has never set one.** I won't invent
it — a number I make up becomes a number quoted in a board deck. But this week turned it
into a harder and more interesting question than "pick a target," and I think that's the
conversation worth 95 minutes.

### Why it got harder

The diagnosis in `CLAUDE.md §2` is that CSI is growing on yield, not volume: **revenue
+4.4% on bookings +1.3%** for Jan–Aug 2026. The stated job is to convert that into
volume-led growth without giving back the yield.

Then Vadim's reply landed. On MIA→GUA, picking the right carrier is worth **$325+ per
shipment at an identical customer price.** If ten lanes look like that, the margin
available from *how CSI books existing volume* may rival or exceed the margin from new
volume — and it requires no new customers, no acquisition cost, and no price increase a
funeral director could object to.

**So there are two different growth engines competing for the same attention, and they
imply different companies:**

| | Volume-led | Margin-led |
|---|---|---|
| What you buy | New funeral homes, new corridors, acquisitions | Better decisions on shipments you already have |
| What it costs | Sales headcount, marketing spend, deal capital | Tooling, and Vadim's time |
| How fast | Quarters to years | Weeks, if the lane list is real |
| What it needs from you | Capital — Priority 1 | A screen in the OMS and a ranked lane list |
| Risk | CAC is currently unmeasurable | The leak may be small outside the lanes Vadim remembers |
| Enterprise value effect | Grows the numerator | Grows the multiple — margin quality is what a buyer pays up for |

### What to decide, in order

1. **Is FY27 a volume year or a margin year?** Or explicitly both, with a split — and if
   both, which one yields when they compete for Vadim's and Kyri's time, because they
   will.
2. **Then set the bookings number.** Three anchors, all traceable: 2025 closed at 10,985;
   Jan–Aug 2026 is +1.3% on volume; the first year above 3% revenue growth in the series
   is the one now in progress. A volume-led FY27 probably means a number with a 3 or 4 in
   front of it on growth, which is roughly 915–950 bookings a month against a current
   run-rate near 930. **Say which it is and I'll build the plan behind it.**
3. **What's the capital actually for?** If FY27 is margin-led, the raise funds
   acquisitions. If volume-led, it funds a sales engine. The valuation work starts this
   week either way and the narrative differs materially.

### What to write down

Three or four sentences is enough. *"FY27 is [X]-led. The bookings target is [N] a month.
Capital is for [Y]. When Vadim's time is contested, [Z] wins."* That unblocks the OKRs,
the valuation, the engineering ranking and the week-46 plan — all of which are currently
waiting on it.

### If you'd rather not decide today

Legitimate — **the one input that would most improve this decision is Vadim's lane list**,
and you'll have it within a day or two of Block 1. If you'd rather wait for it, say so and
I'll hold the OKRs rather than publish them half-blank. **Don't split the difference by
approving OKRs with a made-up number in them.**

---

## Block 4 · 2:40–2:50 · Close out the cheap rulings

Fast calls, no analysis needed. Each is blocking something small.

- [ ] **C10** — years in business. One number.
- [ ] **C12** — HubSpot or spreadsheets as the CRM of record. `revops-crm` recommends you rule *after* the cleanup runs, so **"decide Nov 17" is a valid answer** and probably the right one.
- [ ] **Open questions #1 and #25** — DNS cutover status, GA4 status.
- [ ] **Three brain proposals** — the Donald surcharge priority; Kyri is a contractor not CTO; carrier selection as an unmanaged margin decision. All three are evidenced; approving them makes them binding on every agent.
- [ ] **The 202 partner outreach drafts** — I recommend hold. They say "about 12,000 loved ones a year" against 10,985 actual. A 9% overstatement in writing to partners.
- [ ] **The booking-team routing note** — I've already put it on hold; Vadim's reply killed two of its three premises. Confirm, or tell me to send it anyway.

---

## What I'll do while you're in Block 3

Nothing that needs you. If the HubSpot contact export from Block 2 lands, `revops-crm`
can size the duplicates and have the merge brief ready before Wednesday's cleanup —
that's the one thing in Block 2 with a same-day payoff.
