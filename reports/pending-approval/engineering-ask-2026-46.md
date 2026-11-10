# Engineering ask — to Kyri and Alex

**DRAFT for Ethan. Not sent (`CLAUDE.md §7.1`).** Rewritten 2026-11-09 to Ethan's direction: friendly and laid back, conscious of their capacity and the support-hours position, framed around *what it lets CSI do* rather than *what is broken*.

---

## Notes for Ethan — delete everything above "The note"

**What changed from the week-45 draft, all on your instruction:**

| | |
|---|---|
| **Removed** | EA-45-04 (booking duration) — gone entirely |
| **Rerouted to Donald** | Carrier invoice lines. He should be using the Airline Invoice Audit already |
| **Rerouted to Vadim** | International contracted rates. He has nothing the system doesn't, so he's first |
| **Rerouted to Cheryl + Vadim** | Where the weight allowance and overage terms actually live |
| **Reframed** | The booking file is now "build us the export button", not "run a job for us" |
| **Reframed** | Funeral home master joins the same export-capability bucket. **The admin bulk CSV does not work** — that's why Kyri sent you the file |
| **Rewritten** | EA-45-11 — anyone can add the funeral home, rather than a hard block at invoicing |
| **Added** | What the portal logs at event level |
| **Still the priority** | Margin visibility at carrier selection. Flagged for Vadim to work on with them |
| **Removed 2026-11-10** | The booking history cohort extract, previously item 1. Donald is sourcing it through Rednodo instead. Pulling it also stops the ask advertising that CSI is running churn and cohort analysis |

**The shape of the note, revised 2026-11-10.** The cohort extract is gone, so this is now three asks and one build. Shorter again, which is to the good. The remaining items are all system capability — which is the line Donald drew. The asks are grouped into one theme — *give us the export buttons and we'll run them ourselves* — then two questions, then the one build that matters. That reads as a smaller ask than ten numbered items, which is the point.

**On support hours:** the note acknowledges the 40-hour position without making a meal of it. It invites them to tell you what's chargeable before starting, which is what `§1.2` of the agreement review recommends.

---

## The note

**Subject:** A few asks — mostly export buttons so we can stop bugging you

Hey Kyri, Alex,

Hope you're both well. I've been going deep on our data over the last couple of weeks and I've got a batch of things I'd love your help with. Trying to send one list rather than pinging you every time something comes up — and I'd rather you tell me what's realistic than have me guess at it.

A lot of this is the same idea: **there's data in the system we can't get out of it, and every time we need it, someone has to ask you.** If we can get export buttons on a few things, that problem goes away permanently and you get your time back.

Ranked roughly by what helps us most. Happy to drop anything that doesn't fit.

---

### 1. Export buttons — so we can pull these ourselves

Rather than coming to you each time, could we get export functionality on a few places? We'd run these weekly on our own.

**a) Booking-level export.** One row per booking, from 2024 onward ideally. The columns we'd want:

- IDs and dates — `booking_id`, booking date, flight date
- The funeral home — shipping and receiving
- The route — origin, destination, country, domestic/international flag
- **The carrier** — this one matters most to us
- `awb`, rate type, revenue, carrier cost, accessorials
- Status, plus cancellation and rebooking flags
- Whether it came through the portal

**One hard requirement:** no decedent or family fields in the export — stripped at the query rather than removed afterwards. We don't want that data leaving the system at all.

**Why:** it's the file that turns monthly totals into lanes, corridors, accounts and carriers. It's also the only way to measure whether item 4 below actually works.

**b) Funeral home records.** The bulk CSV in the admin tools doesn't work — that's why Kyri kindly sent me the file directly. Could we get that as a working export? Same fields as the file he sent is perfect.

**c) Airline Invoice Audit.** Donald should be picking this up on his side, so this may already be covered — but if there's an export there, we'd like it.

Each of these could just be a download button on a screen you already have. If one is much easier than the others, start there.

---

### 2. Two questions, no build needed

**a) Are quotes stored anywhere we can query?**

The spec mentions saved quotes and the portal takes quote requests. Are those kept in a queryable form — price, lane, date — and linked to the booking they turn into?

**Why:** we can't currently compute a quote-to-booking rate, which means we can't tell which of our quotes win and which don't. And it's the missing link for working out whether our marketing spend is producing anything.

**b) What does the customer portal log at event level?**

Logins, quote requests, document uploads, bookings started versus completed — what's captured, and can we see it per funeral home?

**Why:** we want to know whether accounts that use the portal stay and grow more than accounts that don't. If they do, that's the business case for pushing adoption hard.

---

### 3. Rate table — a couple of odd ones

Three columns come through empty on every row of the published rates export: `included_weight`, `weight_unit` and `flat_overage_surcharge`.

It means a flat rate of, say, $1,545 doesn't tell us what weight it covers or what we'd charge beyond it — so for a heavy shipment we can't actually quote from the table. There are about 1,170 flat rates affected.

**Our question is narrow:** do those fields hold values in the system and the export is dropping them, or are they genuinely empty? I'm asking Cheryl and Vadim separately where those terms actually live, so this may turn out to be ours rather than yours.

Related and quick: when an agent prices a lane that has more than one rate row, does the quote tool pick one, and how? Some lanes carry both a casket rate and a lighter-weight rate, and we want to be sure the right one is being shown.

---

### 4. The one real build — showing margin when an agent picks a carrier

**This is the one I most want to talk through, and Vadim is going to work on it with you.**

The situation: on a lot of lanes two carriers both work, and the margin difference between them is significant. Vadim put together a list — on MIA-GUA we make $825 on Volaris and $375 on Avianca, and **the funeral home pays $1,450 either way**. Same price, same service.

And it's not a trade-off. On five of the six lanes he listed, **the better-margin carrier is also cheaper for the customer.** On SEA-LAX the better option is a direct flight while the worse one connects. We're currently losing margin, price competitiveness and service quality in the same decision.

Vadim has been giving this guidance verbally for years and it lives in his head. What we'd like is for it to be **on the screen at the moment the agent picks the carrier — the best-margin option highlighted and obvious**, with the customer price shown alongside it.

A few design notes from our side:

- **Never block.** The agent always overrides — space, known-shipper status, timing and customer requests all come first.
- **Highlight, don't just rank.** It needs to be obvious at a glance at 2am, not a column someone has to read.
- **Show both numbers.** On most of these lanes we're also cheaper, and that's the easiest version of this to explain to an agent.
- **Capture why, when they override.** One click — no space / not a known shipper / weight / timing / customer asked. That's how we'd finally measure how often the cheap option genuinely isn't available.

A static margin ranking per lane, from a table we maintain, displayed read-only, would be plenty to start. No live rate maths needed.

Vadim will reach out to work through the detail.

---

### Last thing, on scope

I know we've got the 40-hour monthly support arrangement and I don't want to blow through it without a conversation. **If any of this looks like a Change Order, or like it'd push the month over, just tell me before you start** and I'll sort it out on my end.

Equally, if some of it is half an hour of work, say so and we'll do those first.

Really appreciate you both — the funeral home file Kyri sent over last week has already unlocked a lot on our side.

Thanks,

Ethan
