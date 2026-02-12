from loaders.document import Document
from chunking.fixed_chunker import FixedChunker

def test_fixed_chunker():
    text = "abcdefghijklmnopqrstuvwxyz"  # length = 26
    document = Document(content=text,
                        metadata={"source": "unit_test", "file_type": "txt"})
    chunker = FixedChunker(chunk_size=10)
    chunks = chunker.chunk(document)
    
    # We expect 3 chunks: 10, 10, 6
    assert len(chunks) == 3

    assert chunks[0].content == "abcdefghij"
    assert chunks[1].content == "klmnopqrst"
    assert chunks[2].content == "uvwxyz"

    # Check metadata propagation
    assert chunks[0].metadata["source"] == "unit_test"
    assert chunks[0].metadata["file_type"] == "txt"

    # Check chunk-specific metadata
    assert chunks[0].metadata["chunk_id"] == 0
    assert chunks[1].metadata["chunk_id"] == 1

    assert chunks[0].start_index == 0
    assert chunks[0].end_index == 10

    assert chunks[2].start_index == 20
    assert chunks[2].end_index == 26

