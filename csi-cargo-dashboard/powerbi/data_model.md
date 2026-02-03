# Data Model Reference

This document describes the data model used in the CSI Cargo Dashboard.

---

## Overview

The dashboard uses a **star schema** design with:
- **Fact tables:** Transactions, bookings, time-series metrics
- **Dimension tables:** Classifications, summaries, breakdowns

---

## Input Data Schema

### 1. financial_transactions

Primary table for all financial data from QuickBooks.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| transaction_id | string | Yes | Unique identifier |
| transaction_date | date | Yes | Date of transaction |
| transaction_type | string | Yes | Invoice, Bill, Payment, etc. |
| category | string | Yes | Revenue, COGS, Operating Expense |
| subcategory | string | No | More specific classification |
| description | string | No | Transaction details |
| customer_name | string | No | Customer (for revenue) |
| vendor_name | string | No | Vendor (for expenses) |
| amount | decimal | Yes | Dollar amount |
| payment_status | string | No | Paid, Pending, Overdue |
| due_date | date | No | Payment due date |

**Valid category values:**
- Revenue
- COGS
- Operating Expense
- Other Income
- Other Expense

### 2. cost_classifications

Reference table mapping expense categories to fixed/variable.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| expense_category | string | Yes | Category from QuickBooks |
| cost_type | string | Yes | Fixed or Variable |
| cost_group | string | No | Grouping (Labor, COGS, Overhead) |
| notes | string | No | Additional context |

**Valid cost_type values:**
- Fixed
- Variable

**Valid cost_group values:**
- Labor
- COGS
- Overhead
- Marketing
- Technology
- Other

### 3. booking_log

Primary table for all booking/shipment data.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| booking_id | string | Yes | Unique booking reference |
| booking_date | date | Yes | When booking was created |
| ship_date | date | No | When shipment occurred |
| customer_name | string | Yes | Funeral home name |
| customer_type | string | No | Corporate, Independent, Other |
| origin_city | string | No | Origin city |
| origin_state | string | No | Origin state code |
| destination_city | string | No | Destination city |
| destination_state_country | string | No | Destination state or country |
| route_type | string | No | Domestic or International |
| airline | string | No | Primary carrier name |
| shipment_type | string | No | Whole Body, Cremated Remains |
| published_rate | decimal | No | Rate charged to customer |
| csi_cost | decimal | No | What CSI paid carrier |
| gross_margin | decimal | No | published_rate - csi_cost |
| intl_paperwork_fee | decimal | No | International paperwork fees |
| other_fees | decimal | No | Any additional fees |
| total_revenue | decimal | Yes | Total revenue from booking |
| was_rebooked | string | No | Yes or No |
| rebooking_cost | decimal | No | Cost of rebooking |
| agent_name | string | No | Handling agent |

### 4. ar_aging

Accounts receivable aging snapshot.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| customer_name | string | Yes | Who owes money |
| invoice_number | string | Yes | Invoice reference |
| invoice_date | date | No | When issued |
| due_date | date | No | When due |
| amount | decimal | Yes | Amount owed |
| days_outstanding | integer | No | Days since due |
| aging_bucket | string | No | Current, 1-30, 31-60, 61-90, 90+ |

### 5. ap_aging

Accounts payable aging snapshot.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| vendor_name | string | Yes | Who you owe |
| bill_number | string | Yes | Bill reference |
| bill_date | date | No | When received |
| due_date | date | No | When due |
| amount | decimal | Yes | Amount owed |
| days_outstanding | integer | No | Days until/since due |
| aging_bucket | string | No | Current, 1-30, 31-60, 61-90, 90+ |

---

## Output Data Schema

The Python processor generates these output tables for PowerBI:

### Executive Summary Tables

#### executive_summary

| Column | Type | Description |
|--------|------|-------------|
| metric | string | Metric name |
| value | decimal | Metric value |
| category | string | Grouping (Financial, Operations, Cash Position) |

#### financial_summary

| Column | Type | Description |
|--------|------|-------------|
| category | string | Revenue/COGS/Operating Expense |
| subcategory | string | Specific type |
| total_amount | decimal | Sum of transactions |
| transaction_count | integer | Number of transactions |
| avg_amount | decimal | Average per transaction |

#### cost_analysis

| Column | Type | Description |
|--------|------|-------------|
| cost_type | string | Fixed or Variable |
| cost_group | string | Labor, COGS, Overhead, etc. |
| total_amount | decimal | Sum of costs |
| percentage | decimal | % of total costs |

### Time Series Tables

#### monthly_pnl

| Column | Type | Description |
|--------|------|-------------|
| month | date | First of month |
| revenue | decimal | Total revenue |
| cogs | decimal | Cost of goods sold |
| operating_expense | decimal | Operating expenses |
| gross_profit | decimal | Revenue - COGS |
| net_profit | decimal | Revenue - All expenses |
| gross_margin_pct | decimal | Gross profit % |
| net_margin_pct | decimal | Net profit % |

#### monthly_bookings

| Column | Type | Description |
|--------|------|-------------|
| month | date | First of month |
| booking_count | integer | Number of bookings |
| total_revenue | decimal | Sum of booking revenue |
| gross_margin | decimal | Sum of booking margins |
| rebooking_cost | decimal | Sum of rebooking costs |
| rebook_count | integer | Bookings that were rebooked |
| rebook_rate | decimal | Rebook % |
| avg_booking_value | decimal | Average revenue per booking |
| margin_pct | decimal | Gross margin % |

#### daily_metrics

| Column | Type | Description |
|--------|------|-------------|
| date | date | Calendar date |
| booking_count | integer | Bookings on that day |
| total_revenue | decimal | Revenue on that day |

#### weekly_metrics

| Column | Type | Description |
|--------|------|-------------|
| week | date | Week start date |
| booking_count | integer | Bookings in week |
| total_revenue | decimal | Revenue in week |

### AR/AP Tables

#### ar_summary

| Column | Type | Description |
|--------|------|-------------|
| aging_bucket | string | Current, 1-30, etc. |
| total_amount | decimal | AR in bucket |
| invoice_count | integer | Number of invoices |
| customer_count | integer | Unique customers |

#### ap_summary

| Column | Type | Description |
|--------|------|-------------|
| aging_bucket | string | Current, 1-30, etc. |
| total_amount | decimal | AP in bucket |
| bill_count | integer | Number of bills |
| vendor_count | integer | Unique vendors |

### Booking Analysis Tables

#### booking_summary

| Column | Type | Description |
|--------|------|-------------|
| total_bookings | integer | Total booking count |
| total_revenue | decimal | Sum of all booking revenue |
| avg_booking_value | decimal | Average revenue |
| total_gross_margin | decimal | Sum of margins |
| avg_margin_per_booking | decimal | Average margin |
| margin_percentage | decimal | Overall margin % |
| rebook_count | integer | Rebookings |
| rebook_rate | decimal | Rebook % |
| total_rebooking_cost | decimal | Cost of rebookings |

#### booking_by_route

| Column | Type | Description |
|--------|------|-------------|
| route_type | string | Domestic or International |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |
| gross_margin | decimal | Margin |
| booking_share_pct | decimal | % of total bookings |
| revenue_share_pct | decimal | % of total revenue |
| margin_pct | decimal | Margin % |

#### booking_by_airline

| Column | Type | Description |
|--------|------|-------------|
| airline | string | Carrier name |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |
| gross_margin | decimal | Margin |
| booking_share_pct | decimal | % of bookings |
| revenue_share_pct | decimal | % of revenue |
| margin_pct | decimal | Margin % |

#### booking_by_customer

| Column | Type | Description |
|--------|------|-------------|
| customer_name | string | Funeral home |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |
| gross_margin | decimal | Margin |
| booking_share_pct | decimal | % of bookings |
| revenue_share_pct | decimal | % of revenue |
| margin_pct | decimal | Margin % |

#### booking_by_customer_type

| Column | Type | Description |
|--------|------|-------------|
| customer_type | string | Corporate/Independent/Other |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |
| gross_margin | decimal | Margin |
| booking_share_pct | decimal | % of bookings |
| revenue_share_pct | decimal | % of revenue |
| margin_pct | decimal | Margin % |

#### booking_by_geography

| Column | Type | Description |
|--------|------|-------------|
| location | string | State or country |
| location_type | string | Origin or Destination |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |

### Operational Tables

#### rework_analysis

| Column | Type | Description |
|--------|------|-------------|
| dimension | string | Analysis type (Airline, Route, etc.) |
| dimension_value | string | Specific value |
| rebook_count | integer | Rebookings |
| total_cost | decimal | Rebooking costs |
| total_bookings | integer | Total bookings (for rate calc) |
| rebook_rate | decimal | Rebook % |

#### agent_productivity

| Column | Type | Description |
|--------|------|-------------|
| agent_name | string | Agent name |
| booking_count | integer | Bookings handled |
| total_revenue | decimal | Revenue generated |
| gross_margin | decimal | Margin generated |
| avg_revenue_per_booking | decimal | Avg revenue |
| avg_margin_per_booking | decimal | Avg margin |
| rebook_count | integer | Rebookings |
| rebook_rate | decimal | Rebook % |

#### carrier_performance

| Column | Type | Description |
|--------|------|-------------|
| airline | string | Carrier name |
| booking_count | integer | Bookings |
| total_revenue | decimal | Revenue |
| gross_margin | decimal | Margin |
| margin_pct | decimal | Margin % |
| rebook_count | integer | Rebookings |
| total_rebooking_cost | decimal | Rebook costs |
| rebook_rate | decimal | Rebook % |

---

## Relationships (PowerBI Data Model)

When you load data into PowerBI, create these relationships:

### Primary Relationships

1. **monthly_pnl[month]** → **monthly_bookings[month]**
   - Type: One-to-One
   - Join on month

2. **monthly_pnl[month]** → **monthly_metrics[month]**
   - Type: One-to-One
   - Join on month

### Optional Relationships (for drilling)

These are useful if you want to drill from summary to detail:

1. **booking_by_customer[customer_name]** → **raw_booking_log[customer_name]**
2. **booking_by_airline[airline]** → **raw_booking_log[airline]**
3. **carrier_performance[airline]** → **rework_analysis[dimension_value]** (where dimension = 'Airline')

---

## Data Quality Rules

### Validation Rules Applied

1. **Dates:** Must be between 2020-01-01 and 2030-12-31
2. **Amounts:** Converted to numeric, NaN filled with 0
3. **Categories:** Mapped to valid values, unknowns flagged
4. **Yes/No fields:** Normalized to 'Yes' or 'No'
5. **Percentages:** Calculated with divide-by-zero protection

### Null Handling

| Column Type | Null Handling |
|-------------|---------------|
| Dates | Left as null (filtered out of aggregations) |
| Numbers | Filled with 0 |
| Categories | Mapped to 'Unknown' |
| Names | Left as-is |

---

## Performance Considerations

### Data Volume Guidelines

| Table | Expected Rows | Refresh Frequency |
|-------|---------------|-------------------|
| financial_transactions | 10K-50K | Weekly |
| booking_log | 5K-20K | Daily |
| ar_aging | 100-500 | Weekly |
| ap_aging | 50-200 | Weekly |
| Monthly summaries | 24-36 | With source data |

### PowerBI Performance Tips

1. **Limit date range:** Filter to last 24-36 months
2. **Use aggregated tables:** Prefer monthly_* over daily_*
3. **Avoid DISTINCT counts:** Use pre-calculated counts
4. **Index key columns:** If using DirectQuery

---

## Change Log

| Date | Change | Author |
|------|--------|--------|
| 2026-02-03 | Initial schema design | Dashboard System |

---

## Questions?

- Schema questions: Review `src/config.py` for column definitions
- Calculation questions: Review `src/metrics_calculator.py`
- Validation questions: Review `src/data_validator.py`
