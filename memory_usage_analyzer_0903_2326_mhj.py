# 代码生成时间: 2025-09-03 23:26:58
import psutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
Memory Usage Analyzer - A tkinter application to analyze system memory usage.
This program uses the psutil library to fetch system memory information and
display it in a user-friendly manner using tkinter.
"""

class MemoryUsageAnalyzer:
    def __init__(self, master):
        """Initialize the application window."""
        self.master = master
        self.master.title("Memory Usage Analyzer")

        # Initialize a dictionary to store memory usage data
        self.memory_data = {}

        # Create a frame for the memory usage graph
        self.graph_frame = ttk.Frame(self.master)
        self.graph_frame.pack(padx=10, pady=10)

        # Create a canvas for the memory usage graph
        self.canvas = tk.Canvas(self.graph_frame, width=400, height=200)
        self.canvas.pack()

        # Create a button to fetch memory usage data
        self.fetch_button = ttk.Button(self.master, text="Fetch Memory Usage", command=self.fetch_memory_usage)
        self.fetch_button.pack(pady=5)

    def fetch_memory_usage(self):
        """Fetch system memory usage data and update the graph."""
        try:
            # Fetch memory usage data using psutil
            memory = psutil.virtual_memory()
            self.memory_data = {
                "total": memory.total,
                "available": memory.available,
                "used": memory.used,
                "free": memory.free,
                "percent": memory.percent
            }

            # Update the graph with the new data
            self.update_graph()
        except Exception as e:
            # Handle any exceptions that occur during data fetching
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def update_graph(self):
        """Update the graph with the latest memory usage data."""
        # Clear the canvas
        self.canvas.delete("all")

        # Draw a rectangle for the total memory
        self.canvas.create_rectangle(0, 100, 400, 0, fill="grey")

        # Calculate the width of the used memory rectangle
        used_width = (self.memory_data["used"] / self.memory_data["total"]) * 400

        # Draw a rectangle for the used memory
        self.canvas.create_rectangle(0, 100, used_width, 0, fill="red")

        # Draw a line to represent the total memory
        self.canvas.create_line(0, 50, 400, 50, fill="black")

        # Draw a line to represent the used memory
        self.canvas.create_line(0, 100, 400, 100, fill="black")

        # Add text to display the memory usage percentage
        self.canvas.create_text(200, 150, text=f"Memory Usage: {self.memory_data['percent']}%", fill="black")

def main():
    # Create the main window
    root = tk.Tk()

    # Create an instance of the MemoryUsageAnalyzer class
    app = MemoryUsageAnalyzer(root)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()