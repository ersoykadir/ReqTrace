""" Repo controller"""
from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile
from pydantic import BaseModel
from server.authentication.auth_utils import get_current_user
from server.user import user_schema
# from server.database.database import get_db
from server.neo4j_utils.neo4j_connector import Neo4jConnector
from server.neo4j_utils.neo4j_funcs import (
    populate_db_issues,
    populate_db_prs,
    populate_db_requirements,
)

router = APIRouter(
    prefix="/repo",
    tags=["repo"],
    responses={404: {"description": "Not found"}},
)


class Repo(BaseModel):
    """Repo model."""
    owner_id: int
    repo_owner: str
    repo_name: str
    issues: bool
    pull_requests: bool
    requirements: bool


# TODO1: User privileges! How to allow only users who created the repo to access it?
# neo4j has a user and roles system but it is not available in community edition,
# also it is not very flexible!

# TODO2: Data persistence! compose file set volume for data persistence


# Get a public repository owner/name from the user
# Should all users be able to see all repositories? No
# Are we going to create a new database for each new repo request? Yes
# So each database will belong to a user and represent a repository.
# That means there can be multiple databases for a single repository, with exactly the same data.
# Makes sense if users will do changes


@router.post("/")
async def create_repo(
    repo_owner: Annotated[str, Form()],
    repo_name: Annotated[str, Form()],
    requirements_file: UploadFile,
    user: user_schema.User = Depends(get_current_user), # database: Session = Depends(get_db),
):
    """
    Create a new database for given repository for given user.
    Populate it with the SDAs(issue-pr for now) from the repository.
    Populate it with the requirements from given requirements file.
    """
    # neo4j.create_db(user.id, repo_owner, repo_name)
    database_name = f"{repo_owner}.{repo_name}.id{user.id}"
    if not Neo4jConnector().check_database_exists(database_name):
        Neo4jConnector().create_database(database_name)
    # Acquire repo data from github
    # populate_db_SDA(user.id, repo_owner, repo_name)
    populate_db_issues(repo_owner, repo_name, database_name)
    populate_db_prs(repo_owner, repo_name, database_name)
    # Fetch requirements from given requirements file
    # populate_db_requirements(user.id, repo_owner, repo_name, requirements_file)
    populate_db_requirements(database_name, requirements_file)
    return {"message": "Repo created successfully"}
