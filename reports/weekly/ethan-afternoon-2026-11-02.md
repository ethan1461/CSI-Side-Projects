# This afternoon — a 2h45 plan

**Built:** Monday 2026-11-02. Companion to `reports/weekly/ethan-todo-2026-11-03.md` (tomorrow's list).

**The shape:** 35 minutes of sending, 25 minutes of clicking, **95 minutes of actual
thinking on the one question nobody can answer for you**, 15 minutes to close out.

The first two blocks are deliberately front-loaded and mechanical. They unblock four
colleagues and three agents, and they're the kind of work that expands to fill whatever
time you give it — so they get a box and a clock.

---

## Block 1 · 0:00–0:35 · Send three emails

All four are drafted in `reports/pending-approval/emails-2026-11-02/`. Read, cut the
"Notes for Ethan" block at the top of each, send.

| Order | To | Why this order | Your decision in it |
|---|---|---|---|
| 1 | **Vadim** (`01-vadim.md`) | The lane list is the highest-return ask open anywhere in the program, and he's warm right now | Whether to quote his own $375/$700 back to him before Donald confirms it. Cut that paragraph if not — the ask works without it |
| 2 | **Donald** (`02-donald.md`) | Sets the agenda for next week. He prefers to talk first, so this is a short note, not a data request | None, but **don't lead with "$358,000" in the room.** Lead with "every one of 77 shipments." The pattern is solid; the annual figure is an extrapolation and he'll be right to push |
| 3 | **Arty** (`03-arty.md`) | Meeting is this week, and four of its questions gate the valuation work | **Whether to tell him you're exploring a raise.** One sentence, marked optional in the draft. Real decision — it's a confidence, and the questions all stand without it |

**Not today: Kyri and Alex** (`04-kyri-alex.md`). The ask is ready but two items were
struck this morning on Vadim's word that Donald enters the rate data. If Donald says
otherwise they come back, and revising that list twice in one week is the exact pattern
the weekly rhythm exists to kill. **Wednesday, after Donald.**

---

## Block 2 · 0:35–1:00 · Five clicks that unblock three agents

None of these needs thought. All five are blocking work that is otherwise idle.

- [ ] **Provision Otto and Stacy as HubSpot users** (and Jeff if he'll own records). 3,553 of 3,574 contacts have no owner and ownership can't be assigned to non-users. **This is the hard blocker on the highest-value CRM fix.**
- [ ] **Export all contacts from HubSpot** to `data/raw/` — Record ID, first, last, email, domain, phone, company, state, record source, create date. *Or* just read the number on Contacts → Actions → Manage duplicates and tell me. Duplicate volume can't be sized through the connector at all.
- [ ] **Click the Funeral Home Records bulk CSV export** in the admin tools. If it works, an item drops out of Wednesday's engineering ask.
- [ ] **Which saved view or list was the "58"?** Closes the C16 attribution gap.
- [ ] **What was the 2023 bulk import of 2,283 contacts?** It's the lead source for 64% of the database.

---

## Block 3 · 1:00–2:35 · The question only you can answer

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

## Block 4 · 2:35–2:50 · Close out the cheap rulings

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
