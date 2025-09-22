# 代码生成时间: 2025-09-23 00:31:48
import tkinter as tk
from tkinter import messagebox


# 购物车类，用于存储和管理购物车中的商品
class ShoppingCart:
    def __init__(self):
        self.items = []  # 存储购物车中的商品列表
# FIXME: 处理边界情况

    def add_item(self, item):
# FIXME: 处理边界情况
        """向购物车中添加商品"""
        if item not in self.items:
# TODO: 优化性能
            self.items.append(item)
        else:
            messagebox.showerror("添加失败", "商品已存在于购物车中")

    def remove_item(self, item):
        """从购物车中移除商品"""
        try:
            self.items.remove(item)
        except ValueError:
            messagebox.showerror("移除失败", "商品不存在于购物车中")

    def get_items(self):
        """返回购物车中所有商品的列表"""
        return self.items


# 商品类，用于表示购物车中的商品
class Product:
    def __init__(self, name, price):
        self.name = name  # 商品名称
        self.price = price  # 商品价格

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


# 主窗口类，用于创建和管理购物车应用的界面
class ShoppingCartApp:
    def __init__(self, master):
        self.master = master
        self.master.title("购物车应用")
        self.cart = ShoppingCart()  # 创建购物车实例

        # 创建产品名称和价格输入框
        self.name_label = tk.Label(self.master, text="商品名称：")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        self.price_label = tk.Label(self.master, text="商品价格：")
        self.price_label.grid(row=1, column=0)
        self.price_entry = tk.Entry(self.master)
        self.price_entry.grid(row=1, column=1)

        # 创建添加商品按钮
        self.add_button = tk.Button(self.master, text="添加商品", command=self.add_product)
        self.add_button.grid(row=2, column=0, columnspan=2)

        # 创建清空购物车按钮
        self.clear_button = tk.Button(self.master, text="清空购物车", command=self.clear_cart)
# FIXME: 处理边界情况
        self.clear_button.grid(row=3, column=0, columnspan=2)

        # 创建显示购物车内容的文本框
        self.cart_text = tk.Text(self.master, height=10, width=30)
        self.cart_text.grid(row=4, column=0, columnspan=2)

    def add_product(self):
        """添加商品到购物车"""
        name = self.name_entry.get()
        price = self.price_entry.get()

        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("输入错误", "价格必须为数字")
            return

        product = Product(name, price)
        self.cart.add_item(product)
        self.update_cart_display()

    def clear_cart(self):
        """清空购物车"""
        self.cart.items.clear()
        self.update_cart_display()

    def update_cart_display(self):
        """更新购物车内容的显示"