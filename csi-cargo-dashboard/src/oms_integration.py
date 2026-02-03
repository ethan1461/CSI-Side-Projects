"""
CSI Cargo Dashboard - OMS Integration
======================================
Placeholder module for OMS database/API integration.

CTO: This is your entry point for connecting the dashboard to the OMS platform.

INTEGRATION OPTIONS:

1. DIRECT DATABASE CONNECTION
   - Connect directly to OMS PostgreSQL/MySQL database
   - Query booking, financial, and operational data
   - Recommended for real-time dashboards

2. API INTEGRATION
   - Connect via OMS REST API endpoints
   - Better for security isolation
   - Recommended if OMS has rate limits or needs authentication

3. HYBRID APPROACH
   - Use API for real-time data (current bookings)
   - Use database for historical analytics
   - Best of both worlds

IMPLEMENTATION STEPS:

1. Update config.py with OMS_CONFIG settings
2. Implement the data fetching functions below
3. Update run_dashboard.py to use OMS data when available
4. Test with sample data before going live

SECURITY NOTES:
- Store credentials in environment variables, NOT in code
- Use read-only database users for analytics
- Implement connection pooling for production
"""

import pandas as pd
from typing import Dict, Optional
from datetime import datetime, timedelta

from .config import OMS_CONFIG


class OMSConnectionError(Exception):
    """Raised when OMS connection fails."""
    pass


def is_oms_enabled() -> bool:
    """Check if OMS integration is configured and enabled."""
    return OMS_CONFIG.get('enabled', False)


def get_oms_connection():
    """
    Establish connection to OMS database.

    CTO: Implement this based on your OMS database type.

    Example for PostgreSQL:
    ```
    import psycopg2
    from psycopg2 import pool

    connection_pool = psycopg2.pool.SimpleConnectionPool(
        1, 10,
        host=OMS_CONFIG['database']['host'],
        port=OMS_CONFIG['database']['port'],
        database=OMS_CONFIG['database']['name'],
        user=OMS_CONFIG['database']['user'],
        password=OMS_CONFIG['database']['password']
    )
    return connection_pool.getconn()
    ```

    Example for MySQL:
    ```
    import pymysql

    connection = pymysql.connect(
        host=OMS_CONFIG['database']['host'],
        port=int(OMS_CONFIG['database']['port']),
        database=OMS_CONFIG['database']['name'],
        user=OMS_CONFIG['database']['user'],
        password=OMS_CONFIG['database']['password']
    )
    return connection
    ```
    """
    raise NotImplementedError(
        "OMS database connection not implemented. "
        "CTO: Please implement get_oms_connection() in oms_integration.py"
    )


def fetch_bookings_from_oms(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> pd.DataFrame:
    """
    Fetch booking data from OMS.

    CTO: Implement this query based on your OMS schema.

    Args:
        start_date: Start of date range (default: 24 months ago)
        end_date: End of date range (default: today)

    Returns:
        DataFrame with booking data matching the booking_log schema

    Expected columns (map your OMS columns to these):
        - booking_id
        - booking_date
        - ship_date
        - customer_name
        - customer_type
        - origin_city
        - origin_state
        - destination_city
        - destination_state_country
        - route_type
        - airline
        - shipment_type
        - published_rate
        - csi_cost
        - gross_margin
        - intl_paperwork_fee
        - other_fees
        - total_revenue
        - was_rebooked
        - rebooking_cost
        - agent_name

    Example implementation:
    ```
    if start_date is None:
        start_date = datetime.now() - timedelta(days=730)
    if end_date is None:
        end_date = datetime.now()

    query = '''
        SELECT
            b.id as booking_id,
            b.created_at as booking_date,
            b.ship_date,
            c.name as customer_name,
            c.type as customer_type,
            b.origin_city,
            b.origin_state,
            b.destination_city,
            b.destination_state_country,
            CASE WHEN b.is_international THEN 'International' ELSE 'Domestic' END as route_type,
            a.name as airline,
            b.shipment_type,
            b.published_rate,
            b.csi_cost,
            b.published_rate - b.csi_cost as gross_margin,
            b.intl_paperwork_fee,
            b.other_fees,
            b.total_revenue,
            CASE WHEN b.rebooked_count > 0 THEN 'Yes' ELSE 'No' END as was_rebooked,
            b.rebooking_cost,
            u.name as agent_name
        FROM bookings b
        JOIN customers c ON b.customer_id = c.id
        JOIN airlines a ON b.airline_id = a.id
        JOIN users u ON b.agent_id = u.id
        WHERE b.created_at BETWEEN %s AND %s
        ORDER BY b.created_at
    '''

    conn = get_oms_connection()
    df = pd.read_sql(query, conn, params=[start_date, end_date])
    conn.close()
    return df
    ```
    """
    raise NotImplementedError(
        "OMS booking fetch not implemented. "
        "CTO: Please implement fetch_bookings_from_oms() in oms_integration.py"
    )


def fetch_financial_data_from_oms(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> pd.DataFrame:
    """
    Fetch financial transaction data from OMS (if OMS tracks this).

    CTO: If financial data lives in QuickBooks only, you may want to:
    1. Build a QuickBooks API integration instead
    2. Continue using Excel exports for financial data
    3. Set up a data warehouse that combines OMS + QuickBooks

    Args:
        start_date: Start of date range
        end_date: End of date range

    Returns:
        DataFrame with financial data matching the financial_transactions schema

    Expected columns:
        - transaction_id
        - transaction_date
        - transaction_type
        - category
        - subcategory
        - description
        - customer_name
        - vendor_name
        - amount
        - payment_status
        - due_date
    """
    raise NotImplementedError(
        "OMS financial data fetch not implemented. "
        "CTO: Implement if OMS tracks financial data, otherwise use QuickBooks exports."
    )


def fetch_ar_aging_from_oms() -> pd.DataFrame:
    """
    Fetch current AR aging from OMS or accounting system.

    CTO: This likely needs to come from QuickBooks or your accounting system,
    not OMS. Consider:
    1. QuickBooks API integration
    2. Scheduled export + file pickup
    3. Data warehouse approach
    """
    raise NotImplementedError(
        "AR aging fetch not implemented. "
        "CTO: Implement QuickBooks integration or continue using exports."
    )


def fetch_ap_aging_from_oms() -> pd.DataFrame:
    """
    Fetch current AP aging from OMS or accounting system.

    CTO: Same as AR - likely needs QuickBooks integration.
    """
    raise NotImplementedError(
        "AP aging fetch not implemented. "
        "CTO: Implement QuickBooks integration or continue using exports."
    )


def load_all_data_from_oms() -> Dict[str, pd.DataFrame]:
    """
    Load all data from OMS, falling back to file-based loading where needed.

    CTO: This is the main entry point. Customize which data sources
    come from OMS vs files.

    Returns:
        Dictionary of DataFrames matching the expected schema
    """
    if not is_oms_enabled():
        raise OMSConnectionError("OMS integration is not enabled in config.")

    data = {}

    # Try to load bookings from OMS
    try:
        data['booking_log'] = fetch_bookings_from_oms()
        print("  Loaded booking data from OMS")
    except NotImplementedError:
        print("  [INFO] Booking data: Using file-based loading (OMS not implemented)")
        data['booking_log'] = None

    # Financial data - likely from QuickBooks, not OMS
    try:
        data['financial_transactions'] = fetch_financial_data_from_oms()
        print("  Loaded financial data from OMS")
    except NotImplementedError:
        print("  [INFO] Financial data: Using file-based loading")
        data['financial_transactions'] = None

    # AR/AP - likely from QuickBooks
    try:
        data['ar_aging'] = fetch_ar_aging_from_oms()
        print("  Loaded AR aging from OMS")
    except NotImplementedError:
        print("  [INFO] AR aging: Using file-based loading")
        data['ar_aging'] = None

    try:
        data['ap_aging'] = fetch_ap_aging_from_oms()
        print("  Loaded AP aging from OMS")
    except NotImplementedError:
        print("  [INFO] AP aging: Using file-based loading")
        data['ap_aging'] = None

    # Cost classifications - typically static, file-based is fine
    data['cost_classifications'] = None

    return data


# =============================================================================
# QUICKBOOKS INTEGRATION (FUTURE)
# =============================================================================

def fetch_from_quickbooks_api(endpoint: str) -> pd.DataFrame:
    """
    CTO: Placeholder for QuickBooks API integration.

    QuickBooks Online API docs: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities

    You'll need:
    1. QuickBooks developer account
    2. OAuth 2.0 credentials
    3. Company ID

    Example endpoints:
    - /query?query=select * from Invoice
    - /query?query=select * from Bill
    - /query?query=select * from Account

    Consider using the python-quickbooks library:
    pip install python-quickbooks
    """
    raise NotImplementedError("QuickBooks API integration not implemented")


# =============================================================================
# REAL-TIME DATA HOOKS (FUTURE)
# =============================================================================

def get_live_booking_count() -> int:
    """
    CTO: Get real-time count of today's bookings.

    Useful for live dashboards.
    """
    raise NotImplementedError("Live booking count not implemented")


def get_pending_bookings() -> pd.DataFrame:
    """
    CTO: Get list of bookings in progress.

    Useful for operations dashboard.
    """
    raise NotImplementedError("Pending bookings query not implemented")


def subscribe_to_booking_updates(callback):
    """
    CTO: Subscribe to real-time booking updates.

    For truly real-time dashboards, consider:
    1. WebSocket connection to OMS
    2. Database change data capture (CDC)
    3. Message queue (RabbitMQ, Redis pub/sub)
    """
    raise NotImplementedError("Real-time subscriptions not implemented")
