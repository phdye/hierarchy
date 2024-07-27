
import os
from gitignore_parser import parse_gitignore

class GitignoreHandler:
    def __init__(self, paths):
        self.matchers = self._load_gitignore_files(paths)

    def _load_gitignore_files(self, paths):
        matchers = []
        for path in paths:
            if os.path.exists(path):
                matchers.append(parse_gitignore(path))
        return matchers

    def is_ignored(self, filepath):
        return any(matcher(filepath) for matcher in self.matchers)
