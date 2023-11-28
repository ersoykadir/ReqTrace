"""User schema"""
from typing import List
from pydantic import BaseModel
from server.repo.repo_schema import Repo


class UserBase(BaseModel):
    """User base schema"""

    email: str
    name: str


class User(UserBase):
    """User schema"""

    id: int
    repos: List[Repo] = []

    class Config:
        """Config"""

        from_attribute = True
