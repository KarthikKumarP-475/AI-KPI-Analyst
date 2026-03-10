from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import textwrap


def generate_report(kpis, insights):

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

    c.save()
    return filename