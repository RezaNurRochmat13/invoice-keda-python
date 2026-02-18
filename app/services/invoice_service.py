from app.core.pdf_generator import build_invoice_pdf
from app.schemas.invoice_schema import InvoiceRequest


class InvoiceService:

    @staticmethod
    def generate_invoice(invoice: InvoiceRequest):
        invoice_data = {
            "customer_name": invoice.customer_name,
            "guide_name": invoice.guide_name,
            "date": invoice.date.strftime("%Y-%m-%d"),
            "price": invoice.price,
            "currency": invoice.currency.upper(),
        }

        return build_invoice_pdf(invoice_data)
