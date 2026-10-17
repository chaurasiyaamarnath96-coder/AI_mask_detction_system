from pydantic import BaseModel
class PredictionResponse(BaseModel):
    total_faces: int
    masked: int
    unmasked: int
    incorrectly_masked: int
    compliance_percentage: float