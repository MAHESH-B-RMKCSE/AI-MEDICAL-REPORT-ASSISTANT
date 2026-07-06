import json
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from backend.services.report_service import generate_report

router = APIRouter()

ANALYSIS_DIR = "backend/analysis"


@router.get("/generate/{file_id}")
def generate_pdf(file_id: str):

    json_path = os.path.join(
        ANALYSIS_DIR,
        f"{file_id}.json"
    )

    # Check analysis file exists
    if not os.path.exists(json_path):
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    # Load analysis JSON
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            analysis = json.load(f)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to read analysis file: {str(e)}"
        )

    # Generate PDF
    try:
        pdf_path = generate_report(file_id, analysis)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF generation failed: {str(e)}"
        )

    # Verify PDF exists
    if not os.path.exists(pdf_path):
        raise HTTPException(
            status_code=500,
            detail="PDF was not created."
        )

    # Verify PDF is not empty
    if os.path.getsize(pdf_path) == 0:
        raise HTTPException(
            status_code=500,
            detail="Generated PDF is empty."
        )

    return FileResponse(
        path=pdf_path,
        media_type="application/pdf",
        filename="AI_Medical_Report.pdf"
    )