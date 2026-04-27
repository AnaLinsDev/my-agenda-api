from pydantic import BaseModel, EmailStr, StringConstraints, Field
from typing import Optional, Annotated
from uuid import UUID


class UpdateUserRequest(BaseModel):
    id: UUID
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=6, max_length=128)
    current_password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr