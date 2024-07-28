
# pdirtree

## Introduction
The `pdirtree` project is a command-line tool designed to generate and display the directory structure of a given directory. It supports ignoring files and directories based on `.gitignore` rules and can optionally generate a zip file of the directory structure.

## Features
- Display directory structure in a tree-like format.
- Respect `.gitignore` rules.
- Handle symbolic links appropriately.
- Generate a zip file of the directory structure.
- Modular design for easy integration into other projects.

## Installation

### Prerequisites
- Python 3.8 or higher
- Poetry

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/phdye/pdirtree.git
   cd pdirtree
   ```
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

### Command-Line Interface

Display the structure of the current directory:
```bash
pdirtree .
```

Display the structure of a specific directory:
```bash
pdirtree /path/to/directory
```

Generate a zip file of the directory structure:
```bash
pdirtree --zip /path/to/directory
```

Generate a zip file without displaying the structure:
```bash
pdirtree --zip --no-display /path/to/directory
```

Display the version of the tool:
```bash
pdirtree --version
```

### API

#### Example

```python
from pdirtree.directory_tree import DirectoryTree
from pdirtree.gitignore_handler import GitignoreHandler

gitignore_handler = GitignoreHandler(["/path/to/.gitignore"])
directory_tree = DirectoryTree(root_dir="/path/to/directory", gitignore_handler=gitignore_handler)
tree = directory_tree.build_tree()
directory_tree.create_zip("/path/to/output.zip")
```

## Documentation Links
- [Manual Page](docs/manual.md)
- [API Documentation](docs/api.md)
- [High-Level Design](docs/High-Level-Design.md)
- [Detailed Design](docs/Detailed-Design.md)

## Examples
Display the structure of the current directory:
```bash
pdirtree .
```

Generate a zip file of the directory structure:
```bash
pdirtree --zip /path/to/directory
```

## Contributing
Contributions are welcome! Please follow the guidelines below:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
