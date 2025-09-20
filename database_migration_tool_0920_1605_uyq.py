# 代码生成时间: 2025-09-20 16:05:57
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil

# 数据库迁移工具类
class DatabaseMigrationTool:
    def __init__(self, master):
        # 初始化主窗口
        self.master = master
        self.master.title('Database Migration Tool')

        # 创建界面元素
        self.create_widgets()

    def create_widgets(self):
        # 选择源数据库文件按钮
        self.source_button = tk.Button(self.master, text='Select Source Database', command=self.select_source_db)
        self.source_button.pack()

        # 选择目标数据库文件按钮
        self.target_button = tk.Button(self.master, text='Select Target Database', command=self.select_target_db)
        self.target_button.pack()

        # 迁移按钮
        self.migrate_button = tk.Button(self.master, text='Migrate', command=self.migrate_database)
        self.migrate_button.pack()

        # 显示状态的标签
        self.status_label = tk.Label(self.master, text='')
        self.status_label.pack()

    def select_source_db(self):
        # 选择源数据库文件
        self.source_db = filedialog.askopenfilename()
        if self.source_db:
            self.status_label.config(text=f'Source Database: {self.source_db}')
        else:
            self.status_label.config(text='No source database selected')

    def select_target_db(self):
        # 选择目标数据库文件
        self.target_db = filedialog.askopenfilename()
        if self.target_db:
            self.status_label.config(text=f'Target Database: {self.target_db}')
        else:
            self.status_label.config(text='No target database selected')

    def migrate_database(self):
        # 检查是否选择了源和目标数据库文件
        if not self.source_db or not self.target_db:
            messagebox.showerror('Error', 'Please select both source and target databases')
            return

        try:
            # 复制源数据库文件到目标位置
            shutil.copy2(self.source_db, self.target_db)
            messagebox.showinfo('Success', 'Database migration completed successfully')
        except Exception as e:
            # 显示错误信息
            messagebox.showerror('Error', f'An error occurred: {e}')

# 主函数
def main():
    # 创建主窗口并运行
    root = tk.Tk()
    app = DatabaseMigrationTool(root)
    root.mainloop()

if __name__ == '__main__':
    main()