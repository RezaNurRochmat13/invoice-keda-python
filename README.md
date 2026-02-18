Invoice Generator API

A clean architecture-based backend API built with FastAPI to generate professional PDF invoices dynamically.

🚀 Features

Generate professional-styled PDF invoices

Clean Architecture structure (Router → Service → Core)

In-memory PDF streaming (no file storage required)

Swagger documentation

Production-ready project structure

🏗 Architecture Overview

The application follows a layered Clean Architecture approach:

Client
   ↓
Router (HTTP Controller)
   ↓
Service (Business Logic / Use Case)
   ↓
Core (PDF Generator - Domain Logic)
   ↓
Streaming PDF Response

Project Structure
project-root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── router/
│   ├── services/
│   └── core/
│
├── requirements.txt
├── start-dev.sh
└── README.md

📦 Requirements

Python 3.10+

pip

virtual environment (recommended)

🔧 Local Development Setup
1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Development Server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


Swagger documentation:

http://localhost:8000/docs

🧪 Health Check
curl http://localhost:8000/api/health-check


Response:

{
  "status": "ok"
}

🧾 Generate Invoice
Endpoint
POST /generate-invoice

Request Body
{
  "customer_name": "John Doe",
  "guide_name": "Bali Explorer",
  "date": "2026-04-05",
  "price": 150.00,
  "currency": "USD"
}

Response

Content-Type: application/pdf

Returns downloadable professional invoice PDF

Example cURL
curl -X POST http://localhost:8000/generate-invoice \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe",
    "guide_name": "Bali Explorer",
    "date": "2026-04-05",
    "price": 150.00,
    "currency": "USD"
  }' --output invoice.pdf

🛠 Tech Stack

FastAPI

Uvicorn

ReportLab

Pydantic

🔐 Design Principles

Clear separation of concerns

Core logic independent from framework

Stateless service

In-memory PDF generation

Clean, testable service layer

📈 Possible Improvements

Replace float with Decimal for financial precision

Add tax and subtotal calculation

Add invoice number persistence

Add database storage

Add authentication

Add logging & exception middleware

Add unit and integration tests

Add Docker support

📄 License

MIT License