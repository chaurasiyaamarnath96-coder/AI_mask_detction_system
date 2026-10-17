import json
import os
from datetime import datetime

LOG_FILE = "detection_logs.json"


def save_detection_log(
    masked,
    unmasked,
    incorrect,
    compliance
):

    record = {
        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "masked": masked,
        "unmasked": unmasked,
        "incorrect": incorrect,
        "compliance": compliance
    }

    logs = []

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as f:

            try:
                logs = json.load(f)

            except:
                logs = []

    logs.append(record)

    with open(LOG_FILE, "w") as f:

        json.dump(
            logs,
            f,
            indent=4
        )