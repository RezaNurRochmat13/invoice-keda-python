from io import BytesIO
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import HRFlowable
from datetime import datetime


def build_invoice_pdf(data: dict) -> BytesIO:
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    elements = []

    styles = getSampleStyleSheet()

    # ========================
    # Custom Styles
    # ========================
    title_style = ParagraphStyle(
        name="InvoiceTitle",
        parent=styles["Title"],
        fontSize=22,
        textColor=colors.HexColor("#2E3A59"),
    )

    normal_style = ParagraphStyle(
        name="NormalStyle",
        parent=styles["Normal"],
        fontSize=11,
        textColor=colors.HexColor("#333333"),
    )

    label_style = ParagraphStyle(
        name="LabelStyle",
        parent=styles["Normal"],
        fontSize=10,
        textColor=colors.grey,
    )

    # ========================
    # Header
    # ========================
    elements.append(Paragraph("INVOICE", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
    elements.append(Spacer(1, 0.3 * inch))

    # ========================
    # Company Info (Static Example)
    # ========================
    elements.append(Paragraph("<b>Your Travel Company</b>", normal_style))
    elements.append(Paragraph("info@yourcompany.com", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    # ========================
    # Invoice Info Table
    # ========================
    invoice_meta = [
        ["Invoice Date:", datetime.now().strftime("%Y-%m-%d")],
        ["Service Date:", data["date"]],
        ["Invoice Number:", f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"],
    ]

    meta_table = Table(invoice_meta, colWidths=[120, 300])
    meta_table.setStyle(
        TableStyle(
            [
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.grey),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
            ]
        )
    )

    elements.append(meta_table)
    elements.append(Spacer(1, 0.5 * inch))

    # ========================
    # Customer Section
    # ========================
    elements.append(Paragraph("<b>Bill To:</b>", normal_style))
    elements.append(Paragraph(data["customer_name"], normal_style))
    elements.append(Spacer(1, 0.4 * inch))

    # ========================
    # Service Table
    # ========================
    service_table_data = [
        ["Description", "Guide", "Amount"],
        ["Tour Service", data["guide_name"], f'{data["currency"]} {data["price"]:,.2f}'],
    ]

    service_table = Table(service_table_data, colWidths=[200, 120, 100])
    service_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E3A59")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ALIGN", (2, 1), (2, -1), "RIGHT"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 11),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ]
        )
    )

    elements.append(service_table)
    elements.append(Spacer(1, 0.5 * inch))

    # ========================
    # Total Section
    # ========================
    total_data = [
        ["", ""],
        ["Total:", f'{data["currency"]} {data["price"]:,.2f}'],
    ]

    total_table = Table(total_data, colWidths=[320, 100])
    total_table.setStyle(
        TableStyle(
            [
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 1), (-1, 1), 12),
            ]
        )
    )

    elements.append(total_table)
    elements.append(Spacer(1, 0.7 * inch))

    # ========================
    # Footer
    # ========================
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(
        Paragraph(
            "Thank you for choosing our service.",
            label_style,
        )
    )

    doc.build(elements)
    buffer.seek(0)

    return buffer
