def apply_business_rules(df, profile):

    print("Applying business rules...")

    columns = [c.lower() for c in df.columns]

    if "quantity" in columns and "unitprice" in columns:
        df["Revenue"] = df["Quantity"] * df["UnitPrice"]
        print("Revenue column created")

    return df