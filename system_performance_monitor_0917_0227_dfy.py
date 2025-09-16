# 代码生成时间: 2025-09-17 02:27:52
import tkinter as tk
from tkinter import ttk
import psutil
import threading
import time

"""
系统性能监控工具
使用Python和Tkinter框架创建
"""

class SystemPerformanceMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('系统性能监控工具')
        self.root.geometry('800x600')
        self.create_widgets()
        self.update_system_info()

    def create_widgets(self):
# TODO: 优化性能
        # 创建CPU使用率标签
        cpu_label = tk.Label(self.root, text='CPU使用率(%):', font=('Arial', 12))
        cpu_label.grid(row=0, column=0, pady=10)

        # 创建CPU使用率显示框
        self.cpu_var = tk.DoubleVar()
        self.cpu_label = tk.Label(self.root, textvariable=self.cpu_var, font=('Arial', 12))
        self.cpu_label.grid(row=0, column=1, pady=10)

        # 创建内存使用率标签
        memory_label = tk.Label(self.root, text='内存使用率(%):', font=('Arial', 12))
        memory_label.grid(row=1, column=0, pady=10)

        # 创建内存使用率显示框
        self.memory_var = tk.DoubleVar()
        self.memory_label = tk.Label(self.root, textvariable=self.memory_var, font=('Arial', 12))
        self.memory_label.grid(row=1, column=1, pady=10)

        # 创建磁盘使用率标签
        disk_label = tk.Label(self.root, text='磁盘使用率(%):', font=('Arial', 12))
# TODO: 优化性能
        disk_label.grid(row=2, column=0, pady=10)

        # 创建磁盘使用率显示框
# 优化算法效率
        self.disk_var = tk.DoubleVar()
        self.disk_label = tk.Label(self.root, textvariable=self.disk_var, font=('Arial', 12))
        self.disk_label.grid(row=2, column=1, pady=10)

    def update_system_info(self):
        # 启动线程更新系统信息
        threading.Thread(target=self.monitor_system).start()
# TODO: 优化性能

    def monitor_system(self):
        while True:
            try:
                # 获取CPU使用率
                cpu_usage = psutil.cpu_percent(interval=1)
                self.cpu_var.set(cpu_usage)

                # 获取内存使用率
                memory_usage = psutil.virtual_memory().percent
                self.memory_var.set(memory_usage)

                # 获取磁盘使用率
                disk_usage = psutil.disk_usage('/').percent
                self.disk_var.set(disk_usage)

                # 每隔1秒更新一次
                time.sleep(1)
            except Exception as e:
                # 处理异常
                print(f'监控系统信息时出错: {e}')
# 优化算法效率
                break

    def run(self):
# TODO: 优化性能
        # 启动Tkinter事件循环
# FIXME: 处理边界情况
        self.root.mainloop()

if __name__ == '__main__':
    # 创建系统性能监控工具实例
    monitor = SystemPerformanceMonitor()
    # 运行系统性能监控工具
    monitor.run()