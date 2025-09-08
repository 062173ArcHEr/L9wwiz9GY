# 代码生成时间: 2025-09-08 20:09:18
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

"""
Image Resizer GUI application using Python and Tkinter.
This program allows users to batch resize images.
"""

class ImageResizer:
    def __init__(self, root):
# TODO: 优化性能
        """Initialize the GUI components."""
        self.root = root
        self.root.title('Image Resizer GUI')

        # Create the main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Input path label and entry
        tk.Label(self.frame, text='Source directory:').grid(row=0, column=0)
        self.source_entry = tk.Entry(self.frame, width=50)
        self.source_entry.grid(row=0, column=1)
        tk.Button(self.frame, text='Browse', command=self.browse_source).grid(row=0, column=2)

        # Output path label and entry
        tk.Label(self.frame, text='Destination directory:').grid(row=1, column=0)
        self.destination_entry = tk.Entry(self.frame, width=50)
        self.destination_entry.grid(row=1, column=1)
        tk.Button(self.frame, text='Browse', command=self.browse_destination).grid(row=1, column=2)

        # Resize dimensions label and entry
        tk.Label(self.frame, text='New size (width x height):').grid(row=2, column=0)
        self.size_entry = tk.Entry(self.frame, width=20)
        self.size_entry.grid(row=2, column=1)
# 改进用户体验

        # Start button
        tk.Button(self.frame, text='Resize', command=self.resize_images).grid(row=3, columnspan=3)

    def browse_source(self):
        """Open a file dialog to select the source directory."""
        path = filedialog.askdirectory()
        if path:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, path)

    def browse_destination(self):
        """Open a file dialog to select the destination directory."""
        path = filedialog.askdirectory()
        if path:
# NOTE: 重要实现细节
            self.destination_entry.delete(0, tk.END)
            self.destination_entry.insert(0, path)
# NOTE: 重要实现细节

    def resize_images(self):
# 添加错误处理
        """Resize images in the source directory and save them to the destination directory."""
        source_dir = self.source_entry.get()
        destination_dir = self.destination_entry.get()
# FIXME: 处理边界情况
        new_size = self.size_entry.get().split(' x ')

        if not source_dir or not destination_dir or len(new_size) != 2:
            messagebox.showerror('Error', 'Please fill in all fields correctly.')
            return

        try:
# 扩展功能模块
            width, height = map(int, new_size)
        except ValueError:
            messagebox.showerror('Error', 'Invalid size format. Use width x height.')
            return

        for filename in os.listdir(source_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                try:
                    img_path = os.path.join(source_dir, filename)
# 增强安全性
                    img = Image.open(img_path)
                    img = img.resize((width, height))
                    save_path = os.path.join(destination_dir, filename)
                    img.save(save_path)
                except IOError:
                    messagebox.showerror('Error', f'Failed to resize {filename}.')
        messagebox.showinfo('Success', 'Images have been resized successfully.')

def main():
    """Main function to run the application."""
# 增强安全性
    root = tk.Tk()
    app = ImageResizer(root)
    root.mainloop()

if __name__ == '__main__':
# TODO: 优化性能
    main()