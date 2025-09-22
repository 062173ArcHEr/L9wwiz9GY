# 代码生成时间: 2025-09-22 15:27:23
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import json

# 定义数据备份和恢复类
class DataBackupRestore:
    def __init__(self, master):
        # 初始化窗口
        self.master = master
        master.title("数据备份恢复")
        master.geometry("400x200")

        # 创建按钮
        self.backup_button = tk.Button(master, text="备份数据", command=self.backup_data)
        self.backup_button.pack(pady=10)

        self.restore_button = tk.Button(master, text="恢复数据", command=self.restore_data)
        self.restore_button.pack(pady=10)

    def backup_data(self):
        # 选择备份文件保存路径
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not file_path:
            return

        # 备份数据
        try:
            # 假设数据存储在'data.json'文件中
            data = {"data": "这里是需要备份的数据"}
            with open(file_path, "w") as file:
                json.dump(data, file)
            messagebox.showinfo("成功", "数据备份成功")
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def restore_data(self):
        # 选择备份文件路径
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not file_path:
            return

        # 恢复数据
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                # 假设恢复数据到'data.json'文件中
                with open("data.json", "w") as file:
                    json.dump(data, file)
            messagebox.showinfo("成功", "数据恢复成功")
        except Exception as e:
            messagebox.showerror("错误", str(e))

# 创建主窗口并运行
def main():
    root = tk.Tk()
    app = DataBackupRestore(root)
    root.mainloop()

if __name__ == "__main__":
    main()