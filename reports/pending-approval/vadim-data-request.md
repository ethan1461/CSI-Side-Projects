# DRAFT — note to Vadim

**Status:** Draft for Ethan. Not sent. `CLAUDE.md §7.1`.
**Revised 2026-11-02** after Ethan corrected three premises in the first draft. Most of
what was here has moved to the Kyri/Alex engineering ask.

---

## Context for Ethan (delete before sending)

**What changed from the first draft, and why it matters beyond this note:**

1. **Permissions won't help.** I had assumed Vadim could grant access to contracted
   international rates because the Rate Tables page says they're "restricted to a smaller
   admin set." You don't have that access and neither does he — Kyri and Alex do. But you
   said Vadim holds the latest rate sheets themselves, with Susej and Kim able to fill
   gaps, so the ask becomes **send me the sheets**, not **grant me access**. That's item 2.
2. **The export buttons don't exist.** I had this wrong in both notes: Flight Confirmation,
   Ready to Invoice and Collect Shipments have **no export functionality**. So the
   booking-level export is a genuine build for Kyri and Alex, not a permission request.
3. **Time tracking is a Kyri/Alex question, not Vadim's.** You said it's something you're
   starting to be able to track but may not exist yet — that's about what the system
   captures, so it moves to the engineering ask.

**The knock-on, and it's the important bit:** the Week 45 plan assumed talking to Vadim
*might shrink* the engineering ask because an export button already existed. It doesn't.
The ask is now larger and more certain, and the Friday test — one prioritized ask leaving
the building — matters more, not less. I've told the orchestrator.

**What's left for Vadim is question 1, and it's still the one worth his time.** If the desk
prices from experience rather than the table, cleaning 133 rows drops down the queue and
capturing what's in their heads rises to the top.

---

## The note

Hey Vadim,

Two things, and the first is the one I most want your read on.

### 1. How do the booking agents actually pick a route?

This is the one I most want your read on, given the discussion we had at NFDA where this
continues to be an issue.

Going through the last rate export, I found **133 routes that have two different prices on
them** — same airline, same origin, same destination, same rate type, two numbers, and
nothing indicating which one applies. For example American, West zone to West zone shows up
three times at $207.19, $615.94, and $207.19.

Before I ask anyone to fix the data, I want to understand how much it actually matters:

- When an agent builds a booking, are they pricing off the rate table, or off their own
  knowledge of which carrier handles our shipments well on that lane? Is there like a cheat
  sheet, or a go-to carrier per route that lives outside the system?
- What do they do when the system gives them two numbers?

If the table gives two answers, that's on the data, not on them. I'm asking because if
they're mostly working from experience rather than the table, then cleaning the table is a
lower priority than I thought, and what we should actually be doing is getting that
experience written down.

### 2. The latest rate sheets

Separately — can you send me the most current rate sheets you're working from, particularly
the international ones?

What we have loaded covers American, Delta, United and Southwest — 156 lanes with a cost
against them. There's nothing for any international carrier: IAG alone is over 5,500 lanes
where we can see what we charge but not what we pay. International is where we make our
best margin and it's the half of the book I can't see.

If some of it lives in your sheets rather than the system, that's useful to know too —
I'd rather work from what you actually use than from what got loaded. And if there are
gaps, I can check with Susej and Kim.

Thanks — question 1 especially.

Ethan

---

## Notes for Ethan (delete before sending)

- **Question 1 is the prize.** If the answer is "experience, not the table," the engineering
  queue reorders and the real asset is institutional knowledge that currently has no
  written form and no backup.
- **Item 2 is probably the fastest unblock available this week.** Vadim's own sheets would
  give pricing and corpdev the international cost side without anyone building anything —
  worth more than the booking export in the short run, and free.
- **Don't let the NFDA framing turn into a complaint about his team.** They're choosing
  under genuine ambiguity. The note says so twice on purpose.
- Everything else from the earlier draft — the booking-level export, time tracking, and
  the contracted-rate permission — is now in the Kyri/Alex ask.
