"""Sort files into category folders without touching existing directories."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

RULES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".webp"},
    "Videos": {".mp4", ".mov"},
    "Audio": {".mp3", ".wav"},
    "Documents": {".pdf", ".docx", ".txt", ".csv", ".rtf"},
    "Software": {".exe", ".msi"},
    "Archives": {".zip", ".rar", ".tar", ".gz", ".7z"},
    "Web Files": {".html", ".mhtml"},
    "Calendar": {".ics"},
    "Code": {".cpp", ".json", ".sav", ".tns", ".py"},
    "Temp": {".crdownload", ".part"},
}


def find_folder(file: Path) -> str:
    extension = file.suffix.lower()
    return next((folder for folder, extensions in RULES.items() if extension in extensions), "Misc")


def available_target(destination: Path, filename: str) -> Path:
    target = destination / filename
    counter = 1
    while target.exists():
        source = Path(filename)
        target = destination / f"{source.stem}_{counter}{source.suffix}"
        counter += 1
    return target


def sort_files(source: Path, *, dry_run: bool = False) -> tuple[int, int]:
    moved = failed = 0
    for item in source.iterdir():
        if not item.is_file():
            continue
        folder = source / find_folder(item)
        target = available_target(folder, item.name)
        print(f"{'Would move' if dry_run else 'Moving'} {item.name} -> {folder.name}/{target.name}")
        if dry_run:
            moved += 1
            continue
        try:
            folder.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
            moved += 1
        except OSError as error:
            failed += 1
            print(f"Could not move {item.name}: {error}")
    return moved, failed


def main() -> int:
    parser = argparse.ArgumentParser(description="Organize files into folders by extension.")
    parser.add_argument("folder", nargs="?", type=Path, default=Path.home() / "Downloads")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without changing files.")
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error(f"folder does not exist: {args.folder}")
    moved, failed = sort_files(args.folder.resolve(), dry_run=args.dry_run)
    print(f"{'Planned' if args.dry_run else 'Completed'}: {moved} file(s), {failed} failure(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
