import streamlit as st
from services.api import create_embeddings


def embeddings_component():

    if "file_id" not in st.session_state:
        return

    st.header("🧠 Create Embeddings")

    if st.button("Create Embeddings"):

        with st.spinner("Creating embeddings..."):

            response = create_embeddings(
                st.session_state["file_id"]
            )

        if response.status_code == 200:

            st.success("Embeddings Created Successfully!")
            st.session_state["embeddings_done"] = True

            try:
                st.json(response.json())
            except Exception:
                st.write(response.text)

        else:

            st.error(
                f"Error {response.status_code}"
            )

            st.write(response.text)