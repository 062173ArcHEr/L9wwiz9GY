# 代码生成时间: 2025-07-31 19:16:36
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class FolderOrganizer:
    """
    A class to organize files and folders based on a specified format.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Organizer")
        self.current_dir = ''

        # Set up the interface
        self.setup_interface()

    def setup_interface(self):
        # Directory path label
        self.dir_label = tk.Label(self.root, text="Current Directory: ")
        self.dir_label.pack()

        # Directory path entry
        self.dir_entry = tk.Entry(self.root, width=50)
        self.dir_entry.pack()

        # Browse button
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        # Organize button
        self.organize_button = tk.Button(self.root, text="Organize", command=self.organize_folder)
        self.organize_button.pack()

    def browse_directory(self):
        # Open file dialog to select directory
        self.current_dir = filedialog.askdirectory()
        if self.current_dir:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, self.current_dir)

    def organize_folder(self):
        if not self.current_dir:
            messagebox.showerror("Error", "Please select a directory first")
            return

        try:
            # Organize files and folders in the current directory
            self.organize_files()
            messagebox.showinfo("Success", "Folder organized successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def organize_files(self):
        # List all files and folders in the current directory
        for item in os.listdir(self.current_dir):
            item_path = os.path.join(self.current_dir, item)
            if os.path.isfile(item_path):
                # Move files to a 'files' folder if not already there
                self.move_file(item_path)
            elif os.path.isdir(item_path):
                # Organize sub-folders
                self.organize_folder(item_path)

    def move_file(self, file_path):
        # Define the destination folder
        dest_folder = os.path.join(self.current_dir, 'files')
        # Create the 'files' folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        # Move the file to the 'files' folder
        dest_path = os.path.join(dest_folder, os.path.basename(file_path))
        os.rename(file_path, dest_path)

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    app = FolderOrganizer(root)
    root.mainloop()