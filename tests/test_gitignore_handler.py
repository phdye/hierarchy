import pytest
from pdirtree.gitignore_handler import GitignoreHandler

def test_is_ignored():
    # Test normal use case
    handler = GitignoreHandler(['*.txt'])
    assert handler.is_ignored('example/file1.txt')
    assert not handler.is_ignored('example/file1.py')

def test_load_gitignore_files():
    # Test loading .gitignore files
    handler = GitignoreHandler([])
    handler._load_gitignore_files(['example/.gitignore'])
    assert '*.txt' in handler.specs
