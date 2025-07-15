import os
import tempfile
import unittest
import tkinter as tk
from file_manager.gui import FileManagerApp
from unittest import mock


class TestGUIFileManager(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = FileManagerApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_delete_confirm_yes(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"test")
            tmp_path = tmp.name

        self.app.path_var.set(os.path.dirname(tmp_path))
        self.app.refresh_list()
        idx = self.app.listbox.get(0, tk.END).index(os.path.basename(tmp_path))
        self.app.listbox.selection_set(idx)

        with mock.patch("tkinter.messagebox.askyesno", return_value=True):
            self.app.delete_selected()

        self.assertFalse(os.path.exists(tmp_path))

    def test_delete_confirm_no(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(b"test")
            tmp_path = tmp.name

        self.app.path_var.set(os.path.dirname(tmp_path))
        self.app.refresh_list()
        idx = self.app.listbox.get(0, tk.END).index(os.path.basename(tmp_path))
        self.app.listbox.selection_set(idx)

        with mock.patch("tkinter.messagebox.askyesno", return_value=False):
            self.app.delete_selected()

        self.assertTrue(os.path.exists(tmp_path))
        os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
