import os
import datetime
from neo4j import GraphDatabase

from server.config import Config

# TODO: Create database function
#       You are not allowed to create multiple databases in community edition
#       Opt1: Create a new docker for each user, and load new database data whenever user requests??
#       Opt2: Create a new docker for each repository
#       Opt3: Use another graph database that allows multiple databases in community edition
# TODO: Create issues function, from json data or
# TODO: Create artifacts function, from json data (populate db with SDAs)
# TODO: Create requirements function, from json data (populate db with requirements)

class neo4jConnector:
    # Having single neo4j connection might be worse, must test!!!
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = object.__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

        self.driver = GraphDatabase.driver(
            Config().neo4j_uri,
            auth=(Config().neo4j_username, Config().neo4j_password)
        )

    def close(self):
        self.driver.close()

    @staticmethod
    def tx(tx, query, params):
        """ Transaction function for neo4j queries."""
        try:
            if params is not None:
                result = tx.run(query, params)
            else:
                result = tx.run(query)
            record = result.data()
            return record
        except Exception as e:
            print(Config().neo4j_uri)
            raise e

    def execute_query(self, query, params=None):
        """ Execute neo4j query."""
        try:
            with self.driver.session() as session:
                result = session.execute_write(self.tx, query, params)
        except Exception as e:
            # print(query, params)
            raise e

    def create_issue_from_json(self, json_file):
        """ Create issue nodes from given json file."""
        query = (f'''
            CALL apoc.load.json('{json_file}') YIELD value as v 
            UNWIND v.issues AS properties
            CREATE (n:Issue)
            SET n = properties
            RETURN n
        ''').format(json_file=json_file)
        params = {'json_file': json_file}

        self.execute_query(query)

    def create_artifact_nodes(self, artifacts, label):
        """ Create artifact nodes from given json file."""
        query = (f'''
            UNWIND $artifacts AS properties
            create (n: {label} )
            SET n = properties
            RETURN n
        ''').format(label=label)
        params = {"artifacts": artifacts}
        self.execute_query(query,params)

    def link_commits_prs(self):
        query = '''
            MATCH (n:Commit), (p:PullRequest)
            where n.associatedPullRequests = p.number
            create (p)-[t:relatedCommit]->(n)
            RETURN * 
        '''
        self.execute_query(query)

    def create_indexes(self, label, field):
        index_name = f'{label}_{field}'
        field = f'n.{field}'
        query = (f'''
            CREATE INDEX {index_name} IF NOT EXISTS FOR (n:{label}) ON ({field})
        ''').format(index_name=index_name, label=label, field=field)
        params = { "label": label, "field": field }

        self.execute_query(query)

    def clean_all_data(self):
        query = '''
            MATCH (n)
            detach delete n
        '''

        self.execute_query(query)

    def filter_artifacts(self, date):
        query_issue = (f'''
            Match(n:Issue) 
            where date(n.createdAt) <= date("{date}")
            delete n
        ''').format(date=date)
        query_pr = (f'''
            Match(n:PullRequest) 
            where date(n.createdAt) <= date("{date}")
            delete n
        ''').format(date=date)
        query_commit = (f'''
            Match(n:Commit) 
            where date(n.createdAt) <= date("{date}")
            delete n
        ''').format(date=date)
        params = {'date': date}
        self.execute_query(query_issue)
        self.execute_query(query_pr)
        self.execute_query(query_commit)

    def create_traces_v3(self, traces, label):
        query = (f'''
            UNWIND $traces AS trace
            MATCH (r:Requirement)
            WHERE r.number = trace[0]
            WITH r, trace[1] as trace_list
            unwind trace_list AS art_key_pair
            MATCH (i:{label})
            WHERE i.number = art_key_pair[0]
            CREATE (i)<-[t:tracesTo]-(r)
            SET t.weight = art_key_pair[1][0]
            SET t.keywords = art_key_pair[1][1]
            RETURN *
        ''').format(label=label)

        params = {'traces': traces}
        self.execute_query(query, params)
