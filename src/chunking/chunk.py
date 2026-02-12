from typing import Dict

class Chunk:
    """
    Represents a chunk of text derived from a Document.
    """

    def __init__(
        self,
        content: str,
        metadata: Dict,
        chunk_id: int,
        start_index: int,
        end_index: int
    ):
        self.content = content
        self.metadata = metadata
        self.chunk_id = chunk_id
        self.start_index = start_index
        self.end_index = end_index

    def __repr__(self):
        return (
            f"Chunk(id={self.chunk_id}, "
            f"length={len(self.content)}, "
            f"range=({self.start_index}, {self.end_index}))"
        )
    
