'''
CSC 500 - Module 5 - Part 2
Author: Jessica Reyes
Date: 5/6/2026
Description: This program calculates the total number of points awarded by the number of books purchased in one month.
'''

# Get the number of books purchased from the user
books_purchased = int(input("Enter the number of books you purchased this month: "))

# Initialize points variable
points = 0

# Calculate points based on the number of books purchased
if books_purchased >= 0 and books_purchased < 2:
    points = 0
elif books_purchased >= 2 and books_purchased < 4:
    points = 5
elif books_purchased >= 4 and books_purchased < 6:
    points = 15
elif books_purchased >= 6 and books_purchased < 8:
    points = 30
else:
    points = 60

# Display the total points awarded
print(f"Total points awarded: {points}")
