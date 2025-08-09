# 代码生成时间: 2025-08-09 14:51:27
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import shutil

"""
Database Migration Tool GUI
A simple tkinter-based application to perform database migrations.
"""

class DatabaseMigrationTool:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title('Database Migration Tool')
        self.root.geometry('400x200')

        # Create input fields for source and destination paths
        self.source_label = tk.Label(self.root, text='Source Path:')
        self.source_label.pack()
        self.source_entry = tk.Entry(self.root)
        self.source_entry.pack()

        self.destination_label = tk.Label(self.root, text='Destination Path:')
        self.destination_label.pack()
        self.destination_entry = tk.Entry(self.root)
        self.destination_entry.pack()

        # Create a button to start the migration process
        self.migrate_button = tk.Button(self.root, text='Migrate', command=self.migrate)
        self.migrate_button.pack()

    def migrate(self):
        # Get the source and destination paths from the input fields
        source_path = self.source_entry.get()
        destination_path = self.destination_entry.get()

        # Check if both paths are provided
        if not source_path or not destination_path:
            messagebox.showerror('Error', 'Please provide both source and destination paths.')
            return

        try:
            # Perform the migration by copying files
            shutil.copytree(source_path, destination_path)
            messagebox.showinfo('Success', 'Migration completed successfully.')
        except Exception as e:
            # Handle any errors that occur during the migration
            messagebox.showerror('Error', f'An error occurred: {str(e)}')

# Create the main window and pass it to the DatabaseMigrationTool class
if __name__ == '__main__':
    root = tk.Tk()
    app = DatabaseMigrationTool(root)
    root.mainloop()