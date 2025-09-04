# 代码生成时间: 2025-09-05 07:39:03
import tkinter as tk
from tkinter import ttk
import psutil
import os
# NOTE: 重要实现细节
import threading

# 进程类，用于展示进程信息
class Process:
    def __init__(self, pid, name, username):
# 改进用户体验
        self.pid = pid
        self.name = name
        self.username = username

# 进程管理器GUI类
# 添加错误处理
class ProcessManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Process Manager')
        self.root.geometry('600x400')

        self.tree = ttk.Treeview(root, columns=('PID', 'Name', 'Username'), show='headings')
        self.tree.heading('PID', text='PID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Username', text='Username')
        self.tree.grid(column=0, row=0, padx=10, pady=10)

        self.update_button = ttk.Button(root, text='Update', command=self.update_processes)
# 改进用户体验
        self.update_button.grid(column=1, row=0, padx=10, pady=10)

        self.stop_button = ttk.Button(root, text='Stop Selected', command=self.stop_process)
        self.stop_button.grid(column=2, row=0, padx=10, pady=10)

    def update_processes(self):
        """更新进程列表"""
        self.tree.delete(*self.tree.get_children())  # 清除现有进程
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
# 增强安全性
                info = proc.info
                self.tree.insert('', 'end', values=(info['pid'], info['name'], info['username']))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def stop_process(self):
        """停止选中的进程"""
# 添加错误处理
        selected_items = self.tree.selection()
# 增强安全性
        if not selected_items:
            return

        for item in selected_items:
            pid = int(self.tree.item(item, 'values')[0])
            try:
                process = psutil.Process(pid)
# NOTE: 重要实现细节
                process.terminate()
                process.wait(timeout=3)
# 增强安全性
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

# 主函数
def main():
    root = tk.Tk()
    app = ProcessManagerGUI(root)
    app.update_processes()  # 初始更新进程列表
    root.mainloop()

if __name__ == '__main__':
    main()