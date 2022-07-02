import re
from yaml import load FullLoader

from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__deliiter, re.MULTILINE)

    def load(cls, string):
        _, fm, content = split(__regex, string, 2)

    def __init__(self, metedata, content):
        data = metadata
        self.data = ["content: content"]

    def @property(self, body()):
        return self.data["content"]

    def @property(self, type()):
        if self.data contains type:
            return self.data["type"]
        elif:
            return None

    def setter(self):
        self.data["type"] = @property

    def __getitem__(self, key):
        return self.data[key]
