from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


def generate_patient_pdf(summary, findings, ai_text,
                         filename="Patient_Report.pdf"):

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Patient Health Report", styles["Title"]))
    story.append(Spacer(1, 12))

    # Summary
    story.append(Paragraph(
        f"<b>Total Tests Reviewed:</b> {summary.get('total_markers', 0)}",
        styles["Normal"]
    ))
    story.append(Paragraph(
        f"<b>Abnormal Findings:</b> {summary.get('abnormal_count', 0)}",
        styles["Normal"]
    ))

    story.append(Spacer(1, 18))

    # AI Explanation Section
    story.append(Paragraph("AI Health Explanation",
                           styles["Heading2"]))

    for line in ai_text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    story.append(Spacer(1, 20))

    # Doctor Note
    story.append(Paragraph(
        "<b>Doctor Consultation Recommended</b>",
        styles["Heading3"]
    ))

    story.append(Paragraph(
        "Please consult your doctor for professional medical advice.",
        styles["Normal"]
    ))

    doc.build(story)

    return filename
