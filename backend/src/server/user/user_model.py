"""
Kadir Ersoy
Internship Project
User Model
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from server.database.database import Base


class User(Base):
    """User Model"""

    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("email", name="unique_user_email"),)

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True)
    name = Column(String(64))

    repos = relationship("Repo", back_populates="owner", cascade="all, delete")
