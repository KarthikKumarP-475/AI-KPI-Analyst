from src.ai_engine import model


def generate_executive_brief(results):

    kpis = results.get("kpis", {})
    signals = results.get("signals", {})
    dimensions = results.get("dimensions", {})

    prompt = f"""
You are a senior business analyst preparing a short executive briefing.

Use the data below to produce a concise business summary.

KPIs:
{kpis}

Analytical Signals:
{signals}

Dimension Analysis:
{dimensions}

Provide a short executive brief (3-5 sentences).
"""

    response = model.generate_content(prompt)

    return response.text