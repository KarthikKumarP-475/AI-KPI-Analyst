from src.ai_engine import model


def build_question_prompt(context, user_question, kpis, signals, dimensions, monthly_trend):

    prompt = f"""
You are a senior business analyst.

Use ONLY the business information provided below to answer the user's question.

KPI SUMMARY:
{kpis}

ANALYTICAL SIGNALS:
{signals}

DIMENSION ANALYSIS:
{dimensions}

MONTHLY TREND DATA:
{monthly_trend}

BUSINESS CONTEXT:
{context}

USER QUESTION:
{user_question}

Provide a clear, concise business explanation using the data above.
"""

    return prompt


def ask_business_question(context, question, results):

    kpis = results.get("kpis", {})
    signals = results.get("signals", {})
    dimensions = results.get("dimensions", {})
    monthly_trend = results.get("monthly_trend")

    print("\n--- ANALYZING QUESTION ---")

    prompt = build_question_prompt(
        context,
        question,
        kpis,
        signals,
        dimensions,
        monthly_trend
    )

    response = model.generate_content(prompt)
    answer = response.text

    print("--- ANSWER GENERATED ---\n")

    return answer