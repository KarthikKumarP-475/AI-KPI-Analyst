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

st.set_page_config(page_title="AI KPI Analyst", layout="wide")

st.title("🚀 AI Business KPI Analyst")

uploaded_file = st.file_uploader("Upload a business dataset (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")

    # Run pipeline
    profile = profile_dataset(df)

    # Analyze dataset structure
    dataset_summary = analyze_dataset_structure(profile)

    # Show dataset understanding
    st.subheader("🧠 Dataset Understanding")
    st.info(dataset_summary)

    clean_df = run_cleaning_pipeline(df, profile)
    results = run_kpi_engine(clean_df)

    # Generate analytical signals
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
        f"${kpis.get('total_revenue',0):,.2f}",
        growth_text
    )

    col2.metric(
        "Avg Order Value",
        f"${kpis.get('average_order_value',0):,.2f}"
    )

    col3.metric(
        "Total Quantity",
        kpis.get("total_quantity", 0)
    )

    # Show a monthly revenue trend chart using the KPI engine output
    st.subheader("📈 Revenue Trend")

    monthly_trend = results.get("monthly_trend")

    if monthly_trend is not None:

        trend_df = pd.DataFrame({
            "Month": monthly_trend.index.astype(str),
            "Revenue": monthly_trend.values
        })

        st.line_chart(trend_df.set_index("Month"))

    # Show Dimension Results in Streamlit
    st.subheader("📊 Dimension Analysis")

    dimensions = results.get("dimensions", {})

    for dim, values in dimensions.items():

        st.write(f"Top {dim} Performance")

        dim_df = pd.DataFrame(
            list(values.items()),
            columns=[dim, "Revenue"]
        ).sort_values("Revenue", ascending=False)

        st.bar_chart(dim_df.set_index(dim))

        st.dataframe(dim_df)
        
    # ===============================
    # Analytical Signals
    # ===============================

    st.subheader("📈 Analytical Signals")

    for key, value in signals.items():
        nice_key = key.replace("_", " ").title()
        st.write(f"**{nice_key}:** {value}")


    st.subheader("⚠️ Concentration Risk")

    st.subheader("🚨 Revenue Anomalies")

    anomalies = signals.get("revenue_anomalies", [])

    if anomalies:
        for anomaly in anomalies:
            st.warning(anomaly)
    else:
        st.write("No significant anomalies detected.")

    for dim, value in signals["concentration_risk"].items():
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