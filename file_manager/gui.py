import tkinter as tk
from tkinter import filedialog, messagebox
import os
from file_manager.core import copy_file, move_file, delete_file, list_files


class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager GUI")

        self.path_var = tk.StringVar()
        self.path_var.set(os.getcwd())

        tk.Entry(root, textvariable=self.path_var, width=50).pack()
        tk.Button(root, text="Browse", command=self.browse_folder).pack()

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack()

        self.refresh_list()

        tk.Button(root, text="Delete", command=self.delete_selected).pack()
        tk.Button(root, text="Copy", command=self.copy_selected).pack()
        tk.Button(root, text="Move", command=self.move_selected).pack()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        path = self.path_var.get()
        try:
            for f in list_files(path):
                self.listbox.insert(tk.END, f)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)
            self.refresh_list()

    def get_selected_file(self):
        selected = self.listbox.curselection()
        if selected:
            return os.path.join(self.path_var.get(), self.listbox.get(selected[0]))
        return None

    def delete_selected(self):
        file_path = self.get_selected_file()
        if file_path:
            delete_file(file_path)
            self.refresh_list()

    def copy_selected(self):
        file_path = self.get_selected_file()
        dst = filedialog.askdirectory()
        if file_path and dst:
            copy_file(file_path, dst)
            self.refresh_list()

    def move_selected(self):
        file_path = self.get_selected_file()
        dst = filedialog.askdirectory()
        if file_path and dst:
            move_file(file_path, dst)
            self.refresh_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
