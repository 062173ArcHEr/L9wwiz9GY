# 代码生成时间: 2025-08-12 01:27:08
import tkinter as tk
from tkinter import ttk
import psutil
import os

"""
A simple Python program that analyzes and displays the memory usage of the system using Tkinter for GUI.
"""

class MemoryUsageAnalyzer:
    def __init__(self, master):
        """Initialize the application with a Tkinter master window."""
        self.master = master
        self.master.title('Memory Usage Analyzer')
        
        # Create a frame for the application
        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)
        
        # Add a label to display the information
        self.info_label = ttk.Label(self.frame, text="Memory Usage: Loading...", wraplength=300)
        self.info_label.pack(pady=20)
        
        # Update memory usage information
        self.update_memory_usage()
        
    def update_memory_usage(self):
        """Update the memory usage information."""
        try:
            # Get system memory usage statistics
            mem = psutil.virtual_memory()
            used_mem = mem.used / (1024 ** 3)  # Convert bytes to gigabytes
            total_mem = mem.total / (1024 ** 3)
            
            # Format the information to display
            mem_usage_info = (
                f"Total Memory: {total_mem:.2f} GB
"
                f"Used Memory: {used_mem:.2f} GB
"
                f"Memory Usage Percentage: {mem.percent}%"
            )
            
            # Update the label with the memory usage information
            self.info_label.config(text=mem_usage_info)
        except Exception as e:
            # Handle any exceptions that occur when retrieving memory usage
            self.info_label.config(text=f"Error retrieving memory usage: {e}")
        
        # Schedule the next update after 1000 milliseconds (1 second)
        self.master.after(1000, self.update_memory_usage)

def main():
    """Create and run the application."""
    root = tk.Tk()
    app = MemoryUsageAnalyzer(root)
    root.mainloop()

if __name__ == '__main__':
    main()