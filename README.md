# 🏥 AI Medical Report Analysis Assistant

An AI-powered application that analyzes medical reports using **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)**. The system extracts information from uploaded PDF reports, retrieves relevant medical context using vector search, and generates easy-to-understand summaries, abnormal findings, possible conditions, and recommendations.

---

## 📌 Features

* 📄 Upload medical reports in PDF format
* 🔍 Extract text from reports
* ✂️ Intelligent text chunking
* 🧠 Generate embeddings using OpenAI Embeddings
* 📚 Store embeddings in ChromaDB
* 🔎 Retrieve relevant medical context using RAG
* 🤖 Analyze reports using OpenAI GPT
* 📋 Generate:

  * Patient Summary
  * Abnormal Parameters
  * Possible Conditions
  * Recommendations
  * Diet Suggestions
  * Lifestyle Advice

---

## 🏗️ Project Architecture

```text
                 PDF Medical Report
                        │
                        ▼
              Text Extraction (PyMuPDF)
                        │
                        ▼
                 Text Chunking
                        │
                        ▼
             OpenAI Embedding Model
                        │
                        ▼
                  ChromaDB Vector DB
                        │
              Similarity Search (RAG)
                        │
                        ▼
              Retrieved Relevant Context
                        │
                        ▼
               OpenAI GPT (LLM)
                        │
                        ▼
        AI Medical Report Analysis & Recommendations
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI

### Frontend

* Streamlit

### AI & RAG

* OpenAI GPT
* OpenAI Embeddings
* Retrieval-Augmented Generation (RAG)

### Vector Database

* ChromaDB

### PDF Processing

* PyMuPDF (fitz)

### Other Libraries

* LangChain
* python-dotenv
* Uvicorn

---

## 📂 Project Structure

```text
AI-MEDICAL-REPORT-ASSISTANT
│
├── backend
│   ├── api
│   ├── models
│   ├── prompts
│   ├── services
│   ├── uploads
│   ├── extracted_text
│   ├── utils
│   ├── vector_db
│   └── main.py
│
├── frontend
│   ├── assets
│   ├── components
│   └── pages
│
├── data
├── notebooks
├── tests
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/MAHESH-B-RMKCSE/AI-MEDICAL-REPORT-ASSISTANT.git
```

```bash
cd AI-MEDICAL-REPORT-ASSISTANT
```

### Create a Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the backend folder.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Backend

```bash
cd backend
```

```bash
uvicorn main:app --reload
```

FastAPI will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run the Frontend

Open another terminal.

```bash
cd frontend
```

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. Upload a medical report (PDF).
2. Extract report text.
3. Split the text into chunks.
4. Generate embeddings.
5. Store embeddings in ChromaDB.
6. Retrieve relevant chunks using RAG.
7. Send retrieved context to the LLM.
8. Generate:

   * Summary
   * Abnormal Parameters
   * Possible Conditions
   * Recommendations
9. Display the analysis in the Streamlit interface.

---

## 📸 Future Improvements

* Support multiple report formats
* Medical image analysis
* Voice-based report explanation
* Multi-language support
* Patient history integration
* Doctor dashboard
* Hospital management integration

---

## 🎯 Applications

* Hospitals
* Clinics
* Diagnostic Centers
* Telemedicine Platforms
* Healthcare Assistants
* Medical Education

---

## 👨‍💻 Author

**Mahesh B**

B.E. Computer Science and Engineering

RMK Engineering College

GitHub: https://github.com/MAHESH-B-RMKCSE

---

## 📄 License

This project is intended for educational and research purposes.

---

## ⭐ Acknowledgements

* OpenAI
* LangChain
* ChromaDB
* FastAPI
* Streamlit
* PyMuPDF
