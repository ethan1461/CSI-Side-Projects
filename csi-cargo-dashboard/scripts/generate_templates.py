#!/usr/bin/env python3
"""
CSI Cargo Dashboard - Template Generator
=========================================
Generates blank Excel templates with the correct headers.
Share these with your CFO to ensure data is formatted correctly.

USAGE:
    python scripts/generate_templates.py

OUTPUT:
    Creates template files in data/templates/:
    - financial_transactions_template.xlsx
    - cost_classifications_template.xlsx
    - booking_log_template.xlsx
    - ar_aging_template.xlsx
    - ap_aging_template.xlsx
"""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pandas as pd
from src.config import PATHS, COLUMNS

def create_template(file_key: str, columns_spec: dict) -> pd.DataFrame:
    """Create a template DataFrame with headers and one example row."""

    # Get all columns (required + optional)
    all_columns = columns_spec.get('required', []) + columns_spec.get('optional', [])

    # Create example data
    example_data = {}

    for col in all_columns:
        if 'date' in col.lower():
            example_data[col] = '2024-01-15'
        elif 'amount' in col.lower() or 'rate' in col.lower() or 'cost' in col.lower() or 'fee' in col.lower() or 'margin' in col.lower() or 'revenue' in col.lower():
            example_data[col] = '1000.00'
        elif col == 'transaction_id':
            example_data[col] = 'TXN-2024-0001'
        elif col == 'booking_id':
            example_data[col] = 'CSI-2024-0001'
        elif col == 'invoice_number':
            example_data[col] = 'INV-0001'
        elif col == 'bill_number':
            example_data[col] = 'BILL-0001'
        elif col == 'transaction_type':
            example_data[col] = 'Invoice'
        elif col == 'category':
            example_data[col] = 'Revenue'
        elif col == 'subcategory':
            example_data[col] = 'Air Freight Revenue'
        elif col == 'cost_type':
            example_data[col] = 'Fixed'
        elif col == 'cost_group':
            example_data[col] = 'Labor'
        elif col == 'customer_type':
            example_data[col] = 'Independent'
        elif col == 'route_type':
            example_data[col] = 'Domestic'
        elif col == 'shipment_type':
            example_data[col] = 'Whole Body'
        elif col == 'payment_status':
            example_data[col] = 'Paid'
        elif col == 'was_rebooked':
            example_data[col] = 'No'
        elif col == 'aging_bucket':
            example_data[col] = 'Current'
        elif col == 'days_outstanding':
            example_data[col] = '0'
        elif 'name' in col.lower():
            example_data[col] = 'Example Name'
        elif 'city' in col.lower():
            example_data[col] = 'City Name'
        elif 'state' in col.lower():
            example_data[col] = 'CA'
        elif col == 'airline':
            example_data[col] = 'American Airlines'
        elif col == 'agent_name':
            example_data[col] = 'Agent Name'
        else:
            example_data[col] = 'Example'

    # Create DataFrame with example row
    df = pd.DataFrame([example_data])

    return df


def main():
    """Generate all templates."""

    print("\n" + "=" * 60)
    print("CSI CARGO DASHBOARD - TEMPLATE GENERATOR")
    print("=" * 60)

    # Ensure templates directory exists
    PATHS['templates'].mkdir(parents=True, exist_ok=True)

    templates = {
        'financial_transactions': 'financial_transactions_template.xlsx',
        'cost_classifications': 'cost_classifications_template.xlsx',
        'booking_log': 'booking_log_template.xlsx',
        'ar_aging': 'ar_aging_template.xlsx',
        'ap_aging': 'ap_aging_template.xlsx',
    }

    for key, filename in templates.items():
        print(f"\nGenerating: {filename}")

        columns_spec = COLUMNS.get(key, {})
        df = create_template(key, columns_spec)

        output_path = PATHS['templates'] / filename
        df.to_excel(output_path, index=False)

        print(f"  - Columns: {list(df.columns)}")
        print(f"  - Saved to: {output_path}")

    # Also create a combined template guide
    guide_path = PATHS['templates'] / 'DATA_COLLECTION_GUIDE.txt'
    with open(guide_path, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("CSI CARGO DASHBOARD - DATA COLLECTION GUIDE\n")
        f.write("=" * 70 + "\n\n")

        f.write("Instructions for CFO:\n")
        f.write("-" * 70 + "\n")
        f.write("1. Open each template file\n")
        f.write("2. Export data from QuickBooks/OMS matching the column headers\n")
        f.write("3. Paste the data below the example row\n")
        f.write("4. Delete the example row\n")
        f.write("5. Save as the filename WITHOUT '_template' (e.g., 'financial_transactions.xlsx')\n")
        f.write("6. Place saved files in the data/input/ folder\n\n")

        for key, filename in templates.items():
            columns_spec = COLUMNS.get(key, {})
            required = columns_spec.get('required', [])
            optional = columns_spec.get('optional', [])

            f.write("-" * 70 + "\n")
            f.write(f"FILE: {filename.replace('_template', '')}\n")
            f.write("-" * 70 + "\n\n")

            f.write("REQUIRED COLUMNS (must have data):\n")
            for col in required:
                f.write(f"  - {col}\n")

            f.write("\nOPTIONAL COLUMNS (nice to have):\n")
            for col in optional:
                f.write(f"  - {col}\n")

            f.write("\n")

    print(f"\n  Created guide: {guide_path}")

    print("\n" + "=" * 60)
    print("TEMPLATES GENERATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nTemplates saved to: {PATHS['templates']}")
    print("\nNext steps:")
    print("1. Share the templates folder with your CFO")
    print("2. Have CFO fill in the data and save WITHOUT '_template' suffix")
    print("3. Place completed files in data/input/")
    print("4. Run: python scripts/run_dashboard.py")


if __name__ == '__main__':
    main()
