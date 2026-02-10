from typing import List
import os
import fitz  # PyMuPDF

from loaders.base_loader import BaseLoader
from loaders.document import Document

class PdfLoader(BaseLoader):

    def load(self, file_path: str) -> List[Document]:

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not file_path.lower().endswith(".pdf"):
            raise ValueError("PdfLoader only supports .pdf files")
        
        try:
            pdf = fitz.open(file_path)
        except Exception as e:
            raise RuntimeError(f"Error reading file: {e}")
        
        documents = []
        for page_number in range(len(pdf)):
            page= pdf[page_number]
            text = page.get_text().strip()

            if not text:
                continue
        
            metadata = {
            "source": file_path,
            "file_type": "pdf",
            "page": page_number + 1
        }

        document = Document(content=text, metadata=metadata)
        documents.append(document)
        pdf.close()
        return documents
