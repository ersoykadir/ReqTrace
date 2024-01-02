""" Repo controller"""
from pydantic import BaseModel
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from server.config import Config
from server.user import user_schema
from server.artifacts import artifacts
from server.authentication.auth_utils import get_current_user
from server.trace import tracer_llm, tracer_tfidf, tracer_word_embeddings, tracer

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

# TODO1: Check if user is authorized to access the repo at each endpoint!!!


class RepoBase(BaseModel):
    """Repo model."""

    repo_owner: str
    repo_name: str


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
    repo: RepoBase,
    user: user_schema.User = Depends(get_current_user),
):  # database: Session = Depends(get_db),
    """
    Create a new database for given repository for given user.
    Populate it with the SDAs(issue-pr for now) from the repository.
    Populate it with the requirements from given requirements file.
    """
    # Check if repo exists
    if not artifacts.check_repo_exists(repo.repo_owner, repo.repo_name):
        raise HTTPException(status_code=404, detail="Github Repo doesn't exist!")
    database_name = f"{repo.repo_owner}.{repo.repo_name}.id{user.id}"
    if Neo4jConnector().check_database_exists(database_name):
        raise HTTPException(status_code=400, detail="Repo already exists!")
    Neo4jConnector().create_database(database_name)
    return {"message": "Repo created successfully"}


@router.get("/")
async def get_repos(
    user: user_schema.User = Depends(get_current_user),
):  # database: Session = Depends(get_db),
    """
    Get all repositories of given user.
    """
    database_names = Neo4jConnector().get_database_names()
    repo_names = []
    for name in database_names:
        if f"id{user.id}" in name:
            repo_names.append(name)
    print(repo_names)
    return {"repos": repo_names}


@router.get("/{repo_id}/artifacts")
async def get_artifact_types(
    repo_id: str,
    user: user_schema.User = Depends(get_current_user),
):  # database: Session = Depends(get_db),
    """
    Get all artifact types of given repository for given user.
    """
    if not Neo4jConnector().check_database_exists(repo_id):
        return {"message": "Repo does not exist"}
    if f"id{user.id}" not in repo_id:
        return {"message": "You are not authorized to access this repo"}
    node_labels = Neo4jConnector().get_node_labels(repo_id)
    return {"artifact_types": node_labels}


@router.get("/traceMethods")
async def get_trace_methods():
    """
    Get all trace methods for given repository for given user.
    """
    return {"trace_methods": Config().available_search_methods}


@router.post("/{repo_id}/populate")
def populate_repo(
    repo_id: str,
    requirements_file: UploadFile,
    user: user_schema.User = Depends(get_current_user),
):  # database: Session = Depends(get_db),
    """
    Populate the database with the SDAs(issue-pr for now) from the repository.
    Beware that this will clear the database first!
    """
    print(repo_id)
    repo_owner, repo_name = repo_id.split(".")[0:2]
    repo_creation_date = artifacts.get_repo_created_at(repo_owner, repo_name)
    # database_name = f"{repo_owner}.{repo_name}.id{user.id}"
    if not Neo4jConnector().check_database_exists(repo_id):
        return {"message": "Repo does not exist"}
    if f"id{user.id}" not in repo_id:
        return {"message": "You are not authorized to access this repo"}

    # Clear the database
    Neo4jConnector().clear_database(repo_id)

    issues = artifacts.get_all_pages("issues", repo_owner, repo_name)
    pull_requests = artifacts.get_all_pages("pullRequests", repo_owner, repo_name)
    populate_db_issues(issues, repo_creation_date, repo_id)
    populate_db_prs(pull_requests, repo_creation_date, repo_id)

    requirements = artifacts.get_requirements(requirements_file.file)
    populate_db_requirements(requirements, repo_id)

    # Create natural trace links
    _tracer = tracer.Tracer()
    natural_trace_links = _tracer.find_natural_links(repo_id)

    for link_source, trace_links in natural_trace_links.items():
        Neo4jConnector().create_trace_links_v2(
            link_source,
            trace_links,
            repo_id,
        )
    return {"message": "Database populated successfully, natural trace links created."}


class TraceLink(BaseModel):
    """Trace link between two artifacts of given types."""

    source_artifact_type: str
    target_artifact_type: str
    trace_method: str
    threshold: float


class TraceLinkDelete(BaseModel):
    """Trace link between two artifacts of given types."""

    source_artifact_type: str
    target_artifact_type: str


tracers = {
    "tfidf": tracer_tfidf.TFIDF(),
    "word_embeddings": tracer_word_embeddings.WordEmbeddings(),
    "llm": tracer_llm.LLM(),
}


# TODO1: Should we reset/delete the trace links before creating new ones?
# Build trace links
# Expect user to give (source artifact, target artifact) and trace method
@router.post("/{repo_id}/trace")
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

    node_labels = Neo4jConnector().get_node_labels(repo_id)
    # If one of the source or target artifact types does not exist in the database, return error
    if trace_link.source_artifact_type not in node_labels:
        return {
            "message": f"Source artifact type does not exist, available types: {node_labels}"
        }
    if trace_link.target_artifact_type not in node_labels:
        return {
            "message": f"Target artifact type does not exist, available types: {node_labels}"
        }
    if trace_link.source_artifact_type == trace_link.target_artifact_type:
        # This is not implemented yet, we will decide what to do here later
        return {"message": "Source and target artifact types are the same"}
    # If trace method is not available, return error, inform about available trace methods
    if trace_link.trace_method not in Config().available_search_methods:
        methods = Config().available_search_methods
        return {
            "message": f"Trace method is not available, available methods: {methods}"
        }

    # Get all source artifacts of given type from the database
    source_artifacts = Neo4jConnector().get_artifact_nodes_from_label(
        trace_link.source_artifact_type, repo_id
    )
    # Get all target artifacts of given type from the database
    target_artifacts = Neo4jConnector().get_artifact_nodes_from_label(
        trace_link.target_artifact_type, repo_id
    )

    # For each source artifact, find the related target artifacts and create trace links
    # Create tracer object with given trace method
    # Call trace method with source and target artifacts
    # Trace method will return trace links
    _tracer = tracers[trace_link.trace_method]
    trace_links = _tracer.find_links(
        source_artifacts, target_artifacts, trace_link.threshold
    )

    Neo4jConnector().create_trace_links(
        trace_link.source_artifact_type,
        trace_link.target_artifact_type,
        trace_links,
        repo_id,
    )
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
    return {"message": "Trace links created", "num_of_links": len(trace_links)}


@router.delete("/{repo_id}/trace")
async def delete_all_trace_links(
    repo_id: str,
):
    """Delete all trace links"""
    Neo4jConnector().delete_all_trace_links(repo_id)
    return {"message": "Trace links deleted"}


@router.delete("/{repo_id}/trace")
async def delete_trace_links(
    repo_id: str,
    trace_link: TraceLinkDelete,
):
    """Delete trace links between given artifact types"""
    Neo4jConnector().delete_trace_links(
        trace_link.source_artifact_type, trace_link.target_artifact_type, repo_id
    )
    return {"message": "Trace links between given artifact types deleted"}


@router.get("/{repo_id}")
async def get_repo_details(repo_id: str):
    """Get repo details"""
    if not Neo4jConnector().check_database_exists(repo_id):
        return {"message": "Repo does not exist"}
    details = {}
    # Get repo name and owner
    # Get number of artifacts for each type
    artifact_types = Neo4jConnector().get_node_labels(repo_id)
    for artifact_type in artifact_types:
        details[artifact_type] = Neo4jConnector().get_num_of_artifacts(
            artifact_type, repo_id
        )
    # Get number of trace links
    details["trace_links"] = Neo4jConnector().get_num_of_trace_links(repo_id)
    return details
