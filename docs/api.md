
# API Documentation

## Introduction
The `hierarchy` project provides an API for generating and displaying the directory structure of a given directory. The API respects `.gitignore` rules and can optionally generate a zip file of the directory structure.

## Modules and Classes

### TreeNode Class

**Purpose**: Represents a node in the directory tree.

**Attributes**:
- `name`: The name of the file or directory.
- `is_directory`: Boolean indicating if the node is a directory.
- `children`: List of child `TreeNode` instances.

**Methods**:
- `add_child(node)`: Adds a child node to the current node.
- `__repr__()`: Provides a string representation of the node.

### GitignoreHandler Class

**Purpose**: Manages `.gitignore` patterns and checks if files or directories should be ignored.

**Attributes**:
- `specs`: List of ignore patterns.

**Methods**:
- `_load_gitignore_files(paths)`: Loads ignore patterns from specified paths.
- `is_ignored(filepath)`: Checks if a file or directory should be ignored based on the patterns.

### DirectoryTree Class

**Purpose**: Builds and manages the directory tree structure.

**Attributes**:
- `root_dir`: The root directory to start building the tree from.
- `gitignore_handler`: An optional handler to check if files or directories are ignored.

**Methods**:
- `build_tree(root_dir=None)`: Recursively builds the directory tree as a `TreeNode` structure.
- `create_zip(output_zip)`: Creates a zip file containing the directory structure.

## Functions

### TreeNode Class

#### `add_child(node)`
**Parameters**:
- `node`: The child `TreeNode` to add.

**Returns**:
- None

#### `__repr__()`
**Parameters**:
- None

**Returns**:
- `str`: String representation of the node.

### GitignoreHandler Class

#### `_load_gitignore_files(paths)`
**Parameters**:
- `paths`: List of paths to `.gitignore` files.

**Returns**:
- None

#### `is_ignored(filepath)`
**Parameters**:
- `filepath`: The file or directory path to check.

**Returns**:
- `bool`: True if the file or directory should be ignored, False otherwise.

### DirectoryTree Class

#### `build_tree(root_dir=None)`
**Parameters**:
- `root_dir`: The root directory to start building the tree from.

**Returns**:
- `TreeNode`: The root node of the directory tree.

#### `create_zip(output_zip)`
**Parameters**:
- `output_zip`: The path to the output zip file.

**Returns**:
- None

## Usage Examples

### TreeNode Class

```python
node = TreeNode(name="root", is_directory=True)
child_node = TreeNode(name="child", is_directory=False)
node.add_child(child_node)
print(node)
```

### GitignoreHandler Class

```python
gitignore_handler = GitignoreHandler(["/path/to/.gitignore"])
print(gitignore_handler.is_ignored("/path/to/ignored_file"))
```

### DirectoryTree Class

```python
gitignore_handler = GitignoreHandler(["/path/to/.gitignore"])
directory_tree = DirectoryTree(root_dir="/path/to/directory", gitignore_handler=gitignore_handler)
tree = directory_tree.build_tree()
directory_tree.create_zip("/path/to/output.zip")
```

## Example Directory

An example directory named `example` has been created to demonstrate the usage of the API. It contains a fake test hierarchy to showcase how the API works.
