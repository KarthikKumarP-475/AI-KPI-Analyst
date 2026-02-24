from src.cleaning_rules.duplicate_rule import remove_duplicates
from src.cleaning_rules.date_rule import fix_dates
from src.cleaning_rules.missing_values import handle_missing_values
from src.cleaning_rules.datatype_rule import fix_datatypes
from src.cleaning_rules.business_rule import apply_business_rules


def run_cleaning_pipeline(df, profile):

    print("\n--- STARTING CLEANING PIPELINE ---")

    # 1️⃣ Always safe operations
    df = remove_duplicates(df)

    # 2️⃣ Date handling (only if dates exist)
    if profile.get("date_columns"):
        df = fix_dates(df, profile["date_columns"])

    # 3️⃣ Datatype correction
    df = fix_datatypes(df)

    # 4️⃣ Missing value handling
    df = handle_missing_values(df)

    # 5️⃣ Business logic rules
    df = apply_business_rules(df, profile)

    print("--- CLEANING COMPLETE ---\n")

    return df
