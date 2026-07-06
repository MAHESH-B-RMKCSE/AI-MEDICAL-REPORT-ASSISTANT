from ollama import chat


def translate_text(text: str, language: str):

    prompt = f"""
You are a professional medical translator.

Translate the following medical text into {language}.

Rules:
- Keep medical terminology accurate.
- Do not add or remove information.
- Preserve headings and formatting.
- Return only the translated text.

Text:

{text}
"""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]