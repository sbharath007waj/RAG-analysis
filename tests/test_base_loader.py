from loaders.base_loader import BaseLoader

class DummyLoader(BaseLoader):
    def load(self,file_path: str):
        return []
