from typing import List
from loaders.document import Document
from chunking.chunk import Chunk
from chunking.base_chunker import BaseChunker

class FixedChunker(BaseChunker):

    def __init__(self, chunk_size: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")

        self.chunk_size = chunk_size
    
    def chunk(self, document: Document) -> List[Chunk]:
        text = document.content
        chunks: List[Chunk] = []

        start = 0
        chunk_id = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk_text = text[start:end]

            metadata = document.metadata.copy()
            metadata.update({
                "chunk_id": chunk_id,
                "start_index": start,
                "end_index": min(end, len(text))
            })

            chunk = Chunk(
                content=chunk_text,
                metadata=metadata,
                chunk_id=chunk_id,
                start_index=start,
                end_index=min(end, len(text))
            )

            chunks.append(chunk)

            start = end
            chunk_id += 1

        return chunks


