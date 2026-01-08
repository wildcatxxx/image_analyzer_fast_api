from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.security import decode_token

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

security = HTTPBearer()

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     payload = decode_token(token)
#     email = payload.get("sub")

#     if not email:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid token payload",
#         )
#     return email

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = decode_token(token)
    email = payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )
    return email

