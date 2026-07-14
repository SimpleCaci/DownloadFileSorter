import tempfile
import unittest
from pathlib import Path

from documentSorter import available_target, find_folder, sort_files


class FileSorterTests(unittest.TestCase):
    def test_categories_are_case_insensitive(self):
        self.assertEqual(find_folder(Path('photo.JPG')), 'Images')
        self.assertEqual(find_folder(Path('unknown.xyz')), 'Misc')

    def test_collision_target_preserves_extension(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'report.txt').touch()
            self.assertEqual(available_target(root, 'report.txt').name, 'report_1.txt')

    def test_dry_run_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'photo.png'
            source.touch()
            moved, failed = sort_files(root, dry_run=True)
            self.assertEqual((moved, failed), (1, 0))
            self.assertTrue(source.exists())
            self.assertFalse((root / 'Images').exists())


if __name__ == '__main__':
    unittest.main()
