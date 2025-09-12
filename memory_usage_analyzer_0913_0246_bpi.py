# 代码生成时间: 2025-09-13 02:46:07
import psutil
import tkinter as tk
from tkinter import ttk

"""
这是一个使用Python和Tkinter框架创建的内存使用情况分析工具。
它能够显示系统的内存使用情况，并以图形化的形式展示。
"""

class MemoryUsageAnalyzer:
    def __init__(self):
        """初始化内存使用情况分析器"""
        self.root = tk.Tk()
        self.root.title("Memory Usage Analyzer")
        self.create_widgets()

    def create_widgets(self):
        """创建GUI组件"""
        # 设置窗口大小
        self.root.geometry("400x300")

        # 内存使用情况标签
        self.label = tk.Label(self.root, text="Memory Usage: ", font=("Arial", 12))
        self.label.pack(pady=20)

        # 刷新按钮
        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.refresh_memory_usage)
        self.refresh_button.pack(pady=10)

    def refresh_memory_usage(self):
        """刷新内存使用情况"""
        try:
            # 获取内存使用率
            mem = psutil.virtual_memory()
            usage = mem.percent

            # 更新标签显示
            self.label.config(text=f"Memory Usage: {usage}%")
        except Exception as e:
            # 错误处理
            self.label.config(text=f"Error: {str(e)}")

    def run(self):
        """运行GUI程序"""
        self.root.mainloop()

if __name__ == "__main__":
    """程序入口点"""
    analyzer = MemoryUsageAnalyzer()
    analyzer.run()