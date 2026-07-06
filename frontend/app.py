import streamlit as st

from components.upload import upload_component
from components.summary import summary_component
from components.analysis import analysis_component
from components.embeddings import embeddings_component
from components.chat import chat_component
from components.report import report_component
from components.translation import translation_component

st.set_page_config(
    page_title="AI Medical Report Assistant",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Medical Report Assistant")
st.markdown("## 📊 Workflow Progress")

steps = {
    "Upload PDF": "file_id" in st.session_state,
    "AI Summary": st.session_state.get("summary_done", False),
    "Medical Analysis": st.session_state.get("analysis_done", False),
    "Embeddings": st.session_state.get("embeddings_done", False),
    "AI Chat": st.session_state.get("chat_done", False),
    "PDF Report": st.session_state.get("report_done", False),
    "Translation": st.session_state.get("translation_done", False),
}

completed = sum(steps.values())
progress = completed / len(steps)

st.progress(progress)

for step, done in steps.items():
    if done:
        st.success(f"✅ {step}")
    else:
        st.info(f"⏳ {step}")

st.sidebar.title("🩺 Navigation")

page = st.sidebar.radio(
    "Choose a Module",
    [
        "📤 Upload Report",
        "📝 AI Summary",
        "🩺 Medical Analysis",
        "🧠 Embeddings",
        "💬 AI Chat",
        "📄 PDF Report",
        "🌐 Translation"
    ]
)

st.sidebar.markdown("---")

if "file_id" in st.session_state:
    st.sidebar.success("✅ Report Uploaded")
    st.sidebar.write(f"**File ID:**")
    st.sidebar.code(st.session_state["file_id"])
else:
    st.sidebar.warning("⚠️ No report uploaded")

st.sidebar.markdown("---")
st.sidebar.caption("AI Medical Report Assistant")
st.sidebar.caption("FastAPI • Streamlit • LangChain")
st.sidebar.caption("ChromaDB • Ollama • Llama 3.2")


if page == "📤 Upload Report":
    upload_component()

elif page == "📝 AI Summary":
    summary_component()

elif page == "🩺 Medical Analysis":
    analysis_component()

elif page == "🧠 Embeddings":
    embeddings_component()

elif page == "💬 AI Chat":
    chat_component()

elif page == "📄 PDF Report":
    report_component()

elif page == "🌐 Translation":
    translation_component()