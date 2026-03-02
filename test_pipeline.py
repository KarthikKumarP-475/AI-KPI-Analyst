from src.ingestion import load_data
from src.profiler import profile_dataset
from src.cleaner import run_cleaning_pipeline
from src.kpi_engine import run_kpi_engine
from src.insight_engine import run_insight_engine

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