# 代码生成时间: 2025-09-07 22:34:11
import tkinter as tk
from tkinter import messagebox


class ShoppingCartApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Shopping Cart Application")

        # Initialize the shopping cart list
        self.shopping_cart = {}

        # Set up the main window layout
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the product list
        self.product_frame = tk.Frame(self.root)
        self.product_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Create a listbox for displaying products
        self.product_listbox = tk.Listbox(self.product_frame, height=15, width=50)
        self.product_listbox.pack(side=tk.LEFT)

        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.product_frame, command=self.product_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a frame for the cart operations
        self.cart_frame = tk.Frame(self.root)
        self.cart_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Create a listbox for displaying cart items
        self.cart_listbox = tk.Listbox(self.cart_frame, height=10, width=50)
        self.cart_listbox.pack(side=tk.LEFT)

        # Create a button to add items to the cart
        self.add_button = tk.Button(self.cart_frame, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(side=tk.RIGHT)

        # Populate the product list with sample data
        self.populate_product_list()

    def populate_product_list(self):
        # Sample products
        products = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

        # Add products to the listbox
        for product in products:
            self.product_listbox.insert(tk.END, product)

    def add_to_cart(self):
        # Get the selected product from the listbox
        try:
            selected_product = self.product_listbox.get(tk.ANCHOR)
        except tk.TclError:
            messagebox.showerror("Error", "Please select a product to add to the cart.")
            return

        # Add the selected product to the shopping cart
        if selected_product in self.shopping_cart:
            self.shopping_cart[selected_product] += 1
        else:
            self.shopping_cart[selected_product] = 1

        # Update the cart listbox
        self.update_cart_listbox()

        # Display a message indicating the product has been added
        messagebox.showinfo("Added to Cart", f"{selected_product} has been added to your cart.")

    def update_cart_listbox(self):
        # Clear the current cart listbox
        self.cart_listbox.delete(0, tk.END)

        # Populate the cart listbox with the current shopping cart items
        for item, quantity in self.shopping_cart.items():
            self.cart_listbox.insert(tk.END, f"{item} - {quantity} units")

def main():
    # Create the main window
    root = tk.Tk()

    # Create an instance of the ShoppingCartApp class
    app = ShoppingCartApp(root)

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()