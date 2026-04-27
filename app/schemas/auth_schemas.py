from pydantic import BaseModel, EmailStr, StringConstraints, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)


class AuthResponse(BaseModel):
    id: int
    email: EmailStr
