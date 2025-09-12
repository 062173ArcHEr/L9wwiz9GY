# 代码生成时间: 2025-09-12 14:02:57
import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

"""
Web Content Grabber Tool
========================
This tool is designed to fetch content from a given URL using Python and Tkinter framework.
"""

def fetch_content(url):
    """Fetches content from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch content: {e}")
        return None


def parse_content(html_content):
    """Parses HTML content using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.prettify()


def main():
    """Main function to run the web content grabber tool."""
    root = tk.Tk()
    root.title("Web Content Grabber Tool")

    # Create a text input for URL
    url_label = tk.Label(root, text="Enter URL: ")
    url_label.pack()
    url_entry = tk.Entry(root, width=50)
    url_entry.pack()

    # Create a button to fetch content
    fetch_button = tk.Button(root, text="Fetch Content", command=lambda: display_content(url_entry.get()))
    fetch_button.pack()

    # Create a text area to display fetched content
    content_text = tk.Text(root, height=20, width=100)
    content_text.pack()

    root.mainloop()


def display_content(url):
    """Displays the fetched content in the text area."""
    html_content = fetch_content(url)
    if html_content:
        content_text.delete(1.0, tk.END)  # Clear the text area
        content_text.insert(tk.END, parse_content(html_content))

if __name__ == "__main__":
    main()
