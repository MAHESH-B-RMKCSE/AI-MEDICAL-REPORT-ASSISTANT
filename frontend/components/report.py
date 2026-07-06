import os
import streamlit as st

from services.api import generate_report


def report_component():

    if "file_id" not in st.session_state:
        return

    st.header("📄 AI Medical Report")

    st.info(
        f"Current File ID: {st.session_state['file_id']}"
    )

    if st.button("Generate PDF Report"):

        with st.spinner("Generating Medical Report..."):

            response = generate_report(
                st.session_state["file_id"]
            )

        # -----------------------------
        # Backend Error
        # -----------------------------

        if response.status_code != 200:

            try:
                st.error(response.json()["detail"])

            except Exception:
                st.error(response.text)

            return

        # -----------------------------
        # Validate PDF
        # -----------------------------

        content_type = response.headers.get(
            "content-type",
            ""
        )

        if "application/pdf" not in content_type:

            st.error("Backend did not return a PDF.")

            try:
                st.json(response.json())

            except Exception:
                st.write(response.text)

            return

        # -----------------------------
        # Save PDF
        # -----------------------------

        os.makedirs(
            "downloads",
            exist_ok=True
        )

        pdf_path = os.path.join(
            "downloads",
            f"{st.session_state['file_id']}.pdf"
        )

        with open(pdf_path, "wb") as f:
            f.write(response.content)

        # -----------------------------
        # Verify PDF
        # -----------------------------

        if os.path.getsize(pdf_path) == 0:

            st.error("Generated PDF is empty.")

            return

        st.success("✅ PDF Generated Successfully!")
        st.session_state["report_done"] = True

        st.write(
            f"Saved to: {pdf_path}"
        )

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="📥 Download Medical Report",
                data=pdf,
                file_name="AI_Medical_Report.pdf",
                mime="application/pdf"
            )