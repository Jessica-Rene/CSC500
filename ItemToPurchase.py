"""
CSC 500 - Module 3 - Online Shopping Cart
Author: Jessica R. Reyes
Date: 2 May 2026
Description: This program calculates the total cost of items the user enters.
"""

# Step 1: Create ItemToPurchase class
class ItemToPurchase:
    """Represents an item in the shopping cart."""

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        """Print the item cost."""
        total_cost = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} "
            f"@ ${self.item_price:.0f} = ${total_cost:.0f}"
        )

    def get_total_cost(self):
        """Return the total cost of the item."""
        return self.item_price * self.item_quantity


# Step 2: Input for item 1
print("Item 1")
item1 = ItemToPurchase()

item1.item_name = input("Enter the item name:\n")
item1.item_price = float(input("Enter the item price:\n"))
item1.item_quantity = int(input("Enter the item quantity:\n"))

# Input for item 2
print("\nItem 2")
item2 = ItemToPurchase()

item2.item_name = input("Enter the item name:\n")
item2.item_price = float(input("Enter the item price:\n"))
item2.item_quantity = int(input("Enter the item quantity:\n"))

# Step 3: Output total cost
print("\nTOTAL COST")

item1.print_item_cost()
item2.print_item_cost()

total_cost = item1.get_total_cost() + item2.get_total_cost()
print(f"\nTotal: ${total_cost:.0f}")
