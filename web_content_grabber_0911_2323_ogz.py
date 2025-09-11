# 代码生成时间: 2025-09-11 23:23:58
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading

"""
Web Content Grabber Application
This application allows users to input a URL and retrieve the webpage content.
"""

class WebContentGrabber:
    def __init__(self, root):
        self.root = root
# FIXME: 处理边界情况
        self.root.title("Web Content Grabber")
        self.create_widgets()
# 改进用户体验

    def create_widgets(self):
        # URL Label and Entry
        url_label = tk.Label(self.root, text="Enter URL:")
# NOTE: 重要实现细节
        url_label.pack()
        self.url_entry = tk.Entry(self.root, width=50)
# TODO: 优化性能
        self.url_entry.pack()

        # Go Button
        go_button = tk.Button(self.root, text="Go", command=self.get_web_content)
        go_button.pack()

        # Text Widget to display web content
# TODO: 优化性能
        self.text_widget = tk.Text(self.root, height=20, width=80)
        self.text_widget.pack()

    def get_web_content(self):
        # Get the URL from the entry widget
        url = self.url_entry.get()
        try:
            # Make a GET request to the URL
# NOTE: 重要实现细节
            response = requests.get(url)
# 添加错误处理
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            # Clear the text widget and insert the parsed HTML content
            self.text_widget.delete('1.0', tk.END)
# 增强安全性
            self.text_widget.insert('1.0', soup.prettify())
# 增强安全性
        except requests.exceptions.HTTPError as e:
            messagebox.showerror("HTTP Error", f"HTTP error occurred: {e}")
# 添加错误处理
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Request Exception", f"Request exception occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
# NOTE: 重要实现细节

if __name__ == "__main__":
# 扩展功能模块
    # Create the main window
    root = tk.Tk()
    # Create an instance of the WebContentGrabber class
    app = WebContentGrabber(root)
    # Start the main event loop
    root.mainloop()