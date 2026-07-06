import os
from uuid import uuid4

from fastapi import APIRouter, UploadFile, File

from backend.services.pdf_service import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "backend/uploads"
EXTRACTED_DIR = "backend/extracted_text"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACTED_DIR, exist_ok=True)


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    file_id = str(uuid4())

    pdf_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}.pdf"
    )

    with open(pdf_path, "wb") as buffer:
        buffer.write(await file.read())

    # Automatically extract text
    text = extract_text_from_pdf(pdf_path)

    text_path = os.path.join(
        EXTRACTED_DIR,
        f"{file_id}.txt"
    )

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return {
        "message": "PDF uploaded successfully",
        "file_id": file_id,
        "text_length": len(text)
    }


@router.get("/extract/{file_id}")
def extract_pdf(file_id: str):

    pdf_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}.pdf"
    )

    if not os.path.exists(pdf_path):
        return {"error": "File not found"}

    text = extract_text_from_pdf(pdf_path)

    text_path = os.path.join(
        EXTRACTED_DIR,
        f"{file_id}.txt"
    )

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return {
        "message": "Text extracted successfully",
        "file_id": file_id,
        "text_length": len(text)
    }