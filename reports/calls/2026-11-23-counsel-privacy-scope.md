# Call pack — Matthew Glick & Greg Testa, counsel
**Monday 23 November 2026, 12:30–1:30 EST · with Donald**
**Subject as invited:** CSI Privacy Policy and Guidance Scope

---

## The one-sentence version

Funeral homes send us passports, death certificates and consular paperwork; **we already
accept those uploads on our public website today and cannot say who can reach them, where
they end up, or how long they are kept** — and we want to put the same capability in the
customer portal, properly.

Alex and Kyri, our engineers, flagged this rather than quietly building on top of it.

---

## What we want to leave the call with

1. **Agreement on scope**, and whether it is one engagement or phased.
2. **A view on whether anything needs changing now**, ahead of the new feature — the
   existing upload path is live.
3. **Fee shape.** We would prefer a fixed fee for a defined written memo over open-ended
   hourly review. Say this early.
4. **What they need from us**, and by when.

---

## Part 1 — The facts they need

**The company.** Air transport and logistics broker for human remains. 23 years, Miami.
~11,000 shipments a year. **Customers are funeral homes and funeral home groups — never
consumers.** Sister company Southern Cross Trading under common ownership holds certain
operating certifications.

**The documents.** International shipments require paperwork supplied by the funeral home:

- Passports and cancelled passport bio-data pages of the deceased
- Death certificates
- Letters of non-contagious disease from a health authority
- Permits to transport or dispose of remains
- Embalming certificates
- Consular and apostille paperwork

These carry decedent identity data and, in many cases, **living family members' names and
contact details.** That second part is the one that tends to get missed.

**What runs today.** The public website accepts document uploads. Legacy code saves the
files on the ERP server, records filenames, and **emails them to a shared operational
mailbox.** We have not confirmed the deployed configuration, who can access stored files,
or how retention and deletion work across server, email and backups. Our hosting provider
would need to be involved to establish that.

**What is proposed.** Document upload in the customer portal, stored in **AWS S3**, reachable
from the portal and the ERP, so agents retrieve documents from the system rather than from
email.

---

## Part 2 — The agenda, in the order I would take it

**Lead with what is already running, not the new feature.** The live exposure is the
existing path; the portal is the thing we can still hold.

**1. The existing process — does it meet our obligations, and what needs changing now?**
Interim fixes ahead of any new build.

**2. Authority and access.** What authority does a funeral home need to send us these
documents, and who inside CSI should be able to view, download or share them?

**3. Our notices and agreements.** Do our privacy policy, website terms and funeral home
customer agreements actually cover passports, death certificates and consular paperwork?
We can supply all three. **Nobody has read them for this purpose.**

**4. HIPAA.** Does it reach any of our relationships or services, and if so what follows?

**5. Retention, deletion and incident response.** How long per document type, how deletion
works across backups, and what happens if something is accessed or disclosed improperly.

**6. Cross-border.** Mexico, Dominican Republic, Guatemala, El Salvador, the Caribbean,
Europe, Africa, Asia. What this adds.

**7. Disclosure to outside parties.** Separate from the feature and increasingly live: our
operational exports carry decedent and family data by design, so **today we could not hand
records to an adviser, lender or prospective buyer even if we wanted to.** What are our
obligations, and what would make it possible safely?

---

## Part 3 — What has changed since the brief was written on 3 November

**Raise these. They were not in the brief and they widen the question.**

**New outbound data flows, both involving decedent names leaving our systems:**

- **Flight-status alert emails.** A new system emails the funeral home when a flight slips.
  The email contains **the decedent's name**, the booking and the AWB. Today an agent sends
  it. **Donald has asked whether the system should send it automatically**, without an agent
  in the loop. That turns on whether we hold the right contact for the right person, and we
  know that contact data is uneven. **This is a live decision waiting on an answer.**
- **Portal tracking emails.** Approved and about to start. After a booking confirms, the
  customer gets a link to track and manage it in the portal.

**New third parties:**

- **Rowland Brothers (UK).** A new partner handling collection and delivery in the UK and
  Europe. Shipment information will cross to them, and that is a cross-border transfer the
  brief did not contemplate.
- **A US software vendor** we are in early partnership talks with. Nothing shared yet; worth
  knowing the rules before we do.
- **A partner request this week** for shipment and rate data supporting a federal bid. We
  stripped it to business-level data, no decedent information. **Confirming that instinct was
  right is worth two minutes.**

**Our CRM.** We have been actively cleaning and writing to HubSpot — 800-plus funeral home
records with contact details for funeral directors. Business contacts rather than families,
but it is a system of record holding personal data that has changed a lot this month.

---

## Part 4 — Things to be careful about on the call

- **Do not send them live documents today.** Anything that goes over is redacted first. We
  can supply a redacted sample of each document type.
- **Resist an open-ended "review our privacy posture" engagement.** Ask for a written memo
  answering the agenda above plus a **prioritised list of changes**, marked as
  before-launch versus can-follow. That is a definable piece of work.
- **One engagement, not three.** The portal feature, the existing upload path, and whether
  our customer agreements cover this are the same underlying problem. So is the diligence
  question. Cheaper together.
- **Donald is on the call** — the budget line sits with him. Frame it as a launch blocker
  plus a diligence blocker plus a contract review, not as legal spend on a feature.

---

## Part 5 — What we can give them immediately

- Current privacy policy and website terms
- A representative funeral home customer agreement
- The technical description of the existing upload path and the proposed S3 design
  — Alex and Kyri can write this, and it is better coming from them
- A **redacted** sample of each document type

---

## One thing worth saying out loud

The portal feature is held until we have guidance, and **we would rather hold it than launch
and retrofit.** That is a real constraint, not a negotiating line — it is what makes this
time-bound.
