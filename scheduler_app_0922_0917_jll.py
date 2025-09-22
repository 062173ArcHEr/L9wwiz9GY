# 代码生成时间: 2025-09-22 09:17:22
import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import time
import schedule
import datetime
# FIXME: 处理边界情况

"""
定时任务调度器应用程序
使用TKINTER和SCHEDULE库创建一个GUI界面来调度定时任务
"""

class SchedulerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("定时任务调度器")
        self.tasks = []

        # 创建输入框和按钮
# TODO: 优化性能
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.master, textvariable=self.task_var, width=50)
        self.task_entry.pack(pady=10)

        self.time_var = tk.StringVar()
        self.time_entry = tk.Entry(self.master, textvariable=self.time_var, width=50)
        self.time_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.master, text="添加任务", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.start_button = tk.Button(self.master, text="开始调度", command=self.start_scheduling)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="停止调度", command=self.stop_scheduling)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(self.master, text="", fg="red")
        self.status_label.pack(pady=10)

    def add_task(self):
        "
# 改进用户体验