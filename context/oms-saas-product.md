<!-- converted from: CSI SaaS Product.docx -->

# CSI SaaS Product

## 1. Integrated Shipment Management Dashboard

Description:

This dashboard will act as the mission control center for high-volume funeral homes, giving them a real-time view of:

Active, completed, and draft bookings

Shipment status (e.g., pending, booked, in transit, delivered)

Tags and confirmations

Access to uploaded booking confirmations and delivery receipts

Think of it like a FedEx Delivery Manager, but purpose-built for human remains.

Requirements:

Front-end UI/UX for desktop (mobile-responsive optional for v1)

API endpoint or secure DB calls to pull booking data (from CSI OMS)

Role-based authentication system (agent login → sees only their bookings)

Status tags and shipment metadata displayed dynamically

Document viewer or downloadable links (PDF confirmations, labels, etc.)

Build Effort: High (4.5/5)

Will require UI design, database querying, permissions framework

Real-time status updates may require polling or websockets

Document storage/handling requires careful security protocols

Testing Plan:

Simulate bookings from different accounts → verify visibility restrictions

Validate that updates from the internal CSI system reflect instantly

Ensure document links work and are permission-secure

Perform role-switching and data leakage tests

Prioritization: Top Priority

Impact: 5/5

Feasibility: 4/5

Why: Centralizes value for clients, increases "stickiness," and enables future upsells

## 2. Real-Time Rate and Quote Access

Description:

Empowers trusted partners to bypass the back-and-forth by:

Looking up live rates for lanes they commonly ship

Generating custom quotes with access to their discounted pricing tiers

Turning those quotes into bookings instantly

This reduces friction, call volume, and allows you to become a true logistics-as-a-service layer.

Requirements:

Rate lookup UI component: origin, destination, weight/class filters

Access to internal pricing tables (filtered by customer)

Quote builder (quote → booking conversion path)

Optional: store quote history and allow PDF/email download

Build Effort: Medium-High (4/5)

Rate logic already exists in OMS; exposing it securely is the key

Front-end effort moderate; discounting logic will need testing

Requires database indexing for performance at scale

Testing Plan:

Test accuracy of rate outputs for different customers

Validate that generated quotes can be converted into bookings

Fuzz test for impossible routes or malformed inputs

Confirm discount logic applies correctly by account

Prioritization: #2 Priority

Impact: 5/5

Feasibility: 3.5/5

Why: This is a power feature that builds trust, saves time, and helps funeral homes budget more confidently.

## 3. Automated Documentation Handling

Description:

Automatically generates all required shipment docs (labels, tags, customs checklists, transit permits) based on:

Shipment type (domestic/international)

Destination requirements

Known shipper status

Consulate-specific rules

This is your risk-reduction feature — eliminating costly documentation errors.

Requirements:

Templates for all common documentation types (e.g., BT Permit, airway bill, consulate docs)

Dynamic field injection into documents

Conditional logic based on booking inputs (e.g., international = generate doc set A)

Secure file storage + downloadable links

Reminders for permits or missing docs

Build Effort: High (4.5/5)

Complexity increases for international routes (e.g., Brazil, Dominican Republic)

May need to support templating engine (e.g., Docmosis, Puppeteer for PDF generation)

Version control and compliance checking needed

Testing Plan:

Use real past shipments → compare generated documents to originals

Edge-case testing (e.g., customer skips critical input fields)

Verify PDF generation for every supported consulate

Upload stress testing (multi-doc batch)

Prioritization: #3 Priority

Impact: 4.5/5

Feasibility: 3/5

Why: While technically intensive, it’s a differentiator — no more chasing permit errors or misrouted IDs

## 4. Customized Reporting Tools

Description:

Gives clients analytics on:

Total monthly bookings

Average cost per shipment

Mode splits (domestic vs. international)

Carrier performance (e.g., % of shipments delayed)

These insights help funeral homes justify costs, plan better, and prove value internally.

Requirements:

Define core reporting metrics (start with 5-6 KPIs)

Analytics dashboard with filtering (time range, origin/destination, carrier)

Export feature (PDF, Excel)

Secure access by client account

Build Effort: Medium (3.5/5)

Much of this data exists; needs to be aggregated and visualized

May use BI tools (Metabase, Chart.js, Redash) or in-app charts

Testing Plan:

Match dashboard output to existing financials

User testing with clients to ensure filters and KPIs are intuitive

Test export functionality and visual fidelity of reports

Prioritization: #4 Priority

Impact: 3.5/5

Feasibility: 4/5

Why: Enhances trust and transparency, but not mission-critical for launch

## 5. White-Glove Support Services

Description:

Premium support offering layered on top of the platform:

Dedicated account manager for each top-tier funeral home

Priority support hotline + escalation SLAs

Optional onboarding concierge + training webinars

Annual service reviews + strategy consultations

This is your relationship glue — it converts high-volume shippers into long-term clients.

Requirements:

Staffing plan (dedicated AMs vs. pooled concierge team)

CRM or ticketing tool (Hubspot, Front, or simple Airtable CRM)

SOPs for support SLAs, response times, escalation paths

Training collateral (videos, guides, onboarding decks)

Build Effort: Low-Medium (2.5/5)

Much of this is process-based, not tech-based

Requires thoughtful staffing and support system design

Testing Plan:

Run pilot with top 3 clients

Track satisfaction scores, resolution times, churn/revenue delta

Audit AM-client touchpoints quarterly

Prioritization: #5 Priority

Impact: 3.5/5

Feasibility: 5/5

Why: Easy to implement — especially with the right people — but better after the dashboard and quote system are live

# Pricing Model

Ideal Use Case:

General Access: Low-volume clients, 1–4 shipments/month

Pro: Mid- to high-volume clients, 5–20 shipments/month

Elite: Strategic partners doing 20+ shipments/month who need custom support & integrations

Pricing Tiers

Annual billing: Offer 2 months free ($4,990/year Pro, $9,990/year Elite)

## Feature Matrix

## Financial Model Snapshot (Illustrative)

## Add-Ons (Optional, Across Tiers)

## Packaging Strategy

Onboarding Offer: Waive Pro for first month with minimum shipment commitment

Volume Discount: Free Pro access for clients doing 15+ shipments/month (or bake it into margin)

Trial Funnel: Let General Access clients test Pro features free for 30 days

Bundled Renewal Option: If they commit to 12-month term, offer 10% off + lock in rate

# CSI Pro Onboarding FAQ (Internal or Client-Facing)

| Tier Name | Monthly Fee | Target Client Volume | Primary Benefits |
|---|---|---|---|
| General Access | $0 | 1–4 shipments/month | Manual email-based booking only |
| Pro | $499/month | 5–20 shipments/month | Full dashboard access, quoting tools, real-time updates, premium support |
| Elite | $999/month | 20+ shipments/month | All Pro features + SLA-backed turnaround, integrations, and dedicated concierge |

| Feature | General Access | Pro | Elite |
|---|---|---|---|
| Web-based Booking Dashboard | ❌ | ✅ | ✅ |
| Track All Shipments + View Status | ❌ | ✅ | ✅ |
| Real-Time Rate + Quote Generator | ❌ | ✅ | ✅ |
| Document Generator (Tags, BT Permits, etc.) | ❌ | ✅ | ✅ |
| View + Download Airline Confirmations | ❌ | ✅ | ✅ |
| Reporting Dashboard (Volume, Cost, Carrier) | ❌ | ✅ | ✅ |
| Dedicated Account Manager | ❌ | ✅ | ✅ |
| SLA-Backed Booking Turnaround (<1 hr) | ❌ | ❌ | ✅ |
| Early Access to New Features | ❌ | ❌ | ✅ |
| Custom Integrations (e.g., CRM, API feeds) | ❌ | ❌ | ✅ |

| Scenario | Pro Tier | Elite Tier | Monthly SaaS Revenue |
|---|---|---|---|
| 15 clients at $499 | $7,485 | - | $7,485 |
| 5 clients at $999 | - | $4,995 | $4,995 |
| Total Monthly SaaS Revenue |  |  | $12,480 |
| Annualized Recurring Revenue |  |  | $149,760 |

| Add-On | Price | Notes |
|---|---|---|
| Additional Users | $10/user/month | Base license covers up to 5 users |
| API/CRM Integration | $250 setup + $50/month | For syncing to their case management system |
| Custom Reports Module | $100/month per report | KPI-specific reports (e.g., for corporate buyers) |
| Onboarding Concierge (one-time) | $500 | Recommended for all Pro/Elite clients |

| Question | Answer |
|---|---|
| Who is CSI Pro for? | Funeral homes shipping 5+ cases/month with Cargo Sales who want greater control, speed, and visibility in their booking process. |
| How much does it cost? | $499/month. Annual billing gets you 2 months free. |
| What do I get? | Shipment dashboard, quoting engine, document automation, and premium support. |
| How do I access it? | Once enrolled, you'll receive login credentials and a short onboarding guide from your account manager. |
| Can I try it before committing? | Yes. We offer a 30-day free trial with full access to all Pro features. |
| What if I need help? | Your dedicated account manager is on-call for onboarding and support. |
| Is my data secure? | Yes. The platform uses encrypted connections and role-based access controls. |
| How do I cancel or change plans? | Just email us at support@cargosales.com — no hidden fees or cancellation penalties. |
