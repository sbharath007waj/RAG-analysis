from abc import ABC, abstractmethod
from typing import List, Dict

from chunking.chunk import Chunk


class BaseVectorStore(ABC):
    """
    Abstract base class for vector storage and retrieval.
    """

    @abstractmethod
    def add(self, chunks: List[Chunk], embeddings: List[List[float]]):
        """
        Add chunks and their embeddings to the store.
        """
        pass

    @abstractmethod
    def query(self, query_embedding: List[float], k: int) -> List[Dict]:
        """
        Retrieve top-k similar chunks.
        """
        pass
