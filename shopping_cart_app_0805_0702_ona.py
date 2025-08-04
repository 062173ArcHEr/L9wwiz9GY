# 代码生成时间: 2025-08-05 07:02:50
import tkinter as tk
from tkinter import messagebox

"""
购物车程序实现
使用Python和Tkinter框架创建GUI界面
"""

# 商品列表
PRODUCTS = [
    {'name': '苹果', 'price': 3.5},
    {'name': '香蕉', 'price': 2.0},
    {'name': '橙子', 'price': 4.0},
    {'name': '梨', 'price': 2.5},
]

class ShoppingCartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('购物车')
        self.geometry('400x300')

        self.cart = []  # 购物车列表

        # 创建商品列表界面
        self.create_product_list()

        # 创建按钮
        self.add_button = tk.Button(self, text='添加到购物车', command=self.add_to_cart)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(self, text='清空购物车', command=self.clear_cart)
        self.clear_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # 创建显示购物车信息的标签
        self.cart_label = tk.Label(self, text='购物车: 空')
        self.cart_label.pack(side=tk.BOTTOM, padx=10, pady=10)

    def create_product_list(self):
        """创建商品列表界面"""
        self.product_list = tk.Listbox(self)
        self.product_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for product in PRODUCTS:
            self.product_list.insert(tk.END, f"{product['name']} - ￥{product['price']:.2f}")

    def add_to_cart(self):
        """将选中的商品添加到购物车"""
        try:
            selected_product = self.product_list.get(self.product_list.curselection())
            product_info = selected_product.split(' - ')[0]
            if product_info not in [p['name'] for p in self.cart]:
                self.cart.append({'name': product_info, 'price': PRODUCTS[PRODUCTS.index(next((p for p in PRODUCTS if p['name'] == product_info), None))]['price']})
                self.update_cart_label()
            else:
                messagebox.showwarning('警告', '该商品已在购物车中')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def clear_cart(self):
        """清空购物车"""
        self.cart = []
        self.update_cart_label()

    def update_cart_label(self):
        """更新购物车标签显示"""
        if self.cart:
            total_price = sum(item['price'] for item in self.cart)
            self.cart_label.config(text=f'购物车: {len(self.cart)} 件商品 - 总计: ￥{total_price:.2f}')
        else:
            self.cart_label.config(text='购物车: 空')

if __name__ == '__main__':
    app = ShoppingCartApp()
    app.mainloop()