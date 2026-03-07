import streamlit as st
import pandas as pd

from src.profiler import profile_dataset
from src.cleaner import run_cleaning_pipeline
from src.kpi_engine import run_kpi_engine
from src.insight_engine import run_insight_engine
from src.ai_engine import generate_ai_insights
from src.question_engine import ask_business_question
from src.report_engine import generate_report

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
    clean_df = run_cleaning_pipeline(df, profile)
    results = run_kpi_engine(clean_df)
    ai_context = run_insight_engine(results)

    # Display KPIs
    st.subheader("📊 Key Performance Indicators")

    kpis = results["kpis"]

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Revenue", round(kpis.get("total_revenue", 0), 2))
    col2.metric("Avg Order Value", round(kpis.get("average_order_value", 0), 2))
    col3.metric("Total Quantity", kpis.get("total_quantity", 0))

    # AI Insights
    st.subheader("🤖 AI Executive Insights")

    insights = generate_ai_insights(ai_context)
    st.write(insights)

    # Question Section
    st.subheader("💬 Ask the AI Analyst")

    user_question = st.text_input("Ask a business question:")

    if user_question:
        answer = ask_business_question(ai_context, user_question)
        st.write(answer)

    # Generate Business Report
    if st.button("Generate Business Report"):

        report_file = generate_report(kpis, insights)

        with open(report_file, "rb") as f:
            st.download_button(
                label="Download Report",
                data=f,
                file_name="business_report.pdf",
                mime="application/pdf"
            )