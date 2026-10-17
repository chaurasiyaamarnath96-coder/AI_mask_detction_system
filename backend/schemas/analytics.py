from pydantic import BaseModel
class AnalyticsResponse(BaseModel):

    average_compliance_percentage: float
    total_detections: int
    total_violations: int