# AI Business KPI Analyst

AI Business KPI Analyst is an AI-powered analytics application that automatically analyzes business datasets, generates KPIs, and produces executive insights using AI.

The system simulates an **AI-powered business analyst** capable of profiling datasets, calculating key performance metrics, identifying trends, and answering business questions through natural language.

Users can upload a dataset and instantly receive automated performance analysis, KPI dashboards, and AI-generated business explanations.

---

## Problem Statement

Business teams often rely on analysts to manually clean datasets, calculate KPIs, and interpret trends. This project demonstrates how AI and automated analytics pipelines can assist in performing these tasks instantly.

The system simulates an **AI-powered business analyst** capable of analyzing datasets and explaining performance trends.

---

## Key Highlights

- Built a modular **analytics pipeline architecture**
- Automated **KPI generation and trend detection**
- Integrated **Gemini AI for executive business insights**
- Implemented **Ask-Your-Data natural language interface**
- Developed an **interactive Streamlit dashboard**
- Generated **automated downloadable business reports**

## System Architecture

    Dataset Upload
            │
            ▼
    Data Profiler
            │
            ▼
    Cleaning Engine
            │
            ▼
        KPI Engine
            │
            ▼
    Revenue Trend Chart
            │
            ▼
    Dimension Analysis
            │
            ▼
    Signal Engine
            │
            ▼
    Insight Engine
            │
            ▼
        Gemini AI
            │
            ▼
    Streamlit Web App
            │
            ▼
Business Report Generator

---

## Features

- Automated dataset ingestion
- Rule-based data cleaning pipeline
- Automatic KPI generation
- Dynamic categorical dimension analysis
- AI-generated executive insights
- Interactive Ask-Your-Data interface
- Streamlit web application
- Automated business report generation (PDF)

## Application Preview

### Dashboard
![Dashboard](assets/app_dashboard.png)

### KPI
![KPI](assets/key_performance_indicators.png)

### AI Insights
![AI Insights](assets/ai_insights.png)

### AI Analyst
![AI Analyst](assets/ai_analyst.png)

---

## Ask Your Data (AI Analyst)

Users can ask natural language questions about their dataset.

Example questions:

- Which country generates the most revenue?
- Which month performed worst?
- Which category drives the most sales?
- Is revenue improving over time?
- Summarize overall business performance.

The system builds structured context from KPIs and sends it to Gemini AI to generate business explanations.

---

## Tech Stack

Python — Core application logic  
Pandas — Data processing and KPI calculations  
Streamlit — Interactive web application  
Google Gemini API — AI-generated insights and question answering  
ReportLab — Automated PDF report generation  
python-dotenv — Secure API key management

---

## Demo Datasets

Sample datasets are provided in the `sample_data/` directory for quick testing.

Included datasets:

- **Online Retail** — Transactional retail dataset with country-level sales.
- **Superstore Sales** — Retail dataset with region, category, and segment dimensions.
- **Brazilian E-Commerce** — Multi-table e-commerce dataset containing order and customer information.

Users can upload any of these datasets directly in the Streamlit application to explore KPI analysis and AI-generated insights.

### Brazilian E-Commerce Dataset Note

The original dataset contains several relational tables.
Due to GitHub file size limits, the full geolocation dataset is not included in this repository.

A smaller sample file is provided instead.

The complete dataset can be downloaded from Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## How to Run

Clone the repository: https://github.com/KarthikKumarP-475/AI-KPI-Analyst.git

Install dependencies: python -m pip install -r requirements.txt

Add your Gemini API key in `.env`: GEMINI_API_KEY=your_api_key_here

Run the application: streamlit run app.py

## Development Timeline

Day 1 — Data ingestion and cleaning pipeline  
Day 2 — KPI engine and trend analysis  
Day 3 — Insight engine  
Day 4 — Gemini AI integration  
Day 5 — Ask-Your-Data interface  
Day 6 — Streamlit application  
Day 7 — Documentation improvements  
Day 8 — PDF report generation  
Day 9 — Dimension analysis
Day 10 — Final Polish

## Version 2 Enhancements — Analytical Signal Engine

## Day 11 Progress — Analytical Signals
Introduced an analytical signal engine to enhance business intelligence capabilities.

The system now derives higher-level signals from KPI outputs to provide deeper performance interpretation before AI analysis.

Signals implemented:

• Revenue growth rate  
• Revenue volatility  
• Revenue trend classification  
• Market concentration indicators  
• Top-3 revenue concentration risk

These signals provide structured analytical context that improves the quality of AI-generated executive insights.

## Day 12 Progress — Revenue Trend Visualization

Added a revenue trend visualization to the dashboard.

The application now displays a monthly revenue trend chart derived from KPI engine outputs. This allows users to visually analyze revenue growth patterns, volatility, and seasonal fluctuations before reviewing AI-generated insights.

## Day 13 Progress — Structured AI Question Context

Improved the Ask-Your-Data system by providing structured analytical context to the AI model.

The question engine now supplies KPIs, analytical signals, dimension analysis, and trend data when answering user questions. This significantly improves the quality and reliability of AI-generated explanations.

## Day 14 Progress — Automatic Dataset Understanding

Added an AI-powered dataset understanding module.

When a dataset is uploaded, the system now analyzes the dataset structure and explains:

• The likely business domain of the dataset  
• Which columns may represent revenue or quantity  
• Which categorical dimensions can drive analysis  

This feature helps users quickly understand the structure and analytical potential of their data.

## Future Improvements

- Profit and margin analysis
- Customer cohort analysis
- Multi-table relational dataset support
- Advanced analytics signals (volatility, concentration)
- Interactive visual dashboards