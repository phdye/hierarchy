import os
import zipfile

class ZipCreator:
    def __init__(self, root_node, root_dir):
        self.root_node = root_node
        self.root_dir = root_dir

    def create_zip(self, output_zip):
        """
        Create a zip file containing the directory structure.

        Parameters:
        - output_zip: The path to the output zip file.
        """
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
            self._add_node_to_zip(zipf, self.root_node, self.root_dir)

    def _add_node_to_zip(self, zipf, node, current_path):
        """
        Recursively add nodes to the zip file.

        Parameters:
        - zipf: The ZipFile object.
        - node: The current TreeNode.
        - current_path: The current path in the directory structure.
        """
        for child in node.children:
            child_path = os.path.join(current_path, child.name)
            if child.is_directory:
                self._add_node_to_zip(zipf, child, child_path)
            else:
                zipf.write(child_path, os.path.relpath(child_path, self.root_dir))
