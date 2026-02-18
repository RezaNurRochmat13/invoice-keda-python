from pydantic import BaseModel, Field
from datetime import date


class InvoiceRequest(BaseModel):
    customer_name: str = Field(..., min_length=1)
    guide_name: str = Field(..., min_length=1)
    date: date
    price: float = Field(..., gt=0)
    currency: str = Field(..., min_length=3, max_length=3)

    class Config:
        json_schema_extra = {
            "example": {
                "customer_name": "John Doe",
                "guide_name": "Bali Explorer",
                "date": "2026-04-05",
                "price": 150.00,
                "currency": "USD",
            }
        }

