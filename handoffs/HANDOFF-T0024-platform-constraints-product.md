# HANDOFF — legal-risk → product

**NOT LEGAL ADVICE — PREPARED FOR COUNSEL REVIEW**

**Raised:** 2026-11-24
**Related task:** `reports/freightflow-amendment-scope.md`; TASK-0024
**Urgency:** WHEN CONVENIENT (before any acquired-book migration is designed)
**Status:** OPEN

*Constraints as my two earlier FreightFlow reports read them, on an unsigned copy. Several are
open counsel questions. Nothing here is a legal opinion or an instruction to Kyri or Alex.*

## What I need

Treat the five constraints below as design inputs for the OMS roadmap and for how an acquired
book's data would be brought in, and tell me if any of them is wrong in practice.

1. **Do not assume the Developer will build migration tooling inside the included hours.** A new
   integration needs a signed Change Order the Developer is not obliged to agree to
   (`freightflow-agreement-review.md` §1.2, test 4). Whether CSI may have others extend CSI-owned
   code is an **open counsel question (N1)**. Do not plan around either answer yet.
2. **Specify the migration once, generically.** A single written definition of what importing an
   acquired book requires (fields, validation, volumes, rollback) lets scope be priced once rather
   than per deal. It must carry no target name or deal term (`§7.5`).
3. **Self-serve first.** Ex. A items 3 and 4 give admins bulk rate and shipper edits and item 6 a
   query tool. Check whether a bulk import exists before anything is requested; a bulk import
   is not listed in Ex. A.
4. **Data.** No clause states CSI owns OMS data, there is no export right during the Term, and
   there is no breach-notification or security standard. An acquired book adds decedent and family
   data into that system. Import only what the operation needs (data minimisation), and treat the
   booking-level export (`reports/oms-export-spec.md`) as the practical test of CSI's data position.
5. **Do not build on the Scraping Library or its derivatives without counsel.** It is Background
   Technology; its licence has no stated term or transferability (I1, I2). The SaaS path also
   triggers a 30% subscription share (Ex. C §6), and the website and partner APIs are outside
   Exhibit A.

## Why I need it

Roadmap choices made now either keep CSI's options open or lock the dependency in.

## What I will do with it

Reflect any correction in the amendment scope and in the counsel brief.

## When I need it

No fixed date. Before an acquired book's data-migration design is started.

## What I'll do if I don't get it

Leave the five constraints as written, labelled legal-risk's read.

## PM decision
<Filled by pm-orchestrator.>
