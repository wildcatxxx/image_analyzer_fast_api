from pydantic import BaseModel, EmailStr, field_validator

from core.security import MAX_BCRYPT_BYTES

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password_length(cls, v):
        if len(v.encode('utf-8')) > MAX_BCRYPT_BYTES:
            raise ValueError(f"Password too long, max {MAX_BCRYPT_BYTES} bytes allowed")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
