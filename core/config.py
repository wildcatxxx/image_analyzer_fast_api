import os

API_KEY = os.getenv("API_KEY", "my-secret-key")
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
UPLOAD_DIR = "storage/images"
ALLOWED_TYPES = {"image/jpeg", "image/png"}


SECRET_KEY = "super-secret-jwt-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
