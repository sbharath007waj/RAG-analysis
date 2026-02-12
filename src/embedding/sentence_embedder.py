import time
from typing import List

from sentence_transformers import SentenceTransformer

from embedding.base_embedder import BaseEmbedder


class SentenceEmbedder(BaseEmbedder):
    """
    Wrapper around a SentenceTransformer model.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> List[List[float]]:
        start_time = time.time()

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        elapsed_time = time.time() - start_time

        print(f"Embedding time for {len(texts)} texts: {elapsed_time:.4f} seconds")

        return embeddings.tolist()
