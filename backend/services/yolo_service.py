from ultralytics import YOLO
import cv2
import base64
import os
from pathlib import Path
from utils.logger import save_detection_log

from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "best 1.pt"

model = YOLO(str(MODEL_PATH))

def predict_image(image_path):

    results = model.predict(
        source=image_path,
        conf=0.25
    )

    if not results:

        return {
            "error": "No prediction generated"
        }

    result = results[0]
    annotated = result.plot()
    _,buffer = cv2.imencode(".jpg", annotated)
    annotated_image = base64.b64encode(buffer).decode("utf-8")  


    names = model.names

    masked = 0
    unmasked = 0
    incorrect = 0

    if result.boxes is not None:

        for box in result.boxes:

            cls = int(box.cls[0])

            label = names[cls]

            if label == "with_mask":
                masked += 1

            elif label == "without_mask":
                unmasked += 1

            else:
                incorrect += 1

    total = (
        masked +
        unmasked +
        incorrect
    )

    compliance = (
        (masked / total) * 100
        if total > 0
        else 0
    )
    from utils.logger import save_detection_log

    save_detection_log(
        masked,
        unmasked,
        incorrect,
        round(compliance, 2)
    )

    return {
        "total_faces": total,
        "masked": masked,
        "unmasked": unmasked,
        "incorrect": incorrect,
        "compliance": round(compliance, 2),
        "annotated_image": annotated_image
    }
   

from pathlib import Path
import os


from utils.logger import save_detection_log
from pathlib import Path
import os

def predict_video(video_path):

    results = model.predict(
        source=video_path,
        save=True,
        conf=0.25
    )

    masked = 0
    unmasked = 0
    incorrect = 0

    names = model.names

    for result in results:

        if result.boxes is not None:

            for box in result.boxes:

                cls = int(box.cls[0])
                label = names[cls]

                if label == "with_mask":
                    masked += 1

                elif label == "without_mask":
                    unmasked += 1

                else:
                    incorrect += 1

    total = masked + unmasked + incorrect

    compliance = (
        (masked / total) * 100
        if total > 0 else 0
    )

    # Save analytics record
    save_detection_log(
        masked=masked,
        unmasked=unmasked,
        incorrect=incorrect,
        compliance=round(compliance, 2)
    )

    detect_dir = Path("runs/detect")

    latest_run = max(
        detect_dir.glob("predict*"),
        key=lambda x: x.stat().st_mtime
    )

    input_name = Path(video_path).stem

    mp4_candidate = latest_run / f"{input_name}.mp4"
    avi_candidate = latest_run / f"{input_name}.avi"

    selected_video = None

    if mp4_candidate.exists():
        selected_video = mp4_candidate

    elif avi_candidate.exists():
        selected_video = avi_candidate

    if selected_video is None:

        return {
            "status": "error",
            "message": "Output video not found"
        }

    return {
        "status": "success",
        "output_video": str(selected_video.resolve()),
        "masked": masked,
        "unmasked": unmasked,
        "incorrect": incorrect,
        "compliance": round(compliance, 2)
    }
import tempfile
import cv2
import base64


async def predict_frame(file):

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    contents = await file.read()

    temp.write(contents)

    temp.close()

    results = model.predict(
        source=temp.name,
        conf=0.25
    )

    result = results[0]

    annotated = result.plot()

    _, buffer = cv2.imencode(
        ".jpg",
        annotated
    )

    encoded = base64.b64encode(
        buffer
    ).decode()

    return {
        "annotated_image": encoded
    }