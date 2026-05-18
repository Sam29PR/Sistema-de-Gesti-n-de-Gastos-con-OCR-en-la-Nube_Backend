from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.facturas import router as facturas_router
from app.routers.ai_insights import router as ai_router
from app.db.database import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# EXISTENTE
app.include_router(facturas_router, prefix="/api/facturas")

# NUEVO (IA)
app.include_router(ai_router, prefix="/api/ai")


@app.get("/")
def root():
    return {"message": "API funcionando"}