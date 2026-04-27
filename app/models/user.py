from sqlalchemy import Column, Integer, String
from app.database import Base
from app.models.mixins import TimestampMixin
import uuid
from sqlalchemy.orm import relationship

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(
    String,
    primary_key=True,
    index=True,
    default=lambda: str(uuid.uuid4())
    )
    
    email = Column(String, unique=True, index=True)
    password = Column(String)

    activities = relationship("Activity", back_populates="user")