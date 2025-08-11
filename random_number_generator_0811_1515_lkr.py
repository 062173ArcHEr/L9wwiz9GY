# 代码生成时间: 2025-08-11 15:15:09
import tkinter as tk
from tkinter import messagebox
import random
"""
随机数生成器程序
使用Python和Tkinter框架实现
"""

class RandomNumberGenerator:
    """随机数生成器类"""
    def __init__(self, master):
        """初始化界面"""
        self.master = master
        master.title("随机数生成器")

        # 输入框
        self.lower_label = tk.Label(master, text="最小值:")
        self.lower_label.pack()
        self.lower_entry = tk.Entry(master)
        self.lower_entry.pack()

        self.upper_label = tk.Label(master, text="最大值:")
        self.upper_label.pack()
        self.upper_entry = tk.Entry(master)
        self.upper_entry.pack()

        # 生成按钮
        self.generate_button = tk.Button(master, text="生成随机数", command=self.generate)
        self.generate_button.pack()

        # 结果标签
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def generate(self):
        """生成随机数"""
        try:
            lower = int(self.lower_entry.get())
            upper = int(self.upper_entry.get())
            if lower >= upper:
                messagebox.showerror("错误", "最小值必须小于最大值")
                return
            random_number = random.randint(lower, upper)
            self.result_label.config(text=f"{random_number}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数")

def main():
    """主函数"""
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()