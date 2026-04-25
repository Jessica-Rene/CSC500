"""
Author: Jessica R. Reyes
Date: 25 April 2026
Description: This program calculates the 
tip, sales tax, and total amount 
for a meal based on the charge for the food.
"""

mealCost = int(input("Enter the charge for the food: $"))
tip = mealCost * 0.18
salesTax = mealCost * 0.07
total = mealCost + tip + salesTax

print(f'Tip amount: ${tip:.2f}')
print(f'Sales tax: ${salesTax:.2f}')
print(f'Total amount: ${total:.2f}')
