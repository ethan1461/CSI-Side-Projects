# CSI Cargo Sales Dashboard

A comprehensive executive dashboard for tracking KPIs, financial performance, and booking analytics at Cargo Sales International.

## Overview

This dashboard provides:
- **Executive Summary**: High-level KPIs for CEO visibility
- **Financial Deep Dive**: Granular P&L, cost analysis (fixed vs variable), AP/AR aging
- **Growth Analytics**: Booking revenue by route, airline, customer, geography
- **Operations Insights**: Rework costs, agent productivity, carrier reliability

## Quick Start (For Non-Developers)

### Step 1: Install Python (One-Time Setup)

1. Download Python from https://www.python.org/downloads/
2. During installation, **CHECK THE BOX** that says "Add Python to PATH"
3. Restart your computer after installation

### Step 2: Install Required Tools (One-Time Setup)

1. Open Command Prompt (Windows) or Terminal (Mac)
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac: Press `Cmd + Space`, type `Terminal`, press Enter

2. Navigate to this folder:
   ```
   cd /home/user/CSI-Side-Projects/csi-cargo-dashboard
   ```

3. Run the setup command:
   ```
   pip install -r requirements.txt
   ```

### Step 3: Add Your Data

1. Get the data exports from your CFO (see "Data Requirements" below)
2. Save each export as an Excel file in the `data/input/` folder:
   - `financial_transactions.xlsx`
   - `cost_classifications.xlsx`
   - `booking_log.xlsx`
   - `ar_aging.xlsx`
   - `ap_aging.xlsx`

### Step 4: Process the Data

1. Open Command Prompt/Terminal
2. Navigate to this folder:
   ```
   cd /home/user/CSI-Side-Projects/csi-cargo-dashboard
   ```
3. Run the dashboard processor:
   ```
   python scripts/run_dashboard.py
   ```
4. Check `data/output/` for the processed files

### Step 5: Open in PowerBI

1. Open PowerBI Desktop
2. Click "Get Data" → "Excel"
3. Select `data/output/dashboard_data.xlsx`
4. Follow the PowerBI setup guide in `powerbi/setup_guide.md`

---

## Data Requirements

### Export 1: Financial Transactions (`financial_transactions.xlsx`)
From QuickBooks - all transactions for the past 24-36 months.

Required columns:
| Column | Description | Example |
|--------|-------------|---------|
| transaction_id | Unique ID | INV-2024-001 |
| transaction_date | Date | 2024-01-15 |
| transaction_type | Invoice, Bill, Payment, etc. | Invoice |
| category | Revenue, COGS, Operating Expense | Revenue |
| subcategory | Specific type | Air Freight Revenue |
| description | Details | Booking #1234 - LAX to JFK |
| customer_name | Customer (if applicable) | Smith Funeral Home |
| vendor_name | Vendor (if applicable) | American Airlines |
| amount | Dollar amount | 1250.00 |
| payment_status | Paid, Pending, Overdue | Pending |
| due_date | Payment due date | 2024-02-15 |

### Export 2: Cost Classifications (`cost_classifications.xlsx`)
A reference table mapping expenses to fixed/variable.

Required columns:
| Column | Description | Example |
|--------|-------------|---------|
| expense_category | Category from QuickBooks | Payroll |
| cost_type | Fixed or Variable | Fixed |
| cost_group | Grouping | Labor |
| notes | Context | Includes benefits |

### Export 3: Booking Log (`booking_log.xlsx`)
Detailed booking data - this is the most important file for growth analytics.

Required columns:
| Column | Description | Example |
|--------|-------------|---------|
| booking_id | Unique booking reference | CSI-2024-0542 |
| booking_date | When created | 2024-01-15 |
| ship_date | When shipped | 2024-01-17 |
| customer_name | Funeral home | Smith Funeral Home |
| customer_type | Corporate, Independent, Other | Independent |
| origin_city | Origin | Los Angeles |
| origin_state | State | CA |
| destination_city | Destination | New York |
| destination_state_country | State or country | NY |
| route_type | Domestic or International | Domestic |
| airline | Carrier | American Airlines |
| shipment_type | Whole Body, Cremated Remains | Whole Body |
| published_rate | Rate to customer | 1500.00 |
| csi_cost | What CSI paid | 900.00 |
| gross_margin | Difference | 600.00 |
| intl_paperwork_fee | If applicable | 0.00 |
| other_fees | Other charges | 0.00 |
| total_revenue | All revenue | 1500.00 |
| was_rebooked | Yes/No | No |
| rebooking_cost | If rebooked | 0.00 |
| agent_name | Handler | Maya |

### Export 4: AR Aging (`ar_aging.xlsx`)
Current accounts receivable aging.

Required columns:
| Column | Description |
|--------|-------------|
| customer_name | Who owes you |
| invoice_number | Reference |
| invoice_date | When issued |
| due_date | When due |
| amount | Amount owed |
| days_outstanding | Days since due |
| aging_bucket | Current, 1-30, 31-60, 61-90, 90+ |

### Export 5: AP Aging (`ap_aging.xlsx`)
Current accounts payable aging.

Required columns:
| Column | Description |
|--------|-------------|
| vendor_name | Who you owe |
| bill_number | Reference |
| bill_date | When received |
| due_date | When due |
| amount | Amount owed |
| days_outstanding | Days until/since due |
| aging_bucket | Current, 1-30, 31-60, 61-90, 90+ |

---

## File Structure

```
csi-cargo-dashboard/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── data/
│   ├── templates/           # Blank templates with headers
│   ├── input/               # Put your data exports here
│   └── output/              # Processed data for PowerBI
├── src/
│   ├── config.py            # Settings and configuration
│   ├── data_loader.py       # Loads data from files
│   ├── data_validator.py    # Validates and cleans data
│   ├── metrics_calculator.py # Calculates all KPIs
│   └── oms_integration.py   # [CTO] OMS connection placeholder
├── powerbi/
│   ├── setup_guide.md       # How to build the PowerBI dashboard
│   ├── dax_measures.md      # All DAX formulas
│   └── data_model.md        # Data relationships
└── scripts/
    └── run_dashboard.py     # Main script to run
```

---

## Updating the Dashboard

### Weekly Update Process (5-10 minutes)

1. Export fresh data from QuickBooks
2. Replace files in `data/input/` with new exports
3. Run: `python scripts/run_dashboard.py`
4. Open PowerBI and click "Refresh"

---

## Troubleshooting

### "Python is not recognized"
- Reinstall Python and make sure to check "Add to PATH"
- Restart your computer

### "Module not found" error
- Run: `pip install -r requirements.txt`

### "File not found" error
- Check that your data files are in `data/input/`
- Check that file names match exactly (case-sensitive)

### Data validation errors
- The script will tell you exactly which column is missing or malformed
- Check your export against the required columns listed above

---

## For CTO: Integration Points

See `powerbi/cto_integration_spec.md` for:
- OMS database connection setup
- API endpoint integration
- Automated data pipeline design
- Real-time refresh architecture

The `src/oms_integration.py` file contains placeholder functions ready for your implementation.

---

## Support

For questions or issues:
- Check the troubleshooting section above
- Review error messages - they're designed to be helpful
- Contact your CTO for technical integration issues
