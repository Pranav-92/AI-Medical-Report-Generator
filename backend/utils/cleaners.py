from utils.medical_terms import MEDICAL_TERMS

def is_medical_line(line: str) -> bool:
    line_lower = line.lower()
    return any(term in line_lower for term in MEDICAL_TERMS)
