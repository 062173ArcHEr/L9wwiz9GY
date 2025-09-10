# 代码生成时间: 2025-09-11 07:09:30
import tkinter as tk
from tkinter import messagebox

# 数据模型类
class DataModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        """添加数据到模型中"""
        if item not in self.data:
            self.data.append(item)
            return True
        else:
            return False

    def remove_data(self, item):
        """从模型中移除数据"""
        if item in self.data:
            self.data.remove(item)
            return True
        else:
            return False

    def get_data(self):
        """获取模型中的所有数据"""
        return self.data.copy()

# 应用程序类
class DataModelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data Model Application')
        self.geometry('300x200')
        self.model = DataModel()  # 初始化数据模型

        self.create_widgets()

    def create_widgets(self):
        # 创建输入框
        self.entry_label = tk.Label(self, text='Enter data item:')
        self.entry_label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()

        # 创建添加按钮
        self.add_button = tk.Button(self, text='Add', command=self.add_data)
        self.add_button.pack()

        # 创建显示数据的标签
        self.data_label = tk.Label(self, text='')
        self.data_label.pack()

    def add_data(self):
        # 添加数据到模型并更新界面
        item = self.entry.get()
        if item:
            if self.model.add_data(item):
                messagebox.showinfo('Success', 'Data added successfully')
                self.update_display()
            else:
                messagebox.showerror('Error', 'Data already exists')
        else:
            messagebox.showerror('Error', 'Enter a valid data item')

    def update_display(self):
        # 更新显示数据的标签
        data = self.model.get_data()
        self.data_label.config(text=str(data))

# 主函数
def main():
    app = DataModelApp()
    app.mainloop()

if __name__ == '__main__':
    main()