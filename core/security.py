import bcrypt
from fastapi import Security, HTTPException, status
from core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from core.logging import logger
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status


# User
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
encode_utf = "utf-8"
MAX_BCRYPT_BYTES = 72  # bcrypt limit


def truncate_password(password: str) -> str:
    """
    Truncate password to 72 bytes for bcrypt.
    Handles multi-byte characters safely.
    """
    truncated = password.encode(encode_utf)[:MAX_BCRYPT_BYTES]
    return truncated


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(truncate_password(password), salt)
    # pwd_context.hash()
    return hashed_password.decode(encode_utf)


def verify_password(plain, hashed):
    return bcrypt.checkpw(truncate_password(plain), hashed.encode(encode_utf))


# JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
