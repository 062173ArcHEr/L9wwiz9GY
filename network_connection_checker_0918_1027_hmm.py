# 代码生成时间: 2025-09-18 10:27:29
import tkinter as tk
from tkinter import messagebox
import requests
import socket
import threading

"""
网络连接状态检查器
检查并显示当前网络连接状态
"""

# 检查网络连接状态的函数
def check_connection():
    try:
        # 使用HTTP请求测试网络连接
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            messagebox.showinfo('网络连接状态', '网络连接正常')
        else:
            messagebox.showerror('网络连接状态', '网络连接异常')
    except requests.ConnectionError:
        messagebox.showerror('网络连接状态', '网络连接异常')
    except Exception as e:
        messagebox.showerror('网络连接状态', str(e))

# 在单独的线程中运行网络连接检查
def run_check_connection():
    threading.Thread(target=check_connection).start()

# 创建主窗口
root = tk.Tk()
root.title('网络连接状态检查器')

# 创建并放置按钮
check_button = tk.Button(root, text='检查网络连接', command=run_check_connection)
check_button.pack(pady=20)

# 运行主事件循环
root.mainloop()