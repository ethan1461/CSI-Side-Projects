<!-- converted from: Final CSI OMS Tech Specs.docx -->

CSI OMS Requirements

### Core Features (i.e. required for initial launch, needed before 11/30)

### 1. Booking Creation System

End-to-end workflow for both domestic and international bookings.

Allow agents to input customer, airline, flight, and billing data for bookings.

Ability to add custom fields (e.g. trucking, consulate documents) for international bookings.

Email/text parsing to extract:

Customer info.

Airline confirmation details.

Funeral home fields should be searchable  from the CSI database (with shipper/consignee filters).

Date/time selectors via calendar or dropdowns

Validation checks on each booking, like following examples (suggestions, not hard requirements):

Flight date must be today +0 to +10 days.

No arrivals before departures.

Flight number must match the airline.

First 3 digits of AWB match airline.

Workflow generates:

Templated booking request email to airline(s).

Shipping label, tag, and rendered customer confirmation form matching existing CSI outputs.

Packing instruction rules for international shipments

Booking records stored in CSI-owned database tables, unified with legacy records

Additionally for international shipments:

Custom booking fields (e.g., consulate doc requirements).

Addition of packing instruction rules in confirmation:

Clearly flagged handling for original IDs and document envelopes.

Automated reminders for burial transit permit handling (for shipping funeral homes)

Programmatic generation of pickup lists for each airport.

### 2. Bookings Management Dashboard

Dashboard for managing in-progress and recently-completed bookings.

Features:

Real-time update of bookings (in progress & recently completed).

Automatic creation of dashboard entry upon start of booking process.

Status-saving (e.g. drafts).

Click-to-resume from draft.

Draft with existing reference pulls correct booking ID (doesn’t create duplicates).

### 3. Quote + Facility Hours Lookup Engine

All rate and facility hour data stored in the CSI database

Monthly scrape and update airport facility hours by airline/airport (where available)

Admin only rate tools:

Searchable displayed table of all rates by origin, destination, or airline

Ability to edit rates individually and in bulk

Dedicated quote generation page with:

Enter origin and destination airports to automatically get the contracted rate (where available)

Discount logic (per customer).

Option to create, save, and retrieve quotes.

Ability to store multiple rates per quote.

### 4. Permissioning + Authentication

Authentication system with email-based roles:

Agent:

Bookings creation.

Admin:

All above + edit rates + edit shipper funeral homes.

Super Admin:

All above + edit roles.

### 5. Task Management Dashboard

Dashboard to manage the assignment of in-progress bookings/quote requests

Sections for bookings, pending, out of booking window, rates to quote, and completed

Ability to assign owners and statuses for each task

### Additional Features Discussed (i.e. can launch after 11/30, deadline of 12/31)

### 6. On-Demand Shipment Tracking

Airline API integration (where available) for:

Location/status updates.

Delay and cancellation alerts.

Final weight of shipment

Shipment tracking module for agents to quickly find + send updates.

Alert system for flagged disruptions.

### 7. Advanced Admin Tools

Quickbooks export integration for billing

Ability to create weekly invoices for selected customers

Cleaned database that enables creation of PowerBI reporting dashboards:

Revenue by month/quarter/YTD vs. prior year

# of bookings month/quarter/YTD vs. prior year

Revenue by funeral home group by month/quarter/YTD

# of bookings by funeral home group by month/quarter/YTD

# of bookings by Staff Person by month/quarter/YTD

Export capabilities for audit/compliance.

Agent performance analytics.

### 8. Frontend System for CSI Clients

Automatic Quoting System

Enter origin and destination airports to automatically get a quote estimate

Example quoting methods:

Contracted rates plus profit margin

Average of past shipment rates to same country / region

Save, retrieve, and convert quotes into bookings

Booking Request Form

Submit the “customer information” section of a booking

Attach relevant forms (permits, certificates, etc.)

Integrates to appear in the CSI backend system as a new booking

View Past / Current Bookings

Order tracker with pickup times and other key details for active bookings

Live updates for flight departures, delays, arrivals, and deliveries

Ability to re-print tags, labels, and customer confirmation forms

CSI Frontend System Requirements

Automatic Quoting System

Enter origin and destination airports to automatically get a quote estimate

Calculated via contracted rates plus profit margin or past shipment data

Save, retrieve, and convert quotes into bookings with one click

Booking Request Form

Submit the “customer information” section of a booking

Attach relevant forms (permits, certificates, etc.)

Immediately appears in the backend system as an in-progress booking

View Past / Current Bookings

Order tracker with pickup times and other key details for current bookings

Live updates for flight departures, delays, arrivals, and deliveries

Ability to re-print tags, labels, and customer confirmation forms

Flight & Transport Scheduling with Multi-Carrier Integration

Search and select flights across multiple airlines from within the platform

Integration with flight tracking across partner airlines
