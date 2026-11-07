# Download File Sorter

A Python command-line tool that sorts files into category folders. Duplicate names get numbered instead of overwritten; existing directories are left alone.

## Run

Use Python 3.10+ from the repository root. No third-party packages are needed.

Preview the current user's Downloads folder:

```bash
python documentSorter.py --dry-run
```

Preview a chosen folder, then remove `--dry-run` when the planned moves look right:

```bash
python documentSorter.py "C:\path\to\folder" --dry-run
```

Rules in `documentSorter.py` cover images, video, audio, documents, installers, archives, web files, calendars, code, and incomplete downloads. Unknown extensions go to `Misc`.

## Check changes

```bash
python -m unittest -v
```

The existing tests cover case-insensitive categories, collision naming, and dry-run preservation using temporary folders. GitHub Actions runs the same suite.

Useful next steps: test actual moves and repeated collisions, load custom rules from a file, and add an undo log.

Built by [SimpleCaci](https://github.com/SimpleCaci).
