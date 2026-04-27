from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)
    

class AuthResponse(BaseModel):
    id: UUID
    email: EmailStr
