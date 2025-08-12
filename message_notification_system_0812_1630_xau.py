# 代码生成时间: 2025-08-12 16:30:10
import tkinter as tk
from tkinter import messagebox
import threading
import time

"""
消息通知系统使用Tkinter框架创建，用于显示桌面通知。
该系统允许用户输入消息内容，并在指定的时间后显示通知。
"""

class MessageNotificationSystem:
    def __init__(self, master):
        """初始化窗口界面和组件"""
        self.master = master
        self.master.title("消息通知系统")
        
        self.message_label = tk.Label(master, text="请输入消息内容")
        self.message_label.pack()
        
        self.message_entry = tk.Entry(master)
        self.message_entry.pack()
        
        self.notify_button = tk.Button(master, text="发送通知", command=self.send_notification)
        self.notify_button.pack()
        
    def send_notification(self):
        """发送消息通知"""
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("警告", "请输入消息内容")
            return
        
        self.master.after(5000, self.display_notification, message)
        
    def display_notification(self, message):
        """显示消息通知"""
        messagebox.showinfo("通知", message)

# 创建主窗口
root = tk.Tk()

# 创建消息通知系统实例
notification_system = MessageNotificationSystem(root)

# 运行主循环
root.mainloop()