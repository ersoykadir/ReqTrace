"""
Kadir Ersoy
Internship Project
User Model
"""
from sqlalchemy import Column, Integer, String, UniqueConstraint, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from server.database.database import Base


class Repo(Base):
    """Repo Model"""

    __tablename__ = "repos"
    # __table_args__ = (UniqueConstraint("repo_owner","repo_name","owner_id", name="unique_repo"),)

    id = Column(Integer, primary_key=True, index=True)
    repo_owner = Column(String(64))
    repo_name = Column(String(64))
    issues = Column(Boolean)
    pull_requests = Column(Boolean)
    requirements = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="repos")
