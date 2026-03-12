from src.ai_engine import model


def analyze_dataset_structure(profile):

    columns = profile.get("columns", [])
    numeric_columns = profile.get("numeric_columns", [])
    categorical_columns = profile.get("categorical_columns", [])

    prompt = f"""
You are a senior data analyst.

Analyze the dataset structure below and determine the likely business dataset type.

Possible dataset types include:
- Retail sales
- E-commerce orders
- Financial transactions
- Inventory management
- Generic business data

Dataset Information:

Columns:
{columns}

Numeric Columns:
{numeric_columns}

Categorical Columns:
{categorical_columns}

Tasks:
1. Identify the likely dataset type.
2. Explain what the dataset appears to represent.
3. Identify which columns may represent revenue, quantity, or dates.

Provide a short explanation.
"""

    response = model.generate_content(prompt)

    return response.text