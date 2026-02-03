"""
CSI Cargo Dashboard - Data Validator
=====================================
Validates and cleans data before processing.

HOW IT WORKS:
1. Checks data types are correct (dates are dates, numbers are numbers)
2. Validates categorical values against allowed lists
3. Flags potential data quality issues
4. Cleans and standardizes values

This catches errors early so you don't get confusing results in the dashboard.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Any

from .config import VALIDATION, COLUMNS


class ValidationError(Exception):
    """Raised when data validation fails critically."""
    pass


class ValidationResult:
    """Container for validation results."""

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.fixes_applied: List[str] = []
        self.stats: Dict[str, Any] = {}

    @property
    def is_valid(self) -> bool:
        """Returns True if no critical errors were found."""
        return len(self.errors) == 0

    def summary(self) -> str:
        """Generate a human-readable summary."""
        lines = ["\n" + "=" * 60, "DATA VALIDATION SUMMARY", "=" * 60]

        if self.errors:
            lines.append(f"\nCRITICAL ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  [ERROR] {e}")

        if self.warnings:
            lines.append(f"\nWARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  [WARN] {w}")

        if self.fixes_applied:
            lines.append(f"\nAUTO-FIXES APPLIED ({len(self.fixes_applied)}):")
            for f in self.fixes_applied:
                lines.append(f"  [FIX] {f}")

        if self.stats:
            lines.append("\nDATA STATISTICS:")
            for key, value in self.stats.items():
                lines.append(f"  {key}: {value}")

        if self.is_valid:
            lines.append("\n" + "=" * 60)
            lines.append("VALIDATION PASSED - Data is ready for processing")
            lines.append("=" * 60)
        else:
            lines.append("\n" + "=" * 60)
            lines.append("VALIDATION FAILED - Please fix errors and re-run")
            lines.append("=" * 60)

        return "\n".join(lines)


def validate_all_data(data: Dict[str, pd.DataFrame]) -> Tuple[Dict[str, pd.DataFrame], ValidationResult]:
    """
    Validate all loaded data.

    Args:
        data: Dictionary of DataFrames from data_loader

    Returns:
        Tuple of (cleaned data dict, ValidationResult)
    """
    result = ValidationResult()
    cleaned_data = {}

    print("\n" + "=" * 60)
    print("VALIDATING DATA")
    print("=" * 60)

    # Validate each data file
    validators = {
        'financial_transactions': validate_financial_transactions,
        'cost_classifications': validate_cost_classifications,
        'booking_log': validate_booking_log,
        'ar_aging': validate_ar_aging,
        'ap_aging': validate_ap_aging,
    }

    for key, validator_func in validators.items():
        df = data.get(key)
        if df is not None:
            print(f"\nValidating: {key}...")
            cleaned_df, file_result = validator_func(df)
            cleaned_data[key] = cleaned_df

            # Merge results
            result.errors.extend([f"[{key}] {e}" for e in file_result.errors])
            result.warnings.extend([f"[{key}] {w}" for w in file_result.warnings])
            result.fixes_applied.extend([f"[{key}] {f}" for f in file_result.fixes_applied])
            result.stats[key] = file_result.stats
        else:
            cleaned_data[key] = None

    return cleaned_data, result


def validate_financial_transactions(df: pd.DataFrame) -> Tuple[pd.DataFrame, ValidationResult]:
    """Validate financial transactions data."""
    result = ValidationResult()
    df = df.copy()

    # Convert transaction_date to datetime
    df, date_fixes = convert_to_datetime(df, 'transaction_date')
    result.fixes_applied.extend(date_fixes)

    # Convert amount to numeric
    df, amount_fixes = convert_to_numeric(df, 'amount')
    result.fixes_applied.extend(amount_fixes)

    # Validate transaction_type
    valid_types = VALIDATION['transaction_types']
    invalid_types = df[~df['transaction_type'].isin(valid_types)]['transaction_type'].unique()
    if len(invalid_types) > 0:
        result.warnings.append(
            f"Unknown transaction types found: {list(invalid_types)}. "
            f"Valid types: {valid_types}"
        )
        # Map to 'Other' for unknown types
        df.loc[~df['transaction_type'].isin(valid_types), 'transaction_type'] = 'Other'
        result.fixes_applied.append(f"Mapped {len(invalid_types)} unknown transaction types to 'Other'")

    # Validate category
    valid_categories = VALIDATION['categories']
    invalid_cats = df[~df['category'].isin(valid_categories)]['category'].unique()
    if len(invalid_cats) > 0:
        result.warnings.append(
            f"Unknown categories found: {list(invalid_cats)}. "
            f"Valid categories: {valid_categories}"
        )

    # Check for negative amounts
    negative_count = (df['amount'] < 0).sum()
    if negative_count > 0:
        result.warnings.append(
            f"Found {negative_count} negative amounts. "
            "Ensure this is intentional (e.g., refunds/credits)."
        )

    # Statistics
    result.stats = {
        'row_count': len(df),
        'date_range': f"{df['transaction_date'].min()} to {df['transaction_date'].max()}",
        'total_amount': df['amount'].sum(),
        'categories': df['category'].value_counts().to_dict(),
    }

    return df, result


def validate_cost_classifications(df: pd.DataFrame) -> Tuple[pd.DataFrame, ValidationResult]:
    """Validate cost classifications data."""
    result = ValidationResult()
    df = df.copy()

    # Validate cost_type
    valid_cost_types = VALIDATION['cost_types']
    df['cost_type'] = df['cost_type'].str.strip().str.title()

    invalid_types = df[~df['cost_type'].isin(valid_cost_types)]['cost_type'].unique()
    if len(invalid_types) > 0:
        result.errors.append(
            f"Invalid cost types: {list(invalid_types)}. "
            f"Must be one of: {valid_cost_types}"
        )

    # Validate cost_group if present
    if 'cost_group' in df.columns:
        valid_groups = VALIDATION['cost_groups']
        df['cost_group'] = df['cost_group'].str.strip().str.title()

        invalid_groups = df[~df['cost_group'].isin(valid_groups)]['cost_group'].unique()
        if len(invalid_groups) > 0:
            result.warnings.append(
                f"Unknown cost groups: {list(invalid_groups)}. "
                f"Suggested groups: {valid_groups}"
            )

    # Statistics
    result.stats = {
        'row_count': len(df),
        'fixed_count': (df['cost_type'] == 'Fixed').sum(),
        'variable_count': (df['cost_type'] == 'Variable').sum(),
    }

    return df, result


def validate_booking_log(df: pd.DataFrame) -> Tuple[pd.DataFrame, ValidationResult]:
    """Validate booking log data."""
    result = ValidationResult()
    df = df.copy()

    # Convert dates
    df, date_fixes = convert_to_datetime(df, 'booking_date')
    result.fixes_applied.extend(date_fixes)

    if 'ship_date' in df.columns:
        df, ship_fixes = convert_to_datetime(df, 'ship_date')
        result.fixes_applied.extend(ship_fixes)

    # Convert numeric columns
    numeric_cols = [
        'published_rate', 'csi_cost', 'gross_margin', 'total_revenue',
        'intl_paperwork_fee', 'other_fees', 'rebooking_cost'
    ]
    for col in numeric_cols:
        if col in df.columns:
            df, fixes = convert_to_numeric(df, col)
            result.fixes_applied.extend(fixes)

    # Validate customer_type
    if 'customer_type' in df.columns:
        valid_types = VALIDATION['customer_types']
        df['customer_type'] = df['customer_type'].str.strip().str.title()
        invalid = df[~df['customer_type'].isin(valid_types)]['customer_type'].unique()
        if len(invalid) > 0:
            result.warnings.append(f"Unknown customer types: {list(invalid)}")
            df.loc[~df['customer_type'].isin(valid_types), 'customer_type'] = 'Unknown'

    # Validate route_type
    if 'route_type' in df.columns:
        valid_routes = VALIDATION['route_types']
        df['route_type'] = df['route_type'].str.strip().str.title()
        invalid = df[~df['route_type'].isin(valid_routes)]['route_type'].unique()
        if len(invalid) > 0:
            result.warnings.append(f"Unknown route types: {list(invalid)}")
            df.loc[~df['route_type'].isin(valid_routes), 'route_type'] = 'Unknown'

    # Validate was_rebooked
    if 'was_rebooked' in df.columns:
        df['was_rebooked'] = df['was_rebooked'].str.strip().str.title()
        df.loc[~df['was_rebooked'].isin(['Yes', 'No']), 'was_rebooked'] = 'No'

    # Recalculate gross_margin if we have the components
    if 'published_rate' in df.columns and 'csi_cost' in df.columns:
        calculated_margin = df['published_rate'] - df['csi_cost']
        if 'gross_margin' in df.columns:
            discrepancies = (df['gross_margin'] - calculated_margin).abs() > 0.01
            if discrepancies.sum() > 0:
                result.warnings.append(
                    f"Found {discrepancies.sum()} rows where gross_margin doesn't match "
                    "(published_rate - csi_cost). Recalculating."
                )
                df['gross_margin'] = calculated_margin
                result.fixes_applied.append("Recalculated gross_margin from published_rate - csi_cost")
        else:
            df['gross_margin'] = calculated_margin
            result.fixes_applied.append("Calculated gross_margin from published_rate - csi_cost")

    # Statistics
    result.stats = {
        'row_count': len(df),
        'date_range': f"{df['booking_date'].min()} to {df['booking_date'].max()}",
        'total_revenue': df['total_revenue'].sum() if 'total_revenue' in df.columns else 'N/A',
        'total_bookings': len(df),
        'rebook_count': (df['was_rebooked'] == 'Yes').sum() if 'was_rebooked' in df.columns else 'N/A',
        'customer_types': df['customer_type'].value_counts().to_dict() if 'customer_type' in df.columns else {},
    }

    return df, result


def validate_ar_aging(df: pd.DataFrame) -> Tuple[pd.DataFrame, ValidationResult]:
    """Validate AR aging data."""
    result = ValidationResult()
    df = df.copy()

    # Convert dates
    for col in ['invoice_date', 'due_date']:
        if col in df.columns:
            df, fixes = convert_to_datetime(df, col)
            result.fixes_applied.extend(fixes)

    # Convert amount to numeric
    df, amount_fixes = convert_to_numeric(df, 'amount')
    result.fixes_applied.extend(amount_fixes)

    # Validate aging_bucket
    if 'aging_bucket' in df.columns:
        valid_buckets = VALIDATION['aging_buckets']
        invalid = df[~df['aging_bucket'].isin(valid_buckets)]['aging_bucket'].unique()
        if len(invalid) > 0:
            result.warnings.append(f"Unknown aging buckets: {list(invalid)}")
            df.loc[~df['aging_bucket'].isin(valid_buckets), 'aging_bucket'] = 'Unknown'

    # Statistics
    result.stats = {
        'row_count': len(df),
        'total_ar': df['amount'].sum(),
        'by_bucket': df.groupby('aging_bucket')['amount'].sum().to_dict() if 'aging_bucket' in df.columns else {},
    }

    return df, result


def validate_ap_aging(df: pd.DataFrame) -> Tuple[pd.DataFrame, ValidationResult]:
    """Validate AP aging data."""
    result = ValidationResult()
    df = df.copy()

    # Convert dates
    for col in ['bill_date', 'due_date']:
        if col in df.columns:
            df, fixes = convert_to_datetime(df, col)
            result.fixes_applied.extend(fixes)

    # Convert amount to numeric
    df, amount_fixes = convert_to_numeric(df, 'amount')
    result.fixes_applied.extend(amount_fixes)

    # Validate aging_bucket
    if 'aging_bucket' in df.columns:
        valid_buckets = VALIDATION['aging_buckets']
        invalid = df[~df['aging_bucket'].isin(valid_buckets)]['aging_bucket'].unique()
        if len(invalid) > 0:
            result.warnings.append(f"Unknown aging buckets: {list(invalid)}")
            df.loc[~df['aging_bucket'].isin(valid_buckets), 'aging_bucket'] = 'Unknown'

    # Statistics
    result.stats = {
        'row_count': len(df),
        'total_ap': df['amount'].sum(),
        'by_bucket': df.groupby('aging_bucket')['amount'].sum().to_dict() if 'aging_bucket' in df.columns else {},
    }

    return df, result


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def convert_to_datetime(df: pd.DataFrame, column: str) -> Tuple[pd.DataFrame, List[str]]:
    """Convert a column to datetime, handling errors gracefully."""
    fixes = []

    if column not in df.columns:
        return df, fixes

    try:
        original_nulls = df[column].isna().sum()
        df[column] = pd.to_datetime(df[column], errors='coerce')
        new_nulls = df[column].isna().sum()

        conversion_failures = new_nulls - original_nulls
        if conversion_failures > 0:
            fixes.append(
                f"Could not parse {conversion_failures} dates in '{column}' - set to null"
            )
    except Exception as e:
        fixes.append(f"Error converting '{column}' to datetime: {str(e)}")

    return df, fixes


def convert_to_numeric(df: pd.DataFrame, column: str) -> Tuple[pd.DataFrame, List[str]]:
    """Convert a column to numeric, handling errors gracefully."""
    fixes = []

    if column not in df.columns:
        return df, fixes

    try:
        # Remove currency symbols and commas
        if df[column].dtype == 'object':
            df[column] = df[column].astype(str).str.replace('$', '', regex=False)
            df[column] = df[column].str.replace(',', '', regex=False)
            df[column] = df[column].str.replace('(', '-', regex=False)
            df[column] = df[column].str.replace(')', '', regex=False)
            fixes.append(f"Cleaned currency formatting in '{column}'")

        original_nulls = df[column].isna().sum()
        df[column] = pd.to_numeric(df[column], errors='coerce')
        new_nulls = df[column].isna().sum()

        conversion_failures = new_nulls - original_nulls
        if conversion_failures > 0:
            fixes.append(
                f"Could not parse {conversion_failures} numbers in '{column}' - set to null"
            )

        # Fill nulls with 0 for numeric columns
        df[column] = df[column].fillna(0)

    except Exception as e:
        fixes.append(f"Error converting '{column}' to numeric: {str(e)}")

    return df, fixes
