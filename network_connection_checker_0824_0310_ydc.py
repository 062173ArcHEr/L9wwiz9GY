# 代码生成时间: 2025-08-24 03:10:46
import tkinter as tk
from tkinter import messagebox
import requests
import socket

# 检查网络连接状态的函数
def check_connection():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        if response.status_code == 200:
            messagebox.showinfo('网络状态', '网络连接正常！')
        else:
            messagebox.showerror('网络状态', '网络连接异常！')
    except requests.exceptions.RequestException as e:
        messagebox.showerror('网络状态', '网络连接异常：' + str(e))

# 创建主窗口
root = tk.Tk()
root.title('网络连接状态检查器')
root.geometry('300x150')

# 创建一个按钮，点击后检查网络连接状态
check_button = tk.Button(root, text='检查网络连接', command=check_connection)
check_button.pack(pady=20)

# 运行主循环
root.mainloop()