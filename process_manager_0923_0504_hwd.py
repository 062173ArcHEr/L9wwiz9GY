# 代码生成时间: 2025-09-23 05:04:31
import tkinter as tk
from tkinter import messagebox
import psutil
import os
import sys

"""
Process Manager GUI using Python and Tkinter.
This program allows users to view and terminate system processes.
"""

class ProcessManager:
    def __init__(self, root):
        """ Initialize the Process Manager GUI. """
        self.root = root
        self.root.title('Process Manager')
        self.root.geometry('600x400')

        # Create a frame for the scrollbar and listbox
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Create a vertical scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        # Create a listbox to display processes
        self.process_list = tk.Listbox(self.frame, yscrollcommand=self.scrollbar.set, width=100, height=20)
        self.process_list.pack(side='left', fill='both', expand=True)

        # Configure the scrollbar
        self.scrollbar.config(command=self.process_list.yview)

        # Update the process list
# 优化算法效率
        self.update_process_list()

    def update_process_list(self):
        """ Update the list of processes. """
# NOTE: 重要实现细节
        try:
            # Clear the current list
            self.process_list.delete(0, tk.END)
            
            # Get all running processes
            processes = psutil.process_iter(['pid', 'name', 'status'])
            
            # Iterate through processes and add them to the listbox
            for process in processes:
                try:
# 添加错误处理
                    info = process.info
                    self.process_list.insert(tk.END, f"{info['pid']}: {info['name']} ({info['status']})")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def terminate_process(self, pid):
# 增强安全性
        """ Terminate a process by its PID. """
        try:
            process = psutil.Process(pid)
            process.terminate()
            messagebox.showinfo('Success', 'Process terminated successfully.')
            self.update_process_list()
        except psutil.NoSuchProcess:
            messagebox.showerror('Error', 'Process not found.')
        except psutil.AccessDenied:
# 优化算法效率
            messagebox.showerror('Error', 'Access denied.')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def on_listbox_click(self, event):
        """ Handle listbox click event to terminate a process. """
# 优化算法效率
        try:
            # Get the selected item
            w = event.widget
            index = int(w.curselection()[0])
            pid_name_status = w.get(index)
            
            # Extract the PID from the selected item
            pid = int(pid_name_status.split(':')[0].strip())
            
            # Confirm termination with user
            if messagebox.askokcancel('Terminate Process', f'Are you sure you want to terminate process {pid_name_status}?'):
                self.terminate_process(pid)
        except ValueError:
            messagebox.showerror('Error', 'Invalid selection.')

    def create_menu(self):
        """ Create the menu bar. "