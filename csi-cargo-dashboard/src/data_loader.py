"""
CSI Cargo Dashboard - Data Loader
=================================
Handles loading data from various sources (Excel files, and eventually OMS).

HOW IT WORKS:
1. Looks for Excel files in the data/input/ folder
2. Reads each file and validates the column headers
3. Fills in missing optional columns with default values
4. Returns clean DataFrames ready for processing

CTO NOTE:
- See oms_integration.py for database/API data loading
- This module focuses on file-based loading
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Optional, Tuple
from datetime import datetime

from .config import (
    PATHS,
    INPUT_FILES,
    COLUMNS,
)


class DataLoadError(Exception):
    """Raised when there's a problem loading data."""
    pass


def load_all_data() -> Dict[str, pd.DataFrame]:
    """
    Load all data files from the input directory.

    Returns:
        Dictionary with keys matching INPUT_FILES and DataFrames as values.
        Missing files will have None as their value.

    Raises:
        DataLoadError: If a critical file is missing or unreadable.
    """
    print("\n" + "=" * 60)
    print("LOADING DATA FILES")
    print("=" * 60)

    data = {}
    errors = []
    warnings = []

    for file_key, file_name in INPUT_FILES.items():
        file_path = PATHS['input'] / file_name

        print(f"\nLoading: {file_name}...")

        if not file_path.exists():
            # Check if it's a required file or optional
            if file_key in ['financial_transactions', 'booking_log']:
                errors.append(f"MISSING REQUIRED FILE: {file_name}")
                errors.append(f"  Expected location: {file_path}")
                data[file_key] = None
            else:
                warnings.append(f"Optional file not found: {file_name}")
                data[file_key] = None
            continue

        try:
            # Load the Excel file
            df = pd.read_excel(file_path, engine='openpyxl')

            # Standardize column names (lowercase, strip whitespace)
            df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

            # Validate and fill columns
            df, file_warnings = validate_and_fill_columns(df, file_key)
            warnings.extend(file_warnings)

            data[file_key] = df
            print(f"  SUCCESS: Loaded {len(df)} rows")

        except Exception as e:
            errors.append(f"ERROR reading {file_name}: {str(e)}")
            data[file_key] = None

    # Print summary
    print("\n" + "-" * 60)

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        raise DataLoadError(
            "\n\nData loading failed. Please fix the errors above and try again."
        )

    print("\nAll data files loaded successfully!")
    return data


def validate_and_fill_columns(
    df: pd.DataFrame,
    file_key: str
) -> Tuple[pd.DataFrame, list]:
    """
    Validate that required columns exist and fill optional columns with defaults.

    Args:
        df: The DataFrame to validate
        file_key: Which file type this is (from INPUT_FILES keys)

    Returns:
        Tuple of (validated DataFrame, list of warnings)
    """
    warnings = []
    column_spec = COLUMNS.get(file_key, {})

    required = column_spec.get('required', [])
    optional = column_spec.get('optional', [])
    defaults = column_spec.get('defaults', {})

    # Check required columns
    missing_required = [col for col in required if col not in df.columns]
    if missing_required:
        raise DataLoadError(
            f"Missing required columns in {INPUT_FILES[file_key]}: {missing_required}\n"
            f"Found columns: {list(df.columns)}"
        )

    # Add optional columns with defaults if missing
    for col in optional:
        if col not in df.columns:
            default_value = defaults.get(col, None)
            df[col] = default_value
            warnings.append(
                f"  Added missing optional column '{col}' with default: {default_value}"
            )

    return df, warnings


def load_single_file(file_key: str) -> Optional[pd.DataFrame]:
    """
    Load a single data file.

    Args:
        file_key: Which file to load (from INPUT_FILES keys)

    Returns:
        DataFrame or None if file doesn't exist
    """
    file_name = INPUT_FILES.get(file_key)
    if not file_name:
        raise DataLoadError(f"Unknown file key: {file_key}")

    file_path = PATHS['input'] / file_name

    if not file_path.exists():
        return None

    df = pd.read_excel(file_path, engine='openpyxl')
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    df, _ = validate_and_fill_columns(df, file_key)

    return df


def create_sample_data() -> Dict[str, pd.DataFrame]:
    """
    Create sample data for testing the dashboard.
    This generates realistic fake data to demonstrate functionality.

    Used when no real data is available.
    """
    import numpy as np
    from datetime import timedelta

    print("\nGenerating sample data for testing...")

    # Date range for sample data (24 months)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730)  # ~24 months

    np.random.seed(42)  # For reproducibility

    # Sample financial transactions
    n_transactions = 500
    dates = pd.date_range(start=start_date, end=end_date, periods=n_transactions)

    transaction_types = ['Invoice', 'Bill', 'Payment']
    categories = ['Revenue', 'COGS', 'Operating Expense']
    customers = [
        'Smith Funeral Home', 'Johnson Memorial', 'Heritage Mortuary',
        'Dignity Memorial - LA', 'Dignity Memorial - NYC', 'Oak Grove Funeral',
        'Peaceful Rest Chapel', 'Memorial Gardens', 'Eternal Peace Funeral'
    ]
    vendors = [
        'American Airlines', 'United Airlines', 'Delta Air Lines',
        'Southwest Airlines', 'Alaska Airlines', 'Bergen Funeral Services'
    ]

    financial_transactions = pd.DataFrame({
        'transaction_id': [f'TXN-{i:05d}' for i in range(n_transactions)],
        'transaction_date': dates,
        'transaction_type': np.random.choice(transaction_types, n_transactions),
        'category': np.random.choice(categories, n_transactions, p=[0.4, 0.35, 0.25]),
        'subcategory': ['Air Freight'] * n_transactions,
        'description': ['Sample transaction'] * n_transactions,
        'customer_name': np.random.choice(customers + [''], n_transactions),
        'vendor_name': np.random.choice(vendors + [''], n_transactions),
        'amount': np.random.uniform(500, 5000, n_transactions).round(2),
        'payment_status': np.random.choice(['Paid', 'Pending', 'Overdue'], n_transactions, p=[0.7, 0.2, 0.1]),
        'due_date': dates + timedelta(days=30),
    })

    # Adjust amounts based on category (expenses should be negative conceptually, but we track as positive)

    # Sample cost classifications
    cost_classifications = pd.DataFrame({
        'expense_category': [
            'Payroll - Agents', 'Payroll - Leadership', 'Airline Freight Costs',
            'Office Rent', 'Software Subscriptions', 'Translation Services',
            'Rebooking Fees', 'Marketing', 'Insurance', 'Utilities'
        ],
        'cost_type': [
            'Fixed', 'Fixed', 'Variable',
            'Fixed', 'Fixed', 'Variable',
            'Variable', 'Variable', 'Fixed', 'Fixed'
        ],
        'cost_group': [
            'Labor', 'Labor', 'COGS',
            'Overhead', 'Technology', 'COGS',
            'COGS', 'Marketing', 'Overhead', 'Overhead'
        ],
        'notes': [''] * 10,
    })

    # Sample booking log
    n_bookings = 300
    booking_dates = pd.date_range(start=start_date, end=end_date, periods=n_bookings)

    cities = ['Los Angeles', 'New York', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Denver', 'Seattle']
    states = ['CA', 'NY', 'IL', 'TX', 'AZ', 'FL', 'CO', 'WA']
    airlines = ['American Airlines', 'United Airlines', 'Delta Air Lines', 'Southwest Airlines']
    agents = ['Maya', 'Abe', 'Sue', 'Renee']

    published_rates = np.random.uniform(1200, 3500, n_bookings).round(2)
    discount_pcts = np.random.uniform(0.30, 0.60, n_bookings)  # 30-60% discount
    csi_costs = (published_rates * (1 - discount_pcts)).round(2)
    gross_margins = published_rates - csi_costs

    was_rebooked = np.random.choice(['Yes', 'No'], n_bookings, p=[0.15, 0.85])
    rebooking_costs = np.where(was_rebooked == 'Yes', np.random.uniform(100, 500, n_bookings), 0).round(2)

    booking_log = pd.DataFrame({
        'booking_id': [f'CSI-{d.year}-{i:04d}' for i, d in enumerate(booking_dates)],
        'booking_date': booking_dates,
        'ship_date': booking_dates + timedelta(days=2),
        'customer_name': np.random.choice(customers, n_bookings),
        'customer_type': np.random.choice(['Corporate', 'Independent', 'Other'], n_bookings, p=[0.3, 0.6, 0.1]),
        'origin_city': np.random.choice(cities, n_bookings),
        'origin_state': np.random.choice(states, n_bookings),
        'destination_city': np.random.choice(cities, n_bookings),
        'destination_state_country': np.random.choice(states + ['Mexico', 'Canada', 'UK'], n_bookings),
        'route_type': np.random.choice(['Domestic', 'International'], n_bookings, p=[0.75, 0.25]),
        'airline': np.random.choice(airlines, n_bookings),
        'shipment_type': np.random.choice(['Whole Body', 'Cremated Remains'], n_bookings, p=[0.7, 0.3]),
        'published_rate': published_rates,
        'csi_cost': csi_costs,
        'gross_margin': gross_margins,
        'intl_paperwork_fee': np.where(
            np.random.random(n_bookings) > 0.75,
            np.random.uniform(200, 800, n_bookings),
            0
        ).round(2),
        'other_fees': np.random.choice([0, 50, 100, 150], n_bookings, p=[0.7, 0.1, 0.1, 0.1]),
        'total_revenue': published_rates,  # Will be recalculated
        'was_rebooked': was_rebooked,
        'rebooking_cost': rebooking_costs,
        'agent_name': np.random.choice(agents, n_bookings),
    })

    # Recalculate total revenue
    booking_log['total_revenue'] = (
        booking_log['published_rate'] +
        booking_log['intl_paperwork_fee'] +
        booking_log['other_fees']
    )

    # Sample AR aging
    ar_aging = pd.DataFrame({
        'customer_name': np.random.choice(customers, 25),
        'invoice_number': [f'INV-{i:04d}' for i in range(25)],
        'invoice_date': pd.date_range(end=end_date - timedelta(days=30), periods=25),
        'due_date': pd.date_range(end=end_date, periods=25),
        'amount': np.random.uniform(500, 5000, 25).round(2),
        'days_outstanding': np.random.choice([0, 15, 35, 65, 100], 25, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
        'aging_bucket': np.random.choice(['Current', '1-30', '31-60', '61-90', '90+'], 25, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
    })

    # Sample AP aging
    ap_aging = pd.DataFrame({
        'vendor_name': np.random.choice(vendors, 20),
        'bill_number': [f'BILL-{i:04d}' for i in range(20)],
        'bill_date': pd.date_range(end=end_date - timedelta(days=30), periods=20),
        'due_date': pd.date_range(end=end_date, periods=20),
        'amount': np.random.uniform(1000, 8000, 20).round(2),
        'days_outstanding': np.random.choice([0, 10, 25, 50, 95], 20, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
        'aging_bucket': np.random.choice(['Current', '1-30', '31-60', '61-90', '90+'], 20, p=[0.4, 0.3, 0.15, 0.1, 0.05]),
    })

    print("  Generated sample data successfully!")

    return {
        'financial_transactions': financial_transactions,
        'cost_classifications': cost_classifications,
        'booking_log': booking_log,
        'ar_aging': ar_aging,
        'ap_aging': ap_aging,
    }
