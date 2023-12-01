"""
Kadir Ersoy
Internship Project
User Schema
"""
from pydantic import BaseModel


class RepoBase(BaseModel):
    """User base schema"""

    repo_owner: str
    repo_name: str


class Repo(RepoBase):
    """User schema"""

    id: int
    issues: bool
    pull_requests: bool
    requirements: bool
    owner_id: int

    class Config:
        """Config"""

        from_attribute = True
