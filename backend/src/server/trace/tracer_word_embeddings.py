"""Word embeddings tracer."""
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from server.trace.tracer import Tracer
from server.trace.utils.sent_tok import get_sentences


class WordEmbeddings(Tracer):
    """Word embeddings trace method."""

    def __init__(self):
        super().__init__()
        self.trace_method = "word_embeddings"
        self.model = None

    def create_model(self):
        """Create the vector model for the graph."""
        # model = SentenceTransformer("bert-base-nli-mean-tokens")
        model = SentenceTransformer("roberta-base-nli-mean-tokens")
        self.model = model

    def artifact_vector(self, artifact_text):
        """Create vector for given artifact text."""
        sentences = get_sentences(artifact_text)
        # Average the vectors of the sentences
        vector = self.model.encode(sentences)
        vector = vector.mean(axis=0)
        # Is this properly averaging? Is it okay to just average all sentences?
        return vector

    def find_links(self, source_artifacts, target_artifacts, threshold):
        """Find trace links between artifacts."""
        self.create_model()
        source_artifact_vectors = {}
        target_artifact_vectors = {}
        for source_artifact in source_artifacts:
            source_artifact_vectors[source_artifact["number"]] = self.artifact_vector(
                source_artifact["text"]
            )
        for target_artifact in target_artifacts:
            target_artifact_vectors[target_artifact["number"]] = self.artifact_vector(
                target_artifact["text"]
            )
        trace_links = []
        for source_number, source_vector in source_artifact_vectors.items():
            for target_number, target_vector in target_artifact_vectors.items():
                similarity = 1 - cosine(source_vector, target_vector)
                if similarity > threshold:  # Maybe
                    trace_links.append((source_number, target_number, similarity))
        self.trace_links.extend(trace_links)
