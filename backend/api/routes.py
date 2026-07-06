from fastapi import APIRouter

from backend.api import upload
from backend.api import ai
from backend.api import medical_analysis
from backend.api import report
from backend.api import chat

from backend.api import embeddings

router = APIRouter()

router.include_router(
    chat.router,
    prefix="/chat",
    tags=["Chat"]
)

router.include_router(
    embeddings.router,
    prefix="/embeddings",
    tags=["Embeddings"]
)

# PDF Upload & Text Extraction
router.include_router(
    upload.router,
    prefix="/files",
    tags=["Files"]
)

# AI Summary
router.include_router(
    ai.router,
    prefix="/ai",
    tags=["AI Summary"]
)

# Medical Analysis
router.include_router(
    medical_analysis.router,
    prefix="/medical-analysis",
    tags=["Medical Analysis"]
)

# PDF Report Generation
router.include_router(
    report.router,
    prefix="/report",
    tags=["Report"]
)