# 代码生成时间: 2025-08-15 09:18:20
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

"""
配置文件管理器
"""

class ConfigManager:
    def __init__(self, root):
        """
        构造函数
        :param root: Tkinter窗口对象
        """
        self.root = root
        self.root.title('配置文件管理器')
        self.root.geometry('400x300')

        # 创建菜单栏
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # 创建文件菜单
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='文件', menu=file_menu)
        file_menu.add_command(label='打开', command=self.open_config)
        file_menu.add_command(label='保存', command=self.save_config)
        file_menu.add_separator()
        file_menu.add_command(label='退出', command=self.root.quit)

        # 创建文本框
        self.text = tk.Text(self.root)
        self.text.pack(expand=True, fill='both')

    def open_config(self):
        """
        打开配置文件
        """
        file_path = filedialog.askopenfilename(title='打开配置文件', filetypes=[('配置文件', '*.json'), ('所有文件', '*.*')])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror('打开失败', str(e))

    def save_config(self):
        """
        保存配置文件
        """
        file_path = filedialog.asksaveasfilename(title='保存配置文件', filetypes=[('配置文件', '*.json'), ('所有文件', '*.*')])
        if file_path:
            try:
                content = self.text.get(1.0, tk.END)
                with open(file_path, 'w') as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror('保存失败', str(e))


def main():
    """
    主函数
    """
    root = tk.Tk()
    app = ConfigManager(root)
    root.mainloop()

if __name__ == '__main__':
    main()