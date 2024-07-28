
#!/usr/bin/env python

"""pdirtree

Usage:
  pdirtree [options] <directory>
  pdirtree (-h | --help)
  pdirtree --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --zip             Generate a zip file of the directory structure.
  --no-display      Do not display the hierarchy. This option can be used independently or in conjunction with --zip.

Arguments:
  <directory>       The directory to scan and display its structure.

Description:
  The `pdirtree` command-line tool scans the specified <directory> and displays its structure
  in a tree-like format. It respects .gitignore rules and handles symbolic links appropriately.

  The tool can also generate a zip file containing the directory structure if the --zip option is specified.
  When the --no-display option is used, the tool will suppress the display of the directory structure,
  which is particularly useful when only a zip file is needed.

Examples:
  Display the structure of the current directory:
    pdirtree .

  Display the structure of a specific directory:
    pdirtree /path/to/directory

  Generate a zip file of the directory structure:
    pdirtree --zip /path/to/directory

  Generate a zip file without displaying the structure:
    pdirtree --zip --no-display /path/to/directory

  Display the version of the tool:
    pdirtree --version
""" 

from docopt import docopt
import toml
import os
from pdirtree.app import app

def get_version():
    pyproject_path = os.path.join(os.path.dirname(__file__), '..', '..', 'pyproject.toml')
    pyproject = toml.load(pyproject_path)
    return pyproject['tool']['poetry']['version']

if __name__ == "__main__":
    args = docopt(__doc__, version=get_version())
    app(args)
