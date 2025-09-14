# 代码生成时间: 2025-09-15 06:40:12
import tkinter as tk
from tkinter import messagebox

# 数据库类，用于模拟库存数据存储
class InventoryDatabase:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, quantity):
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity

    def remove_item(self, item_id, quantity):
        if item_id in self.items and self.items[item_id] >= quantity:
            self.items[item_id] -= quantity
            if self.items[item_id] == 0:
                del self.items[item_id]
        else:
            raise ValueError("Insufficient inventory")

    def get_inventory(self):
        return self.items

# 库存管理系统的主窗口类
class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.database = InventoryDatabase()
        self.create_widgets()

    def create_widgets(self):
        # 输入框
        self.item_id_label = tk.Label(self.root, text="Item ID: ")
        self.item_id_label.pack()
        self.item_id_entry = tk.Entry(self.root)
        self.item_id_entry.pack()

        self.quantity_label = tk.Label(self.root, text="Quantity: ")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        # 添加库存按钮
        self.add_button = tk.Button(self.root, text="Add Inventory", command=self.add_inventory)
        self.add_button.pack()

        # 移除库存按钮
        self.remove_button = tk.Button(self.root, text="Remove Inventory", command=self.remove_inventory)
        self.remove_button.pack()

        # 显示库存按钮
        self.display_button = tk.Button(self.root, text="Display Inventory", command=self.display_inventory)
        self.display_button.pack()

    def add_inventory(self):
        item_id = self.item_id_entry.get()
        quantity = self.quantity_entry.get()
        try:
            quantity = int(quantity)
            self.database.add_item(item_id, quantity)
            messagebox.showinfo("Success", "Inventory added successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity")

    def remove_inventory(self):
        item_id = self.item_id_entry.get()
        quantity = self.quantity_entry.get()
        try:
            quantity = int(quantity)
            self.database.remove_item(item_id, quantity)
            messagebox.showinfo("Success", "Inventory removed successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity")
        except KeyError:
            messagebox.showerror("Error", "Item not found")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_inventory(self):
        inventory = self.database.get_inventory()
        if inventory:
            messagebox.showinfo("Inventory", str(inventory))
        else:
            messagebox.showinfo("Inventory", "No items in inventory")

# 主函数
def main():
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()