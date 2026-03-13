from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import textwrap


def generate_report(kpis, insights, brief, recommendations, signals):

    filename = "business_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "AI Business KPI Report")

    y -= 40

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Generated: {datetime.datetime.now()}")

    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Key Metrics")

    y -= 20

    for key, value in kpis.items():
        c.setFont("Helvetica", 12)
        c.drawString(60, y, f"{key}: {value}")
        y -= 20

    y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "AI Insights")

    y -= 20

    text_object = c.beginText(60, y)
    text_object.setFont("Helvetica", 12)

    wrapped_lines = textwrap.wrap(insights, 80)

    for line in wrapped_lines:
        text_object.textLine(line)

    c.drawText(text_object)

    # Executive Summary Section
    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Executive Summary")

    y -= 20

    text_object = c.beginText(60, y)
    text_object.setFont("Helvetica", 12)

    wrapped_lines = textwrap.wrap(brief, 80)

    for line in wrapped_lines:
        text_object.textLine(line)

    c.drawText(text_object)

    y = text_object.getY() - 20

    # Business Recommendation Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Business Recommendations")

    y -= 20

    text_object = c.beginText(60, y)
    text_object.setFont("Helvetica", 12)

    wrapped_lines = textwrap.wrap(recommendations, 80)

    for line in wrapped_lines:
        text_object.textLine(line)

    c.drawText(text_object)

    y = text_object.getY() - 20
    
    # Analytical Signals Section
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Analytical Signals")

    y -= 20

    for key, value in signals.items():

        if key == "revenue_anomalies":
            continue

        c.setFont("Helvetica", 12)
        c.drawString(60, y, f"{key}: {value}")

        y -= 20

    # Revenue Anomalies Section
    anomalies = signals.get("revenue_anomalies", [])

    if anomalies:

        y -= 10

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Revenue Anomalies")

        y -= 20

        for anomaly in anomalies:

            c.setFont("Helvetica", 12)
            c.drawString(60, y, anomaly)

            y -= 20
            
    c.save()
    return filename