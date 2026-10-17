import os
from datetime import datetime

VIOLATION_LOG_DIRECTORY = "violation_logs"
os.makedirs(VIOLATION_LOG_DIRECTORY, exist_ok=True)

def log_violation(image_path, total_faces, unmasked):

   if unmasked > 0:
      name = datetime.now().strftime("%Y%m%d_%H%M%S")
      destination_path = os.path.join(VIOLATION_LOG_DIRECTORY, name)
      with open(image_path, "rb") as source_file:
         with open(destination_path, "wb") as dest_file:
            dest_file.write(source_file.read())