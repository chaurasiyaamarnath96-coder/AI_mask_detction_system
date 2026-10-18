import streamlit as st
import requests
import av
import cv2
import numpy as np
import base64

from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase
)

API_URL = "https://ai-mask-detction-system-1.onrender.com/predict-frame"


class VideoProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(
            format="bgr24"
        )

        success, buffer = cv2.imencode(
            ".jpg",
            img
        )

        if not success:
            return frame

        files = {
            "file": (
                "frame.jpg",
                buffer.tobytes(),
                "image/jpeg"
            )
        }

        try:

            response = requests.post(
                API_URL,
                files=files,
                timeout=5
            )

            if response.status_code != 200:
                return frame

            data = response.json()

            if "annotated_image" not in data:
                return frame

            img_data = base64.b64decode(
                data["annotated_image"]
            )

            np_img = np.frombuffer(
                img_data,
                dtype=np.uint8
            )

            annotated = cv2.imdecode(
                np_img,
                cv2.IMREAD_COLOR
            )

            if annotated is None:
                return frame

            return av.VideoFrame.from_ndarray(
                annotated,
                format="bgr24"
            )

        except Exception as e:

            print("Webcam Error:", e)

            return frame


st.set_page_config(
    page_title="Live Webcam Detection",
    layout="wide"
)

st.title("📹 Live Face Mask Detection")

st.info(
    "Webcam frames are sent to FastAPI for YOLO inference."
)

webrtc_streamer(
    key="webcam",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    }
)