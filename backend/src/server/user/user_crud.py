"""User CRUD operations"""
from sqlalchemy.orm import Session

from server.user import user_model
from server.user import user_schema

# from . import context_instance


class User:
    """User CRUD"""

    def get_user(self, database: Session, user_id: int):
        """Get user by id"""
        return (
            database.query(user_model.User)
            .filter(user_model.User.id == user_id)
            .first()
        )

    def get_user_by_email(self, database: Session, email: str):
        """Get user by email"""
        return (
            database.query(user_model.User)
            .filter(user_model.User.email == email)
            .first()
        )

    def get_users(self, database: Session, skip: int = 0, limit: int = 100):
        """Get all users"""
        return database.query(user_model.User).offset(skip).limit(limit).all()

    def create_user(self, database: Session, user_data: user_schema.UserBase):
        """Create user"""
        db_user = user_model.User(email=user_data.email, name=user_data.name)
        database.add(db_user)
        database.commit()
        database.refresh(db_user)
        return db_user

user = User()
