""" This file contains the functions that interact with the neo4j database. """
from neo4j.time import Date
from server.artifacts import artifacts
from server.neo4j_utils.neo4j_connector import neo4jConnector

# def populate_db_SDA(user_id, repo_owner, repo_name):
#     """ Populate the database with SDAs(issue-pr for now) from the repository. """
#     # Acquire repo data from github
#     issues = artifacts.get_all_pages('issues', repo_owner, repo_name)
#     prs = artifacts.get_all_pages('pullRequests', repo_owner, repo_name)

#     # Fetch requirements from given requirements file
#     # populate_db
#     return {"message": "Repo created successfully"}


def populate_db_requirements(repo_owner, repo_name, database_name, requirements_file):
    """ Populate the database with requirements from given requirements file. """
    # Acquire repo data from github
    # Fetch requirements from given requirements file
    data = artifacts.get_requirements(requirements_file)
    for requirement in data['requirements']:
        requirement['text'] = requirement['description']
    # Create neo4j nodes
    # neo4jConnector().create_artifact_nodes(data['data'], 'Requirement')
    neo4jConnector().create_artifact_nodes(data['requirements'], 'Requirement', database_name)
    neo4jConnector().create_indexes('Requirement', 'number', database_name)

def comment_parser(comments):
    """ Parses the comments of an issue or pull request. """
    comment_list = []
    comments = comments['nodes']
    for comment in comments:
        comment_list.append(comment['body'])
    return comment_list


def populate_db_issues(repo_owner, repo_name, database_name):
    """ Populate the database with issues from given repository."""
    data = artifacts.get_all_pages('issues', repo_owner, repo_name)
    # data = json.loads(data)
    for issue in data['data']:
        # Since neo4j does not support dictionaries as properties,
        # we need to convert the dictionaries to lists or strings.
        issue['commentCount'] = issue['comments']['totalCount']
        issue['comment_list'] = comment_parser(issue['comments'])
        del issue['comments']

        if issue['milestone'] is not None:
            issue['milestone'] = issue['milestone']['description']

        # Concatenate the title, body and comments to create a single text property.
        issue['text'] = issue['title'] + '\n' + issue['body']
        for comment in issue['comment_list']:
            issue['text'] += '\n' + comment

        issue['labels'] = [label['name'] for label in issue['labels']['nodes']]
        issue['trackedIssues'] = [
            tracked_issue['number'] for tracked_issue in issue['trackedIssues']['nodes']
        ]
        related_prs = []
        for item in issue['timelineItems']['nodes']:
            if 'CrossReferencedEvent' in item and item['CrossReferencedEvent'] is not None:
                related_prs.append(item['CrossReferencedEvent']['number'])
            elif 'ConnectedEvent' in item and item['ConnectedEvent'] is not None:
                related_prs.append(item['ConnectedEvent']['number'])
        issue['related_prs'] = related_prs
        del issue['timelineItems']

        # Convert the dates to neo4j compatible format
        issue['createdAt'] = Date.from_iso_format(issue['createdAt'][:10])
        if issue['closedAt'] is not None:
            issue['closedAt'] = Date.from_iso_format(issue['closedAt'][:10])
        repo_creation_date = Date.from_iso_format(data['createdAt'][:10])

        # Calculate the weeks passed since the repo was created (Date.from_iso_format(date[:10]))
        issue['created_week'] = (issue['createdAt'] - repo_creation_date).weeks
        issue['closed_week'] = None
        if issue['closedAt'] is not None:
            issue['closed_week'] = (issue['closedAt'] - repo_creation_date).weeks

    # Create neo4j nodes
    # TODO: There must be a way to switch between databases.
    # If different dockers are used, then neo4jConnector must be initialized with the docker port
    # (a mapping between user.id and docker port needed). (Singleton will not work)
    # Or just clear the database and populate it with new data. each time. (docker for each user)
    # If same docker is used, then neo4j config must be changed to use different databases.
    # neo4jConnector().create_artifact_nodes(data['data'], 'Issue')
    neo4jConnector().create_artifact_nodes(data['data'], 'Issue', database_name)
    neo4jConnector().create_indexes('Issue', 'number', database_name)


# TODO: Get commit data from pr['commits'] and create commit nodes.

def populate_db_prs(repo_owner, repo_name, database_name):
    """ Populate the database with pull requests from given repository."""
    data = artifacts.get_all_pages('pullRequests', repo_owner, repo_name)
    # data = json.loads(data)

    for pr in data['data']:
        # Since neo4j does not support dictionaries as properties,
        # we need to convert the dictionaries to lists or strings.
        pr['commentCount'] = pr['comments']['totalCount']
        pr['comment_list'] = comment_parser(pr['comments'])
        del pr['comments']

        if pr['milestone'] is not None:
            pr['milestone'] = pr['milestone']['description']

        # Parse the commits of the pull request.
        pr['commitCount'] = pr['commits']['totalCount']
        #pr['commit_list'] = commit_parser(pr['commits'])
        del pr['commits']

        # Concatenate the title, body and comments to create a single text property.
        pr['text'] = pr['title'] + ' ' + pr['body']
        for comment in pr['comment_list']:
            pr['text'] += ' ' + comment

        pr['labels'] = [label['name'] for label in pr['labels']['nodes']]

        # Convert the dates to neo4j compatible format
        pr['createdAt'] = Date.from_iso_format(pr['createdAt'][:10])
        if pr['closedAt'] is not None:
            pr['closedAt'] = Date.from_iso_format(pr['closedAt'][:10])
        repo_creation_date = Date.from_iso_format(data['createdAt'][:10])

        # Calculate the weeks passed since the repo was created
        pr['created_week'] = (pr['createdAt'] - repo_creation_date).weeks
        pr['closed_week'] = None
        if pr['closedAt'] is not None:
            pr['closed_week'] = (pr['closedAt'] - repo_creation_date).weeks

    # Create neo4j nodes
    # neo4jConnector().create_artifact_nodes(data['pullRequests'], 'PullRequest')
    neo4jConnector().create_artifact_nodes(data['data'], 'PullRequest', database_name)
    neo4jConnector().create_indexes('PullRequest', 'number', database_name)
