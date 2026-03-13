from src.ai_engine import model


def generate_recommendations(results):

    prompt = f"""
You are a senior business strategy consultant.

Using the business metrics below, generate 3–5 actionable business recommendations.

Focus on:
- revenue performance
- market concentration
- growth trends
- top-performing segments

BUSINESS DATA:
{results}

Provide concise, executive-level recommendations.
"""

    response = model.generate_content(prompt)

    return response.text