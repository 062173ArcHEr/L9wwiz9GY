# 代码生成时间: 2025-09-24 01:20:37
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

"""
Integration Test Tool

A simple GUI application using Tkinter to run integration tests.
This tool allows users to specify a test script, execute it, and view the results.
"""

class IntegrationTestTool:
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Integration Test Tool")

        # Create a frame for the input fields
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Create a label and entry for the test script path
        tk.Label(frame, text="Test Script Path: ").grid(row=0, column=0)
        self.script_path_entry = tk.Entry(frame, width=50)
        self.script_path_entry.grid(row=0, column=1)

        # Create a button to run the test script
        self.run_button = tk.Button(frame, text="Run Test", command=self.run_test)
        self.run_button.grid(row=1, column=0, columnspan=2)

    def run_test(self):
        """Run the test script specified in the input field."""
        try:
            # Get the test script path from the input field
            script_path = self.script_path_entry.get()

            # Check if the script path is empty
            if not script_path:
                messagebox.showerror("Error", "Please specify a test script path.")
                return

            # Run the test script using subprocess
            result = subprocess.run([script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Display the test results in a message box
            messagebox.showinfo("Test Results", f"stdout: {result.stdout.decode('utf-8')}
stderr: {result.stderr.decode('utf-8')}")
        except subprocess.CalledProcessError as e:
            # Handle errors during test script execution
            messagebox.showerror("Error", f"Test script failed with exit code {e.returncode}: {e.stderr.decode('utf-8')}")
        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Error", str(e))

def main():
    """Create the main application window and run the GUI event loop."""
    root = tk.Tk()
    app = IntegrationTestTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()