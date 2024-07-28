import os
from pdirtree.tree_node import TreeNode

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
