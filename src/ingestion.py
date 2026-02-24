import pandas as pd

def load_data(path):

    print("Loading dataset...")

    if path.endswith(".csv"):
        df = pd.read_csv(path)

    elif path.endswith(".xlsx") or path.endswith(".xls"):
        df = pd.read_excel(path)

    else:
        raise ValueError("Unsupported file format")

    print("Dataset Loaded Successfully")
    return df