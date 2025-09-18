# 代码生成时间: 2025-09-18 22:12:00
import requests
from tkinter import *
# 扩展功能模块
from tkinter import messagebox
import threading

"""
A simple web content grabber tool using Python and Tkinter.
This program allows users to input a URL and retrieve the content of the webpage.
"""

class WebContentGrabber:
    def __init__(self, root):
# 扩展功能模块
        """Initialize the GUI and setup the user interface."""
        self.root = root
        self.root.title('Web Content Grabber')
        
        self.url_label = Label(root, text='Enter URL:')
        self.url_label.pack()
        
        self.url_entry = Entry(root, width=50)
# 扩展功能模块
        self.url_entry.pack()
# NOTE: 重要实现细节
        
        self.fetch_button = Button(root, text='Fetch Content', command=self.fetch_content)
        self.fetch_button.pack()
        
        self.content_label = Label(root, text='Content:', font=('Helvetica', 12))
        self.content_label.pack()
        
        self.content_text = Text(root, height=20, width=80)
        self.content_text.pack()
# 添加错误处理
        
    def fetch_content(self):
        """Fetch the content of the webpage specified in the URL entry."""
        url = self.url_entry.get()
        if not url:
            messagebox.showerror('Error', 'Please enter a valid URL.')
            return

        self.content_text.delete('1.0', 'end')  # Clear the content text
# TODO: 优化性能
        self.content_text.insert('1.0', 'Fetching content...')
        
        threading.Thread(target=self.get_web_content, args=(url,)).start()
        
    def get_web_content(self, url):
# 添加错误处理
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            self.content_text.delete('1.0', 'end')  # Clear the 'Fetching content...' message
# 改进用户体验
            self.content_text.insert('1.0', response.text)
        except requests.exceptions.RequestException as e:
            messagebox.showerror('Error', f'Failed to fetch content: {e}')

def main():
    """Create and run the GUI application."""
    root = Tk()
    app = WebContentGrabber(root)
    root.mainloop()

if __name__ == '__main__':
    main()