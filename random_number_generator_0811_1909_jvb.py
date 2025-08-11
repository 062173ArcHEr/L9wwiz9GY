# 代码生成时间: 2025-08-11 19:09:38
import tkinter as tk
from tkinter import messagebox
import random

"""
A simple tkinter application to generate random numbers.
This program allows the user to specify the range of random number generation
and displays the result in a label.
"""

class RandomNumberGeneratorApp:
    def __init__(self, root):
        """Initialize the application with a tkinter root window."""
        self.root = root
        self.root.title("Random Number Generator")

        # Labels for user instructions and displaying the result
        self.instructions_label = tk.Label(root, text="Enter the range to generate a random number:",
                                      font=("Helvetica", 12))
        self.instructions_label.pack(pady=(20, 10))

        # Entry widget for user input
        self.lower_entry = tk.Entry(root, font=("Helvetica\, 12))
        self.lower_entry.pack(pady=5)

        self.upper_entry = tk.Entry(root, font=("Helvetica\, 12))
        self.upper_entry.pack(pady=5)

        # Generate button
        self.generate_button = tk.Button(root, text="Generate", command=self.generate_random_number,
                                          font=("Helvetica\, 12))
        self.generate_button.pack(pady=(10, 20))

        # Label to display the result
        self.result_label = tk.Label(root, text="", font=("Helvetica\, 12))
        self.result_label.pack(pady=10)

    def generate_random_number(self):
        try:
            # Retrieve user input and convert to integers
            lower = int(self.lower_entry.get())
            upper = int(self.upper_entry.get())

            # Check for valid range
            if lower >= upper:
                messagebox.showerror("Error", "Lower bound must be less than the upper bound.")
                return

            # Generate and display the random number
            random_number = random.randint(lower, upper)
            self.result_label.config(text=f"Random Number: {random_number}")
        except ValueError:
            # Handle non-integer input
            messagebox.showerror("Error", "Please enter valid integers for both bounds.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()