from fastapi import APIRouter
import json
import os

router = APIRouter()

LOG_FILE = "detection_logs.json"


@router.get("/logs")
def get_logs():

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:

        try:
            logs = json.load(f)
            return logs

        except Exception:
            return []