from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
import cv2

from utils.video_converter import convert_avi_to_mp4
from utils.file_utils import save_uploaded_file
from services.yolo_service import predict_video

import os

router = APIRouter()


@router.post("/predict-video")
async def predict_video_endpoint(
    file: UploadFile = File(...)
):
   
    video_path = await save_uploaded_file(file)

    print("Uploaded:", video_path)

    result = predict_video(video_path)

    output_video = result["output_video"]

    if output_video.lower().endswith(".avi"):

        mp4_path = convert_avi_to_mp4(output_video)

            

        print("\n========== MP4 DEBUG ==========")

        print("MP4 Path:", mp4_path)
        print("MP4 Exists:", os.path.exists(mp4_path))

        if os.path.exists(mp4_path):

            print("MP4 Size:", os.path.getsize(mp4_path))

            cap = cv2.VideoCapture(mp4_path)

            print("Opened:", cap.isOpened())
            print("FPS:", cap.get(cv2.CAP_PROP_FPS))
            print("Frames:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

            cap.release()

    

        result["output_video"] = mp4_path

    return result
 
