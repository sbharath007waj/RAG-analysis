from loaders.document import Document
from chunking.fixed_chunker import FixedChunker
from embedding.sentence_embedder import SentenceEmbedder
from vector_store.chroma_store import ChromaStore


def test_chroma_add_and_query():
    # Create simple document
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
    store = ChromaStore(collection_name="test_collection")
    store.add(chunks, embeddings)

    # Query
    query_embedding = embedder.embed(["What is AI?"])[0]
    results = store.query(query_embedding, k=2)

    # Assertions
    assert isinstance(results, list)
    assert len(results) > 0

    first_result = results[0]

    assert "content" in first_result
    assert "metadata" in first_result
    assert "distance" in first_result

    assert isinstance(first_result["content"], str)
    assert isinstance(first_result["metadata"], dict)
    assert isinstance(first_result["distance"], float)
