"""Tracer module."""
import re
from server.neo4j_utils.neo4j_connector import Neo4jConnector


class Tracer:
    """Tracer class."""

    def __init__(self):
        self.trace_method = None
        self.trace_links = []  # Not sure how to represent trace links yet!!!


    def find_links(self, source_artifacts, target_artifacts, threshold):
        """Find trace links from source artifacts to target artifacts."""
        # Add found trace links to self.trace_links, do not overwrite existing trace links
        print(
            f"Finding links from {source_artifacts} to {target_artifacts} w/ threshold {threshold}"
        )

    def find_natural_links(self, database):
        """Find natural trace links from source artifacts to target artifacts."""
        # Add found trace links to self.trace_links, do not overwrite existing trace links
        # Issue-Issue and Issue-PR links already exist in the database
        natural_links = {
            'Issue': [],
            'Requirement': [],
        }
        issue_to_targets = Neo4jConnector().get_issue_issuepr_natural_links(database)
        for link in issue_to_targets:
            for target in link["targets"]:
                natural_links["Issue"].append((link["source"], target, 1))

        # Req-Issue and Req-PR links can be found by searching for req number in issue/pr text
        req_to_artifacts = Neo4jConnector().get_artifact_nodes_containing_req_number(
            database
        )
        # Clean false positives
        for link in req_to_artifacts:
            if self.regex_check(link["source"], link["target_text"]):
                natural_links["Requirement"].append((link["source"], link["target"], 1))
        return natural_links

    def regex_check(self, req_number, text):
        """Check if the req number is in the text."""
        pattern = r"(?<![\.\d])" + re.escape(req_number)
        match = re.search(pattern, text)
        if match:
            return True
        return False

    def get_trace_links(self):
        """Return trace links."""
        raise NotImplementedError