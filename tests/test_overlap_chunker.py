from loaders.document import Document
from chunking.overlap_chunker import OverlapChunker


def test_overlap_chunking_basic():
    text = "abcdefghijklmnopqrstuvwxyz"  # length = 26

    document = Document(
        content=text,
        metadata={"source": "unit_test", "file_type": "txt"}
    )

    chunker = OverlapChunker(chunk_size=10, overlap=2)
    chunks = chunker.chunk(document)

    # Expected windows:
    # 0–10  -> abcdefghij
    # 8–18  -> ijklmnopqr
    # 16–26 -> qrstuvwxyz

    assert len(chunks) == 4

    assert chunks[0].content == "abcdefghij"
    assert chunks[1].content == "ijklmnopqr"
    assert chunks[2].content == "qrstuvwxyz"

    # Check correct start positions
    assert chunks[0].start_index == 0
    assert chunks[1].start_index == 8
    assert chunks[2].start_index == 16

    # Check metadata inheritance
    assert chunks[0].metadata["source"] == "unit_test"
    assert chunks[0].metadata["file_type"] == "txt"

    # Check chunk ids
    assert chunks[0].metadata["chunk_id"] == 0
    assert chunks[1].metadata["chunk_id"] == 1
    assert chunks[2].metadata["chunk_id"] == 2

    assert chunks[3].content == "yz"
    assert chunks[3].start_index == 24
    assert chunks[3].end_index == 26



def test_invalid_overlap():
    text = "abcdef"

    document = Document(
        content=text,
        metadata={}
    )

    try:
        OverlapChunker(chunk_size=5, overlap=5)
    except ValueError:
        return

    assert False
