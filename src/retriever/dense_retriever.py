from typing import List, Dict

from embedding.base_embedder import BaseEmbedder
from vector_store.base_vector_store import BaseVectorStore
from retriever.base_retriever import BaseRetriever

class DenseRetriever(BaseRetriever):
    """
    Dense retrieval using embeddings + vector similarity search.
    """

    def __init__(
        self,
        embedder: BaseEmbedder,
        vector_store: BaseVectorStore
    ):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int) -> List[Dict]:
        # Step 1: Embed query
        query_embedding = self.embedder.embed([query])[0]

        # Step 2: Query vector store
        results = self.vector_store.query(query_embedding, k)

        return results
