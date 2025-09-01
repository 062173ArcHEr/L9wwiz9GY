# 代码生成时间: 2025-09-01 10:20:05
import tkinter as tk
from tkinter import messagebox
import hashlib

"""
密码加密解密工具
使用TKINTER框架创建的用户界面
"""

class PasswordTool:
    def __init__(self, master):
        """
        初始化应用界面
        :param master: tkinter的主窗口
        """
        self.master = master
        self.master.title('密码加密解密工具')

        # 创建输入框
        self.password_var = tk.StringVar()
        tk.Entry(self.master, textvariable=self.password_var, width=50).grid(row=0, column=1)

        # 创建加密按钮
        tk.Button(self.master, text='加密', command=self.encrypt).grid(row=1, column=0)

        # 创建解密按钮
        tk.Button(self.master, text='解密', command=self.decrypt).grid(row=1, column=2)

        # 创建输出框
        self.output_var = tk.StringVar()
        tk.Entry(self.master, textvariable=self.output_var, width=50, state='readonly').grid(row=2, column=1)

    def encrypt(self):
        """
        加密密码
        """
        try:
            password = self.password_var.get()
            if password:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                self.output_var.set(hashed_password)
            else:
                messagebox.showwarning('警告', '请输入密码')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def decrypt(self):
        """
        解密密码
        注意：SHA-256是不可逆的，因此无法直接解密
        这里只是显示原始密码（如果已知）
        """
        try:
            password = self.password_var.get()
            if password:
                self.output_var.set(password)  # 显示原始密码
            else:
                messagebox.showwarning('警告', '请输入密码')
        except Exception as e:
            messagebox.showerror('错误', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    PasswordTool(root)
    root.mainloop()