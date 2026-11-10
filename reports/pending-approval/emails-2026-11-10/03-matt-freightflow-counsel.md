# DRAFT — to Matt, on the FreightFlow agreement

**Status:** Draft for Ethan. Not sent (`CLAUDE.md §7.1`).
**Companion:** §2 below is how to raise this with the exec team. That is not part of the email.

---

## Notes for Ethan — delete before sending

**Why the email is short and the report is attached.** Counsel bills for reading. Twelve questions
in an email body invites a twelve-question answer at twelve-question cost. The email gives him the
three gaps and asks for a scoping call; the ranked brief is in the attachment for when he is
actually engaged.

**The one thing that will stop him cold:** our copy is **unsigned, with a blank Effective Date.**
He will ask for the executed version in his first reply. Better that you raise it than he does —
the draft says so up front, and finding it is on the internal list either way.

**Check before you attach (`§7.2`).** The agreement itself contains no decedent or family data,
and neither does the gaps report. That has been verified. If you attach anything else, it gets
checked first.

**Scope it deliberately.** Items 1–6 of the brief are the engagement. Items 7–12 can follow once
you know what the first six cost. Saying that in the email is what keeps this from becoming an
open-ended matter.

**On tone:** he is a former attorney of CSI's and already helping on the privacy side. This reads
as picking something back up, not as a cold instruction.

---

## The note

**Subject:** Our software development agreement — would you take a look?

Hi Matt,

Thanks again for connecting me with your colleague on the privacy side — I'll follow up on that
separately.

Something else I'd value your eyes on, and it's more substantive.

We've been doing a careful internal read of our Software Development and Support Agreement — the
one covering the platform our whole operation runs on: bookings, rates, the customer portal. Not
because anything has gone wrong. More the opposite: the business now depends on that system
completely, and I realised nobody had looked at the paper in a while to ask what we'd find if the
relationship ever changed.

Three things came out of it that I'd like a lawyer's view on.

**1. It isn't clear we own our own data.** No clause establishes that CSI owns what the system
holds, and the definition of our materials appears narrow enough to exclude anything the developer
built. There's also no export right during the term — the only delivery obligation runs for up to
40 days *after* exit, on "commercially reasonable efforts." Meanwhile there's a clause requiring
them to delete our data and certify it, and I can't tell how those two sequence.

**2. There's no security or breach-notification obligation at all.** The only data term is a
general duty to comply with privacy law. No security standard, no breach notice, no audit right,
no backup duty — and the agreement actively disclaims that the work will be secure. Our systems
hold decedent and family information from the people we serve. That's the part I'd most like to be
told I'm reading wrong.

**3. No source-code escrow, and continuity is thin.** The word doesn't appear. Our licence to the
developer's own underlying components has no stated term, and two clauses seem to contradict each
other on whether it survives termination. Hosting, domain and credential control aren't addressed.
And on my reading we'd still owe the remaining fee installments even if they walked.

I've attached our internal write-up. It has a ranked list of questions, with the clause references,
so you're not hunting through 46 pages.

**Two practical notes.** First, the copy I have is **unsigned with a blank effective date** — I'm
locating the executed version and will send it as soon as I have it, along with the change orders.
Second, I'd like to **scope this** rather than open it up: the first six questions are the ones
that matter now, and the rest can wait until we know what those cost.

Would you have 20–30 minutes in the next couple of weeks for a scoping call? And if this isn't your
area, I'd rather you point me at the right person than stretch.

Thanks Matt,

Ethan

---

# §2 — How to raise this with the exec team

**Not part of the email.** Notes for Ethan.

## The framing that works

**Lead with the paper, not with the trigger.** This review was prompted partly by a concern Donald
raised about how widely one vendor is engaged. **Do not open with that.** The moment the
conversation is about a person, the findings become a position in an argument and stop being read
as facts. They are not a position — every one of these gaps would be in the document whoever the
counterparty was.

The opening line that does the work:

> *"The business now runs entirely on a platform we don't own outright, and nobody has read the
> contract against the question of what happens if that relationship changes. I had it read. Three
> things need fixing, and none of them are about anyone's conduct."*

That is true, it is uncontroversial, and it is very hard to argue with.

## What lands with whom

| | What they will care about | Lead with |
|---|---|---|
| **Cheryl (CEO)** | Reputation and the families CSI serves | **Gap 2.** CSI's own standard treats decedent data as the strictest line in the business. The contract covering the system that holds it imposes essentially nothing. That is the gap between what CSI promises and what it has secured |
| **Donald (Finance/ownership)** | Money and downside | The **liability cap** — possibly below $75K — against an unbounded data exposure, plus up to **$225K** still owed if the vendor exits. He is already primed; he needs the numbers, not persuasion |
| **Vadim (COO)** | Continuity | **Gap 3.** No escrow, no transition assistance obligation, no clarity on who holds hosting and credentials. If access lapsed on a Tuesday, what happens Wednesday? He is the one who would find out |

## What to actually ask them for

Three things, all small, none of which require agreeing on a diagnosis:

1. **Authorize a scoped counsel engagement** — the first six questions only, with a cost ceiling.
   Easy yes. It buys information rather than committing to anything.
2. **Find the executed copy.** You and Donald. Everything else is provisional until it exists, and
   it is embarrassing-but-common that nobody can immediately lay hands on it.
3. **Commission a control inventory** — who actually holds the repository, hosting, domain,
   production database and airline API credentials. This is a question for Kyri and Alex, asked
   straightforwardly as a question, and it is the single most useful fact in the whole picture.
   It costs nothing and it is not accusatory: any company should know this.

## What not to do in that room

- **Don't bring NFDA into it.** If the conversation turns to what anyone may or may not be doing
  commercially, the three gaps will not get decided. Keep them separate; they are separate.
- **Don't propose approaching the vendor.** Counsel first. `§7.5` and plain sense both.
- **Don't present the gaps as findings against anyone.** They are findings against a document, and
  documents do not have feelings or lawyers in the room.
- **Don't ask the exec team to adjudicate the legal questions.** They are not lawyers. Ask for the
  budget and the two internal actions; let counsel answer the rest.

## The tone to hold — Ethan's instruction, 2026-11-10

**Do not present any of this as assuming bad faith**, and say so explicitly rather than leaving it
to be inferred. Ethan's position, which the evidence supports: he does not expect the counterparty
to act badly, and the case does not rest on it.

Every one of these gaps bites in scenarios where **everybody behaves well throughout** — the vendor
is acquired and the people change, a key person leaves, a receiver is appointed, or a breach occurs
and no one is *required* to tell CSI however much they want to.

**And the strongest argument involves no falling-out at all.** CSI is pursuing acquisitions and a
capital raise. Any buyer or lender will ask whether CSI owns the data in its own operating system.
"No clause says so" is a valuation discount or an escrow holdback — payable today, against a vendor
relationship that is working fine. That is a forward-looking commercial reason to fix the paper,
and it is the one to lead with in front of Donald in particular.

The line to use if anyone hears an accusation in it:

> *"None of this assumes anyone does anything wrong. Most of it bites hardest when everyone behaves
> perfectly and something outside the relationship changes — and the ownership question costs us in
> a raise whatever happens."*

---

## The honest caveat to say out loud

Every finding rests on an **unsigned copy**. Say that before someone else notices it. It does not
change the direction of any of this — an unsigned draft and its executed version rarely differ on
whether escrow exists — but stating the limit yourself is what makes the rest credible.
