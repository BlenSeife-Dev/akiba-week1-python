# Task 02 - Student ID Card

# 1.i shall Collect user details
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
department = input("Enter department: ")
year = input("Enter academic year: ")
university = input("Enter university: ")
phone_number = input("Enter phone number: ")            
# 2. Displaying formatted Student ID Card in my box

print("\n+--------------------------------+")
print("|       AKIBA STUDENT CARD       |")
print("+--------------------------------+")
print(f"| Name: {student_name}")
print(f"| ID: {student_id}")
print(f"| Department: {department}")
print(f"| Year: {year}")
print(f"| University: {university}")
print(f"| Phone: {phone_number}")
print("+--------------------------------+")