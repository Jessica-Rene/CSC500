"""
CSC 500 - Module 8 - Online Shopping Cart
Author: Jessica R. Reyes
Date: 19 May 2026
Description: Shopping cart program with menu system extended.
"""

# Step 1-3: ItemToPurchase class
class ItemToPurchase:
    """Represents an item in the shopping cart."""

    def __init__(self, name="none", price=0,
                 quantity=0, description="none"):

        self.item_name = name
        self.item_price = int(price)
        self.item_quantity = int(quantity)
        self.item_description = description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity

        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

    def get_total_cost(self):
        return self.item_price * self.item_quantity

# Step 4: ShoppingCart class
class ShoppingCart:
    """Represents a shopping cart for a customer."""

    def __init__(self, customer_name="none",
                 current_date="January 1, 2020"):

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):

        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:

                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description

                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price

                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.get_total_cost() for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")

        print()

        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return

        for item in self.cart_items:
            item.print_item_cost()
        print()
        print(f"Total: ${int(self.get_cost_of_cart())}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"\nItem Descriptions")

        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


# Step 5-10: Menu function
def print_menu(cart):
    while True:

        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("\nChoose an option:\n")

        while choice not in ["a", "r", "c", "i", "o", "q"]:
            choice = input("Choose an option:\n")

        # Add item
        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))


            cart.add_item(ItemToPurchase(name, price, quantity, description))

        # Remove item
        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        # Change quantity
        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))

            cart.modify_item(ItemToPurchase(name, 0, quantity))

        # Output descriptions
        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        # Output cart
        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()
        
        # Quit
        elif choice == "q":
            break


# Step 7: main function
def main():

    print("Enter customer's name:")
    customer_name = input()

    print("Enter today's date:")
    current_date = input()

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)

# Run the program
main()
