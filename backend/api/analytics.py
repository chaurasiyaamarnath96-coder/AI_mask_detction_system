from fastapi import APIRouter

router = APIRouter()

@router.get("/analytics")

def analytics():

    return {

        "average_compliance": 89.4,

        "total_records": 120,

        "total_violations": 20
    }