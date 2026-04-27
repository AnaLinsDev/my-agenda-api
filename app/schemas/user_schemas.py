from pydantic import BaseModel, EmailStr, StringConstraints, Field
from typing import Optional, Annotated


class UpdateUserRequest(BaseModel):
    id: int
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=6, max_length=128)
    current_password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr