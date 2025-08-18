# 代码生成时间: 2025-08-18 15:40:39
import tkinter as tk
from tkinter import messagebox
import json

"""
API Response Formatter Tool
A tkinter-based GUI application for formatting API responses.
"""

class ApiResponseFormatter:
    def __init__(self, master):
        """
        Initialize the GUI application.
        :param master: The parent window.
        """
        self.master = master
        self.master.title("API Response Formatter")

        # Input text area for API response
        self.response_label = tk.Label(master, text="API Response:")
        self.response_label.pack()
        self.response_text = tk.Text(master, height=10, width=50)
        self.response_text.pack()

        # Output text area for formatted response
        self.formatted_label = tk.Label(master, text="Formatted Response:")
        self.formatted_label.pack()
        self.formatted_text = tk.Text(master, height=10, width=50)
        self.formatted_text.pack()

        # Button to format the response
        self.format_button = tk.Button(master, text="Format", command=self.format_response)
        self.format_button.pack()

    def format_response(self):
        """
        Format the API response using JSON formatting.
        """
        try:
            # Get the API response from the input text area
            api_response = self.response_text.get("1.0", tk.END)
            # Parse the API response as JSON
            parsed_response = json.loads(api_response)
            # Format the JSON response
            formatted_response = json.dumps(parsed_response, indent=4)
            # Update the output text area with the formatted response
            self.formatted_text.delete("1.0", tk.END)
            self.formatted_text.insert(tk.END, formatted_response)
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            messagebox.showerror("Error", "Invalid JSON: " + str(e))

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the ApiResponseFormatter class
    app = ApiResponseFormatter(root)
    # Start the GUI event loop
    root.mainloop()