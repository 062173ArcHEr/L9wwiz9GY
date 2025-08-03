# 代码生成时间: 2025-08-03 11:04:32
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import os

"""
数据清洗和预处理工具
使用TKINTER框架创建一个用户界面，允许用户选择数据文件，
然后进行数据清洗和预处理操作。
"""

class DataCleaningTool:
    def __init__(self, root):
        """
        初始化界面和相关组件
        :param root: tkinter主窗口
        """
        self.root = root
        self.root.title('数据清洗和预处理工具')

        # 创建文件选择按钮
        self.btn_open_file = tk.Button(self.root, text='选择文件', command=self.open_file)
        self.btn_open_file.pack()

        # 创建数据清洗按钮
        self.btn_clean_data = tk.Button(self.root, text='数据清洗', command=self.clean_data)
        self.btn_clean_data.pack()

        # 创建预处理按钮
        self.btn_preprocess_data = tk.Button(self.root, text='数据预处理', command=self.preprocess_data)
        self.btn_preprocess_data.pack()

        self.file_path = None

    def open_file(self):
        """
        打开文件选择对话框，选择数据文件
        """
        self.file_path = filedialog.askopenfilename()
        if not self.file_path:
            messagebox.showwarning('警告', '未选择文件')
            return
        messagebox.showinfo('信息', '文件选择成功')

    def clean_data(self):
        """
        对选定的数据文件进行清洗
        """
        if not self.file_path:
            messagebox.showwarning('警告', '请先选择文件')
            return
        try:
            df = pd.read_csv(self.file_path)
            # 假设我们清洗数据的方式是删除空值
            df = df.dropna()
            # 保存清洗后的数据
            df.to_csv(self.file_path, index=False)
            messagebox.showinfo('信息', '数据清洗成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def preprocess_data(self):
        "