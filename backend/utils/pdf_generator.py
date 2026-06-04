from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime


def create_pdf(report_text):

    pdf_path = "executive_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "DecisionPilot AI Executive Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%b-%Y')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    

    content.append(
        Paragraph(
            report_text.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_path