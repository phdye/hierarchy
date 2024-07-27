"""
Hierarchy

Usage:
  hierarchy [options] <directory>
  hierarchy (-h | --help)
  hierarchy --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import os
from hierarchy.gitignore_handler import GitignoreHandler
from hierarchy.directory_tree import DirectoryTree
from docopt import docopt

def main(args):
    print("Starting main function")
    directory = os.path.realpath(args['<directory>'])
    print(f"Resolved directory: {directory}")
    
    # Define paths for .gitignore files
    gitignore_paths = [
        os.path.join(directory, '.gitignore'),
        os.path.expanduser('~/.gitignore'),
        '/etc/gitignore'
    ]
    print(f"Gitignore paths: {gitignore_paths}")

    # Initialize GitignoreHandler
    gitignore_handler = GitignoreHandler(gitignore_paths)
    print("Initialized GitignoreHandler")

    # Initialize DirectoryTree
    directory_tree = DirectoryTree(directory, gitignore_handler)
    print("Initialized DirectoryTree")

    # Create zip and generate tree structure
    tree_structure_output = directory_tree.create_zip(os.path.join(directory, 'directory_structure.zip'))
    print("Created zip file")

    # Print tree structure
    print(tree_structure_output)
    print(f"\nDirectory structure zipped into: {os.path.join(directory, 'directory_structure.zip')}")

if __name__ == "__main__":
    args = docopt(__doc__, version="Hierarchy 0.1.0")
    main(args)
