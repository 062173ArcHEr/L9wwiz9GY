# 代码生成时间: 2025-08-21 07:34:53
import json
import tkinter as tk
from tkinter import messagebox

"""
JSON数据格式转换器程序。
该程序使用Tkinter框架创建一个图形用户界面(GUI)，
允许用户输入JSON字符串，并将其美化或压缩。
"""

class JSONConverter:
    """JSON数据格式转换器类。"""
    def __init__(self, root):
        """初始化GUI界面。"""
        self.root = root
        self.root.title("JSON Converter")

        # 输入区域
        self.input_label = tk.Label(root, text="Enter JSON data: ")
        self.input_label.pack()

        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.pack()

        # 输出区域
        self.output_label = tk.Label(root, text="Formatted JSON data: ")
        self.output_label.pack()

        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()

        # 按钮
        self.format_button = tk.Button(root, text="Format JSON", command=self.format_json)
        self.format_button.pack()

        self.compact_button = tk.Button(root, text="Compact JSON", command=self.compact_json)
        self.compact_button.pack()

    def format_json(self):
        "