# 代码生成时间: 2025-09-06 22:44:07
import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
import requests

"""
URL链接有效性验证程序，使用Python和Tkinter框架实现。
该程序允许用户输入一个URL链接，然后验证其有效性。
"""

class URLValidator:
    def __init__(self):
        """
        初始化URL验证类。
        """
        self.root = tk.Tk()
        self.root.title("URL Validator")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        """
        创建GUI组件。
        """
        self.url_label = tk.Label(self.root, text="Enter URL: ")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        self.validate_button = tk.Button(self.root, text="Validate URL", command=self.validate_url)
        self.validate_button.pack(pady=5)

    def validate_url(self):
        """
        验证用户输入的URL链接。
        """
        url = self.url_entry.get()
        try:
            self.validate_url_link(url)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def validate_url_link(self, url):
        """
        检查URL链接的有效性。
        """
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            messagebox.showerror("Invalid URL", "Please enter a valid URL.")
            return

        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                messagebox.showinfo("Valid URL", "The URL is valid.")
            else:
                messagebox.showerror("Invalid URL", f"The URL is invalid. Status code: {response.status_code}")
        except requests.RequestException as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    URLValidator()