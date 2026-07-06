from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.upload import router as upload_router
from backend.api.ai import router as ai_router
from backend.api.medical_analysis import router as medical_router
from backend.api.embeddings import router as embeddings_router
from backend.api.chat import router as chat_router
from backend.api.report import router as report_router
from backend.api.translation import router as translation_router

app = FastAPI(
    title="AI Medical Report Assistant",
    version="1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home
@app.get("/")
def home():
    return {
        "message": "AI Medical Report Assistant API Running Successfully 🚀"
    }

# Upload & Extract PDF
app.include_router(
    upload_router,
    prefix="/api/files",
    tags=["Files"]
)

# AI Summary
app.include_router(
    ai_router,
    prefix="/api/ai",
    tags=["AI Summary"]
)

# Medical Analysis
app.include_router(
    medical_router,
    prefix="/api/medical-analysis",
    tags=["Medical Analysis"]
)

# Embeddings
app.include_router(
    embeddings_router,
    prefix="/api/embeddings",
    tags=["Embeddings"]
)

# Chat
app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"]
)

# Report
app.include_router(
    report_router,
    prefix="/api/report",
    tags=["Report"]
)

# Translation
app.include_router(
    translation_router,
    prefix="/api/translation",
    tags=["Translation"]
)