# DAX Measures Reference

This document contains all DAX measures for the CSI Cargo Dashboard.

## How to Add DAX Measures in PowerBI

1. Go to **Modeling** tab
2. Click **New Measure**
3. Paste the DAX formula
4. Press Enter
5. The measure appears in your Fields pane

---

## Financial Measures

### Total Revenue
```dax
Total Revenue =
SUM(monthly_pnl[revenue])
```

### Total Expenses
```dax
Total Expenses =
SUM(monthly_pnl[cogs]) + SUM(monthly_pnl[operating_expense])
```

### Gross Profit
```dax
Gross Profit =
SUM(monthly_pnl[revenue]) - SUM(monthly_pnl[cogs])
```

### Net Profit
```dax
Net Profit =
SUM(monthly_pnl[revenue]) - SUM(monthly_pnl[cogs]) - SUM(monthly_pnl[operating_expense])
```

### Gross Margin %
```dax
Gross Margin % =
DIVIDE(
    [Gross Profit],
    [Total Revenue],
    0
) * 100
```

### Net Margin %
```dax
Net Margin % =
DIVIDE(
    [Net Profit],
    [Total Revenue],
    0
) * 100
```

### Revenue YoY Growth
```dax
Revenue YoY Growth =
VAR CurrentPeriod = [Total Revenue]
VAR PriorPeriod = CALCULATE(
    [Total Revenue],
    DATEADD(monthly_pnl[month], -12, MONTH)
)
RETURN
DIVIDE(CurrentPeriod - PriorPeriod, PriorPeriod, 0) * 100
```

### Revenue MoM Growth
```dax
Revenue MoM Growth =
VAR CurrentMonth = [Total Revenue]
VAR PriorMonth = CALCULATE(
    [Total Revenue],
    DATEADD(monthly_pnl[month], -1, MONTH)
)
RETURN
DIVIDE(CurrentMonth - PriorMonth, PriorMonth, 0) * 100
```

### Revenue Running Total
```dax
Revenue Running Total =
CALCULATE(
    [Total Revenue],
    FILTER(
        ALL(monthly_pnl[month]),
        monthly_pnl[month] <= MAX(monthly_pnl[month])
    )
)
```

---

## Cost Analysis Measures

### Fixed Costs Total
```dax
Fixed Costs =
CALCULATE(
    SUM(cost_analysis[total_amount]),
    cost_analysis[cost_type] = "Fixed"
)
```

### Variable Costs Total
```dax
Variable Costs =
CALCULATE(
    SUM(cost_analysis[total_amount]),
    cost_analysis[cost_type] = "Variable"
)
```

### Fixed Cost Ratio
```dax
Fixed Cost Ratio =
DIVIDE(
    [Fixed Costs],
    [Fixed Costs] + [Variable Costs],
    0
) * 100
```

### Cost per Booking
```dax
Cost per Booking =
DIVIDE(
    [Total Expenses],
    SUM(booking_summary[total_bookings]),
    0
)
```

---

## Booking Measures

### Total Bookings
```dax
Total Bookings =
SUM(booking_summary[total_bookings])
```

### Average Booking Value
```dax
Avg Booking Value =
DIVIDE(
    SUM(booking_summary[total_revenue]),
    SUM(booking_summary[total_bookings]),
    0
)
```

### Booking Revenue
```dax
Booking Revenue =
SUM(monthly_bookings[total_revenue])
```

### Booking Gross Margin
```dax
Booking Gross Margin =
SUM(monthly_bookings[gross_margin])
```

### Booking Margin %
```dax
Booking Margin % =
DIVIDE(
    [Booking Gross Margin],
    [Booking Revenue],
    0
) * 100
```

### Bookings This Month
```dax
Bookings This Month =
CALCULATE(
    SUM(monthly_bookings[booking_count]),
    MONTH(monthly_bookings[month]) = MONTH(TODAY()) &&
    YEAR(monthly_bookings[month]) = YEAR(TODAY())
)
```

### Bookings Last Month
```dax
Bookings Last Month =
CALCULATE(
    SUM(monthly_bookings[booking_count]),
    MONTH(monthly_bookings[month]) = MONTH(EDATE(TODAY(), -1)) &&
    YEAR(monthly_bookings[month]) = YEAR(EDATE(TODAY(), -1))
)
```

---

## Rework/Rebooking Measures

### Rebook Count
```dax
Rebook Count =
SUM(monthly_bookings[rebook_count])
```

### Rebook Rate
```dax
Rebook Rate =
DIVIDE(
    [Rebook Count],
    [Total Bookings],
    0
) * 100
```

### Total Rebooking Cost
```dax
Total Rebooking Cost =
SUM(monthly_bookings[rebooking_cost])
```

### Avg Rebooking Cost
```dax
Avg Rebooking Cost =
DIVIDE(
    [Total Rebooking Cost],
    [Rebook Count],
    0
)
```

### Margin Erosion from Rebooking
```dax
Margin Erosion % =
DIVIDE(
    [Total Rebooking Cost],
    [Booking Gross Margin],
    0
) * 100
```

### Net Margin After Rework
```dax
Net Margin After Rework =
[Booking Gross Margin] - [Total Rebooking Cost]
```

---

## AR/AP Measures

### Total AR
```dax
Total AR =
SUM(ar_summary[total_amount])
```

### Total AP
```dax
Total AP =
SUM(ap_summary[total_amount])
```

### Net Working Capital
```dax
Net Working Capital =
[Total AR] - [Total AP]
```

### AR Over 90 Days
```dax
AR Over 90 =
CALCULATE(
    SUM(ar_summary[total_amount]),
    ar_summary[aging_bucket] = "90+"
)
```

### AR Over 90 %
```dax
AR Over 90 % =
DIVIDE(
    [AR Over 90],
    [Total AR],
    0
) * 100
```

### AP Over 90 Days
```dax
AP Over 90 =
CALCULATE(
    SUM(ap_summary[total_amount]),
    ap_summary[aging_bucket] = "90+"
)
```

### Days Sales Outstanding (DSO)
```dax
DSO Estimate =
DIVIDE(
    [Total AR],
    [Total Revenue] / 365,
    0
)
```

---

## Customer Concentration Measures

### Top Customer Revenue
```dax
Top Customer Revenue =
CALCULATE(
    SUM(booking_by_customer[total_revenue]),
    TOPN(1, ALL(booking_by_customer), booking_by_customer[total_revenue], DESC)
)
```

### Top Customer %
```dax
Top Customer % =
DIVIDE(
    [Top Customer Revenue],
    [Booking Revenue],
    0
) * 100
```

### Top 5 Customers %
```dax
Top 5 Customers % =
VAR Top5Revenue = CALCULATE(
    SUM(booking_by_customer[total_revenue]),
    TOPN(5, ALL(booking_by_customer), booking_by_customer[total_revenue], DESC)
)
RETURN
DIVIDE(Top5Revenue, [Booking Revenue], 0) * 100
```

### Corporate vs Independent Split
```dax
Corporate % =
CALCULATE(
    DIVIDE(
        SUM(booking_by_customer_type[total_revenue]),
        [Booking Revenue],
        0
    ),
    booking_by_customer_type[customer_type] = "Corporate"
) * 100
```

---

## Carrier Performance Measures

### Carrier Rebook Rate
```dax
Carrier Rebook Rate =
DIVIDE(
    SUM(carrier_performance[rebook_count]),
    SUM(carrier_performance[booking_count]),
    0
) * 100
```

### Best Performing Carrier
```dax
Best Carrier =
CALCULATE(
    FIRSTNONBLANK(carrier_performance[airline], 1),
    TOPN(1, ALL(carrier_performance), carrier_performance[margin_pct], DESC)
)
```

### Worst Rebook Carrier
```dax
Worst Rebook Carrier =
CALCULATE(
    FIRSTNONBLANK(carrier_performance[airline], 1),
    TOPN(1, ALL(carrier_performance), carrier_performance[rebook_rate], DESC)
)
```

---

## Agent Productivity Measures

### Avg Bookings per Agent
```dax
Avg Bookings per Agent =
DIVIDE(
    [Total Bookings],
    DISTINCTCOUNT(agent_productivity[agent_name]),
    0
)
```

### Top Agent
```dax
Top Agent =
CALCULATE(
    FIRSTNONBLANK(agent_productivity[agent_name], 1),
    TOPN(1, ALL(agent_productivity), agent_productivity[booking_count], DESC)
)
```

### Agent Revenue per Booking
```dax
Agent Revenue per Booking =
DIVIDE(
    SUM(agent_productivity[total_revenue]),
    SUM(agent_productivity[booking_count]),
    0
)
```

---

## Time Intelligence Measures

### YTD Revenue
```dax
YTD Revenue =
CALCULATE(
    [Total Revenue],
    DATESYTD(monthly_pnl[month])
)
```

### YTD Bookings
```dax
YTD Bookings =
CALCULATE(
    SUM(monthly_bookings[booking_count]),
    DATESYTD(monthly_bookings[month])
)
```

### Last 12 Months Revenue
```dax
L12M Revenue =
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(monthly_pnl[month], MAX(monthly_pnl[month]), -12, MONTH)
)
```

### Same Period Last Year
```dax
SPLY Revenue =
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR(monthly_pnl[month])
)
```

---

## Conditional Formatting Measures

Use these measures for conditional formatting (red/yellow/green indicators):

### Revenue Status
```dax
Revenue Status =
VAR Growth = [Revenue MoM Growth]
RETURN
SWITCH(
    TRUE(),
    Growth >= 10, "Good",
    Growth >= 0, "Okay",
    "Warning"
)
```

### Margin Status
```dax
Margin Status =
VAR Margin = [Gross Margin %]
RETURN
SWITCH(
    TRUE(),
    Margin >= 40, "Good",
    Margin >= 30, "Okay",
    "Warning"
)
```

### Rebook Status
```dax
Rebook Status =
VAR Rate = [Rebook Rate]
RETURN
SWITCH(
    TRUE(),
    Rate <= 10, "Good",
    Rate <= 20, "Okay",
    "Warning"
)
```

### AR Aging Status
```dax
AR Aging Status =
VAR Over90Pct = [AR Over 90 %]
RETURN
SWITCH(
    TRUE(),
    Over90Pct <= 5, "Good",
    Over90Pct <= 15, "Okay",
    "Warning"
)
```

---

## Notes

- All percentage measures return values as percentages (e.g., 45 for 45%)
- Format these measures in PowerBI: Measure tools → Format → Percentage
- For currency measures, use: Measure tools → Format → Currency
- Some measures require specific tables to exist - check your data model

For questions on implementing these measures, refer to the PowerBI setup guide.
