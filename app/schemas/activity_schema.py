from pydantic import BaseModel, Field
from typing import Literal
from uuid import UUID

CategoryType = Literal["personal", "work", "study", "health", "others"]

class ActivityBase(BaseModel):
    title: str = Field(min_length=6, max_length=128)

    date: str = Field(
        pattern=r"^\d{4}-\d{2}-\d{2}$",
        description="Format: YYYY-MM-DD"
    )

    time: str = Field(
        pattern=r"^\d{2}:\d{2}$",
        description="Format: HH:MM (24h)"
    )

    category: CategoryType
    completed: bool

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: UUID

    class Config:
        from_attributes = True
