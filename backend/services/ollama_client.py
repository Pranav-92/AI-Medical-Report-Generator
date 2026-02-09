import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3"

def explain_for_patient(doctor_json):
    prompt = f"""
You are a medical assistant.
Explain the following abnormal lab results in SIMPLE language for a patient.
Do NOT give medical advice.
Do NOT mention doctors.
Do NOT suggest medicines.

JSON:
{doctor_json}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    return {
        "patient_explanation": response.json().get("response", "")
    }
