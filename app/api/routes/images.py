from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.schemas.responses import ImageUploadResponse
from app.services.image_service import save_image, get_image_path
from app.services.analysis_service import analyze_image
from utils.validators import validate_image
from app.api.deps import get_current_user

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/upload", response_model=ImageUploadResponse)
async def upload_image(
    file: UploadFile = File(...),
    _: str = Depends(get_current_user),
):
    contents = await file.read()
    size = len(contents)
    file.file.seek(0)

    validate_image(file, size)

    image_id = save_image(file)

    return {
        "image_id": image_id,
        "message": "Image uploaded successfully",
    }


@router.post("/analyze/{image_id}")
def analyze_image_endpoint(image_id: str, user: str = Depends(get_current_user)):

    path = get_image_path(image_id)

    if not path:
        raise HTTPException(
            status_code=404,
            detail="Image not found for the given image_id",
        )

    analysis_result = analyze_image(image_id)

    return analysis_result
