import os
import zipfile

class DirectoryTree:
    def __init__(self, root_dir, gitignore_handler=None):
        self.root_dir = os.path.abspath(root_dir)
        self.gitignore_handler = gitignore_handler

    def build_tree_structure(self, prefix=''):
        if not os.path.isdir(self.root_dir):
            return [f"{self.root_dir} is not a valid directory."]

        tree_structure = []
        tree_structure.append(prefix + os.path.basename(self.root_dir) + "/")
        prefix += "│   "

        files_and_dirs = sorted(os.listdir(self.root_dir))
        for idx, name in enumerate(files_and_dirs):
            path = os.path.join(self.root_dir, name)
            if os.path.isdir(path):
                if idx == len(files_and_dirs) - 1:
                    tree_structure.append(prefix[:-4] + "└── " + name + "/")
                    tree_structure.extend(
                        DirectoryTree(path, self.gitignore_handler).build_tree_structure(prefix[:-4] + "    ")
                    )
                else:
                    tree_structure.append(prefix[:-4] + "├── " + name + "/")
                    tree_structure.extend(
                        DirectoryTree(path, self.gitignore_handler).build_tree_structure(prefix)
                    )
            else:
                if not self.gitignore_handler or not self.gitignore_handler.is_ignored(path):
                    if idx == len(files_and_dirs) - 1:
                        tree_structure.append(prefix[:-4] + "└── " + name)
                    else:
                        tree_structure.append(prefix[:-4] + "├── " + name)
        return tree_structure

    def create_zip(self, output_zip):
        tree_structure = self.build_tree_structure()

        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            for root, dirs, files in os.walk(self.root_dir):
                for file in files:
                    filepath = os.path.relpath(os.path.join(root, file), self.root_dir)
                    if not self.gitignore_handler or not self.gitignore_handler.is_ignored(filepath):
                        zipf.write(os.path.join(root, file), filepath)

        return "\n".join(tree_structure)