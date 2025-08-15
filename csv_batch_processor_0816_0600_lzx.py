# 代码生成时间: 2025-08-16 06:00:21
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

"""CSV文件批量处理器

该程序用于批量处理CSV文件。
"""

class CSVBatchProcessor:
    def __init__(self, root):
        """初始化CSVBatchProcessor类
        :param root: Tkinter窗口对象
        """
        self.root = root
        self.root.title('CSV文件批量处理器')
        self.create_widgets()

    def create_widgets(self):
        "