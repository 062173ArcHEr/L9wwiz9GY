# 代码生成时间: 2025-09-07 07:48:36
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import os
import datetime

"""
A Python program that creates a simple GUI application for security audit logging using Tkinter.
"""

# Define the main window
class SecurityAuditLogApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Security Audit Log')
        self.root.geometry('600x400')

        # Create a scrolled text widget to display log entries
        self.log_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=15)
        self.log_display.pack(pady=10)

        # Create a frame for input and buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Create an input field for log message
        self.log_entry = tk.Entry(frame, width=50)
        self.log_entry.pack(side=tk.LEFT, padx=5)

        # Create a button to add log entry
        self.add_log_button = tk.Button(frame, text='Add Log', command=self.add_log_entry)
        self.add_log_button.pack(side=tk.LEFT, padx=5)

        # Create a button to clear log
        self.clear_log_button = tk.Button(frame, text='Clear Log', command=self.clear_log)
        self.clear_log_button.pack(side=tk.LEFT, padx=5)

        # Create a button to save log to file
        self.save_log_button = tk.Button(frame, text='Save Log', command=self.save_log_to_file)
        self.save_log_button.pack(side=tk.LEFT, padx=5)

    def add_log_entry(self):
        """
        Add a new log entry to the display.
        """
        try:
            log_message = self.log_entry.get()
            if log_message.strip():
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.log_display.insert(tk.END, f'{timestamp} - {log_message}
')
                self.log_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to add log entry: {e}')

    def clear_log(self):
        """
        Clear all log entries from the display.
        """
        self.log_display.delete(1.0, tk.END)

    def save_log_to_file(self):
        """
        Save the current log to a file.
        """
        try:
            file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')],
                                                     initialdir=os.getcwd(), title='Save Log As')
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.log_display.get(1.0, tk.END))
                messagebox.showinfo('Success', 'Log has been saved successfully.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save log: {e}')

# Create the main window and app
if __name__ == '__main__':
    root = tk.Tk()
    app = SecurityAuditLogApp(root)
    root.mainloop()