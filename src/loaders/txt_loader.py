from typing import List
from .base_loader import BaseLoader
from .document import Document
import os


class TxtLoader(BaseLoader):

    def load(self, file_path: str) -> List[Document]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        try:
             with open(file_path, "r", encoding="utf-8") as file:
               content = file.read()
        except Exception as e:
               raise RuntimeError(f"Error reading file: {e}")

        metadata = {
                    "source": file_path,
                    "file_type": "text"
                }   
        document = Document(content=content, metadata=metadata)
        return [document]