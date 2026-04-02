from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.azure_service import analyze_invoice
from app.services.normalizer_service import normalize_invoice

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_invoice(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_invoice(file_path)
    normalized = normalize_invoice(result)

    return {
        "message": "Procesado con Azure",
        "raw": result,
        "data": normalized

    }