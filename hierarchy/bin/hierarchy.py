#!/usr/bin/env python

"""Hierarchy

Usage:
  hierarchy [options] <directory>
  hierarchy (-h | --help)
  hierarchy --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  --zip             Generate a zip file of the directory structure.
  --no-display      Do not display the hierarchy. This option can be used independently or in conjunction with --zip.

Arguments:
  <directory>       The directory to scan and display its structure.

Description:
  The `hierarchy` command-line tool scans the specified <directory> and displays its structure
  in a tree-like format. It respects .gitignore rules and handles symbolic links appropriately.

  The tool can also generate a zip file containing the directory structure if the --zip option is specified.
  When the --no-display option is used, the tool will suppress the display of the directory structure,
  which is particularly useful when only a zip file is needed.

Examples:
  Display the structure of the current directory:
    hierarchy .

  Display the structure of a specific directory:
    hierarchy /path/to/directory

  Generate a zip file of the directory structure:
    hierarchy --zip /path/to/directory

  Generate a zip file without displaying the structure:
    hierarchy --zip --no-display /path/to/directory

  Display the version of the tool:
    hierarchy --version
"""

from docopt import docopt
import toml
import os
from hierarchy.app import app

def get_version():
    pyproject_path = os.path.join(os.path.dirname(__file__), '..', '..', 'pyproject.toml')
    pyproject = toml.load(pyproject_path)
    return pyproject['tool']['poetry']['version']

if __name__ == "__main__":
    args = docopt(__doc__, version=get_version())
    app(args)
