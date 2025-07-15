import os
import shutil
import tempfile
import unittest
from file_manager import core


class TestCoreFunctions(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file1 = os.path.join(self.test_dir, "file1.txt")
        with open(self.file1, "w") as f:
            f.write("test")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_copy_file(self):
        dest = os.path.join(self.test_dir, "copied.txt")
        core.copy_file(self.file1, dest)
        self.assertTrue(os.path.exists(dest))

    def test_move_file(self):
        dest = os.path.join(self.test_dir, "moved.txt")
        core.move_file(self.file1, dest)
        self.assertTrue(os.path.exists(dest))
        self.assertFalse(os.path.exists(self.file1))

    def test_delete_file(self):
        core.delete_file(self.file1)
        self.assertFalse(os.path.exists(self.file1))

    def test_list_files(self):
        files = core.list_files(self.test_dir)
        self.assertIn("file1.txt", files)


if __name__ == "__main__":
    unittest.main()
