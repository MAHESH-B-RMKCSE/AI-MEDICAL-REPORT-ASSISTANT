import json
from ollama import chat


def analyze_medical_report(text: str):
    """
    Analyze a medical report using Ollama and return structured JSON.
    """

    prompt = f"""
You are an expert medical AI assistant.

Analyze the following medical report.

IMPORTANT RULES

1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT wrap the JSON inside ``` blocks.
4. Do NOT invent patient information.
5. If information is missing, return "Not Available".
6. Extract every abnormal laboratory parameter.
7. Determine the patient's overall health risk as Low, Moderate or High.
8. If medicines are not explicitly mentioned, suggest ONLY commonly recommended medications that a doctor MAY consider based on the report.
9. Recommendations should be short sentences.

Return JSON in EXACTLY this format:

{{
  "patient_information": {{
      "name": "",
      "age": "",
      "gender": ""
  }},

  "report_information": {{
      "report_type": "",
      "test_date": "",
      "laboratory": ""
  }},

  "abnormal_parameters": [
      {{
          "parameter": "",
          "value": "",
          "unit": "",
          "reference_range": "",
          "status": ""
      }}
  ],

  "possible_conditions":[
      ""
  ],

  "medications":[
      {{
          "medication":"",
          "purpose":""
      }}
  ],

  "recommendations":[
      {{
          "recommendation":""
      }}
  ],

  "overall_health_risk":""
}}

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

    result = response["message"]["content"]

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        analysis = json.loads(result)

    except Exception:

        analysis = {
            "patient_information": {
                "name": "Not Available",
                "age": "Not Available",
                "gender": "Not Available"
            },
            "report_information": {
                "report_type": "Not Available",
                "test_date": "Not Available",
                "laboratory": "Not Available"
            },
            "abnormal_parameters": [],
            "possible_conditions": [],
            "medications": [],
            "recommendations": [],
            "overall_health_risk": "Not Available"
        }

    analysis.setdefault("patient_information", {})
    analysis.setdefault("report_information", {})
    analysis.setdefault("abnormal_parameters", [])
    analysis.setdefault("possible_conditions", [])
    analysis.setdefault("medications", [])
    analysis.setdefault("recommendations", [])
    analysis.setdefault("overall_health_risk", "Not Available")

    patient = analysis["patient_information"]

    patient.setdefault("name", "Not Available")
    patient.setdefault("age", "Not Available")
    patient.setdefault("gender", "Not Available")

    report = analysis["report_information"]

    report.setdefault("report_type", "Not Available")
    report.setdefault("test_date", "Not Available")
    report.setdefault("laboratory", "Not Available")

    for item in analysis["abnormal_parameters"]:

        item.setdefault("parameter", "Not Available")
        item.setdefault("value", "Not Available")
        item.setdefault("unit", "")
        item.setdefault("reference_range", "Not Available")
        item.setdefault("status", "Not Available")

    cleaned_medications = []

    for med in analysis["medications"]:

        if isinstance(med, str):

            cleaned_medications.append({
                "medication": med,
                "purpose": "Not Available"
            })

        elif isinstance(med, dict):

            cleaned_medications.append({
                "medication": med.get("medication", "Not Available"),
                "purpose": med.get("purpose", "Not Available")
            })

    analysis["medications"] = cleaned_medications

    cleaned_recommendations = []

    for rec in analysis["recommendations"]:

        if isinstance(rec, str):

            cleaned_recommendations.append({
                "recommendation": rec
            })

        elif isinstance(rec, dict):

            cleaned_recommendations.append({
                "recommendation": rec.get(
                    "recommendation",
                    rec.get("description", "Not Available")
                )
            })

    analysis["recommendations"] = cleaned_recommendations

    return analysis