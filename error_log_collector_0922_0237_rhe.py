# 代码生成时间: 2025-09-22 02:37:48
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime

"""
# FIXME: 处理边界情况
Error Log Collector is a simple GUI application that allows users to select a file or directory,
and it will collect any error messages from the selected file(s) and save them into a log file.
"""

class ErrorLogCollector:
    def __init__(self, master):
        self.master = master
# 增强安全性
        master.title("Error Log Collector")
# 添加错误处理

        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Select a file or directory: ")
        self.label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=(0, 10))

        self.browse_button = tk.Button(self.frame, text="Browse", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.frame, text="Collect Errors", command=self.collect_errors)
        self.start_button.pack(side=tk.LEFT)

        self.status_label = tk.Label(self.frame, text="")
        self.status_label.pack(side=tk.LEFT)

    def browse_file(self):
        """Open a file dialog for the user to select a file or directory."""
        path = filedialog.askopenfilename(title="Select a file or directory")
# 添加错误处理
        if path:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, path)

    def collect_errors(self):
        """Collect error messages from the selected file and save them to a log file."""
        path = self.entry.get()
# 添加错误处理
        if not path:
            messagebox.showerror("Error", "Please select a file or directory first.")
            return

        try:
            if os.path.isfile(path):
                self.process_file(path)
            else:
                self.process_directory(path)

            log_file_path = self.create_log_file()
            messagebox.showinfo("Success", f"Error log saved to: {log_file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def process_file(self, file_path):
        """Read a file and collect error messages.""
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line:  # Assuming error messages contain the word 'ERROR'
                    self.write_to_log(line)
# 增强安全性

    def process_directory(self, directory_path):
        """Recursively process all files in a directory.""
# 改进用户体验
        for root, dirs, files in os.walk(directory_path):
# TODO: 优化性能
            for file in files:
# 优化算法效率
                file_path = os.path.join(root, file)
                self.process_file(file_path)

    def write_to_log(self, error_message):
        """Write an error message to the log file.""
        with open("error_log.txt", "a") as log_file:
            log_file.write(error_message)

    def create_log_file(self):
        """Create a log file with a timestamp.""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file_name = f"error_log_{timestamp}.txt"
        os.rename("error_log.txt", log_file_name)
        return log_file_name

if __name__ == "__main__":
# 添加错误处理
    root = tk.Tk()
    app = ErrorLogCollector(root)
    root.mainloop()