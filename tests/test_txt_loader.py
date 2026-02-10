from loaders.txt_loader import TxtLoader
loader = TxtLoader()
docs = loader.load("tests/data/sample.txt")
print(docs)
print(docs[0].content)
print(docs[0].metadata)