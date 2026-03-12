from src.ai_engine import model


def analyze_dataset_structure(profile):

    columns = profile.get("columns", [])
    numeric_columns = profile.get("numeric_columns", [])
    categorical_columns = profile.get("categorical_columns", [])

    prompt = f"""
You are a data analyst.

A dataset has been uploaded. Analyze the dataset structure and explain what type of business dataset it appears to be.

Columns:
{columns}

Numeric Columns:
{numeric_columns}

Categorical Columns:
{categorical_columns}

Explain:

1. What type of dataset this likely is
2. What metrics may represent revenue or quantity
3. What dimensions may be useful for analysis

Provide a short explanation.
"""

    response = model.generate_content(prompt)

    return response.text