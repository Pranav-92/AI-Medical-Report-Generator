import requests
import json

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "llama3"   # change if using mistral / phi3 etc.


def generate_patient_explanation(lab_json: dict) -> str:

    prompt = f"""
You are a medical assistant.

Convert the following lab report JSON into a patient-friendly explanation.

Rules:
- Use simple English
- Explain abnormal findings
- Add causes
- Add lifestyle actions
- Do NOT use medical jargon
- Make it structured

Lab Report JSON:
{json.dumps(lab_json, indent=2)}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        return "AI explanation could not be generated."

    return response.json()["response"]
