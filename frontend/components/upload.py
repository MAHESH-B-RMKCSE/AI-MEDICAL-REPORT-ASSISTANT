import streamlit as st
from services.api import upload_pdf


def upload_component():
    """
    Upload PDF Component
    """

    st.header("📄 Upload Medical Report")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file:

        st.info(f"Selected File: {uploaded_file.name}")

        if st.button("⬆️ Upload Report"):

            with st.spinner("Uploading PDF..."):

                response = upload_pdf(uploaded_file)

            if response.status_code == 200:

                data = response.json()

                st.success(data["message"])

                st.session_state["file_id"] = data["file_id"]

                st.code(data["file_id"])

            else:

                st.error("Upload Failed")

                st.write(response.text)