from loaders.document import Document
from chunking.fixed_chunker import FixedChunker
from embedding.sentence_embedder import SentenceEmbedder
from vector_store.chroma_store import ChromaStore
from retriever.dense_retriever import DenseRetriever
from pipeline.retrieval_pipeline import RetrievalPipeline


def test_retrieval_pipeline_end_to_end():
    text = (
        "Artificial intelligence is powerful. "
        "Machine learning is a subset of AI. "
        "Deep learning is part of machine learning."
    )

    document = Document(
        content=text,
        metadata={"source": "pipeline_test", "file_type": "txt"}
    )

    # Components
    chunker = FixedChunker(chunk_size=60)
    embedder = SentenceEmbedder()
    store = ChromaStore(collection_name="pipeline_test_collection")
    retriever = DenseRetriever(embedder=embedder, vector_store=store)

    # Pipeline
    pipeline = RetrievalPipeline(
        chunker=chunker,
        embedder=embedder,
        retriever=retriever
    )

    # Index
    pipeline.index_documents([document])

    # Search
    results = pipeline.search("What is machine learning?", k=2)

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
