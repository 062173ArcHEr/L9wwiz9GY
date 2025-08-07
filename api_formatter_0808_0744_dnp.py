# 代码生成时间: 2025-08-08 07:44:41
import tkinter as tk
from tkinter import messagebox
# 扩展功能模块
import json

"""
# TODO: 优化性能
API Response Formatter Tool
This tool provides a GUI to format and prettify API responses.
It takes JSON text as input and displays the formatted JSON.
"""

class APIFormatter:
    """Class responsible for formatting API responses."""
    def __init__(self, master):
        self.master = master
        self.master.title("API Response Formatter")

        # Create input text area
        self.input_text = tk.Text(master, height=15, width=50)
        self.input_text.pack(pady=10)
# FIXME: 处理边界情况

        # Create output text area
        self.output_text = tk.Text(master, height=15, width=50)
        self.output_text.pack(pady=10)

        # Create button to format JSON
        self.format_button = tk.Button(master, text="Format JSON", command=self.format_json)
        self.format_button.pack(pady=5)

    def format_json(self):
        """Formats the JSON input in the input text area."""
        input_text = self.input_text.get("1.0", tk.END)
        try:
            # Attempt to parse JSON and format it
            json_data = json.loads(input_text)
            formatted_json = json.dumps(json_data, indent=4)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", formatted_json)
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            messagebox.showerror("Error", f"Invalid JSON: {e.msg}")

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = APIFormatter(root)
    root.mainloop()

if __name__ == "__main__":
    main()