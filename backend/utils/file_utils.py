import os
import uuid

UPLOAD_DIRECTORY = "uploads"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

async def save_uploaded_file(file):
    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid.uuid4()}{extension}"
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    content = await file.read()
    print("Content Length:", len(content))
    with open(file_path, "wb") as f:
        f.write(content)
    return file_path