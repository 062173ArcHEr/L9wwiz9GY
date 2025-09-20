# 代码生成时间: 2025-09-20 12:22:30
import tkinter as tk
from tkinter import messagebox
import requests
import socket
import threading

"""
Network Status Checker application using Python and Tkinter framework.
This application checks the network connection status and provides feedback to the user.
"""

class NetworkStatusChecker:
    """Class responsible for checking network connection status."""

    def __init__(self, host="www.google.com", port=80, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout

    def check_connection(self):
        """Check if the network connection is active."""
        try:
            socket.create_connection((self.host, self.port), self.timeout)
            return True
        except OSError:
            return False

    def check_connection_thread(self):
        """Threaded function to check network connection."""
        connection_status = self.check_connection()
        if connection_status:
            print("Network connection is active.")
        else:
            print("Network connection is inactive.")

class App:
    """Tkinter GUI application class."""

    def __init__(self, root):
        self.root = root
        self.root.title("Network Status Checker")

        self.network_checker = NetworkStatusChecker()

        # Create buttons
        tk.Button(self.root, text="Check Network Connection",
                  command=self.check_network_connection).pack(pady=20)

    def check_network_connection(self):
        """Function to check network connection and display the result."""
        threading.Thread(target=self.network_checker.check_connection_thread).start()
        try:
            response = requests.get("https://www.google.com")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Network connection is active.")
            else:
                messagebox.showerror("Error", "Network connection is inactive.")
        except requests.ConnectionError:
            messagebox.showerror("Error", "Network connection is inactive.")

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()