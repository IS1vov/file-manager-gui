import os
import tempfile
import pytest
from unittest import mock
from file_manager.gui import FileManagerApp
import tkinter as tk


@pytest.fixture
def app():
    root = tk.Tk()
    app = FileManagerApp(root)
    yield app
    root.destroy()


def test_delete_selected_confirm_yes(app, monkeypatch):
    # Создаем временный файл
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test")
        tmp_path = tmp.name

    app.path_var.set(os.path.dirname(tmp_path))
    app.refresh_list()

    # Выбираем файл в listbox
    idx = app.listbox.get(0, tk.END).index(os.path.basename(tmp_path))
    app.listbox.selection_set(idx)

    # Мокаем подтверждение (да)
    monkeypatch.setattr("tkinter.messagebox.askyesno", lambda *args, **kwargs: True)

    app.delete_selected()

    assert not os.path.exists(tmp_path)


def test_delete_selected_confirm_no(app, monkeypatch):
    # Создаем временный файл
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"test")
        tmp_path = tmp.name

    app.path_var.set(os.path.dirname(tmp_path))
    app.refresh_list()

    idx = app.listbox.get(0, tk.END).index(os.path.basename(tmp_path))
    app.listbox.selection_set(idx)

    # Мокаем подтверждение (нет)
    monkeypatch.setattr("tkinter.messagebox.askyesno", lambda *args, **kwargs: False)

    app.delete_selected()

    assert os.path.exists(tmp_path)
    os.remove(tmp_path)
