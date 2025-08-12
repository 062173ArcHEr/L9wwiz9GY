# 代码生成时间: 2025-08-12 08:56:43
import tkinter as tk
from tkinter import messagebox

"""
A simple math calculator app using Tkinter framework in Python.
This calculator provides basic mathematical operations: addition, subtraction, multiplication, and division.
"""

class MathCalculator:
    def __init__(self, root):
        """Initialize the calculator GUI."""
        self.root = root
        self.root.title('Math Calculator')

        # Create the entry widget for input and display
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for basic operations
        operations = {
            '7': 7, '8': 8, '9': 9, '+': self.add,
            '4': 4, '5': 5, '6': 6, '-': self.subtract,
            '1': 1, '2': 2, '3': 3, '*': self.multiply,
            'C': self.clear, '0': 0, '=': self.equals, '/': self.divide
        }

        # Create the buttons and assign operations
        row = 1
        col = 0
        for key, value in operations.items():
            if key in ('+', '-', '*', '/'):
                button = tk.Button(root, text=key, padx=40, pady=20,
                                  command=lambda v=value: self.operation(v))
            else:
                button = tk.Button(root, text=key, padx=40, pady=20,
                                  command=lambda v=value: self.insert(v))
            button.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def insert(self, value):
        """Insert the value into the entry widget."""
        self.entry.insert(tk.END, str(value))

    def clear(self):
        "