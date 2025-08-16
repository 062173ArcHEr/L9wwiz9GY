# 代码生成时间: 2025-08-17 04:46:12
import tkinter as tk
from tkinter import messagebox

"""
FormValidator: A simple form validator using Python and Tkinter.

This script creates a GUI application with a form that includes a text entry for user input.
It provides basic validation for the input to ensure it meets the predefined criteria.

Features:
- Validation of input to check if it is not empty and has at least 5 characters.
- Displaying error messages if the input does not meet the criteria.
"""

class FormValidator:
    def __init__(self, master):
        """Initialize the FormValidator with the parent window."""
        self.master = master
        self.master.title("Form Validator")
        self.master.geometry("300x200")

        # Create a Label for the input field
        self.label = tk.Label(master, text="Enter your input: ")
        self.label.pack(padx=10, pady=10)

        # Create an Entry widget for user input
        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=10)

        # Create a Button to trigger the validation
        self.button = tk.Button(master, text="Submit", command=self.validate_input)
        self.button.pack(padx=10, pady=10)

    def validate_input(self):
        """Validate the input from the Entry widget."""
        user_input = self.entry.get()
        if not user_input:
            messagebox.showerror("Error", "Input cannot be empty.")
        elif len(user_input) < 5:
            messagebox.showerror("Error", "Input must be at least 5 characters long.")
        else:
            messagebox.showinfo("Success", "Input is valid!")

if __name__ == "__main__":
    # Create the main window and pass it to the FormValidator
    root = tk.Tk()
    app = FormValidator(root)
    root.mainloop()
