# AI Business KPI Analyst

An AI-powered analytics application that automatically analyzes business datasets, generates KPIs, and produces executive insights using AI.

Users can upload a dataset and instantly receive performance analysis and business explanations.

---

## Problem Statement

Business teams often rely on analysts to manually clean datasets, calculate KPIs, and interpret trends. This project demonstrates how AI and automated analytics pipelines can assist in performing these tasks instantly.

The system simulates an **AI-powered business analyst** capable of analyzing datasets and explaining performance trends.

---

## System Architecture

Dataset Upload  
↓  
Data Profiler  
↓  
Cleaning Engine  
↓  
KPI Engine  
↓  
Insight Engine  
↓  
Gemini AI  
↓  
Streamlit Web App

---

## Features

- Automatic dataset ingestion (CSV / Excel)
- Automated data cleaning pipeline
- KPI generation and trend analysis
- AI-generated executive insights
- Ask-your-data question interface
- Streamlit web application for interaction

---

## Tech Stack

- Python
- Pandas
- Streamlit
- Google Gemini API
- Modular Data Pipeline Architecture

---

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

## How to Run

Clone the repository: https://github.com/KarthikKumarP-475/AI-KPI-Analyst.git

Install dependencies: python -m pip install -r requirements.txt

Add your Gemini API key in `.env`: GEMINI_API_KEY=your_api_key_here

Run the application: streamlit run app.py

## Day 1

- Created project structure
- Implemented dataset ingestion module
- Built dataset profiling system
- Developed rule-based data cleaning engine

## Day 2

- Implemented KPI Engine
- Automatic detection of revenue, quantity, and date fields
- Generated business KPIs
- Added monthly revenue trend analysis

## Day 3

- Built Insight Engine to convert KPIs into structured summaries
- Added growth trend detection
- Prepared AI-ready business context

## Day 4

- Integrated Google Gemini AI for automated insights
- Implemented ai_engine.py
- Generated executive-level business explanations
Example output:
 "Revenue growth appears driven by increasing order quantities, while mid-period fluctuations suggest seasonal demand patterns."

## Day 5

- Added AI Ask-Your-Data interface
- Users can ask business questions about dataset performance
Example questions:
- Which period performed worst?
- Is revenue improving over time?
- Summarize overall business performance.

## Day 6

- Built Streamlit web application
- Upload dataset and automatically generate KPIs
- AI insights and interactive Q&A interface
- The system now functions as a mini AI-powered analytics product.