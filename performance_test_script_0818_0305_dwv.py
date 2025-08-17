# 代码生成时间: 2025-08-18 03:05:11
import tkinter as tk
from tkinter import messagebox
import requests
from time import time

"""
Performance Test Script using Python and TKinter.
This script allows the user to enter a URL and then tests the performance
by making a request to the entered URL and measuring the response time.
"""

class PerformanceTestApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Performance Test Script")
        self.geometry("400x200")
        self.url_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Enter URL: ").grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = tk.Entry(self, textvariable=self.url_var)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self, text="Test Performance", command=self.test_performance).grid(row=1, column=0, columnspan=2, pady=10)

    def test_performance(self):
        url = self.url_var.get()
        try:
            start_time = time()
            response = requests.get(url)
            response_time = time() - start_time
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            messagebox.showinfo("Performance Test", f"Response Time: {response_time:.2f} seconds, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app = PerformanceTestApp()
    app.mainloop()