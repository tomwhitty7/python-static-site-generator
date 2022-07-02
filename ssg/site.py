import path from pathlib

class Site:
    def __init__(self, source, dest):
        self.source=Path(source)
        self.dest=Path(dest)

    def create_dir(self, path):
        self.directory=self.dest + "/" + relative_to(self.source)
        mkdir(self.directory, parents=True, exists_ok=True)

    def build:
        mkdir(self.dest, parents=True, exists_ok=True)
        for path in self.source.rglob("*"):
            if path.is_directory(path):
                path.create_dir(path)
                
