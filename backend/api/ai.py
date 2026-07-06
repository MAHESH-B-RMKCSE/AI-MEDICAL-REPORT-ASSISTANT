import os
from fastapi import APIRouter
from backend.services.llm_service import summarize_medical_text

router = APIRouter()

EXTRACTED_DIR = "backend/extracted_text"
SUMMARY_DIR = "backend/summaries"

os.makedirs(SUMMARY_DIR, exist_ok=True)


@router.post("/summarize/{file_id}")
def summarize(file_id: str):

    file_path = os.path.join(EXTRACTED_DIR, f"{file_id}.txt")

    if not os.path.exists(file_path):
        return {"error": "Extracted file not found"}

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    summary = summarize_medical_text(text)

    summary_path = os.path.join(SUMMARY_DIR, f"{file_id}.txt")

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary)

    return {
        "message": "Summary generated successfully",
        "file_id": file_id,
        "summary": summary,
        "summary_file": summary_path
    }