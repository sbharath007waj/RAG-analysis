from abc import ABC , abstractmethod
from typing import List
from .document import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, file_path: str) -> List[Document]:
        pass
