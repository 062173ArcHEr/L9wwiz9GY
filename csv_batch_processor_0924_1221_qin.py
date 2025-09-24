# 代码生成时间: 2025-09-24 12:21:12
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

"""
CSV文件批量处理器
该程序允许用户选择一个包含CSV文件的文件夹，然后对每个CSV文件执行批量处理。
"""

class CSVBatchProcessor:
    def __init__(self, root):
        """初始化CSVBatchProcessor类"""
        self.root = root
        self.root.title('CSV文件批量处理器')
        self.create_widgets()

    def create_widgets(self):
        "