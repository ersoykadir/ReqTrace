"""LLM tracer"""
from server.trace.tracer import Tracer


class LLM(Tracer):
    """LLM trace method."""

    def __init__(self):
        super().__init__()
        self.trace_method = "llm"

    def find_links(self, source_artifacts, target_artifacts):
        super().find_links(source_artifacts, target_artifacts)
        # TODO1: Implement LLM tracing
        raise NotImplementedError
