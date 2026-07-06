from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import ollama

VECTOR_DB = "backend/vector_db"


def ask_question(file_id: str, question: str, history=None):
    """
    Answers a user's question using Retrieval-Augmented Generation (RAG).

    Args:
        file_id (str): Uploaded report ID.
        question (str): User's question.
        history (list): Optional chat history.
            Example:
            [
                {
                    "user": "What is my CRP level?",
                    "assistant": "Your CRP level is 12 mg/L."
                }
            ]
    """

    # Initialize embedding model
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    # Load the correct ChromaDB collection
    collection_name = f"report_{file_id}"

    vector_db = Chroma(
        persist_directory=VECTOR_DB,
        embedding_function=embeddings,
        collection_name=collection_name
    )

    # Retrieve relevant chunks
    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Build conversation history
    history_text = ""

    if history:
        for chat in history:
            history_text += f"User: {chat['user']}\n"
            history_text += f"Assistant: {chat['assistant']}\n\n"

    # Create prompt
    prompt = f"""
You are an expert AI Medical Assistant.

Your job is to answer ONLY using the information from the uploaded medical report.

Rules:
1. Do not make up information.
2. If the answer is not present in the report, reply:
   "I could not find this information in the uploaded report."
3. Keep answers clear and concise.
4. If appropriate, mention abnormal values and their significance.

Conversation History:
{history_text}

Medical Report:
{context}

Current Question:
{question}

Answer:
"""

    # Generate response
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]