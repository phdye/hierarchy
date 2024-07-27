import os
import pathspec

class GitignoreHandler:
    def __init__(self, gitignore_paths):
        self.specs = self._load_gitignore_files(gitignore_paths)

    def _load_gitignore_files(self, paths):
        specs = []
        for path in paths:
            real_path = os.path.realpath(path)  # Resolve symbolic links
            if os.path.exists(real_path):
                with open(real_path, 'r') as f:
                    spec = pathspec.PathSpec.from_lines('gitwildmatch', f)
                    specs.append((spec, os.path.dirname(real_path)))
        return specs

    def is_ignored(self, filepath):
        abs_filepath = os.path.realpath(filepath)  # Convert to absolute path
        for spec, base_dir in self.specs:
            rel_filepath = os.path.relpath(abs_filepath, base_dir)  # Relative to .gitignore's directory
            if spec.match_file(rel_filepath):
                return True
        return False
