from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.invoice_schema import InvoiceRequest
from app.services.invoice_service import InvoiceService

router = APIRouter(prefix="/api", tags=["Invoice"])


@router.post("/generate-invoice")
def generate_invoice(invoice: InvoiceRequest):
    pdf_buffer = InvoiceService.generate_invoice(invoice)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=invoice.pdf"
        },
    )
