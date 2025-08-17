# 代码生成时间: 2025-08-17 14:15:46
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileBackupSyncTool:
    def __init__(self, root):
        self.root = root
        self.root.title('File Backup & Sync Tool')
        self.root.geometry('400x200')

        # 创建源文件夹选择按钮
        self.source_button = tk.Button(self.root, text='Select Source Folder', command=self.select_source_folder)
        self.source_button.pack(pady=10)

        # 创建目标文件夹选择按钮
        self.target_button = tk.Button(self.root, text='Select Target Folder', command=self.select_target_folder)
        self.target_button.pack(pady=10)

        # 创建备份和同步按钮
        self.backup_button = tk.Button(self.root, text='Backup and Sync', command=self.backup_and_sync)
        self.backup_button.pack(pady=10)

        # 用于存储源文件夹和目标文件夹的路径
        self.source_folder = ''
        self.target_folder = ''

    def select_source_folder(self):
        "