import requests

BASE_URL = "http://127.0.0.1:8000"


# -----------------------------
# Upload PDF
# -----------------------------
def upload_pdf(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    return requests.post(
        f"{BASE_URL}/api/files/upload-pdf",
        files=files
    )


# -----------------------------
# AI Summary
# -----------------------------
def generate_summary(file_id):

    return requests.post(
        f"{BASE_URL}/api/ai/summarize/{file_id}"
    )


# -----------------------------
# Medical Analysis
# -----------------------------
def analyze_report(file_id):

    return requests.get(
        f"{BASE_URL}/api/medical-analysis/analyze/{file_id}"
    )


# -----------------------------
# Create Embeddings
# -----------------------------
def create_embeddings(file_id):

    return requests.post(
        f"{BASE_URL}/api/embeddings/create/{file_id}"
    )


# -----------------------------
# Chatbot
# -----------------------------
def chat_with_report(file_id, question):

    payload = {
        "file_id": file_id,
        "question": question
    }

    return requests.post(
        f"{BASE_URL}/api/chat/",
        json=payload
    )


# -----------------------------
# Generate PDF
# -----------------------------
def generate_report(file_id):

    return requests.get(
        f"{BASE_URL}/api/report/generate/{file_id}"
    )


# -----------------------------
# Translation
# -----------------------------
def translate(text, language):

    payload = {
        "text": text,
        "language": language
    }

    return requests.post(
        f"{BASE_URL}/api/translation/translate",
        json=payload
    )