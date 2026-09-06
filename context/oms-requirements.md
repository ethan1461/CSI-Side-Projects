<!-- converted from: CSI OMS Requirements.docx -->

CSI OMS Requirements

Core Features (i.e. required for initial launch, needed before Sep 30th)

1. Booking Creation System

End-to-end workflow for both domestic and international bookings.

Inputs:

Drag-and-drop support for .eml files (Outlook).

Email parsing to extract:

Customer info (name, company, contact).

Airline confirmation details.

Manual override/edit form for customer and airline data.

Funeral home lookups with shipper filters.

Validation checks:

Flight date must be today +0 to +10 days.

No arrivals before departures.

Flight number must match the airline.

First 3 digits of AWB match airline.

Date/time selectors via calendar or dropdowns.

Generates:

Booking request email to airline(s).

Shipping label, tag, and rendered customer confirmation form.

Writes booking to existing CSI DB tables used by the current system.

Additionally for international shipments:

Custom booking fields (e.g., consulate doc requirements).

Addition of packing instruction rules in confirmation:

Clearly flagged handling for original IDs and document envelopes.

Automated reminders for burial transit permit handling (for shipping funeral homes)

Auto-generation of pickup list.

2. Bookings Management Dashboard

Dashboard for managing in-progress and recently-completed bookings.

Features:

Real-time update of bookings (in progress & recently completed).

Auto-create dashboard entry upon start of booking process.

Status-saving (e.g., drafts).

Click-to-resume from draft.

Draft with existing reference pulls correct booking ID (doesn’t create duplicates).

3. Quote + Facility Hours Lookup Engine

All rate and facility hour data stored in the CSI database

Displayed table of editable rates (admin only).

Scrape and update airport facility hours by airline/airport (monthly)

Searchable quotes database (search by origin/destination).

Create quotes that can be turned into bookings.

Ability to store multiple rates per quote.

Dedicated quote generation page with:

Discount logic (per customer).

Option to save and retrieve quotes.

4. Permissioning + Authentication

Authentication system with email-based roles:

Agent:

Bookings creation.

Admin:

All above + edit rates + edit shipper funeral homes.

Super Admin:

All above + edit roles.

5. Task Management Dashboard

Dashboard to facilitate the management of in-progress bookings/quote requests

Sections for bookings, pending, out of booking window, rates to quote, and completed

Ability to assign owners and statuses for each task

Additional Features Discussed (i.e. can launch after Sep 30th without penalty)

6. On-Demand Shipment Tracking

Airline API integration (where available) for:

Location/status updates.

Delay and cancellation alerts.

Shipment tracking module for agents to quickly find + send updates.

Alert system for flagged disruptions.

7. Advanced Admin Tools

Reporting dashboards:

Monthly booking volumes.

Carrier performance and usage.

Route-level tracking.

Export capabilities for audit/compliance.

Quickbooks export integration for billing

Agent performance analytics.
