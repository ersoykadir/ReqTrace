"""Tracer module."""


class Tracer:
    """Tracer class."""

    def __init__(self):
        self.trace_method = None
        self.trace_links = []  # Not sure how to represent trace links yet!!!

    def find_links(self, source_artifacts, target_artifacts, threshold):
        """Find trace links from source artifacts to target artifacts."""
        # Add found trace links to self.trace_links, do not overwrite existing trace links
        print(f"Finding trace links from {source_artifacts} to {target_artifacts}... with threshold {threshold}")

    def find_natural_links(self, source_artifacts, target_artifacts):
        """Find natural trace links from source artifacts to target artifacts."""
        # Add found trace links to self.trace_links, do not overwrite existing trace links
        print(f"Finding natural trace links from {source_artifacts} to {target_artifacts}...")
        raise NotImplementedError

    def get_trace_links(self):
        """Return trace links."""
        return self.trace_links
