from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def build_invoice_pdf(data: dict) -> BytesIO:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph("<b>INVOICE</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    table_data = [
        ["Customer Name", data["customer_name"]],
        ["Guide Name", data["guide_name"]],
        ["Date", data["date"]],
        ["Price", f'{data["currency"]} {data["price"]:,.2f}'],
    ]

    table = Table(table_data, colWidths=[150, 250])
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(table)
    elements.append(Spacer(1, 30))
    elements.append(Paragraph("Thank you for your business!", styles["Normal"]))

    doc.build(elements)
    buffer.seek(0)
    return buffer
