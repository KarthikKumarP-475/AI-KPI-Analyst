from src.ai_engine import model


def explain_chart(chart_type, data_summary):

    prompt = f"""
You are a senior business analyst.

Explain the following business chart in clear executive language.

Chart Type:
{chart_type}

Data Summary:
{data_summary}

Focus on trends, patterns, and business implications.
"""

    response = model.generate_content(prompt)

    return response.text