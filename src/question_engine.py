def build_question_prompt(context, user_question):

    prompt = f"""
    You are a senior business analyst.

    Use ONLY the business information provided below
    to answer the user's question.

    BUSINESS CONTEXT:
    {context}

    USER QUESTION:
    {user_question}

    Provide a clear, concise business explanation.
    """

    return prompt


from src.ai_engine import model


def ask_business_question(context, question):

    print("\n--- ANALYZING QUESTION ---")

    prompt = build_question_prompt(context, question)
    response = model.generate_content(prompt)
    answer = response.text

    print("--- ANSWER GENERATED ---\n")
    return answer