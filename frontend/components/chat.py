import streamlit as st
from services.api import chat_with_report


def chat_component():

    if "file_id" not in st.session_state:
        return

    st.header("💬 Chat with Medical Report")

    question = st.text_input(
        "Ask a question about your medical report:"
    )

    if st.button("Ask AI"):

        if not question.strip():

            st.warning("Please enter a question.")

            return

        with st.spinner("Searching report and generating answer..."):

            response = chat_with_report(
                st.session_state["file_id"],
                question
            )

        if response.status_code == 200:

            data = response.json()

            st.success("Answer")
            st.session_state["chat_done"] = True

            st.write(data.get("answer", "No answer found."))

        else:

            st.error("Chat failed")

            try:
                st.json(response.json())
            except Exception:
                st.write(response.text)