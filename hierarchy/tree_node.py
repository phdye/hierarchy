class TreeNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self):
        return f"TreeNode(name={self.name}, is_directory={self.is_directory}, children={len(self.children)})"
