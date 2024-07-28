
% pdirtree(1) Version 0.1.0 | pdirtree User Manual

# NAME
pdirtree - Generate and display the directory structure of a given directory

# SYNOPSIS
`pdirtree` [options] <directory>

# DESCRIPTION
The `pdirtree` command-line tool scans the specified `<directory>` and displays its structure in a tree-like format. It respects `.gitignore` rules and handles symbolic links appropriately. The tool can also generate a zip file containing the directory structure if the `--zip` option is specified. When the `--no-display` option is used, the tool will suppress the display of the directory structure, which is particularly useful when only a zip file is needed.

# OPTIONS
- `-h`, `--help`:
  Show this help message and exit.
- `--version`:
  Show version information and exit.
- `--zip`:
  Generate a zip file of the directory structure.
- `--no-display`:
  Do not display the directory structure. This option can be used independently or in conjunction with `--zip`.

# EXAMPLES
- Display the structure of the current directory:
  ```bash
  pdirtree .
  ```

- Display the structure of a specific directory:
  ```bash
  pdirtree /path/to/directory
  ```

- Generate a zip file of the directory structure:
  ```bash
  pdirtree --zip /path/to/directory
  ```

- Generate a zip file without displaying the structure:
  ```bash
  pdirtree --zip --no-display /path/to/directory
  ```

- Display the version of the tool:
  ```bash
  pdirtree --version
  ```

# SEE ALSO
- [README.md](../README.md)
- [API Documentation](api.md)
- [High-Level Design](High-Level-Design.md)
- [Detailed Design](Detailed-Design.md)

# AUTHOR
Philip Dye <phdye@acm.org>
