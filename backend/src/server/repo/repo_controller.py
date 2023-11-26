from fastapi import APIRouter, Depends, File, Form, UploadFile

from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session

from server.authentication.auth_utils import get_current_user
from server.user import user_schema
from server.database.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

class Repo(BaseModel):
    owner_id: int
    repo_owner: str
    repo_name: str
    issues: bool
    pull_requests: bool
    requirements: bool


# Get a public repository owner/name from the user
# Should all users be able to see all repositories? No
# Are we going to create a new database for each new repo request? Yes
# So each database will belong to a user and represent a repository. 
# That means there can be multiple databases for a single repository, with exactly the same data. Makes sense if users will do changes

@router.post("/repos")
async def create_repo(
    repo_owner: Annotated[str, Form()],
    repo_name: Annotated[str, Form()],
    requirements_file: Annotated[bytes, File()],
    user: user_schema.User = Depends(get_current_user),
    database: Session = Depends(get_db),
):
    """ 
        Create a new database for given repository for given user. 
        Populate it with the SDAs(issue-pr for now) from the repository.
        Populate it with the requirements from given requirements file.
    """
    # neo4j.create_db(user.id, repo_owner, repo_name)
    # populate_db_SDA(user.id, repo_owner, repo_name)
    # populate_db_requirements(user.id, repo_owner, repo_name, requirements_file)
    return {"message": "Repo created successfully"}