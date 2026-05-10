'''
CSC 500 - Module 5 - Part 1
Author: Jessica Reyes
Date: 5/6/2026
Description: This program calculates the total and average rainfall over a specified number of years.
'''
# Get the number of years from the user
num_years = int(input("Enter the number of years: "))
# create a dictionary to map month numbers to month names
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",  
    11: "November",
    12: "December"
}
# Initialize total rainfall and calculate the total number of months
rainfall = 0
month = num_years * 12

# Loop through each year and month to get the rainfall input from the user
for year in range(1, num_years + 1):
    for month in range(1, 13):
        inches_rainfall = int(input(f"Enter the total inches of rainfall for {months[month]}: "))
        rainfall += inches_rainfall
average_rainfall = rainfall / (num_years * 12)

# Display the total and average rainfall
print(f"The total rainfall over {month} months is: {rainfall:.0f} inches.")
print(f"The average monthly rainfall over {month} months is: {average_rainfall:.2f} inches.")
