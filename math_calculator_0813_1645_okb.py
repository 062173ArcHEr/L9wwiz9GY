# 代码生成时间: 2025-08-13 16:45:07
import tkinter as tk
from tkinter import messagebox

"""
Math Calculator
A simple GUI calculator for basic mathematical operations.
"""

class MathCalculator:
    def __init__(self, master):
        """Initialize the calculator GUI."""
        self.master = master
# 增强安全性
        self.master.title("Math Calculator")
        self.create_widgets()
# 改进用户体验

    def create_widgets(self):
        """Create the calculator's widgets."""
        frame = tk.Frame(self.master)
        frame.pack(side="top", fill="both", expand=True)

        self.result = tk.StringVar()
        self.result_label = tk.Label(frame, textvariable=self.result, width=35, height=2)
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.buttons = {
# 改进用户体验
            "7": (1, 0),
            "8": (1, 1),
# TODO: 优化性能
            "9": (1, 2),
            "/": (1, 3),
            "4": (2, 0),
# 增强安全性
            "5": (2, 1),
            "6": (2, 2),
            "*": (2, 3),
# FIXME: 处理边界情况
            "1": (3, 0),
            "2": (3, 1),
            "3": (3, 2),
            "-": (3, 3),
            "0": (4, 0),
# 添加错误处理
            ".": (4, 1),
            "=": (4, 2),
            "+": (4, 3)
# 改进用户体验
        }
        for button, pos in self.buttons.items():
            b = tk.Button(frame, text=button, width=5, height=2,
                         command=lambda x=button: self.click_button(x))
            b.grid(row=pos[0]+1, column=pos[1])

    def click_button(self, button):
        """Handle button clicks."""
        if button == ".":
            current = self.result.get()
# FIXME: 处理边界情况
            if "." not in current:
# 添加错误处理
                self.result.set(current + ".")
        elif button == "=":
            try:
# 增强安全性
                self.result.set(str(eval(self.result.get())))
            except Exception as e:
# 优化算法效率
                messagebox.showerror("Error", "Invalid expression")
                self.result.set("")
        else:
            current = self.result.get()
# TODO: 优化性能
            if button == "+" and current == "":
                self.result.set("0+")
            elif button == "-" and current == ""::
                self.result.set("0-")
            elif button == "*" and current == ""::
                self.result.set("0*")
            elif button == "/" and current == ""::
                self.result.set("0/")
# 改进用户体验
            else:
                self.result.set(current + button)

    def run(self):
        """Run the calculator's main loop."""
        self.master.mainloop()
# 增强安全性

if __name__ == "__main__":
    root = tk.Tk()
    app = MathCalculator(root)
# FIXME: 处理边界情况
    app.run()