"""
CSI Cargo Dashboard - Configuration
====================================
Central configuration for all dashboard settings, column definitions, and validation rules.

HOW TO MODIFY:
- Add new columns by adding them to the appropriate COLUMNS dictionary
- Change file paths by updating the PATHS dictionary
- Adjust validation rules in the VALIDATION dictionary
- Add new metrics by defining them in metrics_calculator.py

CTO NOTE:
- OMS connection settings are in oms_integration.py
- Database credentials should be stored in environment variables, not here
"""

import os
from pathlib import Path
from datetime import datetime

# =============================================================================
# PATH CONFIGURATION
# =============================================================================

# Base directory (where this project lives)
BASE_DIR = Path(__file__).parent.parent

# Data directories
PATHS = {
    'templates': BASE_DIR / 'data' / 'templates',
    'input': BASE_DIR / 'data' / 'input',
    'output': BASE_DIR / 'data' / 'output',
}

# Input file names (what the user should name their exports)
INPUT_FILES = {
    'financial_transactions': 'financial_transactions.xlsx',
    'cost_classifications': 'cost_classifications.xlsx',
    'booking_log': 'booking_log.xlsx',
    'ar_aging': 'ar_aging.xlsx',
    'ap_aging': 'ap_aging.xlsx',
}

# Output file name (what PowerBI will connect to)
OUTPUT_FILE = 'dashboard_data.xlsx'

# =============================================================================
# COLUMN DEFINITIONS
# =============================================================================
# These define the expected columns for each data file.
# Required columns MUST be present; optional columns will be filled with defaults if missing.

COLUMNS = {
    'financial_transactions': {
        'required': [
            'transaction_id',      # Unique identifier
            'transaction_date',    # Date of transaction
            'transaction_type',    # Invoice, Bill, Payment, etc.
            'category',            # Revenue, COGS, Operating Expense, etc.
            'amount',              # Dollar amount
        ],
        'optional': [
            'subcategory',         # More specific classification
            'description',         # What it's for
            'customer_name',       # Customer (if applicable)
            'vendor_name',         # Vendor (if applicable)
            'payment_status',      # Paid, Pending, Overdue
            'due_date',            # When payment is due
        ],
        'defaults': {
            'subcategory': 'Unclassified',
            'description': '',
            'customer_name': '',
            'vendor_name': '',
            'payment_status': 'Unknown',
            'due_date': None,
        }
    },

    'cost_classifications': {
        'required': [
            'expense_category',    # The category from QuickBooks
            'cost_type',           # Fixed or Variable
        ],
        'optional': [
            'cost_group',          # Grouping for dashboard (Labor, COGS, Overhead)
            'notes',               # Any context
        ],
        'defaults': {
            'cost_group': 'Other',
            'notes': '',
        }
    },

    'booking_log': {
        'required': [
            'booking_id',          # Unique booking reference
            'booking_date',        # When booking was created
            'customer_name',       # Funeral home name
            'total_revenue',       # All revenue from booking
        ],
        'optional': [
            'ship_date',           # When remains were shipped
            'customer_type',       # Corporate, Independent, Other
            'origin_city',         # Origin city
            'origin_state',        # Origin state
            'destination_city',    # Destination city
            'destination_state_country',  # State or country
            'route_type',          # Domestic or International
            'airline',             # Primary carrier
            'shipment_type',       # Whole Body, Cremated Remains
            'published_rate',      # Rate charged to customer
            'csi_cost',            # What CSI paid airline
            'gross_margin',        # published_rate - csi_cost
            'intl_paperwork_fee',  # If applicable
            'other_fees',          # Any other charges
            'was_rebooked',        # Yes/No
            'rebooking_cost',      # If rebooked, what did it cost
            'agent_name',          # Who handled it
        ],
        'defaults': {
            'ship_date': None,
            'customer_type': 'Unknown',
            'origin_city': 'Unknown',
            'origin_state': 'Unknown',
            'destination_city': 'Unknown',
            'destination_state_country': 'Unknown',
            'route_type': 'Unknown',
            'airline': 'Unknown',
            'shipment_type': 'Unknown',
            'published_rate': 0.0,
            'csi_cost': 0.0,
            'gross_margin': 0.0,
            'intl_paperwork_fee': 0.0,
            'other_fees': 0.0,
            'was_rebooked': 'No',
            'rebooking_cost': 0.0,
            'agent_name': 'Unknown',
        }
    },

    'ar_aging': {
        'required': [
            'customer_name',       # Who owes you
            'invoice_number',      # Invoice reference
            'amount',              # Amount owed
        ],
        'optional': [
            'invoice_date',        # When issued
            'due_date',            # When due
            'days_outstanding',    # Days since due
            'aging_bucket',        # Current, 1-30, 31-60, 61-90, 90+
        ],
        'defaults': {
            'invoice_date': None,
            'due_date': None,
            'days_outstanding': 0,
            'aging_bucket': 'Unknown',
        }
    },

    'ap_aging': {
        'required': [
            'vendor_name',         # Who you owe
            'bill_number',         # Bill reference
            'amount',              # Amount owed
        ],
        'optional': [
            'bill_date',           # When received
            'due_date',            # When due
            'days_outstanding',    # Days until/since due
            'aging_bucket',        # Current, 1-30, 31-60, 61-90, 90+
        ],
        'defaults': {
            'bill_date': None,
            'due_date': None,
            'days_outstanding': 0,
            'aging_bucket': 'Unknown',
        }
    },
}

# =============================================================================
# VALIDATION RULES
# =============================================================================

VALIDATION = {
    # Valid values for categorical columns
    'transaction_types': ['Invoice', 'Bill', 'Payment', 'Credit', 'Adjustment', 'Other'],
    'categories': ['Revenue', 'COGS', 'Operating Expense', 'Other Income', 'Other Expense'],
    'cost_types': ['Fixed', 'Variable'],
    'cost_groups': ['Labor', 'COGS', 'Overhead', 'Marketing', 'Technology', 'Other'],
    'customer_types': ['Corporate', 'Independent', 'Other', 'Unknown'],
    'route_types': ['Domestic', 'International', 'Unknown'],
    'shipment_types': ['Whole Body', 'Cremated Remains', 'Unknown'],
    'payment_statuses': ['Paid', 'Pending', 'Overdue', 'Unknown'],
    'yes_no': ['Yes', 'No'],
    'aging_buckets': ['Current', '1-30', '31-60', '61-90', '90+', 'Unknown'],

    # Date range validation (for sanity checks)
    'min_date': datetime(2020, 1, 1),  # No data before 2020
    'max_date': datetime(2030, 12, 31),  # No data after 2030
}

# =============================================================================
# METRIC DEFINITIONS
# =============================================================================
# These define how KPIs are calculated. Used by metrics_calculator.py.

METRICS = {
    # Financial KPIs
    'total_revenue': 'Sum of all revenue transactions',
    'total_expenses': 'Sum of all expense transactions (COGS + Operating)',
    'gross_profit': 'Revenue - COGS',
    'net_profit': 'Revenue - All Expenses',
    'gross_margin_pct': 'Gross Profit / Revenue * 100',
    'net_margin_pct': 'Net Profit / Revenue * 100',

    # Cost Analysis
    'fixed_costs': 'Sum of all fixed cost expenses',
    'variable_costs': 'Sum of all variable cost expenses',
    'fixed_cost_ratio': 'Fixed Costs / Total Expenses * 100',

    # AR/AP
    'total_ar': 'Total accounts receivable',
    'total_ap': 'Total accounts payable',
    'ar_over_90': 'AR amount over 90 days',
    'ap_over_90': 'AP amount over 90 days',
    'net_working_capital': 'AR - AP',

    # Booking KPIs
    'total_bookings': 'Count of all bookings',
    'booking_revenue': 'Sum of booking revenue',
    'avg_booking_value': 'Average revenue per booking',
    'avg_margin_per_booking': 'Average gross margin per booking',
    'margin_percentage': 'Total margin / Total revenue * 100',

    # Rework Analysis
    'rebook_count': 'Number of bookings that were rebooked',
    'rebook_rate': 'Rebook count / Total bookings * 100',
    'total_rebook_cost': 'Sum of all rebooking costs',
    'avg_rebook_cost': 'Average cost per rebooking',
}

# =============================================================================
# DASHBOARD TIME PERIODS
# =============================================================================

TIME_PERIODS = {
    'current_month': 'Current calendar month',
    'last_month': 'Previous calendar month',
    'current_quarter': 'Current calendar quarter',
    'last_quarter': 'Previous calendar quarter',
    'ytd': 'Year to date',
    'last_12_months': 'Rolling 12 months',
    'last_24_months': 'Rolling 24 months',
    'all_time': 'All available data',
}

# =============================================================================
# DISPLAY SETTINGS
# =============================================================================

DISPLAY = {
    'currency_format': '${:,.2f}',
    'percentage_format': '{:.1f}%',
    'number_format': '{:,.0f}',
    'date_format': '%Y-%m-%d',
}

# =============================================================================
# OMS INTEGRATION SETTINGS (CTO: Configure these)
# =============================================================================
# These are placeholders. Update in oms_integration.py when ready.

OMS_CONFIG = {
    'enabled': False,  # Set to True when OMS integration is ready
    'connection_type': 'database',  # 'database' or 'api'
    'refresh_interval_minutes': 60,  # How often to pull from OMS

    # Database settings (if using direct DB connection)
    'database': {
        'host': os.environ.get('OMS_DB_HOST', 'localhost'),
        'port': os.environ.get('OMS_DB_PORT', '5432'),
        'name': os.environ.get('OMS_DB_NAME', 'csi_oms'),
        'user': os.environ.get('OMS_DB_USER', ''),
        'password': os.environ.get('OMS_DB_PASSWORD', ''),
    },

    # API settings (if using API)
    'api': {
        'base_url': os.environ.get('OMS_API_URL', ''),
        'api_key': os.environ.get('OMS_API_KEY', ''),
    },
}
