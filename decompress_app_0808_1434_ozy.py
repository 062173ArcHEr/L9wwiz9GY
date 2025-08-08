# 代码生成时间: 2025-08-08 14:34:05
import os
import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
A simple GUI application for decompressing files using tkinter and zipfile.
"""
# 添加错误处理

class DecompressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Decompress App")
        self.root.geometry("400x200")
        
        # Button to select the file
        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=20)
        
        # Button to decompress the file
        self.decompress_button = tk.Button(self.root, text="Decompress", command=self.decompress_file)
# FIXME: 处理边界情况
        self.decompress_button.pack(pady=20)
        
        # Label to display file path
        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack(pady=10)
# 改进用户体验
        
        self.file_path = ""
        
    def select_file(self):
        """
# 扩展功能模块
        Open a file dialog to select the zip file.
        """
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Zip files", "*.zip"), ("All files", "*.*")]
        )
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))
        else:
            self.file_label.config(text="No file selected")
        
    def decompress_file(self):
# 改进用户体验
        """
        Decompress the selected file to the same directory.
        """
        if not self.file_path:
            messagebox.showwarning("Warning", "Please select a file first.")
            return
        
        try:
            # Extract all the contents of zip file in {'write', 'read', 'a'} mode and specify the permissions.
            with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
# 扩展功能模块
                zip_ref.extractall(os.path.dirname(self.file_path))
                messagebox.showinfo("Success", "File decompressed successfully.")
        except zipfile.BadZipFile:
            messagebox.showerror("Error", "The selected file is not a valid zip file.")
        except Exception as e:
# FIXME: 处理边界情况
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DecompressApp(root)
    root.mainloop()