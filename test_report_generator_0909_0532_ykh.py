# 代码生成时间: 2025-09-09 05:32:57
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime

"""
A simple Test Report Generator using Python and Tkinter framework.
This script allows the user to input test data, save it, and generate a test report.
"""

class TestReportGenerator:
    def __init__(self, root):
        """
        Initialize the Test Report Generator application.
        :param root: The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Test Report Generator")

        # Define the layout
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets for the Test Report Generator application.
        """
        # Frame for input fields
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Input field for test name
        tk.Label(input_frame, text="Test Name: ").grid(row=0, column=0, padx=10)
        self.test_name_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.test_name_var).grid(row=0, column=1, padx=10)

        # Input field for test date
        tk.Label(input_frame, text="Test Date (YYYY-MM-DD): ").grid(row=1, column=0, padx=10)
        self.test_date_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.test_date_var).grid(row=1, column=1, padx=10)

        # Input field for test result
        tk.Label(input_frame, text="Test Result (Pass/Fail): ").grid(row=2, column=0, padx=10)
        self.test_result_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.test_result_var).grid(row=2, column=1, padx=10)

        # Button to save test data
        tk.Button(self.root, text="Save Test Data", command=self.save_test_data).pack(pady=10)

        # Button to generate test report
        tk.Button(self.root, text="Generate Test Report", command=self.generate_test_report).pack(pady=10)

    def save_test_data(self):
        """
        Save the test data to a file.
        """
        try:
            # Get the test data from the input fields
            test_name = self.test_name_var.get()
            test_date = self.test_date_var.get()
            test_result = self.test_result_var.get()

            # Check if the test data is valid
            if not test_name or not test_date or not test_result:
                messagebox.showerror("Error", "Please enter all test data fields.")
                return

            # Save the test data to a file
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(f"Test Name: {test_name}\
")
                    file.write(f"Test Date: {test_date}\
")
                    file.write(f"Test Result: {test_result}\
")

                messagebox.showinfo("Success", "Test data saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def generate_test_report(self):
        """
        Generate a test report based on the saved test data.
        """
        try:
            # Get the file path of the saved test data
            file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if not file_path:
                messagebox.showerror("Error", "Please select a test data file.")
                return

            # Read the test data from the file
            with open(file_path, "r\) as file:
                test_data = file.readlines()

            # Create the test report
            test_report = "Test Report\
\
"
            for line in test_data:
                test_report += line.strip() + "\
"

            test_report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\
"

            # Save the test report to a file
            report_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if report_file_path:
                with open(report_file_path, "w\) as report_file:
                    report_file.write(test_report)

                messagebox.showinfo("Success", "Test report generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    TestReportGenerator(root)
    root.mainloop()