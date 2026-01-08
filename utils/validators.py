from fastapi import HTTPException, UploadFile
from core.config import MAX_FILE_SIZE, ALLOWED_TYPES

def validate_image(file: UploadFile, size: int):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only JPEG and PNG allowed.",
        )

    if size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File too large. Max size is 5MB.",
        )
