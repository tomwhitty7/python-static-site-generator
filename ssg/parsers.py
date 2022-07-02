from typing import List
from pathlib import Path
import shutil

class Parser:
    extenstions = [] # list of str

    def valid_extension(self, extension):
        return extension in self.extenstions

    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path, "rt") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / self.path.with_suffix(ext).name
        with open(full_path, "wt") as file:
            file.write(content)

    def copy(self, path, source, dest):
        copy2(self.path, self.dest / path.relative_to(self.source))

    def ResourceParser(self, extensions=(".jpg", ".png", ".gif", "css", ".html")):
        parse(self.path, self.source, self.dest)
        copy(self.path, self.source, self.dest)
