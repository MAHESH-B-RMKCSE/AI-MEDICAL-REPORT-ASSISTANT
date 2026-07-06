import os
import json
from fastapi import APIRouter
from backend.services.medical_analysis_service import analyze_medical_report

router = APIRouter()

EXTRACTED_DIR = "backend/extracted_text"
ANALYSIS_DIR = "backend/analysis"

os.makedirs(ANALYSIS_DIR, exist_ok=True)


@router.get("/analyze/{file_id}")
def analyze(file_id: str):

    file_path = os.path.join(EXTRACTED_DIR, f"{file_id}.txt")

    if not os.path.exists(file_path):
        return {
            "error": "Extracted text file not found"
        }

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    analysis = analyze_medical_report(text)

    output_path = os.path.join(ANALYSIS_DIR, f"{file_id}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=4)

    return {
        "message": "Medical analysis completed successfully",
        "file_id": file_id,
        "analysis": analysis
    }