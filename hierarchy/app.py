import os
from hierarchy.gitignore_handler import GitignoreHandler
from hierarchy.directory_tree import DirectoryTree
from hierarchy.zip_creator import ZipCreator
from hierarchy.tree_node import TreeNode

def display_tree(node, prefix=''):
    """
    Display the directory tree structure starting from the given node.

    Parameters:
    - node: The current TreeNode to display.
    - prefix: The prefix to use for the current level of the tree structure.
    """
    if node.is_directory:
        print(prefix + node.name + "/")
        prefix += "│   "
        for idx, child in enumerate(node.children):
            if idx == len(node.children) - 1:
                display_tree(child, prefix[:-4] + "    ")
            else:
                display_tree(child, prefix)
    else:
        print(prefix + node.name)

def app(args):
    directory = os.path.realpath(args['<directory>'])
    generate_zip = args['--zip']
    no_display = args['--no-display']
    
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

    # Build the tree structure
    tree_structure = directory_tree.build_tree()
    
    if not no_display:
        # Display the tree structure
        display_tree(tree_structure)
    
    if generate_zip:
        # Create the zip file
        zip_creator = ZipCreator(tree_structure, directory)
        zip_creator.create_zip(os.path.join(directory, 'directory_structure.zip'))
        print("Directory structure zipped into:", os.path.join(directory, 'directory_structure.zip'))
