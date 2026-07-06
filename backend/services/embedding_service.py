import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings


UPLOAD_FOLDER = "backend/extracted_text"
VECTOR_DB = "backend/vector_db"


def create_embeddings(file_id: str):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        f"{file_id}.txt"
    )

    if not os.path.exists(file_path):
        raise Exception("Extracted text not found.")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    collection_name = f"report_{file_id}"

    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB,
        collection_name=collection_name
    )

    vector_db.persist()

    return len(chunks)