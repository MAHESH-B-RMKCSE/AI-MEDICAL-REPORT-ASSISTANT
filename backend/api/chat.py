from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.chatbot_service import ask_question

router = APIRouter()


# Temporary in-memory chat history
# Structure:
# {
#     file_id: [
#         {
#             "user": "...",
#             "assistant": "..."
#         }
#     ]
# }
chat_history = {}


class ChatRequest(BaseModel):
    file_id: str
    question: str


@router.post("/")
def chat(request: ChatRequest):

    try:

        history = chat_history.get(request.file_id, [])

        answer = ask_question(
            request.file_id,
            request.question,
            history
        )

        history.append(
            {
                "user": request.question,
                "assistant": answer
            }
        )

        chat_history[request.file_id] = history

        return {
            "answer": answer,
            "history_length": len(history)
        }

    except Exception as e:

        return {
            "error": str(e)
        }


@router.delete("/{file_id}")
def clear_chat(file_id: str):

    chat_history.pop(file_id, None)

    return {
        "message": "Chat history cleared."
    }