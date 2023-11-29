"""TF-IDF tracer."""
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.spatial.distance import cosine
from server.trace.tracer import Tracer


class TFIDF(Tracer):
    """TF-IDF trace method."""

    def __init__(self):
        super().__init__()
        self.trace_method = "tfidf"
        self.model = None

    def create_model(self, source_artifacts, target_artifacts):
        """Create the vector model for the graph."""
        # Should we create model based on all artifacts or only given types?
        # For now I am only using given types
        # TODO1: Implement TF-IDF tracing
        source_vectors = {}
        target_vectors = {}
        data = source_artifacts + target_artifacts
        corpus = [node["text"] for node in data]
        tfidf_vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
        tfidf_matrix = tfidf_matrix.toarray()
        for i, node in enumerate(data):
            if i < len(source_artifacts):
                source_vectors[node["number"]] = tfidf_matrix[i]
            else:
                target_vectors[node["number"]] = tfidf_matrix[i]
        return source_vectors, target_vectors

    def find_links(self, source_artifacts, target_artifacts):
        # super().find_links(source_artifacts, target_artifacts)
        # TODO1: Implement TF-IDF tracing
        trace_links = []
        source_vectors, target_vectors = self.create_model(source_artifacts, target_artifacts)
        for source_number, source_vector in source_vectors.items():
            for target_number, target_vector in target_vectors.items():
                similarity = 1 - cosine(source_vector, target_vector)
                if similarity > 0.5:
                    trace_links.append((source_number, target_number, similarity))

        self.trace_links = trace_links
