"""Main module for the backend server."""
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.repo import repo_controller
from server.authentication import auth_controller


HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

if HOST is None or PORT is None:
    raise ValueError("HOST and PORT environment variables must be set.")

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router, prefix="/api", tags=["auth"])
app.include_router(repo_controller.router, prefix="/api", tags=["repo"])

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


@app.get("/api")
async def healthcheck():
    """Health check endpoint."""
    return {"message": "App is running"}


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
