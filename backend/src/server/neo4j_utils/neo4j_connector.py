""" Neo4j connector class. """
from neo4j import GraphDatabase
from server.config import Config


# Create database function
#       You are not allowed to create multiple databases in community edition
#       Opt1: Create a new docker for each user, and load new database data whenever user requests??
#       Opt2: Create a new docker for each repository
#       Opt3: Use another graph database that allows multiple databases in community edition
# --> Opt3 used with neo4j+dozerdb plugin
# Create artifacts function, from json data (populate db with SDAs). DONE
class Neo4jConnector:
    """Neo4j connector class."""

    # Having single neo4j connection might be worse, must test!!!
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = object.__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

        self.driver = GraphDatabase.driver(
            f"bolt://{Config().neo4j_host}:7687",
            auth=(Config().neo4j_username, Config().neo4j_password),
        )

    def close(self):
        """Close neo4j connection."""
        self.driver.close()

    @staticmethod
    def tx(tx, query, params):
        """Transaction function for neo4j queries."""
        try:
            if params is not None:
                result = tx.run(query, params)
            else:
                result = tx.run(query)
            record = result.data()
            return record
        except Exception as e:
            raise e

    def execute_query(self, query, database, params=None):
        """Execute neo4j query."""
        try:
            with self.driver.session(database=database) as session:
                result = session.execute_write(self.tx, query, params)
                return result
        except Exception as e:
            # print(query, params)
            raise e

    def get_node_labels(self, database):
        """Get all node labels."""
        query = """
            MATCH (n) RETURN distinct labels(n) as label
        """
        result = self.execute_query(query, database)
        node_labels = [label["label"][0] for label in result]
        return node_labels

    def get_database_names(self):
        """Get all database names."""
        query = "SHOW DATABASES YIELD name"
        database_names = self.execute_query(query, "system")
        database_names = [name["name"] for name in database_names]
        return database_names

    def check_database_exists(self, database_name):
        """Check if database exists."""
        query = "SHOW DATABASES YIELD name"
        database_names = self.execute_query(query, "system")
        print(database_names)
        for name in database_names:
            if name["name"] == database_name:
                print(f"Database {database_name} already exists.")
                return True
        print(f"Database {database_name} does not exist.")
        return False

    def create_database(self, database_name):
        """Create a new database."""
        query = (
            f"""
            CREATE DATABASE {database_name}
        """
        ).format(database_name=database_name)
        self.execute_query(query, "system")

    def create_issue_from_json(self, json_file, database):
        """Create issue nodes from given json file."""
        query = (
            f"""
            CALL apoc.load.json('{json_file}') YIELD value as v 
            UNWIND v.issues AS properties
            CREATE (n:Issue)
            SET n = properties
            RETURN n
        """
        ).format(json_file=json_file)
        self.execute_query(query, database)

    def create_artifact_nodes(self, artifacts, label, database):
        """Create artifact nodes from given data."""
        query = (
            f"""
            UNWIND $artifacts AS properties
            create (n: {label} )
            SET n = properties
            RETURN n
        """
        ).format(label=label)
        params = {"artifacts": artifacts}
        self.execute_query(query, database, params)

    def get_artifact_nodes(self, label, database):
        """Get artifact nodes from given label."""
        query = (
            f"""
            MATCH (n:{label})
            RETURN n
        """
        ).format(label=label)
        result = self.execute_query(query, database)
        return result

    def get_artifact_nodes_from_label(self, label, database):
        """Get artifact nodes from given label."""
        query = (
            f"""
            MATCH (n:{label})
            RETURN n.number as number, n.text as text
        """
        ).format(label=label)
        result = self.execute_query(query, database)
        return result

    def get_artifact_nodes_filtered(self, filter_text, database):
        """Get artifact nodes from given label."""
        query = (
            f"""
            MATCH (n)
            where (n:Issue or n:PullRequest) and n.text contains '{filter_text}'
            RETURN n.number as number, n.text as text
        """
        ).format(filter_text=filter_text)
        result = self.execute_query(query, database)
        return result

    def link_commits_prs(self, database):
        """Link commits and pull requests."""
        query = """
            MATCH (n:Commit), (p:PullRequest)
            where n.associatedPullRequests = p.number
            create (p)-[t:relatedCommit]->(n)
            RETURN * 
        """
        self.execute_query(query, database)

    def create_indexes(self, label, field, database):
        """Create indexes for given label and field."""
        index_name = f"{label}_{field}"
        field = f"n.{field}"
        query = (
            f"""
            CREATE INDEX {index_name} IF NOT EXISTS FOR (n:{label}) ON ({field})
        """
        ).format(index_name=index_name, label=label, field=field)
        params = {"label": label, "field": field}
        self.execute_query(query, database, params)

    def clear_database(self, database):
        """Delete all data from database."""
        query = """
            MATCH (n)
            detach delete n
        """
        self.execute_query(query, database)

    def clear_trace_links(self, database):
        """Delete all trace links from database."""
        query = """
            MATCH ()-[n:tracesTo]->()
            delete n
        """
        self.execute_query(query, database)

    def filter_artifacts(self, date, database):
        """Delete all artifacts created before given date."""
        query_issue = (
            f"""
            Match(n:Issue) 
            where date(n.createdAt) <= date("{date}")
            delete n
        """
        ).format(date=date)
        query_pr = (
            f"""
            Match(n:PullRequest) 
            where date(n.createdAt) <= date("{date}")
            delete n
        """
        ).format(date=date)
        query_commit = (
            f"""
            Match(n:Commit) 
            where date(n.createdAt) <= date("{date}")
            delete n
        """
        ).format(date=date)
        self.execute_query(query_issue, database)
        self.execute_query(query_pr, database)
        self.execute_query(query_commit, database)

    def create_trace_links(self, source_artifact, target_artifact, traces, database):
        """Create traces between artifacts."""
        print(traces)
        query = (
            f"""
            UNWIND $traces AS trace
            MATCH (r:{source_artifact})
            WHERE r.number = trace[0]
            WITH r, trace[1] as target, trace[2] as weight
            MATCH (i:{target_artifact})
            WHERE i.number = target
            MERGE (i)<-[t:tracesTo]-(r)
            SET t.weight = weight
            RETURN *
        """
        ).format(source_artifact=source_artifact, target_artifact=target_artifact)

        params = {"traces": traces}
        self.execute_query(query, database, params)

    def get_num_of_trace_links(self, database):
        """Get all trace links."""
        query = """
            MATCH ()-[n:tracesTo]->()
            RETURN count(n) as num_of_trace_links
        """
        result = self.execute_query(query, database)
        return result[0].get("num_of_trace_links")

    def get_num_of_artifacts(self, label, database):
        """Get all artifacts."""
        query = (
            f"""
            MATCH (n:{label})
            RETURN count(n) as num_of_artifacts
        """
        ).format(label=label)
        result = self.execute_query(query, database)
        return result[0].get("num_of_artifacts")

    def get_issue_issuepr_natural_links(self, database):
        """Get natural trace links between issues and issues/prs."""
        query = """
            MATCH (n:Issue)
            RETURN n.number as source, n.related_prs+n.trackedIssues as targets
        """
        result = self.execute_query(query, database)
        return result

    def get_artifact_nodes_containing_req_number(self, database):
        """Get all artifact nodes containing requirement numbers."""
        query = """
            match (r:Requirement)
            where size(r.number) > 1
            with r
            match (n)
            where (n:Issue or n:PullRequest) and n.text contains r.number
            return r.number as soruce, n.number as target, n.text as target_text
        """
        result = self.execute_query(query, database)
        return result

    # def create_trace_links(self, traces, label, database):
    #     """ Create traces between artifacts."""
    #     query = (f'''
    #         UNWIND $traces AS trace
    #         MATCH (r:Requirement)
    #         WHERE r.number = trace[0]
    #         WITH r, trace[1] as trace_list
    #         unwind trace_list AS art_key_pair
    #         MATCH (i:{label})
    #         WHERE i.number = art_key_pair[0]
    #         CREATE (i)<-[t:tracesTo]-(r)
    #         SET t.weight = art_key_pair[1][0]
    #         SET t.keywords = art_key_pair[1][1]
    #         RETURN *
    #     ''').format(label=label)

    #     params = {'traces': traces}
    #     self.execute_query(query, database, params)
