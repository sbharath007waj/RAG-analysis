from abc import ABC, abstractmethod
from typing import List, Dict


class BaseRetriever(ABC):
    """
    Abstract retrieval strategy interface.
    """

    @abstractmethod
    def retrieve(self, query: str, k: int) -> List[Dict]:
        """
        Retrieve top-k relevant chunks for a query.
        """
        pass
