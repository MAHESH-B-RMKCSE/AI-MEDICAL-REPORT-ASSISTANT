import streamlit as st
from services.api import translate


def translation_component():

    st.header("🌐 Translate Medical Report")

    language = st.selectbox(
        "Select Language",
        [
            "English",
            "Telugu",
            "Hindi",
            "Tamil",
            "Kannada",
            "Malayalam",
            "Marathi"
        ]
    )

    text = st.text_area("Enter text to translate")

    if st.button("Translate"):

        response = translate(text, language)

        if response.status_code == 200:

            st.success("Translation Complete")
            st.session_state["translation_done"] = True

            st.write(
                response.json()["translated_text"]
            )

        else:

            st.error(response.text)