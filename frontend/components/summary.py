import streamlit as st
from services.api import generate_summary


def summary_component():

    if "file_id" not in st.session_state:
        return

    st.header("📝 AI Summary")

    if st.button("Generate AI Summary"):

        with st.spinner("Generating Summary..."):

            response = generate_summary(
                st.session_state["file_id"]
            )

        if response.status_code == 200:

            data = response.json()

            st.success("Summary Generated")
            st.session_state["summary_done"] = True

            if "summary" in data:
                st.write(data["summary"])
            else:
                st.json(data)

        else:

            st.error("Failed to generate summary")
            st.write(response.text)