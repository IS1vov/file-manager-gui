import os
import shutil


def list_files(path):
    return os.listdir(path)


def copy_file(src, dst):
    shutil.copy2(src, dst)


def move_file(src, dst):
    shutil.move(src, dst)


def delete_file(path):
    os.remove(path)
