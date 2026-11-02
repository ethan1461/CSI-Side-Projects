---
title: AWS account takeover and hosting
owner: Ethan Silvey
as_of: 2026-11-01
source: 57fb3179, 847f5e06, 22cc12e7, 9d6d7fa8 (see sources.md)
---

# AWS

**Goal:** move CSI's AWS account off vendor Rednodo to CSI self-management, decide hosting
for the new OMS/portal, and check eligibility for AWS funding programs.

**Owner:** Ethan.

## Facts (as of 2026-10-13)

- AWS today hosts only the legacy ERP (EC2 + RDS), built and managed by Rednodo. The
  website, Microsoft 365 mail and AI work run elsewhere. The new OMS/portal is the real
  migration candidate; its hosting is undecided [847f5e06].
- The account is standalone (not reseller-billed). Root sits on an address the vendor
  set up under the CEO's name and the vendor holds root MFA; Ethan has an admin IAM user,
  not root [847f5e06].
- Workload as described to AWS: ~925 bookings/month, small in compute; document storage
  is the main sizing unknown [57fb3179].

## Decisions

- Root email moves to an address Ethan controls, with the CEO as MFA backup; the MFA
  transfer needs an in-person session with Claudio and the CEO [847f5e06].
- AWS rep calls: resolve root access first; ask whether the OMS/portal qualifies for MAP
  or POC credits (incl. implementation support with Kyri); no spend or architecture
  commitments [22cc12e7, 2026-09-28].
- Avoid migrating during peak winter mortality season [57fb3179].

## Status / next steps

- Ethan emailed Claudio about root access by 2026-10-04 [9d6d7fa8].
- IAM audit found contractor users without MFA and duplicate users; cleanup pending
  [847f5e06].
- **Status unknown since 2026-10-13:** root MFA transfer, IAM cleanup, credit
  eligibility, whether the new OMS uses AWS Bedrock (Alex to confirm).
