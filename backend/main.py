from fastapi import FastAPI

from api.predict import router as predict_router
from api.logs import router as logs_router
from api.analytics import router as analytics_router
from api.video import router as video_router
from api.wecam import router as webcam_router

app = FastAPI(
    title="Face Mask Monitoring API"
)

app.include_router(
    predict_router,
    tags=["Prediction"]
)

app.include_router(
    logs_router,
    tags=["Logs"]
)

app.include_router(
    analytics_router,
    tags=["Analytics"]
)
app.include_router(
    video_router,
    tags=["Video Detection"]
)
app.include_router(
    webcam_router,
    tags=["Webcam Detection"]
)


@app.get("/")

def home():

    return {
        "message":
        "API Running Successfully"
    }