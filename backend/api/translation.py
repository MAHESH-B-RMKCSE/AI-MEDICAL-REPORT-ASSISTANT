from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.translation_service import translate_text

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str
    language: str


@router.post("/translate")
def translate(request: TranslationRequest):

    translated = translate_text(
        request.text,
        request.language
    )

    return {
        "translated_text": translated
    }