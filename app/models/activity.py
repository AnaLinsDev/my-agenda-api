from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Index
from app.database import Base
from app.models.mixins import TimestampMixin
import uuid
from sqlalchemy.orm import relationship

class Activity(Base, TimestampMixin):
    __tablename__ = "activities"

    id = Column(
    String,
    primary_key=True,
    index=True,
    default=lambda: str(uuid.uuid4())
    )

    title = Column(String, nullable=False)
    date = Column(String, nullable=False, index=True)
    time = Column(String, nullable=False)

    category = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    user_id = Column(String, ForeignKey("users.id"), index=True)

    user = relationship("User", back_populates="activities")

    __table_args__ = (
        Index("idx_date_time", "date", "time"),
    )