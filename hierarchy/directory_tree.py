import os
import zipfile

class TreeNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"TreeNode(name={self.name}, is_directory={self.is_directory}, children={len(self.children)})"

class DirectoryTree:
    def __init__(self, root_dir, gitignore_handler=None):
        """
        Initialize the DirectoryTree with the root directory and an optional gitignore handler.
        Resolve the root directory to its absolute path.
        
        Parameters:
        - root_dir: The root directory to start building the tree from.
        - gitignore_handler: An optional handler to check if files or directories are ignored.
        """
        self.root_dir = os.path.realpath(root_dir)  # Resolve to absolute path
        self.gitignore_handler = gitignore_handler

    def build_tree(self, root_dir=None):
        """
        Recursively build the directory tree as a TreeNode structure.

        Parameters:
        - root_dir: The current directory to build the tree from. Defaults to the initial root_dir.

        Returns:
        - A TreeNode representing the directory tree structure.
        """
        if root_dir is None:
            root_dir = self.root_dir  # Use the initial root directory if not specified

        # Check if the specified directory is valid
        if not os.path.isdir(root_dir):
            return TreeNode(name=f"{root_dir} is not a valid directory.")

        root_node = TreeNode(name=os.path.basename(root_dir), is_directory=True)

        files_and_dirs = sorted(os.listdir(root_dir))
        for name in files_and_dirs:
            path = os.path.join(root_dir, name)
            
            # Skip the .git directory and symbolic links
            if name == '.git' or os.path.islink(path):
                continue

            # Check if the current item is a directory
            if os.path.isdir(path):
                if not self.gitignore_handler or not self.gitignore_handler.is_ignored(path):
                    child_node = self.build_tree(path)
                    root_node.add_child(child_node)
            else:
                if not self.gitignore_handler or not self.gitignore_handler.is_ignored(path):
                    root_node.add_child(TreeNode(name=name, is_directory=False))
        
        return root_node

    def create_zip(self, output_zip):
        """
        Create a zip file containing the directory structure.

        Parameters:
        - output_zip: The path to the output zip file.

        Returns:
        - The directory tree structure as a TreeNode.
        """
        root_node = self.build_tree()  # Build the directory tree structure

        # Create the zip file and add files that are not ignored
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            for root, dirs, files in os.walk(self.root_dir):
                # Skip the .git directory and symbolic links
                if '.git' in dirs:
                    dirs.remove('.git')
                dirs[:] = [d for d in dirs if not os.path.islink(os.path.join(root, d))]
                for file in files:
                    abs_filepath = os.path.join(root, file)
                    if os.path.islink(abs_filepath):
                        continue  # Skip symlink files
                    rel_filepath = os.path.relpath(abs_filepath, self.root_dir)  # Relative to root directory
                    if not self.gitignore_handler or not self.gitignore_handler.is_ignored(abs_filepath):
                        zipf.write(abs_filepath, rel_filepath)

        return root_node

def display_tree(node, prefix=''):
    """
    Display the directory tree structure starting from the given node.

    Parameters:
    - node: The current TreeNode to display.
    - prefix: The prefix to use for the current level of the tree structure.
    """
    if node.is_directory:
        print(prefix + node.name + "/")
        prefix += "│   "
        for idx, child in enumerate(node.children):
            if idx == len(node.children) - 1:
                display_tree(child, prefix[:-4] + "    ")
            else:
                display_tree(child, prefix)
    else:
        print(prefix + node.name)
