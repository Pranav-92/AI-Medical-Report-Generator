from fastapi import APIRouter
from services.ollama_client import explain_for_patient

router = APIRouter(prefix="/explain", tags=["Explain"])

@router.post("/patient")
async def explain_patient(doctor_json: dict):
    return explain_for_patient(doctor_json)
