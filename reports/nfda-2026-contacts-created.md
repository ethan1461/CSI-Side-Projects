# NFDA 2026 contacts created in HubSpot — log

**revops-crm, 2026-11-10. Handoff: `handoffs/HANDOFF-nfda-2026-contacts-revops-crm.md`.** No sequence, no enrolment, no workflow, no email. Marketing status untouched (all read back `false`, the HubSpot default for new contacts).

Pre-check: search by all 8 emails returned 0 existing contacts. Created 8 contacts, 1 Company, 8 notes.

| Contact id | Contact | Owner | Lifecycle | Company association |
|---|---|---|---|---|
| 261610996354 | L. Gundrum (ICCFA) | Ethan | other | none (no ICCFA company exists; name in text field only) |
| 261613577290 | T. Griffin (Carriage Services) | Ethan | lead | **new Company "Carriage Services" 60854605591** (no OMS id, owner Ethan) |
| 261612415890 | Z. Woodall (AFP Horizon) | Stacy | lead | none |
| 261620002439 | R. Haug Edman (Wozney-Killian, inferred) | Otto | lead | none |
| 261622255732 | L. Karlese (Heritage Life Story) | Otto | customer | existing Company 60878018986 (OMS 8162) |
| 261621029533 | Meghan (Heritage, Charlotte) | Stacy | lead | none; HOLD note: no call before Ethan's Carriage note |
| 261619915533 | M. Guevara (Donaldson) | Otto | lead | none; not associated to Sagel Bloomfield 60872321678 |
| 261612433518 | K. Wards (S.L. Carter) | Stacy | lead | none |

Read-back: 8/8 contacts match intended owner and lifecycle; both associations returned 1 successful, 0 failed; 8/8 notes created and associated.

## Decisions made under default-and-proceed (reverse if wrong)
1. **Ethan's owner id.** `search_owners` returns two active "Ethan Silvey" ids (79582603 and 520666215). I used **520666215** because it already owns 7 existing contacts; 79582603 owns none. Reassignment is a single property edit on 3 records (2 contacts, 1 company).
2. **Lead source "NFDA 2026" is NOT a property.** No lead-source or event property exists on contacts (`hs_analytics_source` and `hs_object_source_label` are system-set). The source is recorded in a note on every contact. If Ethan wants it filterable, he must create a contact property (suggest `lead_source_detail`, dropdown or single-line text, value `NFDA 2026`); then I populate it.
3. **Carriage Services parent Company created**, as the handoff allowed ("create or find"). Creating the record is not outreach; the Ethan-gate on contact with Carriage stands.
4. **Lifecycle for Lindsy and Tony** was "per Ethan" with no value given: Lindsy = `other` (not a prospect), Tony = `lead`. Both are one-field edits.
5. Surname for Raven recorded as "Haug Edman" (as supplied); Meghan has no surname.
