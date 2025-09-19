# 代码生成时间: 2025-09-19 08:11:27
import tkinter as tk
from tkinter import messagebox
import threading
import time

"""
消息通知系统
该程序使用Python和Tkinter框架实现一个简单的桌面通知系统。
它允许用户输入消息，并在指定的时间后显示通知。
"""

class MessageNotificationSystem:
    """消息通知系统类"""
    def __init__(self, master):
        """初始化GUI"""
        self.master = master
        self.master.title("消息通知系统")

        # 创建输入框和标签
        self.label = tk.Label(master, text="输入消息：")
        self.label.pack()
        self.message_entry = tk.Entry(master)
        self.message_entry.pack()

        # 创建通知时间输入框和标签
        self.time_label = tk.Label(master, text="通知时间（秒）：")
        self.time_label.pack()
        self.time_entry = tk.Entry(master)
        self.time_entry.pack()

        # 创建按钮
        self.send_button = tk.Button(master, text="发送消息", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        """发送消息的方法"""
        try:
            # 获取用户输入的消息和通知时间
            message = self.message_entry.get()
            time_to_notify = int(self.time_entry.get())
            if message and time_to_notify > 0:
                # 创建一个线程来处理通知
                threading.Thread(target=self.notify, args=(message, time_to_notify)).start()
            else:
                messagebox.showerror("错误", "请输入有效的消息和通知时间！")
        except ValueError:
            messagebox.showerror("错误", "通知时间必须是整数！")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def notify(self, message, time_to_notify):
        """显示通知的方法"""
        try:
            # 等待指定的时间
            time.sleep(time_to_notify)
            # 显示通知
            messagebox.showinfo("通知", message)
        except Exception as e:
            messagebox.showerror("错误", str(e))

# 创建主窗口
root = tk.Tk()
# 创建消息通知系统实例
app = MessageNotificationSystem(root)
# 运行主循环
root.mainloop()