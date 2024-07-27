import os
import tempfile
import unittest
from hierarchy.directory_tree import DirectoryTree
from hierarchy.gitignore_handler import GitignoreHandler

class TestDirectoryTree(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root_dir = self.temp_dir.name
        os.makedirs(os.path.join(self.root_dir, 'subdir'))
        with open(os.path.join(self.root_dir, 'file.txt'), 'w') as f:
            f.write('test file')
        with open(os.path.join(self.root_dir, 'subdir', 'file.py'), 'w') as f:
            f.write('test file')

        self.gitignore_path = os.path.join(self.root_dir, '.gitignore')
        with open(self.gitignore_path, 'w') as f:
            f.write('*.py\n')

        self.gitignore_handler = GitignoreHandler([self.gitignore_path])
        self.directory_tree = DirectoryTree(self.root_dir, self.gitignore_handler)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_build_tree_structure(self):
        tree_structure = self.directory_tree.build_tree_structure()
        expected_structure = [
            os.path.basename(self.root_dir) + '/',
            '│   ├── .gitignore',
            '│   ├── file.txt',
            '│   └── subdir/',
        ]
        self.assertEqual(tree_structure[:3], expected_structure[:3])

    def test_create_zip(self):
        output_zip = os.path.join(self.root_dir, 'directory_structure.zip')
        tree_structure_output = self.directory_tree.create_zip(output_zip)
        self.assertTrue(os.path.exists(output_zip))
        expected_structure_output = "\n".join([
            os.path.basename(self.root_dir) + '/',
            '│   ├── .gitignore',
            '│   ├── file.txt',
            '│   └── subdir/',
        ])
        self.assertIn(expected_structure_output, tree_structure_output)

if __name__ == '__main__':
    unittest.main()
