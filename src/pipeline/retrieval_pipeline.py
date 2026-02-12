from typing import List

from loaders.document import Document
from chunking.base_chunker import BaseChunker
from embedding.base_embedder import BaseEmbedder
from retriever.base_retriever import BaseRetriever
from chunking.chunk import Chunk

class RetrievalPipeline:
    """
    Orchestrates indexing and retrieval.
    """
    def __init__(
        self,
        chunker: BaseChunker,
        embedder: BaseEmbedder,
        retriever: BaseRetriever
    ):
        self.chunker = chunker
        self.embedder = embedder
        self.retriever = retriever

    def index_documents(self, documents: List[Document]):
        all_chunks: List[Chunk] = []

        for document in documents:
            chunks = self.chunker.chunk(document)
            all_chunks.extend(chunks)

        embeddings = self.embedder.embed(
            [chunk.content for chunk in all_chunks]
        )

        # Vector store is accessed through retriever
        self.retriever.vector_store.add(all_chunks, embeddings)

    def search(self, query: str, k: int):
        return self.retriever.retrieve(query, k)



