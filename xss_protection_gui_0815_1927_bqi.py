# 代码生成时间: 2025-08-15 19:27:48
import tkinter as tk
from tkinter import messagebox

# 导入第三方库，用于HTML转义和XSS攻击防护
import html

class XSSProtectionApplication:
    """
    使用Tkinter创建的GUI应用程序，用于防护XSS攻击。
    """
    def __init__(self, master):
        self.master = master
        self.master.title("XSS Protection")

        # 创建输入框和输出框
        self.input_text = tk.Text(master, height=10, width=50)
        self.output_text = tk.Text(master, height=10, width=50)
        self.input_text.pack()
        self.output_text.pack()

        # 创建防护按钮
        button = tk.Button(master, text="Protect against XSS", command=self.protect_against_xss)
        button.pack()

    def protect_against_xss(self):
        try:
            # 获取用户输入
            user_input = self.input_text.get("1.0", tk.END)
            # 对用户输入进行HTML转义，以防护XSS攻击
            escaped_input = html.escape(user_input)
            # 将防护后的文本放入输出框
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", escaped_input)
        except Exception as e:
            # 错误处理
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = XSSProtectionApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()