# 代码生成时间: 2025-09-10 16:07:59
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import logging
from logging.handlers import RotatingFileHandler

# 设置日志记录器
def setup_logger():
    logger = logging.getLogger('SecurityAuditLogger')
    logger.setLevel(logging.INFO)
    # 创建一个handler，用于写入日志文件
    handler = RotatingFileHandler('security_audit.log', maxBytes=2000, backupCount=5)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# GUI主窗口
class SecurityAuditApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Security Audit Log')
        self.logger = setup_logger()
        self.log_area = scrolledtext.ScrolledText(root, state='disabled', height=15, width=80)
        self.log_area.pack(padx=10, pady=10)
        
        self.status_bar = tk.Label(root, text='', bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 按钮
        tk.Button(root, text='Open Log File', command=self.open_log_file).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(root, text='Clear Log Area', command=self.clear_log_area).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(root, text='Log Event', command=self.log_event).pack(side=tk.LEFT, padx=10, pady=10)

    def open_log_file(self):
        """打开日志文件对话框"""
        filepath = filedialog.askopenfilename(title='Open Log File', filetypes=[('Log files', '*.log')], initialdir=os.getcwd())
        if filepath:
            with open(filepath, 'r') as file:
                log_content = file.read()
                self.log_area.config(state='normal')
                self.log_area.delete(1.0, tk.END)
                self.log_area.insert(tk.END, log_content)
                self.log_area.config(state='disabled')
        else:
            self.status_bar.config(text='No file selected')

    def clear_log_area(self):
        """清空日志显示区域"""
        self.log_area.config(state='normal')
        self.log_area.delete(1.0, tk.END)
        self.log_area.config(state='disabled')
        self.status_bar.config(text='Log area cleared')

    def log_event(self):
        """记录日志事件"""
        try:
            log_message = tk.simpledialog.askstring('Input', 'Enter log message:')
            if log_message:
                self.logger.info(log_message)
                self.status_bar.config(text='Logged: {}'.format(log_message))
            else:
                self.status_bar.config(text='No log message entered')
        except Exception as e:
            messagebox.showerror('Error', str(e))
            self.status_bar.config(text='Error logging event')

# 运行GUI应用
if __name__ == '__main__':
    root = tk.Tk()
    app = SecurityAuditApp(root)
    root.mainloop()