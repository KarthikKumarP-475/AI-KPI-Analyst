def profile_dataset(df):

    profile = {
        "date_columns": [],
        "numeric_columns": [],
        "categorical_columns": []
    }

    for col in df.columns:
        col_lower = col.lower()

        if "date" in col_lower or "time" in col_lower:
            profile["date_columns"].append(col)

        elif df[col].dtype in ["int64", "float64"]:
            profile["numeric_columns"].append(col)

        else:
            profile["categorical_columns"].append(col)

    print("Dataset profile created")
    return profile