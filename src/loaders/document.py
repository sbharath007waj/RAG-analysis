from typing import Dict
class Document:
    def __init__(self, content:str, metadata: Dict):
        self.content = content
        self.metadata = metadata
        
    def __repr__(self):
        return f"document(content_length={len(self.content)},metadata={self.metadata})"
    