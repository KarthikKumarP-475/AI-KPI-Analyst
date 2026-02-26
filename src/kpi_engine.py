# Detect business columns automatically
def detect_kpi_columns(df):

    columns = [c.lower() for c in df.columns]

    detected = {
        "revenue": None,
        "quantity": None,
        "date": None
    }

    for col in df.columns:
        name = col.lower()

        if any(k in name for k in ["revenue", "sales", "amount"]):
            detected["revenue"] = col

        if any(k in name for k in ["quantity", "qty", "units"]):
            detected["quantity"] = col

        if "date" in name or "time" in name:
            detected["date"] = col

    print("Detected KPI columns:", detected)
    return detected


# Create Core KPIs
def generate_basic_kpis(df, detected):

    kpis = {}

    revenue_col = detected["revenue"]
    quantity_col = detected["quantity"]

    if revenue_col:
        kpis["total_revenue"] = df[revenue_col].sum()
        kpis["average_order_value"] = df[revenue_col].mean()

    if quantity_col:
        kpis["total_quantity"] = df[quantity_col].sum()

    print("KPIs generated")
    return kpis


# Time Based Analysis
def revenue_over_time(df, detected):

    date_col = detected["date"]
    revenue_col = detected["revenue"]

    if not date_col or not revenue_col:
        return None

    df["YearMonth"] = df[date_col].dt.to_period("M")

    monthly = (
        df.groupby("YearMonth")[revenue_col]
        .sum()
        .reset_index()
    )

    print("Monthly trend created")
    return monthly


# Main KPI Engine Function
def run_kpi_engine(df):

    print("\n--- RUNNING KPI ENGINE ---")

    detected = detect_kpi_columns(df)

    kpis = generate_basic_kpis(df, detected)

    monthly_trend = revenue_over_time(df, detected)

    print("--- KPI ENGINE COMPLETE ---\n")

    return {
        "kpis": kpis,
        "monthly_trend": monthly_trend
    }