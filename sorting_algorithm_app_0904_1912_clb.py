# 代码生成时间: 2025-09-04 19:12:36
import tkinter as tk
from tkinter import messagebox

"""
A simple tkinter application showcasing various sorting algorithms.
This app allows the user to input a list of numbers, select a sorting algorithm,
and see the sorted result.
"""

# Define a class to handle sorting algorithms
class SortingAlgorithms:
    def __init__(self):
        self.algorithms = {
            'Bubble Sort': self.bubble_sort,
            'Selection Sort': self.selection_sort,
            'Insertion Sort': self.insertion_sort
        }

    def bubble_sort(self, arr):
        """Implement bubble sort algorithm."""
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def selection_sort(self, arr):
        """Implement selection sort algorithm."""
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        """Implement insertion sort algorithm."""
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

# Define the main application class
class SortingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sorting Algorithm Visualizer')
        self.algorithms = SortingAlgorithms()
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(side=tk.TOP, fill=tk.X)
        self.input_label = tk.Label(self.input_frame, text='Enter numbers separated by spaces:')
        self.input_label.pack(side=tk.LEFT)
        self.input_entry = tk.Entry(self.input_frame, width=50)
        self.input_entry.pack(side=tk.LEFT)

        # Algorithm selection frame
        self.algorithm_frame = tk.Frame(self)
        self.algorithm_frame.pack(side=tk.TOP, fill=tk.X)
        self.algorithm_label = tk.Label(self.algorithm_frame, text='Select a sorting algorithm:')
        self.algorithm_label.pack(side=tk.LEFT)
        self.algorithm_var = tk.StringVar(self)
        self.algorithm_var.set('Bubble Sort')  # default value
        self.algorithm_options = self.algorithms.algorithms.keys()
        self.algorithm_menu = tk.OptionMenu(self.algorithm_frame, self.algorithm_var, *self.algorithm_options)
        self.algorithm_menu.pack(side=tk.LEFT)

        # Sort button
        self.sort_button = tk.Button(self, text='Sort', command=self.sort_numbers)
        self.sort_button.pack(side=tk.TOP)

        # Result label
        self.result_label = tk.Label(self, text='')
        self.result_label.pack(side=tk.TOP)

    def sort_numbers(self):
        try:
            # Get input and convert to list of integers
            input_str = self.input_entry.get()
            numbers = list(map(int, input_str.split()))
            # Get the selected algorithm and sort the numbers
            selected_algorithm = self.algorithms.algorithms[self.algorithm_var.get()]
            sorted_numbers = selected_algorithm(numbers.copy())
            # Display the sorted result
            self.result_label.config(text=f'Sorted numbers: {sorted_numbers}')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers separated by spaces.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    app = SortingApp()
    app.mainloop()