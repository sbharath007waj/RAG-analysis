from typing import List
from loaders.document import Document
from chunking.chunk import Chunk
from chunking.base_chunker import BaseChunker

class OverlapChunker(BaseChunker):
    def __init__(self, chunk_size: int, overlap: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")

        if overlap < 0:
            raise ValueError("overlap cannot be negative")

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap
    def chunk(self, document: Document) -> List[Chunk]:
        text = document.content
        chunks: List[Chunk] = []

        start = 0
        chunk_id = 0

        step = self.chunk_size - self.overlap

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

            start += step
            chunk_id += 1

        return chunks


