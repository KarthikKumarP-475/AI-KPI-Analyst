from src.ingestion import load_data
from src.profiler import profile_dataset
from src.cleaner import run_cleaning_pipeline

# Load dataset
df = load_data("data/raw/online_retail.xlsx")

# Profile dataset
profile = profile_dataset(df)

# Run cleaning engine
clean_df = run_cleaning_pipeline(df, profile)

print(clean_df.head())
print(clean_df.info())