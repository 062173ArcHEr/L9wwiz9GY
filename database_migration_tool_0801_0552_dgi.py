# 代码生成时间: 2025-08-01 05:52:10
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sqlite3
import shutil

"""
数据库迁移工具使用TKINTER框架创建GUI界面，
允许用户选择源数据库文件和目标数据库文件，
并执行数据库迁移操作。"""

class DatabaseMigrationTool:
    def __init__(self, root):
        """初始化GUI界面"""
        self.root = root
        self.root.title("数据库迁移工具")

        # 设置窗口大小
        self.root.geometry("400x200")

        # 创建标签和输入框
        self.label_source = tk.Label(self.root, text="源数据库文件：")
        self.label_source.grid(row=0, column=0)
        self.entry_source = tk.Entry(self.root, width=40)
        self.entry_source.grid(row=0, column=1)
        self.btn_source = tk.Button(self.root, text="浏览", command=self.browse_source)
        self.btn_source.grid(row=0, column=2)

        self.label_target = tk.Label(self.root, text="目标数据库文件：")
        self.label_target.grid(row=1, column=0)
        self.entry_target = tk.Entry(self.root, width=40)
        self.entry_target.grid(row=1, column=1)
        self.btn_target = tk.Button(self.root, text="浏览", command=self.browse_target)
        self.btn_target.grid(row=1, column=2)

        self.btn_migrate = tk.Button(self.root, text="迁移", command=self.migrate)
        self.btn_migrate.grid(row=2, column=1)

    def browse_source(self):
        """浏览源数据库文件"""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.entry_source.delete(0, tk.END)
            self.entry_source.insert(0, file_path)

    def browse_target(self):
        """浏览目标数据库文件"""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.entry_target.delete(0, tk.END)
            self.entry_target.insert(0, file_path)

    def migrate(self):
        """执行数据库迁移操作"""
        source_path = self.entry_source.get()
        target_path = self.entry_target.get()

        if not source_path or not target_path:
            messagebox.showwarning("警告", "请选择源数据库文件和目标数据库文件！")
            return

        try:
            # 复制源数据库文件到目标路径
            shutil.copy2(source_path, target_path)
            messagebox.showinfo("成功", "数据库迁移成功！")
        except Exception as e:
            messagebox.showerror("错误", str(e))


def main():
    """主函数"""
    root = tk.Tk()
    app = DatabaseMigrationTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()