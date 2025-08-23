# 代码生成时间: 2025-08-23 22:15:25
 * A tkinter-based GUI program that generates test data.
 */

import tkinter as tk
from tkinter import messagebox
import random
import string

"""
A class to handle the GUI and test data generation.
"""
class TestDataGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Test Data Generator')

        # Initialize variables
        self.string_length = tk.IntVar()
        self.string_length.set(10)  # Default length of the generated string

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Generate button
        tk.Button(self.master, text='Generate', command=self.generate_data).pack(pady=20)

        # String length label and entry
        tk.Label(self.master, text='Length of the string:').pack()
        tk.Entry(self.master, textvariable=self.string_length).pack()

        # Results label
        self.results_label = tk.Label(self.master, text='')
        self.results_label.pack(pady=20)

    def generate_data(self):
        """
        Generate a random string based on the provided length.
        """
        try:
            length = self.string_length.get()
            if not length.isdigit() or int(length) <= 0:
                raise ValueError('Length must be a positive integer.')

            # Generate a random string with the specified length
            data = ''.join(random.choices(string.ascii_letters + string.digits, k=int(length)))
            self.results_label.config(text=data)
        except ValueError as e:
            messagebox.showerror('Error', str(e))

"""
The main function that runs the GUI program.
"""
def main():
    root = tk.Tk()
    app = TestDataGenerator(root)
    root.mainloop()

if __name__ == '__main__':
    main()