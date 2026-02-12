from embedding.sentence_embedder import SentenceEmbedder


def test_sentence_embedder_basic():
    embedder = SentenceEmbedder()

    texts = [
        "Artificial intelligence is powerful.",
        "Machine learning is a subset of AI."
    ]

    embeddings = embedder.embed(texts)

    # Check structure
    assert isinstance(embeddings, list)
    assert len(embeddings) == 2

    # Each embedding should be a list of floats
    assert isinstance(embeddings[0], list)
    assert isinstance(embeddings[0][0], float)

    # Check embedding dimensionality (MiniLM-L6-v2 = 384 dims)
    assert len(embeddings[0]) == 384
