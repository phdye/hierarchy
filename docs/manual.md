
% hierarchy(1) Version 0.1.0 | hierarchy User Manual

# NAME
hierarchy - Generate and display the directory structure of a given directory

# SYNOPSIS
`hierarchy` [options] <directory>

# DESCRIPTION
The `hierarchy` command-line tool scans the specified `<directory>` and displays its structure in a tree-like format. It respects `.gitignore` rules and handles symbolic links appropriately. The tool can also generate a zip file containing the directory structure if the `--zip` option is specified. When the `--no-display` option is used, the tool will suppress the display of the directory structure, which is particularly useful when only a zip file is needed.

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
  hierarchy .
  ```

- Display the structure of a specific directory:
  ```bash
  hierarchy /path/to/directory
  ```

- Generate a zip file of the directory structure:
  ```bash
  hierarchy --zip /path/to/directory
  ```

- Generate a zip file without displaying the structure:
  ```bash
  hierarchy --zip --no-display /path/to/directory
  ```

- Display the version of the tool:
  ```bash
  hierarchy --version
  ```

# SEE ALSO
- [README.md](../README.md)
- [API Documentation](api.md)
- [High-Level Design](High-Level-Design.md)
- [Detailed Design](Detailed-Design.md)

# AUTHOR
Philip Dye <phdye@acm.org>
