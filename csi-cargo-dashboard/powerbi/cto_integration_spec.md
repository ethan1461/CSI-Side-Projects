# CTO Integration Specification

This document outlines how to integrate the CSI Cargo Dashboard with the OMS platform and other data sources.

---

## Current Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     CURRENT STATE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   QuickBooks ──► Excel Export ──► data/input/ ──┐              │
│                                                  │              │
│   Manual Booking ──► Excel ──► data/input/ ─────┼──► Python    │
│   Records                                        │    Processor │
│                                                  │              │
│   (Future) OMS ─────────────────────────────────┘      │       │
│                                                        │       │
│                                                        ▼       │
│                                              data/output/      │
│                                              dashboard_data.xlsx│
│                                                        │       │
│                                                        ▼       │
│                                                   PowerBI      │
│                                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Target Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     TARGET STATE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐      │
│   │  QuickBooks │     │    OMS      │     │   Other     │      │
│   │    API      │     │  Database   │     │   Sources   │      │
│   └──────┬──────┘     └──────┬──────┘     └──────┬──────┘      │
│          │                   │                   │              │
│          └───────────────────┼───────────────────┘              │
│                              │                                  │
│                              ▼                                  │
│                    ┌─────────────────┐                         │
│                    │  ETL Pipeline   │                         │
│                    │  (Python/Airflow)│                         │
│                    └────────┬────────┘                         │
│                             │                                   │
│          ┌──────────────────┼──────────────────┐               │
│          │                  │                  │               │
│          ▼                  ▼                  ▼               │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐         │
│   │   Data      │   │   PowerBI   │   │   Real-time │         │
│   │   Warehouse │   │   Direct    │   │   Alerts    │         │
│   │   (Postgres)│   │   Query     │   │   (Slack?)  │         │
│   └─────────────┘   └─────────────┘   └─────────────┘         │
│                                                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Integration Points

### 1. OMS Database Connection

**Location:** `src/oms_integration.py`

**What to implement:**

```python
def get_oms_connection():
    """
    Returns a database connection to OMS.

    Implementation depends on your database type:
    - PostgreSQL: Use psycopg2
    - MySQL: Use pymysql
    - SQL Server: Use pyodbc
    """
```

**Required environment variables:**

```bash
export OMS_DB_HOST=your-database-host
export OMS_DB_PORT=5432
export OMS_DB_NAME=csi_oms
export OMS_DB_USER=dashboard_readonly
export OMS_DB_PASSWORD=your-secure-password
```

**Security requirements:**
- Create a **read-only database user** for the dashboard
- Never use the application's write credentials
- Use SSL/TLS for database connections
- Store credentials in environment variables or secrets manager

### 2. Booking Data Query

**Location:** `src/oms_integration.py` → `fetch_bookings_from_oms()`

**Required mapping:**

Map your OMS schema to the dashboard schema:

| Dashboard Column | OMS Table.Column | Notes |
|-----------------|------------------|-------|
| booking_id | bookings.id | Unique identifier |
| booking_date | bookings.created_at | When booking was created |
| ship_date | bookings.ship_date | Actual ship date |
| customer_name | customers.name | Join on customer_id |
| customer_type | customers.type | Corporate/Independent/Other |
| origin_city | bookings.origin_city | |
| origin_state | bookings.origin_state | |
| destination_city | bookings.destination_city | |
| destination_state_country | bookings.destination_state | Or country for intl |
| route_type | DERIVED | Domestic if US, else International |
| airline | airlines.name | Join on airline_id |
| shipment_type | bookings.shipment_type | Whole Body/Cremated |
| published_rate | bookings.customer_rate | What customer paid |
| csi_cost | bookings.carrier_cost | What CSI paid carrier |
| gross_margin | DERIVED | published_rate - csi_cost |
| intl_paperwork_fee | bookings.paperwork_fee | |
| other_fees | bookings.other_fees | |
| total_revenue | DERIVED | Sum of all revenue |
| was_rebooked | DERIVED | rebook_count > 0 |
| rebooking_cost | bookings.rebooking_cost | |
| agent_name | users.name | Join on agent_id |

**Example SQL:**

```sql
SELECT
    b.id as booking_id,
    b.created_at as booking_date,
    b.ship_date,
    c.name as customer_name,
    c.customer_type,
    b.origin_city,
    b.origin_state,
    b.destination_city,
    COALESCE(b.destination_country, b.destination_state) as destination_state_country,
    CASE
        WHEN b.destination_country IS NULL OR b.destination_country = 'US'
        THEN 'Domestic'
        ELSE 'International'
    END as route_type,
    a.name as airline,
    b.shipment_type,
    b.customer_rate as published_rate,
    b.carrier_cost as csi_cost,
    b.customer_rate - b.carrier_cost as gross_margin,
    COALESCE(b.paperwork_fee, 0) as intl_paperwork_fee,
    COALESCE(b.other_fees, 0) as other_fees,
    b.customer_rate + COALESCE(b.paperwork_fee, 0) + COALESCE(b.other_fees, 0) as total_revenue,
    CASE WHEN b.rebook_count > 0 THEN 'Yes' ELSE 'No' END as was_rebooked,
    COALESCE(b.rebooking_cost, 0) as rebooking_cost,
    u.name as agent_name
FROM bookings b
LEFT JOIN customers c ON b.customer_id = c.id
LEFT JOIN airlines a ON b.airline_id = a.id
LEFT JOIN users u ON b.agent_id = u.id
WHERE b.created_at >= %(start_date)s
  AND b.created_at <= %(end_date)s
  AND b.status != 'cancelled'
ORDER BY b.created_at;
```

### 3. QuickBooks Integration (Optional)

**Recommended approach:** QuickBooks API

**Library:** `python-quickbooks`

```bash
pip install python-quickbooks
```

**Required credentials:**
- QuickBooks developer account
- OAuth 2.0 client ID and secret
- Company ID

**Implementation location:** Create new file `src/quickbooks_integration.py`

**Endpoints to query:**
- Invoice: Revenue transactions
- Bill: Expense transactions
- Payment: Cash receipts
- Account: Chart of accounts

**Alternative:** Continue using manual Excel exports from QuickBooks

### 4. PowerBI Direct Query (Advanced)

Instead of Excel output, you can configure PowerBI to query directly.

**Option A: PostgreSQL Direct Connect**
1. In PowerBI: Get Data → PostgreSQL
2. Enter OMS database credentials
3. Write DirectQuery SQL

**Option B: Python Script in PowerBI**
1. In PowerBI: Get Data → Python script
2. Paste the data loading code
3. PowerBI executes Python and loads data

**Option C: PowerBI Dataflows**
1. Create Dataflow in PowerBI Service
2. Connect to multiple sources
3. Transform and combine data
4. Dashboard connects to Dataflow

---

## Recommended Implementation Plan

### Phase 1: OMS Read Integration (Week 1-2)

**Goal:** Replace `booking_log.xlsx` with live OMS data

**Steps:**
1. Create read-only database user in OMS
2. Implement `get_oms_connection()` in `oms_integration.py`
3. Implement `fetch_bookings_from_oms()` with proper schema mapping
4. Test with `python scripts/run_dashboard.py`
5. Verify data matches manual exports

**Validation:**
```python
# Run this to compare OMS vs manual data
import pandas as pd
oms_data = fetch_bookings_from_oms()
manual_data = pd.read_excel('data/input/booking_log.xlsx')
# Compare row counts, totals, date ranges
```

### Phase 2: Automated Refresh (Week 3)

**Goal:** Dashboard updates automatically without manual exports

**Options:**

**Option A: Cron Job**
```bash
# Add to crontab (runs daily at 6 AM)
0 6 * * * cd /path/to/csi-cargo-dashboard && python scripts/run_dashboard.py
```

**Option B: Windows Task Scheduler**
1. Create batch file: `run_dashboard.bat`
2. Schedule daily execution

**Option C: Airflow DAG (if you have Airflow)**
```python
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG('csi_dashboard_refresh', schedule_interval='0 6 * * *')

refresh_task = BashOperator(
    task_id='refresh_dashboard',
    bash_command='cd /path/to/dashboard && python scripts/run_dashboard.py',
    dag=dag
)
```

### Phase 3: Financial Data Integration (Week 4-5)

**Goal:** Replace QuickBooks Excel exports with automated data

**Options:**
1. QuickBooks API integration
2. Scheduled QuickBooks export + file pickup
3. Data warehouse (combine OMS + QuickBooks)

**Recommendation:** Start with scheduled exports, move to API later

### Phase 4: Real-Time Dashboards (Future)

**Goal:** Live updating dashboards without refresh

**Architecture:**
1. OMS sends events to message queue (Redis/RabbitMQ)
2. Dashboard service consumes events
3. PowerBI connects via streaming dataset

**Alternative:** PowerBI Premium with DirectQuery mode

---

## Data Model Reference

### Expected Tables in Dashboard

| Table | Source | Update Frequency |
|-------|--------|------------------|
| financial_transactions | QuickBooks | Weekly |
| cost_classifications | Manual | Monthly (static) |
| booking_log | OMS | Daily |
| ar_aging | QuickBooks | Weekly |
| ap_aging | QuickBooks | Weekly |

### Calculated Tables (Generated by Python)

| Table | Description |
|-------|-------------|
| executive_summary | High-level KPIs |
| financial_summary | Category breakdown |
| cost_analysis | Fixed vs variable |
| monthly_pnl | Monthly P&L |
| ar_summary | AR by aging bucket |
| ap_summary | AP by aging bucket |
| booking_summary | Booking totals |
| booking_by_* | Various breakdowns |
| rework_analysis | Rebooking patterns |
| agent_productivity | Agent metrics |
| carrier_performance | Airline metrics |
| *_metrics | Time series data |

---

## Security Checklist

- [ ] Database user is read-only
- [ ] Credentials stored in environment variables
- [ ] No credentials in code or config files
- [ ] SSL enabled for database connections
- [ ] API keys rotated regularly
- [ ] Access logs monitored
- [ ] PowerBI workspace has appropriate permissions

---

## Testing Checklist

Before going live with OMS integration:

- [ ] Data counts match between OMS and manual exports
- [ ] Revenue totals match
- [ ] Date ranges are correct
- [ ] All required columns are populated
- [ ] NULL handling is correct
- [ ] Character encoding is correct (especially customer names)
- [ ] Timezone handling is correct
- [ ] Historical data loads correctly (24+ months)
- [ ] Performance is acceptable (< 30 seconds for full load)

---

## Monitoring & Alerts

### Recommended Monitoring

1. **Data freshness:** Alert if dashboard data is > 24 hours old
2. **Row count anomalies:** Alert if booking count drops significantly
3. **Revenue anomalies:** Alert if daily revenue is outside normal range
4. **Script failures:** Alert if `run_dashboard.py` exits with error

### Implementation with Python

```python
# Add to run_dashboard.py
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message):
    # Configure your email/Slack/Teams webhook here
    pass

# After processing
if validation_result.errors:
    send_alert("Dashboard Error", validation_result.summary())
```

---

## Contact

For questions about this integration:
- **Dashboard Logic:** Review `src/metrics_calculator.py`
- **Data Validation:** Review `src/data_validator.py`
- **OMS Connection:** Review `src/oms_integration.py`

---

## Appendix: Environment Setup

### Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OMS_DB_HOST=localhost
export OMS_DB_PORT=5432
export OMS_DB_NAME=csi_oms_dev
export OMS_DB_USER=dashboard_dev
export OMS_DB_PASSWORD=dev_password

# Run dashboard
python scripts/run_dashboard.py
```

### Production Environment

```bash
# Use production credentials (from secrets manager)
export OMS_DB_HOST=prod-db.csi.internal
export OMS_DB_PORT=5432
export OMS_DB_NAME=csi_oms
export OMS_DB_USER=dashboard_readonly
export OMS_DB_PASSWORD=$(aws secretsmanager get-secret-value --secret-id csi/dashboard/db)

# Run with logging
python scripts/run_dashboard.py 2>&1 | tee -a /var/log/csi-dashboard.log
```
