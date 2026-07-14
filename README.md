# Download File Sorter

A lightweight Python command-line tool that organizes a folder into useful categories while preserving duplicate files.

## Tech stack

- Python 3.10+
- `pathlib` for portable paths
- `argparse` for the command-line interface
- `shutil` for file moves

## Features

- Sorts images, documents, video, audio, archives, code, and other files.
- Defaults to the current user's Downloads folder.
- Accepts any source folder as an argument.
- Provides a dry-run preview before files are moved.
- Renames collisions instead of overwriting existing files.
- Leaves existing directories untouched.

## Usage

Preview the default Downloads folder:

```bash
python documentSorter.py --dry-run
```

Sort a chosen folder:

```bash
python documentSorter.py "C:\path\to\folder"
```

No third-party dependencies are required.

## Status

Functional command-line utility. Start with `--dry-run` whenever testing new rules or a new folder.

## Next steps

- Add automated tests around category selection and collision handling.
- Allow rules to be loaded from a configuration file.
- Add an optional undo log.

Built by [SimpleCaci](https://github.com/SimpleCaci).
