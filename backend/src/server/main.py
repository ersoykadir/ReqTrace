"""Main module for the backend server."""
import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from server.authentication import auth_controller
from server.repo import repo_controller


HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

if HOST is None or PORT is None:
    raise ValueError("HOST and PORT environment variables must be set.")

app = FastAPI()

app.include_router(auth_controller.router)
app.include_router(repo_controller.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=int(PORT),
        reload=True,
    )

# NEXT TIME

# Question: How will users reach dashboards for their repositories?
# Do we create databases for each repository? Yes
# Do we create a new neo4j docker for each user?
# If no, does dashboard allow multiple users to connect to a single neo4j docker?
# If yes, how will neo4j connection from backend handled?
# Be careful to connect to the user's neo4j docker. Be careful to redirect user to its own dashboard


@app.get("/")
async def healthcheck():
    """Health check endpoint."""
    return {"message": "App is running"}




class TraceLink(BaseModel):
    """Trace link between two artifacts of given types."""
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
        Create trace links btw given source and target artifacts for given repo for given user.
        Trace method is given by the user.
    """
    print(repo_id, trace_link)
    # If repo does not exist, return error
    # If one of the source or target artifact types does not exist in the database, return error
    # If trace method is not available, return error, inform about available trace methods
    # Get all source artifacts of given type from the database
    # Get all target artifacts of given type from the database
    # For each source artifact, find the related target artifacts and create trace links
    # Save trace links to the database
        # Apart from trace_method, there are natural trace links.
        # for issue-pr, there is a natural trace link between issue and pr(linked prs for issue)
        # for req-issue/pr, there is a natural link btw req-issue/pr(req number in issue/pr body)
        # for issue-issue, there is a natural trace link between issues(traces issues for issue)
    # TODO1: How will we handle the case where
    #       there are multiple target artifacts for a single source artifact?
    # TODO2: Are we going to allow a list of source or target artifact types? Lets not mix them,
    #       if user wants such thing, let them make multiple requests
    # TODO3: trace methods -> tfidf, word_embeddings(from bert or LLM), direct llm training
    return {"message": "Trace links created"}

# Let user select one of the created repos
# Redirect user to the neo4j dashboard or browser with the selected repo
# How will neo4j dashboard display the data from the selected repo?
# I remember neo4j dashboard config had something to solve this

# We try to publish neo4j dashboards for each user,
# how will this work if there is a single neo4j docker
# Can we get multiple neo4j dashboards from a single neo4j docker?
# If not, we can create a new neo4j docker for each user.
# This is not too bad,since we will have a neo4j docker for each user and db for each of their repo.

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
