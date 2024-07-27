### High Level Design Document for Hierarchy

---

#### Project Name: Hierarchy

#### Version: 1.0.0

---

## Table of Contents

1. **Introduction**
2. **Objectives**
3. **System Overview**
4. **Architecture**
5. **Components**
   - 5.1 Main Component
   - 5.2 DirectoryTree Component
   - 5.3 GitignoreHandler Component
   - 5.4 Tests
6. **Data Flow**
7. **Installation and Usage**
8. **Dependencies**
9. **Assumptions and Constraints**

---

### 1. Introduction

The Hierarchy project is a Python-based tool designed to print the directory hierarchy of a given path and create a zip file of the directory contents while respecting `.gitignore` rules. This document outlines the high-level design of the project, detailing the architecture, components, data flow, and usage.

### 2. Objectives

- Provide a CLI tool to display the directory structure.
- Create a zip file of the directory contents.
- Respect `.gitignore` rules to exclude specified files and directories.
- Ensure the tool is modular, testable, and follows SOLID principles.

### 3. System Overview

Hierarchy is a command-line tool that scans a specified directory, constructs a tree representation of its structure, and creates a zip archive of its contents. It uses `.gitignore` files to determine which files and directories should be excluded from the archive.

### 4. Architecture

The system is designed using a modular architecture, with each component responsible for a specific functionality. The main components are:
- **Main Component**: Handles command-line arguments and orchestrates the process.
- **DirectoryTree Component**: Builds the directory tree and creates the zip archive.
- **GitignoreHandler Component**: Parses `.gitignore` files and determines which files to exclude.

### 5. Components

#### 5.1 Main Component

**Responsibilities**:
- Parse command-line arguments.
- Initialize the `GitignoreHandler` and `DirectoryTree` components.
- Orchestrate the process of building the directory tree and creating the zip file.

**File**: `hierarchy/main.py`

#### 5.2 DirectoryTree Component

**Responsibilities**:
- Traverse the directory structure.
- Build a tree representation of the directory.
- Create a zip archive of the directory contents, excluding ignored files.

**File**: `hierarchy/directory_tree.py`

**Class**: `DirectoryTree`

#### 5.3 GitignoreHandler Component

**Responsibilities**:
- Parse `.gitignore` files.
- Determine whether a file or directory should be excluded based on `.gitignore` rules.

**File**: `hierarchy/gitignore_handler.py`

**Class**: `GitignoreHandler`

#### 5.4 Tests

**Responsibilities**:
- Provide unit tests for the `GitignoreHandler` and `DirectoryTree` components.
- Ensure the system behaves as expected.

**Files**:
- `tests/test_gitignore_handler.py`
- `tests/test_directory_tree.py`
- `tests/test_main.py`

### 6. Data Flow

1. **Initialization**:
   - The main script (`main.py`) is executed.
   - Command-line arguments are parsed to determine the target directory.
   - `GitignoreHandler` is initialized with paths to `.gitignore` files.

2. **Directory Traversal**:
   - `DirectoryTree` traverses the directory structure.
   - For each file and directory, `GitignoreHandler` checks if it should be excluded.

3. **Tree Building**:
   - `DirectoryTree` builds a tree representation of the directory structure.

4. **Zip Creation**:
   - `DirectoryTree` creates a zip archive of the directory contents, excluding ignored files.

5. **Output**:
   - The tree structure is printed to the console.
   - The zip file is saved to the specified output path.

### 7. Installation and Usage

**Installation**:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.

**Usage**:
```sh
python -m hierarchy.main [DIRECTORY]
```
- `DIRECTORY`: The target directory to list and zip (default: current directory).

### 8. Dependencies

- `gitignore-parser`: Used to parse `.gitignore` files.
- `argparse`: Used for command-line argument parsing.
- `zipfile`: Used for creating zip archives.

### 9. Assumptions and Constraints

- The tool assumes that `.gitignore` files are present and correctly formatted.
- The tool is designed to run on systems where Python 3.6 or higher is installed.
- The tool respects the `.gitignore` rules and excludes specified files and directories from the output.

---

This high-level design document provides an overview of the Hierarchy project, detailing its components, architecture, and data flow. This should serve as a guide for understanding the system's design and functionality.