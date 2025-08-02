# 代码生成时间: 2025-08-02 11:29:01
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

# TestReportGenerator class to create a GUI application for generating test reports
class TestReportGenerator:
    """
    The TestReportGenerator class provides a graphical user interface for generating test reports.
    It allows users to specify the test results, and then generates a test report file.
    """

    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Test Report Generator")

        # Create the interface components
        self.create_widgets()

    def create_widgets(self):
        # Create a text area for entering test results
        self.test_results_text = tk.Text(self.root, height=10, width=50)
        self.test_results_text.pack(pady=10)

        # Create a button to select the output file path
        self.browse_button = tk.Button(self.root, text="Select Output File", command=self.browse_file)
        self.browse_button.pack()

        # Create a button to generate the test report
        self.generate_button = tk.Button(self.root, text="Generate Test Report", command=self.generate_report)
        self.generate_button.pack(pady=5)

    def browse_file(self):
        try:
            # Open a file dialog to select the output file path
            self.output_file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
            )
        except Exception as e:
            # Handle any exceptions that occur during file selection
            messagebox.showerror("Error", f"An error occurred: {e}")

    def generate_report(self):
        try:
            if not self.output_file_path:
                # Prompt the user to select an output file path if none is chosen
                messagebox.showwarning("Warning", "Please select an output file path.")
                return

            # Get the test results from the text area
            test_results = self.test_results_text.get("1.0", "end-1c")

            # Generate the test report and write it to the output file
            with open(self.output_file_path, "w") as file:
                file.write(test_results)

            # Notify the user that the report has been generated
            messagebox.showinfo("Success", "Test report generated successfully.")
        except Exception as e:
            # Handle any exceptions that occur during report generation
            messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window and pass it to the TestReportGenerator class
if __name__ == "__main__":
    root = tk.Tk()
    app = TestReportGenerator(root)
    root.mainloop()