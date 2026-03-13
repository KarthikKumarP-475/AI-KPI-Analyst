import streamlit as st
import pandas as pd

from src.profiler import profile_dataset
from src.cleaner import run_cleaning_pipeline
from src.kpi_engine import run_kpi_engine
from src.insight_engine import run_insight_engine
from src.ai_engine import generate_ai_insights
from src.question_engine import ask_business_question
from src.report_engine import generate_report
from src.signal_engine import generate_signals
from src.dataset_understanding import analyze_dataset_structure
from src.brief_engine import generate_executive_brief
from src.query_engine import generate_pandas_query, run_generated_query
from src.recommendation_engine import generate_recommendations
from src.chart_explainer import explain_chart


# A Formatting Function for numbers
def format_large_number(value):

    if value is None:
        return value

    if abs(value) >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"

    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"{value/1_000:.2f}K"

    return f"{value:.2f}"

st.set_page_config(page_title="AI KPI Analyst", layout="wide")

st.title("🚀 AI Business KPI Analyst")

uploaded_file = st.file_uploader("Upload a business dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")
    st.subheader("📂 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isna().sum().sum())

    st.subheader("🔎 Dataset Preview")
    st.dataframe(df.head(10))

    st.subheader("🔎 Interactive Filters")

    filter_columns = [
        col for col in df.columns
        if df[col].dtype == "object" and df[col].nunique() < 50
    ]

    filters = {}

    for col in filter_columns:

        selected_values = st.multiselect(
            f"Filter by {col}",
            options=sorted(df[col].dropna().unique())
        )

        if selected_values:
            filters[col] = selected_values
    filtered_df = df.copy()

    for col, values in filters.items():
        filtered_df = filtered_df[filtered_df[col].isin(values)]

    st.subheader("📊 Column Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.values
    })

    st.dataframe(dtype_df)

    # Run pipeline
    profile = profile_dataset(filtered_df)

    # Analyze dataset structure
    dataset_summary = analyze_dataset_structure(profile)

    # Show dataset understanding
    st.subheader("🧠 Dataset Understanding")
    st.info(dataset_summary)

    # Run cleaning pipeline
    clean_df = run_cleaning_pipeline(filtered_df, profile)

    # Safety check
    if clean_df is None or clean_df.empty:
        st.error("⚠️ Dataset does not contain sufficient data for analysis.")
        st.stop()

    # Run KPI engine
    results = run_kpi_engine(clean_df)

    # -----------------------------
    # Detected Analytical Columns
    # -----------------------------
    st.subheader("🧭 Detected Analytical Columns")

    detected_cols = results.get("detected_columns", {})

    if detected_cols:

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Revenue Column",
            detected_cols.get("revenue", "Not detected")
        )

        col2.metric(
            "Quantity Column",
            detected_cols.get("quantity", "Not detected")
        )

        col3.metric(
            "Date Column",
            detected_cols.get("date", "Not detected")
        )

    clean_df = run_cleaning_pipeline(df, profile)

    st.subheader("💾 Download Cleaned Dataset")

    clean_csv = clean_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned Data (CSV)",
        data=clean_csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )
    st.subheader("🧹 Cleaned Dataset Preview")
    st.dataframe(clean_df.head(10))

    # Safety check before running KPI engine
    if clean_df is None or clean_df.empty:
        st.error("⚠️ Dataset does not contain sufficient data for analysis.")
        st.stop()

    results = run_kpi_engine(clean_df)

    # Generate analytical signals
    signals = {}

    if results:
        signals = generate_signals(results)

    # Add signals into results dictionary
    results["signals"] = signals

    # Build AI context
    ai_context = run_insight_engine(results)

    # Display KPIs
    st.subheader("📊 Key Performance Indicators")

    kpis = results["kpis"]

    monthly_trend = results.get("monthly_trend")

    revenue_growth = None

    if monthly_trend is not None and len(monthly_trend) > 1:

        # If DataFrame, extract numeric column
        if isinstance(monthly_trend, pd.DataFrame):
            monthly_trend = monthly_trend.select_dtypes(include="number").iloc[:, 0]

        latest = monthly_trend.iloc[-1]
        previous = monthly_trend.iloc[-2]

        if previous != 0:
            revenue_growth = ((latest - previous) / previous) * 100


    col1, col2, col3 = st.columns(3)

    if revenue_growth is not None:
        growth_text = f"{revenue_growth:.2f}%"
    else:
        growth_text = None


    col1.metric(
        "Total Revenue",
        f"${format_large_number(kpis.get('total_revenue',0))}",
        growth_text
    )

    col2.metric(
        "Avg Order Value",
        f"${format_large_number(kpis.get('average_order_value',0))}"
    )

    col3.metric(
        "Total Quantity",
        format_large_number(kpis.get("total_quantity", 0))
    )

    # Show a monthly revenue trend chart using the KPI engine output
    st.subheader("📈 Revenue Trend")

    monthly_trend = results.get("monthly_trend")

    if monthly_trend is not None:

        if isinstance(monthly_trend, pd.DataFrame):
            monthly_trend = monthly_trend.select_dtypes(include="number").iloc[:, 0]

        trend_df = pd.DataFrame({
            "Month": monthly_trend.index.astype(str),
            "Revenue": monthly_trend.values
        })

        trend_df = trend_df.set_index("Month")

        st.line_chart(trend_df)

    # Chart Explainer Function
    trend_summary = monthly_trend.describe().to_string()
    st.subheader("📊 Revenue Trend Explanation")

    trend_explanation = explain_chart(
        "Revenue Trend",
        trend_summary
    )

    st.write(trend_explanation)
    # Show Dimension Results in Streamlit
    chart_view = st.radio(
        "Dimension Visualization",
        ["Chart View", "Table View"]
    )

    st.subheader("📊 Dimension Analysis")

    dimensions = results.get("dimensions", {})

    for dim, values in dimensions.items():

        st.write(f"Top {dim} Performance")

        dim_df = pd.DataFrame(
            list(values.items()),
            columns=[dim, "Revenue"]
        ).sort_values("Revenue", ascending=False)

        dim_df["Revenue"] = dim_df["Revenue"].apply(format_large_number)

        chart_df = dim_df.set_index(dim)

        if chart_view == "Chart View":
            st.bar_chart(chart_df)
            
            dim_summary = dim_df.head().to_string()
            st.write("📊 AI Explanation")

            dim_explanation = explain_chart(
                f"{dim} Revenue Distribution",
                dim_summary
            )

            st.write(dim_explanation)
        else:
            st.dataframe(dim_df)

        with st.expander(f"View {dim} Data Table"):
            st.dataframe(dim_df)
        
    # ===============================
    # Analytical Signals
    # ===============================

    st.subheader("📈 Analytical Signals")

    for key, value in signals.items():
        nice_key = key.replace("_", " ").title()
        st.write(f"**{nice_key}:** {value}")

    st.subheader("🚨 Revenue Anomalies")

    anomalies = signals.get("revenue_anomalies", [])

    if anomalies:
        for anomaly in anomalies:
            st.warning(anomaly)
    else:
        st.write("No significant anomalies detected.")

    for dim, value in signals.get("concentration_risk", {}).items():
        st.write(f"Top 3 {dim} share:", round(value * 100, 2), "%")

    # AI Insights
    st.subheader("🤖 AI Executive Insights")

    insights = generate_ai_insights(ai_context)
    st.write(insights)

    st.subheader("📝 AI Executive Brief")

    brief = generate_executive_brief(results)
    st.write(brief)

    st.download_button(
        label="Download Executive Brief",
        data=brief,
        file_name="executive_brief.txt",
        mime="text/plain"
    )

    st.subheader("📌 Business Recommendations")
    recommendations = generate_recommendations(results)
    st.write(recommendations)

    # Question Section
    st.subheader("💬 Ask the AI Analyst")

    user_question = st.text_input("Ask a business question:")

    if user_question:
        answer = ask_business_question(ai_context, user_question, results)
        st.write(answer)

    # NLP Query-Ask a question about the dataset
    st.subheader("📊 Natural Language Data Query")

    query_question = st.text_input("Ask a question about the dataset (data query):")

    if query_question:

        query = generate_pandas_query(df.columns.tolist(), query_question)

        st.write("Generated Query:")
        st.code(query)

        result = run_generated_query(df, query)

        st.write("Query Result:")
        st.write(result)
    # Generate Business Report
    if st.button("Generate Business Report"):

        report_file = generate_report(kpis, insights)

        if report_file:
            with open(report_file, "rb") as f:
                st.download_button(
                    label="Download Report",
                    data=f,
                    file_name="business_report.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("Report generation failed.")