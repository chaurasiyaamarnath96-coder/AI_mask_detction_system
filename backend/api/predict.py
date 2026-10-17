from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from utils.file_utils import save_uploaded_file

from services.yolo_service import predict_image

router = APIRouter()

@router.post("/predict")

async def predict_endpoint(
    file: UploadFile = File(...)
):

    path = await save_uploaded_file(file)

    data =  predict_image(path)

    return data