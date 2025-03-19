import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def get_details(self):
        return f"{self.name}\nPrice: {self.price}\nDeal Price: {self.deal_price}\nYou Save: {self.you_save}\nRatings: {self.ratings}"

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    def get_details(self):
        return super().get_details() + f"\nWarranty: {self.warranty_in_months} months"


class GroceryItem(Product):
    pass


class Order:
    def __init__(self):
        self.items_in_cart = []

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def get_order_details(self):
        details = ""
        for product, quantity in self.items_in_cart:
            details += f"{product.name} - Quantity: {quantity}\n"
        return details

    def calculate_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            total_bill += product.get_deal_price() * quantity
        return total_bill


def main():
    # Initialize products
    laptop = ElectronicItem("Laptop", 80000, 75000, 4.5, 24)
    smartphone = ElectronicItem("Smartphone", 50000, 45000, 4.7, 12)
    rice = GroceryItem("Rice", 1000, 800, 4.2)
    cooking_oil = GroceryItem("Cooking Oil", 1200, 1000, 4.0)

    products = [laptop, smartphone, rice, cooking_oil]

    # Order instance
    order = Order()

    # GUI setup
    root = tk.Tk()
    root.title("Smart Shopping System")
    root.geometry("600x600")
    root.configure(bg="#f5f5f5")

    def display_products():
        product_list.delete(0, tk.END)
        for product in products:
            product_list.insert(tk.END, product.name)

    def show_product_details():
        selected_index = product_list.curselection()
        if selected_index:
            selected_product = products[selected_index[0]]
            product_details.config(state="normal")
            product_details.delete(1.0, tk.END)
            product_details.insert(tk.END, selected_product.get_details())
            product_details.config(state="disabled")
        else:
            messagebox.showwarning("No Selection", "Please select a product to view details.")

    def add_to_cart():
        selected_index = product_list.curselection()
        if selected_index:
            selected_product = products[selected_index[0]]
            quantity = quantity_entry.get()
            if quantity.isdigit() and int(quantity) > 0:
                order.add_item(selected_product, int(quantity))
                messagebox.showinfo("Success", f"Added {quantity} of {selected_product.name} to cart.")
                quantity_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Invalid Input", "Please enter a valid quantity.")
        else:
            messagebox.showwarning("No Selection", "Please select a product to add to cart.")

    def view_cart():
        if order.items_in_cart:
            cart_details = order.get_order_details()
            total_bill = order.calculate_total_bill()
            cart_text.config(state="normal")
            cart_text.delete(1.0, tk.END)
            cart_text.insert(tk.END, cart_details)
            cart_text.insert(tk.END, f"\nTotal Bill: ₹{total_bill}")
            cart_text.config(state="disabled")
        else:
            messagebox.showinfo("Cart Empty", "Your cart is empty.")

    # GUI layout
    tk.Label(root, text="Smart Shopping System", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

    # Product list
    product_frame = tk.Frame(root, bg="#f5f5f5")
    product_frame.pack(pady=10)
    tk.Label(product_frame, text="Available Products", font=("Helvetica", 14), bg="#f5f5f5", fg="#555").pack()
    product_list = tk.Listbox(product_frame, height=8, width=50, font=("Helvetica", 12), bg="#fff", fg="#333", selectbackground="#d1d1d1")
    product_list.pack()
    display_products()

    # Product details
    product_details = tk.Text(root, height=8, width=50, font=("Helvetica", 12), bg="#fff", fg="#333", state="disabled")
    product_details.pack(pady=10)

    # Quantity and add to cart
    quantity_frame = tk.Frame(root, bg="#f5f5f5")
    quantity_frame.pack(pady=5)
    tk.Label(quantity_frame, text="Quantity:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333").pack(side=tk.LEFT)
    quantity_entry = tk.Entry(quantity_frame, font=("Helvetica", 12), bg="#fff", fg="#333")
    quantity_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(quantity_frame, text="Add to Cart", font=("Helvetica", 12), bg="#4CAF50", fg="#fff", command=add_to_cart).pack(side=tk.LEFT, padx=5)

    # View cart button
    tk.Button(root, text="View Cart", font=("Helvetica", 12), bg="#2196F3", fg="#fff", command=view_cart).pack(pady=5)

    # Cart details
    cart_text = tk.Text(root, height=10, width=50, font=("Helvetica", 12), bg="#fff", fg="#333", state="disabled")
    cart_text.pack(pady=10)

    # Show product details button
    tk.Button(root, text="Show Details", font=("Helvetica", 12), bg="#FFC107", fg="#333", command=show_product_details).pack(pady=5)

    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
