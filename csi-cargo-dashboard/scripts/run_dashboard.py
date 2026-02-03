#!/usr/bin/env python3
"""
CSI Cargo Dashboard - Main Runner
=================================
This is the main script you run to process data and generate the dashboard.

USAGE:
    python scripts/run_dashboard.py

OPTIONS:
    --sample     Use sample data for testing (no input files needed)
    --validate   Only validate data, don't generate output
    --help       Show this help message

WHAT IT DOES:
    1. Loads data from Excel files in data/input/
    2. Validates and cleans the data
    3. Calculates all metrics and KPIs
    4. Outputs processed data to data/output/dashboard_data.xlsx
    5. PowerBI can then connect to the output file

OUTPUT:
    The script creates data/output/dashboard_data.xlsx with multiple sheets:
    - executive_summary: High-level KPIs
    - financial_summary: Detailed financial breakdown
    - cost_analysis: Fixed vs variable costs
    - monthly_pnl: Month-by-month P&L
    - ar_summary: Accounts receivable aging
    - ap_summary: Accounts payable aging
    - booking_summary: Overall booking metrics
    - booking_by_route: Bookings by domestic/international
    - booking_by_airline: Bookings by carrier
    - booking_by_customer: Bookings by funeral home
    - booking_by_customer_type: Bookings by corporate/independent/other
    - booking_by_geography: Bookings by origin/destination
    - monthly_bookings: Monthly booking trends
    - rework_analysis: Rebooking patterns
    - agent_productivity: Agent-level metrics
    - carrier_performance: Airline performance metrics
    - daily_metrics: Daily trends
    - weekly_metrics: Weekly trends
    - monthly_metrics: Monthly combined trends
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add the src directory to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import PATHS, OUTPUT_FILE, OMS_CONFIG
from src.data_loader import load_all_data, create_sample_data
from src.data_validator import validate_all_data
from src.metrics_calculator import calculate_all_metrics
from src.oms_integration import is_oms_enabled, load_all_data_from_oms


def main():
    """Main entry point for the dashboard processor."""

    print("\n" + "=" * 60)
    print("CSI CARGO SALES DASHBOARD")
    print("=" * 60)
    print(f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Parse command line arguments
    use_sample = '--sample' in sys.argv
    validate_only = '--validate' in sys.argv

    if '--help' in sys.argv:
        print(__doc__)
        return

    # =========================================================================
    # STEP 1: LOAD DATA
    # =========================================================================

    if use_sample:
        print("\n[MODE: SAMPLE DATA]")
        print("Using generated sample data for testing...")
        data = create_sample_data()
    elif is_oms_enabled():
        print("\n[MODE: OMS INTEGRATION]")
        print("Loading data from OMS...")
        try:
            oms_data = load_all_data_from_oms()
            # Fall back to file-based loading for any None values
            file_data = load_all_data()
            data = {}
            for key in set(list(oms_data.keys()) + list(file_data.keys())):
                if oms_data.get(key) is not None:
                    data[key] = oms_data[key]
                else:
                    data[key] = file_data.get(key)
        except Exception as e:
            print(f"\n[WARNING] OMS loading failed: {e}")
            print("Falling back to file-based loading...")
            data = load_all_data()
    else:
        print("\n[MODE: FILE-BASED]")
        print("Loading data from Excel files...")
        data = load_all_data()

    # =========================================================================
    # STEP 2: VALIDATE DATA
    # =========================================================================

    data, validation_result = validate_all_data(data)
    print(validation_result.summary())

    if not validation_result.is_valid:
        print("\n[ERROR] Data validation failed. Please fix the errors and re-run.")
        sys.exit(1)

    if validate_only:
        print("\n[VALIDATE ONLY MODE] Skipping output generation.")
        return

    # =========================================================================
    # STEP 3: CALCULATE METRICS
    # =========================================================================

    metrics = calculate_all_metrics(data)

    # =========================================================================
    # STEP 4: GENERATE OUTPUT
    # =========================================================================

    print("\n" + "=" * 60)
    print("GENERATING OUTPUT")
    print("=" * 60)

    output_path = PATHS['output'] / OUTPUT_FILE

    # Ensure output directory exists
    PATHS['output'].mkdir(parents=True, exist_ok=True)

    # Write to Excel with multiple sheets
    print(f"\nWriting to: {output_path}")

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for sheet_name, df in metrics.items():
            if df is not None and len(df) > 0:
                # Clean sheet name (Excel has 31 char limit)
                clean_name = sheet_name[:31]
                df.to_excel(writer, sheet_name=clean_name, index=False)
                print(f"  - {clean_name}: {len(df)} rows")

        # Also include the raw validated data for reference
        print("\nAdding raw data sheets...")
        for data_name, df in data.items():
            if df is not None and len(df) > 0:
                sheet_name = f"raw_{data_name}"[:31]
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"  - {sheet_name}: {len(df)} rows")

    # =========================================================================
    # STEP 5: SUMMARY
    # =========================================================================

    print("\n" + "=" * 60)
    print("COMPLETE!")
    print("=" * 60)
    print(f"\nOutput file: {output_path}")
    print("\nNEXT STEPS:")
    print("1. Open PowerBI Desktop")
    print("2. Click 'Get Data' > 'Excel'")
    print(f"3. Select: {output_path}")
    print("4. Follow the setup guide in powerbi/setup_guide.md")
    print("\nFor questions, see README.md")


# Import pandas here to avoid issues if it's not installed
try:
    import pandas as pd
except ImportError:
    print("\n[ERROR] pandas is not installed.")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)


if __name__ == '__main__':
    main()
