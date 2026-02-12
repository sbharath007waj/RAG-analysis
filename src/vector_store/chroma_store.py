import time
from typing import List, Dict

import chromadb
from chromadb.config import Settings

from chunking.chunk import Chunk
from vector_store.base_vector_store import BaseVectorStore


class ChromaStore(BaseVectorStore):
    """
    Chroma-based vector store implementation.
    """

    def __init__(self, collection_name: str = "rag_collection"):
        self.client = chromadb.Client(
            Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )
    def add(self, chunks: List[Chunk], embeddings: List[List[float]]):
        if len(chunks) != len(embeddings):
            raise ValueError("Chunks and embeddings must have same length")

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:
            ids.append(f"{chunk.metadata.get('source', 'unknown')}_{chunk.chunk_id}")
            documents.append(chunk.content)
            metadatas.append(chunk.metadata)

        start_time = time.time()

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

        elapsed_time = time.time() - start_time
        print(f"Vector store add time: {elapsed_time:.4f} seconds")

    def query(self, query_embedding: List[float], k: int) -> List[Dict]:
        start_time = time.time()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        elapsed_time = time.time() - start_time
        print(f"Vector store query time: {elapsed_time:.4f} seconds")

        retrieved = []

        for i in range(len(results["documents"][0])):
            retrieved.append({
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i]
            })

        return retrieved


