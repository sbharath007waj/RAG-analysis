from loaders.pdf_loader import PdfLoader

def test_valid_pdf_file():
    loader = PdfLoader()
    docs = loader.load("sample.pdf")

    assert isinstance(docs, list)
    assert len(docs) > 0

    first_doc = docs[0]

    assert isinstance(first_doc.content, str)
    assert first_doc.content.strip() != ""

    assert first_doc.metadata["file_type"] == "pdf"
    assert "source" in first_doc.metadata
    assert "page" in first_doc.metadata
    assert first_doc.metadata["page"] >= 1


def test_invalid_pdf_file():
    loader = PdfLoader()

    try:
        loader.load("non_existing.pdf")
    except FileNotFoundError:
        return

    assert False