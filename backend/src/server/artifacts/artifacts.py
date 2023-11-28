"""
Acquires software artifacts(issue, pr, commmit, requirement).
"""

import os
import requests
import io
import re
from bs4 import BeautifulSoup

from server.artifacts.graphql_templates import ISSUE_queryTemplate, PR_queryTemplate
from server.config import Config


def get_data_from_api(query):
    """ Acquires data from the github graphql api, given a graphql query."""
    url = 'https://api.github.com/graphql'
    r = requests.post(url = url,
                      json = {"query":query},
                      auth=(Config().github_username, Config().github_token),
                      timeout=10
    )
    data = r.json()
    if r.status_code != 200:
        r.raise_for_status()
    return data


def get_artifact_page(query, artifact_type):
    """ Gets a page of artifacts and returns them with the hasNextPage and endCursor values."""
    data = get_data_from_api(query)
    if Config().REPO_CREATED_AT is None:
        Config().REPO_CREATED_AT = data['data']['repository']['createdAt']
    artifact_data = data['data']['repository'][artifact_type]['nodes']
    has_next_page = data['data']['repository'][artifact_type]['pageInfo']['hasNextPage']
    end_cursor = data['data']['repository'][artifact_type]['pageInfo']['endCursor']
    return artifact_data, has_next_page, end_cursor


# Github GraphQL query templates for each artifact type
artifact_template = {
    'issues': ISSUE_queryTemplate,
    'pullRequests': PR_queryTemplate
}

def get_all_pages(artifact_type, repo_owner, repo_name):
    """ Gets all pages for an artifact type and returns them."""

    template = artifact_template[artifact_type]
    pages = []
    has_next_page, end_cursor = True, "null"

    # Traverse the pages
    while has_next_page:
        if end_cursor != "null":
            end_cursor = "\"" + end_cursor + "\""
        # Update the query with the new end_cursor
        query = template.substitute(
            owner=repo_owner,
            name=repo_name,
            cursor=end_cursor
        )
        # Get the next page of artifacts
        page_data, has_next_page, end_cursor = get_artifact_page(query, artifact_type)
        pages = pages + page_data

    pages = filter_before(pages, Config().filter_date)
    return {"data": pages}


def filter_before(pages, filter_date):
    """ Filters the artifacts before the given date."""
    filtered_pages = []
    for data in pages:
        if data['createdAt'] > filter_date:
            filtered_pages.append(data)
    return filtered_pages


def get_requirements(req_file_data):
    """
    Assumptions:    The requirements have the format <requirement_number> <requirement_description>
                    The parent of a requirement is the requirement with the same number,
                    but without the last number. (1.1 is the parent of 1.1.1)       
    """
    # if Config().parent_mode:
    #     requirements_file_name = f'data_{Config().repo_name}/requirements(req_tree).txt'
    # else:
    #     requirements_file_name = f'data_{Config().repo_name}/requirements.txt'

    # Parse the HTML content
    html_content = req_file_data.file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    # Get the text content without HTML tags
    clean_text = soup.get_text()
    # Define a regular expression pattern to extract requirement numbers and statements
    pattern = re.compile(r'(?!#*\s+)(\d+(\.\d+)*)(.{0,1})\s+(.+)')
    matches = pattern.findall(clean_text)
    requirements = []

    for match in matches:
        req_number = match[0]
        req_description = match[3]
        req_dict = {
            'number': req_number,
            'description': req_description
        }
            # 'parent': '.'.join(req_number.split('.')[:-1])
        requirements.append(req_dict)

    # async with req_file_data.file as f:
    #     async for line in f:
    #         req_number, req_description = req_parser(line)
    #         req_dict = {
    #             'number': req_number,
    #             'description': req_description,
    #             'parent': '.'.join(req_number.split('.')[:-1])
    #         }
    #         requirements.append(req_dict)

    return {"data": requirements}
