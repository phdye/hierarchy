import os
import pytest
from unittest import mock
from pdirtree.directory_tree import DirectoryTree
from pdirtree.gitignore_handler import GitignoreHandler

def test_permission_denied(monkeypatch):
    def mock_os_walk(_):
        raise PermissionError("Permission Denied")
    monkeypatch.setattr(os, 'walk', mock_os_walk)
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir='restricted', gitignore_handler=gitignore_handler)
    with pytest.raises(PermissionError):
        directory_tree.build_tree()

def test_circular_references(monkeypatch):
    def mock_os_walk(_):
        raise RecursionError("Circular Reference")
    monkeypatch.setattr(os, 'walk', mock_os_walk)
    gitignore_handler = GitignoreHandler([])
    directory_tree = DirectoryTree(root_dir='circular', gitignore_handler=gitignore_handler)
    with pytest.raises(RecursionError):
        directory_tree.build_tree()
