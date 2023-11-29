"""TF-IDF tracer."""
from server.trace.tracer import Tracer


class TFIDF(Tracer):
    """TF-IDF trace method."""

    def __init__(self):
        super().__init__()
        self.trace_method = "tfidf"

    def find_links(self, source_artifacts, target_artifacts):
        super().find_links(source_artifacts, target_artifacts)
        # TODO1: Implement TF-IDF tracing
        raise NotImplementedError
