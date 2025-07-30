# 代码生成时间: 2025-07-31 04:02:21
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

"""
批量文件重命名工具
使用TKINTER框架创建的图形用户界面，允许用户选择文件夹，并对该文件夹下的文件进行批量重命名。
"""

class BatchRenameTool:
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title('批量文件重命名工具')
        self.root.geometry('600x400')

        self.folder_path = ''
        self.filename_pattern = ''
        self.counter = 0

        # 创建文件夹选择按钮
        self.btn_select_folder = tk.Button(root, text='选择文件夹', command=self.select_folder)
        self.btn_select_folder.pack(pady=10)

        # 创建文件名模式输入框
        self.lbl_filename_pattern = tk.Label(root, text='文件名模式：')
        self.lbl_filename_pattern.pack()
        self.entry_filename_pattern = tk.Entry(root)
        self.entry_filename_pattern.pack()

        # 创建重命名按钮
        self.btn_rename = tk.Button(root, text='开始重命名', command=self.rename_files)
        self.btn_rename.pack(pady=10)

    def select_folder(self):
        "