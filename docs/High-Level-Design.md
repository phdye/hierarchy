### High-Level Design Document

#### Project Name: pdirtree

#### Author: Philip Dye

#### Contact: phdye@acm.org

---

### 1. Overview

The `pdirtree` project is a command-line tool designed to generate and display the directory structure of a given directory. It supports ignoring files and directories based on `.gitignore` rules and can optionally generate a zip file of the directory structure.

### 2. Objectives

- **Display Directory Structure**: Recursively display the directory structure starting from a given directory.
- **Respect .gitignore Rules**: Ignore files and directories based on `.gitignore` patterns.
- **Handle Symlinks**: Properly handle symbolic links to avoid following them.
- **Generate Zip File**: Optionally generate a zip file of the directory structure.
- **Modular Design**: Separate the core functionality from the display logic and ensure the core can be used programmatically.

### 3. Components

1. **TreeNode Class**
   - Represents a node in the directory tree.
   - Attributes: `name`, `is_directory`, `children`.
   - Methods: `add_child(node)`, `__repr__()`.

2. **GitignoreHandler Class**
   - Manages .gitignore patterns and checks if files or directories should be ignored.
   - Attributes: `specs`.
   - Methods: `_load_gitignore_files(paths)`, `is_ignored(filepath)`.

3. **DirectoryTree Class**
   - Builds and manages the directory tree structure.
   - Attributes: `root_dir`, `gitignore_handler`.
   - Methods: `build_tree(root_dir=None)`, `create_zip(output_zip)`.

4. **Display Logic**
   - Function: `display_tree(node, prefix='')`.
   - Recursively displays the directory tree structure starting from a given `TreeNode`.

5. **Command-Line Interface (CLI)**
   - Command: `pdirtree`.
   - Uses `docopt` for argument parsing.
   - Options: `-h --help`, `--version`, `--zip`.

### 4. Workflow

1. **Initialize**: 
   - Parse command-line arguments.
   - Initialize `GitignoreHandler` with paths to `.gitignore` files.
   - Initialize `DirectoryTree` with the root directory and `GitignoreHandler`.

2. **Build Tree**:
   - Call `DirectoryTree.build_tree()` to construct the tree structure using `TreeNode` objects.

3. **Generate Zip (Optional)**:
   - If the `--zip` option is specified, call `DirectoryTree.create_zip(output_zip)` to generate a zip file of the directory structure.

4. **Display Tree**:
   - Call `display_tree(tree_structure)` to display the directory tree structure.

### 5. Detailed Descriptions

#### 5.1 TreeNode Class
- **Purpose**: Represents a node in the directory tree.
- **Attributes**:
  - `name`: The name of the file or directory.
  - `is_directory`: Boolean indicating if the node is a directory.
  - `children`: List of child `TreeNode` objects.
- **Methods**:
  - `add_child(node)`: Adds a child node to the current node.
  - `__repr__()`: Provides a string representation of the node for debugging.

#### 5.2 GitignoreHandler Class
- **Purpose**: Manages .gitignore patterns and checks if files or directories should be ignored.
- **Attributes**:
  - `specs`: List of tuples containing `PathSpec` objects and their base directories.
- **Methods**:
  - `_load_gitignore_files(paths)`: Loads .gitignore files and creates `PathSpec` objects.
  - `is_ignored(filepath)`: Checks if a given file or directory should be ignored based on the .gitignore patterns.

#### 5.3 DirectoryTree Class
- **Purpose**: Builds and manages the directory tree structure.
- **Attributes**:
  - `root_dir`: The root directory to start building the tree from.
  - `gitignore_handler`: An optional handler to check if files or directories are ignored.
- **Methods**:
  - `build_tree(root_dir=None)`: Recursively builds the directory tree as a `TreeNode` structure.
  - `create_zip(output_zip)`: Creates a zip file containing the directory structure.

#### 5.4 Display Logic
- **Function**: `display_tree(node, prefix='')`
- **Purpose**: Recursively displays the directory tree structure starting from a given `TreeNode`.
- **Parameters**:
  - `node`: The current `TreeNode` to display.
  - `prefix`: The prefix to use for the current level of the tree structure.

#### 5.5 Command-Line Interface (CLI)
- **Command**: `pdirtree`
- **Purpose**: Parses command-line arguments and invokes the core functionality.
- **Options**:
  - `-h --help`: Shows the help message.
  - `--version`: Shows the version.
  - `--zip`: Generates a zip file of the directory structure.

### 6. Future Enhancements

- **Enhanced .gitignore Handling**: Support for multiple .gitignore files in different directories.
- **Configuration File**: Allow users to specify custom patterns and rules in a configuration file.
- **Parallel Processing**: Optimize directory traversal using parallel processing for large directories.

### 7. Conclusion

The `pdirtree` project provides a flexible and efficient way to display and manage directory structures while respecting .gitignore rules. By separating core functionality from display logic and using a tree data structure, the project ensures modularity and ease of maintenance. Future enhancements can further improve its functionality and performance.

---

This high-level design document provides an overview of the `pdirtree` project, outlining its objectives, components, workflow, and future enhancements. Please review the document and let me know if there are any adjustments or additional details needed.