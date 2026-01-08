import os
import uuid
from fastapi import UploadFile
from core.config import UPLOAD_DIR
from core.logging import logger

def save_image(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    image_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    filename = f"{image_id}{ext}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as f:
        f.write(file.file.read())

    logger.info(f"Image saved: {filename}")
    return image_id

def get_image_path(image_id: str):
    for file in os.listdir(UPLOAD_DIR):
        if file.startswith(image_id):
            return os.path.join(UPLOAD_DIR, file)
    return None
