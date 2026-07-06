from fastapi import APIRouter
from backend.services.embedding_service import create_embeddings

router = APIRouter()


@router.post("/create/{file_id}")
def create_vector_embeddings(file_id: str):

    try:
        chunks = create_embeddings(file_id)

        return {
            "message": "Embeddings created successfully",
            "chunks_created": chunks
        }

    except Exception as e:

        return {
            "error": str(e)
        }