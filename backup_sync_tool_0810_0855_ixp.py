# 代码生成时间: 2025-08-10 08:55:39
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import logging

"""
文件备份和同步工具

这个程序使用Tkinter框架创建一个GUI，允许用户选择源文件夹和目标文件夹，
然后备份和同步源文件夹中的文件到目标文件夹。
"""

class BackupSyncTool:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title("文件备份和同步工具")

        # 设置源文件夹和目标文件夹的标签和输入框
        self.label_source = tk.Label(root, text="源文件夹：")
        self.label_source.pack()
        self.entry_source = tk.Entry(root)
        self.entry_source.pack()
        self.btn_browse_source = tk.Button(root, text="浏览", command=self.browse_source)
        self.btn_browse_source.pack()

        self.label_target = tk.Label(root, text="目标文件夹：")
        self.label_target.pack()
        self.entry_target = tk.Entry(root)
        self.entry_target.pack()
        self.btn_browse_target = tk.Button(root, text="浏览", command=self.browse_target)
        self.btn_browse_target.pack()

        # 设置备份和同步按钮
        self.btn_backup = tk.Button(root, text="备份", command=self.backup)
        self.btn_backup.pack()
        self.btn_sync = tk.Button(root, text="同步", command=self.sync)
        self.btn_sync.pack()

    def browse_source(self):
        """浏览源文件夹"""
        source_dir = filedialog.askdirectory()
        if source_dir:
            self.entry_source.delete(0, tk.END)
            self.entry_source.insert(0, source_dir)

    def browse_target(self):
        """浏览目标文件夹"""
        target_dir = filedialog.askdirectory()
        if target_dir:
            self.entry_target.delete(0, tk.END)
            self.entry_target.insert(0, target_dir)

    def backup(self):
        """备份源文件夹中的文件到目标文件夹"""
        try:
            source_dir = self.entry_source.get()
            target_dir = self.entry_target.get()
            if not source_dir or not target_dir:
                messagebox.showerror("错误", "源文件夹和目标文件夹不能为空")
                return

            # 备份文件
            for filename in os.listdir(source_dir):
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)
                if os.path.isfile(source_file):
                    shutil.copy2(source_file, target_file)
        except Exception as e:
            logging.error(f"备份失败：{e}")
            messagebox.showerror("错误", f"备份失败：{e}")

    def sync(self):
        """同步源文件夹中的文件到目标文件夹"""
        try:
            source_dir = self.entry_source.get()
            target_dir = self.entry_target.get()
            if not source_dir or not target_dir:
                messagebox.showerror("错误", "源文件夹和目标文件夹不能为空")
                return

            # 同步文件
            for filename in os.listdir(source_dir):
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)
                if os.path.isfile(source_file):
                    if not os.path.exists(target_file):
                        shutil.copy2(source_file, target_file)
                    elif os.path.getmtime(source_file) > os.path.getmtime(target_file):
                        shutil.copy2(source_file, target_file)
        except Exception as e:
            logging.error(f"同步失败：{e}")
            messagebox.showerror("错误", f"同步失败：{e}")

def main():
    """程序入口"""
    root = tk.Tk()
    app = BackupSyncTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()