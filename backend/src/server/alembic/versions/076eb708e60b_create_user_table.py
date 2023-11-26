"""create user table

Revision ID: 076eb708e60b
Revises: 
Create Date: 2023-11-26 03:12:04.950645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '076eb708e60b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(64), nullable=False),
        sa.Column("name", sa.String(64), nullable=False),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"])
    op.create_unique_constraint("unique_user_email", "users", ["email"])


def downgrade() -> None:
    op.drop_constraint("unique_user_email", "users", type_="unique")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
