# 代码生成时间: 2025-08-29 15:15:23
import tkinter as tk
from tkinter import messagebox

# 缓存策略类
class CachePolicy:
    def __init__(self, capacity):
        """
        初始化缓存策略类
        :param capacity: 缓存容量
        """
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        获取缓存数据
        :param key: 缓存数据的键
        :return: 缓存数据的值，如果没有则返回None
        """
        return self.cache.get(key)

    def put(self, key, value):
        """
        添加或更新缓存数据
        :param key: 缓存数据的键
        :param value: 缓存数据的值
        """
        if len(self.cache) >= self.capacity:
            # 如果缓存已满，移除最旧的数据
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

# 应用程序类
class CachePolicyApp:
    def __init__(self, master):
        """
        初始化应用程序
        :param master: Tkinter主窗口
        """
        self.master = master
        self.master.title('Cache Policy App')
        self.master.geometry('400x300')

        self.cache_policy = CachePolicy(3)  # 缓存容量为3

        # 创建输入框
        self.key_entry = tk.Entry(master)
        self.key_entry.pack(pady=10)

        # 创建值输入框
        self.value_entry = tk.Entry(master)
        self.value_entry.pack(pady=10)

        # 创建获取按钮
        self.get_button = tk.Button(master, text='Get', command=self.get_cache)
        self.get_button.pack(pady=10)

        # 创建设置按钮
        self.put_button = tk.Button(master, text='Put', command=self.put_cache)
        self.put_button.pack(pady=10)

        # 创建显示框
        self.display_label = tk.Label(master, text='')
        self.display_label.pack(pady=10)

    def get_cache(self):
        """
        获取缓存数据
        """
        key = self.key_entry.get()
        value = self.cache_policy.get(key)
        if value is not None:
            self.display_label.config(text=f"Value for key '{key}' is: {value}")
        else:
            self.display_label.config(text=f"No value found for key '{key}'")

    def put_cache(self):
        """
        添加或更新缓存数据
        """
        key = self.key_entry.get()
        value = self.value_entry.get()
        try:
            value = int(value)  # 尝试将值转换为整数
        except ValueError:
            messagebox.showerror('Error', 'Invalid value. Please enter an integer.')
            return

        self.cache_policy.put(key, value)
        self.display_label.config(text=f"Cache updated with key '{key}' and value '{value}'")

# 主函数
def main():
    root = tk.Tk()
    app = CachePolicyApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()