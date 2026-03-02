from src.ingestion import load_data
from src.profiler import profile_dataset
from src.cleaner import run_cleaning_pipeline
from src.kpi_engine import run_kpi_engine
from src.insight_engine import run_insight_engine
from src.ai_engine import generate_ai_insights
from src.question_engine import ask_business_question

# Load dataset
df = load_data("data/raw/online_retail.xlsx")

# Profile dataset
profile = profile_dataset(df)

# Run cleaning engine
clean_df = run_cleaning_pipeline(df, profile)

print(clean_df.head())
print(clean_df.info())

# Results of KPI Engine
results = run_kpi_engine(clean_df)

print(results["kpis"])
print(results["monthly_trend"].head())

# Results of AI context
ai_context = run_insight_engine(results)
print(ai_context)

# Results of AI insights
ai_insights = generate_ai_insights(ai_context)
print(ai_insights)

while True:
    question = input("\nAsk a business question (type 'exit' to stop): ")
    if question.lower() == "exit":
        break
    answer = ask_business_question(ai_context, question)
    print("\nAI Analyst:", answer)
