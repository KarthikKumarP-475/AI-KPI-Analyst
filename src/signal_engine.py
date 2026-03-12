import pandas as pd

# Measures whether the business is growing
def revenue_growth(monthly_revenue):
    if len(monthly_revenue) < 2:
        return None

    last = monthly_revenue.iloc[-1]
    prev = monthly_revenue.iloc[-2]

    if prev == 0:
        return None

    return (last - prev) / prev

# Measures how unstable revenue is
def revenue_volatility(monthly_revenue):

    if monthly_revenue.mean() == 0:
        return None

    return monthly_revenue.std() / monthly_revenue.mean()

# Simply classification of Revenue Trend 
def revenue_trend(monthly_revenue):

    if len(monthly_revenue) < 2:
        return "unknown"

    if monthly_revenue.iloc[-1] > monthly_revenue.iloc[0]:
        return "increasing"

    elif monthly_revenue.iloc[-1] < monthly_revenue.iloc[0]:
        return "decreasing"

    return "stable"

# Measures dependency on one Market segment
def market_concentration(dimension_analysis):

    concentration = {}

    for dim, values in dimension_analysis.items():

        total = sum(values.values())
        top = max(values.values())

        concentration[dim] = top / total

    return concentration


# This measures how dependent the business is on a few customers, products, or markets.
def concentration_risk(dimension_analysis):

    risk = {}

    for dim, values in dimension_analysis.items():

        sorted_values = sorted(values.values(), reverse=True)

        top3 = sum(sorted_values[:3])
        total = sum(sorted_values)

        if total == 0:
            risk[dim] = None
        else:
            risk[dim] = top3 / total

    return risk


# Generate signals from KPI results
def generate_signals(kpi_results):

    monthly = kpi_results["monthly_trend"]
    dimensions = kpi_results["dimension_analysis"]

    signals = {}

    signals["revenue_growth_rate"] = revenue_growth(monthly)
    signals["revenue_volatility"] = revenue_volatility(monthly)
    signals["trend_direction"] = revenue_trend(monthly)
    signals["market_concentration"] = market_concentration(dimensions)

    # NEW SIGNAL
    signals["concentration_risk"] = concentration_risk(dimensions)

    return signals