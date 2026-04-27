from fastapi import APIRouter, UploadFile, File , Depends
import shutil
import os
from app.services.azure_service import analyze_invoice
from app.services.normalizer_service import normalize_invoice
from app.services.db_service import save_invoice
from app.db.database import get_session
from sqlmodel import Session
from app.models.invoice import Invoice, Item
from sqlmodel import select
from app.schemas.factura_schema import FacturaPublic, ItemRead
from sqlalchemy.orm import selectinload



router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_invoice(
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_invoice(file_path)
    normalized = normalize_invoice(result)

    #  guardar en la base de datos
    save_invoice(session, normalized)

    return {
        "message": "Procesado con Azure",
        "raw": result,
        "data": normalized

    }

@router.get("/", response_model=list[FacturaPublic])
def get_facturas(session: Session = Depends(get_session)):
    
    statement = select(Invoice).options(
        selectinload(Invoice.items)
        
    )

    facturas = session.exec(statement).all()
    return facturas
