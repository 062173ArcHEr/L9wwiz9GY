# 代码生成时间: 2025-09-10 10:00:31
import tkinter as tk
from tkinter import messagebox
import random
import json

"""
测试数据生成器，使用TKINTER框架创建图形界面，生成随机测试数据。

功能：
- 输入数据项的数量
- 生成随机的测试数据
- 将测试数据保存为JSON文件
"""

class TestDataGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('测试数据生成器')
        self.master.geometry('400x300')

        # 创建输入框和标签
        self.label = tk.Label(master, text='输入数据项的数量：')
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()

        # 创建按钮
        self.generate_button = tk.Button(master, text='生成测试数据', command=self.generate_data)
        self.generate_button.pack()

        # 创建保存按钮
        self.save_button = tk.Button(master, text='保存测试数据', command=self.save_data)
        self.save_button.pack()

    def generate_data(self):
        """生成随机测试数据"""
        try:
            count = int(self.entry.get())
            if count <= 0:
                raise ValueError("数据项数量必须大于0")

            # 生成随机测试数据
            data = []
            for _ in range(count):
                data.append({
                    'id': random.randint(1, 100),
                    'name': f'用户{random.randint(1, 100)}',
                    'age': random.randint(18, 60)
                })

            # 显示测试数据
            messagebox.showinfo('测试数据', json.dumps(data, indent=4, ensure_ascii=False))
        except ValueError as e:
            messagebox.showerror('错误', str(e))

    def save_data(self):
        """保存测试数据为JSON文件"""
        try:
            count = int(self.entry.get())
            if count <= 0:
                raise ValueError("数据项数量必须大于0")

            # 生成随机测试数据
            data = []
            for _ in range(count):
                data.append({
                    'id': random.randint(1, 100),
                    'name': f'用户{random.randint(1, 100)}',
                    'age': random.randint(18, 60)
                })

            # 保存测试数据为JSON文件
            filename = 'test_data.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            messagebox.showinfo('保存成功', f'测试数据已保存到{filename}')
        except ValueError as e:
            messagebox.showerror('错误', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = TestDataGenerator(root)
    root.mainloop()