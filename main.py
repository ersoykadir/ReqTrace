from fastapi import FastAPI, File, Form, UploadFile, Depends
from pydantic import BaseModel, 
from typing import Annotated


app = FastAPI()

# NEXT TIME
# TODO: Start with repo creation, implement db creation, populate db with SDAs and requirements


@app.get("/")
async def root():
    return {"message": "Hello World"}


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

@app.post("/repos")
async def create_repo(
    repo_owner: Annotated[str, Form()],
    repo_name: Annotated[str, Form()],
    requirements_file: Annotated[bytes, File()],
    user: schemas.user.User = Depends(get_current_user),
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

class TraceLink(BaseModel):
    source_artifact_type: str
    target_artifact_type: str
    trace_method: str

# Build trace links
# Expect user to give (source artifact, target artifact) and trace method
@app.post("/repos/{repo_id}/tracelinks")
async def create_trace_links(
    repo_id: int,
    trace_link: TraceLink,
):
    """ 
        Create trace links between given source and target artifacts for given repository for given user.
        Trace method is given by the user.
    """
    # If repo does not exist, return error
    # If one of the source or target artifact types does not exist in the database, return error
    # If trace method is not available, return error, inform about available trace methods
    # Get all source artifacts of given type from the database
    # Get all target artifacts of given type from the database
    # For each source artifact, find the related target artifacts and create trace links
    # Save trace links to the database
        # Apart from trace_method, there are natural trace links.
        # for issue-pr, there is a natural trace link between issue and pr(linked prs for issue)
        # for req-issue, req-pr, there is a natural trace link between req and issue/pr(req number in issue/pr body)
        # for issue-issue, there is a natural trace link between issues(traces issues for issue)
    # TODO: How will we handle the case where there are multiple target artifacts for a single source artifact?
    # TODO: Are we going to allow a list of source or target artifact types? Lets not mix them, 
    #       if user wants such thing, let them make multiple requests
    # TODO: trace methods -> tfidf, word_embeddings(from bert or LLM), direct llm training
    return {"message": "Trace links created"}

# Let user select one of the created repos
# Redirect user to the neo4j dashboard or browser with the selected repo
# How will neo4j dashboard display the data from the selected repo?
# I remember neo4j dashboard config had something to solve this

# We try to publish neo4j dashboards for each user, how will this work if there is a single neo4j docker
# Can we get multiple neo4j dashboards from a single neo4j docker?
# If not, we can create a new neo4j docker for each user. 
# This is not too bad, since we will have a neo4j docker for each user and db for each of their repo. 

# Not a bad idea to have a separate endpoints for updating requirements and SDAs
# !!! This might mean we need to reset the trace links
# @app.post("/repos/{repo_id}/requirements")
# async def update_requirements():
#     """ 
#         Create a new requirements file for given repository for given user. 
#         Populate it with the requirements from given requirements file. 
#         Delete old requirements file. Delete old requirements from database.
#     """
#     return {"message": "Requirements file updated"}

# @app.post("/repos/{repo_id}/issues")
# async def update_issues():
#     """ 
#         Delete old SDAs from database.
#         Populate it with the current SDAs(issue-pr for now) from the repository.
#     """
#     return {"message": "Issues updated"}