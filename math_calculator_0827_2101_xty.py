# 代码生成时间: 2025-08-27 21:01:26
import tkinter as tk
from tkinter import messagebox

"""
Math Calculator - A simple graphical interface for mathematical calculations.

This program uses Tkinter to create a user-friendly calculator that performs basic
mathematical operations.
"""

class MathCalculator:
    def __init__(self, root):
        """Initialize the Math Calculator with a Tkinter window."""
        self.root = root
        self.root.title("Math Calculator")
        
        # Input field
        self.input_field = tk.Entry(root, width=35, borderwidth=5)
        self.input_field.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Labels for operations
        operations = ["Addition", "Subtraction", "Multiplication", "Division", "Square", "Square Root"]
        self.labels = {}
        for i, op in enumerate(operations):
            label = tk.Label(root, text=op)
            label.grid(row=i+1, column=0, padx=10, pady=5)
            self.labels[op] = label
        
        # Result labels
        self.results = {}
        for i, op in enumerate(operations):
            result = tk.Label(root, text=" ", fg="blue")
            result.grid(row=i+1, column=1, padx=10)
            self.results[op] = result
        
        # Calculate button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=len(operations)+1, column=0, columnspan=2, pady=10)
        
    def calculate(self):
        """Perform calculations based on the user input and update the labels."""
        try:
            value = float(self.input_field.get())
            for op, label in self.labels.items():
                if op == 'Addition':
                    self.results[op].config(text=str(value + value))
                elif op == 'Subtraction':
                    self.results[op].config(text=str(value - value))
                elif op == 'Multiplication':
                    self.results[op].config(text=str(value * value))
                elif op == 'Division':
                    self.results[op].config(text=str(value / value) if value != 0 else "Undefined")
                elif op == 'Square':
                    self.results[op].config(text=str(value ** 2))
                elif op == 'Square Root':
                    self.results[op].config(text=str(value ** 0.5))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()
    
    # Create an instance of MathCalculator
    calculator = MathCalculator(root)
    
    # Start the Tkinter event loop
    root.mainloop()