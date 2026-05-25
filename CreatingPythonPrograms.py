"""
CSC 500 - Module 7 - Creating Python Programs
Author: Jessica R. Reyes
Date: 25 May 2026
Description: This program creates a dictionary containing course 
numbers and the room numbers where the courses are held. The program 
then prompts the user to enter a course number and displays the corresponding 
room number. | Another dictionary containing course numbers and the names of the 
instructors is also created. | Finally, an additional dictionary containing course 
numbers and the meeting times of each course. 
"""

# Create a dictionary for course numbers and room numbers
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}  
# Create a dictionary for course numbers and instructor names
course_instructors = { 
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
# Create a dictionary for course numbers and meeting times
course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}
# Prompt the user to enter a course number
course_number = input("Enter a course number (e.g., CSC101): ")
# Display the corresponding room number, instructor name, and meeting time
if course_number in course_rooms:
    print(f"Room Number: {course_rooms[course_number]}")
    print(f"Instructor: {course_instructors[course_number]}")
    print(f"Meeting Time: {course_times[course_number]}")
else:
    print("Course number not found.")
    