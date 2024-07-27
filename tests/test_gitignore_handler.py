
import os
import tempfile
import unittest
from hierarchy.gitignore_handler import GitignoreHandler

class TestGitignoreHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.gitignore_path = os.path.join(self.temp_dir.name, '.gitignore')
        with open(self.gitignore_path, 'w') as f:
            f.write('*.pyc
__pycache__
')

        self.handler = GitignoreHandler([self.gitignore_path])

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_is_ignored(self):
        self.assertTrue(self.handler.is_ignored('test.pyc'))
        self.assertTrue(self.handler.is_ignored('subdir/__pycache__'))
        self.assertFalse(self.handler.is_ignored('test.py'))

if __name__ == '__main__':
    unittest.main()
