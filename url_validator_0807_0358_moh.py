# 代码生成时间: 2025-08-07 03:58:14
import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
import requests

"""
A simple GUI application using Tkinter to validate the validity of a URL.
"""

class URLValidator:
    """
    A class to validate the URL.
    """
    def __init__(self, master):
        """
        Initialize the main window.
        """
        self.master = master
        master.title('URL Validator')

        # Label for the URL input
        self.label = tk.Label(master, text='Enter URL: ')
        self.label.pack()

        # Entry widget for the URL input
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Button to trigger URL validation
        self.button = tk.Button(master, text='Validate', command=self.validate_url)
        self.button.pack()

    def validate_url(self):
        """
        Validate the URL entered by the user.
        """
        url = self.entry.get()
        try:
            # Parse the URL to check if it's valid
            parsed_url = urlparse(url)
            if not parsed_url.scheme or not parsed_url.netloc:
                raise ValueError('Invalid URL')

            # Check if the URL is accessible
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code != 200:
                raise ConnectionError(f'URL is not accessible. Status code: {response.status_code}')

            # If the URL is valid and accessible, display a success message
            messagebox.showinfo('Validation', 'The URL is valid and accessible.')
        except ValueError as ve:
            messagebox.showerror('Error', str(ve))
        except ConnectionError as ce:
            messagebox.showerror('Error', str(ce))
        except Exception as e:
            messagebox.showerror('Error', 'An unexpected error occurred.')

def main():
    """
    The main function to run the application.
    """
    root = tk.Tk()
    app = URLValidator(root)
    root.mainloop()

if __name__ == '__main__':
    main()