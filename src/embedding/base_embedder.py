from abc import ABC, abstractmethod
from typing import List


class BaseEmbedder(ABC):
    """
    Abstract base class for embedding models.
    """

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        """
        Converts a list of texts into a list of embedding vectors.
        """
        pass
