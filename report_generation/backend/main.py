from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

from pdf_generator import generate_patient_pdf
from ollama_client import generate_patient_explanation

app = FastAPI()


@app.post("/generate/patient-pdf")
def generate_pdf(payload: dict = Body(...)):

    summary = payload.get("summary", {})
    findings = payload.get("abnormal_findings", [])

    # 🔹 Generate AI text from Ollama
    ai_text = generate_patient_explanation(payload)

    # 🔹 Generate PDF
    filename = generate_patient_pdf(
        summary,
        findings,
        ai_text
    )

    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename="Patient_Report.pdf"
    )
