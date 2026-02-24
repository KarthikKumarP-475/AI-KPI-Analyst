import pandas as pd

def fix_dates(df, date_columns):

    print("Parsing date columns...")

    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    return df