# 代码生成时间: 2025-10-09 01:47:24
import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import os

"""进程管理器程序，使用tkinter框架实现基本的进程查看、结束功能。"""

# 定义进程管理器类
class ProcessManager:
    def __init__(self, root):
        self.root = root
        self.root.title('进程管理器')
        self.root.geometry('600x400')

        # 创建进程列表框
        self.process_list = tk.Listbox(root, width=50, height=20)
        self.process_list.pack(pady=10)

        # 创建按钮
        self.refresh_button = tk.Button(root, text='刷新进程', command=self.refresh_processes)
        self.refresh_button.pack(pady=5)

        self.kill_button = tk.Button(root, text='结束选中进程', command=self.kill_selected_process)
        self.kill_button.pack(pady=5)

    # 刷新进程列表
    def refresh_processes(self):
        try:
            # 获取所有进程
            processes = psutil.process_iter(['pid', 'name'])
            # 清空进程列表
            self.process_list.delete(0, tk.END)
            # 添加进程到列表
            for process in processes:
                self.process_list.insert(tk.END, f"{process.info['pid']}: {process.info['name']}")
        except Exception as e:
            messagebox.showerror('错误', str(e))

    # 结束选中的进程
    def kill_selected_process(self):
        try:
            # 获取选中的进程索引
            selected_process = self.process_list.curselection()
            if not selected_process:
                messagebox.showinfo('提示', '请选中一个进程')
                return
            # 获取进程PID
            pid = int(self.process_list.get(selected_process[0]).split(':')[0])
            # 结束进程
            process = psutil.Process(pid)
            process.terminate()
            messagebox.showinfo('提示', '进程已结束')
            # 刷新进程列表
            self.refresh_processes()
        except Exception as e:
            messagebox.showerror('错误', str(e))

# 主函数
def main():
    root = tk.Tk()
    app = ProcessManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()