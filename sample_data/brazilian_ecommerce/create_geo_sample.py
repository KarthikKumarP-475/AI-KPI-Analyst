import pandas as pd

df = pd.read_csv("sample_data/brazilian_ecommerce/olist_geolocation_dataset.csv")

sample = df.sample(5000, random_state=42)

sample.to_csv("sample_data/brazilian_ecommerce/olist_geolocation_sample.csv", index=False)

print("Sample dataset created.")