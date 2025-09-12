# 代码生成时间: 2025-09-12 19:13:39
import tkinter as tk
from tkinter import messagebox

"""
访问权限控制程序，使用TKINTER框架。
用户输入用户名和密码，程序检查是否匹配预设的凭证。
如果匹配，显示访问权限信息；如果不匹配，显示错误消息。
"""

# 预设的用户名和密码
PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD = "password123"

class AccessControlApp:
    def __init__(self, root):
        """初始化应用界面"""
        self.root = root
        self.root.title("Access Control")
        self.create_widgets()

    def create_widgets(self):
        """创建应用界面的控件"""
        # 用户名标签和输入框
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        # 密码标签和输入框
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # 登录按钮
        self.login_button = tk.Button(self.root, text="Login", command=self.check_credentials)
        self.login_button.pack()

    def check_credentials(self):
        """检查用户名和密码是否正确"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            # 检查用户名和密码
            if username == PREDEFINED_USERNAME and password == PREDEFINED_PASSWORD:
                messagebox.showinfo("Access Granted", "You have access to the system.")
            else:
                messagebox.showerror("Access Denied", "Invalid username or password.")
        except Exception as e:
            # 错误处理
            messagebox.showerror("Error", f"An error occurred: {e}")

# 主函数
def main():
    root = tk.Tk()
    app = AccessControlApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()