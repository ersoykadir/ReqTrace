"""create repos table

Revision ID: 0d0757ec0e38
Revises: 076eb708e60b
Create Date: 2023-11-26 03:18:15.158488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d0757ec0e38'
down_revision: Union[str, None] = '076eb708e60b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "repos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("repo_owner", sa.String(64), nullable=False),
        sa.Column("repo_name", sa.String(64), nullable=False),
        sa.Column("issues", sa.Boolean(), nullable=False),
        sa.Column("pull_requests", sa.Boolean(), nullable=False),
        sa.Column("requirements", sa.Boolean(), nullable=False),
    )
    op.create_index(op.f("ix_repos_id"), "repos", ["id"])
    op.add_column("repos", sa.Column("owner_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "repos_owner_fk",
        "repos",
        "users",
        ["owner_id"],
        ["id"],
        ondelete="CASCADE"
    )
    op.create_unique_constraint(
        "unique_repo",
        "repos",
        ["repo_owner", "repo_name", "owner_id"]
    )


def downgrade() -> None:
    op.drop_constraint("repos_owner_fk", "repos", type_="foreignkey")
    op.drop_column("repos", "owner_id")
    op.drop_constraint("unique_repo", "repos", type_="unique")
    op.drop_index(op.f("ix_repos_id"), table_name="repos")
    op.drop_table("repos")