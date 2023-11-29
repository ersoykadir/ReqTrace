"""Word embeddings tracer."""
from server.trace.tracer import Tracer


class WordEmbeddings(Tracer):
    """Word embeddings trace method."""

    def __init__(self):
        super().__init__()
        self.trace_method = "word_embeddings"

    def find_links(self, source_artifacts, target_artifacts):
        super().find_links(source_artifacts, target_artifacts)
        # TODO1: Implement word embeddings tracing
        raise NotImplementedError
