# 代码生成时间: 2025-09-21 10:15:52
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# 定义一个类，用于创建集成测试工具的GUI界面
class IntegrationTestTool:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Integration Test Tool")
        self.create_widgets()

    def create_widgets(self):
        # 创建一个文本框，用于输入要测试的命令
        self.cmd_label = tk.Label(self.master, text="Enter test command: ")
        self.cmd_label.pack()
        self.cmd_entry = tk.Entry(self.master, width=80)
        self.cmd_entry.pack()

        # 创建一个按钮，用于执行测试命令
        self.run_button = tk.Button(self.master, text="Run Test", command=self.run_test)
        self.run_button.pack()

        # 创建一个文本框，用于显示测试结果
        self.result_label = tk.Label(self.master, text="Test result: ")
        self.result_label.pack()
        self.result_text = tk.Text(self.master, height=10, width=80)
        self.result_text.pack()

    def run_test(self):
        # 获取用户输入的测试命令
        command = self.cmd_entry.get()

        # 检查命令是否为空
        if not command:
            messagebox.showerror("Error", "Please enter a test command.")
            return

        try:
            # 执行测试命令，并捕获输出
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            # 将输出结果显示在文本框中
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, output.decode())
        except subprocess.CalledProcessError as e:
            # 如果命令执行失败，显示错误信息
            messagebox.showerror("Error", f"Command failed with return code {e.returncode}: {e.output.decode()}")
        except Exception as e:
            # 处理其他异常
            messagebox.showerror("Error", str(e))

# 创建主窗口并运行程序
if __name__ == '__main__':
    root = tk.Tk()
    app = IntegrationTestTool(master=root)
    root.mainloop()