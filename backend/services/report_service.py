import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from backend.services.chart_service import generate_chart
from reportlab.platypus import Image
from reportlab.lib.styles import getSampleStyleSheet

REPORT_DIR = "backend/reports"

os.makedirs(REPORT_DIR, exist_ok=True)


def generate_report(file_id: str, analysis: dict):

    pdf_path = os.path.join(REPORT_DIR, f"{file_id}.pdf")

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    # -----------------------------
    # Title
    # -----------------------------

    elements.append(
        Paragraph("<b>AI Medical Report Analysis</b>", styles["Title"])
    )

    elements.append(Spacer(1, 20))

    # -----------------------------
    # Patient Information
    # -----------------------------

    patient = analysis.get("patient_information", {})

    elements.append(
        Paragraph("<b>Patient Information</b>", styles["Heading2"])
    )

    patient_table = Table([
        ["Name", patient.get("name", "Not Available")],
        ["Age", patient.get("age", "Not Available")],
        ["Gender", patient.get("gender", "Not Available")]
    ])

    patient_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))

    elements.append(patient_table)
    elements.append(Spacer(1,20))

    # -----------------------------
    # Report Information
    # -----------------------------

    report = analysis.get("report_information", {})

    elements.append(
        Paragraph("<b>Report Information</b>", styles["Heading2"])
    )

    report_table = Table([
        ["Report Type", report.get("report_type", "Not Available")],
        ["Test Date", report.get("test_date", "Not Available")],
        ["Laboratory", report.get("laboratory", "Not Available")]
    ])

    report_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (0,-1), colors.lightgrey),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))

    elements.append(report_table)
    elements.append(Spacer(1,20))

    # -----------------------------
    # Abnormal Parameters
    # -----------------------------

    elements.append(
    Paragraph("<b>Abnormal Parameters</b>", styles["Heading2"])
    )

    data = [
        [
            "Test",
            "Value",
            "Status"
        ]
    ]

    for item in analysis.get("abnormal_parameters", []):

        data.append([
            item.get("parameter", ""),
            item.get("value", ""),
            item.get("unit", "")
        ])

    table = Table(data)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

    ]))

    elements.append(table)

    elements.append(Spacer(1,20))

    # -----------------------------
    # Possible Conditions
    # -----------------------------

    elements.append(
        Paragraph("<b>Possible Conditions</b>", styles["Heading2"])
    )

    conditions = analysis.get("possible_conditions", [])

    if conditions:

        for condition in conditions:

            elements.append(
                Paragraph(
                    f"• {condition}",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph("Not Available", styles["BodyText"])
        )

    elements.append(Spacer(1, 15))

    # -----------------------------
    # Medications
    # -----------------------------

    elements.append(
        Paragraph("<b>Possible Medications</b>", styles["Heading2"])
    )

    medications = analysis.get("medications", [])

    if medications:

        for med in medications:

            if isinstance(med, dict):

                medicine = med.get(
                    "medication",
                    "Not Available"
                )

                purpose = med.get(
                    "purpose",
                    "Not Available"
                )

                elements.append(
                    Paragraph(
                        f"• <b>{medicine}</b><br/>Purpose : {purpose}",
                        styles["BodyText"]
                    )
                )

            else:

                elements.append(
                    Paragraph(
                        f"• {med}",
                        styles["BodyText"]
                    )
                )

    else:

        elements.append(
            Paragraph(
                "No medications suggested.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    # -----------------------------
    # Recommendations
    # -----------------------------

    elements.append(
        Paragraph("<b>Recommendations</b>", styles["Heading2"])
    )

    recommendations = analysis.get("recommendations", [])

    if recommendations:

        for rec in recommendations:

            if isinstance(rec, dict):

                text = rec.get(
                    "recommendation",
                    "Not Available"
                )

            else:

                text = rec

            elements.append(
                Paragraph(
                    f"• {text}",
                    styles["BodyText"]
                )
            )

    else:

        elements.append(
            Paragraph(
                "No recommendations available.",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    # -----------------------------
    # Overall Health Risk
    # -----------------------------

    elements.append(
        Paragraph(
            "<b>Overall Health Risk</b>",
            styles["Heading2"]
        )
    )

    risk = analysis.get(
        "overall_health_risk",
        "Not Available"
    )

    elements.append(
        Paragraph(
            f"<b>{risk}</b>",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 20))

    # -----------------------------
    # Disclaimer
    # -----------------------------

    elements.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "This report is AI-generated and is intended only for educational and informational purposes. Please consult a qualified healthcare professional for diagnosis and treatment.",
            styles["BodyText"]
        )
    )
    chart = generate_chart(file_id, analysis)

    elements.append(
        Paragraph("<b>Health Dashboard</b>", styles["Heading2"])
    )

    elements.append(
        Image(chart, width=450, height=250)
    )

    doc.build(elements)

    return pdf_path