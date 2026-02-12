from loaders.document import Document
from chunking.fixed_chunker import FixedChunker
from embedding.sentence_embedder import SentenceEmbedder
from vector_store.chroma_store import ChromaStore
from retriever.dense_retriever import DenseRetriever


def test_dense_retriever_basic():
    text = "Artificial intelligence is powerful. Machine learning is part of AI."

    document = Document(
        content=text,
        metadata={"source": "unit_test", "file_type": "txt"}
    )

    # Chunk
    chunker = FixedChunker(chunk_size=50)
    chunks = chunker.chunk(document)

    # Embed
    embedder = SentenceEmbedder()
    embeddings = embedder.embed([chunk.content for chunk in chunks])

    # Store
    store = ChromaStore(collection_name="dense_test_collection")
    store.add(chunks, embeddings)

    # Retriever
    retriever = DenseRetriever(embedder=embedder, vector_store=store)

    results = retriever.retrieve("What is AI?", k=2)

    # Assertions
    assert isinstance(results, list)
    assert len(results) > 0

    first = results[0]

    assert "content" in first
    assert "metadata" in first
    assert "distance" in first

    assert isinstance(first["content"], str)
    assert isinstance(first["metadata"], dict)
    assert isinstance(first["distance"], float)
