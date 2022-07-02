from typing import List
from pathlib import Path
import shutil

class Parser:
    extenstions List[str] = []

    def valid_extension(self, extension):
        return extension in self.extenstions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplemented

    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(self.source))

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", "css", ".html"]

    def parse(self, path, source, dest)
        self.copy(path, source, dest)
