from loaders.docx_loader import DocxLoader

def test_valid_docx_file():
    loader=DocxLoader()
    docs = loader.load("sample.docx")
    assert isinstance(docs, list)
    assert len(docs) == 1
    assert isinstance(docs[0].content, str)
    assert docs[0].metadata["file_type"] == "docx"
    assert "source" in docs[0].metadata
    assert "This is a valid DOCX file." in docs[0].content

def test_invalid_docx_file():
    loader = DocxLoader()

    try:
        loader.load("non_existing.docx")
    except FileNotFoundError:
        return

    assert False