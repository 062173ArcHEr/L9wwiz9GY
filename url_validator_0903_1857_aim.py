# 代码生成时间: 2025-09-03 18:57:23
import tkinter as tk
from tkinter import messagebox
import requests
from urllib.parse import urlparse

"""
URL Validator using Tkinter GUI

This program creates a simple GUI to validate the validity of a URL.
It checks if the URL is well-formed and if it can be accessed.
"""

class URLValidator:
    def __init__(self, master):
        self.master = master
        self.master.title("URL Validator")

        # Label
        self.label = tk.Label(master, text="Enter URL to validate:")
        self.label.pack(pady=10)

        # Entry Field
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=5)

        # Validate Button
        self.validate_button = tk.Button(master, text="Validate", command=self.validate_url)
        self.validate_button.pack(pady=5)

    def validate_url(self):
        url = self.entry.get()
        try:
            # Validate URL format
            if not self.is_valid_url(url):
                messagebox.showerror("Error", "Invalid URL format.")
                return

            # Check if URL is accessible
            if self.is_url_accessible(url):
                messagebox.showinfo("Success", "URL is valid and accessible.")
            else:
                messagebox.showerror("Error", "URL is valid but not accessible.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def is_valid_url(self, url):
        """
        Check if the URL is well-formed using urlparse.
        """
        result = urlparse(url)
        return all([result.scheme, result.netloc])

    def is_url_accessible(self, url):
        """
        Check if the URL is accessible using requests.
        """
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

def main():
    root = tk.Tk()
    app = URLValidator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
