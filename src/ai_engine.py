import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use ONE model name from list_models()
model = genai.GenerativeModel("models/gemini-2.5-flash-lite")


def generate_ai_insights(context):

    print("\n--- GENERATING AI INSIGHTS (GEMINI) ---")

    prompt = f"""
    You are a senior business analyst.

    Analyze the KPI summary below and provide
    concise executive insights explaining trends,
    risks, and opportunities.

    {context}
    """

    response = model.generate_content(prompt)

    insights = response.text

    print("--- AI INSIGHTS GENERATED ---\n")

    return insights