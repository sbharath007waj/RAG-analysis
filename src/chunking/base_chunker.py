from abc import ABC, abstractmethod
from typing import List
from loaders.document import Document
from chunking.chunk import Chunk

class BaseChunker(ABC):
    """
    Abstract base class for all chunking strategies.
    """

    @abstractmethod
    def chunk(self, document: Document) -> List[Chunk]:
        """
        Splits a Document into a list of Chunks.
        """
        pass