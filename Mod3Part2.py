"""
CSC 500 - Module 3 - Part 2
Author: Jessica R. Reyes
Date: 25 April 2026
Description: This program calculates the time an alarm will 
go off based on the current time and the number of hours to wait.
"""

currentTime = int(input("Enter the current hour in 24-hour format (0-23): "))
waitHours = int(input("Enter the number of hours to wait for alarm: "))

alarmTime = (currentTime + waitHours) % 24
print(f"The alarm will go off at: {alarmTime}:00")
