from ollama import chat


def summarize_medical_text(text: str) -> str:
    """
    Summarize a medical report using Ollama (Llama 3.2).
    """

    prompt = f"""
You are an expert medical AI assistant.

Analyze the following medical report.

Provide:
1. Simple Summary
2. Abnormal Findings
3. Possible Health Concerns
4. Recommendations

Medical Report:

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