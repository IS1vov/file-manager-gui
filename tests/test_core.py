import os
import shutil
import pytest
from file_manager import core
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def temp_dir(tmp_path):
    f1 = tmp_path / "test.txt"
    f1.write_text("hello")
    return tmp_path


def test_list_files(temp_dir):
    files = core.list_files(temp_dir)
    assert "test.txt" in files


def test_copy_file(temp_dir):
    src = temp_dir / "test.txt"
    dst = temp_dir / "copied.txt"
    core.copy_file(src, dst)
    assert dst.exists()


def test_move_file(temp_dir):
    src = temp_dir / "test.txt"
    dst = temp_dir / "moved.txt"
    core.move_file(src, dst)
    assert dst.exists()
    assert not src.exists()


def test_delete_file(temp_dir):
    file = temp_dir / "test.txt"
    core.delete_file(file)
    assert not file.exists()
