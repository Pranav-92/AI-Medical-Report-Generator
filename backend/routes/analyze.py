from fastapi import APIRouter, UploadFile, File
from services.pdf_reader import extract_pdf_lines
from services.analyzer import analyze_lines
from services.doctor_formatter import format_doctor_output

router = APIRouter(prefix="/analyze", tags=["Analyze"])

@router.post("/pdf")
async def analyze_pdf(file: UploadFile = File(...)):
    lines = extract_pdf_lines(file.file)
    analyzed = analyze_lines(lines)
    return format_doctor_output(analyzed)
