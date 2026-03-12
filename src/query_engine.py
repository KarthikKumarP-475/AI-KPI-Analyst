from src.ai_engine import model


# Generate a pandas query that runs on the dataset
def generate_pandas_query(columns, question):

    prompt = f"""
You are a data analyst.

A user asked a question about a dataset.

Dataset Columns:
{columns}

User Question:
{question}

Generate a pandas query that answers the question.

Rules:
- Use pandas syntax
- Assume dataframe name is df
- Return only the code
"""

    response = model.generate_content(prompt)

    return response.text.strip()


def run_generated_query(df, query):

    try:
        result = eval(query)
        return result
    except Exception as e:
        return f"Query execution failed: {e}"