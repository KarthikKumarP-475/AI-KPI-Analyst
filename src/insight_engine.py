# Business Summary Generator

def build_business_summary(results):

    kpis = results["kpis"]
    monthly = results["monthly_trend"]

    summary = {}

    # Core KPI summary
    summary["total_revenue"] = round(kpis.get("total_revenue", 0), 2)
    summary["avg_order_value"] = round(kpis.get("average_order_value", 0), 2)
    summary["total_quantity"] = kpis.get("total_quantity", 0)

    # Trend detection
    if monthly is not None and len(monthly) > 1:

        first = monthly.iloc[0, 1]
        last = monthly.iloc[-1, 1]

        growth = ((last - first) / first) * 100 if first != 0 else 0
        summary["growth_percent"] = round(growth, 2)

    print("Business summary created")
    return summary


# Convert Summary into AI context
def create_ai_context(summary):

    context = f"""
    Business Performance Summary:

    Total Revenue: {summary['total_revenue']}
    Average Order Value: {summary['avg_order_value']}
    Total Quantity Sold: {summary['total_quantity']}
    Revenue Growth: {summary.get('growth_percent', 0)}%

    Provide executive-level insights explaining performance trends.
    """

    print("AI context prepared")
    return context


# Insight Engine Runner
def run_insight_engine(results):

    print("\n--- RUNNING INSIGHT ENGINE ---")

    summary = build_business_summary(results)
    context = create_ai_context(summary)

    print("--- INSIGHT ENGINE READY ---\n")

    return context