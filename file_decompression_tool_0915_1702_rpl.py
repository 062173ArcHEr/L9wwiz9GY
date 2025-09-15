# 代码生成时间: 2025-09-15 17:02:23
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import tarfile
import os

class FileDecompressionTool:
    def __init__(self, master):
        """Initialize the application with a main window."""
        self.master = master
        self.master.title("File Decompression Tool")

        # Set up the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Set up the main frame
        frame = tk.Frame(self.master)
        frame.pack(padx=10, pady=10)

        # Add a button to select the compressed file
        self.select_button = tk.Button(frame, text="Select Compressed File", command=self.select_compressed_file)
        self.select_button.pack(side=tk.LEFT, padx=10)

        # Add a button to extract the file
        self.extract_button = tk.Button(frame, text="Extract File", command=self.extract_file, state=tk.DISABLED)
        self.extract_button.pack(side=tk.LEFT, padx=10)

        # Add a label to show the status of the process
        self.status_label = tk.Label(frame, text="No file selected")
        self.status_label.pack(side=tk.LEFT, padx=10)

    def select_compressed_file(self):
        """Open a file dialog to select a compressed file."""
        self.file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip"), ("Tar files", "*.tar.gz")])
        if self.file_path:
            self.status_label.config(text=os.path.basename(self.file_path))
            self.extract_button.config(state=tk.NORMAL)

    def extract_file(self):
        """Extract the selected compressed file."""
        try:
            # Check if the file is a zip or tar file and extract accordingly
            if self.file_path.endswith('.zip'):
                self.extract_zip()
            elif self.file_path.endswith('.tar.gz'):
                self.extract_tar()
            else:
                raise ValueError("Unsupported file format")

            # Update the status label to indicate success
            self.status_label.config(text="File extracted successfully")
            messagebox.showinfo("Success", "File extracted successfully")
        except Exception as e:
            # Handle any errors that occur during extraction
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="Error: " + str(e))

    def extract_zip(self):
        """Extract a zip file."""
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(self.file_path))

    def extract_tar(self):
        """Extract a tar file."""
        with tarfile.open(self.file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(self.file_path))

# Create the main window and run the application
root = tk.Tk()
app = FileDecompressionTool(root)
root.mainloop()