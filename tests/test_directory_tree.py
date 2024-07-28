import os
import pytest
from pdirtree.directory_tree import DirectoryTree
from pdirtree.gitignore_handler import GitignoreHandler
from pdirtree.tree_node import TreeNode

example_dir = '/mnt/data/pdtree/example'

def test_empty_directory():
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir=os.path.join(example_dir, 'empty_dir'), gitignore_handler=gitignore_handler)
    tree = directory_tree.build_tree()
    assert isinstance(tree, TreeNode)
    assert len(tree.children) == 0

def test_nested_directories():
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir=os.path.join(example_dir, 'nested'), gitignore_handler=gitignore_handler)
    tree = directory_tree.build_tree()
    assert isinstance(tree, TreeNode)
    assert len(tree.children) == 1
    assert tree.children[0].name == "dir"

def test_symbolic_links():
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir=os.path.join(example_dir, 'symlink'), gitignore_handler=gitignore_handler)
    tree = directory_tree.build_tree()
    assert isinstance(tree, TreeNode)
    assert any(child.name == "link.txt" for child in tree.children)

def test_large_directory():
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir=os.path.join(example_dir, 'large'), gitignore_handler=gitignore_handler)
    tree = directory_tree.build_tree()
    assert isinstance(tree, TreeNode)
    assert len(tree.children) == 1000

def test_complex_gitignore_patterns():
    gitignore_handler = GitignoreHandler([os.path.join(example_dir, '.gitignore')])
    directory_tree = DirectoryTree(root_dir=example_dir, gitignore_handler=gitignore_handler)
    tree = directory_tree.build_tree()
    assert isinstance(tree, TreeNode)
    assert any(child.name == "file.txt" for child in tree.children)
    assert not any(child.name == "file.py" for child in tree.children)
