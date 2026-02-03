# PowerBI Dashboard Setup Guide

This guide walks you through setting up the CSI Cargo Sales Dashboard in PowerBI Desktop.

## Prerequisites

- PowerBI Desktop installed (free download from Microsoft)
- Processed data file: `data/output/dashboard_data.xlsx`
- Run `python scripts/run_dashboard.py` first to generate the data

---

## Step 1: Connect to Data

1. **Open PowerBI Desktop**

2. **Click "Get Data"** (Home tab → Get Data → Excel)

3. **Navigate to and select:** `data/output/dashboard_data.xlsx`

4. **In the Navigator window, select ALL sheets** by checking each box:
   - executive_summary
   - financial_summary
   - cost_analysis
   - monthly_pnl
   - ar_summary
   - ap_summary
   - booking_summary
   - booking_by_route
   - booking_by_airline
   - booking_by_customer
   - booking_by_customer_type
   - booking_by_geography
   - monthly_bookings
   - rework_analysis
   - agent_productivity
   - carrier_performance
   - daily_metrics
   - weekly_metrics
   - monthly_metrics
   - (plus any raw_ sheets you want)

5. **Click "Load"**

---

## Step 2: Create Dashboard Pages

Create the following report pages (click the "+" at the bottom to add pages):

1. **Executive Summary**
2. **Financial Deep Dive**
3. **Growth Analytics**
4. **Operations Insights**

---

## Step 3: Build Executive Summary Page

This page gives the CEO a quick snapshot of business health.

### KPI Cards

1. **Add Card visuals** for these key metrics (drag from executive_summary table):
   - Revenue (YTD)
   - Net Profit (YTD)
   - Profit Margin %
   - Total Bookings (YTD)
   - Gross Margin %
   - Total AR
   - Total AP

2. **Format cards:**
   - Right-click → Format visual
   - Data label → Display units: Auto
   - For currency: Format → Currency

### Revenue Trend Chart

1. **Add Line Chart**
2. **X-axis:** month (from monthly_pnl)
3. **Y-axis:** revenue
4. **Add a second line:** net_profit

### Customer Mix Donut

1. **Add Donut Chart**
2. **Values:** booking_count (from booking_by_customer_type)
3. **Legend:** customer_type

### Alerts Section

1. **Add Card** showing AR Over 90 Days (from executive_summary)
2. **Add Card** showing Rebook Rate %
3. **Use Conditional Formatting** to highlight when values exceed thresholds:
   - Right-click card → Conditional formatting → Background color
   - Set rules: If value > X then Red

---

## Step 4: Build Financial Deep Dive Page

This page is for the CFO to analyze costs and margins.

### P&L Table

1. **Add Table visual**
2. **Columns from monthly_pnl:**
   - month
   - revenue
   - cogs
   - operating_expense
   - gross_profit
   - net_profit
   - gross_margin_pct
   - net_margin_pct

3. **Format as currency** (right-click column → Conditional formatting)

### Fixed vs Variable Costs

1. **Add Stacked Bar Chart**
2. **Y-axis:** cost_group (from cost_analysis)
3. **X-axis:** total_amount
4. **Legend:** cost_type

### Cost Breakdown Donut

1. **Add Donut Chart**
2. **Values:** total_amount (from cost_analysis)
3. **Legend:** cost_group

### AR Aging Chart

1. **Add Stacked Column Chart**
2. **X-axis:** aging_bucket (from ar_summary)
3. **Y-axis:** total_amount
4. **Sort by bucket order** (Current, 1-30, 31-60, etc.)

### AP Aging Chart

1. **Add Stacked Column Chart** (same structure as AR)
2. **Use ap_summary table**

### Monthly Trend Multi-Line

1. **Add Line Chart**
2. **X-axis:** month (from monthly_pnl)
3. **Y-axis:** Add multiple lines:
   - revenue
   - cogs
   - operating_expense

---

## Step 5: Build Growth Analytics Page

This page helps the CSO/CRO understand where revenue comes from.

### Revenue by Airline

1. **Add Horizontal Bar Chart**
2. **Y-axis:** airline (from booking_by_airline)
3. **X-axis:** total_revenue
4. **Sort descending by total_revenue**

### Revenue by Customer

1. **Add Horizontal Bar Chart**
2. **Y-axis:** customer_name (from booking_by_customer)
3. **X-axis:** total_revenue
4. **Show Top 10:** Add filter → Top N → Top 10 by total_revenue

### Revenue by Route Type

1. **Add Donut Chart**
2. **Values:** total_revenue (from booking_by_route)
3. **Legend:** route_type

### Geographic Heatmap (if you have state data)

1. **Add Map visual**
2. **Location:** origin_state (from booking_by_geography)
3. **Size:** total_revenue

### Monthly Booking Trend

1. **Add Area Chart**
2. **X-axis:** month (from monthly_bookings)
3. **Y-axis:** booking_count and total_revenue (add as separate series)

### Customer Concentration Table

1. **Add Table**
2. **Columns from booking_by_customer:**
   - customer_name
   - booking_count
   - total_revenue
   - revenue_share_pct
3. **Add data bars** to revenue_share_pct column

---

## Step 6: Build Operations Insights Page

This page helps the COO monitor operational efficiency.

### Rework Analysis

1. **Add Clustered Bar Chart**
2. **Y-axis:** dimension_value (from rework_analysis)
3. **X-axis:** rebook_rate
4. **Filter to:** dimension = "Airline"

### Carrier Performance Table

1. **Add Table**
2. **Columns from carrier_performance:**
   - airline
   - booking_count
   - total_revenue
   - rebook_count
   - rebook_rate
   - margin_pct
3. **Add conditional formatting** to rebook_rate (red if > 15%)

### Agent Productivity

1. **Add Horizontal Bar Chart**
2. **Y-axis:** agent_name (from agent_productivity)
3. **X-axis:** booking_count

### Agent Metrics Table

1. **Add Table**
2. **Columns from agent_productivity:**
   - agent_name
   - booking_count
   - total_revenue
   - avg_revenue_per_booking
   - rebook_rate (if available)

### Daily Volume Trend

1. **Add Line Chart**
2. **X-axis:** date (from daily_metrics)
3. **Y-axis:** booking_count

---

## Step 7: Add Slicers (Filters)

Add slicers to allow filtering across pages:

1. **Date Range Slicer**
   - Add Slicer visual
   - Field: month (from monthly_bookings or monthly_pnl)
   - Format as "Between" date range

2. **Customer Type Slicer**
   - Add Slicer
   - Field: customer_type (from booking_by_customer_type)
   - Format as buttons or dropdown

3. **Route Type Slicer**
   - Add Slicer
   - Field: route_type (from booking_by_route)

**To sync slicers across pages:**
- View → Sync slicers
- Check the pages where each slicer should apply

---

## Step 8: Add DAX Measures (Advanced)

For more dynamic calculations, add these DAX measures:

### In PowerBI, go to: Modeling → New Measure

```dax
// Year-over-Year Revenue Growth
Revenue YoY Growth =
VAR CurrentYear = SUM(monthly_pnl[revenue])
VAR PriorYear = CALCULATE(
    SUM(monthly_pnl[revenue]),
    DATEADD(monthly_pnl[month], -1, YEAR)
)
RETURN
DIVIDE(CurrentYear - PriorYear, PriorYear, 0)
```

```dax
// Running Total Revenue
Revenue Running Total =
CALCULATE(
    SUM(monthly_pnl[revenue]),
    FILTER(
        ALL(monthly_pnl[month]),
        monthly_pnl[month] <= MAX(monthly_pnl[month])
    )
)
```

```dax
// Average Booking Value
Avg Booking Value =
DIVIDE(
    SUM(booking_summary[total_revenue]),
    SUM(booking_summary[total_bookings]),
    0
)
```

```dax
// Margin at Risk (from rebookings)
Margin at Risk =
VAR TotalMargin = SUM(monthly_bookings[gross_margin])
VAR RebookCosts = SUM(monthly_bookings[rebooking_cost])
RETURN
DIVIDE(RebookCosts, TotalMargin, 0)
```

See `dax_measures.md` for more DAX formulas.

---

## Step 9: Format and Polish

### Apply Consistent Theme

1. **View → Themes → Browse for themes**
2. Or create custom: View → Themes → Customize current theme
3. Set brand colors, fonts

### Add Titles and Labels

1. Select each visual
2. Format → Title → Turn on
3. Add descriptive titles

### Add Company Logo

1. Insert → Image
2. Select CSI logo
3. Position in header area

---

## Step 10: Set Up Refresh

### Manual Refresh

1. **Home → Refresh** to pull latest data
2. Do this after running `python scripts/run_dashboard.py`

### Scheduled Refresh (PowerBI Service)

1. Publish report to PowerBI Service
2. In PowerBI Service: Dataset settings → Scheduled refresh
3. Configure daily/weekly refresh
4. Note: Requires data source to be accessible (e.g., OneDrive, SharePoint, or Gateway)

---

## Troubleshooting

### "Can't find the file"
- Make sure you ran `python scripts/run_dashboard.py` first
- Check the file path in the error message

### Data not updating
- Click Home → Refresh
- If still not updating, check that input files have new data

### Visuals showing blank
- Check that the table has data (Preview in data view)
- Check for filter conflicts

### Performance is slow
- Reduce data volume in output (filter to recent 24 months)
- Simplify complex DAX measures

---

## Next Steps

1. **Share with team:** File → Publish to PowerBI Service
2. **Create mobile view:** View → Mobile layout
3. **Set up alerts:** In PowerBI Service, set alerts on KPI tiles
4. **Embed in Teams:** Share → Embed in Microsoft Teams

For CTO integration with live OMS data, see `cto_integration_spec.md`.
