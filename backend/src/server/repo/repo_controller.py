""" Repo controller"""
from typing import Annotated
from fastapi import APIRouter, Depends, Form, UploadFile
from pydantic import BaseModel
from server.authentication.auth_utils import get_current_user
from server.user import user_schema
from server.artifacts import artifacts
from server.config import Config
from server.trace import tracer_llm, tracer_tfidf, tracer_word_embeddings
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
    database_name = f"{repo_owner}.{repo_name}.id{user.id}"
    repo_creation_date = artifacts.get_repo_created_at(repo_owner, repo_name)
    if not Neo4jConnector().check_database_exists(database_name):
        Neo4jConnector().create_database(database_name)

    issues = artifacts.get_all_pages('issues', repo_owner, repo_name)
    pull_requests = artifacts.get_all_pages('pullRequests', repo_owner, repo_name)
    populate_db_issues(issues, repo_creation_date, database_name)
    populate_db_prs(pull_requests, repo_creation_date, database_name)

    requirements = artifacts.get_requirements(requirements_file)
    populate_db_requirements(requirements, database_name)

    return {"message": "Repo created successfully"}



class TraceLink(BaseModel):
    """Trace link between two artifacts of given types."""
    source_artifact_type: str
    target_artifact_type: str
    trace_method: str

tracers = {
    "tfidf": tracer_tfidf.TFIDF(),
    "word_embeddings": tracer_word_embeddings.WordEmbeddings(),
    "llm": tracer_llm.LLM(),
}

# Build trace links
# Expect user to give (source artifact, target artifact) and trace method
@router.post("/repos/{repo_id}/tracelinks")
async def create_trace_links(
    repo_id: str,
    trace_link: TraceLink,
):
    """ 
        Create trace links btw given source and target artifacts for given repo for given user.
        Trace method is given by the user.
    """
    print(repo_id, trace_link)
    # repo_id = {repo_owner}.{repo_name}.id{user.id}
    # If repo does not exist, return error
    if not Neo4jConnector().check_database_exists(repo_id):
        return {"message": "Repo does not exist"}
    # If one of the source or target artifact types does not exist in the database, return error
    if trace_link.source_artifact_type not in ["issue", "pull_request", "requirement"]:
        return {"message": "Source artifact type does not exist"}
    if trace_link.target_artifact_type not in ["issue", "pull_request", "requirement"]:
        return {"message": "Target artifact type does not exist"}
    if trace_link.source_artifact_type == trace_link.target_artifact_type:
        # This is not implemented yet, we will decide what to do here later
        return {"message": "Source and target artifact types are the same"}
    # If trace method is not available, return error, inform about available trace methods
    if trace_link.trace_method not in Config().available_search_methods:
        return {"message": "Trace method is not available"}

    # Get all source artifacts of given type from the database
    source_artifacts = Neo4jConnector().get_artifact_nodes(trace_link.source_artifact_type, repo_id)
    # Get all target artifacts of given type from the database
    target_artifacts = Neo4jConnector().get_artifact_nodes(trace_link.target_artifact_type, repo_id)

    # For each source artifact, find the related target artifacts and create trace links
    # Create tracer object with given trace method
    # Call trace method with source and target artifacts
    # Trace method will return trace links
    tracer = tracers[trace_link.trace_method]
    tracer.find_natural_links(source_artifacts, target_artifacts)
    tracer.find_links(source_artifacts, target_artifacts)
    trace_links = tracer.get_trace_links()

    Neo4jConnector().create_trace_links(source_artifacts, target_artifacts, trace_links, repo_id)
    # Save trace links to the database
        # Apart from trace_method, there are natural trace links.
        # for issue-pr, there is a natural trace link between issue and pr(linked prs for issue)
        # for req-issue/pr, there is a natural link btw req-issue/pr(req number in issue/pr body)
        # for issue-issue, there is a natural trace link between issues(traces issues for issue)
    # TODO1: How will we handle the case where
    #       there are multiple target artifacts for a single source artifact?
    # TODO2: Are we going to allow a list of source or target artifact types? Lets not mix them,
    #       if user wants such thing, let them make multiple requests
    # TODO3: How will we handle the case where
    #       the source and target artifact types are the same?
    # TODO4: trace methods -> tfidf, word_embeddings(from bert or LLM), direct llm training
    return {"message": "Trace links created"}
