# 代码生成时间: 2025-08-27 00:00:10
import tkinter as tk
from tkinter import messagebox
import requests
import threading

"""
HTTP Request Handler application using Python and Tkinter.
This application allows the user to send HTTP requests to a specified URL and
displays the response or any errors that may occur.
"""

class HttpRequestHandler:
    def __init__(self, master):
        """Initialize the application's GUI."""
        self.master = master
        self.master.title("HTTP Request Handler")

        # Create GUI elements
        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()

        self.request_type_label = tk.Label(master, text="Request Type:")
        self.request_type_label.pack()
        self.get_button = tk.Radiobutton(master, text="GET", value="GET", variable=self.request_type)
        self.post_button = tk.Radiobutton(master, text="POST", value="POST", variable=self.request_type)
        self.get_button.pack()
        self.post_button.pack()

        self.request_type = tk.StringVar(value="GET")

        self.send_button = tk.Button(master, text="Send Request", command=self.send_request)
        self.send_button.pack()

        self.response_label = tk.Label(master, text="Response:")
        self.response_label.pack()
        self.response_text = tk.Text(master, height=10, width=50)
        self.response_text.pack()

    def send_request(self):
        """Send the HTTP request based on the user's input and display the response."""
        url = self.url_entry.get()
        request_type = self.request_type.get()

        # Clear the response text area
        self.response_text.delete(1.0, tk.END)

        # Send the request in a separate thread to avoid blocking the GUI
        threading.Thread(target=self.execute_request, args=(url, request_type)).start()

    def execute_request(self, url, request_type):
        """Execute the HTTP request and update the GUI with the response."""
        try:
            if request_type.upper() == 'GET':
                response = requests.get(url)
            elif request_type.upper() == 'POST':
                response = requests.post(url)  # You can add data to send with the POST request if needed
            else:
                messagebox.showerror("Error", "Invalid request type")
                return

            # Update the GUI with the response
            self.response_text.insert(tk.END, response.text)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = HttpRequestHandler(root)
    root.mainloop()

if __name__ == "__main__":
    main()