"""Configuration class for the backend."""
import os


class Config:
    """
    Configuration class for the backend.
    Contains environment variables and tracing parameters.
    """

    # environment variables
    neo4j_username = os.environ.get("NEO4J_USERNAME")
    neo4j_password = os.environ.get("NEO4J_PASSWORD")
    neo4j_host = os.environ.get("NEO4J_HOST")
    github_username = os.environ.get("GITHUB_USERNAME")
    github_token = os.environ.get("GITHUB_TOKEN")

    # Tracing parameters
    available_search_methods = ["tfidf", "word_embeddings", "llm"]
    # search_method = 'keyword'
    # parent_mode = False
    # reset_graph = False
    # experiment_mode = False
    # model_setup = False
    # filter_threshold = 0.5
    # pretrained_model_path = os.environ.get('PRETRAINED_MODEL_PATH')

    filter_date = "2023-08-01"

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = object.__new__(cls)
            cls.instance.__initialized = False
        return cls.instance

    def __init__(self) -> None:
        if self.__initialized:
            return
        self.__initialized = True
