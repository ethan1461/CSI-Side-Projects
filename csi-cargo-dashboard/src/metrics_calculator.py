"""
CSI Cargo Dashboard - Metrics Calculator
=========================================
Calculates all KPIs and metrics for the dashboard.

HOW IT WORKS:
1. Takes validated data as input
2. Calculates executive-level KPIs (revenue, profit, margins)
3. Calculates operational metrics (bookings, rework, productivity)
4. Generates time-series data for trend analysis
5. Creates breakdown summaries (by route, airline, customer, etc.)

The output is a set of DataFrames optimized for PowerBI consumption.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional, List, Any
from dateutil.relativedelta import relativedelta

from .config import DISPLAY, TIME_PERIODS


def calculate_all_metrics(data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
    """
    Calculate all metrics and return DataFrames ready for PowerBI.

    Args:
        data: Dictionary of validated DataFrames

    Returns:
        Dictionary of output DataFrames for different dashboard sections
    """
    print("\n" + "=" * 60)
    print("CALCULATING METRICS")
    print("=" * 60)

    output = {}

    # ==========================================================================
    # EXECUTIVE SUMMARY METRICS
    # ==========================================================================
    print("\nCalculating executive summary metrics...")
    output['executive_summary'] = calculate_executive_summary(data)

    # ==========================================================================
    # FINANCIAL METRICS
    # ==========================================================================
    print("Calculating financial metrics...")
    output['financial_summary'] = calculate_financial_summary(data)
    output['cost_analysis'] = calculate_cost_analysis(data)
    output['monthly_pnl'] = calculate_monthly_pnl(data)

    # ==========================================================================
    # AR/AP METRICS
    # ==========================================================================
    print("Calculating AR/AP metrics...")
    output['ar_summary'] = calculate_ar_summary(data)
    output['ap_summary'] = calculate_ap_summary(data)

    # ==========================================================================
    # BOOKING METRICS
    # ==========================================================================
    print("Calculating booking metrics...")
    output['booking_summary'] = calculate_booking_summary(data)
    output['booking_by_route'] = calculate_booking_by_dimension(data, 'route')
    output['booking_by_airline'] = calculate_booking_by_dimension(data, 'airline')
    output['booking_by_customer'] = calculate_booking_by_dimension(data, 'customer')
    output['booking_by_customer_type'] = calculate_booking_by_dimension(data, 'customer_type')
    output['booking_by_geography'] = calculate_geographic_breakdown(data)
    output['monthly_bookings'] = calculate_monthly_bookings(data)

    # ==========================================================================
    # OPERATIONAL METRICS
    # ==========================================================================
    print("Calculating operational metrics...")
    output['rework_analysis'] = calculate_rework_analysis(data)
    output['agent_productivity'] = calculate_agent_productivity(data)
    output['carrier_performance'] = calculate_carrier_performance(data)

    # ==========================================================================
    # TIME SERIES DATA
    # ==========================================================================
    print("Generating time series data...")
    output['daily_metrics'] = calculate_daily_metrics(data)
    output['weekly_metrics'] = calculate_weekly_metrics(data)
    output['monthly_metrics'] = calculate_monthly_metrics(data)

    print("\nMetrics calculation complete!")
    return output


# =============================================================================
# EXECUTIVE SUMMARY
# =============================================================================

def calculate_executive_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate high-level KPIs for CEO dashboard."""

    financial = data.get('financial_transactions')
    bookings = data.get('booking_log')
    ar = data.get('ar_aging')
    ap = data.get('ap_aging')

    metrics = []

    # Current date for calculations
    today = datetime.now()
    current_month_start = today.replace(day=1)
    last_month_start = (current_month_start - relativedelta(months=1))
    last_month_end = current_month_start - timedelta(days=1)
    ytd_start = today.replace(month=1, day=1)

    # --- Financial KPIs ---
    if financial is not None:
        # Total Revenue (YTD)
        ytd_revenue = financial[
            (financial['transaction_date'] >= ytd_start) &
            (financial['category'] == 'Revenue')
        ]['amount'].sum()
        metrics.append({'metric': 'Revenue (YTD)', 'value': ytd_revenue, 'category': 'Financial'})

        # Total Expenses (YTD)
        ytd_expenses = financial[
            (financial['transaction_date'] >= ytd_start) &
            (financial['category'].isin(['COGS', 'Operating Expense']))
        ]['amount'].sum()
        metrics.append({'metric': 'Expenses (YTD)', 'value': ytd_expenses, 'category': 'Financial'})

        # Net Profit (YTD)
        ytd_profit = ytd_revenue - ytd_expenses
        metrics.append({'metric': 'Net Profit (YTD)', 'value': ytd_profit, 'category': 'Financial'})

        # Profit Margin
        profit_margin = (ytd_profit / ytd_revenue * 100) if ytd_revenue > 0 else 0
        metrics.append({'metric': 'Profit Margin %', 'value': profit_margin, 'category': 'Financial'})

        # Last Month Revenue
        last_month_revenue = financial[
            (financial['transaction_date'] >= last_month_start) &
            (financial['transaction_date'] <= last_month_end) &
            (financial['category'] == 'Revenue')
        ]['amount'].sum()
        metrics.append({'metric': 'Revenue (Last Month)', 'value': last_month_revenue, 'category': 'Financial'})

    # --- Booking KPIs ---
    if bookings is not None:
        # Total Bookings (YTD)
        ytd_bookings = bookings[bookings['booking_date'] >= ytd_start]
        metrics.append({'metric': 'Total Bookings (YTD)', 'value': len(ytd_bookings), 'category': 'Operations'})

        # Booking Revenue (YTD)
        booking_revenue_ytd = ytd_bookings['total_revenue'].sum()
        metrics.append({'metric': 'Booking Revenue (YTD)', 'value': booking_revenue_ytd, 'category': 'Operations'})

        # Average Booking Value
        avg_booking = ytd_bookings['total_revenue'].mean() if len(ytd_bookings) > 0 else 0
        metrics.append({'metric': 'Avg Booking Value', 'value': avg_booking, 'category': 'Operations'})

        # Gross Margin (from bookings)
        if 'gross_margin' in bookings.columns:
            total_margin = ytd_bookings['gross_margin'].sum()
            margin_pct = (total_margin / ytd_bookings['published_rate'].sum() * 100) if ytd_bookings['published_rate'].sum() > 0 else 0
            metrics.append({'metric': 'Gross Margin (YTD)', 'value': total_margin, 'category': 'Operations'})
            metrics.append({'metric': 'Gross Margin %', 'value': margin_pct, 'category': 'Operations'})

        # Rebook Rate
        if 'was_rebooked' in bookings.columns:
            rebook_count = (ytd_bookings['was_rebooked'] == 'Yes').sum()
            rebook_rate = (rebook_count / len(ytd_bookings) * 100) if len(ytd_bookings) > 0 else 0
            metrics.append({'metric': 'Rebook Rate %', 'value': rebook_rate, 'category': 'Operations'})

            # Rebooking Costs
            if 'rebooking_cost' in bookings.columns:
                total_rebook_cost = ytd_bookings['rebooking_cost'].sum()
                metrics.append({'metric': 'Rebooking Costs (YTD)', 'value': total_rebook_cost, 'category': 'Operations'})

    # --- AR/AP KPIs ---
    if ar is not None:
        total_ar = ar['amount'].sum()
        metrics.append({'metric': 'Total AR', 'value': total_ar, 'category': 'Cash Position'})

        ar_over_90 = ar[ar['aging_bucket'] == '90+']['amount'].sum() if 'aging_bucket' in ar.columns else 0
        metrics.append({'metric': 'AR Over 90 Days', 'value': ar_over_90, 'category': 'Cash Position'})

    if ap is not None:
        total_ap = ap['amount'].sum()
        metrics.append({'metric': 'Total AP', 'value': total_ap, 'category': 'Cash Position'})

        ap_over_90 = ap[ap['aging_bucket'] == '90+']['amount'].sum() if 'aging_bucket' in ap.columns else 0
        metrics.append({'metric': 'AP Over 90 Days', 'value': ap_over_90, 'category': 'Cash Position'})

    # Net Working Capital
    if ar is not None and ap is not None:
        net_wc = total_ar - total_ap
        metrics.append({'metric': 'Net Working Capital', 'value': net_wc, 'category': 'Cash Position'})

    return pd.DataFrame(metrics)


# =============================================================================
# FINANCIAL METRICS
# =============================================================================

def calculate_financial_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate detailed financial summary by category."""

    financial = data.get('financial_transactions')
    if financial is None:
        return pd.DataFrame()

    summary = financial.groupby(['category', 'subcategory']).agg({
        'amount': ['sum', 'count', 'mean']
    }).reset_index()

    summary.columns = ['category', 'subcategory', 'total_amount', 'transaction_count', 'avg_amount']
    return summary


def calculate_cost_analysis(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate fixed vs variable cost breakdown."""

    financial = data.get('financial_transactions')
    cost_class = data.get('cost_classifications')

    if financial is None:
        return pd.DataFrame()

    # Filter to expenses only
    expenses = financial[financial['category'].isin(['COGS', 'Operating Expense'])].copy()

    if cost_class is not None and len(cost_class) > 0:
        # Join with cost classifications
        expenses = expenses.merge(
            cost_class[['expense_category', 'cost_type', 'cost_group']],
            left_on='subcategory',
            right_on='expense_category',
            how='left'
        )
        expenses['cost_type'] = expenses['cost_type'].fillna('Unclassified')
        expenses['cost_group'] = expenses['cost_group'].fillna('Other')
    else:
        expenses['cost_type'] = 'Unclassified'
        expenses['cost_group'] = 'Other'

    # Aggregate by cost type and group
    summary = expenses.groupby(['cost_type', 'cost_group']).agg({
        'amount': 'sum'
    }).reset_index()

    summary.columns = ['cost_type', 'cost_group', 'total_amount']

    # Add percentages
    total = summary['total_amount'].sum()
    summary['percentage'] = (summary['total_amount'] / total * 100) if total > 0 else 0

    return summary


def calculate_monthly_pnl(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate month-by-month P&L."""

    financial = data.get('financial_transactions')
    if financial is None:
        return pd.DataFrame()

    # Create month column
    df = financial.copy()
    df['month'] = df['transaction_date'].dt.to_period('M').dt.to_timestamp()

    # Pivot by category
    monthly = df.groupby(['month', 'category'])['amount'].sum().unstack(fill_value=0).reset_index()

    # Calculate derived metrics
    if 'Revenue' in monthly.columns:
        monthly['revenue'] = monthly['Revenue']
    else:
        monthly['revenue'] = 0

    if 'COGS' in monthly.columns:
        monthly['cogs'] = monthly['COGS']
    else:
        monthly['cogs'] = 0

    if 'Operating Expense' in monthly.columns:
        monthly['operating_expense'] = monthly['Operating Expense']
    else:
        monthly['operating_expense'] = 0

    monthly['gross_profit'] = monthly['revenue'] - monthly['cogs']
    monthly['net_profit'] = monthly['revenue'] - monthly['cogs'] - monthly['operating_expense']
    monthly['gross_margin_pct'] = (monthly['gross_profit'] / monthly['revenue'] * 100).fillna(0)
    monthly['net_margin_pct'] = (monthly['net_profit'] / monthly['revenue'] * 100).fillna(0)

    return monthly[['month', 'revenue', 'cogs', 'operating_expense', 'gross_profit', 'net_profit', 'gross_margin_pct', 'net_margin_pct']]


# =============================================================================
# AR/AP METRICS
# =============================================================================

def calculate_ar_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate AR aging summary."""

    ar = data.get('ar_aging')
    if ar is None:
        return pd.DataFrame()

    if 'aging_bucket' not in ar.columns:
        return pd.DataFrame({'total_ar': [ar['amount'].sum()]})

    summary = ar.groupby('aging_bucket').agg({
        'amount': ['sum', 'count'],
        'customer_name': 'nunique'
    }).reset_index()

    summary.columns = ['aging_bucket', 'total_amount', 'invoice_count', 'customer_count']

    # Order buckets correctly
    bucket_order = ['Current', '1-30', '31-60', '61-90', '90+', 'Unknown']
    summary['bucket_order'] = summary['aging_bucket'].apply(
        lambda x: bucket_order.index(x) if x in bucket_order else 99
    )
    summary = summary.sort_values('bucket_order').drop('bucket_order', axis=1)

    return summary


def calculate_ap_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate AP aging summary."""

    ap = data.get('ap_aging')
    if ap is None:
        return pd.DataFrame()

    if 'aging_bucket' not in ap.columns:
        return pd.DataFrame({'total_ap': [ap['amount'].sum()]})

    summary = ap.groupby('aging_bucket').agg({
        'amount': ['sum', 'count'],
        'vendor_name': 'nunique'
    }).reset_index()

    summary.columns = ['aging_bucket', 'total_amount', 'bill_count', 'vendor_count']

    # Order buckets correctly
    bucket_order = ['Current', '1-30', '31-60', '61-90', '90+', 'Unknown']
    summary['bucket_order'] = summary['aging_bucket'].apply(
        lambda x: bucket_order.index(x) if x in bucket_order else 99
    )
    summary = summary.sort_values('bucket_order').drop('bucket_order', axis=1)

    return summary


# =============================================================================
# BOOKING METRICS
# =============================================================================

def calculate_booking_summary(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate overall booking summary."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    summary = {
        'total_bookings': len(bookings),
        'total_revenue': bookings['total_revenue'].sum(),
        'avg_booking_value': bookings['total_revenue'].mean(),
    }

    if 'gross_margin' in bookings.columns:
        summary['total_gross_margin'] = bookings['gross_margin'].sum()
        summary['avg_margin_per_booking'] = bookings['gross_margin'].mean()
        summary['margin_percentage'] = (
            bookings['gross_margin'].sum() / bookings['published_rate'].sum() * 100
            if bookings['published_rate'].sum() > 0 else 0
        )

    if 'was_rebooked' in bookings.columns:
        summary['rebook_count'] = (bookings['was_rebooked'] == 'Yes').sum()
        summary['rebook_rate'] = summary['rebook_count'] / len(bookings) * 100

    if 'rebooking_cost' in bookings.columns:
        summary['total_rebooking_cost'] = bookings['rebooking_cost'].sum()

    return pd.DataFrame([summary])


def calculate_booking_by_dimension(
    data: Dict[str, pd.DataFrame],
    dimension: str
) -> pd.DataFrame:
    """Calculate booking metrics by a specific dimension."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    # Map dimension to column(s)
    dimension_map = {
        'route': ['route_type'],
        'airline': ['airline'],
        'customer': ['customer_name'],
        'customer_type': ['customer_type'],
        'shipment_type': ['shipment_type'],
    }

    columns = dimension_map.get(dimension, [dimension])

    # Check if columns exist
    for col in columns:
        if col not in bookings.columns:
            return pd.DataFrame()

    # Aggregate
    agg_dict = {
        'booking_id': 'count',
        'total_revenue': 'sum',
    }

    if 'gross_margin' in bookings.columns:
        agg_dict['gross_margin'] = 'sum'
    if 'rebooking_cost' in bookings.columns:
        agg_dict['rebooking_cost'] = 'sum'

    summary = bookings.groupby(columns).agg(agg_dict).reset_index()

    # Rename columns
    rename_map = {'booking_id': 'booking_count'}
    summary = summary.rename(columns=rename_map)

    # Add percentages
    total_bookings = summary['booking_count'].sum()
    total_revenue = summary['total_revenue'].sum()

    summary['booking_share_pct'] = (summary['booking_count'] / total_bookings * 100) if total_bookings > 0 else 0
    summary['revenue_share_pct'] = (summary['total_revenue'] / total_revenue * 100) if total_revenue > 0 else 0

    if 'gross_margin' in summary.columns:
        summary['margin_pct'] = (summary['gross_margin'] / summary['total_revenue'] * 100).fillna(0)

    # Sort by revenue descending
    summary = summary.sort_values('total_revenue', ascending=False)

    return summary


def calculate_geographic_breakdown(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate booking metrics by origin/destination geography."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    results = []

    # By origin state
    if 'origin_state' in bookings.columns:
        origin = bookings.groupby('origin_state').agg({
            'booking_id': 'count',
            'total_revenue': 'sum'
        }).reset_index()
        origin.columns = ['location', 'booking_count', 'total_revenue']
        origin['location_type'] = 'Origin'
        results.append(origin)

    # By destination
    if 'destination_state_country' in bookings.columns:
        dest = bookings.groupby('destination_state_country').agg({
            'booking_id': 'count',
            'total_revenue': 'sum'
        }).reset_index()
        dest.columns = ['location', 'booking_count', 'total_revenue']
        dest['location_type'] = 'Destination'
        results.append(dest)

    if results:
        combined = pd.concat(results, ignore_index=True)
        return combined.sort_values('total_revenue', ascending=False)

    return pd.DataFrame()


def calculate_monthly_bookings(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate monthly booking trends."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    df = bookings.copy()
    df['month'] = df['booking_date'].dt.to_period('M').dt.to_timestamp()

    agg_dict = {
        'booking_id': 'count',
        'total_revenue': 'sum',
    }

    if 'gross_margin' in df.columns:
        agg_dict['gross_margin'] = 'sum'
    if 'rebooking_cost' in df.columns:
        agg_dict['rebooking_cost'] = 'sum'
    if 'was_rebooked' in df.columns:
        df['rebooked_flag'] = (df['was_rebooked'] == 'Yes').astype(int)
        agg_dict['rebooked_flag'] = 'sum'

    monthly = df.groupby('month').agg(agg_dict).reset_index()
    monthly = monthly.rename(columns={'booking_id': 'booking_count'})

    if 'rebooked_flag' in monthly.columns:
        monthly = monthly.rename(columns={'rebooked_flag': 'rebook_count'})
        monthly['rebook_rate'] = (monthly['rebook_count'] / monthly['booking_count'] * 100).fillna(0)

    # Add average booking value
    monthly['avg_booking_value'] = (monthly['total_revenue'] / monthly['booking_count']).fillna(0)

    if 'gross_margin' in monthly.columns:
        monthly['margin_pct'] = (monthly['gross_margin'] / monthly['total_revenue'] * 100).fillna(0)

    return monthly


# =============================================================================
# OPERATIONAL METRICS
# =============================================================================

def calculate_rework_analysis(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Analyze rebooking/rework patterns."""

    bookings = data.get('booking_log')
    if bookings is None or 'was_rebooked' not in bookings.columns:
        return pd.DataFrame()

    # Filter to rebooked only
    rebooked = bookings[bookings['was_rebooked'] == 'Yes'].copy()

    if len(rebooked) == 0:
        return pd.DataFrame({'message': ['No rebookings found in data']})

    # Analyze by different dimensions
    analyses = []

    # By airline
    if 'airline' in rebooked.columns:
        by_airline = rebooked.groupby('airline').agg({
            'booking_id': 'count',
            'rebooking_cost': 'sum' if 'rebooking_cost' in rebooked.columns else 'count'
        }).reset_index()
        by_airline.columns = ['dimension_value', 'rebook_count', 'total_cost']
        by_airline['dimension'] = 'Airline'

        # Add total bookings for rate calculation
        total_by_airline = bookings.groupby('airline')['booking_id'].count().reset_index()
        total_by_airline.columns = ['dimension_value', 'total_bookings']
        by_airline = by_airline.merge(total_by_airline, on='dimension_value', how='left')
        by_airline['rebook_rate'] = (by_airline['rebook_count'] / by_airline['total_bookings'] * 100).fillna(0)

        analyses.append(by_airline)

    # By route type
    if 'route_type' in rebooked.columns:
        by_route = rebooked.groupby('route_type').agg({
            'booking_id': 'count',
            'rebooking_cost': 'sum' if 'rebooking_cost' in rebooked.columns else 'count'
        }).reset_index()
        by_route.columns = ['dimension_value', 'rebook_count', 'total_cost']
        by_route['dimension'] = 'Route Type'

        total_by_route = bookings.groupby('route_type')['booking_id'].count().reset_index()
        total_by_route.columns = ['dimension_value', 'total_bookings']
        by_route = by_route.merge(total_by_route, on='dimension_value', how='left')
        by_route['rebook_rate'] = (by_route['rebook_count'] / by_route['total_bookings'] * 100).fillna(0)

        analyses.append(by_route)

    # By customer type
    if 'customer_type' in rebooked.columns:
        by_cust = rebooked.groupby('customer_type').agg({
            'booking_id': 'count',
            'rebooking_cost': 'sum' if 'rebooking_cost' in rebooked.columns else 'count'
        }).reset_index()
        by_cust.columns = ['dimension_value', 'rebook_count', 'total_cost']
        by_cust['dimension'] = 'Customer Type'

        total_by_cust = bookings.groupby('customer_type')['booking_id'].count().reset_index()
        total_by_cust.columns = ['dimension_value', 'total_bookings']
        by_cust = by_cust.merge(total_by_cust, on='dimension_value', how='left')
        by_cust['rebook_rate'] = (by_cust['rebook_count'] / by_cust['total_bookings'] * 100).fillna(0)

        analyses.append(by_cust)

    if analyses:
        return pd.concat(analyses, ignore_index=True)

    return pd.DataFrame()


def calculate_agent_productivity(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate agent-level productivity metrics."""

    bookings = data.get('booking_log')
    if bookings is None or 'agent_name' not in bookings.columns:
        return pd.DataFrame()

    agg_dict = {
        'booking_id': 'count',
        'total_revenue': 'sum',
    }

    if 'gross_margin' in bookings.columns:
        agg_dict['gross_margin'] = 'sum'

    productivity = bookings.groupby('agent_name').agg(agg_dict).reset_index()
    productivity = productivity.rename(columns={'booking_id': 'booking_count'})

    # Add averages
    productivity['avg_revenue_per_booking'] = (
        productivity['total_revenue'] / productivity['booking_count']
    ).fillna(0)

    if 'gross_margin' in productivity.columns:
        productivity['avg_margin_per_booking'] = (
            productivity['gross_margin'] / productivity['booking_count']
        ).fillna(0)

    # Add rework metrics if available
    if 'was_rebooked' in bookings.columns:
        rebook_by_agent = bookings[bookings['was_rebooked'] == 'Yes'].groupby('agent_name')['booking_id'].count().reset_index()
        rebook_by_agent.columns = ['agent_name', 'rebook_count']
        productivity = productivity.merge(rebook_by_agent, on='agent_name', how='left')
        productivity['rebook_count'] = productivity['rebook_count'].fillna(0)
        productivity['rebook_rate'] = (
            productivity['rebook_count'] / productivity['booking_count'] * 100
        ).fillna(0)

    return productivity.sort_values('booking_count', ascending=False)


def calculate_carrier_performance(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate carrier/airline performance metrics."""

    bookings = data.get('booking_log')
    if bookings is None or 'airline' not in bookings.columns:
        return pd.DataFrame()

    agg_dict = {
        'booking_id': 'count',
        'total_revenue': 'sum',
    }

    if 'gross_margin' in bookings.columns:
        agg_dict['gross_margin'] = 'sum'

    carrier = bookings.groupby('airline').agg(agg_dict).reset_index()
    carrier = carrier.rename(columns={'booking_id': 'booking_count'})

    # Add margin percentage
    if 'gross_margin' in carrier.columns:
        carrier['margin_pct'] = (carrier['gross_margin'] / carrier['total_revenue'] * 100).fillna(0)

    # Add rebook metrics
    if 'was_rebooked' in bookings.columns:
        rebook = bookings[bookings['was_rebooked'] == 'Yes'].groupby('airline').agg({
            'booking_id': 'count',
            'rebooking_cost': 'sum' if 'rebooking_cost' in bookings.columns else 'count'
        }).reset_index()
        rebook.columns = ['airline', 'rebook_count', 'total_rebooking_cost']
        carrier = carrier.merge(rebook, on='airline', how='left')
        carrier['rebook_count'] = carrier['rebook_count'].fillna(0)
        carrier['total_rebooking_cost'] = carrier['total_rebooking_cost'].fillna(0)
        carrier['rebook_rate'] = (carrier['rebook_count'] / carrier['booking_count'] * 100).fillna(0)

    return carrier.sort_values('booking_count', ascending=False)


# =============================================================================
# TIME SERIES DATA
# =============================================================================

def calculate_daily_metrics(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate daily metrics for trend charts."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    df = bookings.copy()
    df['date'] = df['booking_date'].dt.date

    daily = df.groupby('date').agg({
        'booking_id': 'count',
        'total_revenue': 'sum',
    }).reset_index()

    daily = daily.rename(columns={'booking_id': 'booking_count'})
    daily['date'] = pd.to_datetime(daily['date'])

    return daily


def calculate_weekly_metrics(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate weekly metrics for trend charts."""

    bookings = data.get('booking_log')
    if bookings is None:
        return pd.DataFrame()

    df = bookings.copy()
    df['week'] = df['booking_date'].dt.to_period('W').dt.start_time

    weekly = df.groupby('week').agg({
        'booking_id': 'count',
        'total_revenue': 'sum',
    }).reset_index()

    weekly = weekly.rename(columns={'booking_id': 'booking_count'})

    return weekly


def calculate_monthly_metrics(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Calculate monthly metrics combining financial and booking data."""

    financial = data.get('financial_transactions')
    bookings = data.get('booking_log')

    results = []

    # Financial monthly
    if financial is not None:
        fin_monthly = financial.copy()
        fin_monthly['month'] = fin_monthly['transaction_date'].dt.to_period('M').dt.to_timestamp()

        fin_agg = fin_monthly.groupby(['month', 'category'])['amount'].sum().unstack(fill_value=0).reset_index()
        fin_agg.columns.name = None

        # Standardize column names
        col_map = {}
        for col in fin_agg.columns:
            if col == 'month':
                continue
            col_map[col] = f"fin_{col.lower().replace(' ', '_')}"
        fin_agg = fin_agg.rename(columns=col_map)

        results.append(fin_agg)

    # Booking monthly
    if bookings is not None:
        book_monthly = bookings.copy()
        book_monthly['month'] = book_monthly['booking_date'].dt.to_period('M').dt.to_timestamp()

        agg_dict = {
            'booking_id': 'count',
            'total_revenue': 'sum',
        }
        if 'gross_margin' in book_monthly.columns:
            agg_dict['gross_margin'] = 'sum'

        book_agg = book_monthly.groupby('month').agg(agg_dict).reset_index()
        book_agg = book_agg.rename(columns={
            'booking_id': 'booking_count',
            'total_revenue': 'booking_revenue',
            'gross_margin': 'booking_margin'
        })

        results.append(book_agg)

    if len(results) == 2:
        # Merge financial and booking
        return results[0].merge(results[1], on='month', how='outer').sort_values('month')
    elif len(results) == 1:
        return results[0].sort_values('month')

    return pd.DataFrame()
