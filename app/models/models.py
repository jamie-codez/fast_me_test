import uuid
from app.repository.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, default=False,server_default=text("false"))
    role = Column(String, default="user", server_default=text("'user'"))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=text("now()"))
    posts = relationship("Post", back_populates="owner")
