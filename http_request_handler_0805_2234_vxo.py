# 代码生成时间: 2025-08-05 22:34:00
import tkinter as tk
from tkinter import messagebox
import requests

"""
HTTP请求处理器，使用TKINTER创建图形界面。
允许用户输入HTTP请求的URL和方法，并显示响应结果。
"""

class HttpRequestHandler:
    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title('HTTP Request Handler')
        self.master.geometry('400x200')

        # 创建输入框和标签
        self.url_label = tk.Label(master, text='URL:')
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(master)
        self.url_entry.pack(pady=5)

        self.method_label = tk.Label(master, text='Method (GET/POST):')
        self.method_label.pack(pady=5)
        self.method_entry = tk.Entry(master)
        self.method_entry.pack(pady=5)

        # 创建按钮，点击时发送HTTP请求
        self.send_button = tk.Button(master, text='Send Request', command=self.send_http_request)
        self.send_button.pack(pady=10)

        # 创建结果显示区域
        self.result_label = tk.Label(master, text='')
        self.result_label.pack(pady=10)

    def send_http_request(self):
        """发送HTTP请求并显示结果"""
        url = self.url_entry.get()
        method = self.method_entry.get().upper()

        if not url:
            messagebox.showerror('Error', 'Please enter a URL')
            return

        try:
            if method == 'GET':
                response = requests.get(url)
            elif method == 'POST':
                response = requests.post(url)
            else:
                messagebox.showerror('Error', 'Unsupported method')
                return

            result_text = f'Status Code: {response.status_code}
Response Text: {response.text}'
            self.result_label.config(text=result_text)
        except requests.RequestException as e:
            messagebox.showerror('Error', str(e))


def main():
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()

if __name__ == '__main__':
    main()