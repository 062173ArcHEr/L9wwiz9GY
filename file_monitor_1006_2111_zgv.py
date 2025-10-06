# 代码生成时间: 2025-10-06 21:11:43
import os
import time
from tkinter import Tk, Label, Button

"""
文件监控和变更通知程序
使用Python和Tkinter框架实现文件监控和变更通知的功能。
"""

class FileMonitor:
    def __init__(self, path):
        """初始化文件监控器"""
        self.path = path
        self.last_modification_time = None
        try:
            self.last_modification_time = os.path.getmtime(self.path)
        except OSError as e:
            print(f"Error: {e}")

    def check_file_change(self):
        """检查文件是否发生变化"""
        try:
            current_modification_time = os.path.getmtime(self.path)
            if current_modification_time != self.last_modification_time:
                self.last_modification_time = current_modification_time
                return True
            return False
        except OSError as e:
            print(f"Error: {e}")
            return False

    def monitor(self):
        """监控文件直到发生变更"""
        while True:
            if self.check_file_change():
                print(f"File {self.path} has changed.")
                break
            time.sleep(1)

class TkinterApp:
    def __init__(self, root):
        """初始化Tkinter应用程序"""
        self.root = root
        self.root.title('File Monitor')

        self.label = Label(root, text='Monitoring file for changes...')
        self.label.pack(pady=20)

        self.monitor_button = Button(root, text='Start Monitoring', command=self.start_monitoring)
        self.monitor_button.pack(pady=10)

    def start_monitoring(self):
        "