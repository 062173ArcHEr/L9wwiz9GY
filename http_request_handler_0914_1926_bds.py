# 代码生成时间: 2025-09-14 19:26:12
import tkinter as tk
from tkinter import messagebox
import requests
import threading

"""
HTTP请求处理器GUI应用程序
使用Tkinter框架创建一个简单的HTTP请求处理器，
用户可以通过这个界面发送HTTP请求，并显示响应结果。"""

class HttpRequestHandler:
    def __init__(self, root):
        self.root = root
        self.root.title('HTTP Request Handler')

        # 设置HTTP请求参数
        self.label_url = tk.Label(root, text='URL:')
        self.label_url.grid(row=0, column=0)
        self.entry_url = tk.Entry(root)
        self.entry_url.grid(row=0, column=1)

        self.label_method = tk.Label(root, text='Method:')
        self.label_method.grid(row=1, column=0)
        self.option_method = tk.StringVar(root)
        self.option_method.set('GET')  # 默认方法为GET
        self.option_menu = tk.OptionMenu(root, self.option_method, 'GET', 'POST', 'PUT', 'DELETE')
        self.option_menu.grid(row=1, column=1)

        self.label_data = tk.Label(root, text='Data (JSON):')
        self.label_data.grid(row=2, column=0)
        self.text_data = tk.Text(root, height=5, width=40)
        self.text_data.grid(row=2, column=1)

        # 发送按钮
        self.send_button = tk.Button(root, text='Send', command=self.send_request)
        self.send_button.grid(row=3, column=0, columnspan=2)

        # 显示响应结果
        self.label_response = tk.Label(root, text='Response:')
        self.label_response.grid(row=4, column=0)
        self.text_response = tk.Text(root, height=10, width=40)
        self.text_response.grid(row=4, column=1)
        self.text_response.config(state='disabled')

    def send_request(self):
        """发送HTTP请求并显示响应结果。"""
        url = self.entry_url.get()
        method = self.option_method.get()
        data = self.text_data.get('1.0', 'end-1c')
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            messagebox.showerror('Error', 'Invalid JSON data')
            return

        def threaded_request():
            try:
                response = requests.request(method, url, json=data)
                response_text = response.text
                self.display_response(response_text)
            except requests.RequestException as e:
                messagebox.showerror('Error', str(e))

        threading.Thread(target=threaded_request).start()

    def display_response(self, response_text):
        """在文本框中显示响应结果。"""
        self.text_response.config(state='normal')
        self.text_response.delete('1.0', 'end')
        self.text_response.insert('1.0', response_text)
        self.text_response.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()