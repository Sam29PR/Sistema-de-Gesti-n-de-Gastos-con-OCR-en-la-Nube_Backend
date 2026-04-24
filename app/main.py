from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.facturas import router as facturas_router
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager

#from app.models.factura import Factura
#from app.models.item import Item


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🔥 startup
    create_db_and_tables()
    yield
    # 🔻 shutdown (si lo necesitas después)


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(facturas_router, prefix="/api/facturas")


@app.get("/")
def root():
    return {"message": "API funcionando"}