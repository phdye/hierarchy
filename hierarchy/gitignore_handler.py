import os
from gitignore_parser import parse_gitignore

class GitignoreHandler:
    def __init__(self, paths):
        self.base_path = os.path.dirname(os.path.abspath(paths[0]))  # Use the first .gitignore file's directory as base path
        self.matchers = self._load_gitignore_files(paths)

    def _load_gitignore_files(self, paths):
        matchers = []
        for path in paths:
            if os.path.exists(path):
                matchers.append(parse_gitignore(path))
        return matchers

    def is_ignored(self, filepath):
        abs_filepath = os.path.abspath(filepath)
        rel_filepath = os.path.relpath(abs_filepath, self.base_path)
        return any(matcher(rel_filepath) for matcher in self.matchers)