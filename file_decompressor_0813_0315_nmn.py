# 代码生成时间: 2025-08-13 03:15:35
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os

class FileDecompressor:
    """压缩文件解压工具，使用TKINTER框架实现图形界面。"""

    def __init__(self, root):
        self.root = root
        self.root.title('文件解压工具')
        self.root.geometry('300x150')

        # 选择文件按钮
        self.choose_button = tk.Button(self.root, text='选择压缩文件', command=self.choose_file)
        self.choose_button.pack(pady=10)

        # 解压按钮
        self.extract_button = tk.Button(self.root, text='解压文件', command=self.extract_file, state='disabled')
        self.extract_button.pack(pady=10)

        self.filename = ''

    def choose_file(self):
        """选择文件并更新界面状态。"""
        self.filename = filedialog.askopenfilename(filetypes=[('Zip files', '*.zip')])
        if self.filename:
            self.extract_button['state'] = 'normal'
        else:
            self.extract_button['state'] = 'disabled'

    def extract_file(self):
        """解压文件到指定目录。"""
        if not self.filename:
            messagebox.showerror('错误', '请先选择一个压缩文件！')
            return

        try:
            # 解压文件
            with zipfile.ZipFile(self.filename, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(self.filename))
            messagebox.showinfo('成功', '文件解压成功！')
        except zipfile.BadZipFile:
            messagebox.showerror('错误', '压缩文件损坏！')
        except Exception as e:
            messagebox.showerror('错误', f'解压失败：{e}')

if __name__ == '__main__':
    root = tk.Tk()
    app = FileDecompressor(root)
    root.mainloop()