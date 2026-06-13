from pydantic import BaseModel

class InvestigationResult(BaseModel):
    customer_id: str
    risk_score: int
    risk_level: str
    findings: list[str]
    recommendation: str