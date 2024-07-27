
import os
import argparse
from hierarchy.gitignore_handler import GitignoreHandler
from hierarchy.directory_tree import DirectoryTree

def main():
    parser = argparse.ArgumentParser(description='Print directory hierarchy and create a zip file.')
    parser.add_argument('directory', nargs='?', default=os.getcwd(), help='Target directory to list and zip (default: current directory)')
    args = parser.parse_args()

    directory_to_zip = args.directory
    output_zip = os.path.join(directory_to_zip, 'directory_structure.zip')

    gitignore_paths = [
        os.path.join(directory_to_zip, '.gitignore'),
        os.path.expanduser('~/.gitignore'),
        '/etc/gitignore'
    ]

    gitignore_handler = GitignoreHandler(gitignore_paths)
    directory_tree = DirectoryTree(directory_to_zip, gitignore_handler)

    tree_structure_output = directory_tree.create_zip(output_zip)

    print(tree_structure_output)
    print(f"\nDirectory structure zipped into: {output_zip}")

if __name__ == "__main__":
    main()
