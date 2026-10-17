from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.yolo_service import predict_frame

router = APIRouter()


@router.post("/predict-frame")
async def predict_frame_endpoint(
    file: UploadFile = File(...)
):

    result = await predict_frame(file)

    return result