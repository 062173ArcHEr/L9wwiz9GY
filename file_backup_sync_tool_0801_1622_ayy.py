# 代码生成时间: 2025-08-01 16:22:57
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import hashlib

"""
文件备份和同步工具
使用TKINTER框架创建图形界面，实现文件备份和同步功能。
"""

class FileBackupSyncTool:
    def __init__(self, root):
        """
        初始化应用
        :param root: 应用的主窗口
        """
        self.root = root
        self.root.title('文件备份和同步工具')
        self.root.geometry('400x200')

        # 创建源文件夹输入框和按钮
        self.source_label = tk.Label(root, text='源文件夹:')
        self.source_label.pack()
        self.source_entry = tk.Entry(root, width=50)
        self.source_entry.pack()
        self.source_button = tk.Button(root, text='浏览', command=self.select_source_folder)
        self.source_button.pack()

        # 创建目标文件夹输入框和按钮
        self.target_label = tk.Label(root, text='目标文件夹:')
        self.target_label.pack()
        self.target_entry = tk.Entry(root, width=50)
        self.target_entry.pack()
        self.target_button = tk.Button(root, text='浏览', command=self.select_target_folder)
        self.target_button.pack()

        # 创建备份和同步按钮
        self.backup_button = tk.Button(root, text='备份', command=self.backup)
        self.backup_button.pack()
        self.sync_button = tk.Button(root, text='同步', command=self.sync)
        self.sync_button.pack()

    def select_source_folder(self):
        """
        选择源文件夹
        """
        source_folder = filedialog.askdirectory()
        if source_folder:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, source_folder)

    def select_target_folder(self):
        """
        选择目标文件夹
        """
        target_folder = filedialog.askdirectory()
        if target_folder:
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, target_folder)

    def backup(self):
        """
        备份文件
        """
        try:
            source_folder = self.source_entry.get()
            target_folder = self.target_entry.get()
            if not source_folder or not target_folder:
                messagebox.showerror('错误', '源文件夹和目标文件夹不能为空')
                return
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    src_file_path = os.path.join(root, file)
                    dst_file_path = os.path.join(target_folder, os.path.relpath(src_file_path, source_folder))
                    if not os.path.exists(os.path.dirname(dst_file_path)):
                        os.makedirs(os.path.dirname(dst_file_path))
                    shutil.copy2(src_file_path, dst_file_path)
            messagebox.showinfo('成功', '文件备份成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def sync(self):
        """
        同步文件
        """
        try:
            source_folder = self.source_entry.get()
            target_folder = self.target_entry.get()
            if not source_folder or not target_folder:
                messagebox.showerror('错误', '源文件夹和目标文件夹不能为空')
                return
            source_files = self.get_files(source_folder)
            target_files = self.get_files(target_folder)
            for file in source_files:
                if file not in target_files:
                    src_file_path = os.path.join(source_folder, file)
                    dst_file_path = os.path.join(target_folder, file)
                    if not os.path.exists(os.path.dirname(dst_file_path)):
                        os.makedirs(os.path.dirname(dst_file_path))
                    shutil.copy2(src_file_path, dst_file_path)
            for file in target_files:
                if file not in source_files:
                    os.remove(os.path.join(target_folder, file))
            messagebox.showinfo('成功', '文件同步成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def get_files(self, folder):
        """
        获取文件夹内所有文件
        :param folder: 文件夹路径
        :return: 文件列表
        """
        files = []
        for root, dirs, file_list in os.walk(folder):
            for file in file_list:
                files.append(os.path.relpath(os.path.join(root, file), folder))
        return files

if __name__ == '__main__':
    root = tk.Tk()
    app = FileBackupSyncTool(root)
    root.mainloop()