# 代码生成时间: 2025-09-06 02:17:03
import tkinter as tk
from tkinter import messagebox
import sqlite3

"""
库存管理系统
"""

class InventoryManagement:
    def __init__(self, root):
        # 初始化数据库连接
        self.conn = sqlite3.connect('inventory.db')
        self.cursor = self.conn.cursor()
        # 创建库存表
        self.create_table()
        # 设置主窗口
        self.root = root
        self.root.title('库存管理系统')
        # 创建UI组件
        self.create_widgets()

    def create_table(self):
        """创建库存表"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             quantity INTEGER NOT NULL)''')
        self.conn.commit()

    def create_widgets(self):
        """创建UI组件"""
        self.name_label = tk.Label(self.root, text='商品名称：')
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        self.quantity_label = tk.Label(self.root, text='库存数量：')
        self.quantity_label.grid(row=1, column=0)
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.root, text='添加库存', command=self.add_inventory)
        self.add_button.grid(row=2, column=0, columnspan=2)

    def add_inventory(self):
        """添加库存"""
        try:
            name = self.name_entry.get()
            quantity = int(self.quantity_entry.get())
            if name and quantity > 0:
                self.cursor.execute('''INSERT INTO inventory (name, quantity) VALUES (?, ?)''', (name, quantity))
                self.conn.commit()
                messagebox.showinfo('成功', '库存添加成功')
            else:
                messagebox.showerror('错误', '商品名称和数量不能为空或负数')
        except ValueError:
            messagebox.showerror('错误', '库存数量必须是整数')
        finally:
            self.name_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)

    def run(self):
        "