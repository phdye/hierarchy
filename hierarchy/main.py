"""
Hierarchy

Usage:
  hierarchy [options] <directory>
  hierarchy (-h | --help)
  hierarchy --version
  --zip         Generate zip file of the directory structure.
"""

import os
from hierarchy.gitignore_handler import GitignoreHandler
from hierarchy.directory_tree import DirectoryTree, display_tree
from docopt import docopt

def main(args):
    directory = os.path.realpath(args['<directory>'])
    generate_zip = args['--zip']
    
    # Define paths for .gitignore files
    gitignore_paths = [
        os.path.join(directory, '.gitignore'),
        os.path.expanduser('~/.gitignore'),
        '/etc/gitignore'
    ]

    # Initialize GitignoreHandler
    gitignore_handler = GitignoreHandler(gitignore_paths)

    # Initialize DirectoryTree
    directory_tree = DirectoryTree(directory, gitignore_handler)

    if generate_zip:
        # Create zip and generate tree structure
        tree_structure = directory_tree.create_zip(os.path.join(directory, 'directory_structure.zip'))
        print("Directory structure zipped into:", os.path.join(directory, 'directory_structure.zip'))
    else:
        # Generate tree structure without zip
        tree_structure = directory_tree.build_tree()
    
    # Display the tree structure
    display_tree(tree_structure)

if __name__ == "__main__":
    args = docopt(__doc__, version="Hierarchy 0.1.0")
    main(args)
