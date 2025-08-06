# 代码生成时间: 2025-08-06 17:15:47
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import hashlib
import logging

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileBackupSyncTool:
    def __init__(self, master):
        self.master = master
        self.master.title('文件备份和同步工具')
        self.create_widgets()

    def create_widgets(self):
        # 源文件夹选择按钮
        self.source_button = tk.Button(self.master, text='选择源文件夹', command=self.select_source_folder)
        self.source_button.pack()

        # 目标文件夹选择按钮
        self.target_button = tk.Button(self.master, text='选择目标文件夹', command=self.select_target_folder)
        self.target_button.pack()

        # 备份按钮
        self.backup_button = tk.Button(self.master, text='开始备份', command=self.backup_files)
        self.backup_button.pack()

        # 同步按钮
        self.sync_button = tk.Button(self.master, text='开始同步', command=self.sync_files)
        self.sync_button.pack()

        # 显示源文件夹路径
        self.source_label = tk.Label(self.master, text='源文件夹路径: ')
        self.source_label.pack()
        self.source_folder = ''
        self.source_path_label = tk.Label(self.master, textvariable=tk.StringVar())
        self.source_path_label.pack()

        # 显示目标文件夹路径
        self.target_label = tk.Label(self.master, text='目标文件夹路径: ')
        self.target_label.pack()
        self.target_folder = ''
        self.target_path_label = tk.Label(self.master, textvariable=tk.StringVar())
        self.target_path_label.pack()

    def select_source_folder(self):
        # 选择源文件夹
        self.source_folder = filedialog.askdirectory()
        self.source_path_label['textvariable'] = tk.StringVar(value=self.source_folder)
        self.source_path_label['textvariable'].set(self.source_folder)

    def select_target_folder(self):
        # 选择目标文件夹
        self.target_folder = filedialog.askdirectory()
        self.target_path_label['textvariable'] = tk.StringVar(value=self.target_folder)
        self.target_path_label['textvariable'].set(self.target_folder)

    def backup_files(self):
        # 备份文件
        if not self.source_folder or not self.target_folder:
            messagebox.showerror('错误', '请先选择源文件夹和目标文件夹')
            return
        try:
            for root, dirs, files in os.walk(self.source_folder):
                for file in files:
                    src_file_path = os.path.join(root, file)
                    dst_file_path = os.path.join(self.target_folder, os.path.relpath(src_file_path, self.source_folder))
                    os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                    shutil.copy2(src_file_path, dst_file_path)
            messagebox.showinfo('成功', '备份完成')
        except Exception as e:
            logging.error(f'备份文件时出错: {e}')
            messagebox.showerror('错误', f'备份文件时出错: {e}')

    def sync_files(self):
        # 同步文件
        if not self.source_folder or not self.target_folder:
            messagebox.showerror('错误', '请先选择源文件夹和目标文件夹')
            return
        try:
            source_files = self.get_file_list(self.source_folder)
            target_files = self.get_file_list(self.target_folder)
            for file in source_files:
                if file not in target_files or self.get_file_hash(os.path.join(self.source_folder, file)) != self.get_file_hash(os.path.join(self.target_folder, file)):
                    shutil.copy2(os.path.join(self.source_folder, file), os.path.join(self.target_folder, file))
            for file in target_files:
                if file not in source_files:
                    os.remove(os.path.join(self.target_folder, file))
            messagebox.showinfo('成功', '同步完成')
        except Exception as e:
            logging.error(f'同步文件时出错: {e}')
            messagebox.showerror('错误', f'同步文件时出错: {e}')

    def get_file_list(self, folder):
        # 获取文件夹内所有文件名
        return [os.path.relpath(file, folder) for root, dirs, files in os.walk(folder) for file in files]

    def get_file_hash(self, file_path):
        # 获取文件的MD5哈希值
        with open(file_path, 'rb') as file:
            md5 = hashlib.md5()
            while chunk := file.read(4096):
                md5.update(chunk)
        return md5.hexdigest()

if __name__ == '__main__':
    root = tk.Tk()
    app = FileBackupSyncTool(root)
    root.mainloop()