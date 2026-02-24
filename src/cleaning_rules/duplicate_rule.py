def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicates")
    return df