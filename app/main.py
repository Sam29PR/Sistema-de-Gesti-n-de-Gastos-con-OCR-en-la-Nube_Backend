from fastapi import FastAPI
from app.routers.facturas import router as facturas_router

app = FastAPI()

app.include_router(facturas_router, prefix="/api/facturas")


@app.get("/")
def root():
    return {"message": "API funcionando"}