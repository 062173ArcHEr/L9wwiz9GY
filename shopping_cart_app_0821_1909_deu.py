# 代码生成时间: 2025-08-21 19:09:41
import tkinter as tk
from tkinter import messagebox

"""
Shopping Cart Application using Python and Tkinter.
This application allows users to add items to a cart,
view the cart contents, and remove items from the cart.
"""

class ShoppingCart:
    """
    The ShoppingCart class represents a shopping cart with items.
    It provides methods to add items, remove items, and get the total price.
    """
    def __init__(self):
        self.items = []
        self.item_count = 0

    def add_item(self, item, price):
        """
        Add an item to the cart with its price.
        """
        self.items.append((item, price))
        self.item_count += 1

    def remove_item(self, item):
        """
        Remove an item from the cart.
        """
        try:
            self.items.remove((item, self.get_price(item)))
            self.item_count -= 1
        except ValueError:
            messagebox.showerror("Error", f"Item '{item}' not found in the cart.")

    def get_price(self, item):
        """
        Get the price of an item.
        """
        for i, p in self.items:
            if i == item:
                return p
        return None

    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        total = sum(p for i, p in self.items)
        return total

    def get_cart_items(self):
        """
        Get a list of all items in the cart.
        """
        return [item for item, _ in self.items]

class ShoppingCartApp:
    """
    The ShoppingCartApp class creates a GUI application for the shopping cart.
    It provides methods to interact with the ShoppingCart class through the GUI.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Shopping Cart App")
        self.cart = ShoppingCart()
        self.create_widgets()

    def create_widgets(self):
        # Create the frame for the cart
        self.cart_frame = tk.Frame(self.master)
        self.cart_frame.pack(padx=10, pady=10)

        # Create the listbox to display cart items
        self.cart_listbox = tk.Listbox(self.cart_frame)
        self.cart_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the buttons to add and remove items
        self.add_button = tk.Button(self.cart_frame, text="Add Item", command=self.add_item_dialog)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.cart_frame, text="Remove Item", command=self.remove_item_dialog)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        # Create the label to display the total price
        self.total_label = tk.Label(self.cart_frame, text="Total Price: $0.00")
        self.total_label.pack(side=tk.LEFT, padx=10)

    def add_item_dialog(self):
        """
        Open a dialog to add a new item to the cart.
        """
        def add_item(item, price):
            self.cart.add_item(item, price)
            self.update_cart_listbox()
            self.update_total_price()
            item_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            add_item_window.destroy()

        add_item_window = tk.Toplevel(self.master)
        add_item_window.title("Add Item")

        tk.Label(add_item_window, text="Item Name:").pack(pady=5)
        item_entry = tk.Entry(add_item_window)
        item_entry.pack(pady=5)

        tk.Label(add_item_window, text="Price ($):").pack(pady=5)
        price_entry = tk.Entry(add_item_window)
        price_entry.pack(pady=5)

        add_button = tk.Button(add_item_window, text="Add Item", command=lambda: add_item(item_entry.get(), price_entry.get()))
        add_button.pack(pady=10)

    def remove_item_dialog(self):
        """
        Open a dialog to remove an existing item from the cart.
        """
        def remove_item():
            item = item_listbox.get(tk.ACTIVE)
            if item:
                self.cart.remove_item(item)
                self.update_cart_listbox()
                self.update_total_price()
            item_listbox_window.destroy()

        if self.cart.get_cart_items():
            item_listbox_window = tk.Toplevel(self.master)
            item_listbox_window.title("Remove Item")

            item_listbox = tk.Listbox(item_listbox_window)
            item_listbox.pack(pady=5)
            for item in self.cart.get_cart_items():
                item_listbox.insert(tk.END, item)

            remove_button = tk.Button(item_listbox_window, text="Remove Item", command=remove_item)
            remove_button.pack(pady=10)
        else:
            messagebox.showwarning("Warning", "Cart is empty.")

    def update_cart_listbox(self):
        """
        Update the cart listbox with the current cart items.
        """
        self.cart_listbox.delete(0, tk.END)
        for item in self.cart.get_cart_items():
            self.cart_listbox.insert(tk.END, item)

    def update_total_price(self):
        """
        Update the total price label with the current total price.
        """
        total_price = self.cart.get_total_price()
        self.total_label.config(text=f"Total Price: ${total_price:.2f}")

def main():
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()