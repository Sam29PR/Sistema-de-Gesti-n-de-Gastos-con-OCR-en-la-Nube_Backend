from fastapi import FastAPI
from app.routers.facturas import router as facturas_router
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔥 startup
    create_db_and_tables()
    yield
    # 🔻 shutdown (si lo necesitas después)


app = FastAPI(lifespan=lifespan)

app.include_router(facturas_router, prefix="/api/facturas")


@app.get("/")
def root():
    return {"message": "API funcionando"}