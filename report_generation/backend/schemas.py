from pydantic import BaseModel
from typing import List

class AbnormalFinding(BaseModel):
    test: str
    value: float
    normal_range: str
    status: str
    page_no: int

class DoctorReport(BaseModel):
    summary: dict
    abnormal_findings: List[AbnormalFinding]
