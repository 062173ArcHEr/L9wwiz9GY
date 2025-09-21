# 代码生成时间: 2025-09-21 21:44:19
import tkinter as tk
from tkinter import messagebox
import hashlib

"""
哈希值计算工具
这是一个使用Python和Tkinter框架创建的图形界面程序，
用于计算字符串的哈希值。
"""

class HashCalculator:
    def __init__(self, master):
        """初始化界面"""
        self.master = master
        master.title("哈希值计算工具")
        
        # 输入框
        self.input_label = tk.Label(master, text="请输入字符串：")
        self.input_label.pack()
        self.input_text = tk.Entry(master, width=50)
        self.input_text.pack()
        
        # 选择哈希算法的下拉菜单
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("sha256")  # 默认选择sha256
        self.algorithm_label = tk.Label(master, text="选择哈希算法：")
        self.algorithm_label.pack()
        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, 'md5', 'sha1', 'sha256', 'sha512')
        self.algorithm_menu.pack()
        
        # 计算按钮
        self.calculate_button = tk.Button(master, text="计算哈希值", command=self.calculate_hash)
        self.calculate_button.pack()
        
        # 显示结果的标签
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
    def calculate_hash(self):
        "