from fastapi import FastAPI
import uvicorn
from app.router import invoice_router

app = FastAPI(title="Invoice API")


@app.get("/api/health-check")
async def health_check():
    return {"status": "ok"}


app.include_router(invoice_router.router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
