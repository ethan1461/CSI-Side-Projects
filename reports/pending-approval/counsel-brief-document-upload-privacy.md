# Counsel brief — document upload, privacy and sensitive data

**DRAFT for Ethan.** Not sent (`CLAUDE.md §7.1`).
**Purpose:** a one-page brief to send to candidate attorneys so they can scope and quote without a discovery call. Raised by Alex and Kyri; Ethan wants counsel engaged by Wednesday 2026-11-05.

---

## Notes for Ethan — delete before sending

**Start with Matt.** CSI's former attorney already knows the business, which is worth more
than any cold search. Ask him two things: is this in his lane, or is it far enough into
privacy and data protection that he'd want a specialist — and if the latter, who would he
send you to?

*(Correction, 2026-11-03: an earlier version of this note said to start with Palermo
Landsman & Ross. **They are CSI's outside tax and CPA firm, not attorneys** —
`context/brain/people.md` records this correctly and I did not check it. Worth asking
separately whether Arty sits at that firm; if so, two threads are one relationship.)*

**What kind of lawyer you want.** Privacy and data protection, with **sensitive-category
data** experience — healthcare-adjacent is the closest analogue even if HIPAA turns out not
to apply. **IAPP credentials (CIPP/US) are a reasonable filter.** You do not need a
funeral-industry specialist and you will struggle to find one; the industry context is
something you supply, not something you hire for.

**Scope it as a fixed-fee written opinion, not an hourly open-ended review.** You want a
memo answering the seven questions below, plus a short list of what to change before
launch. That is a defined piece of work a firm can price. Open-ended "review our privacy
posture" engagements are how this gets expensive without getting decided.

**Two things to bundle in, because they are the same underlying problem and one engagement
is cheaper than three:**

- **The diligence question.** CSI cannot currently send operational exports to any outside
  party — a lender, an adviser, a buyer — because they carry decedent and family data by
  design. Same data, same law, same lawyer.
- **The customer agreements.** Whatever CSI's funeral home agreements say about data is
  the foundation for both questions, and nobody has read them for this purpose.

**For Donald tomorrow:** this needs a budget line. Frame it as **one engagement covering a
launch blocker, a diligence blocker and a contract review** — not as legal spend on a
feature. And it is time-bound: the portal feature cannot ship without it.

**One thing to say plainly to counsel:** CSI already accepts document uploads on its public
website today. **This is not a question about a future feature. It is a question about
something already running**, which Alex and Kyri flagged honestly rather than quietly
building on top of.

---

## The brief

**Company:** Cargo Sales International, Miami FL. 23 years. ~$15M revenue. Air transport
and logistics broker for human remains. Customers are funeral homes and funeral home
groups — **never consumers.** Roughly 11,000 shipments a year, domestic and international.

**Sister company:** Southern Cross Trading, under common ownership, holding certain
operating certifications.

### What we need

A written opinion on CSI's collection, storage and sharing of sensitive documents — both
the process running today and a proposed new feature — and a list of what we should change
before we launch the new one.

### The data in question

International shipments require documents that are supplied by the funeral home and may
include:

- **Passports** and cancelled passport bio-data pages of the deceased
- **Death certificates**
- Letters of non-contagious disease from a health authority
- Permits to transport or dispose of human remains
- Embalming certificates
- Consular and apostille paperwork

These contain decedent identity data, and in many cases **living family members' names and
contact details.**

### What exists today

- CSI's **public website already accepts document uploads.**
- The legacy code saves uploaded documents on the ERP server, records the filenames, and
  emails them to a shared operational mailbox.
- **We have not confirmed** the deployed configuration, who can access the stored files, or
  how retention and deletion work across the server, the email system and backups. Our
  hosting provider would need to be involved to establish this.

### What is proposed

A document upload feature in CSI's customer portal, storing documents in **AWS S3**, with
access from the portal and the ERP, so agents retrieve documents from the system rather
than from email.

### The questions

1. **Existing process.** Does CSI's current collection, storage and sharing of these
   documents meet applicable obligations? **Are interim changes needed now**, ahead of any
   new feature?
2. **Authority and access.** What authority does a funeral home need in order to upload
   these documents to us, and who inside CSI should be permitted to view, download or
   share them?
3. **Notices and agreements.** Do CSI's existing privacy policy, website terms and funeral
   home customer agreements adequately cover passports, death certificates and consular
   paperwork? We can supply all three.
4. **HIPAA.** Does it apply to any of CSI's customer relationships or services, and if so
   what additional agreements or safeguards would be required?
5. **International.** Our shipments and partner relationships span Mexico, the Dominican
   Republic, Guatemala, El Salvador, the Caribbean, Europe, Africa and Asia. What
   additional privacy, cross-border transfer or document-sharing obligations does that
   create?
6. **Retention and security.** How long should each document type be kept, how should
   deletion work across all systems including backups, and what safeguards and incident
   procedures should exist if information is accessed or disclosed improperly?
7. **Disclosure to third parties.** Separately from the feature: CSI's operational exports
   contain decedent and family data. **What are our obligations if such records would be
   disclosed to outside parties** — advisers, lenders, prospective investors or acquirers —
   and what should we do to make that possible safely?

### How we would like it delivered

A written memo answering the above, with a **prioritised list of changes**, marking which
must happen before the new feature launches and which can follow. We would prefer a
**fixed fee** for that defined scope.

### Timing

We would like to engage this week. The portal feature is held until we have guidance, and
we would rather hold it than launch and retrofit.

### What we can provide immediately

Current privacy policy and website terms; a representative funeral home customer
agreement; the technical description of the existing upload path and the proposed design;
a sample of the document types above **with the personal data redacted**.
