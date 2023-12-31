""" This file contains the functions that interact with the neo4j database. """
from neo4j.time import Date
from server.neo4j_utils.neo4j_connector import Neo4jConnector


def populate_db_requirements(data, database_name):
    """Populate the database with requirements from given requirements file."""
    for requirement in data["data"]:
        requirement["text"] = requirement["description"]
    # Create neo4j nodes
    Neo4jConnector().create_artifact_nodes(data["data"], "Requirement", database_name)
    Neo4jConnector().create_indexes("Requirement", "number", database_name)


def comment_parser(comments):
    """Parses the comments of an issue or pull request."""
    comment_list = []
    comments = comments["nodes"]
    for comment in comments:
        comment_list.append(comment["body"])
    return comment_list


def populate_db_issues(data, repo_creation_date, database_name):
    """Populate the database with issues from given repository."""
    for issue in data["data"]:
        # Since neo4j does not support dictionaries as properties,
        # we need to convert the dictionaries to lists or strings.
        issue["commentCount"] = issue["comments"]["totalCount"]
        issue["comment_list"] = comment_parser(issue["comments"])
        del issue["comments"]

        if issue["milestone"] is not None:
            issue["milestone"] = issue["milestone"]["description"]

        # Concatenate the title, body and comments to create a single text property.
        issue["text"] = issue["title"] + "\n" + issue["body"]
        for comment in issue["comment_list"]:
            issue["text"] += "\n" + comment

        issue["labels"] = [label["name"] for label in issue["labels"]["nodes"]]
        issue["trackedIssues"] = [
            tracked_issue["number"] for tracked_issue in issue["trackedIssues"]["nodes"]
        ]
        related_prs = []
        for item in issue["timelineItems"]["nodes"]:
            if "CrossReferencedEvent" in item and item["CrossReferencedEvent"]:
                related_prs.append(item["CrossReferencedEvent"]["number"])
            elif "ConnectedEvent" in item and item["ConnectedEvent"]:
                related_prs.append(item["ConnectedEvent"]["number"])
        issue["related_prs"] = related_prs
        del issue["timelineItems"]

        # Convert the dates to neo4j compatible format
        issue["createdAt"] = Date.from_iso_format(issue["createdAt"][:10])
        if issue["closedAt"] is not None:
            issue["closedAt"] = Date.from_iso_format(issue["closedAt"][:10])
        repo_created_at = Date.from_iso_format(repo_creation_date[:10])

        # Calculate the weeks passed since the repo was created (Date.from_iso_format(date[:10]))
        issue["created_week"] = (issue["createdAt"] - repo_created_at).days // 7
        issue["closed_week"] = None
        if issue["closedAt"] is not None:
            issue["closed_week"] = (issue["closedAt"] - repo_created_at).days // 7

    # Create neo4j nodes
    # There must be a way to switch between databases.
    #   -> With dozerdb plugin, we can create databases and switch between them.
    # TODO1: Still we need to find a way to set each user to access only their own database.
    Neo4jConnector().create_artifact_nodes(data["data"], "Issue", database_name)
    Neo4jConnector().create_indexes("Issue", "number", database_name)


# TODO2: Get commit data from pr['commits'] and create commit nodes.


def populate_db_prs(data, repo_creation_date, database_name):
    """Populate the database with pull requests from given repository."""
    for pr in data["data"]:
        # Since neo4j does not support dictionaries as properties,
        # we need to convert the dictionaries to lists or strings.
        pr["commentCount"] = pr["comments"]["totalCount"]
        pr["comment_list"] = comment_parser(pr["comments"])
        del pr["comments"]

        if pr["milestone"] is not None:
            pr["milestone"] = pr["milestone"]["description"]

        # Parse the commits of the pull request.
        pr["commitCount"] = pr["commits"]["totalCount"]
        # pr['commit_list'] = commit_parser(pr['commits'])
        del pr["commits"]

        # Concatenate the title, body and comments to create a single text property.
        pr["text"] = pr["title"] + " " + pr["body"]
        for comment in pr["comment_list"]:
            pr["text"] += " " + comment

        pr["labels"] = [label["name"] for label in pr["labels"]["nodes"]]

        # Convert the dates to neo4j compatible format
        pr["createdAt"] = Date.from_iso_format(pr["createdAt"][:10])
        if pr["closedAt"] is not None:
            pr["closedAt"] = Date.from_iso_format(pr["closedAt"][:10])
        repo_created_at = Date.from_iso_format(repo_creation_date[:10])

        # Calculate the weeks passed since the repo was created
        pr["created_week"] = (pr["createdAt"] - repo_created_at).days // 7
        pr["closed_week"] = None
        if pr["closedAt"] is not None:
            pr["closed_week"] = (pr["closedAt"] - repo_created_at).days // 7

    # Create neo4j nodes
    # neo4jConnector().create_artifact_nodes(data['pullRequests'], 'PullRequest')
    Neo4jConnector().create_artifact_nodes(data["data"], "PullRequest", database_name)
    Neo4jConnector().create_indexes("PullRequest", "number", database_name)
