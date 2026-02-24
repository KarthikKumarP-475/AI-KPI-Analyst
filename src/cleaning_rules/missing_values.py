import pandas as pd
from pandas.api.types import is_numeric_dtype


def handle_missing_values(df):

    print("Handling missing values...")

    for col in df.columns:

        # ✅ Numeric columns
        if is_numeric_dtype(df[col]):
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)

        # ✅ Non-numeric columns
        else:
            df[col] = df[col].fillna("Unknown")

    return df